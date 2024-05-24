///bin/sh -c "${CC} -std:c++20 -O2 -o ${0%.cpp}.exe ${0} -march=native" ; exit
#include <algorithm>
#include <array>
#include <cctype>
#include <corecrt_wstdio.h>
#include <iomanip>
#include <charconv>
#include <filesystem>
#include <stdio.h>
#include <string.h>
#include <string>
#include <string_view>
#include <iostream>
#include <fstream>
#include <span>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

[[noreturn]] static void raise_error(std::string str) {
    fprintf(stderr, "Failed: %s\n", str.c_str());
    exit(-1);
}

static constexpr std::string_view ALPHABET =  "_ABCDEFGHIJKLMNOPQRSTUVWXYZ";

using path = std::filesystem::path;
using HashSet = std::unordered_set<std::uint32_t>;
using HashDict = std::unordered_set<std::u8string>;
using WordList = std::vector<std::u8string>;
using SentenceList = std::vector<WordList>;

constexpr auto fnv1a(std::u8string_view data, std::uint32_t h = 0x811c9dc5u) -> std::uint32_t {
    for (auto const& c: data) {
        h ^= c >= 'A' && c <= 'Z' ? ((c -'A') + 'a') : c;
        h *= 0x01000193u;
    }
    return h;
}

auto read_HashSet(path const& source) -> HashSet {
    auto results = std::unordered_set<std::uint32_t>{};
    auto file = std::ifstream{source};
    if (!file) {
        raise_error("Failed to read hash set: " + source.generic_string());
    }
    for (auto line = std::string{}; std::getline(file, line); line.clear()) {
        if (line.size() < 8)
            continue;
        auto hash = std::uint32_t{};
        auto ec_ptr = std::from_chars(line.data(), line.data() + 8, hash, 16);
        if (ec_ptr.ec != std::errc{} || ec_ptr.ptr != line.data() + 8 || !hash) {
            continue;
        }
        results.insert(hash);
    }
    return results;
}

auto read_Bad(path const& source) -> HashDict {
    HashDict results;
    for (auto const& entry: std::filesystem::directory_iterator(source)) {
        if (!entry.is_regular_file()) {
            continue;
        }
        auto const source = entry.path();
        auto file = std::ifstream{source};
        if (!file) {
            raise_error("Failed to read bad list: " + source.generic_string());
        }
        for (auto line = std::string{}; std::getline(file, line); line.clear()) {
            if (line.size() < 8)
                continue;
            auto hash = std::uint32_t{};
            auto ec_ptr = std::from_chars(&line[0], &line[8], hash, 16);
            if (ec_ptr.ec != std::errc{} || ec_ptr.ptr != &line[8] || !hash) {
                continue;
            }
            auto str = std::string_view(line).substr(8);
            while (!str.empty() && std::isspace(str.front())) {
                str.remove_prefix(1);
            }
            while (!str.empty() && std::isspace(str.back())) {
                str.remove_suffix(1);
            }
            if (str.empty()) {
                continue;
            }
            results.insert(std::u8string{str.begin(), str.end()});
        }
    }
    return results;
}

auto read_WordList(path const& source) -> WordList {
    auto results = std::vector<std::u8string>{};
    auto file = std::ifstream{source};
    if (!file) {
        raise_error("Failed to read word list: " + source.generic_string());
    }
    for (auto line = std::string{}; std::getline(file, line) && !line.empty(); line.clear()) {
        results.emplace_back(line.begin(), line.end());
    }
    return results;
}

auto read_SentenceList(path const& source) -> SentenceList {
    auto results = std::vector<std::vector<std::u8string>>{};
    auto file = std::ifstream{source};
    if (!file) {
        raise_error("Failed to read sentence list: " + source.generic_string());
    }
    for (auto line = std::string{}; std::getline(file, line) && line.size() >= 8; line.clear()) {
        auto hash = std::uint32_t{};
        auto ec_ptr = std::from_chars(&line[0], &line[8], hash, 16);
        if (ec_ptr.ec != std::errc{} || ec_ptr.ptr != &line[8] || !hash) {
            continue;
        }
        auto str = std::string_view(line).substr(8);
        while (!str.empty() && std::isspace(str.front())) {
            str.remove_prefix(1);
        }
        while (!str.empty() && std::isspace(str.back())) {
            str.remove_suffix(1);
        }
        if (str.empty()) {
            continue;
        }
        auto words = WordList{};
        auto i = str.begin();
        do {
            auto start = i++;
            i = std::find_first_of(i, str.end(), ALPHABET.begin(), ALPHABET.end());
            words.push_back(std::u8string{start, i});
        } while(i != str.end());
        results.push_back(std::move(words));
    }
    return results;
}


auto read_SentenceList2(path const& source1, path const& source2) -> SentenceList {
    auto result1 = read_SentenceList(source1);
    auto result2 = read_SentenceList(source2);
    result1.insert(result1.end(), result2.cbegin(), result2.cend());
    return result1;
}

struct Prefix {
    std::u8string_view prefix;
    std::uint32_t hash;
    Prefix(char8_t const* prefix = u8"") : prefix(prefix), hash(fnv1a(prefix)) {}
};

template <std::size_t S>
struct PrefixList {
    Prefix list[S];
};
template <typename...args>
PrefixList(args...) -> PrefixList<sizeof...(args)>;

template <std::size_t S>
struct Guesser {
    HashSet all;
    HashSet known;

    HashDict bad;

    SentenceList sentences;
    WordList words;
    PrefixList<S> prefixes;
    HashDict found;

    struct Stack {
        HashSet const& all;
        HashSet const& known;
        HashDict const& bad;
        HashDict& found;
        PrefixList<S> prefixes;
        std::vector<std::u8string_view> stack = {};

        void guess_word(std::u8string_view word, bool show = true) {
            stack.push_back(word);
            for (auto& [prefix, h]: prefixes.list) {
                h = fnv1a(word, h);
                if (show && all.contains(h) && !known.contains(h)) {
                    auto name = std::u8string(prefix);
                    for (auto const& w: stack) {
                        name += w;
                    }
                    if (!bad.contains(name) && !found.contains(name)) {
                        printf("%08X %s\n", fnv1a(name), (char const*)name.c_str());
                        found.insert(name);
                    }
                }
            }
        }

        void guess_span(std::span<std::u8string const> words) {
            for (auto const& word: words) {
                guess_word(word);
            }
        }
    };

    void run_force(Stack const& stack, int count, int countEnd) {
        if (count >= countEnd) {
            return;
        }
        for (auto const& word: words) {
            auto stack_copy = stack;
            stack_copy.guess_word(word);
            run_force(stack_copy, count + 1, countEnd);
        }
    }

    void run(int mode) {
        if (mode > 0) {
            run_force({all, known, bad, found, prefixes}, 0, mode);
            return;
        }
        for (auto const& word: words) {
            for (auto const& sentence: sentences) {
                for (auto i = std::size_t{0}; i != sentence.size(); ++i) {
                    auto stack0 = Stack { all, known, bad, found, prefixes };
                    bool mutated0 = false;
                    auto stack1 = Stack { all, known, bad, found, prefixes };
                    bool mutated1 = false;
                    auto stack2 = Stack { all, known, bad, found, prefixes };
                    bool mutated2 = false;
                    auto stack3 = Stack { all, known, bad, found, prefixes };
                    bool mutated3 = false;
                    for (auto c = std::size_t{0}; c != sentence.size(); ++c) {
                        if (i == c) {
                            mutated0 = true;
                            mutated1 = true;
                            stack1.guess_word(word, mutated0);
                        } else {
                            stack0.guess_word(sentence[c], mutated1);
                            stack1.guess_word(sentence[c], mutated1);
                        }

                        if (i == c) {
                            mutated2 = true;
                            stack2.guess_word(word, mutated2);
                        }
                        stack2.guess_word(sentence[c], mutated2);

                        stack3.guess_word(sentence[c], mutated3);
                        if (i == c) {
                            mutated3 = true;
                            stack3.guess_word(word, mutated3);
                        }
                    }
                }
            }
        }
    }

    void print() {
        for (auto const& f: found) {
            if (bad.contains(f)) {
                continue;
            }
            printf("%08X %s\n", fnv1a(f), (char const*)f.c_str());
        }
    }
};
template <size_t S>
Guesser(auto, auto, auto, auto, auto, PrefixList<S>) -> Guesser<S>;

void guess_fields(path const& words, int mode) {
    auto guesser = Guesser {
        read_HashSet("all/all.binfields.txt"),
        read_HashSet("hashes/hashes.binfields.txt"),
        read_Bad("hashes_bad"),
        read_SentenceList2("hashes/hashes.bintypes.txt", "hashes/hashes.binfields.txt"),
        read_WordList(words),
        PrefixList {  u8"", /*u8"m", u8"b", u8"ar", u8"m_",*/ }
    };
    guesser.run(mode);
}

void guess_types(path const& words, int mode) {
    auto guesser = Guesser {
        read_HashSet("all/all.bintypes.txt"),
        read_HashSet("hashes/hashes.bintypes.txt"),
        read_Bad("hashes_bad"),
        read_SentenceList2("hashes/hashes.bintypes.txt", "hashes/hashes.binfields.txt"),
        read_WordList(words),
        PrefixList {  u8"", u8"I" }
    };
    guesser.run(mode);
}

int main(int argc, char** argv) {
    {
        if (argc != 4) {
            raise_error("hashguesser types/fields wordlist.txt isreplace(0/1)");
        }
        auto guesser = std::string_view{argv[1]};
        auto word_list = argv[2];
        auto replace = atoi(argv[3]);
        if (guesser == "types") {
            guess_types(word_list, replace);
        } else if (guesser == "fields") {
            guess_fields(word_list, replace);
        } else {
            raise_error("Unknown guesser!");
        }
        return EXIT_SUCCESS;
    }
    return 0;
}
