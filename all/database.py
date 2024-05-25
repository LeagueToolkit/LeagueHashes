#!python
class StringDefaultTableGet(IStringGet):
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Table: (Pointer, 0x0, 0x0, RsTable)
    Var: (String, 0x0, 0x0, 0x0)
    Default: (String, 0x0, 0x0, 0x0)
    pass

class 0x103b4f7d(0x65a1bb16):
    DeltaDriver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class LevelScriptFunctionLink():
    FunctionName: (Hash, 0x0, 0x0, 0x0)
    LevelScriptLink: (Link, 0x0, 0x0, LevelControlScript)
    pass

class AndInputSourceBool(IInputSourceBool):
    Sources: (List2, 0x0, Pointer, IInputSourceBool)
    pass

class CcBehaviorData(ICcBehaviorData):
    CcBehavior: (Embed, 0x0, 0x0, TargetingPriorityList)
    pass

class 0x1099c885(GameModeConstant):
    Character: (Link, 0x0, 0x0, TftCharacter)
    pass

class GetModePreloadFlags(LevelScriptBlock):
    ModePreloadFlags: (Embed, 0x0, 0x0, IntTableSet)
    pass

class 0x10b5dae9(0x26d26471):
    PercentageRequired: (U8, 0x0, 0x0, 0x0)
    pass

class MilestoneData():
    Milestones: (List, 0x0, U64, 0x0)
    MilestoneTraKey: (String, 0x0, 0x0, 0x0)
    pass

class IsMeleeCastRequirement(ICastRequirement):
    pass

class TempTable2Table(ScriptTable):
    pass

class ChampionRuneRecommendation():
    pass

class FxActionVfxAttach(FxActionVfxBase):
    pass

class 0x1125294b(ILolSpellScriptEvent):
    pass

class 0x114828a9():
    0xf3e8505f: (U16, 0x0, 0x0, 0x0)
    pass

class TftCutsceneBasePostFxClip(TftCutsceneClip):
    BlendOutTime: (F32, 0x0, 0x0, 0x0)
    BlendInTime: (F32, 0x0, 0x0, 0x0)
    VisibleFilter: (U32, 0x0, 0x0, 0x0)
    BlackboardAssociatedPlayers: (List2, 0x0, String, 0x0)
    pass

class 0x115b5460(0x3e265091):
    TextureToOverride: (Hash, 0x0, 0x0, 0x0)
    TacticianIndex: (U32, 0x0, 0x0, 0x0)
    pass

class TftBehaviorScript(BehaviorScript):
    Sequences: (Map, U32, Embed, ScriptBtSequence)
    pass

class 0x1181085f():
    0x77cef4e0: (List, 0x0, Embed, 0xf2bc55fb)
    Stage: (U8, 0x0, 0x0, 0x0)
    VisibleElements: (List, 0x0, Hash, 0x0)
    TitleTra: (String, 0x0, 0x0, 0x0)
    pass

class GrassSwayIntensityParametricUpdater(IFloatParametricUpdater):
    pass

class CharacterHealthBarDataRecord():
    CustomHealthBarTemplate: (Pointer, 0x0, 0x0, HealthbarTemplate)
    UnitHealthBarStyle: (U8, 0x0, 0x0, 0x0)
    AttachToBone: (String, 0x0, 0x0, 0x0)
    ScreenOffset: (Vec2, 0x0, 0x0, 0x0)
    HpPerTick: (F32, 0x0, 0x0, 0x0)
    ShowCharacterStateIndicatorToAllies: (Bool, 0x0, 0x0, 0x0)
    UnitBarKey: (String, 0x0, 0x0, 0x0)
    ShowCharacterStateIndicatorOnStartGame: (Bool, 0x0, 0x0, 0x0)
    Scale: (F32, 0x0, 0x0, 0x0)
    ShowCharacterStateIndicatorToEnemies: (Bool, 0x0, 0x0, 0x0)
    ShowWhileUntargetable: (Bool, 0x0, 0x0, 0x0)
    AlphaOutWhileUntargetable: (Bool, 0x0, 0x0, 0x0)
    WorldOffset: (Vec3, 0x0, 0x0, 0x0)
    CharacterStateIndicatorMaxCount: (U32, 0x0, 0x0, 0x0)
    pass

class InputSourceFloatRemap(IInputSourceFloat):
    Scale: (F32, 0x0, 0x0, 0x0)
    Bias: (F32, 0x0, 0x0, 0x0)
    pass

class MapVisibilityFlagRange():
    MinIndex: (U8, 0x0, 0x0, 0x0)
    MaxIndex: (U8, 0x0, 0x0, 0x0)
    pass

class TftCondensedItemCombineTooltipData():
    Scene: (Hash, 0x0, 0x0, 0x0)
    ItemIconTwo: (Hash, 0x0, 0x0, 0x0)
    ComponentIcons: (Hash, 0x0, 0x0, 0x0)
    ItemIconOne: (Hash, 0x0, 0x0, 0x0)
    pass

class TftMatchupBannerUiContainer():
    IconEnableTime: (F32, 0x0, 0x0, 0x0)
    TacticianIcon: (Hash, 0x0, 0x0, 0x0)
    VfxEnableTime: (F32, 0x0, 0x0, 0x0)
    Vfx: (Hash, 0x0, 0x0, 0x0)
    TextEnableTime: (F32, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    0xe291ee04: (List2, 0x0, Embed, 0x84c56837)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x11efc9e9():
    mDataId: (U32, 0x0, 0x0, 0x0)
    mFrame: (F32, 0x0, 0x0, 0x0)
    pass

class AiMarker(AiBaseClient):
    pass

class IMapVisibilityController():
    PathHash: (Hash, 0x0, 0x0, 0x0)
    pass

class TftHudAnnouncementData():
    mSceneTransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mSceneTransitionOut: (Embed, 0x0, 0x0, HudMenuTransitionData)
    pass

class LoadingScreenPlayerCardTftData(LoadingScreenPlayerCardBaseData):
    SummonerIcon: (Hash, 0x0, 0x0, 0x0)
    SummonerIcon: (List, 0x0, Hash, 0x0)
    CharacterBannerSkinName: (Hash, 0x0, 0x0, 0x0)
    Honor: (Embed, 0x0, 0x0, LoadingScreenHonorFlairData)
    CharacterSplashEmblem: (Embed, 0x0, 0x0, LoadingScreenEmblemData)
    Regalia: (Embed, 0x0, 0x0, LoadingScreenRegaliaData)
    CharacterSplashSkinName: (Hash, 0x0, 0x0, 0x0)
    RankedFrames: (Link, 0x0, 0x0, LoadingScreenRankedFrames)
    CharacterSplash: (Hash, 0x0, 0x0, 0x0)
    SummonerName: (Embed, 0x0, 0x0, LoadingScreenSummonerNameData)
    SummonerName: (List, 0x0, Hash, 0x0)
    Rating: (Embed, 0x0, 0x0, LoadingScreenRatedData)
    pass

class DestroyOnMovementCompleteSpec(MissileBehaviorSpec):
    mDelay: (I32, 0x0, 0x0, 0x0)
    pass

class X3dSharedConstantDef():
    Register: (I32, 0x0, 0x0, 0x0)
    Count: (U32, 0x0, 0x0, 0x0)
    Type: (U32, 0x0, 0x0, 0x0)
    SetManually: (Bool, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    PlatformMask: (U32, 0x0, 0x0, 0x0)
    pass

class IGameCalculationPartByCharLevel(IGameCalculationPart):
    pass

class TimeMultiplierCheat(Cheat):
    mSpeedDown: (Bool, 0x0, 0x0, 0x0)
    mSpeedUp: (Bool, 0x0, 0x0, 0x0)
    pass

class StatUiData():
    mName: (String, 0x0, 0x0, 0x0)
    mAbbreviation: (String, 0x0, 0x0, 0x0)
    mIconKey: (String, 0x0, 0x0, 0x0)
    mScalingTagKey: (String, 0x0, 0x0, 0x0)
    mDisplayType: (U8, 0x0, 0x0, 0x0)
    pass

class ParametricMovementEntry():
    Value: (F32, 0x0, 0x0, 0x0)
    MovementSpec: (Pointer, 0x0, 0x0, MissileMovementSpec)
    pass

class OptionTemplateLabel(IOptionTemplate):
    Label1: (Hash, 0x0, 0x0, 0x0)
    Label2: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxParentInheritanceParams():
    RelativeOffset: (Embed, 0x0, 0x0, ValueVector3)
    Mode: (U8, 0x0, 0x0, 0x0)
    pass

class VfxShapeCylinder(VfxShapeVolume):
    Height: (F32, 0x0, 0x0, 0x0)
    Radius: (F32, 0x0, 0x0, 0x0)
    pass

class 0x12b12bdf():
    0xa41734ff: (Hash, 0x0, 0x0, 0x0)
    0xa9d41f94: (Hash, 0x0, 0x0, 0x0)
    SubTeamName: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x12b69e95():
    Behaviors: (List2, 0x0, Embed, 0xfe897399)
    pass

class TftUnitPropertyNames():
    CharacterRoleOverride: (Link, 0x0, 0x0, TftUnitPropertyDefinition)
    RerollTraitLastCombatActive: (Link, 0x0, 0x0, TftUnitPropertyDefinition)
    UnitGoldValue: (Link, 0x0, 0x0, TftUnitPropertyDefinition)
    RerollTraitCounter: (Link, 0x0, 0x0, TftUnitPropertyDefinition)
    0x5f9096dc: (Link, 0x0, 0x0, TftUnitPropertyDefinition)
    0x819c43fe: (Link, 0x0, 0x0, TftUnitPropertyDefinition)
    ForceLookAtCamera: (Link, 0x0, 0x0, TftUnitPropertyDefinition)
    0x9dc71969: (Link, 0x0, 0x0, TftUnitPropertyDefinition)
    0xeab20b3: (Link, 0x0, 0x0, TftUnitPropertyDefinition)
    pass

class 0x12de3fcb(IScriptBlock, IBehaviorScriptBlock):
    Sequence: (Embed, 0x0, 0x0, ScriptBtRandomSelector)
    pass

class LevelPropAiClient(LevelPropAiCommon):
    pass

class FloatOffsetTableGet(ScriptTableGet, IFloatGet):
    Offset: (F32, 0x0, 0x0, 0x0)
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Table: (Pointer, 0x0, 0x0, RsTable)
    Var: (Hash, 0x0, 0x0, 0x0)
    Var: (String, 0x0, 0x0, 0x0)
    pass

class DeathTimes():
    mAllowRespawnMods: (Bool, 0x0, 0x0, 0x0)
    mStartDeathTimerForZombies: (Bool, 0x0, 0x0, 0x0)
    mScalingStartTime: (U32, 0x0, 0x0, 0x0)
    mScalingPercentCap: (F32, 0x0, 0x0, 0x0)
    mScalingPercentIncrease: (F32, 0x0, 0x0, 0x0)
    mTimeDeadPerLevel: (List, 0x0, F32, 0x0)
    mScalingIncrementTime: (U32, 0x0, 0x0, 0x0)
    mScalingPoints: (List, 0x0, Embed, DeathTimesScalingPoint)
    pass

class 0x131f5725(0x911f126a):
    StaticTexture: (Hash, 0x0, 0x0, 0x0)
    pass

class TargetingParameters():
    TargetingParamName: (String, 0x0, 0x0, 0x0)
    0x2b9c6a13: (Bool, 0x0, 0x0, 0x0)
    RangeValue: (Pointer, 0x0, 0x0, ITargetingRangeValue)
    TargetSpell: (Hash, 0x0, 0x0, 0x0)
    0x791c5fa3: (Bool, 0x0, 0x0, 0x0)
    mAffectsStatusFlags: (U32, 0x0, 0x0, 0x0)
    0x9845aa67: (Bool, 0x0, 0x0, 0x0)
    UnitObjectTags: (Embed, 0x0, 0x0, ObjectTags)
    mSpellFlags: (U32, 0x0, 0x0, 0x0)
    Radius: (F32, 0x0, 0x0, 0x0)
    ExitConditions: (List2, 0x0, U8, 0x0)
    mAffectsTypeFlags: (U32, 0x0, 0x0, 0x0)
    0xfc462d60: (List2, 0x0, Embed, 0xe90af953)
    pass

class HealthBarTickStyleUnit(HealthBarTickStyleBase):
    StandardTick: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x135a0579():
    ResultGridItem: (Hash, 0x0, 0x0, 0x0)
    TooltipOffset: (Hash, 0x0, 0x0, 0x0)
    ResultIcon: (Hash, 0x0, 0x0, 0x0)
    ResultText: (Hash, 0x0, 0x0, 0x0)
    ResultRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class UiPerkSummonerSpecialistSelectorButtonData():
    Button: (Hash, 0x0, 0x0, 0x0)
    SpellIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class ChatThrottlerData():
    CooldownTimeSeconds: (F32, 0x0, 0x0, 0x0)
    ThrottleLimit: (U32, 0x0, 0x0, 0x0)
    CheckDurationSeconds: (F32, 0x0, 0x0, 0x0)
    pass

class 0x138c3d23():
    Subtitle: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    Description: (Hash, 0x0, 0x0, 0x0)
    Title: (Hash, 0x0, 0x0, 0x0)
    SubtitleTra: (String, 0x0, 0x0, 0x0)
    pass

class UiPerksStatData():
    Type: (U32, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    HitRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class AboveHealthPercentCastRequirement(ICastRequirement):
    mCurrentPercentHealth: (F32, 0x0, 0x0, 0x0)
    pass

class TftTeamPlannerMemberData():
    TraitIconBgs: (List, 0x3, Hash, 0x0)
    SnapshotHighlight: (Hash, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    HoverEffectGlowChampion: (Hash, 0x0, 0x0, 0x0)
    TraitIcons: (List, 0x3, Hash, 0x0)
    Traits: (List, 0x3, Embed, TftTeamPlannerMemberDisplayTrait)
    HoverEffectGlowTier: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    HoverEffectGlowTraitBackgrounds: (List, 0x3, Hash, 0x0)
    Tiers: (List, 0x5, Hash, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    HoverEffectGlowTraitIcons: (List, 0x3, Hash, 0x0)
    pass

class UiPropertyOverrideLoadable(PropertyOverrideLoadable):
    pass

class ScriptFunction(RootScriptSequence, ScriptSequence):
    FunctionDef: (Embed, 0x0, 0x0, 0xeca2da9a)
    pass

class 0x13ed57fb(BaseEventData):
    0x6b2c8262: (List, 0x0, Embed, 0x88b225d6)
    pass

class TftGameStartViewController(ViewController):
    GameStartTextShowDelaySecs: (F32, 0x0, 0x0, 0x0)
    GameStartText: (Hash, 0x0, 0x0, 0x0)
    GameWelcomeVfx: (Hash, 0x0, 0x0, 0x0)
    GameWelcomeLocVnVn: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    GameWelcomeVfxStartTimeSecs: (F32, 0x0, 0x0, 0x0)
    GameStartTraMap: (Map, U32, String, 0x0)
    GameStartVfxStartTimeSecs: (F32, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    GameWelcomeScene: (Hash, 0x0, 0x0, 0x0)
    GameWelcomeLocZhCn: (Hash, 0x0, 0x0, 0x0)
    TutorialOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    GameWelcomeLocZhTw: (Hash, 0x0, 0x0, 0x0)
    GameStartVfxTop: (Hash, 0x0, 0x0, 0x0)
    GameStartTextShowDurationSecs: (F32, 0x0, 0x0, 0x0)
    GameStartLabs: (Map, U32, Embed, TftGameStartLabFields)
    GameStartIconBaseTexture: (String, 0x0, 0x0, 0x0)
    GameStartTable: (Map, U32, Link, TftGameStartSequence)
    GameWelcomeLocScene: (Hash, 0x0, 0x0, 0x0)
    GameWelcomeVfxShowDurationSecs: (F32, 0x0, 0x0, 0x0)
    GameStartTextScene: (Hash, 0x0, 0x0, 0x0)
    GameStartVfxBottom: (Hash, 0x0, 0x0, 0x0)
    pass

class EsportTeamEntry():
    LeagueName: (String, 0x0, 0x0, 0x0)
    TeamName: (String, 0x0, 0x0, 0x0)
    TextureName: (String, 0x0, 0x0, 0x0)
    pass

class CheatMenuUiData():
    mPage: (U32, 0x0, 0x0, 0x0)
    mHotkeys: (List, 0x0, String, 0x0)
    mFloatingTextDisplayName: (String, 0x0, 0x0, 0x0)
    mRow: (U32, 0x0, 0x0, 0x0)
    mDisplayName: (String, 0x0, 0x0, 0x0)
    mIsToggleCheat: (Bool, 0x0, 0x0, 0x0)
    mHotkey: (String, 0x0, 0x0, 0x0)
    mDynamicTooltipText: (String, 0x0, 0x0, 0x0)
    mTooltipText: (String, 0x0, 0x0, 0x0)
    pass

class FxActionMaterialAnimate(IFxAction):
    Target: (Embed, 0x0, 0x0, FxTarget)
    Target: (Embed, 0x0, 0x0, FxObjectSelector)
    ParameterName: (String, 0x0, 0x0, 0x0)
    FromValue: (F32, 0x0, 0x0, 0x0)
    EasingType: (U8, 0x0, 0x0, 0x0)
    ToValue: (F32, 0x0, 0x0, 0x0)
    pass

class ContextualConditionCharacterHasTimeRemainingForAnimation(ICharacterSubcondition):
    mMinRemainingTime: (F32, 0x0, 0x0, 0x0)
    mAnimationName: (Hash, 0x0, 0x0, 0x0)
    pass

class TftCutsceneLegacyCamClip(TftCutsceneClip):
    AssociatedPlayers: (List2, 0x0, String, 0x0)
    VisibleFilter: (U32, 0x0, 0x0, 0x0)
    BlackboardOffsetPosition: (String, 0x0, 0x0, 0x0)
    Overrides: (List2, 0x0, Embed, TftCutsceneCamOverrideEntry)
    pass

class 0x1472ec25(IFxAction):
    Location: (Pointer, 0x0, 0x0, IFxLocation)
    TargetObject: (Embed, 0x0, 0x0, FxObjectSelector)
    pass

class 0x1493959a():
    0x1bb7131a: (Embed, 0x0, 0x0, 0x990115ea)
    EventPassExpText: (Hash, 0x0, 0x0, 0x0)
    EventPassNextRewardIcon: (Hash, 0x0, 0x0, 0x0)
    EventPassNameText: (Hash, 0x0, 0x0, 0x0)
    EventPassNextRewardText: (Hash, 0x0, 0x0, 0x0)
    EventPassButton: (Hash, 0x0, 0x0, 0x0)
    EventPassCompletedText: (Hash, 0x0, 0x0, 0x0)
    EventPassCompletedFrame: (Hash, 0x0, 0x0, 0x0)
    0xed10fe9a: (Embed, 0x0, 0x0, UiMilestoneProgressMeter)
    pass

class CherryArenaData():
    0x7680caf3: (U32, 0x0, 0x0, 0x0)
    ArenaDisplayNameTra: (String, 0x0, 0x0, 0x0)
    pass

class ShaderLogicalParameter():
    Fields: (U32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class StoreCategoryInventoryFilter():
    mInventoryType: (String, 0x0, 0x0, 0x0)
    mOrder: (U8, 0x0, 0x0, 0x0)
    mInventoryFilters: (List, 0x0, Embed, StoreCategoryInventoryFilter)
    mItemIds: (List, 0x0, I32, 0x0)
    mItemIds: (List, 0x0, U32, 0x0)
    pass

class DelayedBoolMaterialDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    mDelayOff: (F32, 0x0, 0x0, 0x0)
    mDelayOn: (F32, 0x0, 0x0, 0x0)
    mBoolDriver: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    mBoolDriver: (Pointer, 0x0, 0x0, IDynamicMaterialBoolDriver)
    pass

class LinkedCcBehaviorData(ICcBehaviorData):
    CcBehaviorLink: (Hash, 0x0, 0x0, 0x0)
    pass

class OptionItemFilter_ClassicMusicAllowed(IOptionItemFilter):
    pass

class 0x14e5d6d8(ViewController):
    MessageTemplate: (Embed, 0x0, 0x0, 0x5ad4a256)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MessageDisplayData: (Embed, 0x0, 0x0, HudMessageDisplayData)
    ItemSceneTemplate: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxVector3fBase():
    pass

class FxTableEntry():
    Sequence: (Link, 0x0, 0x0, FxSequence)
    Type: (Link, 0x0, 0x0, FxType)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class ScriptBtOverrideResolveState(IScriptBt, IScriptSequence):
    Blocks: (List2, 0x0, Pointer, IBehaviorScriptBlock)
    pass

class 0x150d1b92():
    0x717e686: (Bool, 0x0, 0x0, 0x0)
    0xe38f54f7: (U32, 0x0, 0x0, 0x0)
    pass

class BehaviorScriptContainer():
    CharacterRecord: (Hash, 0x0, 0x0, 0x0)
    0x915b2238: (Hash, 0x0, 0x0, 0x0)
    BotSpell1: (Hash, 0x0, 0x0, 0x0)
    Position: (String, 0x0, 0x0, 0x0)
    BehaviorScriptList: (List2, 0x0, Hash, 0x0)
    BehaviorScriptList: (List2, 0x0, Link, BehaviorScript)
    pass

class SpawnTurret(IScriptBlock, LevelScriptBlock):
    AiUnitName: (String, 0x0, 0x0, 0x0)
    Lane: (U16, 0x0, 0x0, 0x0)
    AiGroupName: (Hash, 0x0, 0x0, 0x0)
    Position: (U16, 0x0, 0x0, 0x0)
    Team: (U32, 0x0, 0x0, 0x0)
    MapObjectName: (String, 0x0, 0x0, 0x0)
    pass

class ReturnToCasterOnMovementCompleteSpec(MissileBehaviorSpec):
    pass

class 0x1519e8d2():
    pass

class GameModeSpellList():
    Spells: (List2, 0x0, Hash, 0x0)
    pass

class ConditionBoolClipData(ClipBaseData):
    Updater: (Pointer, 0x0, 0x0, IBooleanParametricUpdater)
    mUpdaterType: (U32, 0x0, 0x0, 0x0)
    mFalseConditionClipName: (Hash, 0x0, 0x0, 0x0)
    mPlayAnimChangeFromBeginning: (Bool, 0x0, 0x0, 0x0)
    mChangeAnimationMidPlay: (Bool, 0x0, 0x0, 0x0)
    mTrueConditionClipName: (Hash, 0x0, 0x0, 0x0)
    mTrackIndex: (U32, 0x0, 0x0, 0x0)
    DontStompTransitionClip: (Bool, 0x0, 0x0, 0x0)
    SyncFrameOnChangeAnim: (Bool, 0x0, 0x0, 0x0)
    mTrueClipId: (U32, 0x0, 0x0, 0x0)
    mChildAnimDelaySwitchTime: (F32, 0x0, 0x0, 0x0)
    mFalseClipId: (U32, 0x0, 0x0, 0x0)
    pass

class LoadingScreenClash():
    OrderTeam: (Embed, 0x0, 0x0, LoadingScreenClashTeam)
    ChaosTeam: (Embed, 0x0, 0x0, LoadingScreenClashTeam)
    pass

class 0x159bf4ba(0x7319918a):
    Value: (List2, 0x0, Hash, 0x0)
    pass

class IsCannonMinion(IStatStoneLogicDriver):
    pass

class 0x15ebaa9c(IScriptBlock):
    Formula: (String, 0x0, 0x0, 0x0)
    Dest: (Embed, 0x0, 0x0, ScriptTableSet)
    pass

class TftCharacterRoleData():
    ItemRoleNameTra: (String, 0x0, 0x0, 0x0)
    Items: (List, 0x0, Link, TftItemData)
    Items: (List2, 0x0, Hash, 0x0)
    CharacterRoleNameTra: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    DescriptionTra: (String, 0x0, 0x0, 0x0)
    pass

class LoadingScreenPlayerCardClassicData(LoadingScreenPlayerCardBaseData):
    SummonerIcon: (Hash, 0x0, 0x0, 0x0)
    SummonerIcon: (List, 0x0, Hash, 0x0)
    Border: (Hash, 0x0, 0x0, 0x0)
    Mastery: (Embed, 0x0, 0x0, LoadingScreenChampionMasteryData)
    Honor: (Embed, 0x0, 0x0, LoadingScreenHonorFlairData)
    CharacterSkinName: (List, 0x0, Hash, 0x0)
    CharacterSplashEmblem: (Embed, 0x0, 0x0, LoadingScreenEmblemData)
    Regalia: (Embed, 0x0, 0x0, LoadingScreenRegaliaData)
    BorderScene: (Hash, 0x0, 0x0, 0x0)
    SummonerTitle: (Embed, 0x0, 0x0, LoadingScreenSummonerTitleData)
    RankedFrames: (Link, 0x0, 0x0, LoadingScreenRankedFrames)
    Perks: (List, 0x2, Embed, LoadingScreenPlayerCardClassicSpellData)
    Challenges: (Embed, 0x0, 0x0, LoadingScreenChallengesData)
    CharacterSplash: (Hash, 0x0, 0x0, 0x0)
    SummonerName: (Embed, 0x0, 0x0, LoadingScreenSummonerNameData)
    SummonerName: (List, 0x0, Hash, 0x0)
    SummonerSpells: (List, 0x2, Embed, LoadingScreenPlayerCardClassicSpellData)
    pass

class ContextualActionCooldownModifications():
    IgnoreTimer: (Bool, 0x0, 0x0, 0x0)
    ResetTimer: (Bool, 0x0, 0x0, 0x0)
    DontResetTimer: (Bool, 0x0, 0x0, 0x0)
    pass

class ByCharLevelInterpolationCalculationPart(IGameCalculationPartByCharLevel, ISpellCalculationPartByCharLevel, ISpellCalculationPart):
    mEndValue: (F32, 0x0, 0x0, 0x0)
    mScaleByStatProgressionMultiplier: (Bool, 0x0, 0x0, 0x0)
    mScalePastDefaultMaxLevel: (Bool, 0x0, 0x0, 0x0)
    mStartValue: (F32, 0x0, 0x0, 0x0)
    pass

class MissileBehaviorSpec():
    pass

class TransitionClipBlendData(BaseBlendData):
    mClipName: (Hash, 0x0, 0x0, 0x0)
    pass

class MapNavigationMesh():
    NavMeshFileName: (String, 0x0, 0x0, 0x0)
    pass

class ViewControllerListFilter_Or(ViewControllerListFilterI):
    Filters: (List, 0x0, Pointer, ViewControllerListFilterI)
    pass

class IBooleanParametricUpdater(IBaseParametricUpdater):
    pass

class IDialogPickChoice():
    pass

class 0x165cc655(ILolSpellScriptEvent):
    pass

class 0x1668b3e5():
    EventPassLevelText: (Hash, 0x0, 0x0, 0x0)
    0x1bb7131a: (Embed, 0x0, 0x0, 0x8d8b1535)
    EventPassExpText: (Hash, 0x0, 0x0, 0x0)
    EventPassNextRewardIcon: (Hash, 0x0, 0x0, 0x0)
    EventPassNameText: (Hash, 0x0, 0x0, 0x0)
    EventPassNextRewardText: (Hash, 0x0, 0x0, 0x0)
    EventPassButton: (Hash, 0x0, 0x0, 0x0)
    EventPassCompletedText: (Hash, 0x0, 0x0, 0x0)
    EventPassCompletedFrame: (Hash, 0x0, 0x0, 0x0)
    0xed10fe9a: (Embed, 0x0, 0x0, UiMilestoneProgressMeter)
    pass

class 0x16892533(IFxAction):
    ArmLength: (F32, 0x0, 0x0, 0x0)
    Follow: (Bool, 0x0, 0x0, 0x0)
    Yaw: (F32, 0x0, 0x0, 0x0)
    ZoomEase: (U8, 0x0, 0x0, 0x0)
    Fov: (F32, 0x0, 0x0, 0x0)
    Pitch: (F32, 0x0, 0x0, 0x0)
    Location: (Pointer, 0x0, 0x0, IFxLocation)
    pass

class MapSunProperties(MapComponent):
    PbrSunAdditionalScale: (F32, 0x0, 0x0, 0x0)
    FogColor: (Vec4, 0x0, 0x0, 0x0)
    FogEmissiveRemap: (F32, 0x0, 0x0, 0x0)
    FogLowQualityModeEmissiveRemap: (F32, 0x0, 0x0, 0x0)
    SunIntensityScale: (F32, 0x0, 0x0, 0x0)
    UseBloom: (Bool, 0x0, 0x0, 0x0)
    FogAlternateColor: (Vec4, 0x0, 0x0, 0x0)
    GroundColor: (Vec4, 0x0, 0x0, 0x0)
    SunColor: (Vec4, 0x0, 0x0, 0x0)
    AoStrength: (F32, 0x0, 0x0, 0x0)
    FogStartAndEnd: (Vec2, 0x0, 0x0, 0x0)
    AoRadius: (F32, 0x0, 0x0, 0x0)
    FogEnabled: (Bool, 0x0, 0x0, 0x0)
    LightMapColorScale: (F32, 0x0, 0x0, 0x0)
    SurfaceAreaToShadowMapScale: (F32, 0x0, 0x0, 0x0)
    OverrideSunSpecDirection: (Option, 0x0, Vec3, 0x0)
    SkyLightColor: (Vec4, 0x0, 0x0, 0x0)
    TempAmbientColor: (Vec4, 0x0, 0x0, 0x0)
    SkyLightScale: (F32, 0x0, 0x0, 0x0)
    ScaleSunShadowIntensity: (F32, 0x0, 0x0, 0x0)
    0xc6d048fc: (F32, 0x0, 0x0, 0x0)
    ShadowBias: (F32, 0x0, 0x0, 0x0)
    SunRadiusForShadows: (F32, 0x0, 0x0, 0x0)
    SunDirection: (Vec3, 0x0, 0x0, 0x0)
    HorizonColor: (Vec4, 0x0, 0x0, 0x0)
    pass

class TftBanner():
    BannerTexturePath: (String, 0x0, 0x0, 0x0)
    PityThreshold: (U32, 0x0, 0x0, 0x0)
    Id: (String, 0x0, 0x0, 0x0)
    ChaseTable: (Link, 0x0, 0x0, TftBannerTable)
    ActivationDateTime: (String, 0x0, 0x0, 0x0)
    DeactivationDateTime: (String, 0x0, 0x0, 0x0)
    BannerCurrencyId: (String, 0x0, 0x0, 0x0)
    NameTraKey: (String, 0x0, 0x0, 0x0)
    PityCounterId: (String, 0x0, 0x0, 0x0)
    RootTable: (Link, 0x0, 0x0, TftBannerTable)
    DescriptionTraKey: (String, 0x0, 0x0, 0x0)
    MythicTokenOfferId: (String, 0x0, 0x0, 0x0)
    pass

class NotificationsPanelViewController(ViewController):
    EmptyStateGroup: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    ClearAllButton: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    ViewPaneDefinition: (Embed, 0x0, 0x0, ViewPaneDefinition)
    ListItemData: (Embed, 0x0, 0x0, NotificationListItemData)
    ClearAllButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    ViewPaneLink: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x16b1df95():
    mOffset: (Vec2, 0x0, 0x0, 0x0)
    mAggroEffect: (Link, 0x0, 0x0, EffectElement)
    pass

class EmblemSettings():
    mBottomFraction: (F32, 0x0, 0x0, 0x0)
    mDebugDrawEmblems: (Bool, 0x0, 0x0, 0x0)
    pass

class FloatTextIconData():
    mIconFileName: (String, 0x0, 0x0, 0x0)
    mOffset: (Vec2, 0x0, 0x0, 0x0)
    mColor: (Color, 0x0, 0x0, 0x0)
    mDisplaySize: (Vec2, 0x0, 0x0, 0x0)
    mAlignment: (U32, 0x0, 0x0, 0x0)
    pass

class ScaleByScaleSkinCoef(MissileBehaviorSpec):
    pass

class UiWeeklyMissionTemplate():
    DoubleDivider: (Hash, 0x0, 0x0, 0x0)
    ObjectiveListLayout: (Hash, 0x0, 0x0, 0x0)
    DescriptionText: (Hash, 0x0, 0x0, 0x0)
    CompletionVfx: (Hash, 0x0, 0x0, 0x0)
    DoubleBackdrop: (Hash, 0x0, 0x0, 0x0)
    SingleRewardIcon: (Hash, 0x0, 0x0, 0x0)
    RewardGroup: (Hash, 0x0, 0x0, 0x0)
    SingleTitleText: (Hash, 0x0, 0x0, 0x0)
    SingleRewardFrame: (Hash, 0x0, 0x0, 0x0)
    0x34918fbe: (Embed, 0x0, 0x0, UiMissionObjectiveData)
    0x35919151: (Embed, 0x0, 0x0, UiMissionObjectiveData)
    SingleBackdrop: (Hash, 0x0, 0x0, 0x0)
    RewardIconFrame: (Hash, 0x0, 0x0, 0x0)
    MissionObjectiveData: (Embed, 0x0, 0x0, UiMissionObjectiveData)
    HorizontalSpacer: (Hash, 0x0, 0x0, 0x0)
    DoubleAlertText: (Hash, 0x0, 0x0, 0x0)
    DoubleRewardFrame: (Hash, 0x0, 0x0, 0x0)
    DoubleAlertIcon: (Hash, 0x0, 0x0, 0x0)
    ObjectiveLayout: (Hash, 0x0, 0x0, 0x0)
    RewardText: (Hash, 0x0, 0x0, 0x0)
    MissionLayout: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    NewMissionVfx: (Hash, 0x0, 0x0, 0x0)
    RewardIcon: (Hash, 0x0, 0x0, 0x0)
    TitleGroup: (Hash, 0x0, 0x0, 0x0)
    DoubleRewardText: (Hash, 0x0, 0x0, 0x0)
    SingleRewardText: (Hash, 0x0, 0x0, 0x0)
    VerticalSpacer: (Hash, 0x0, 0x0, 0x0)
    FooterGroup: (Hash, 0x0, 0x0, 0x0)
    AlertText: (Hash, 0x0, 0x0, 0x0)
    DoubleSeparatorText: (Hash, 0x0, 0x0, 0x0)
    AlertIcon: (Hash, 0x0, 0x0, 0x0)
    RewardLayout: (Hash, 0x0, 0x0, 0x0)
    SingleExpiryText: (Hash, 0x0, 0x0, 0x0)
    DoubleExpiryText: (Hash, 0x0, 0x0, 0x0)
    DoubleSeparator: (Hash, 0x0, 0x0, 0x0)
    LeftManagedLayout: (Hash, 0x0, 0x0, 0x0)
    SingleAlertIcon: (Hash, 0x0, 0x0, 0x0)
    HelperText: (Hash, 0x0, 0x0, 0x0)
    SingleDivider: (Hash, 0x0, 0x0, 0x0)
    DoubleTitleText: (Hash, 0x0, 0x0, 0x0)
    LayoutGroup: (Hash, 0x0, 0x0, 0x0)
    SingleAlertText: (Hash, 0x0, 0x0, 0x0)
    SingleObjective: (Embed, 0x0, 0x0, UiMissionObjectiveData)
    ExpiryText: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    Divder: (Hash, 0x0, 0x0, 0x0)
    DoubleRewardIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x1717869f(MapGraphicsFeature):
    Settings: (Embed, 0x0, 0x0, 0x502b0c72)
    0xce8f4190: (Embed, 0x0, 0x0, 0xce8f4190)
    pass

class 0x172f5c92():
    Enabler: (Link, 0x0, 0x0, IEnabler)
    pass

class IGameCalculation():
    mMultiplier: (Pointer, 0x0, 0x0, IGameCalculationPart)
    mExpandedTooltipCalculationDisplay: (U8, 0x0, 0x0, 0x0)
    ResultModifier: (U8, 0x0, 0x0, 0x0)
    mSimpleTooltipCalculationDisplay: (U8, 0x0, 0x0, 0x0)
    TooltipOnly: (Bool, 0x0, 0x0, 0x0)
    StaticTooltipCalculationDisplay: (U8, 0x0, 0x0, 0x0)
    pass

class 0x1761983a(ISequenceActionInstance):
    pass

class 0x1778b398():
    Group: (Link, 0x0, 0x0, 0xb26bd951)
    Name: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x1792fdb5(ILogicFloatDriver):
    0x3a302e74: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    ValueArray: (List2, 0x0, Pointer, ILogicFloatDriver)
    pass

class FloatingTextTunables():
    mAnimatedTextQueueDelay: (F32, 0x0, 0x0, 0x0)
    mMinionComparisonMultiplier: (F32, 0x0, 0x0, 0x0)
    mLocalPlayerHealthComparison: (F32, 0x0, 0x0, 0x0)
    mYResolutionBaseline: (F32, 0x0, 0x0, 0x0)
    mScrollSpeed: (F32, 0x0, 0x0, 0x0)
    mMaxFloatingTextItems: (U32, 0x0, 0x0, 0x0)
    mIntervalInPix: (F32, 0x0, 0x0, 0x0)
    mMaximumDynamicScale: (F32, 0x0, 0x0, 0x0)
    mComparisonByLevel: (List, 0x0, F32, 0x0)
    mExpirationTimeThreshold: (F32, 0x0, 0x0, 0x0)
    CameraMask: (U32, 0x0, 0x0, 0x0)
    mMinimumDynamicScale: (F32, 0x0, 0x0, 0x0)
    mExpirationPriorityThreshold: (F32, 0x0, 0x0, 0x0)
    pass

class 0x179a7e40(IBehaviorScriptBlock):
    pass

class ItemRecommendationCondition():
    mGroupId: (U8, 0x0, 0x0, 0x0)
    mItem: (Hash, 0x0, 0x0, 0x0)
    mDisplayLimit: (U32, 0x0, 0x0, 0x0)
    pass

class VersionString():
    VersionText: (Hash, 0x0, 0x0, 0x0)
    pass

class TransitionMissileSpecification(MissileSpecification):
    pass

class TextureOverride():
    TexturePath: (String, 0x0, 0x0, 0x0)
    pass

class UiPerkSummonerSpecialistSelector():
    Scene: (Hash, 0x0, 0x0, 0x0)
    SelectorButtonTemplate: (Embed, 0x0, 0x0, UiPerkSummonerSpecialistSelectorButtonData)
    Layout: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x17eb9592(ILolSpellScriptEvent):
    pass

class GameModeItemList():
    mItems: (List, 0x0, Hash, 0x0)
    mItems: (List2, 0x0, Hash, 0x0)
    pass

class BannerOptions():
    SubMeshName: (String, 0x0, 0x0, 0x0)
    IsSpectatorOnly: (Bool, 0x0, 0x0, 0x0)
    DefaultMaterial: (Link, 0x0, 0x0, IMaterialDef)
    pass

class 0x1818fe10(ILolSpellScriptEvent):
    pass

class 0x182cf031():
    0xf5533ae0: (Map, U32, Link, VfxSystemDefinitionData)
    pass

class TftTrovesBannerTableEntry():
    Weight: (U32, 0x0, 0x0, 0x0)
    BannerNode: (Link, 0x0, 0x0, TftTrovesBannerNode)
    pass

class HealthMeter():
    FadeBar: (Hash, 0x0, 0x0, 0x0)
    ValueText: (Hash, 0x0, 0x0, 0x0)
    Meter: (Hash, 0x0, 0x0, 0x0)
    FadeSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class 0x186c58e4(IBehaviorScriptBlock):
    pass

class NumberFormattingBehavior():
    WesternNumberGrouping: (Bool, 0x0, 0x0, 0x0)
    MinimumDigitCountForThousandsSeparator: (U32, 0x0, 0x0, 0x0)
    TrimTrailingZeroesAfterDecimalPoint: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x18871c61():
    0x9d6e31fd: (Hash, 0x0, 0x0, 0x0)
    0xc742ceb4: (Hash, 0x0, 0x0, 0x0)
    BottomHrMomentumPost: (List2, 0x0, Hash, 0x0)
    pass

class TargeterDefinitionMinimap(TargeterDefinition):
    UseCasterBoundingBox: (Bool, 0x0, 0x0, 0x0)
    UseCasterBoundingBox: (Option, 0x0, Bool, 0x0)
    CenterLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    OverrideBaseRange: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    pass

class 0x18bec123(Rscript):
    Sequence: (Embed, 0x0, 0x0, RootScriptSequence)
    pass

class 0x18ce0cda(IFxActionInstance):
    pass

class TftConditionalTraitSetData(TftBaseTraitSetData):
    RequiredUnitProperty: (Embed, 0x0, 0x0, TftRequiredUnitProperty)
    MaxUnits: (Option, 0x0, U32, 0x0)
    MinUnits: (U32, 0x0, 0x0, 0x0)
    ShouldAlwaysDisplay: (Bool, 0x0, 0x0, 0x0)
    Style: (U8, 0x0, 0x0, 0x0)
    pass

class ConfigString():
    Enabler: (Link, 0x0, 0x0, IEnabler)
    Value: (String, 0x0, 0x0, 0x0)
    pass

class OrScriptCondition(IScriptCondition):
    Conditions: (List, 0x0, Pointer, IScriptCondition)
    pass

class IScriptBt(IScriptSequence):
    Blocks: (List2, 0x0, Pointer, IBehaviorScriptBlock)
    pass

class UiMissionObjectiveData():
    ProgressText: (Hash, 0x0, 0x0, 0x0)
    ProgressCompleteVfx: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    AlertText: (Hash, 0x0, 0x0, 0x0)
    SeparatorText: (Hash, 0x0, 0x0, 0x0)
    AlertIcon: (Hash, 0x0, 0x0, 0x0)
    SeparatorIcon: (Hash, 0x0, 0x0, 0x0)
    ProgressFill: (Hash, 0x0, 0x0, 0x0)
    ProgressMeterBg: (Hash, 0x0, 0x0, 0x0)
    BodyText: (Hash, 0x0, 0x0, 0x0)
    ProgressComplete: (Hash, 0x0, 0x0, 0x0)
    ExpiryText: (Hash, 0x0, 0x0, 0x0)
    pass

class HudLoadingScreenWidgetProgressBar(IHudLoadingScreenWidget):
    pass

class ToolAlternateForm():
    TheSwitch: (String, 0x0, 0x0, 0x0)
    Spells: (List, 0x0, String, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    Champion: (String, 0x0, 0x0, 0x0)
    pass

class SystemAudioDataProperties():
    SystemTagEventList: (List, 0x0, Embed, AudioTagListProperties)
    SystemTagEventList: (Map, Hash, Embed, AudioTagListProperties)
    pass

class BackdropElementTeamParams():
    mEnemyParams: (Pointer, 0x0, 0x0, BackdropElementParams)
    mAllyParams: (Pointer, 0x0, 0x0, BackdropElementParams)
    mNeutralParams: (Pointer, 0x0, 0x0, BackdropElementParams)
    pass

class GrassSwayDirectionParametricUpdater(IFloatParametricUpdater):
    pass

class HudEmotePopupData():
    0x1432ccc0: (Bool, 0x0, 0x0, 0x0)
    0x3a8409fd: (F32, 0x0, 0x0, 0x0)
    EmotePopupDisplayTime: (F32, 0x0, 0x0, 0x0)
    mUiSound: (String, 0x0, 0x0, 0x0)
    0x6bd76883: (F32, 0x0, 0x0, 0x0)
    mEmotePopupTransitionOutro: (Embed, 0x0, 0x0, HudMenuTransitionData)
    0x728d935f: (F32, 0x0, 0x0, 0x0)
    0x75d54c28: (F32, 0x0, 0x0, 0x0)
    0x7cd0d83: (F32, 0x0, 0x0, 0x0)
    mEmotePopupDisplayTime: (F32, 0x0, 0x0, 0x0)
    0x946c7d22: (F32, 0x0, 0x0, 0x0)
    mEmotePopupTransitionIntro: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mEmoteFloatEnabled: (Bool, 0x0, 0x0, 0x0)
    0xf680b7d9: (F32, 0x0, 0x0, 0x0)
    pass

class 0x1a4d18fe(ISequenceAction):
    EnableOnEnd: (Bool, 0x0, 0x0, 0x0)
    Element: (Pointer, 0x0, 0x0, 0xe561be2e)
    DisableOnStart: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x1a4d9bd(ICharacterSubcondition):
    SpellBuff: (Hash, 0x0, 0x0, 0x0)
    pass

class UiElementIconData(UiElementAssetData):
    Color: (Color, 0x0, 0x0, 0x0)
    FlipX: (Bool, 0x0, 0x0, 0x0)
    FlipY: (Bool, 0x0, 0x0, 0x0)
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    mColor: (Color, 0x0, 0x0, 0x0)
    mUseAlpha: (Bool, 0x0, 0x0, 0x0)
    mMaterial: (Link, 0x0, 0x0, StaticMaterialDef)
    UseAlpha: (Bool, 0x0, 0x0, 0x0)
    Extension: (Pointer, 0x0, 0x0, IconElementDataExtension)
    Material: (Link, 0x0, 0x0, StaticMaterialDef)
    TextureData: (Pointer, 0x0, 0x0, IUiTextureDataProvider)
    PerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    PerPixelUvsY: (Bool, 0x0, 0x0, 0x0)
    mAtlas: (Pointer, 0x0, 0x0, IUiTextureDataProvider)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    mExtension: (Pointer, 0x0, 0x0, IconElementDataExtension)
    pass

class 0x1a6649ce(BaseLoadoutData):
    mThreshold: (I64, 0x0, 0x0, 0x0)
    mEventsToTrack: (List, 0x0, Embed, 0xde69c8a4)
    0x926bd12a: (String, 0x0, 0x0, 0x0)
    pass

class EventValueConstraintInfo(ListenerConstraintInfo):
    ComparisonType: (U32, 0x0, 0x0, 0x0)
    ValueRequired: (F32, 0x0, 0x0, 0x0)
    pass

class VfxFieldAttractionDefinitionData():
    Acceleration: (Embed, 0x0, 0x0, ValueFloat)
    Acceleration: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    Position: (Embed, 0x0, 0x0, ValueVector3)
    Position: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    Radius: (Embed, 0x0, 0x0, ValueFloat)
    Radius: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    pass

class UiMetricClash(UiMetricTypeI):
    ClashRoundIcon: (Hash, 0x0, 0x0, 0x0)
    ClashFrame: (Hash, 0x0, 0x0, 0x0)
    ClashRoundText: (Hash, 0x0, 0x0, 0x0)
    Team1: (Embed, 0x0, 0x0, UiClashTeam)
    Team2: (Embed, 0x0, 0x0, UiClashTeam)
    ClashFrameMirror: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x1a8a8853(ILolSpellScriptEvent):
    pass

class UiElementToggle():
    OffState: (List, 0x0, Hash, 0x0)
    OnState: (List, 0x0, Hash, 0x0)
    pass

class 0x1aaa358b(0x6ca3cfd):
    Value: (String, 0x0, 0x0, 0x0)
    pass

class 0x1aae122(0x377491e8):
    0x7863785e: (F32, 0x0, 0x0, 0x0)
    MaxOffsetDelta: (F32, 0x0, 0x0, 0x0)
    MinDistance: (F32, 0x0, 0x0, 0x0)
    MaxDistance: (F32, 0x0, 0x0, 0x0)
    pass

class TriggerOnHit(MissileTriggerSpec):
    pass

class 0x1ab4d045(0x2b00c366):
    0x2484d6c3: (Bool, 0x0, 0x0, 0x0)
    Boom: (Link, 0x0, 0x0, TftDamageSkin)
    pass

class UiPositionPolygon(UiPositionRect):
    Polygon: (List, 0x0, Vec2, 0x0)
    PolygonVertices: (List2, 0x0, Vec2, 0x0)
    pass

class TftMapShopData():
    DisplayName: (String, 0x0, 0x0, 0x0)
    pass

class TftUnitPropertyValueFloat(TftUnitPropertyValue):
    Value: (F32, 0x0, 0x0, 0x0)
    pass

class MovingTowardEnemyParametricUpdater(IFloatParametricUpdater):
    pass

class SpellRankPipsUiData():
    RankPips: (List, 0x4, Embed, SpellPipsUiData)
    RankPips: (List, 0x4, Pointer, SpellPipsUiData)
    pass

class UiSocialChatMessageTemplate():
    DateDivider: (Hash, 0x0, 0x0, 0x0)
    MessageText: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    DateSpacingUnder: (Hash, 0x0, 0x0, 0x0)
    0x7037b16a: (Hash, 0x0, 0x0, 0x0)
    DateSpacingOver: (Hash, 0x0, 0x0, 0x0)
    MessageRow: (Hash, 0x0, 0x0, 0x0)
    0x8f644cb: (Hash, 0x0, 0x0, 0x0)
    MessageBackground: (Hash, 0x0, 0x0, 0x0)
    Timestamp: (Hash, 0x0, 0x0, 0x0)
    Datestamp: (Hash, 0x0, 0x0, 0x0)
    BottomPadding: (Hash, 0x0, 0x0, 0x0)
    HitRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class HudLoadingScreenProgressBarData():
    0x37a74c29: (Bool, 0x0, 0x0, 0x0)
    0x9f3d3433: (F32, 0x0, 0x0, 0x0)
    0xb550de8d: (F32, 0x0, 0x0, 0x0)
    0xd69543e7: (F32, 0x0, 0x0, 0x0)
    0xe4a8e1a9: (F32, 0x0, 0x0, 0x0)
    pass

class AbilityResourceBarData():
    UseAnimatedSkins: (Bool, 0x0, 0x0, 0x0)
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    TextData: (Pointer, 0x0, 0x0, AbilityResourceBarTextData)
    ValueText: (Hash, 0x0, 0x0, 0x0)
    StandardTick: (Hash, 0x0, 0x0, 0x0)
    AbilityResourceBars: (Embed, 0x0, 0x0, BarTypeMap)
    AbilityResourceBars: (Pointer, 0x0, 0x0, ResourceMeterBaseData)
    pass

class FloatValueGet(DirectValueGet):
    Value: (F32, 0x0, 0x0, 0x0)
    pass

class TftItemCodexViewEntryData():
    ComponentIcon: (Hash, 0x0, 0x0, 0x0)
    ArrowIcon: (Hash, 0x0, 0x0, 0x0)
    FullItemIcon: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    FullItemNameText: (Hash, 0x0, 0x0, 0x0)
    PlusIcon: (Hash, 0x0, 0x0, 0x0)
    HoverRegion: (Hash, 0x0, 0x0, 0x0)
    HighlightIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class DirectionAim(TargetingTypeData):
    pass

class PhysicsMovement(MissileMovementSpec):
    mDrag: (F32, 0x0, 0x0, 0x0)
    mInitialSpeed: (F32, 0x0, 0x0, 0x0)
    mWallSliding: (Bool, 0x0, 0x0, 0x0)
    mWallSlidingFrictionMultiplier: (F32, 0x0, 0x0, 0x0)
    mLifetime: (F32, 0x0, 0x0, 0x0)
    pass

class SpellCalculationModified(ISpellCalculation):
    mMultiplier: (Pointer, 0x0, 0x0, ISpellCalculationPart)
    mModifiedSpellCalculation: (Hash, 0x0, 0x0, 0x0)
    mOverrideSpellLevel: (Option, 0x0, I32, 0x0)
    pass

class HudLoadingScreenCarouselData():
    HeaderTraKey: (String, 0x0, 0x0, 0x0)
    mTipType: (U8, 0x0, 0x0, 0x0)
    Image: (String, 0x0, 0x0, 0x0)
    BodyTraKey: (String, 0x0, 0x0, 0x0)
    pass

class 0x1c12183d(ITftBehaviorScriptEvent):
    pass

class BuffStackingTemplate():
    BuffAddType: (U32, 0x0, 0x0, 0x0)
    MaxStacks: (I32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    StacksToAdd: (I32, 0x0, 0x0, 0x0)
    StacksExclusive: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x1c22201c(0x51f54b8e):
    pass

class DestroyOnHitSpec(MissileBehaviorSpec):
    pass

class IFxLocation():
    Transform: (Mtx44, 0x0, 0x0, 0x0)
    pass

class HeroStatsDefinition():
    mStats: (List, 0x0, Embed, HeroStatData)
    pass

class TftArmoryBadgeDisplayData():
    Group: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x1c55e499(IScriptBlock, IBehaviorScriptBlock):
    pass

class 0x1c5e3bb6(0x2b00c366):
    0x2484d6c3: (Bool, 0x0, 0x0, 0x0)
    Tactician: (Link, 0x0, 0x0, CompanionData)
    pass

class CustomTableContainsValueBlock(IScriptBlock):
    SrcTable: (Embed, 0x0, 0x0, CustomTableGet)
    Value: (Pointer, 0x0, 0x0, IScriptValueGet)
    OutWasFound: (Embed, 0x0, 0x0, BoolTableSet)
    OutKey: (Embed, 0x0, 0x0, ScriptTableSet)
    MatchingKey: (Embed, 0x0, 0x0, ScriptTableSet)
    WasFound: (Embed, 0x0, 0x0, BoolTableSet)
    CustomTable: (Embed, 0x0, 0x0, CustomTableGet)
    pass

class CharacterQuestObjective():
    ObjectiveRewardList: (List2, 0x0, Pointer, CharacterQuestReward)
    0x42cd1140: (List2, 0x0, Hash, 0x0)
    0x856d8176: (List2, 0x0, Pointer, 0xa495afda)
    0xcbca11f6: (List2, 0x0, Pointer, CharacterQuestReward)
    0xf7c78187: (List2, 0x0, Pointer, 0xa495afda)
    ObjectiveName: (Hash, 0x0, 0x0, 0x0)
    pass

class TftBannerTable(TftBannerNode):
    Children: (List, 0x0, Embed, TftBannerTableEntry)
    pass

class MapNavGrid(MapComponent):
    RegionBoundaryConfig: (Embed, 0x0, 0x0, RegionBoundaryConfig)
    0x34ffd0bd: (Bool, 0x0, 0x0, 0x0)
    NavGridConfig: (Link, 0x0, 0x0, NavGridConfig)
    NavGridPath: (String, 0x0, 0x0, 0x0)
    pass

class SyncCircleMovement(MissileMovementSpec):
    mRotateAroundCasterFacingDirection: (Bool, 0x0, 0x0, 0x0)
    mAxisOfRotation: (U8, 0x0, 0x0, 0x0)
    mAngularVelocity: (F32, 0x0, 0x0, 0x0)
    mLifetime: (F32, 0x0, 0x0, 0x0)
    pass

class TftTrovesCelebrationThemeData():
    HighlightSegmentData: (Embed, 0x0, 0x0, TftTrovesCelebrationHighlightSegmentData)
    Scene: (Hash, 0x0, 0x0, 0x0)
    CurrencySegmentData: (Embed, 0x0, 0x0, TftTrovesCelebrationCurrencySegmentData)
    PortalSegmentData: (Embed, 0x0, 0x0, TftTrovesCelebrationChestSegmentData)
    StandardSegmentData: (Embed, 0x0, 0x0, TftTrovesCelebrationStandardSegmentData)
    UseSequencer: (Bool, 0x0, 0x0, 0x0)
    pass

class MapPlaceableName():
    PlaceableName: (String, 0x0, 0x0, 0x0)
    pass

class SequenceLocationAttachment(ISequenceLocation):
    Attachment: (String, 0x0, 0x0, 0x0)
    Object: (Embed, 0x0, 0x0, SequenceObjectSelector)
    Object: (Link, 0x0, 0x0, SequenceObjectSelector)
    pass

class AiUnitGroup():
    Buildings: (Map, String, Embed, AiBuildingConfig)
    Units: (Map, String, Embed, AiUnitConfig)
    Units: (Map, String, Pointer, AiUnitConfigBase)
    pass

class PropertyOverrideLoadable():
    OverrideSrcFolder: (File, 0x0, 0x0, 0x0)
    FilepathHash: (File, 0x0, 0x0, 0x0)
    pass

class 0x1d2ea7ed():
    MinResolution: (U32, 0x0, 0x0, 0x0)
    Scale: (F32, 0x0, 0x0, 0x0)
    pass

class TargetLaserComponentEffects():
    TowerTargetingEffectDefinition: (Embed, 0x0, 0x0, SkinCharacterDataProperties_CharacterIdleEffect)
    BeamEffectDefinition: (Embed, 0x0, 0x0, SkinCharacterDataProperties_CharacterIdleEffect)
    ChampTargetingEffectDefinition: (Embed, 0x0, 0x0, SkinCharacterDataProperties_CharacterIdleEffect)
    TowerTargetingEffect2DeathDefinition: (Embed, 0x0, 0x0, SkinCharacterDataProperties_CharacterIdleEffect)
    TargetEffectDefinition: (Embed, 0x0, 0x0, SkinCharacterDataProperties_CharacterIdleEffect)
    ShouldAlwaysTargetEnemy: (Bool, 0x0, 0x0, 0x0)
    TowerTargetingEffect2Definition: (Embed, 0x0, 0x0, SkinCharacterDataProperties_CharacterIdleEffect)
    pass

class 0x1d54119c():
    XpRequired: (U32, 0x0, 0x0, 0x0)
    BattlepassRewards: (List2, 0x0, Pointer, 0xb639bddc)
    pass

class EmotesViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    0x40c8d1c2: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    0x949bbb90: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    EmoteData: (Embed, 0x0, 0x0, EmoteItemData)
    TopRegion: (Hash, 0x0, 0x0, 0x0)
    ObjectName: (String, 0x0, 0x0, 0x0)
    EmoteSettings: (Embed, 0x0, 0x0, EmoteConfigData)
    pass

class TftTraitTrackerTraitIconData():
    HoverIcon: (Hash, 0x0, 0x0, 0x0)
    DefaultIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class TftModeData():
    TftPlaybookDefault: (Hash, 0x0, 0x0, 0x0)
    ItemTagOptions: (List, 0x0, Hash, 0x0)
    ItemTagOptions: (List2, 0x0, Hash, 0x0)
    SurrenderVoteCompleteDialogPersistSec: (F32, 0x0, 0x0, 0x0)
    0x12dc2914: (F32, 0x0, 0x0, 0x0)
    MinHealthAfterPartnerDamage: (I32, 0x0, 0x0, 0x0)
    SurrenderAfkAutoVoteThresholdSec: (F32, 0x0, 0x0, 0x0)
    FinisherLocatorName: (String, 0x0, 0x0, 0x0)
    mDefaultSetData: (Link, 0x0, 0x0, TftSetData)
    mTftMapSkinDefault: (Hash, 0x0, 0x0, 0x0)
    ActiveSets: (List, 0x0, Link, TftSetData)
    ActiveSets: (List2, 0x0, Link, TftSetData)
    TftPartnerGroupColors: (List, 0x4, Color, 0x0)
    0x3c1eafbe: (F32, 0x0, 0x0, 0x0)
    mSpectateAfterDeathPromptDelay: (F32, 0x0, 0x0, 0x0)
    mTftDamageSkinDefault: (Hash, 0x0, 0x0, 0x0)
    0x4527cab3: (Hash, 0x0, 0x0, 0x0)
    mBotLoadoutConfig: (Link, 0x0, 0x0, TftBotLoadoutConfiguration)
    mStages: (List, 0x0, Link, TftStageData)
    mClickDistanceDiv: (F32, 0x0, 0x0, 0x0)
    mClickDistanceMul: (F32, 0x0, 0x0, 0x0)
    NumRoundsLossForgiven: (U32, 0x0, 0x0, 0x0)
    SurrenderRetryDelaySec: (F32, 0x0, 0x0, 0x0)
    TftZoomSkinDefault: (Hash, 0x0, 0x0, 0x0)
    mTutorialTftCompanion: (Hash, 0x0, 0x0, 0x0)
    SurrenderVoteDurationSec: (F32, 0x0, 0x0, 0x0)
    mDragData: (Embed, 0x0, 0x0, TftDragData)
    mMobileCharacterScale: (F32, 0x0, 0x0, 0x0)
    mDefaultTftCompanion: (Hash, 0x0, 0x0, 0x0)
    mDragBlendTime: (F32, 0x0, 0x0, 0x0)
    mMobileDragData: (Embed, 0x0, 0x0, TftDragData)
    EventSetData: (Link, 0x0, 0x0, TftSetData)
    0xd0c165ba: (Hash, 0x0, 0x0, 0x0)
    mClickTimeMul: (F32, 0x0, 0x0, 0x0)
    DefaultSetData: (Link, 0x0, 0x0, TftSetData)
    GroupSurrenderVoterCount: (U32, 0x0, 0x0, 0x0)
    MinHealthAfterLossForgiven: (I32, 0x0, 0x0, 0x0)
    EncounterTagOptions: (List, 0x0, Hash, 0x0)
    SurrenderVoteCompleteEliminateDelaySec: (F32, 0x0, 0x0, 0x0)
    HexToRangeMap: (List, 0x0, Embed, TftHexToRangeTranslation)
    mClickDistanceExp: (F32, 0x0, 0x0, 0x0)
    MemoryReportMinimalSet: (Link, 0x0, 0x0, TftSetData)
    mTftDamageSkinScriptDefault: (String, 0x0, 0x0, 0x0)
    pass

class 0x1d786017(ILolSpellScriptEvent):
    pass

class HudTooltipAdjustments():
    TopHrYPostAdjustment: (I32, 0x0, 0x0, 0x0)
    BottomYPaddingAdjustment: (I32, 0x0, 0x0, 0x0)
    TitleYAdjustment: (I32, 0x0, 0x0, 0x0)
    TopHrYPreAdjustment: (I32, 0x0, 0x0, 0x0)
    BottomHrYPreAdjustment: (I32, 0x0, 0x0, 0x0)
    BottomHrYPostAdjustment: (I32, 0x0, 0x0, 0x0)
    pass

class VfxSoftParticleDefinitionData():
    DeltaIn: (F32, 0x0, 0x0, 0x0)
    DepthFadeInBegin: (F32, 0x0, 0x0, 0x0)
    DepthFadeInOneOverWidth: (F32, 0x0, 0x0, 0x0)
    UsesSoftParticles: (Bool, 0x0, 0x0, 0x0)
    BeginIn: (F32, 0x0, 0x0, 0x0)
    DeltaOut: (F32, 0x0, 0x0, 0x0)
    DepthFadeOutOneOverWidth: (F32, 0x0, 0x0, 0x0)
    DepthFadeOutBegin: (F32, 0x0, 0x0, 0x0)
    BeginOut: (F32, 0x0, 0x0, 0x0)
    pass

class 0x1db6d987(ILogicBoolDriver):
    VisibilityController: (Link, 0x0, 0x0, IMapVisibilityController)
    pass

class ContextualActionTriggerEvent(IContextualAction):
    pass

class RsTableGet(RsValueGet):
    pass

class AvatarVarsTable(ScriptTable):
    pass

class PerkScript():
    mSpellScriptName: (String, 0x0, 0x0, 0x0)
    mSpellScript: (Pointer, 0x0, 0x0, LolSpellScript)
    mSpellScriptData: (Embed, 0x0, 0x0, PerkScriptData)
    pass

class 0x1ddfbeeb(0x377491e8):
    pass

class VfxPrimitiveCubeProjection(VfxPrimitiveProjectionBase):
    pass

class AnnouncementDefinitionData():
    CommonElements: (Hash, 0x0, 0x0, 0x0)
    MakeLowerPriorityEventsObsolete: (Bool, 0x0, 0x0, 0x0)
    TextKeyFallback: (String, 0x0, 0x0, 0x0)
    AlliedElements: (Hash, 0x0, 0x0, 0x0)
    CanBeMadeObsolete: (Bool, 0x0, 0x0, 0x0)
    TextKey: (String, 0x0, 0x0, 0x0)
    SoundKey: (String, 0x0, 0x0, 0x0)
    ChatMessageKey: (String, 0x0, 0x0, 0x0)
    Priority: (U16, 0x0, 0x0, 0x0)
    SpectatorSoundKey: (String, 0x0, 0x0, 0x0)
    Style: (Link, 0x0, 0x0, AnnouncementStyleBasic)
    ChatMessageKeyFallback: (String, 0x0, 0x0, 0x0)
    EnemyElements: (Hash, 0x0, 0x0, 0x0)
    pass

class BehaviorDebugPrintToChatBlock(DebugPrintToChatBlock, IBehaviorScriptBlock):
    ExecutePrint: (Pointer, 0x0, 0x0, BoolGet)
    ExecutePrint: (Pointer, 0x0, 0x0, IBoolGet)
    ReturnSuccess: (Pointer, 0x0, 0x0, BoolGet)
    ReturnSuccess: (Pointer, 0x0, 0x0, IBoolGet)
    ChatBlock: (Embed, 0x0, 0x0, DebugPrintToChatBlock)
    pass

class HudHealthBarProgressiveTickData():
    HealthPerTick: (F32, 0x0, 0x0, 0x0)
    MicroTickPerTickData: (List, 0x0, Embed, MicroTicksPerTickData)
    pass

class HealthBarTickStyleHero(HealthBarTickStyleBase):
    HealthPerstandardTick: (F32, 0x0, 0x0, 0x0)
    MicroTick: (Hash, 0x0, 0x0, 0x0)
    MicroTickPerStandardTickData: (List, 0x0, Embed, MicroTicksPerStandardTickData)
    StandardTick: (Hash, 0x0, 0x0, 0x0)
    pass

class MasteryData():
    Texture: (String, 0x0, 0x0, 0x0)
    LevelTraKey: (String, 0x0, 0x0, 0x0)
    TextureMini: (String, 0x0, 0x0, 0x0)
    DetailsTraKey: (String, 0x0, 0x0, 0x0)
    pass

class ForEachInCustomTableBlock(IScriptBlock, ILoopScriptBlock):
    Sequence: (Embed, 0x0, 0x0, ScriptSequence)
    SortedByKeys: (Bool, 0x0, 0x0, 0x0)
    SortedByKeys: (Pointer, 0x0, 0x0, IBoolGet)
    Table: (Embed, 0x0, 0x0, CustomTableGet)
    DestKey: (Embed, 0x0, 0x0, ScriptTableSet)
    OutKey: (Embed, 0x0, 0x0, ScriptTableSet)
    OutValue: (Embed, 0x0, 0x0, ScriptTableSet)
    DestValue: (Embed, 0x0, 0x0, ScriptTableSet)
    CustomTable: (Embed, 0x0, 0x0, CustomTableGet)
    pass

class GameModeContent():
    mModeName: (Hash, 0x0, 0x0, 0x0)
    mChampions: (List, 0x0, Link, Champion)
    mGameMutator: (Link, 0x0, 0x0, GameMutatorExpansions)
    mGameMode: (U32, 0x0, 0x0, 0x0)
    pass

class SummonerEmoteSettings():
    mFirstBlood: (Link, 0x0, 0x0, SummonerEmote)
    mAce: (Link, 0x0, 0x0, SummonerEmote)
    pass

class FloatPerSpellLevel():
    mValueType: (U32, 0x0, 0x0, 0x0)
    mPerLevelValues: (List, 0x6, F32, 0x0)
    pass

class GetFxObjectDynamicMaterialFloatDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    mKeyName: (String, 0x0, 0x0, 0x0)
    pass

class FxLocationTftLocator(IFxLocation, ISequenceLocation):
    LocationName: (String, 0x0, 0x0, 0x0)
    pass

class UiAbilityPromptAnimData():
    PulseInterval: (F32, 0x0, 0x0, 0x0)
    PulseTime: (F32, 0x0, 0x0, 0x0)
    PulseNativeOffset: (Vec2, 0x0, 0x0, 0x0)
    PulseEndColor: (Color, 0x0, 0x0, 0x0)
    PulseStartColor: (Color, 0x0, 0x0, 0x0)
    pass

class 0x1eb9b37a(ILolSpellScriptEvent):
    pass

class CooldownMultiplierCalculationPart(IGameCalculationPart, ISpellCalculationPart):
    pass

class OptionTemplateSlider(IOptionTemplate):
    SliderBarDefinition: (Hash, 0x0, 0x0, 0x0)
    ValueElement: (Hash, 0x0, 0x0, 0x0)
    LabelElement: (Hash, 0x0, 0x0, 0x0)
    pass

class MinimapData():
    mCustomIcons: (Map, Hash, Embed, MinimapIcon)
    mIcons: (Map, U8, Embed, MinimapIcon)
    BehaviorSets: (Map, Hash, Link, MinimapIconBehaviorSet)
    mUseOldData: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x1f3ce132(0x26d26471):
    Duration: (F32, 0x0, 0x0, 0x0)
    pass

class MinimapIcon():
    mBaseTexture: (Embed, 0x0, 0x0, MinimapIconTextureData)
    mRelativeTeams: (Bool, 0x0, 0x0, 0x0)
    mTeamTextures: (Map, U8, Embed, MinimapIconTextureData)
    mSize: (Vec2, 0x0, 0x0, 0x0)
    mTeamColors: (Map, U8, Embed, MinimapIconColorData)
    mBaseColor: (Embed, 0x0, 0x0, MinimapIconColorData)
    mMinScale: (F32, 0x0, 0x0, 0x0)
    mMaxScale: (F32, 0x0, 0x0, 0x0)
    pass

class PfxComplexEmitterDefinitionData():
    FluidDynamicsDefinition: (Pointer, 0x0, 0x0, 0xdb7c04f8)
    FieldCollectionDefinition: (Embed, 0x0, 0x0, PfxFieldCollectionDefinitionData)
    pass

class 0x1f8480d8(IScriptBlock):
    InputString: (Pointer, 0x0, 0x0, IStringGet)
    FoundIndex: (Embed, 0x0, 0x0, IntTableSet)
    TargetString: (Pointer, 0x0, 0x0, IStringGet)
    pass

class 0x1f8db674(MissileBehaviorSpec):
    pass

class TftBannerIconData():
    Button: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    NewPip: (Embed, 0x0, 0x0, 0x6241da2)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class TargetOrLocation(TargetingTypeData):
    0xfb5bbd7: (Bool, 0x0, 0x0, 0x0)
    pass

class SpellChoiceTemplate():
    Description: (Hash, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    Title: (Hash, 0x0, 0x0, 0x0)
    TopLevelGroup: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class GameObject(UObject):
    pass

class VfxBeamDefinitionData():
    mSegments: (I32, 0x0, 0x0, 0x0)
    mTrailMode: (U32, 0x0, 0x0, 0x0)
    mTrailMode: (U8, 0x0, 0x0, 0x0)
    mBirthTilingSize: (Embed, 0x0, 0x0, ValueVector3)
    mIsColorBindedWithDistance: (Bool, 0x0, 0x0, 0x0)
    mMode: (U32, 0x0, 0x0, 0x0)
    mMode: (U8, 0x0, 0x0, 0x0)
    mAnimatedColorWithDistance: (Embed, 0x0, 0x0, ValueColor)
    mLocalSpaceTargetOffset: (Vec3, 0x0, 0x0, 0x0)
    mLocalSpaceSourceOffset: (Vec3, 0x0, 0x0, 0x0)
    pass

class PlayerPositionDynamicMaterialDriver(IDynamicMaterialDriver, ILogicDriver):
    pass

class TftBannerNode():
    Id: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class HudItemShopItemDetailsClickDataDefinition():
    HoverIconDefinition: (Hash, 0x0, 0x0, 0x0)
    ClickRegionDefinition: (Hash, 0x0, 0x0, 0x0)
    ItemBriefTextDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class ExponentSubPartsCalculationPart(IGameCalculationPart):
    Part1: (Pointer, 0x0, 0x0, IGameCalculationPart)
    Part2: (Pointer, 0x0, 0x0, IGameCalculationPart)
    pass

class UiSceneData():
    mName: (String, 0x0, 0x0, 0x0)
    mHandleInputDuringPause: (Bool, 0x0, 0x0, 0x0)
    mHealthBar: (Bool, 0x0, 0x0, 0x0)
    Enabled: (Bool, 0x0, 0x0, 0x0)
    HandleInputDuringPause: (Bool, 0x0, 0x0, 0x0)
    0x49d8f2c4: (Bool, 0x0, 0x0, 0x0)
    mEnabled: (Bool, 0x0, 0x0, 0x0)
    Layer: (U32, 0x0, 0x0, 0x0)
    mLayer: (U32, 0x0, 0x0, 0x0)
    SceneTransitionOut: (Pointer, 0x0, 0x0, SceneBaseTransitionData)
    SceneTransitionIn: (Pointer, 0x0, 0x0, SceneBaseTransitionData)
    Name: (String, 0x0, 0x0, 0x0)
    mParentScene: (Link, 0x0, 0x0, UiSceneData)
    ParentScene: (Link, 0x0, 0x0, UiSceneData)
    InheritScissoring: (Bool, 0x0, 0x0, 0x0)
    pass

class LobbyPlayerData():
    SummonerIcon: (Hash, 0x0, 0x0, 0x0)
    ArenaSkinIcon: (Hash, 0x0, 0x0, 0x0)
    PartyLeaderIcon: (Hash, 0x0, 0x0, 0x0)
    LoadoutsButton: (Hash, 0x0, 0x0, 0x0)
    CustomButton: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    LoadoutsFrame: (Hash, 0x0, 0x0, 0x0)
    0x7ec3f9ad: (Hash, 0x0, 0x0, 0x0)
    SummonerIconFrame: (Hash, 0x0, 0x0, 0x0)
    RandomLoadoutButton: (Hash, 0x0, 0x0, 0x0)
    RankText: (Hash, 0x0, 0x0, 0x0)
    LittleLegendIcon: (Hash, 0x0, 0x0, 0x0)
    EditButton: (Hash, 0x0, 0x0, 0x0)
    CustomButtonIcon: (Hash, 0x0, 0x0, 0x0)
    FrameRanked: (Hash, 0x0, 0x0, 0x0)
    SwapButton: (Hash, 0x0, 0x0, 0x0)
    NameText: (Hash, 0x0, 0x0, 0x0)
    UseLeaderControlsModal: (Bool, 0x0, 0x0, 0x0)
    InviteButton: (Hash, 0x0, 0x0, 0x0)
    DamageSkinIcon: (Hash, 0x0, 0x0, 0x0)
    RankTextLine2: (Hash, 0x0, 0x0, 0x0)
    FrameUnranked: (Hash, 0x0, 0x0, 0x0)
    EmptySlotButton: (Hash, 0x0, 0x0, 0x0)
    pass

class ChampSelectCharacterData():
    Record: (Embed, 0x0, 0x0, ChampSelectCharacterRecord)
    SkinData: (List, 0x0, Embed, ChampSelectCharacterSkinData)
    RootSkin: (Embed, 0x0, 0x0, ChampSelectCharacterSkinData)
    pass

class CustomShaderDef(IShaderDef):
    ObjectPath: (String, 0x0, 0x0, 0x0)
    pass

class OffscreenKilledEnemyPipSource(IPictureInPictureSource):
    TimeToShowSeconds: (F32, 0x0, 0x0, 0x0)
    pass

class Scene():
    mName: (String, 0x0, 0x0, 0x0)
    mEnabled: (Bool, 0x0, 0x0, 0x0)
    mDynamic: (Bool, 0x0, 0x0, 0x0)
    mLayer: (U32, 0x0, 0x0, 0x0)
    mParentScene: (Link, 0x0, 0x0, Scene)
    mAtlased: (Bool, 0x0, 0x0, 0x0)
    pass

class CooldownGemUiData():
    AllyGem: (Hash, 0x0, 0x0, 0x0)
    EnemyGem: (Hash, 0x0, 0x0, 0x0)
    GemBackground: (Hash, 0x0, 0x0, 0x0)
    CooldownEffects: (Embed, 0x0, 0x0, CooldownEffectUiData)
    pass

class HeroFloatingInfoBorderData():
    ResistBorders: (Pointer, 0x0, 0x0, HeroFloatingInfoResistBorderData)
    HasAttachedAllyBorder: (Pointer, 0x0, 0x0, HeroFloatingInfoBorderTypeData)
    LevelTextColorSelfColorblind: (Color, 0x0, 0x0, 0x0)
    LevelTextColorEnemy: (Color, 0x0, 0x0, 0x0)
    DefenseModifierIcons: (Pointer, 0x0, 0x0, HeroFloatingInfoBorderDefenseIconData)
    LevelText: (Hash, 0x0, 0x0, 0x0)
    InvulnerableBorder: (Pointer, 0x0, 0x0, HeroFloatingInfoBorderTypeData)
    LevelTextColorSelf: (Color, 0x0, 0x0, 0x0)
    DefaultBorder: (Embed, 0x0, 0x0, HeroFloatingInfoBorderTypeData)
    ExecutableBorder: (Pointer, 0x0, 0x0, HeroFloatingInfoBorderTypeData)
    SpellShieldBorder: (Pointer, 0x0, 0x0, HeroFloatingInfoBorderTypeData)
    LevelTextColorAlly: (Color, 0x0, 0x0, 0x0)
    AdditionalStatusIcons: (Map, U32, Hash, 0x0)
    pass

class OffScreenPoiConfigData():
    DownscaleBezier: (Vec4, 0x0, 0x0, 0x0)
    BezierMaxSize: (F32, 0x0, 0x0, 0x0)
    DownscaleTime: (F32, 0x0, 0x0, 0x0)
    OffscreenCamps: (List, 0x0, Embed, OffScreenPoiCamp)
    OffscreenPings: (List, 0x0, Embed, OffScreenPoiPing)
    IntroBezier: (Vec4, 0x0, 0x0, 0x0)
    EdgeBuffer: (U32, 0x0, 0x0, 0x0)
    OutroTime: (F32, 0x0, 0x0, 0x0)
    MaxDisplayedPoi: (U8, 0x0, 0x0, 0x0)
    IntroTime: (F32, 0x0, 0x0, 0x0)
    pass

class TftPassAsset():
    IconTexturePath: (String, 0x0, 0x0, 0x0)
    InternalName: (String, 0x0, 0x0, 0x0)
    IconNeedsFrame: (Bool, 0x0, 0x0, 0x0)
    pass

class ReturnToCasterOnMovementComplete(MissileBehaviorSpec):
    mPreserveSpeed: (Bool, 0x0, 0x0, 0x0)
    mOverrideSpec: (Pointer, 0x0, 0x0, MissileMovementSpec)
    pass

class AttackableUnit(GameObject):
    pass

class UiButtonSoundEvents():
    RollOutEvent: (String, 0x0, 0x0, 0x0)
    MouseDownOnInactive: (String, 0x0, 0x0, 0x0)
    MouseUpEvent: (String, 0x0, 0x0, 0x0)
    RolloverEvent: (String, 0x0, 0x0, 0x0)
    MouseUpOnInactive: (String, 0x0, 0x0, 0x0)
    MouseDownEvent: (String, 0x0, 0x0, 0x0)
    pass

class BuffModifier():
    DescriptionAppendPriority: (U32, 0x0, 0x0, 0x0)
    DescriptionAppendTra: (String, 0x0, 0x0, 0x0)
    ModifierId: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x209fa685():
    UiBar: (Hash, 0x0, 0x0, 0x0)
    RewardSoundEvent: (String, 0x0, 0x0, 0x0)
    UiElements: (List2, 0x0, Hash, 0x0)
    Points: (U32, 0x0, 0x0, 0x0)
    0xcebbf565: (Hash, 0x0, 0x0, 0x0)
    pass

class IResource():
    pass

class 0x20b66cd9():
    0x6eb7250f: (List2, 0x0, Embed, 0x50714aa1)
    Planning: (Embed, 0x0, 0x0, 0x12b69e95)
    pass

class ElementGroupFramedData(ElementGroupData):
    FrameElement: (Link, 0x0, 0x0, IconElementData)
    pass

class UiLevelUp():
    ButtonsScene: (Hash, 0x0, 0x0, 0x0)
    ButtonEasingData: (Embed, 0x0, 0x0, UiLevelUpButtonEasingData)
    Spells: (List, 0x4, Embed, SpellLevelUpUiData)
    Spells: (List, 0x4, Pointer, SpellLevelUpUiData)
    FxInScene: (Hash, 0x0, 0x0, 0x0)
    Title: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x20fd5854(IBehaviorScriptBlock):
    pass

class FxActionContinue(IFxAction):
    pass

class IEnvironmentShadingModel(0x38a77cab, IX3dShadingModel):
    pass

class ArenaOwnerLevelParametricUpdater(IFloatParametricUpdater):
    pass

class TftTraitInfoCard():
    0x3eedfe4f: (Bool, 0x0, 0x0, 0x0)
    UnitGridLink: (Hash, 0x0, 0x0, 0x0)
    TraitName: (Hash, 0x0, 0x0, 0x0)
    CardScene: (Hash, 0x0, 0x0, 0x0)
    0x7b313643: (Bool, 0x0, 0x0, 0x0)
    PortraitRegion: (Hash, 0x0, 0x0, 0x0)
    0x7f4a4a4: (Bool, 0x0, 0x0, 0x0)
    CardSceneAnchor: (Hash, 0x0, 0x0, 0x0)
    TraitIcon: (Hash, 0x0, 0x0, 0x0)
    ResizableBackdrop: (Hash, 0x0, 0x0, 0x0)
    HorizontalRule: (Hash, 0x0, 0x0, 0x0)
    TraitDescription: (Hash, 0x0, 0x0, 0x0)
    HudTraitUnitSlotTemplate: (Embed, 0x0, 0x0, TftHudTraitUnitSlotData)
    TraitFooterPadding: (Hash, 0x0, 0x0, 0x0)
    TraitFooter: (Hash, 0x0, 0x0, 0x0)
    HudTraitUnitSlotBorders: (Embed, 0x0, 0x0, TftHudTraitUnitSlotBorders)
    pass

class ParallelClipData(ClipBaseData):
    mClipNameList: (List, 0x0, Hash, 0x0)
    mClipIndexList: (List, 0x0, U32, 0x0)
    pass

class ViewControllerListFilter_Not(ViewControllerListFilterI):
    Filter: (Pointer, 0x0, 0x0, ViewControllerListFilterI)
    pass

class VfxPrimitiveTrailBase(VfxPrimitiveBase):
    mTrail: (Embed, 0x0, 0x0, VfxTrailDefinitionData)
    pass

class 0x21a128f8(IGameModeConfig):
    0x47da838e: (Map, U32, Bool, 0x0)
    pass

class SpellEvolutionUiData():
    Button: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class DynamicMaterialTextureSwapOption():
    TextureName: (String, 0x0, 0x0, 0x0)
    Driver: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    Driver: (Pointer, 0x0, 0x0, IDynamicMaterialBoolDriver)
    pass

class TftArmoryActionButtonData():
    NumericTextDefault: (I32, 0x0, 0x0, 0x0)
    ActionButton: (Hash, 0x0, 0x0, 0x0)
    DynamicNumericTextDisabledColor: (Color, 0x0, 0x0, 0x0)
    0x4ca9e6c0: (Color, 0x0, 0x0, 0x0)
    DynamicNumericTextTra: (String, 0x0, 0x0, 0x0)
    DynamicNumericText: (Hash, 0x0, 0x0, 0x0)
    0xabef78e0: (Color, 0x0, 0x0, 0x0)
    NumericText: (Hash, 0x0, 0x0, 0x0)
    0xca0ffb2d: (Hash, 0x0, 0x0, 0x0)
    DynamicNumericTextColor: (Color, 0x0, 0x0, 0x0)
    IsActiveByDefault: (Bool, 0x0, 0x0, 0x0)
    DisableOnAction: (Bool, 0x0, 0x0, 0x0)
    pass

class ICcBehaviorData():
    pass

class SpellSlotDetailedUiDefinition(SpellSlotPassiveUiDefinition):
    AmmoFx: (Hash, 0x0, 0x0, 0x0)
    AmmoBg: (Hash, 0x0, 0x0, 0x0)
    CostBg: (Hash, 0x0, 0x0, 0x0)
    TimerBorderBg: (Hash, 0x0, 0x0, 0x0)
    Hotkey: (Hash, 0x0, 0x0, 0x0)
    TimerBorderFx: (Hash, 0x0, 0x0, 0x0)
    HotKeyBg: (Hash, 0x0, 0x0, 0x0)
    ToggleFx: (Hash, 0x0, 0x0, 0x0)
    Ammo: (Hash, 0x0, 0x0, 0x0)
    ResetFlashFxAttention: (Hash, 0x0, 0x0, 0x0)
    TimerBarFill: (Hash, 0x0, 0x0, 0x0)
    OverlayOom: (Hash, 0x0, 0x0, 0x0)
    OverlayCced: (Hash, 0x0, 0x0, 0x0)
    TimerBarBg: (Hash, 0x0, 0x0, 0x0)
    TimerBarFx: (Hash, 0x0, 0x0, 0x0)
    ResetFlashFx: (Hash, 0x0, 0x0, 0x0)
    BuffTimer: (Pointer, 0x0, 0x0, SpellSlotBuffTimerData)
    Cost: (Hash, 0x0, 0x0, 0x0)
    AmmoText: (Hash, 0x0, 0x0, 0x0)
    CooldownGem: (Pointer, 0x0, 0x0, CooldownGemUiData)
    pass

class TftMissionList():
    Missions: (List2, 0x0, String, 0x0)
    pass

class ItemAdviceAttribute():
    mAttribute: (String, 0x0, 0x0, 0x0)
    0xb1891df6: (String, 0x0, 0x0, 0x0)
    pass

class MapPerInstanceInfo():
    ShadowMapUvScaleAndBias: (Vec4, 0x0, 0x0, 0x0)
    EnvironmentShIrradiance: (Embed, 0x0, 0x0, ShData)
    ShadowMapPath: (String, 0x0, 0x0, 0x0)
    pass

class GetTurretBlock(IScriptBlock):
    Lane: (Pointer, 0x0, 0x0, IIntGet)
    Team: (Pointer, 0x0, 0x0, IIntGet)
    TurretIndex: (Pointer, 0x0, 0x0, IIntGet)
    pass

class ScriptTableGet(IScriptValueGet):
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Var: (Hash, 0x0, 0x0, 0x0)
    Var: (String, 0x0, 0x0, 0x0)
    pass

class UiAssetElementData(BaseElementData):
    pass

class TftItemPanelViewController(ViewController):
    SlotRegions: (List, 0xa, Hash, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    PanelScene: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    SlotTemplate: (Embed, 0x0, 0x0, TftItemSlotDisplayTemplate)
    pass

class IContextualConditionSpell(IContextualCondition):
    pass

class VerticalFacingFaceTarget(VerticalFacingType):
    pass

class GetNextBuildingInLaneBlock(IScriptBlock):
    RelativeIndex: (Pointer, 0x0, 0x0, IIntGet)
    pass

class OffScreenPoiCamp():
    TextField: (U8, 0x0, 0x0, 0x0)
    ShowIfOnScreen: (Bool, 0x0, 0x0, 0x0)
    MaxDistanceFromCenterOfScreen: (U32, 0x0, 0x0, 0x0)
    ShowDistance: (Bool, 0x0, 0x0, 0x0)
    AnchorTo: (U8, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    DurationSecs: (F32, 0x0, 0x0, 0x0)
    pass

class FloatArrayTableSet(ScriptTableSet):
    pass

class ContextualRule():
    mConditions: (List, 0x0, Pointer, IContextualCondition)
    mAnimationAction: (Pointer, 0x0, 0x0, IContextualAction)
    mAnimationAction: (Pointer, 0x0, 0x0, ContextualActionPlayAnimation)
    mOverrideCacCooldown: (Bool, 0x0, 0x0, 0x0)
    mConditionRelationship: (U32, 0x0, 0x0, 0x0)
    CanStompSelf: (Bool, 0x0, 0x0, 0x0)
    StompLowerPriority: (Bool, 0x0, 0x0, 0x0)
    CooldownModifications: (Pointer, 0x0, 0x0, ContextualActionCooldownModifications)
    ChanceWeight: (F32, 0x0, 0x0, 0x0)
    mTriggerEventAction: (Pointer, 0x0, 0x0, ContextualActionTriggerEvent)
    mAudioAction: (Pointer, 0x0, 0x0, IContextualAction)
    mAudioAction: (Pointer, 0x0, 0x0, ContextualActionPlayAudio)
    mPriority: (Option, 0x0, I32, 0x0)
    mPriority: (Option, 0x0, U32, 0x0)
    pass

class LerpVec4LogicDriver(ILogicDriver):
    TurnOffTimeSec: (F32, 0x0, 0x0, 0x0)
    OffValue: (Vec4, 0x0, 0x0, 0x0)
    TurnOnTimeSec: (F32, 0x0, 0x0, 0x0)
    OnValue: (Vec4, 0x0, 0x0, 0x0)
    BoolDriver: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    pass

class 0x22d93e23(0x85ec5cc):
    pass

class 0x22dd5ebf():
    0xd9306080: (Embed, 0x0, 0x0, 0xdc24bc6f)
    pass

class RegionSettings():
    mContentTypeAllowedSettings: (Map, Hash, Embed, RegionsThatAllowContent)
    pass

class FloatTextFormattingData():
    DisableHorizontalReverse: (Bool, 0x0, 0x0, 0x0)
    VerticalAlignment: (U32, 0x0, 0x0, 0x0)
    VerticalAlignment: (U8, 0x0, 0x0, 0x0)
    CombinableTextShowCrit: (Bool, 0x0, 0x0, 0x0)
    RandomStartOffsetMaxY: (F32, 0x0, 0x0, 0x0)
    RandomStartOffsetMaxX: (F32, 0x0, 0x0, 0x0)
    IgnoreCombineRules: (Bool, 0x0, 0x0, 0x0)
    MinYVelocity: (F32, 0x0, 0x0, 0x0)
    Disabled: (Bool, 0x0, 0x0, 0x0)
    RelativeOffsetMin: (F32, 0x0, 0x0, 0x0)
    CombinableCounterDisplay: (Bool, 0x0, 0x0, 0x0)
    CombinableCounterCategory: (I32, 0x0, 0x0, 0x0)
    OffsetByBoundingBox: (Bool, 0x0, 0x0, 0x0)
    MinScale: (F32, 0x0, 0x0, 0x0)
    RelativeOffsetMax: (F32, 0x0, 0x0, 0x0)
    GrowthYScalar: (F32, 0x0, 0x0, 0x0)
    OverwritePreviousNumber: (Bool, 0x0, 0x0, 0x0)
    MaxInstances: (I32, 0x0, 0x0, 0x0)
    ExtendTimeOnNewDamage: (F32, 0x0, 0x0, 0x0)
    RefreshExisting: (Bool, 0x0, 0x0, 0x0)
    ContinualForceYBase: (F32, 0x0, 0x0, 0x0)
    MinXVelocity: (F32, 0x0, 0x0, 0x0)
    ContinualForceXBase: (F32, 0x0, 0x0, 0x0)
    Scale: (F32, 0x0, 0x0, 0x0)
    mFontDescription: (Link, 0x0, 0x0, GameFontDescription)
    HangTime: (F32, 0x0, 0x0, 0x0)
    CombinableNumberFormat: (String, 0x0, 0x0, 0x0)
    Priority: (I32, 0x0, 0x0, 0x0)
    MaxXVelocity: (F32, 0x0, 0x0, 0x0)
    MaxLifeTime: (F32, 0x0, 0x0, 0x0)
    RandomStartOffsetMinY: (F32, 0x0, 0x0, 0x0)
    RandomStartOffsetMinX: (F32, 0x0, 0x0, 0x0)
    ShrinkTime: (F32, 0x0, 0x0, 0x0)
    MaxScale: (F32, 0x0, 0x0, 0x0)
    ContinualForceY: (F32, 0x0, 0x0, 0x0)
    ShrinkScale: (F32, 0x0, 0x0, 0x0)
    ContinualForceX: (F32, 0x0, 0x0, 0x0)
    StartOffsetX: (F32, 0x0, 0x0, 0x0)
    StartOffsetY: (F32, 0x0, 0x0, 0x0)
    MomentumFromHit: (Bool, 0x0, 0x0, 0x0)
    IsAnimated: (Bool, 0x0, 0x0, 0x0)
    MaxYVelocity: (F32, 0x0, 0x0, 0x0)
    AlternateRightLeft: (Bool, 0x0, 0x0, 0x0)
    DecayDelay: (F32, 0x0, 0x0, 0x0)
    Interval: (F32, 0x0, 0x0, 0x0)
    AttachToHealthBar: (Bool, 0x0, 0x0, 0x0)
    Decay: (F32, 0x0, 0x0, 0x0)
    DisableVerticalReverse: (Bool, 0x0, 0x0, 0x0)
    GrowthXScalar: (F32, 0x0, 0x0, 0x0)
    Height: (F32, 0x0, 0x0, 0x0)
    FontName: (String, 0x0, 0x0, 0x0)
    FollowSource: (Bool, 0x0, 0x0, 0x0)
    mTypeName: (Hash, 0x0, 0x0, 0x0)
    CombinableNegativeNumberFormat: (String, 0x0, 0x0, 0x0)
    ScrollSpeed: (F32, 0x0, 0x0, 0x0)
    ColorOffsetB: (I32, 0x0, 0x0, 0x0)
    ColorOffsetG: (I32, 0x0, 0x0, 0x0)
    IgnoreQueue: (Bool, 0x0, 0x0, 0x0)
    ColorOffsetR: (I32, 0x0, 0x0, 0x0)
    HorizontalAlignment: (U32, 0x0, 0x0, 0x0)
    HorizontalAlignment: (U8, 0x0, 0x0, 0x0)
    Icons: (List, 0x0, Embed, FloatTextIconData)
    FillPattern: (String, 0x0, 0x0, 0x0)
    pass

class MapPointLight(MapStaticPointLightBase, MapPlaceable, MapPointLightBase):
    OverrideCastStaticShadows: (Option, 0x0, Bool, 0x0)
    IntensityScale: (F32, 0x0, 0x0, 0x0)
    Type: (Link, 0x0, 0x0, MapPointLightType)
    OverrideUseSpecular: (Option, 0x0, Bool, 0x0)
    RadiusScale: (F32, 0x0, 0x0, 0x0)
    pass

class ExtendedSpellSlotIntDriver(ILogicIntDriver):
    pass

class 0x22fa35f4(ViewController):
    MythicTokenButton: (Hash, 0x0, 0x0, 0x0)
    TftBannerIconData: (Embed, 0x0, 0x0, TftBannerIconData)
    Scene: (Hash, 0x0, 0x0, 0x0)
    BannerList: (Hash, 0x0, 0x0, 0x0)
    SubtitleText: (Hash, 0x0, 0x0, 0x0)
    ActiveBannerIcon: (Hash, 0x0, 0x0, 0x0)
    MoreInfoButton: (Hash, 0x0, 0x0, 0x0)
    Roll1Button: (Hash, 0x0, 0x0, 0x0)
    Roll10Button: (Hash, 0x0, 0x0, 0x0)
    MythicTokenText: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class ElementDataI():
    mName: (String, 0x0, 0x0, 0x0)
    mScene: (Link, 0x0, 0x0, SceneData)
    pass

class FxSfxBeamEvent():
    EventName: (String, 0x0, 0x0, 0x0)
    AudioSource: (Embed, 0x0, 0x0, FxObjectSelector)
    UseCharacterTags: (Bool, 0x0, 0x0, 0x0)
    pass

class TftMobileLoginData():
    Scene: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    RegionalLogoMapping: (Map, U32, Hash, 0x0)
    UsernameText: (Hash, 0x0, 0x0, 0x0)
    VnLogo: (Hash, 0x0, 0x0, 0x0)
    StatusText: (Hash, 0x0, 0x0, 0x0)
    PasswordText: (Hash, 0x0, 0x0, 0x0)
    TwLogo: (Hash, 0x0, 0x0, 0x0)
    DefaultLogo: (Hash, 0x0, 0x0, 0x0)
    pass

class WallSlidingPrototype(MissileBehaviorSpec):
    ScanWidthOverride: (F32, 0x0, 0x0, 0x0)
    mMinimumGapBetweenTerrainWalls: (F32, 0x0, 0x0, 0x0)
    mFrictionMultiplier: (F32, 0x0, 0x0, 0x0)
    pass

class HudTooltipDisplayData():
    mTooltipTransitionOut: (Embed, 0x0, 0x0, HudMenuTransitionData)
    DefaultAdjustments: (Embed, 0x0, 0x0, HudTooltipAdjustments)
    mTooltipTransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    0xc67e4655: (U8, 0x0, 0x0, 0x0)
    PerLocaleAdjustments: (Map, String, Embed, HudTooltipAdjustments)
    pass

class 0x2373fc78(0xa24429bf):
    BoneName: (String, 0x0, 0x0, 0x0)
    EffectKey: (String, 0x0, 0x0, 0x0)
    pass

class 0x23b2b9a1(TargetingTypeData):
    pass

class 0x23d5c391(IScriptBlock, IBehaviorScriptBlock):
    Lane: (U16, 0x0, 0x0, 0x0)
    pass

class 0x23d6622f(ISequenceActionInstance):
    pass

class CharacterRecord():
    0x104d2294: (Bool, 0x0, 0x0, 0x0)
    DisguiseMinimapIconOverride: (String, 0x0, 0x0, 0x0)
    mEducationToolData: (Embed, 0x0, 0x0, ToolEducationData)
    mAdaptiveForceToAbilityPowerWeight: (F32, 0x0, 0x0, 0x0)
    BaseHp: (F32, 0x0, 0x0, 0x0)
    AreaIndicatorTextureSize: (F32, 0x0, 0x0, 0x0)
    AttackSpeedPerLevel: (F32, 0x0, 0x0, 0x0)
    CharAudioNameOverride: (String, 0x0, 0x0, 0x0)
    Script: (Pointer, 0x0, 0x0, CharScript)
    MinionFlags: (U32, 0x0, 0x0, 0x0)
    HoverIndicatorRotateToPlayer: (Bool, 0x0, 0x0, 0x0)
    CriticalAttack: (String, 0x0, 0x0, 0x0)
    OutlineBboxExpansion: (F32, 0x0, 0x0, 0x0)
    PassiveLuaName: (String, 0x0, 0x0, 0x0)
    mPerkReplacements: (Embed, 0x0, 0x0, PerkReplacementList)
    mGameComponentList: (List, 0x0, Pointer, GameComponentData)
    mFallbackCharacterName: (String, 0x0, 0x0, 0x0)
    HoverLineIndicatorWidth: (F32, 0x0, 0x0, 0x0)
    BaseSpellBlock: (F32, 0x0, 0x0, 0x0)
    PackmanagerData: (Pointer, 0x0, 0x0, PackManagerData)
    UnitTagsString: (String, 0x0, 0x0, 0x0)
    RecSpellRankUpInfo: (List, 0x0, Embed, RecSpellRankUpInfo)
    AssetCategory: (String, 0x0, 0x0, 0x0)
    TargetLaserEffects: (Pointer, 0x0, 0x0, TargetLaserComponentEffects)
    HoverIndicatorRadius: (F32, 0x0, 0x0, 0x0)
    SelfChampSpecificHealthSuffix: (String, 0x0, 0x0, 0x0)
    MovingTowardEnemyActivationAngle: (F32, 0x0, 0x0, 0x0)
    mCharacterCalculations: (Map, Hash, Pointer, IGameCalculation)
    OnKillEvent: (U32, 0x0, 0x0, 0x0)
    BaseDamage: (F32, 0x0, 0x0, 0x0)
    CritPerLevel: (F32, 0x0, 0x0, 0x0)
    0x43135375: (F32, 0x0, 0x0, 0x0)
    ParMaxSegments: (I32, 0x0, 0x0, 0x0)
    HoverIndicatorRadiusMinimap: (F32, 0x0, 0x0, 0x0)
    mClientSideItemInventory: (List, 0x0, Hash, 0x0)
    LocalExpGivenOnDeath: (F32, 0x0, 0x0, 0x0)
    BaseStaticHpRegen: (F32, 0x0, 0x0, 0x0)
    0x4b2ddaa0: (Bool, 0x0, 0x0, 0x0)
    TreatAutoAttacksAsNormalSpells: (Pointer, 0x0, 0x0, TreatAutoAttacksAsNormalSpells)
    BasePar: (F32, 0x0, 0x0, 0x0)
    SkipSequencedAttackEvents: (Bool, 0x0, 0x0, 0x0)
    SelectionRadius: (F32, 0x0, 0x0, 0x0)
    PerceptionBoundingBoxSize: (Option, 0x0, Vec3, 0x0)
    HoverLineIndicatorWidthMinimap: (F32, 0x0, 0x0, 0x0)
    OnKillEventForSpectator: (U32, 0x0, 0x0, 0x0)
    mPreferredPerkStyle: (Link, 0x0, 0x0, PerkStyle)
    RecSpellRankUpInfolist: (Embed, 0x0, 0x0, RecSpellRankUpInfoList)
    HoverLineIndicatorTargetTextureName: (String, 0x0, 0x0, 0x0)
    ParIncrements: (F32, 0x0, 0x0, 0x0)
    DeathEventListeningRadius: (F32, 0x0, 0x0, 0x0)
    DisplayCamoVfx: (Bool, 0x0, 0x0, 0x0)
    BaseFactorHpRegen: (F32, 0x0, 0x0, 0x0)
    AttackSpeedRatio: (F32, 0x0, 0x0, 0x0)
    EnemyTooltip: (String, 0x0, 0x0, 0x0)
    AreaIndicatorRadius: (F32, 0x0, 0x0, 0x0)
    Significance: (F32, 0x0, 0x0, 0x0)
    StatStoneSets: (List, 0x0, Link, StatStoneSet)
    AcquisitionRange: (F32, 0x0, 0x0, 0x0)
    FirstAcquisitionRange: (Option, 0x0, F32, 0x0)
    GoldRadius: (F32, 0x0, 0x0, 0x0)
    WakeUpRange: (Option, 0x0, F32, 0x0)
    TowerTargetingPriorityBoost: (F32, 0x0, 0x0, 0x0)
    AreaIndicatorMinRadius: (F32, 0x0, 0x0, 0x0)
    EvolutionData: (Pointer, 0x0, 0x0, EvolutionDescription)
    PlatformEnabled: (Bool, 0x0, 0x0, 0x0)
    ExperienceRadius: (F32, 0x0, 0x0, 0x0)
    AllyChampSpecificHealthSuffix: (String, 0x0, 0x0, 0x0)
    ExtraAttacks: (List, 0x0, Embed, AttackSlotData)
    BaseMoveSpeed: (F32, 0x0, 0x0, 0x0)
    BaseArmor: (F32, 0x0, 0x0, 0x0)
    AttackSpeed: (F32, 0x0, 0x0, 0x0)
    BaseDodge: (F32, 0x0, 0x0, 0x0)
    MonsterDataTableId: (I32, 0x0, 0x0, 0x0)
    FriendlyTooltip: (String, 0x0, 0x0, 0x0)
    FriendlyUxOverrideTeam: (U32, 0x0, 0x0, 0x0)
    OverrideGameplayCollisionRadius: (Option, 0x0, F32, 0x0)
    AbilityPower: (F32, 0x0, 0x0, 0x0)
    PerceptionBubbleRadius: (F32, 0x0, 0x0, 0x0)
    PerceptionBubbleRadius: (Option, 0x0, F32, 0x0)
    0x8263e1d: (Pointer, 0x0, 0x0, 0x8263e1d)
    Tips2: (String, 0x0, 0x0, 0x0)
    PassiveDescription: (String, 0x0, 0x0, 0x0)
    Tips1: (String, 0x0, 0x0, 0x0)
    CritDamageMultiplier: (F32, 0x0, 0x0, 0x0)
    ExtraSpells: (List, 0x10, String, 0x0)
    BufferedInputData: (Pointer, 0x0, 0x0, BufferedInputData)
    Name: (String, 0x0, 0x0, 0x0)
    HoverIndicatorMinimapOverride: (String, 0x0, 0x0, 0x0)
    PathfindingCollisionRadius: (F32, 0x0, 0x0, 0x0)
    GlobalGoldGivenOnDeath: (F32, 0x0, 0x0, 0x0)
    UntargetableSpawnTime: (F32, 0x0, 0x0, 0x0)
    ParName: (String, 0x0, 0x0, 0x0)
    ParRegenPerLevel: (F32, 0x0, 0x0, 0x0)
    OverrideParColor: (Option, 0x0, Color, 0x0)
    PassiveIsPingable: (Bool, 0x0, 0x0, 0x0)
    DodgePerLevel: (F32, 0x0, 0x0, 0x0)
    SpellLevelUpInfo: (List, 0x4, Embed, SpellLevelUpInfo)
    Flags: (U32, 0x0, 0x0, 0x0)
    GlobalExpGivenOnDeath: (F32, 0x0, 0x0, 0x0)
    mAbilitySlotCc: (List, 0x4, I32, 0x0)
    OnKillEventSteal: (U32, 0x0, 0x0, 0x0)
    HealthBarHeight: (F32, 0x0, 0x0, 0x0)
    HighlightHealthbarIcons: (Bool, 0x0, 0x0, 0x0)
    SilhouetteAttachmentAnim: (String, 0x0, 0x0, 0x0)
    AttackAutoInterruptPercent: (F32, 0x0, 0x0, 0x0)
    PassiveToolTip: (String, 0x0, 0x0, 0x0)
    AreaIndicatorTextureName: (String, 0x0, 0x0, 0x0)
    AreaIndicatorTargetDistance: (F32, 0x0, 0x0, 0x0)
    DamagePerLevel: (F32, 0x0, 0x0, 0x0)
    HealthBarFullParallax: (Bool, 0x0, 0x0, 0x0)
    DeathTime: (F32, 0x0, 0x0, 0x0)
    LocalGoldSplitWithLastHitter: (Bool, 0x0, 0x0, 0x0)
    BasicAttack: (Embed, 0x0, 0x0, AttackSlotData)
    Lore1: (String, 0x0, 0x0, 0x0)
    mCharacterPassiveBuffs: (List, 0x0, Embed, CharacterPassiveData)
    PrimaryAbilityResource: (Embed, 0x0, 0x0, AbilityResourceSlotInfo)
    SpellBlockPerLevel: (F32, 0x0, 0x0, 0x0)
    0xbd5ba640: (Pointer, 0x0, 0x0, 0xbd5ba640)
    FriendlyUxOverrideExcludeTagsString: (String, 0x0, 0x0, 0x0)
    SpellNames: (List, 0x4, String, 0x0)
    OccludedUnitSelectableDistance: (F32, 0x0, 0x0, 0x0)
    AttackRange: (F32, 0x0, 0x0, 0x0)
    SelfCbChampSpecificHealthSuffix: (String, 0x0, 0x0, 0x0)
    BaseCritChance: (F32, 0x0, 0x0, 0x0)
    BaseFactorParRegen: (F32, 0x0, 0x0, 0x0)
    AbilityPowerIncPerLevel: (F32, 0x0, 0x0, 0x0)
    PassiveName: (String, 0x0, 0x0, 0x0)
    RotationSmoothing: (F32, 0x0, 0x0, 0x0)
    HpRegenPerLevel: (F32, 0x0, 0x0, 0x0)
    ExpGivenOnDeath: (F32, 0x0, 0x0, 0x0)
    ParType: (U32, 0x0, 0x0, 0x0)
    ParType: (U8, 0x0, 0x0, 0x0)
    DisabledTargetLaserEffects: (Pointer, 0x0, 0x0, TargetLaserComponentEffects)
    WeaponMaterials: (List, 0x0, String, 0x0)
    PassiveRange: (F32, 0x0, 0x0, 0x0)
    LaunchAreaData: (Pointer, 0x0, 0x0, LaunchAreaData)
    CritAttacks: (List, 0x0, Embed, AttackSlotData)
    LocalGoldGivenOnDeath: (F32, 0x0, 0x0, 0x0)
    JointForAnimAdjustedSelection: (String, 0x0, 0x0, 0x0)
    ArmorPerLevel: (F32, 0x0, 0x0, 0x0)
    MinimapIconOverride: (String, 0x0, 0x0, 0x0)
    0xdd661aab: (Pointer, 0x0, 0x0, 0x280745b1)
    0xdd661aab: (Pointer, 0x0, 0x0, 0xdd661aab)
    HoverLineIndicatorBaseTextureName: (String, 0x0, 0x0, 0x0)
    DoesNotGiveMinionScore: (Bool, 0x0, 0x0, 0x0)
    mAbilities: (List, 0x0, Link, AbilityObject)
    mDefaultStatOverrides: (Embed, 0x0, 0x0, StatFormulaDataList)
    ParHasRegenText: (Bool, 0x0, 0x0, 0x0)
    mCharacterPassiveSpell: (Link, 0x0, 0x0, SpellObject)
    AreaIndicatorMaxDistance: (F32, 0x0, 0x0, 0x0)
    SelectionHeight: (F32, 0x0, 0x0, 0x0)
    CharacterToolData: (Embed, 0x0, 0x0, CharacterToolData)
    UseRiotRelationships: (Bool, 0x0, 0x0, 0x0)
    HoverIndicatorTextureName: (String, 0x0, 0x0, 0x0)
    BaseStaticParRegen: (F32, 0x0, 0x0, 0x0)
    ParPerLevel: (F32, 0x0, 0x0, 0x0)
    Passive1IconName: (String, 0x0, 0x0, 0x0)
    RecordAsWard: (Bool, 0x0, 0x0, 0x0)
    EnemyChampSpecificHealthSuffix: (String, 0x0, 0x0, 0x0)
    BaseMissChance: (F32, 0x0, 0x0, 0x0)
    UseableData: (Embed, 0x0, 0x0, UseableData)
    PassiveSpell: (String, 0x0, 0x0, 0x0)
    GoldGivenOnDeath: (F32, 0x0, 0x0, 0x0)
    FriendlyUxOverrideIncludeTagsString: (String, 0x0, 0x0, 0x0)
    AreaIndicatorMinDistance: (F32, 0x0, 0x0, 0x0)
    SecondaryAbilityResource: (Embed, 0x0, 0x0, AbilityResourceSlotInfo)
    mUseCcAnimations: (Bool, 0x0, 0x0, 0x0)
    PurchaseIdentities: (List, 0x0, Hash, 0x0)
    HitFxScale: (F32, 0x0, 0x0, 0x0)
    HpPerLevel: (F32, 0x0, 0x0, 0x0)
    MinionScoreValue: (F32, 0x0, 0x0, 0x0)
    mCharacterName: (String, 0x0, 0x0, 0x0)
    pass

class StealthFadeColorEffect():
    MaxWeight: (F32, 0x0, 0x0, 0x0)
    OwnerOnly: (Bool, 0x0, 0x0, 0x0)
    ColorB: (U32, 0x0, 0x0, 0x0)
    Team: (U8, 0x0, 0x0, 0x0)
    FadeTime: (F32, 0x0, 0x0, 0x0)
    ColorG: (U32, 0x0, 0x0, 0x0)
    ColorR: (U32, 0x0, 0x0, 0x0)
    pass

class ModeProgressionRewardData(BaseLoadoutData):
    mBuffName: (String, 0x0, 0x0, 0x0)
    mVfxResourceResolver: (Pointer, 0x0, 0x0, ResourceResolver)
    mCharacters: (List, 0x0, String, 0x0)
    pass

class IVfxMaterialDriver():
    pass

class ReplayGameStateViewController(GameStateViewController):
    ChaosObjectiveBountiesData: (Pointer, 0x0, 0x0, SbObjectiveBounties)
    OrderObjectiveBountiesData: (Pointer, 0x0, 0x0, SbObjectiveBounties)
    pass

class RangeBetweenTargetsConstraintInfo(ListenerConstraintInfo):
    DistanceToCheck: (F32, 0x0, 0x0, 0x0)
    pass

class ByCharLevelFormulaCalculationPart(IGameCalculationPartByCharLevel, ISpellCalculationPartByCharLevel, ISpellCalculationPart):
    mValues: (List, 0x1f, F32, 0x0)
    pass

class CatalogEntry():
    ItemId: (U32, 0x0, 0x0, 0x0)
    ContentId: (String, 0x0, 0x0, 0x0)
    OfferId: (String, 0x0, 0x0, 0x0)
    TypeId: (String, 0x0, 0x0, 0x0)
    pass

class DamageSpellDisplayData():
    HotkeyText: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    IconHoverOverlay: (Hash, 0x0, 0x0, 0x0)
    Textures: (Embed, 0x0, 0x0, DamageSpellTextureData)
    DamageText: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class IRunFunctionBlock(IScriptBlock):
    InputParameters: (List, 0x0, Pointer, IScriptValueGet)
    OutputParameters: (List, 0x0, Embed, ScriptTableSet)
    Function: (Embed, 0x0, 0x0, FunctionTableGet)
    FunctionDefinition: (Embed, 0x0, 0x0, 0x2a2c82dc)
    pass

class ItemData():
    ItemId: (I32, 0x0, 0x0, 0x0)
    ItemId: (U32, 0x0, 0x0, 0x0)
    mSidegradeCredit: (F32, 0x0, 0x0, 0x0)
    mFlatHpRegenMod: (F32, 0x0, 0x0, 0x0)
    m_FlatCritDamageModPerLevel: (F32, 0x0, 0x0, 0x0)
    mFlatCooldownMod: (F32, 0x0, 0x0, 0x0)
    mDeathRecapName: (String, 0x0, 0x0, 0x0)
    m_FlatMovementSpeedModPerLevel: (F32, 0x0, 0x0, 0x0)
    mPercentSlowResistMod: (F32, 0x0, 0x0, 0x0)
    mFlatMovementSpeedMod: (F32, 0x0, 0x0, 0x0)
    PercentPhysicalVampMod: (F32, 0x0, 0x0, 0x0)
    mDataValues: (List, 0x0, Embed, ItemDataValue)
    Script: (Pointer, 0x0, 0x0, ItemScript)
    m_PercentMagicPenetrationModPerLevel: (F32, 0x0, 0x0, 0x0)
    ItemVoGroup: (Hash, 0x0, 0x0, 0x0)
    ItemVoGroup: (String, 0x0, 0x0, 0x0)
    0x224a3815: (I32, 0x0, 0x0, 0x0)
    mEffectAmount: (List, 0x0, F32, 0x0)
    mEffectAmount: (List, 0x8, F32, 0x0)
    m_FlatArmorModPerLevel: (F32, 0x0, 0x0, 0x0)
    m_FlatMagicPenetrationModPerLevel: (F32, 0x0, 0x0, 0x0)
    mFlatMagicDamageMod: (F32, 0x0, 0x0, 0x0)
    m_FlatMagicPenetrationMod: (F32, 0x0, 0x0, 0x0)
    m_FlatCritChanceModPerLevel: (F32, 0x0, 0x0, 0x0)
    RecipeItemLinks: (List, 0x0, Link, ItemData)
    m_FlatTimeDeadMod: (F32, 0x0, 0x0, 0x0)
    mPercentCritDamageMod: (F32, 0x0, 0x0, 0x0)
    mPercentLifeStealMod: (F32, 0x0, 0x0, 0x0)
    m_FlatHpRegenModPerLevel: (F32, 0x0, 0x0, 0x0)
    PercentMpRegenMod: (F32, 0x0, 0x0, 0x0)
    ItemGroup: (String, 0x0, 0x0, 0x0)
    mPercentHpRegenMod: (F32, 0x0, 0x0, 0x0)
    mRequiredAlly: (String, 0x0, 0x0, 0x0)
    StringCalculations: (Map, Hash, Pointer, IStringCalculation)
    mRequiredBuffCurrencyCost: (I32, 0x0, 0x0, 0x0)
    mPercentArmorPenetrationMod: (F32, 0x0, 0x0, 0x0)
    SellBackModifier: (F32, 0x0, 0x0, 0x0)
    mFlatCastRangeMod: (F32, 0x0, 0x0, 0x0)
    mFlatGoldPer10Mod: (F32, 0x0, 0x0, 0x0)
    Consumed: (Bool, 0x0, 0x0, 0x0)
    mFlatPhysicalDamageMod: (F32, 0x0, 0x0, 0x0)
    LastMajorChangeMinorPatchVersion: (U8, 0x0, 0x0, 0x0)
    mItemCalloutSpectator: (Bool, 0x0, 0x0, 0x0)
    RequiredItems: (List, 0x8, I32, 0x0)
    mFlatArmorPenetrationMod: (F32, 0x0, 0x0, 0x0)
    RestrictedBuffName: (String, 0x0, 0x0, 0x0)
    mFlatMagicReduction: (F32, 0x0, 0x0, 0x0)
    PercentMpPoolMod: (F32, 0x0, 0x0, 0x0)
    mItemAttributes: (I8, 0x0, 0x0, 0x0)
    mItemAttributes: (List, 0x0, U8, 0x0)
    mItemDataAvailability: (Embed, 0x0, 0x0, ItemDataAvailability)
    mPercentMagicPenetrationMod: (F32, 0x0, 0x0, 0x0)
    MapInclusions: (U32, 0x0, 0x0, 0x0)
    mSecondaryAttribute: (U8, 0x0, 0x0, 0x0)
    mItemAdviceAttributes: (List, 0x0, Hash, 0x0)
    mItemAdviceAttributes: (List, 0x0, Link, ItemAdviceAttribute)
    mAbilityHasteMod: (F32, 0x0, 0x0, 0x0)
    Epicness: (U8, 0x0, 0x0, 0x0)
    mVfxResourceResolver: (Pointer, 0x0, 0x0, ResourceResolver)
    mBuildDepth: (I32, 0x0, 0x0, 0x0)
    mPercentPhysicalReduction: (F32, 0x0, 0x0, 0x0)
    mPercentBonusArmorPenetrationMod: (F32, 0x0, 0x0, 0x0)
    mPercentMagicDamageMod: (F32, 0x0, 0x0, 0x0)
    SidegradeItemLinks: (List, 0x0, Link, ItemData)
    mPercentSpellVampMod: (F32, 0x0, 0x0, 0x0)
    mPercentBonusMagicPenetrationMod: (F32, 0x0, 0x0, 0x0)
    m_FlatTimeDeadModPerLevel: (F32, 0x0, 0x0, 0x0)
    m_FlatArmorPenetrationModPerLevel: (F32, 0x0, 0x0, 0x0)
    CustomInclusions: (List, 0x0, String, 0x0)
    mFlatHpPoolMod: (F32, 0x0, 0x0, 0x0)
    mHiddenFromOpponents: (Bool, 0x0, 0x0, 0x0)
    mMapStringIdInclusions: (List, 0x0, Hash, 0x0)
    m_FlatDodgeMod: (F32, 0x0, 0x0, 0x0)
    mFlatBubbleRadiusMod: (F32, 0x0, 0x0, 0x0)
    SpecialRecipe: (I32, 0x0, 0x0, 0x0)
    SpecialRecipe: (U32, 0x0, 0x0, 0x0)
    mItemGroups: (List, 0x0, Link, ItemGroup)
    mDisplayName: (String, 0x0, 0x0, 0x0)
    mPrimaryAttribute: (U8, 0x0, 0x0, 0x0)
    mParentEnchantmentId: (I32, 0x0, 0x0, 0x0)
    CustomExclusions: (List, 0x0, String, 0x0)
    m_FlatHpModPerLevel: (F32, 0x0, 0x0, 0x0)
    mFlatPhysicalReduction: (F32, 0x0, 0x0, 0x0)
    RecommendationTags: (List2, 0x0, Hash, 0x0)
    mMajorActiveItem: (Bool, 0x0, 0x0, 0x0)
    ConsumeOnAcquire: (Bool, 0x0, 0x0, 0x0)
    SpellName: (String, 0x0, 0x0, 0x0)
    mRequiredPurchaseIdentities: (List, 0x0, Hash, 0x0)
    m_PercentTimeDeadMod: (F32, 0x0, 0x0, 0x0)
    mFlatAttackRangeMod: (F32, 0x0, 0x0, 0x0)
    mPercentSpellBlockMod: (F32, 0x0, 0x0, 0x0)
    MaxStack: (I32, 0x0, 0x0, 0x0)
    RecipeItems: (List, 0x8, I32, 0x0)
    mItemDataBuild: (Embed, 0x0, 0x0, ItemDataBuild)
    m_PercentCooldownModPerLevel: (F32, 0x0, 0x0, 0x0)
    mRequiredBuffCurrencyName: (String, 0x0, 0x0, 0x0)
    UsableInStore: (Bool, 0x0, 0x0, 0x0)
    SecondaryEpicness: (U8, 0x0, 0x0, 0x0)
    mPercentExpBonus: (F32, 0x0, 0x0, 0x0)
    mPercentArmorMod: (F32, 0x0, 0x0, 0x0)
    mPercentHpPoolMod: (F32, 0x0, 0x0, 0x0)
    mDisabledDescriptionOverride: (String, 0x0, 0x0, 0x0)
    mScripts: (List, 0x0, String, 0x0)
    mPercentCooldownMod: (F32, 0x0, 0x0, 0x0)
    m_FlatArmorPenetrationMod: (F32, 0x0, 0x0, 0x0)
    FlatMpPoolMod: (F32, 0x0, 0x0, 0x0)
    ShopOrderPriority: (U8, 0x0, 0x0, 0x0)
    m_FlatSpellBlockModPerLevel: (F32, 0x0, 0x0, 0x0)
    mIsEnchantment: (Bool, 0x0, 0x0, 0x0)
    ShowCooldownInPings: (Bool, 0x0, 0x0, 0x0)
    m_PercentAttackSpeedModPerLevel: (F32, 0x0, 0x0, 0x0)
    PercentBaseMpRegenMod: (F32, 0x0, 0x0, 0x0)
    mPercentMultiplicativeMovementSpeedMod: (F32, 0x0, 0x0, 0x0)
    mItemCalculations: (Map, Hash, Pointer, IGameCalculation)
    mPercentMagicReduction: (F32, 0x0, 0x0, 0x0)
    m_FlatDodgeModPerLevel: (F32, 0x0, 0x0, 0x0)
    mPercentBubbleRadiusMod: (F32, 0x0, 0x0, 0x0)
    mModeNameInclusions: (List, 0x0, Hash, 0x0)
    mShowInActiveItemDisplay: (Bool, 0x0, 0x0, 0x0)
    m_FlatMagicDamageModPerLevel: (F32, 0x0, 0x0, 0x0)
    Price: (I32, 0x0, 0x0, 0x0)
    m_PercentArmorPenetrationMod: (F32, 0x0, 0x0, 0x0)
    mFlatArmorMod: (F32, 0x0, 0x0, 0x0)
    mItemModifiers: (List, 0x0, Link, ItemModifier)
    mPercentMovementSpeedMod: (F32, 0x0, 0x0, 0x0)
    PercentOmnivampMod: (F32, 0x0, 0x0, 0x0)
    PhysicalLethality: (F32, 0x0, 0x0, 0x0)
    mFlatDodgeMod: (F32, 0x0, 0x0, 0x0)
    mFlatSpellBlockMod: (F32, 0x0, 0x0, 0x0)
    mRequiredLevel: (I32, 0x0, 0x0, 0x0)
    mFlatCritChanceMod: (F32, 0x0, 0x0, 0x0)
    LastMajorChangeMajorPatchVersion: (U8, 0x0, 0x0, 0x0)
    mPercentBaseHpRegenMod: (F32, 0x0, 0x0, 0x0)
    mPercentHealingAmountMod: (F32, 0x0, 0x0, 0x0)
    mRequiredSpellName: (String, 0x0, 0x0, 0x0)
    mPercentAttackSpeedMod: (F32, 0x0, 0x0, 0x0)
    mFlatMissChanceMod: (F32, 0x0, 0x0, 0x0)
    m_PercentMagicPenetrationMod: (F32, 0x0, 0x0, 0x0)
    mPercentMultiplicativeAttackSpeedMod: (F32, 0x0, 0x0, 0x0)
    mCooldownShowDisabledDuration: (F32, 0x0, 0x0, 0x0)
    mPercentAttackRangeMod: (F32, 0x0, 0x0, 0x0)
    mCategories: (List, 0x0, String, 0x0)
    m_PercentCooldownMod: (F32, 0x0, 0x0, 0x0)
    ClearUndoHistoryOnActivate: (Bool, 0x0, 0x0, 0x0)
    mItemDataModifiable: (Embed, 0x0, 0x0, ItemDataModifiable)
    mPercentTenacityItemMod: (F32, 0x0, 0x0, 0x0)
    ClearUndoHistory: (U8, 0x0, 0x0, 0x0)
    mFlatCritDamageMod: (F32, 0x0, 0x0, 0x0)
    mCanBeSold: (Bool, 0x0, 0x0, 0x0)
    mItemAdvice: (List, 0x0, Embed, ItemAdvice)
    mPercentPhysicalDamageMod: (F32, 0x0, 0x0, 0x0)
    mItemPurchaseModifiers: (List, 0x0, Link, ItemPurchaseModifier)
    FlatMpRegenMod: (F32, 0x0, 0x0, 0x0)
    mItemDataClient: (Embed, 0x0, 0x0, ItemDataClient)
    mItemCalloutPlayer: (Bool, 0x0, 0x0, 0x0)
    mPercentCastRangeMod: (F32, 0x0, 0x0, 0x0)
    ParentItemLink: (Link, 0x0, 0x0, ItemData)
    mIsPopular: (Bool, 0x0, 0x0, 0x0)
    ParentEnchantmentLink: (Link, 0x0, 0x0, ItemData)
    mRequiredChampion: (String, 0x0, 0x0, 0x0)
    mParentEnchantmentGroup: (String, 0x0, 0x0, 0x0)
    m_PercentMovementSpeedModPerLevel: (F32, 0x0, 0x0, 0x0)
    mParentItemId: (I32, 0x0, 0x0, 0x0)
    mFlatMagicPenetrationMod: (F32, 0x0, 0x0, 0x0)
    IsRecipe: (Bool, 0x0, 0x0, 0x0)
    Clickable: (Bool, 0x0, 0x0, 0x0)
    m_PercentArmorPenetrationModPerLevel: (F32, 0x0, 0x0, 0x0)
    m_PercentTimeDeadModPerLevel: (F32, 0x0, 0x0, 0x0)
    mPercentSpellEffectivenessMod: (F32, 0x0, 0x0, 0x0)
    ShowCooldownVfxToAllies: (Bool, 0x0, 0x0, 0x0)
    mEnchantmentEffectAmount: (List, 0x0, F32, 0x0)
    ModeInclusions: (U32, 0x0, 0x0, 0x0)
    mSidegradeItems: (List, 0x8, I32, 0x0)
    RequiredItemLinks: (List, 0x0, Link, ItemData)
    DataValuesModeOverride: (Map, Hash, Embed, ItemDataValues)
    mEffectByLevelAmount: (List, 0x0, F32, 0x0)
    m_FlatPhysicalDamageModPerLevel: (F32, 0x0, 0x0, 0x0)
    pass

class AlternateSpellAssets():
    mHitEffectOrientType: (U32, 0x0, 0x0, 0x0)
    mHitEffectPlayerKey: (Hash, 0x0, 0x0, 0x0)
    mHaveHitBone: (Bool, 0x0, 0x0, 0x0)
    mHitBoneName: (String, 0x0, 0x0, 0x0)
    mHitEffectKey: (Hash, 0x0, 0x0, 0x0)
    mAfterEffectName: (String, 0x0, 0x0, 0x0)
    mUseAnimatorFramerate: (Bool, 0x0, 0x0, 0x0)
    mHaveHitEffect: (Bool, 0x0, 0x0, 0x0)
    mHitEffectName: (String, 0x0, 0x0, 0x0)
    mAnimationLeadOutName: (String, 0x0, 0x0, 0x0)
    mAfterEffectKey: (Hash, 0x0, 0x0, 0x0)
    mAnimationLoopName: (String, 0x0, 0x0, 0x0)
    mHitEffectPlayerName: (String, 0x0, 0x0, 0x0)
    mAnimationWinddownName: (String, 0x0, 0x0, 0x0)
    mAnimationName: (String, 0x0, 0x0, 0x0)
    pass

class FxType():
    Name: (String, 0x0, 0x0, 0x0)
    Hash: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x2483c715():
    BaseLoadable: (Hash, 0x0, 0x0, 0x0)
    MobileLoadable: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x24c7aea():
    Config: (List, 0x0, Pointer, 0x6a6e3b03)
    Mutator: (String, 0x0, 0x0, 0x0)
    pass

class TooltipInstanceKeyword(TooltipInstance):
    pass

class TftLobbyViewController(LobbyViewController):
    0x354d2b95: (Hash, 0x0, 0x0, 0x0)
    ReadyCheckDeclineVfx: (Hash, 0x0, 0x0, 0x0)
    LabPopupHitRegion: (Hash, 0x0, 0x0, 0x0)
    0x47aa5f76: (Hash, 0x0, 0x0, 0x0)
    LeaderControls: (Embed, 0x0, 0x0, LobbyLeaderControls)
    LobbyLayouts: (Map, U8, Pointer, LobbyLayout)
    EventTypeFields: (Map, String, Embed, LobbyLabFields)
    RatedOnlyTraKey: (String, 0x0, 0x0, 0x0)
    SoulfighterField: (Embed, 0x0, 0x0, LobbyLabFields)
    RankOnlyTraKey: (String, 0x0, 0x0, 0x0)
    ReadyCheckAcceptVfx: (Hash, 0x0, 0x0, 0x0)
    PopupHitRegion: (Hash, 0x0, 0x0, 0x0)
    CustomButtonPopupViewController: (Link, 0x0, 0x0, TftLobbyCustomButtonPopupViewController)
    RankAndRatedTraKey: (String, 0x0, 0x0, 0x0)
    0xc20a812c: (Link, 0x0, 0x0, 0xdbede580)
    DoubleUpFullLobbyEnabled: (Bool, 0x0, 0x0, 0x0)
    ReadyCheckTimerVfx: (Hash, 0x0, 0x0, 0x0)
    0xe31300f: (Hash, 0x0, 0x0, 0x0)
    0xe397d18b: (Map, Hash, Embed, TftLobbyCustomAssets)
    GameTypeFields: (Map, U32, Embed, LobbyLabFields)
    0xf0a2677: (Hash, 0x0, 0x0, 0x0)
    BottomButtons: (Embed, 0x0, 0x0, LobbyBottomButtons)
    pass

class 0x24e1cb45():
    0x95d5c48c: (Bool, 0x0, 0x0, 0x0)
    0xc080021c: (U32, 0x0, 0x0, 0x0)
    0xec211346: (U32, 0x0, 0x0, 0x0)
    pass

class ScriptTable():
    pass

class 0x24f4a711(SelectSpellBlock):
    pass

class 0x24fc182b(0xa24429bf):
    CameraBone: (String, 0x0, 0x0, 0x0)
    StartFrame: (I32, 0x0, 0x0, 0x0)
    FovBone: (String, 0x0, 0x0, 0x0)
    pass

class DisplayStatsUiData():
    BasicLayout: (Hash, 0x0, 0x0, 0x0)
    BasicStatUi: (Embed, 0x0, 0x0, DisplayBasicStatUiData)
    DetailedLayout: (Hash, 0x0, 0x0, 0x0)
    DetailedStatUi: (Embed, 0x0, 0x0, 0xee28fb8d)
    DisplayStats: (List2, 0x0, Embed, DisplayStatUiData)
    pass

class BannerData():
    BannerName: (String, 0x0, 0x0, 0x0)
    Team: (U32, 0x0, 0x0, 0x0)
    pass

class 0x2515101c(0xac83c7b):
    Quantity: (U32, 0x0, 0x0, 0x0)
    Rarity: (U32, 0x0, 0x0, 0x0)
    RewardTexturePath: (String, 0x0, 0x0, 0x0)
    pass

class RefundAbilityPointsCheat(Cheat):
    Target: (U32, 0x0, 0x0, 0x0)
    pass

class ObjectTags():
    mObjectTagList: (List2, 0x0, Hash, 0x0)
    mTagList: (String, 0x0, 0x0, 0x0)
    pass

class 0x252c22fd():
    0x27c5053e: (Bool, 0x0, 0x0, 0x0)
    0x7e29603: (U8, 0x0, 0x0, 0x0)
    0xa211c44d: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x253f5ab(0x64c18f7d):
    Cooldown: (F32, 0x0, 0x0, 0x0)
    PushDuration: (F32, 0x0, 0x0, 0x0)
    0x901d5b0c: (F32, 0x0, 0x0, 0x0)
    PushDistance: (F32, 0x0, 0x0, 0x0)
    ConeAngle: (F32, 0x0, 0x0, 0x0)
    0xc9cbfa01: (F32, 0x0, 0x0, 0x0)
    ConeRadius: (F32, 0x0, 0x0, 0x0)
    pass

class IBlock():
    pass

class RelicSubList():
    mName: (String, 0x0, 0x0, 0x0)
    mRelics: (List, 0x0, Link, Relic)
    pass

class TftPlaybook(BaseLoadoutData):
    Augments: (List2, 0x0, Hash, 0x0)
    Enabled: (Bool, 0x0, 0x0, 0x0)
    0x37f7e4d1: (F32, 0x0, 0x0, 0x0)
    LeagueClientSplashPath: (String, 0x0, 0x0, 0x0)
    LoadoutsIcon: (String, 0x0, 0x0, 0x0)
    0x5b560887: (String, 0x0, 0x0, 0x0)
    0x5bc372e6: (Bool, 0x0, 0x0, 0x0)
    LeagueClientIconPath: (String, 0x0, 0x0, 0x0)
    EarlyAugments: (List2, 0x0, Hash, 0x0)
    LateAugments: (List2, 0x0, Hash, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    BuffName: (String, 0x0, 0x0, 0x0)
    EarlyAugmentNames: (Map, U8, String, 0x0)
    VfxResourceResolver: (Hash, 0x0, 0x0, 0x0)
    LateAugmentNames: (Map, U8, String, 0x0)
    RotationThrottler: (String, 0x0, 0x0, 0x0)
    0xbf351f86: (Bool, 0x0, 0x0, 0x0)
    MidAugmentNames: (Map, U8, String, 0x0)
    LeagueClientSmallIconPath: (String, 0x0, 0x0, 0x0)
    Unit: (Hash, 0x0, 0x0, 0x0)
    MidAugments: (List2, 0x0, Hash, 0x0)
    LargeLoadoutsIcon: (String, 0x0, 0x0, 0x0)
    pass

class TftCombatRecapViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    CombatRecapLineTemplate: (Embed, 0x0, 0x0, TftCombatRecapLineTemplate)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    UtilityModeButton: (Hash, 0x0, 0x0, 0x0)
    OffensiveModeButton: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideBinName: (String, 0x0, 0x0, 0x0)
    CombatRecapPanelTemplate: (Embed, 0x0, 0x0, TftCombatRecapPanelTemplate)
    ToggleLeftPanelButton: (Hash, 0x0, 0x0, 0x0)
    VsBadgeScene: (Hash, 0x0, 0x0, 0x0)
    ButtonScene: (Hash, 0x0, 0x0, 0x0)
    ToggleLeftPanelButtonScene: (Hash, 0x0, 0x0, 0x0)
    DefensiveModeButton: (Hash, 0x0, 0x0, 0x0)
    PanelTransition: (Embed, 0x0, 0x0, HudMenuTransitionData)
    0xe446a2a1: (Hash, 0x0, 0x0, 0x0)
    BaseBinName: (String, 0x0, 0x0, 0x0)
    pass

class TftBannerLoadoutReward(TftBannerReward):
    LoadoutsItem: (Link, 0x0, 0x0, BaseLoadoutData)
    pass

class 0x2565db21(TargetingTypeData):
    mWallCursor: (Embed, 0x0, 0x0, CursorData)
    mBrushCursor: (Embed, 0x0, 0x0, CursorData)
    mRiverCursor: (Embed, 0x0, 0x0, CursorData)
    pass

class TftUnitAttachmentSlotsData():
    LargeSlots: (List, 0x0, Embed, TftUnitAttachmentLargeSlotData)
    StandardSlots: (List, 0x0, Embed, TftUnitAttachmentStandardSlotData)
    pass

class SequenceCategory():
    Name: (String, 0x0, 0x0, 0x0)
    Hash: (Hash, 0x0, 0x0, 0x0)
    Phases: (List, 0x0, Embed, SequencePhase)
    pass

class TftPhaseData():
    mDisplay: (U32, 0x0, 0x0, 0x0)
    mAnnouncementData: (Link, 0x0, 0x0, TftAnnouncementData)
    mEnabled: (Bool, 0x0, 0x0, 0x0)
    mDuration: (F32, 0x0, 0x0, 0x0)
    mLabel: (String, 0x0, 0x0, 0x0)
    pass

class UiElementGroupButtonData(UiElementGroupData):
    DefaultStateElements: (Embed, 0x0, 0x0, UiElementGroupButtonState)
    SelectedTooltipTraKey: (String, 0x0, 0x0, 0x0)
    TabOrder: (U32, 0x0, 0x0, 0x0)
    SelectedStateElements: (Embed, 0x0, 0x0, UiElementGroupButtonState)
    InactiveTooltipTraKey: (String, 0x0, 0x0, 0x0)
    SelectedClickedStateElements: (Embed, 0x0, 0x0, UiElementGroupButtonState)
    HitRegionElement: (Link, 0x0, 0x0, RegionElementData)
    HitRegionElement: (Link, 0x0, 0x0, UiElementRegionData)
    InactiveStateElements: (Embed, 0x0, 0x0, UiElementGroupButtonState)
    ClickReleaseParticleElement: (Link, 0x0, 0x0, UiElementParticleSystemData)
    ClickReleaseParticleElement: (Link, 0x0, 0x0, ParticleSystemElementData)
    IsFocusable: (Bool, 0x0, 0x0, 0x0)
    ActiveTooltipTraKey: (String, 0x0, 0x0, 0x0)
    SoundEvents: (Pointer, 0x0, 0x0, UiElementGroupButtonSoundEvents)
    AddTextSizeToHitRegion: (Bool, 0x0, 0x0, 0x0)
    ClickedStateElements: (Embed, 0x0, 0x0, UiElementGroupButtonState)
    SelectedHoverStateElements: (Embed, 0x0, 0x0, UiElementGroupButtonState)
    HoverStateElements: (Embed, 0x0, 0x0, UiElementGroupButtonState)
    IsActive: (Bool, 0x0, 0x0, 0x0)
    InactiveSelectedStateElements: (Embed, 0x0, 0x0, UiElementGroupButtonState)
    IsEnabled: (Bool, 0x0, 0x0, 0x0)
    IsSelected: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x25fe6ccb(UiMetricTypeI):
    0x32355648: (Hash, 0x0, 0x0, 0x0)
    0x42b4f315: (Embed, 0x0, 0x0, UiElementMeterSkin)
    0x6807e4e6: (Embed, 0x0, 0x0, UiElementMeterSkin)
    0x7c680b9f: (Hash, 0x0, 0x0, 0x0)
    0xb920a7a: (Embed, 0x0, 0x0, UiElementMeterSkin)
    Frame: (Hash, 0x0, 0x0, 0x0)
    0xe9e74973: (Embed, 0x0, 0x0, UiElementMeterSkin)
    pass

class TftArmorySlotData():
    ItemFootprintSelectedVfx: (Hash, 0x0, 0x0, 0x0)
    RadiantItemButton: (Hash, 0x0, 0x0, 0x0)
    RecipeHintButton: (Hash, 0x0, 0x0, 0x0)
    ItemIconBordered: (Hash, 0x0, 0x0, 0x0)
    DefaultItemButton: (Hash, 0x0, 0x0, 0x0)
    ItemDragRegion: (Hash, 0x0, 0x0, 0x0)
    SelectionCostText: (Hash, 0x0, 0x0, 0x0)
    0x63c87650: (Hash, 0x0, 0x0, 0x0)
    ItemFrame: (Hash, 0x0, 0x0, 0x0)
    ButtonStyles: (Map, String, Embed, TftArmoryButtonStyleData)
    ShadowItemButton: (Hash, 0x0, 0x0, 0x0)
    0x7a1e4997: (Hash, 0x0, 0x0, 0x0)
    NormalItemButton: (Hash, 0x0, 0x0, 0x0)
    ItemAction: (U8, 0x0, 0x0, 0x0)
    ItemIconShadow: (Hash, 0x0, 0x0, 0x0)
    Traits: (List, 0x0, Embed, TftArmoryItemTraitData)
    DesaturateOnInactive: (List, 0x0, Hash, 0x0)
    BadgeData: (Embed, 0x0, 0x0, TftArmoryBadgeDisplayData)
    ItemDesc: (Hash, 0x0, 0x0, 0x0)
    ItemFootprintUnselectedVfx: (Hash, 0x0, 0x0, 0x0)
    ItemActionButton: (Hash, 0x0, 0x0, 0x0)
    IconMaskRegion: (Hash, 0x0, 0x0, 0x0)
    DefaultButtonStyle: (Embed, 0x0, 0x0, TftArmoryButtonStyleData)
    CharacterTierGroups: (List, 0x0, Hash, 0x0)
    Styles: (List2, 0x0, Embed, TftArmoryStyleData)
    ItemStats: (Hash, 0x0, 0x0, 0x0)
    ItemName: (Hash, 0x0, 0x0, 0x0)
    ItemIcon: (Hash, 0x0, 0x0, 0x0)
    ElementGroup: (Hash, 0x0, 0x0, 0x0)
    pass

class FeatureId():
    mFeatureId: (String, 0x0, 0x0, 0x0)
    pass

class SortCustomTableBlock(IScriptBlock):
    Table: (Embed, 0x0, 0x0, CustomTableGet)
    pass

class OptionItemSliderInt(OptionItemSlider):
    OptionScale: (U32, 0x0, 0x0, 0x0)
    Option: (U16, 0x0, 0x0, 0x0)
    pass

class 0x26435b25(ViewController):
    DescriptionText: (Hash, 0x0, 0x0, 0x0)
    Highlight: (Hash, 0x0, 0x0, 0x0)
    TransitionTime: (F32, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    CountdownText: (Hash, 0x0, 0x0, 0x0)
    EasingType: (U8, 0x0, 0x0, 0x0)
    MinAlpha: (U8, 0x0, 0x0, 0x0)
    CountdownBackground: (Hash, 0x0, 0x0, 0x0)
    MaxAlpha: (U8, 0x0, 0x0, 0x0)
    SceneHandle: (Hash, 0x0, 0x0, 0x0)
    CardBackground: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class EnemyRespawnTimersViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    FlippedMinimapOverride: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    PortraitData: (List, 0x5, Embed, ScoreLinePortraitUiData)
    PortraitData: (List, 0x5, Embed, UiPlayerPortraitData)
    0x949bbb90: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    ObjectName: (String, 0x0, 0x0, 0x0)
    pass

class PlayerHeroStatsViewController(PlayerStatsPanelViewController):
    BasicStats: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    TooltipRegion: (Hash, 0x0, 0x0, 0x0)
    ObjectName: (String, 0x0, 0x0, 0x0)
    AdvancedStats: (Hash, 0x0, 0x0, 0x0)
    StatsUiData: (Embed, 0x0, 0x0, UnitStatsUiData)
    pass

class DropRateSlot():
    TierIcon: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    pass

class ICharacterQuestReward():
    pass

class TftStreak():
    mMinimumStreakLength: (Option, 0x0, U32, 0x0)
    mMaximumStreakLength: (Option, 0x0, U32, 0x0)
    mStreakFormat: (String, 0x0, 0x0, 0x0)
    mGoldRewardAmount: (U32, 0x0, 0x0, 0x0)
    pass

class SummonerEmoteManagerSettings():
    mAllyFacingDetectionRange: (F32, 0x0, 0x0, 0x0)
    mDefaultBadgeIds: (List, 0x7, U32, 0x0)
    mDefaultBadgeIds: (List, 0x8, U32, 0x0)
    mEnemyFacingDetectionRange: (F32, 0x0, 0x0, 0x0)
    mNoEmoteWheelTexture: (String, 0x0, 0x0, 0x0)
    pass

class 0x26917ba6(TftPassRewardBase):
    0x2484d6c3: (Bool, 0x0, 0x0, 0x0)
    Type: (String, 0x0, 0x0, 0x0)
    Currency: (Link, 0x0, 0x0, TftCurrency)
    pass

class 0x26949c34():
    ButtonType: (U8, 0x0, 0x0, 0x0)
    Id: (U32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    ButtonElement: (Hash, 0x0, 0x0, 0x0)
    pass

class TftGameStartSequenceSimple(TftGameStartSequence):
    Events: (List2, 0x0, Embed, TftGameStartSequenceSimpleEvent)
    Duration: (F32, 0x0, 0x0, 0x0)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    GameStartVfx: (Hash, 0x0, 0x0, 0x0)
    TotalDurationSecs: (F32, 0x0, 0x0, 0x0)
    pass

class ClearAlreadyHitTrackingOnMovementComplete(MissileBehaviorSpec):
    pass

class 0x26d26471():
    pass

class GdsMapObjectLightingInfo(GdsMapObjectExtraInfo):
    Colors: (List, 0x6, Vec4, 0x0)
    pass

class LayoutStyleHorizontalList(LayoutStyleBase):
    RowVerticalAlignment: (U8, 0x0, 0x0, 0x0)
    HorizontalFillDirection: (U8, 0x0, 0x0, 0x0)
    pass

class 0x27071fbd():
    pass

class StaticMaterialSharedTextureDef():
    FilterMip: (U32, 0x0, 0x0, 0x0)
    Address: (U32, 0x0, 0x0, 0x0)
    SharedTextureName: (String, 0x0, 0x0, 0x0)
    Filter: (U32, 0x0, 0x0, 0x0)
    TexturePath: (String, 0x0, 0x0, 0x0)
    pass

class UnitShopItemFrameData():
    Clicked: (Hash, 0x0, 0x0, 0x0)
    Hover: (Hash, 0x0, 0x0, 0x0)
    Default: (Hash, 0x0, 0x0, 0x0)
    pass

class CherryEliminationViewController(ViewController):
    0x156acc5e: (F32, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    VictoryHighlightVfx: (Hash, 0x0, 0x0, 0x0)
    WaitingHighlightVfx: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    EliminationHighlightVfx: (Hash, 0x0, 0x0, 0x0)
    LeaveButton: (Hash, 0x0, 0x0, 0x0)
    SpectateButton: (Hash, 0x0, 0x0, 0x0)
    RankText: (Hash, 0x0, 0x0, 0x0)
    0xd83858e8: (String, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class TftZoomSkin(BaseLoadoutData):
    Rarity: (U32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    VfxResourceResolver: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x2755f1f9():
    pass

class 0x276246d8():
    0x90ebcab0: (Map, String, Embed, 0x72553f91)
    pass

class UiMetricTeamTowerKills(UiMetricTypeI):
    Team1TowerKillsText: (Hash, 0x0, 0x0, 0x0)
    Team2TowerKillsIcon: (Hash, 0x0, 0x0, 0x0)
    Team2TowerKillsText: (Hash, 0x0, 0x0, 0x0)
    Team1TowerKillsIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class GoldTooltipTraKeys():
    BodyKey: (String, 0x0, 0x0, 0x0)
    TitleKey: (String, 0x0, 0x0, 0x0)
    pass

class IntTableSet(RsTableSet, ScriptTableSet):
    pass

class CallOnMissileBounceOnMovementComplete(MissileBehaviorSpec):
    pass

class AddParCheat(Cheat):
    mAmount: (F32, 0x0, 0x0, 0x0)
    mTarget: (U32, 0x0, 0x0, 0x0)
    pass

class VfxPrimitiveArbitrarySegmentBeam(VfxPrimitiveBeamBase):
    pass

class MapPointLightType():
    Impact: (I32, 0x0, 0x0, 0x0)
    Impact: (U8, 0x0, 0x0, 0x0)
    Type: (U8, 0x0, 0x0, 0x0)
    FalloffColor: (Vec4, 0x0, 0x0, 0x0)
    LightColor: (Vec4, 0x0, 0x0, 0x0)
    Specular: (Bool, 0x0, 0x0, 0x0)
    CastStaticShadows: (Bool, 0x0, 0x0, 0x0)
    HdrScale: (F32, 0x0, 0x0, 0x0)
    Radius: (F32, 0x0, 0x0, 0x0)
    pass

class GearSkinUpgrade(ISkinUpgradeObject):
    mBoneToAttachTo: (String, 0x0, 0x0, 0x0)
    mGearData: (Pointer, 0x0, 0x0, GearData)
    pass

class 0x27e1d5d2(TableValue):
    pass

class TargeterDefinitionSpline(TargeterDefinition):
    FrontTextureName: (String, 0x0, 0x0, 0x0)
    EndLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    ConstraintRange: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    IsConstrainedToRange: (Bool, 0x0, 0x0, 0x0)
    SplineWidth: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    OverrideSpline: (Pointer, 0x0, 0x0, ISplineInfo)
    TextureName: (String, 0x0, 0x0, 0x0)
    MinSegmentCount: (U32, 0x0, 0x0, 0x0)
    StartLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    BaseTextureName: (String, 0x0, 0x0, 0x0)
    MaxSegmentLength: (F32, 0x0, 0x0, 0x0)
    pass

class 0x27f036af(0x64c18f7d):
    0x5d1c6fe9: (Bool, 0x0, 0x0, 0x0)
    StartMoveSpeed: (F32, 0x0, 0x0, 0x0)
    LerpTimeSeconds: (F32, 0x0, 0x0, 0x0)
    EndMoveSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class 0x280745b1():
    Params: (Pointer, 0x0, 0x0, 0xc7e628b9)
    0x50aad250: (List2, 0x0, Pointer, 0xdd661aab)
    pass

class ProgressBarViewController(ViewController):
    CastBar: (Embed, 0x0, 0x0, ProgressBarDisplayData)
    Scene: (Hash, 0x0, 0x0, 0x0)
    ProgressBar: (Embed, 0x0, 0x0, ProgressBarDisplayData)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    Layout: (Hash, 0x0, 0x0, 0x0)
    ObjectName: (String, 0x0, 0x0, 0x0)
    pass

class VfxMaterialDefinitionData():
    MaterialDrivers: (Map, String, Pointer, IVfxMaterialDriver)
    Material: (Link, 0x0, 0x0, IMaterialDef)
    pass

class HudReplaySlider():
    SliderProgressBar: (Hash, 0x0, 0x0, 0x0)
    Slider: (Hash, 0x0, 0x0, 0x0)
    Tooltip: (Embed, 0x0, 0x0, HudReplayEventTooltip)
    SliderBackdrop: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x2848d6a0(IEnabler):
    Enablers: (List2, 0x0, Pointer, IEnabler)
    pass

class RecSpellRecommendations():
    RecSpellRankUpInfolist: (Hash, 0x0, 0x0, 0x0)
    DesignerRecSpellOverride: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxPrimitiveCameraTrail(VfxPrimitiveTrailBase):
    pass

class 0x288b8edc():
    SpellObjects: (List, 0x4, Hash, 0x0)
    SpellObjects: (List, 0x4, Link, SpellObject)
    0x40a9978e: (Bool, 0x0, 0x0, 0x0)
    pass

class SummonerSpellUpgradeDescription():
    mTitle: (String, 0x0, 0x0, 0x0)
    mFlags: (U32, 0x0, 0x0, 0x0)
    mIconNames: (List, 0x2, String, 0x0)
    mTooltips: (List, 0x2, String, 0x0)
    pass

class TestMap(WadFileDescriptor):
    AdditionalRoots: (List, 0x0, String, 0x0)
    pass

class TftCurrency():
    CurrencyId: (String, 0x0, 0x0, 0x0)
    Rarity: (U32, 0x0, 0x0, 0x0)
    0x5f944701: (String, 0x0, 0x0, 0x0)
    NameTraKey: (String, 0x0, 0x0, 0x0)
    RewardTexturePath: (String, 0x0, 0x0, 0x0)
    TrovesHighlightVfx: (Hash, 0x0, 0x0, 0x0)
    0x8e2a4357: (Hash, 0x0, 0x0, 0x0)
    TrovesRewardTexturePath: (String, 0x0, 0x0, 0x0)
    pass

class 0x28be1dfd():
    Duration: (F32, 0x0, 0x0, 0x0)
    StartTime: (F32, 0x0, 0x0, 0x0)
    BlendOutTime: (F32, 0x0, 0x0, 0x0)
    Priority: (U8, 0x0, 0x0, 0x0)
    BlendInTime: (F32, 0x0, 0x0, 0x0)
    EffectKey: (String, 0x0, 0x0, 0x0)
    pass

class 0x28dee5e9():
    0x1732050: (Hash, 0x0, 0x0, 0x0)
    0x5438ead6: (List, 0x0, Embed, 0xb4f87c91)
    LoadoutsButtonData: (List, 0x0, Embed, 0x93228fac)
    LoadingSpinnerVfx: (Hash, 0x0, 0x0, 0x0)
    pass

class LootStatus():
    mLifetimeMax: (I32, 0x0, 0x0, 0x0)
    mTags: (List, 0x0, String, 0x0)
    mImageTexturePath: (String, 0x0, 0x0, 0x0)
    mInactiveDate: (String, 0x0, 0x0, 0x0)
    mActiveDate: (String, 0x0, 0x0, 0x0)
    mActive: (Bool, 0x0, 0x0, 0x0)
    mAutoRedeem: (Bool, 0x0, 0x0, 0x0)
    pass

class UiTeamMemberData():
    UltimateSpellSlot: (Pointer, 0x0, 0x0, SpellSlotSimpleUiDefinition)
    HealthMeter: (Pointer, 0x0, 0x0, HealthBarData)
    SummonerSpellSlots: (Pointer, 0x0, 0x0, ScoreLineSpellSlots)
    0x1d924766: (Pointer, 0x0, 0x0, 0x37a8385c)
    ObjectivePlanningIcon: (Pointer, 0x0, 0x0, 0x6c84152e)
    UltimateCooldownGem: (Pointer, 0x0, 0x0, CooldownGemUiData)
    Portrait: (Embed, 0x0, 0x0, UiPlayerPortraitData)
    ReciprocityOverlay: (Hash, 0x0, 0x0, 0x0)
    VoiceChatHalo: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    ParMeter: (Pointer, 0x0, 0x0, AbilityResourceBarData)
    Level: (Pointer, 0x0, 0x0, UnitLevelUiData)
    KeystoneIcon: (Hash, 0x0, 0x0, 0x0)
    SummonerName: (Pointer, 0x0, 0x0, SummonerNameUiData)
    StatusEffects: (Pointer, 0x0, 0x0, UiUnitStatusData)
    HitRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class KillAllTurretsCheat(Cheat):
    pass

class BlendedLinearHeightSolver(HeightSolverType):
    pass

class UiElementInstancedEffect(UiElementEffect):
    pass

class 0x296338f8(0x377491e8):
    0x7863785e: (F32, 0x0, 0x0, 0x0)
    MinDistance: (F32, 0x0, 0x0, 0x0)
    MaxDistance: (F32, 0x0, 0x0, 0x0)
    pass

class 0x296c4c00(0xa8a6ac21):
    Value: (String, 0x0, 0x0, 0x0)
    pass

class RecallDecalData():
    EffectFile: (String, 0x0, 0x0, 0x0)
    EmpoweredArrivalFile: (String, 0x0, 0x0, 0x0)
    EmpoweredEffectFile: (String, 0x0, 0x0, 0x0)
    RecallDecalId: (U32, 0x0, 0x0, 0x0)
    ArrivalEffectFile: (String, 0x0, 0x0, 0x0)
    pass

class MilestoneDefinition():
    Properties: (List, 0x0, Link, IMilestoneProperty)
    Id: (String, 0x0, 0x0, 0x0)
    TriggerValue: (I32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    IsPremium: (Bool, 0x0, 0x0, 0x0)
    Counter: (Link, 0x0, 0x0, CounterDefinition)
    MilestoneSize: (U32, 0x0, 0x0, 0x0)
    pass

class ContextualActionPlayVo(ContextualActionPlayAudio):
    pass

class ItemSlotSimpleUiData():
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    HitArea: (Hash, 0x0, 0x0, 0x0)
    StackText: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    CooldownEffects: (Embed, 0x0, 0x0, CooldownEffectUiData)
    pass

class TargeterDefinitionAoeScalar():
    MaxAdjustedRadius: (F32, 0x0, 0x0, 0x0)
    MinAdjustedRadius: (F32, 0x0, 0x0, 0x0)
    Scalar: (F32, 0x0, 0x0, 0x0)
    pass

class 0x29ec74eb(VfxSpawnConditionData):
    CasterCondition: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    OwnerCondition: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    pass

class ChampionPerkKeystoneUiData():
    KeystoneSubstyleIcon: (Hash, 0x0, 0x0, 0x0)
    KeystoneIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class EsportsRotatingBannerConfiguration():
    IndividualBannerOverrides: (List, 0x0, Embed, RotatingBanner)
    GlobalRotationTimeInSeconds: (F32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    Priority: (U32, 0x0, 0x0, 0x0)
    LeagueRotatingFlavors: (List, 0x0, Embed, LeagueRotatingFlavor)
    AssociatedTeams: (List, 0x0, String, 0x0)
    IsAnEvent: (Bool, 0x0, 0x0, 0x0)
    GlobalRotationTime: (F32, 0x0, 0x0, 0x0)
    DefaultBannerTexturePath: (File, 0x0, 0x0, 0x0)
    TexturePath: (File, 0x0, 0x0, 0x0)
    EventMutator: (Link, 0x0, 0x0, GameMutatorExpansions)
    AssociatedVersions: (List, 0x0, String, 0x0)
    StartupDelayInSeconds: (F32, 0x0, 0x0, 0x0)
    pass

class OptionTemplateHotkeys(IOptionTemplate):
    QuickCastButtonPos: (Hash, 0x0, 0x0, 0x0)
    HotkeyModifierText: (Hash, 0x0, 0x0, 0x0)
    BoundingRegion: (Hash, 0x0, 0x0, 0x0)
    CastAllButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    HotkeyButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    NormalCastButtonPos: (Hash, 0x0, 0x0, 0x0)
    Labels: (List, 0x0, Embed, OptionTemplateHotkeysLabel)
    HotkeyButtonTextSmall: (Hash, 0x0, 0x0, 0x0)
    HotkeyQuickCastButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    Keys: (List, 0x0, Embed, OptionTemplateHotkeysKey)
    pass

class 0x2a2c82dc():
    Inputs: (List2, 0x0, Pointer, IScriptValueGet)
    Outputs: (List2, 0x0, Pointer, ScriptTableSet)
    pass

class IntGet(IIntGet, IScriptValueGet):
    Value: (I32, 0x0, 0x0, 0x0)
    pass

class MapMinimap(MapComponent):
    MinimapEnabled: (Bool, 0x0, 0x0, 0x0)
    TexturePath: (String, 0x0, 0x0, 0x0)
    pass

class 0x2a598565(TftFinisherData):
    IntroVfx: (String, 0x0, 0x0, 0x0)
    TargetAnimData: (List2, 0x0, Embed, 0x64e7b9e1)
    TargetIdleAnimation: (Hash, 0x0, 0x0, 0x0)
    OutroVfx: (String, 0x0, 0x0, 0x0)
    StopAudioEventName: (String, 0x0, 0x0, 0x0)
    PostFxData: (List2, 0x0, Embed, 0x28be1dfd)
    0x567421af: (List2, 0x0, Embed, 0x24fc182b)
    CameraBone: (String, 0x0, 0x0, 0x0)
    0x721f9044: (String, 0x0, 0x0, 0x0)
    NearClipPlane: (F32, 0x0, 0x0, 0x0)
    0x7c67d7e9: (String, 0x0, 0x0, 0x0)
    AudioEventName: (String, 0x0, 0x0, 0x0)
    AnimationName: (Hash, 0x0, 0x0, 0x0)
    AnimationName: (String, 0x0, 0x0, 0x0)
    0x9fa5a56c: (List2, 0x0, Embed, 0x2373fc78)
    FovBone: (String, 0x0, 0x0, 0x0)
    0xc7b9055a: (F32, 0x0, 0x0, 0x0)
    FarClipPlane: (F32, 0x0, 0x0, 0x0)
    0xe9e6d319: (F32, 0x0, 0x0, 0x0)
    OpponentAttachToBone: (String, 0x0, 0x0, 0x0)
    pass

class RecallSkinUpgrade(ISkinUpgradeObject):
    mArrivalEffectFile: (String, 0x0, 0x0, 0x0)
    mEmpoweredEffectFile: (String, 0x0, 0x0, 0x0)
    mEmpoweredArrivalFile: (String, 0x0, 0x0, 0x0)
    mEffectFile: (String, 0x0, 0x0, 0x0)
    pass

class 0x2a84083e(0x114828a9):
    Radius: (F32, 0x0, 0x0, 0x0)
    pass

class HasAtleastNSubRequirementsCastRequirement(ICastRequirement):
    mSuccessesRequired: (U32, 0x0, 0x0, 0x0)
    mSubRequirements: (List, 0x0, Pointer, ICastRequirement)
    pass

class TipTrackerViewController(ViewController):
    MessageTemplate: (Embed, 0x0, 0x0, HudTipTrackerMessageTemplate)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MessageDisplayData: (Embed, 0x0, 0x0, HudMessageDisplayData)
    ItemSceneTemplate: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x2a98259f(0xb0e1e45e):
    Updater: (Pointer, 0x0, 0x0, IFloatParametricUpdater)
    Comparator: (U8, 0x0, 0x0, 0x0)
    TargetValue: (F32, 0x0, 0x0, 0x0)
    pass

class 0x2aa61eb4():
    SourceIcon: (Hash, 0x0, 0x0, 0x0)
    CenterKnownSourceIcon: (Hash, 0x0, 0x0, 0x0)
    CenterActiveSourceIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class MinimapBackgroundConfig():
    mCustomMinimapBackgrounds: (Map, Hash, Embed, MinimapBackground)
    0x7035cf20: (Bool, 0x0, 0x0, 0x0)
    PreloadTextures: (Bool, 0x0, 0x0, 0x0)
    mDefaultTextureName: (String, 0x0, 0x0, 0x0)
    pass

class FxActionAlpha(IFxAction):
    EasingType: (U8, 0x0, 0x0, 0x0)
    TargetAlpha: (F32, 0x0, 0x0, 0x0)
    TargetObject: (Embed, 0x0, 0x0, FxTarget)
    TargetObject: (Embed, 0x0, 0x0, FxObjectSelector)
    ResetOnEnd: (Bool, 0x0, 0x0, 0x0)
    pass

class VfxSineMaterialDriver(IVfxMaterialDriver):
    mBias: (F32, 0x0, 0x0, 0x0)
    mFrequency: (F32, 0x0, 0x0, 0x0)
    mScale: (F32, 0x0, 0x0, 0x0)
    pass

class ScriptCommentBlock(IScriptBlock, IFunctionalScriptBlock):
    Sequence: (Embed, 0x0, 0x0, ScriptSequence)
    pass

class GameModeConstantsGroup():
    mConstants: (Map, Hash, Pointer, GameModeConstant)
    pass

class 0x2b00c366(TftPassRewardBase):
    Type: (String, 0x0, 0x0, 0x0)
    TypeId: (String, 0x0, 0x0, 0x0)
    pass

class UiElementIcon(UiElementAsset):
    pass

class FxActionVfxBaseInstance(IFxActionInstance):
    pass

class MaskData():
    mName: (Hash, 0x0, 0x0, 0x0)
    mFlags: (U16, 0x0, 0x0, 0x0)
    mWeightList: (List, 0x0, F32, 0x0)
    mId: (U32, 0x0, 0x0, 0x0)
    pass

class UiElement(UiElementI):
    pass

class CoinsPromoDialogViewController(ModalDialogViewController):
    pass

class 0x2b6fac9a():
    Tag: (Hash, 0x0, 0x0, 0x0)
    Amount: (I32, 0x0, 0x0, 0x0)
    pass

class AnnouncementIcon():
    MainIconGroup: (Hash, 0x0, 0x0, 0x0)
    AlliedElementGroup: (Hash, 0x0, 0x0, 0x0)
    BorderRingElement: (Hash, 0x0, 0x0, 0x0)
    MainContentElement: (Hash, 0x0, 0x0, 0x0)
    MasteryBorderLevel6: (Hash, 0x0, 0x0, 0x0)
    MasteryBorderLevel7: (Hash, 0x0, 0x0, 0x0)
    MasteryBorderLevel4: (Hash, 0x0, 0x0, 0x0)
    MasteryBorderLevel5: (Hash, 0x0, 0x0, 0x0)
    EnemyElementGroup: (Hash, 0x0, 0x0, 0x0)
    pass

class TeamFramesViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    0x25f3de6e: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    FlippedMinimapOverride: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    TeamFrameTemplate: (Embed, 0x0, 0x0, UiTeamMemberData)
    Layout: (Hash, 0x0, 0x0, 0x0)
    ReciprocityButton: (Pointer, 0x0, 0x0, HudReciprocityButton)
    pass

class FxSequence():
    Actions: (List, 0x0, Pointer, IFxAction)
    Actions: (List2, 0x0, Pointer, IFxAction)
    Category: (Link, 0x0, 0x0, FxCategory)
    PhaseOverrides: (List, 0x0, Embed, FxPhaseOverride)
    pass

class MapVisibilityFlagDefinition():
    PublicName: (String, 0x0, 0x0, 0x0)
    TransitionTime: (F32, 0x0, 0x0, 0x0)
    Name: (Hash, 0x0, 0x0, 0x0)
    BitIndex: (U8, 0x0, 0x0, 0x0)
    pass

class RegaliaRatedBadgeMap():
    RatingToBadgeMap: (Map, String, Embed, RegaliaData)
    pass

class 0x2bcba3b4(ISequenceActionInstance):
    pass

class ContinueBlock(IScriptBlock):
    pass

class 0x2bde0c9c(0x8e30b80e):
    OrientOffset: (Bool, 0x0, 0x0, 0x0)
    OffsetVector: (Vec3, 0x0, 0x0, 0x0)
    pass

class CastOnMovementCompleteSpec(MissileBehaviorSpec):
    pass

class InputSourceBoolAsFloat(IInputSourceFloat):
    OffValue: (F32, 0x0, 0x0, 0x0)
    BoolSource: (Pointer, 0x0, 0x0, IInputSourceBool)
    OnValue: (F32, 0x0, 0x0, 0x0)
    pass

class ReplayCameraControlsViewController(ViewController):
    TeamFowComboBoxDefinition: (Hash, 0x0, 0x0, 0x0)
    DirectedCameraToggleButton: (Hash, 0x0, 0x0, 0x0)
    DirectedCameraStatusText: (Hash, 0x0, 0x0, 0x0)
    TooltipLink: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    CameraControlsComboBoxDefinition: (Hash, 0x0, 0x0, 0x0)
    VisibilityMenuButton: (Hash, 0x0, 0x0, 0x0)
    SceneLink: (Hash, 0x0, 0x0, 0x0)
    FowToggleButton: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxColorOverLifeMaterialDriver(IVfxMaterialDriver):
    Frequency: (U8, 0x0, 0x0, 0x0)
    Colors: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    pass

class 0x2bfb084c():
    GroupName: (Hash, 0x0, 0x0, 0x0)
    Tags: (List2, 0x0, Embed, 0xf6f4bb5f)
    pass

class LevelPropGameObjectCommon(GameObject):
    pass

class TftTrovesViewController(ViewController):
    FailureSubtitleTraKey: (String, 0x0, 0x0, 0x0)
    MythicTokenButton: (Hash, 0x0, 0x0, 0x0)
    TftBannerIconData: (Embed, 0x0, 0x0, TftBannerIconData)
    Scene: (Hash, 0x0, 0x0, 0x0)
    UrgentBannerTimer: (Pointer, 0x0, 0x0, TftEventTimer)
    BannerList: (Hash, 0x0, 0x0, 0x0)
    SubtitleText: (Hash, 0x0, 0x0, 0x0)
    ActiveBannerIcon: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    DefaultBannerTimer: (Pointer, 0x0, 0x0, TftEventTimer)
    MoreInfoClickRegion: (Hash, 0x0, 0x0, 0x0)
    NoActiveBannersIcon: (Hash, 0x0, 0x0, 0x0)
    Roll10TextDisable: (Hash, 0x0, 0x0, 0x0)
    FailureIcon: (Hash, 0x0, 0x0, 0x0)
    MoreInfoButton: (Hash, 0x0, 0x0, 0x0)
    Roll10Text: (Hash, 0x0, 0x0, 0x0)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    ActiveBannerParent: (Hash, 0x0, 0x0, 0x0)
    FailureTitleTraKey: (String, 0x0, 0x0, 0x0)
    Roll1Button: (Hash, 0x0, 0x0, 0x0)
    BannerTimer: (Pointer, 0x0, 0x0, TftEventTimer)
    FailureText: (Hash, 0x0, 0x0, 0x0)
    Roll10Button: (Hash, 0x0, 0x0, 0x0)
    Roll1TextDisable: (Hash, 0x0, 0x0, 0x0)
    DefaultPlatform: (Hash, 0x0, 0x0, 0x0)
    NoContentSubtitleTraKey: (String, 0x0, 0x0, 0x0)
    NoContentTitleTraKey: (String, 0x0, 0x0, 0x0)
    CustomPlatform: (Hash, 0x0, 0x0, 0x0)
    Roll1Text: (Hash, 0x0, 0x0, 0x0)
    BannerBackground: (Hash, 0x0, 0x0, 0x0)
    MythicTokenText: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class SurrenderTypeData():
    StartTimeWithAfk: (F32, 0x0, 0x0, 0x0)
    WindowLength: (F32, 0x0, 0x0, 0x0)
    VoteTimeout: (F32, 0x0, 0x0, 0x0)
    PercentageRequired: (F32, 0x0, 0x0, 0x0)
    StartTime: (F32, 0x0, 0x0, 0x0)
    pass

class FloatingTextTypeList():
    EnemyMagicalDamage: (Link, 0x0, 0x0, FloatTextFormattingData)
    ScoreProject0: (Link, 0x0, 0x0, FloatTextFormattingData)
    ScoreProject1: (Link, 0x0, 0x0, FloatTextFormattingData)
    MagicalDamage: (Link, 0x0, 0x0, FloatTextFormattingData)
    Dodge: (Link, 0x0, 0x0, FloatTextFormattingData)
    TftUnitLabel: (Link, 0x0, 0x0, FloatTextFormattingData)
    Heal: (Link, 0x0, 0x0, FloatTextFormattingData)
    PracticeToolTotal: (Link, 0x0, 0x0, FloatTextFormattingData)
    ManaDamage: (Link, 0x0, 0x0, FloatTextFormattingData)
    Debug: (Link, 0x0, 0x0, FloatTextFormattingData)
    EnemyTrueDamageCritical: (Link, 0x0, 0x0, FloatTextFormattingData)
    EnemyMagicalDamageCritical: (Link, 0x0, 0x0, FloatTextFormattingData)
    MagicalDamageCritical: (Link, 0x0, 0x0, FloatTextFormattingData)
    Invulnerable: (Link, 0x0, 0x0, FloatTextFormattingData)
    ScoreDarkStar: (Link, 0x0, 0x0, FloatTextFormattingData)
    Absorbed: (Link, 0x0, 0x0, FloatTextFormattingData)
    EnemyPhysicalDamage: (Link, 0x0, 0x0, FloatTextFormattingData)
    Experience: (Link, 0x0, 0x0, FloatTextFormattingData)
    PhysicalDamageCritical: (Link, 0x0, 0x0, FloatTextFormattingData)
    PracticeToolDps: (Link, 0x0, 0x0, FloatTextFormattingData)
    Level: (Link, 0x0, 0x0, FloatTextFormattingData)
    EnemyTrueDamage: (Link, 0x0, 0x0, FloatTextFormattingData)
    QuestReceived: (Link, 0x0, 0x0, FloatTextFormattingData)
    Omw: (Link, 0x0, 0x0, FloatTextFormattingData)
    Countdown: (Link, 0x0, 0x0, FloatTextFormattingData)
    QuestComplete: (Link, 0x0, 0x0, FloatTextFormattingData)
    Disable: (Link, 0x0, 0x0, FloatTextFormattingData)
    EnemyPhysicalDamageCritical: (Link, 0x0, 0x0, FloatTextFormattingData)
    Score: (Link, 0x0, 0x0, FloatTextFormattingData)
    TrueDamageCritical: (Link, 0x0, 0x0, FloatTextFormattingData)
    Special: (Link, 0x0, 0x0, FloatTextFormattingData)
    PracticeToolLastHit: (Link, 0x0, 0x0, FloatTextFormattingData)
    TrueDamage: (Link, 0x0, 0x0, FloatTextFormattingData)
    ShieldBonusDamage: (Link, 0x0, 0x0, FloatTextFormattingData)
    ManaHeal: (Link, 0x0, 0x0, FloatTextFormattingData)
    Gold: (Link, 0x0, 0x0, FloatTextFormattingData)
    PhysicalDamage: (Link, 0x0, 0x0, FloatTextFormattingData)
    pass

class TftCutsceneBeamVfxClip(TftCutsceneVfxClip):
    HideWhenNotViewed: (Bool, 0x0, 0x0, 0x0)
    BlackboardTargetObject: (String, 0x0, 0x0, 0x0)
    Startpoint: (Pointer, 0x0, 0x0, TftCutscenePositionProvider)
    Endpoint: (Pointer, 0x0, 0x0, TftCutscenePositionProvider)
    pass

class HudHealthBarDefenseModifierData():
    DefenseDownL3Percent: (F32, 0x0, 0x0, 0x0)
    DefenseUpPercent: (F32, 0x0, 0x0, 0x0)
    DefenseDownL2Percent: (F32, 0x0, 0x0, 0x0)
    DefenseDownL1Percent: (F32, 0x0, 0x0, 0x0)
    pass

class DisplayBasicStatUiData():
    BasicStatAmount: (Hash, 0x0, 0x0, 0x0)
    BasicIcon: (Hash, 0x0, 0x0, 0x0)
    BasicGroup: (Hash, 0x0, 0x0, 0x0)
    BasicHoverRegion: (Hash, 0x0, 0x0, 0x0)
    BasicStatName: (Hash, 0x0, 0x0, 0x0)
    pass

class PfxAnimatedVector2fVariableData():
    Values: (List, 0x0, Vec2, 0x0)
    Times: (List, 0x0, F32, 0x0)
    ProbabilityTables: (List, 0x2, Pointer, PfxProbabilityTableData)
    pass

class LineTargetToCaster(TargetingTypeData):
    pass

class FxTransform():
    Type: (U32, 0x0, 0x0, 0x0)
    Index: (I32, 0x0, 0x0, 0x0)
    AttachmentName: (String, 0x0, 0x0, 0x0)
    Transform: (Mtx44, 0x0, 0x0, 0x0)
    pass

class UiMetricLatencyText(UiMetricTypeI):
    LatencyText: (Hash, 0x0, 0x0, 0x0)
    pass

class TftFinisherPlayerProxyClient(GameObject):
    pass

class IsOwnerAliveSpawnConditions(IVfxSpawnConditions):
    mConditions: (List, 0x0, Embed, IsOwnerAliveConditionData)
    mDefaultVfxData: (Embed, 0x0, 0x0, VfxDefaultSpawnConditionData)
    pass

class OmwPingRange():
    Message: (String, 0x0, 0x0, 0x0)
    MaxRange: (F32, 0x0, 0x0, 0x0)
    pass

class ElementGroupSliderData(ElementGroupData):
    SliderClickedState: (Embed, 0x0, 0x0, ElementGroupSliderState)
    SliderHitRegion: (Link, 0x0, 0x0, RegionElementData)
    SliderHoveredState: (Embed, 0x0, 0x0, ElementGroupSliderState)
    SoundEvents: (Pointer, 0x0, 0x0, ElementGroupSliderSoundEvents)
    BarHoveredState: (Embed, 0x0, 0x0, ElementGroupSliderState)
    DefaultState: (Embed, 0x0, 0x0, ElementGroupSliderState)
    Direction: (U8, 0x0, 0x0, 0x0)
    BarHitRegion: (Link, 0x0, 0x0, RegionElementData)
    pass

class EsportsBannerData():
    BannerName: (String, 0x0, 0x0, 0x0)
    Team: (U32, 0x0, 0x0, 0x0)
    pass

class RegaliaRankedBannerMap():
    RankingToBannerMap: (Map, String, Link, RegaliaData)
    pass

class ElementGroupGridData(ElementGroupData):
    AllowOverflow: (Bool, 0x0, 0x0, 0x0)
    LayoutType: (U32, 0x0, 0x0, 0x0)
    GridRegion: (Link, 0x0, 0x0, RegionElementData)
    LayoutStyle: (Pointer, 0x0, 0x0, LayoutStyleBase)
    pass

class DynamicMaterialDef(IMaterialDef):
    StaticSwitch: (Pointer, 0x0, 0x0, DynamicMaterialStaticSwitch)
    Parameters: (List, 0x0, Embed, DynamicMaterialParameterDef)
    AllowSkipping: (Bool, 0x0, 0x0, 0x0)
    Textures: (List, 0x0, Embed, DynamicMaterialTextureSwapDef)
    SourceMaterial: (Link, 0x0, 0x0, StaticMaterialDef)
    pass

class TftTextInfoNubData(TftInfoNubData):
    BodyKey: (String, 0x0, 0x0, 0x0)
    TitleKey: (String, 0x0, 0x0, 0x0)
    pass

class 0x2da50c9f():
    OnBarClickedEvent: (String, 0x0, 0x0, 0x0)
    OnDragEndEvent: (String, 0x0, 0x0, 0x0)
    OnDragStartEvent: (String, 0x0, 0x0, 0x0)
    pass

class RegionBoundaryConfig():
    0x240ebb1b: (U8, 0x0, 0x0, 0x0)
    0xb9ace82c: (F32, 0x0, 0x0, 0x0)
    0xbec32eb5: (F32, 0x0, 0x0, 0x0)
    pass

class FontType():
    LocaleTypes: (List, 0x0, Embed, FontLocaleType)
    pass

class ContextualConditionChanceToPlay(IContextualCondition):
    mPercentChanceToPlay: (U8, 0x0, 0x0, 0x0)
    pass

class WidthPerSecond(MissileBehaviorSpec):
    mWidthPerSecond: (F32, 0x0, 0x0, 0x0)
    pass

class MapCloudsLayer():
    Speed: (F32, 0x0, 0x0, 0x0)
    Scale: (F32, 0x0, 0x0, 0x0)
    Direction: (Vec2, 0x0, 0x0, 0x0)
    pass

class ISplineInfo():
    mUseMissilePositionAsOrigin: (Bool, 0x0, 0x0, 0x0)
    mStartPositionOffset: (Vec3, 0x0, 0x0, 0x0)
    pass

class LoadingScreenClassicViewController(LoadingScreenBasicViewController):
    ClashLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    Clash: (Embed, 0x0, 0x0, LoadingScreenClash)
    0xf2af7d00: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxAnimatedVector2fVariableData(VfxVector2fBase):
    Values: (List, 0x0, Vec2, 0x0)
    Times: (List, 0x0, F32, 0x0)
    ProbabilityTables: (List, 0x2, Pointer, VfxProbabilityTableData)
    pass

class ItemRecommendationMatrix():
    Mrows: (List, 0x6, Embed, ItemRecommendationMatrixRow)
    pass

class SpellSlotEqualOrGreaterThanLevelRequirement(ICastRequirement):
    Level: (U32, 0x0, 0x0, 0x0)
    pass

class ParStateData():
    AnimationSuffix: (String, 0x0, 0x0, 0x0)
    TextureSuffix: (String, 0x0, 0x0, 0x0)
    Color: (Color, 0x0, 0x0, 0x0)
    VideoPrefix: (String, 0x0, 0x0, 0x0)
    FadeColor: (Color, 0x0, 0x0, 0x0)
    pass

class ContextualConditionAnyOtherHero(IContextualCondition):
    mChildConditions: (List, 0x0, Pointer, ICharacterSubcondition)
    pass

class ITftBehaviorScriptEvent(IScriptBtEvent):
    pass

class TftCharacterRoleCardItem():
    RecipeGroup: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    ComponentIcons: (List, 0x2, Hash, 0x0)
    ItemIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class InstanceVars(ScriptTable):
    pass

class 0x2f165570(ILolSpellScriptEvent):
    pass

class FloatDefaultTableGet(IFloatGet):
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Table: (Pointer, 0x0, 0x0, RsTable)
    Var: (String, 0x0, 0x0, 0x0)
    Default: (F32, 0x0, 0x0, 0x0)
    pass

class TftLobbyCustomButtonPopupViewController(ModalDialogViewController):
    pass

class PreloadCharacters(IScriptBlock, LevelScriptBlock):
    GroupName: (Hash, 0x0, 0x0, 0x0)
    pass

class ScriptBtRandomSelector(IScriptBt, IScriptSequence):
    Blocks: (List2, 0x0, Pointer, IScriptBlock)
    Blocks: (List2, 0x0, Pointer, IBehaviorScriptBlock)
    pass

class AboveParPercentCastRequirement(ICastRequirement):
    mParType: (U8, 0x0, 0x0, 0x0)
    mCurrentPercentPar: (F32, 0x0, 0x0, 0x0)
    pass

class ScriptPreloadCharacter():
    PreloadResourceName: (String, 0x0, 0x0, 0x0)
    pass

class FlexTypeFloat():
    mValue: (F32, 0x0, 0x0, 0x0)
    mFlexId: (U32, 0x0, 0x0, 0x0)
    mIsUsed: (Bool, 0x0, 0x0, 0x0)
    mTypeValue: (F32, 0x0, 0x0, 0x0)
    mFlexValueId: (U32, 0x0, 0x0, 0x0)
    pass

class TftItemSlotDisplayTemplate():
    Scene: (Hash, 0x0, 0x0, 0x0)
    ItemTransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    0xb1017e3e: (Hash, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    SelectedFrame: (Hash, 0x0, 0x0, 0x0)
    pass

class TimedVariableWaveBehavior(IMinionWaveBehavior):
    DefaultSpawnCount: (I32, 0x0, 0x0, 0x0)
    Behaviors: (List2, 0x0, Embed, TimedWaveBehaviorInfo)
    pass

class PackManagerData():
    CollisionRadius: (F32, 0x0, 0x0, 0x0)
    OrderDelay: (F32, 0x0, 0x0, 0x0)
    0x377491e8: (Pointer, 0x0, 0x0, 0x377491e8)
    RankToFormationMap: (Map, U32, Embed, PackFormationData)
    UiTargetForgivenessRange: (F32, 0x0, 0x0, 0x0)
    TargetForgivenessRange: (F32, 0x0, 0x0, 0x0)
    BuffOverrides: (List, 0x0, Link, SpellObject)
    0x879eb9a2: (String, 0x0, 0x0, 0x0)
    OnLeaderMoveFollowerAnimation: (Hash, 0x0, 0x0, 0x0)
    0xb97a9b92: (Bool, 0x0, 0x0, 0x0)
    OrderTrailingDelay: (F32, 0x0, 0x0, 0x0)
    LeashDistance: (F32, 0x0, 0x0, 0x0)
    0xc4e7b996: (Map, F32, Hash, 0x0)
    AttackMoveTargetForgivenessRange: (F32, 0x0, 0x0, 0x0)
    FollowerCrossoverAnimation: (Hash, 0x0, 0x0, 0x0)
    pass

class LoadingScreenProgressMeter():
    Text: (Hash, 0x0, 0x0, 0x0)
    Meter: (Hash, 0x0, 0x0, 0x0)
    pass

class FunctionTableGet(ScriptTableGet, IFunctionGet):
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Var: (Hash, 0x0, 0x0, 0x0)
    Var: (String, 0x0, 0x0, 0x0)
    pass

class MapCubemapProbe(MapPlaceable):
    VisibilityController: (Link, 0x0, 0x0, IMapVisibilityController)
    CubemapProbeScale: (F32, 0x0, 0x0, 0x0)
    CubemapProbeGroup: (Hash, 0x0, 0x0, 0x0)
    CubemapRegion: (Pointer, 0x0, 0x0, MapCubemapRegion)
    CubemapProbePath: (String, 0x0, 0x0, 0x0)
    pass

class UiMetricTypeI():
    DeviceUx: (I32, 0x0, 0x0, 0x0)
    pass

class ViewControllerFilter_Clash(ViewControllerFilterI):
    pass

class AreaClamped(TargetingTypeData):
    pass

class TftCharacterRecord(CharacterRecord):
    mMoveProximity: (F32, 0x0, 0x0, 0x0)
    mLinkedTraits: (List, 0x0, Embed, TftTraitContributionData)
    mLinkedTraits: (List, 0x0, Link, TftTraitData)
    UnitPropertyOverrides: (List, 0x0, Embed, TftUnitPropertyOverride)
    OmitFromCombatRecap: (Bool, 0x0, 0x0, 0x0)
    MobileHealthBarHeightOverride: (Option, 0x0, F32, 0x0)
    NumToCombine: (U8, 0x0, 0x0, 0x0)
    mIsDiscoverable: (Bool, 0x0, 0x0, 0x0)
    mUnitInfoCardAttachToBone: (String, 0x0, 0x0, 0x0)
    mInitialMana: (F32, 0x0, 0x0, 0x0)
    Tier: (U8, 0x0, 0x0, 0x0)
    mMoveRange: (F32, 0x0, 0x0, 0x0)
    0x7161d081: (Bool, 0x0, 0x0, 0x0)
    mManaPerAttack: (F32, 0x0, 0x0, 0x0)
    BoardCountContribution: (U8, 0x0, 0x0, 0x0)
    mMoveHeight: (F32, 0x0, 0x0, 0x0)
    CharacterRole: (Link, 0x0, 0x0, TftCharacterRoleData)
    0xbb71cb89: (Bool, 0x0, 0x0, 0x0)
    CharacterRoles: (List, 0x1, Link, TftCharacterRoleData)
    CharacterRoles: (List, 0x2, Link, TftCharacterRoleData)
    UnitInfoCardDisplayType: (U32, 0x0, 0x0, 0x0)
    mUnitInfoCardWorldOffset: (Vec3, 0x0, 0x0, 0x0)
    OmitFromMatchHistory: (Bool, 0x0, 0x0, 0x0)
    mMoveInterval: (F32, 0x0, 0x0, 0x0)
    mShopData: (Link, 0x0, 0x0, TftShopData)
    LinkedUnits: (List2, 0x0, Hash, 0x0)
    mUsesAbilityPower: (Bool, 0x0, 0x0, 0x0)
    PortraitIcon: (String, 0x0, 0x0, 0x0)
    ShowItemsUnsorted: (Bool, 0x0, 0x0, 0x0)
    0xf94987a3: (Bool, 0x0, 0x0, 0x0)
    0xfe0d6477: (List2, 0x0, U32, 0x0)
    pass

class 0x304e703f():
    OwnerChampion: (Hash, 0x0, 0x0, 0x0)
    OwnerChampion: (Link, 0x0, 0x0, Champion)
    pass

class 0x30aa7360():
    pass

class LearnedSpellDynamicMaterialBoolDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    mSlot: (U8, 0x0, 0x0, 0x0)
    pass

class GameScript(Rscript):
    PreloadData: (Embed, 0x0, 0x0, LolSpellPreloadData)
    Functions: (Map, Hash, Embed, ScriptFunction)
    CustomSequences: (Map, Hash, Embed, RootScriptSequence)
    CustomSequences: (Map, Hash, Embed, ScriptSequence)
    ScriptName: (String, 0x0, 0x0, 0x0)
    IsEnabled: (Bool, 0x0, 0x0, 0x0)
    GlobalProperties: (Embed, 0x0, 0x0, ScriptGlobalProperties)
    Sequences: (Map, Hash, Embed, RootScriptSequence)
    Sequences: (Map, Hash, Embed, ScriptSequence)
    pass

class SineMaterialDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    mBias: (F32, 0x0, 0x0, 0x0)
    mFrequency: (F32, 0x0, 0x0, 0x0)
    mScale: (F32, 0x0, 0x0, 0x0)
    mDriver: (Pointer, 0x0, 0x0, IDynamicMaterialFloatDriver)
    mDriver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class ComparisonScriptCondition(IScriptCondition):
    Operation: (U32, 0x0, 0x0, 0x0)
    Value2: (Pointer, 0x0, 0x0, IScriptValueGet)
    Value1: (Pointer, 0x0, 0x0, IScriptValueGet)
    pass

class RecSpellRankUpInfo():
    mDefaultPriority: (List, 0x4, U32, 0x0)
    mDefaultPriority: (List, 0x4, U8, 0x0)
    mEarlyLevelOverrides: (List, 0x0, U32, 0x0)
    mEarlyLevelOverrides: (List, 0x0, U8, 0x0)
    0x5b968ffb: (Bool, 0x0, 0x0, 0x0)
    ModeNameStringId: (Hash, 0x0, 0x0, 0x0)
    IsDefaultRecommendation: (Bool, 0x0, 0x0, 0x0)
    Position: (Hash, 0x0, 0x0, 0x0)
    MapId: (U32, 0x0, 0x0, 0x0)
    IsDefaultPosition: (Bool, 0x0, 0x0, 0x0)
    pass

class GamepadAxisInputSourceFloat(IInputSourceFloat):
    Invert: (Bool, 0x0, 0x0, 0x0)
    Axis: (U8, 0x0, 0x0, 0x0)
    Clamp: (Vec2, 0x0, 0x0, 0x0)
    pass

class ShaderTexture():
    DefaultTexturePath: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class 0x31f7aded(ISequenceActionInstance):
    pass

class VfxShapeVolume(IVfxShape):
    Flags: (U8, 0x0, 0x0, 0x0)
    pass

class 0x31ff922d():
    0x37efaba6: (Bool, 0x0, 0x0, 0x0)
    RoundDamage: (U8, 0x0, 0x0, 0x0)
    0xecf20ef8: (U8, 0x0, 0x0, 0x0)
    pass

class ScoreboardViewController(ViewController):
    OverlayScene: (Hash, 0x0, 0x0, 0x0)
    Team2AllyGlow: (Hash, 0x0, 0x0, 0x0)
    MainTooltipAnchor: (Hash, 0x0, 0x0, 0x0)
    Team2SwapHoverIcon: (Hash, 0x0, 0x0, 0x0)
    Team1SwapHoverIcon: (Hash, 0x0, 0x0, 0x0)
    ScoreboardScene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    UiData: (Embed, 0x0, 0x0, ScoreboardUiData)
    ChaosScoreLineUiData: (Pointer, 0x0, 0x0, ScoreLineBaseUiData)
    DragOverlayScene: (Hash, 0x0, 0x0, 0x0)
    Team1AllyGlow: (Hash, 0x0, 0x0, 0x0)
    ChaosObjectiveBountiesData: (Pointer, 0x0, 0x0, SbObjectiveBounties)
    OrderObjectiveBountiesData: (Pointer, 0x0, 0x0, SbObjectiveBounties)
    Team1EnemyGlow: (Hash, 0x0, 0x0, 0x0)
    OrderScoreLineUiData: (Pointer, 0x0, 0x0, ScoreLineBaseUiData)
    ChaosTeamIdentity: (Pointer, 0x0, 0x0, UiTeamIdentityData)
    TeamScoresDefinitions: (Pointer, 0x0, 0x0, ScoreboardTeamScoresDefinitions)
    0xb01c9387: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    Team1SwapDragTarget: (Hash, 0x0, 0x0, 0x0)
    Team1ReportModalAnchor: (Hash, 0x0, 0x0, 0x0)
    DragonUiLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    SummonerSocialCard: (Pointer, 0x0, 0x0, UiSummonerSocialCardData)
    Team2ReportModalAnchor: (Hash, 0x0, 0x0, 0x0)
    Team2EnemyGlow: (Hash, 0x0, 0x0, 0x0)
    Team2SwapDragTarget: (Hash, 0x0, 0x0, 0x0)
    ObjectName: (String, 0x0, 0x0, 0x0)
    OrderTeamIdentity: (Pointer, 0x0, 0x0, UiTeamIdentityData)
    PlayerSlotHeightReference: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionCharacterPlayingEmote(ICharacterSubcondition):
    mEmoteId: (U8, 0x0, 0x0, 0x0)
    pass

class NextBuffVarsTable(ScriptTable):
    pass

class MatchHistoryTraitTemplate():
    FrameLevelsSelected: (List, 0x0, Hash, 0x0)
    FrameLevelsSelected: (List, 0x4, Hash, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    FrameLevels: (List, 0x0, Hash, 0x0)
    FrameLevels: (List, 0x4, Hash, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    TooltipButton: (Hash, 0x0, 0x0, 0x0)
    pass

class SlowCrowdControlFilter(IStatStoneLogicDriver):
    pass

class Target(TargetingTypeData):
    mCanCompleteCastWithoutTarget: (Bool, 0x0, 0x0, 0x0)
    0xfb5bbd7: (Bool, 0x0, 0x0, 0x0)
    pass

class LoadoutDamageSkinInfoPanel(ILoadoutInfoPanel):
    GamePassIcon: (Hash, 0x0, 0x0, 0x0)
    UnownedTierButton: (List, 0x3, Hash, 0x0)
    RarityIcon: (List, 0x5, Hash, 0x0)
    TierButton: (List, 0x3, Hash, 0x0)
    LockIcon: (List, 0x3, Hash, 0x0)
    ItemIconText: (Hash, 0x0, 0x0, 0x0)
    ItemIcon: (Hash, 0x0, 0x0, 0x0)
    0xee425ddc: (Hash, 0x0, 0x0, 0x0)
    pass

class MapActionAnimationData():
    ForceRestart: (Bool, 0x0, 0x0, 0x0)
    Looping: (Bool, 0x0, 0x0, 0x0)
    AnimationName: (String, 0x0, 0x0, 0x0)
    pass

class LockRootOrientationRigPoseModifierData(BaseRigPoseModifierData):
    pass

class IntensityLogicDriverLightUpdater(IMapLightUpdater):
    Driver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class FxActionTftCameraAnimationInstance(ISequenceActionInstance, IFxActionInstance):
    pass

class MapAlternateAssets():
    mAlternateAssets: (List, 0x0, Embed, MapAlternateAsset)
    pass

class StatStoneMasteryEffectLookup():
    SetsCompletedToBackgroundEffects: (Map, U32, Link, StatStoneMasteryEffects)
    pass

class SummonerNameUiData():
    SummonerNameText: (Hash, 0x0, 0x0, 0x0)
    pass

class SinglePurchaseDialog(PurchaseDialogBase):
    SingleTitleText: (Hash, 0x0, 0x0, 0x0)
    SinglePurchaseItemIcon: (Hash, 0x0, 0x0, 0x0)
    SingleCloseButtonRegion: (Hash, 0x0, 0x0, 0x0)
    SingleScene: (Hash, 0x0, 0x0, 0x0)
    SingleBodyText: (Hash, 0x0, 0x0, 0x0)
    pass

class TftPassCurrencyInfo():
    Id: (String, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class ResourceMeterBaseData():
    pass

class TftTierEntry():
    Count: (I32, 0x0, 0x0, 0x0)
    ShopData: (Link, 0x0, 0x0, TftShopData)
    pass

class SkinCharacterDataProperties_CharacterIdleEffect():
    BoneName: (String, 0x0, 0x0, 0x0)
    EffectName: (String, 0x0, 0x0, 0x0)
    Position: (Vec3, 0x0, 0x0, 0x0)
    EffectKey: (Hash, 0x0, 0x0, 0x0)
    TargetBoneName: (String, 0x0, 0x0, 0x0)
    pass

class TftGameVariationData():
    mName: (String, 0x0, 0x0, 0x0)
    mAnnouncementData: (Link, 0x0, 0x0, TftAnnouncementData)
    mTooltipIconPath: (String, 0x0, 0x0, 0x0)
    mTooltipTitleTra: (String, 0x0, 0x0, 0x0)
    mTooltipDescriptionTra: (String, 0x0, 0x0, 0x0)
    mStageIconPath: (String, 0x0, 0x0, 0x0)
    pass

class 0x3316a795(TargetingTypeData):
    pass

class NamedDataValueCalculationPart(IGameCalculationPart, ISpellCalculationPart):
    mDataValue: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x333fb750():
    pass

class SequenceTableEntry():
    Sequence: (Link, 0x0, 0x0, Sequence)
    Type: (Link, 0x0, 0x0, SequenceType)
    pass

class IconLink():
    ClickedIcon: (Hash, 0x0, 0x0, 0x0)
    ActiveIcon: (Hash, 0x0, 0x0, 0x0)
    DisabledIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class UseAutoattackCastTimeData():
    mAutoattackCastTimeCalculation: (Pointer, 0x0, 0x0, IGameCalculation)
    mUseCastTimeAsTotalTime: (Bool, 0x0, 0x0, 0x0)
    pass

class TargeterDefinitionLine(TargeterDefinition):
    MaxAngleFadeCos: (F32, 0x0, 0x0, 0x0)
    MinAngleRangeFactor: (F32, 0x0, 0x0, 0x0)
    LineWidth: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    FadeAngle: (F32, 0x0, 0x0, 0x0)
    TextureBaseMaxGrowName: (String, 0x0, 0x0, 0x0)
    UseGlobalLineIndicator: (Bool, 0x0, 0x0, 0x0)
    MinAngleFadeCos: (F32, 0x0, 0x0, 0x0)
    TextureBaseOverrideName: (String, 0x0, 0x0, 0x0)
    mCenterArrowToEndPoint: (Bool, 0x0, 0x0, 0x0)
    MaxAngleCos: (F32, 0x0, 0x0, 0x0)
    IndicatorType: (Pointer, 0x0, 0x0, ILineIndicatorType)
    TextureTargetOverrideName: (String, 0x0, 0x0, 0x0)
    RangeGrowthMax: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    EndLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    FacingLine: (Bool, 0x0, 0x0, 0x0)
    LineStopsAtEndPosition: (Bool, 0x0, 0x0, 0x0)
    LineStopsAtEndPosition: (Option, 0x0, Bool, 0x0)
    AlwaysDraw: (Bool, 0x0, 0x0, 0x0)
    RangeGrowthDuration: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    MaxAngleRangeFactor: (F32, 0x0, 0x0, 0x0)
    MaxAngle: (F32, 0x0, 0x0, 0x0)
    mAngleLineToEndpointHeight: (Bool, 0x0, 0x0, 0x0)
    FallbackDirection: (U32, 0x0, 0x0, 0x0)
    ArrowSize: (F32, 0x0, 0x0, 0x0)
    MinAngleCos: (F32, 0x0, 0x0, 0x0)
    RangeGrowthStartTime: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    MinimumDisplayedRange: (F32, 0x0, 0x0, 0x0)
    StartLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    OverrideBaseRange: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    HasMaxGrowRange: (Bool, 0x0, 0x0, 0x0)
    TextureTargetMaxGrowName: (String, 0x0, 0x0, 0x0)
    Fade: (Bool, 0x0, 0x0, 0x0)
    MinAngle: (F32, 0x0, 0x0, 0x0)
    pass

class DeathRecapShowcasePips():
    PipOnIcon: (Hash, 0x0, 0x0, 0x0)
    Layout: (Hash, 0x0, 0x0, 0x0)
    PipGroup: (Hash, 0x0, 0x0, 0x0)
    pass

class LoadingScreenPlayerCardSwitcherViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    CardSwitcher: (Embed, 0x0, 0x0, LoadingScreenPlayerCardSwitcherData)
    pass

class BuffDisplayList():
    BuffDisplayTemplate: (Embed, 0x0, 0x0, BuffDisplayData)
    Layout: (Hash, 0x0, 0x0, 0x0)
    MaxBuffDisplayCount: (U32, 0x0, 0x0, 0x0)
    pass

class CharacterQuestDefinitionsData():
    0x869c3e32: (List2, 0x0, Pointer, 0x7b40445f)
    QuestName: (String, 0x0, 0x0, 0x0)
    IsEnabled: (Bool, 0x0, 0x0, 0x0)
    pass

class X3dSharedData():
    Textures: (List, 0x0, Embed, X3dSharedTextureDef)
    ConstantBuffers: (List, 0x0, Link, X3dSharedConstantBufferDef)
    pass

class UiElementGroupFramedData(UiElementGroupData):
    FrameElement: (Link, 0x0, 0x0, UiElementIconData)
    FrameElement: (Link, 0x0, 0x0, IconElementData)
    pass

class 0x347698ff(0x6a6e3b03):
    0x2ab3b60a: (Bool, 0x0, 0x0, 0x0)
    0x36678f17: (Bool, 0x0, 0x0, 0x0)
    0x4e1e2198: (Bool, 0x0, 0x0, 0x0)
    0x735e6c1c: (Bool, 0x0, 0x0, 0x0)
    0xbb01454d: (Bool, 0x0, 0x0, 0x0)
    pass

class ContextualConditionSpellSlot(IContextualConditionSpell, IContextualCondition):
    mSpellSlot: (U32, 0x0, 0x0, 0x0)
    mSpellSlot: (U8, 0x0, 0x0, 0x0)
    pass

class 0x349845d9(ViewControllerFilterI):
    TftSetData: (String, 0x0, 0x0, 0x0)
    pass

class 0x34cca270():
    Subtitle: (Hash, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    ModalUpperLeftAnchor: (Hash, 0x0, 0x0, 0x0)
    ButtonIcon: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    TitleBackground: (Hash, 0x0, 0x0, 0x0)
    Title: (Hash, 0x0, 0x0, 0x0)
    SubtitleBackground: (Hash, 0x0, 0x0, 0x0)
    ButtonIcons: (List2, 0x0, Hash, 0x0)
    pass

class 0x34d37457():
    0x77721473: (List2, 0x0, Embed, 0xdec5122e)
    0xb0a8523e: (List2, 0x0, Link, TftItemData)
    0xf6e276c: (Embed, 0x0, 0x0, 0x20b66cd9)
    pass

class ContextualConditionKillCount(IContextualCondition):
    mCompareOp: (U8, 0x0, 0x0, 0x0)
    mTotalKills: (U16, 0x0, 0x0, 0x0)
    pass

class 0x34f43159(0x6ca3cfd):
    0x3a302e74: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    ValueArray: (List2, 0x0, Pointer, 0x6ca3cfd)
    pass

class TerrainType(TargetingTypeData):
    mWallCursor: (Embed, 0x0, 0x0, CursorData)
    mBrushCursor: (Embed, 0x0, 0x0, CursorData)
    mRiverCursor: (Embed, 0x0, 0x0, CursorData)
    pass

class OverridePerkSelectionSet():
    mPerks: (List, 0x0, Link, Perk)
    mStyle: (Link, 0x0, 0x0, PerkStyle)
    mSubStyle: (Link, 0x0, 0x0, PerkStyle)
    pass

class 0x3519dc31():
    0x125ffd9b: (F32, 0x0, 0x0, 0x0)
    CameoPortraitIcon: (Hash, 0x0, 0x0, 0x0)
    0x6c42f089: (Hash, 0x0, 0x0, 0x0)
    0x93412050: (Hash, 0x0, 0x0, 0x0)
    CameoTooltipAnchor: (Hash, 0x0, 0x0, 0x0)
    0xb26cff08: (Hash, 0x0, 0x0, 0x0)
    CameoPortraitRegion: (Hash, 0x0, 0x0, 0x0)
    0xf02bce06: (Hash, 0x0, 0x0, 0x0)
    0xfc5bf017: (Hash, 0x0, 0x0, 0x0)
    pass

class ValueProcessorData():
    pass

class OptionTemplateSecondaryHotkeys_Button():
    ButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class PingRadialViewController(RadialMenuViewController, PingRadialBaseViewController):
    CategoryText: (List, 0x0, Hash, 0x0)
    CategoryText: (List, 0x5, Hash, 0x0)
    pass

class 0x3562d439(0xca4d32d1):
    Source: (Link, 0x0, 0x0, SequenceObjectSelector)
    pass

class TftMapTransitionPositions(MapTransitionPositions):
    pass

class 0x359681d9(0x87a6a884):
    pass

class CherryScoreboardViewController(ViewController):
    MainTooltipAnchor: (Hash, 0x0, 0x0, 0x0)
    TeamBanners: (List2, 0x0, Hash, 0x0)
    MatchupHistoryData: (Pointer, 0x0, 0x0, 0x8444401a)
    ScoreboardScene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TeamPositions: (List, 0x0, Hash, 0x0)
    TeamPositions: (List2, 0x0, Hash, 0x0)
    ReportModalAnchor: (Hash, 0x0, 0x0, 0x0)
    ScoreLineUi: (Pointer, 0x0, 0x0, ScoreLineBaseUiData)
    ScoreLineUi: (Pointer, 0x0, 0x0, ScoreLineCherryUiData)
    0xb1f34e3f: (Pointer, 0x0, 0x0, 0xf2dd2d14)
    0xca86315a: (List2, 0x0, Hash, 0x0)
    SummonerSocialCard: (Pointer, 0x0, 0x0, UiSummonerSocialCardData)
    TeamIcons: (List, 0x0, Hash, 0x0)
    TeamIcons: (List2, 0x0, Hash, 0x0)
    PlayerSlotHeightReference: (Hash, 0x0, 0x0, 0x0)
    TeamData: (List2, 0x0, Embed, 0x69057401)
    pass

class SetModePreloadFlags(LevelScriptBlock):
    ModePreloadFlags: (Pointer, 0x0, 0x0, IIntGet)
    pass

class DestroyOnDistanceFromCaster(MissileBehaviorSpec):
    mDistance: (F32, 0x0, 0x0, 0x0)
    pass

class WeightedSelectionCalculator():
    TimeLimitSeconds: (F32, 0x0, 0x0, 0x0)
    PercentageHeadSamplesToDrop: (F32, 0x0, 0x0, 0x0)
    PrioritizeTailSample: (Bool, 0x0, 0x0, 0x0)
    Weights: (List, 0x0, F32, 0x0)
    StopIfOverMaxNumDifferentCategories: (Bool, 0x0, 0x0, 0x0)
    NumMaxDifferentCategories: (U32, 0x0, 0x0, 0x0)
    PercentageTailSamplesToDrop: (F32, 0x0, 0x0, 0x0)
    pass

class 0x35d3f11a(IScriptBlock):
    pass

class IScriptSequence(Rscript):
    pass

class EnchantmentGroup():
    mEnchantments: (List, 0x0, I32, 0x0)
    mEnchantmentIds: (List, 0x0, I32, 0x0)
    mBaseItems: (List, 0x0, I32, 0x0)
    mItemIdRangeMaximum: (I32, 0x0, 0x0, 0x0)
    mItemIdRangeMaximum: (U32, 0x0, 0x0, 0x0)
    mBaseItemIds: (List, 0x0, I32, 0x0)
    mCanSidegrade: (Bool, 0x0, 0x0, 0x0)
    mItemIdRangeMinimum: (I32, 0x0, 0x0, 0x0)
    mItemIdRangeMinimum: (U32, 0x0, 0x0, 0x0)
    pass

class TooltipInstanceItem(TooltipInstance):
    pass

class TftHexToRangeTranslation():
    HexNumber: (U32, 0x0, 0x0, 0x0)
    RawRange: (F32, 0x0, 0x0, 0x0)
    pass

class MinMaterialDriver(IDynamicMaterialDriver, ILogicDriver):
    mDrivers: (List, 0x0, Pointer, IDynamicMaterialDriver)
    mDrivers: (List, 0x0, Pointer, ILogicDriver)
    pass

class GearSelectionViewController(ViewController):
    ToggleScene: (Hash, 0x0, 0x0, 0x0)
    CooldownAnimations: (List, 0x0, Hash, 0x0)
    Loadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    ToggleButton: (Hash, 0x0, 0x0, 0x0)
    GearMenuScene: (Hash, 0x0, 0x0, 0x0)
    GearButtons: (List, 0x0, Hash, 0x0)
    IntroAnimations: (List, 0x0, Hash, 0x0)
    EnabledAnimations: (List, 0x0, Hash, 0x0)
    SelectionButtonCooldownSecs: (F32, 0x0, 0x0, 0x0)
    pass

class TftShopMobileDelays():
    CloseReminderDelaySecs: (F32, 0x0, 0x0, 0x0)
    AutoOpenShopInPlanningPhaseDelaySecs: (F32, 0x0, 0x0, 0x0)
    pass

class RootScriptSequence(ScriptSequence):
    pass

class TftScoreboardNotificationTemplate():
    NotificationBottomIcon2: (Hash, 0x0, 0x0, 0x0)
    NotificationIcon: (Hash, 0x0, 0x0, 0x0)
    NotificationBottomIcon3: (Hash, 0x0, 0x0, 0x0)
    NotificationTopline: (Hash, 0x0, 0x0, 0x0)
    NotificationTitle: (Hash, 0x0, 0x0, 0x0)
    TransitionOut: (Embed, 0x0, 0x0, HudMenuTransitionData)
    TransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    NotificationScene: (Hash, 0x0, 0x0, 0x0)
    NotificationBottomline: (Hash, 0x0, 0x0, 0x0)
    NotificationBottomIcon1: (Hash, 0x0, 0x0, 0x0)
    pass

class TftPassLevel():
    ImageOverridePath: (String, 0x0, 0x0, 0x0)
    IsKeystone: (Bool, 0x0, 0x0, 0x0)
    MilestoneId: (String, 0x0, 0x0, 0x0)
    NameTraKey: (String, 0x0, 0x0, 0x0)
    PassRewards: (List2, 0x0, Pointer, TftPassRewardBase)
    IsPremium: (Bool, 0x0, 0x0, 0x0)
    0x96f93ea0: (U32, 0x0, 0x0, 0x0)
    Rewards: (List2, 0x0, Pointer, TftPassRewardBase)
    XpRequired: (U32, 0x0, 0x0, 0x0)
    DescriptionTraKey: (String, 0x0, 0x0, 0x0)
    ImageOverride: (Hash, 0x0, 0x0, 0x0)
    IsBonus: (Bool, 0x0, 0x0, 0x0)
    pass

class FinisherParticleData():
    FinisherParticleId: (U32, 0x0, 0x0, 0x0)
    FinisherParticleTroyFile: (String, 0x0, 0x0, 0x0)
    FinisherParticleFriendlyName: (String, 0x0, 0x0, 0x0)
    pass

class LogicDriverSource():
    pass

class AudioSystemDataProperties():
    SystemTagEventList: (List, 0x0, Embed, AudioTagListProperties)
    pass

class TftShopDataList():
    ShopDatas: (List, 0x0, Link, TftShopData)
    pass

class SubteamSurrenderViewController(VotePanelViewController):
    DefaultTitleTra: (String, 0x0, 0x0, 0x0)
    DoneVotingTitleTra: (String, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class VoiceChatViewController(ViewController):
    PlayerSlotData: (Embed, 0x0, 0x0, VoiceChatViewPlayerSlotData)
    PlayerGrid: (Hash, 0x0, 0x0, 0x0)
    ErrorText: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TftOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    ConnectedBgRegionHandle: (Hash, 0x0, 0x0, 0x0)
    PlayerSlotRegionHandle: (Hash, 0x0, 0x0, 0x0)
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    SelfSlot: (Embed, 0x0, 0x0, VoiceChatViewSelfSlot)
    PanelSceneHandle: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x36cad521():
    Banners: (List, 0x0, Link, 0x839f4f73)
    pass

class VfxDefaultSpawnConditionData(VfxSpawnConditionData):
    pass

class GoldSourceFilter(IStatStoneLogicDriver):
    ValidGoldSource: (U8, 0x0, 0x0, 0x0)
    pass

class TftHudUnitShopData():
    0x88606883: (F32, 0x0, 0x0, 0x0)
    0xc38c6ba9: (F32, 0x0, 0x0, 0x0)
    pass

class TftCutsceneScaleClip(TftCutsceneClip):
    Scale: (Vec3, 0x0, 0x0, 0x0)
    BlackboardGameObject: (String, 0x0, 0x0, 0x0)
    pass

class X3dSharedTextureDef():
    Register: (I32, 0x0, 0x0, 0x0)
    Frequency: (U8, 0x0, 0x0, 0x0)
    Type: (U32, 0x0, 0x0, 0x0)
    Type: (U8, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    BindLocation: (U32, 0x0, 0x0, 0x0)
    IsCurrentFramebufferDepthRead: (Bool, 0x0, 0x0, 0x0)
    PlatformMask: (U32, 0x0, 0x0, 0x0)
    pass

class ChildMissileParentRepulsion(MissileBehaviorSpec):
    mRepulsionModel: (U32, 0x0, 0x0, 0x0)
    mParentRepulsion: (F32, 0x0, 0x0, 0x0)
    mMaxSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class 0x3764abee(IScriptBlock, IBehaviorScriptBlock):
    Sequence: (Embed, 0x0, 0x0, ScriptBtSelector)
    pass

class HudVoiceChatData():
    HighlightTimeoutSeconds: (F32, 0x0, 0x0, 0x0)
    pass

class UiElementEffectInstancedData(UiElementEffectData):
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    mColor: (Color, 0x0, 0x0, 0x0)
    Offsets: (List, 0x0, Vec2, 0x0)
    TextureData: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mAtlas: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x376e71c2(ViewController):
    ChallengeTitleTooltipData: (Embed, 0x0, 0x0, 0x9b1b08e6)
    0x32925e75: (Embed, 0x0, 0x0, 0xf8739c73)
    0x4c6557d5: (Hash, 0x0, 0x0, 0x0)
    0x6f003bbf: (Embed, 0x0, 0x0, 0x9e380c11)
    0xe44c2603: (Hash, 0x0, 0x0, 0x0)
    TooltipTitleScene: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x377491e8():
    pass

class 0x37841b56(0xe561be2e):
    Value: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x37a8385c():
    ItemSlots: (Embed, 0x0, 0x0, DetailedItemSlots)
    ExpandedRegion: (Hash, 0x0, 0x0, 0x0)
    TeamFrameRegion: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    BuffDisplay: (Embed, 0x0, 0x0, 0x3aee5d80)
    SummonerName: (Embed, 0x0, 0x0, SummonerNameUiData)
    pass

class ChangeHeightSolver(MissileTriggeredActionSpec):
    mOverrideHeightSolver: (Pointer, 0x0, 0x0, HeightSolverType)
    pass

class 0x37ccf49():
    Id: (String, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class EmoteRadialViewController(RadialMenuViewController):
    EmoteIcons: (List, 0x0, Hash, 0x0)
    EmoteIcons: (List, 0x5, Hash, 0x0)
    pass

class HudHealthBarDefenseIconData():
    EnlargeSize: (F32, 0x0, 0x0, 0x0)
    SettleTime: (F32, 0x0, 0x0, 0x0)
    EnlargeTime: (F32, 0x0, 0x0, 0x0)
    pass

class 0x38638e52(IGameModeConfig):
    0x32bb3d02: (Bool, 0x0, 0x0, 0x0)
    0x44fa071c: (U32, 0x0, 0x0, 0x0)
    0x4f3f87f4: (U32, 0x0, 0x0, 0x0)
    0x5ffba43f: (U32, 0x0, 0x0, 0x0)
    0x6f2e6a0d: (U32, 0x0, 0x0, 0x0)
    0xd2335df3: (U32, 0x0, 0x0, 0x0)
    pass

class HudItemShopItemGroupDefinition():
    EpicnessesInGroup: (List, 0x0, U8, 0x0)
    GroupName: (String, 0x0, 0x0, 0x0)
    pass

class 0x38749c0a(TftCutsceneMissileClip):
    MissileSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class GetSizeOfCustomTableBlock(IScriptBlock):
    Size: (Embed, 0x0, 0x0, ScriptTableSet)
    Table: (Embed, 0x0, 0x0, CustomTableGet)
    OutSize: (Embed, 0x0, 0x0, ScriptTableSet)
    CustomTable: (Embed, 0x0, 0x0, CustomTableGet)
    pass

class AddExperienceCheat(Cheat):
    mTarget: (U32, 0x0, 0x0, 0x0)
    mGiveMaxLevel: (Bool, 0x0, 0x0, 0x0)
    pass

class TftCharacterRoleCardItemRowData():
    Group: (Hash, 0x0, 0x0, 0x0)
    Icons: (List, 0x4, Hash, 0x0)
    pass

class TrailComponentData(GameComponentData):
    mLength: (F32, 0x0, 0x0, 0x0)
    mSegmentCount: (I32, 0x0, 0x0, 0x0)
    pass

class IDebugScriptBlock(IScriptBlock):
    pass

class 0x38a77cab():
    ObjectPath: (Hash, 0x0, 0x0, 0x0)
    SharedTextures: (List, 0x0, Embed, X3dSharedTextureDef)
    SharedConstantBuffers: (List, 0x0, Link, X3dSharedConstantBufferDef)
    pass

class 0x38a7f9b3():
    IsDisabled: (Bool, 0x0, 0x0, 0x0)
    pass

class MapNavigationGridOverlay():
    Filename: (String, 0x0, 0x0, 0x0)
    NavGridFileName: (String, 0x0, 0x0, 0x0)
    RegionsFilename: (String, 0x0, 0x0, 0x0)
    pass

class LiveFeatureToggles():
    mLolToggles: (Embed, 0x0, 0x0, LolFeatureToggles)
    mGameplayToggles: (Embed, 0x0, 0x0, GameplayFeatureToggles)
    mEngineToggles: (Embed, 0x0, 0x0, EngineFeatureToggles)
    pass

class BorderSkinAugment(ISkinAugment):
    Border: (Pointer, 0x0, 0x0, BorderPropertyData)
    pass

class MapSkinColorizationPostEffect():
    mMultipliersRgb: (Vec3, 0x0, 0x0, 0x0)
    mMultipliersSaturation: (F32, 0x0, 0x0, 0x0)
    pass

class MinimapIconColorData():
    mBase: (Color, 0x0, 0x0, 0x0)
    mColorblind: (Option, 0x0, Color, 0x0)
    pass

class NeutralTimerData():
    SourceIcons: (List, 0x0, Embed, NeutralTimerSourceIconData)
    mTooltipCampName: (String, 0x0, 0x0, 0x0)
    0x3995c23b: (Bool, 0x0, 0x0, 0x0)
    mSourceIcons: (Map, Hash, Embed, NeutralTimerSourceIconData)
    mTimerKeyName: (String, 0x0, 0x0, 0x0)
    TimerName: (Hash, 0x0, 0x0, 0x0)
    TooltipRespawn: (String, 0x0, 0x0, 0x0)
    TooltipChatNameChaos: (String, 0x0, 0x0, 0x0)
    mTooltipChatNameChaos: (String, 0x0, 0x0, 0x0)
    TimerElements: (Embed, 0x0, 0x0, NeutralTimerElements)
    TimerKeyName: (String, 0x0, 0x0, 0x0)
    TimerKeyName: (U16, 0x0, 0x0, 0x0)
    mTooltipRespawn: (String, 0x0, 0x0, 0x0)
    TooltipCampName: (String, 0x0, 0x0, 0x0)
    TooltipChatNameOrder: (String, 0x0, 0x0, 0x0)
    Tooltip: (String, 0x0, 0x0, 0x0)
    mTooltipChatNameOrder: (String, 0x0, 0x0, 0x0)
    CampName: (Hash, 0x0, 0x0, 0x0)
    mTooltip: (String, 0x0, 0x0, 0x0)
    pass

class 0x3985a371(IFxActionInstance):
    pass

class UiElementIData():
    mName: (String, 0x0, 0x0, 0x0)
    Scene: (Link, 0x0, 0x0, UiSceneData)
    Scene: (Link, 0x0, 0x0, SceneData)
    Name: (String, 0x0, 0x0, 0x0)
    mScene: (Link, 0x0, 0x0, SceneData)
    pass

class CircleMovement(MissileMovementSpec):
    mAngularVelocity: (F32, 0x0, 0x0, 0x0)
    mLinearVelocity: (F32, 0x0, 0x0, 0x0)
    mRadialVelocity: (F32, 0x0, 0x0, 0x0)
    mLifetime: (F32, 0x0, 0x0, 0x0)
    pass

class SocialActionsDialogViewController(ModalDialogViewController):
    ActionButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    BlockPlayerIcon: (Hash, 0x0, 0x0, 0x0)
    OpenPartyStatusIcon: (Hash, 0x0, 0x0, 0x0)
    OnlineStatusIcon: (Hash, 0x0, 0x0, 0x0)
    InviteToLobbyIcon: (Hash, 0x0, 0x0, 0x0)
    MobileAppStatusIcon: (Hash, 0x0, 0x0, 0x0)
    OfflineStatusIcon: (Hash, 0x0, 0x0, 0x0)
    SummonerNameText: (Hash, 0x0, 0x0, 0x0)
    IngameStatusIcon: (Hash, 0x0, 0x0, 0x0)
    SocialStatusIcons: (Embed, 0x0, 0x0, SocialStatusIcons)
    ButtonsRegion: (Hash, 0x0, 0x0, 0x0)
    AwayStatusIcon: (Hash, 0x0, 0x0, 0x0)
    RemoveFriendIcon: (Hash, 0x0, 0x0, 0x0)
    PlayerPortrait: (Hash, 0x0, 0x0, 0x0)
    pass

class UiElementEffectArcFillData(UiElementEffectData):
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    TextureData: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mAtlas: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    pass

class EventResourceData():
    mName: (String, 0x0, 0x0, 0x0)
    mEventNameHashList: (List, 0x0, Embed, 0x3ac5d197)
    mEventFrameList: (List, 0x0, Embed, 0x11efc9e9)
    mFlags: (U16, 0x0, 0x0, 0x0)
    mEventDataList: (List, 0x0, Pointer, BaseEventData)
    mId: (U32, 0x0, 0x0, 0x0)
    pass

class EncounterUiTunables():
    mProgressMeterSuffix: (String, 0x0, 0x0, 0x0)
    0x3fc8ecec: (Bool, 0x0, 0x0, 0x0)
    mProgressBarEaseRate: (F32, 0x0, 0x0, 0x0)
    mProgressMeterPingText: (String, 0x0, 0x0, 0x0)
    mSceneTransition: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mUnitBarFadeSpeed: (F32, 0x0, 0x0, 0x0)
    mTimerMeterSuffix: (String, 0x0, 0x0, 0x0)
    mProgressMeterHoverText: (String, 0x0, 0x0, 0x0)
    mPipsHoverText: (String, 0x0, 0x0, 0x0)
    pass

class BankUnitList():
    BankUnits: (List, 0x0, Embed, BankUnit)
    pass

class HeightSolverType():
    pass

class ArenaSkinLoadoutGridButtonData(LoadoutGridButtonData):
    FavoriteIcon: (Hash, 0x0, 0x0, 0x0)
    RarityIcon: (List, 0x0, Hash, 0x0)
    pass

class PlayerInventoryViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    DrawAreaList: (Embed, 0x0, 0x0, DrawAreaList)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    ShopButton: (Embed, 0x0, 0x0, HudShopButton)
    TooltipRegion: (Hash, 0x0, 0x0, 0x0)
    0xc8d95618: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    ItemSlotUiData: (List, 0x8, Embed, ItemSlotDetailedUiData)
    pass

class 0x3a6a30b6():
    ForbiddenWordList: (List, 0x0, String, 0x0)
    pass

class FloatingHealthbarDefaults():
    mChampionSingleResource: (Link, 0x0, 0x0, HealthbarTemplate)
    mUnitSingleResource: (Link, 0x0, 0x0, HealthbarTemplate)
    mChampionDoubleResource: (Link, 0x0, 0x0, HealthbarTemplate)
    mUnitHealthOnly: (Link, 0x0, 0x0, HealthbarTemplate)
    mChampionSingleResourceInvulnerable: (Link, 0x0, 0x0, HealthbarTemplate)
    pass

class AcceleratingMovementSpec(MissileMovementSpec):
    mProjectTargetToCastRange: (Bool, 0x0, 0x0, 0x0)
    mUseGroundHeightAtTarget: (Bool, 0x0, 0x0, 0x0)
    mInferDirectionFromFacingIfNeeded: (Bool, 0x0, 0x0, 0x0)
    mInitialSpeed: (F32, 0x0, 0x0, 0x0)
    mAcceleration: (F32, 0x0, 0x0, 0x0)
    mTargetHeightAugment: (F32, 0x0, 0x0, 0x0)
    mMinSpeed: (F32, 0x0, 0x0, 0x0)
    mMaxSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class PrototypeAkaliWMissileRender(MissileRenderSpec):
    mQuadScale: (F32, 0x0, 0x0, 0x0)
    mRadius: (F32, 0x0, 0x0, 0x0)
    mAkaliWMissileMaterialReference: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x3ac5d197():
    mNameHash: (U32, 0x0, 0x0, 0x0)
    mDataId: (U32, 0x0, 0x0, 0x0)
    pass

class 0x3aee5d80():
    BuffLayout: (Hash, 0x0, 0x0, 0x0)
    BuffDisplayTemplate: (Embed, 0x0, 0x0, BuffDisplayData)
    MaxBuffDisplayCount: (U32, 0x0, 0x0, 0x0)
    pass

class DrawAreaList():
    DrawRegions: (List, 0x0, Hash, 0x0)
    pass

class FixedDurationTriggeredBoolDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    mCustomDuration: (F32, 0x0, 0x0, 0x0)
    mBoolDriver: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    mBoolDriver: (Pointer, 0x0, 0x0, IDynamicMaterialBoolDriver)
    pass

class 0x3b2ba6c0():
    IconOverrideTexturePath: (String, 0x0, 0x0, 0x0)
    pass

class ItemGroup():
    mPurchaseCooldown: (F32, 0x0, 0x0, 0x0)
    mItemGroupId: (Hash, 0x0, 0x0, 0x0)
    mCooldownExtendedByAmbientGoldStart: (Bool, 0x0, 0x0, 0x0)
    mMaxGroupOwnable: (I32, 0x0, 0x0, 0x0)
    mItemModifiers: (List, 0x0, Link, ItemModifier)
    mInventorySlotMin: (I32, 0x0, 0x0, 0x0)
    mItemPurchaseModifiers: (List, 0x0, Link, ItemPurchaseModifier)
    mInventorySlotMax: (I32, 0x0, 0x0, 0x0)
    pass

class AbilityResourceTypeConfig():
    Wind: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    Heat: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    Energy: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    Shield: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    BattleFury: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    0x49e12631: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    Ammo: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    Rage: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    Ferocity: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    DragonFury: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    PrimalFury: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    None: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    Moonlight: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    Other: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    Bloodwell: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    0xd70134be: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    Mana: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    0xf0479924: (Embed, 0x0, 0x0, AbilityResourceTypeData)
    pass

class ItemAdvice():
    mAttributes: (List, 0x0, Hash, 0x0)
    mReason: (Hash, 0x0, 0x0, 0x0)
    pass

class ClearSkillsSumsCooldownCheat(Cheat):
    mTarget: (U32, 0x0, 0x0, 0x0)
    pass

class 0x3bd6ea88(ElementDataBase):
    InstanceData: (List2, 0x0, Embed, 0x8f92cfab)
    pass

class SkinScaleParametricUpdater(IFloatParametricUpdater):
    pass

class ShaderParamDef():
    Offset: (U32, 0x0, 0x0, 0x0)
    ParamName: (String, 0x0, 0x0, 0x0)
    Values: (List, 0x0, Vec4, 0x0)
    pass

class TftSurrenderCheat(Cheat):
    pass

class IconElementData(UiAssetElementData, BaseElementData, UiElementAssetData):
    mTextureUv: (Vec4, 0x0, 0x0, 0x0)
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    mColor: (Color, 0x0, 0x0, 0x0)
    mUseAlpha: (Bool, 0x0, 0x0, 0x0)
    mMaterial: (Link, 0x0, 0x0, StaticMaterialDef)
    mTextureSourceResolutionHeight: (U32, 0x0, 0x0, 0x0)
    mTextureSourceResolutionWidth: (U32, 0x0, 0x0, 0x0)
    mTexture: (String, 0x0, 0x0, 0x0)
    PerPixelUvsY: (Bool, 0x0, 0x0, 0x0)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mAtlas: (Pointer, 0x0, 0x0, AtlasDataBase)
    mAtlas: (Pointer, 0x0, 0x0, IUiTextureDataProvider)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    mExtension: (Pointer, 0x0, 0x0, IconElementDataExtension)
    pass

class IDynamicMaterialDriver():
    pass

class IScriptBlock(0x38a7f9b3):
    IsDisabled: (Bool, 0x0, 0x0, 0x0)
    pass

class ContextualConditionGameTimer(IContextualCondition):
    mCompareOp: (U8, 0x0, 0x0, 0x0)
    mGameTimeInMinutes: (F32, 0x0, 0x0, 0x0)
    pass

class MoveSpeedParametricUpdater(IFloatParametricUpdater):
    pass

class Sequence():
    mBlocks: (List, 0x0, Pointer, IBlock)
    Actions: (List2, 0x0, Pointer, ISequenceAction)
    Category: (Link, 0x0, 0x0, SequenceCategory)
    PhaseOverrides: (List, 0x0, Embed, SequencePhaseOverride)
    pass

class 0x3c5f9d3d(0xed4b858b):
    Key: (Pointer, 0x0, 0x0, 0xca4d32d1)
    Data: (Pointer, 0x0, 0x0, 0x27071fbd)
    pass

class LootTableDialogViewController(ModalDialogViewController):
    NoDuplicatesTraKey: (String, 0x0, 0x0, 0x0)
    LootLineHeaderText: (Hash, 0x0, 0x0, 0x0)
    SearchbarText: (Hash, 0x0, 0x0, 0x0)
    0x3a79eb8b: (String, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    LootTablelayout: (Hash, 0x0, 0x0, 0x0)
    0x5ba7b7c9: (String, 0x0, 0x0, 0x0)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    0x749fcb22: (String, 0x0, 0x0, 0x0)
    0x791accf7: (String, 0x0, 0x0, 0x0)
    NoDuplicatesButton: (Hash, 0x0, 0x0, 0x0)
    LootLineItemDropRateText: (Hash, 0x0, 0x0, 0x0)
    SubArrowCollapsedTexturePath: (String, 0x0, 0x0, 0x0)
    RolloverProtectionTraKey: (String, 0x0, 0x0, 0x0)
    RootArrowExpandedTexturePath: (String, 0x0, 0x0, 0x0)
    RolloverProtectionButton: (Hash, 0x0, 0x0, 0x0)
    LootTableTitleText: (Hash, 0x0, 0x0, 0x0)
    0xb7d3735d: (String, 0x0, 0x0, 0x0)
    0xc5e35c96: (String, 0x0, 0x0, 0x0)
    0xc99290c6: (String, 0x0, 0x0, 0x0)
    RootArrowCollapsedTexturePath: (String, 0x0, 0x0, 0x0)
    LootItemLineElements: (Embed, 0x0, 0x0, LootItemLineElements)
    SubArrowExpandedTexturePath: (String, 0x0, 0x0, 0x0)
    LootLineItemNameText: (Hash, 0x0, 0x0, 0x0)
    0xead14f26: (String, 0x0, 0x0, 0x0)
    pass

class MapBehavior(GenericMapPlaceable):
    CooldownInSec: (F32, 0x0, 0x0, 0x0)
    Actions: (List, 0x0, Pointer, MapAction)
    Cue: (String, 0x0, 0x0, 0x0)
    pass

class UnitObjectTagsSettings():
    UnitTags: (List2, 0x0, String, 0x0)
    pass

class HealthBarTickStyleTftCompanion(HealthBarTickStyleBase):
    StandardTick: (Hash, 0x0, 0x0, 0x0)
    pass

class FxActionMoveBase(IFxAction):
    OvershootDistance: (F32, 0x0, 0x0, 0x0)
    EasingType: (U32, 0x0, 0x0, 0x0)
    EasingType: (U8, 0x0, 0x0, 0x0)
    FaceVelocity: (Bool, 0x0, 0x0, 0x0)
    TargetObject: (Embed, 0x0, 0x0, FxTarget)
    TargetObject: (Embed, 0x0, 0x0, FxObjectSelector)
    pass

class LoadingScreenHonorFlairData():
    FlairIcons: (List, 0x3, Hash, 0x0)
    pass

class 0x3c995caf(IPath):
    Segments: (List2, 0x0, Vec3, 0x0)
    pass

class 0x3cabf2f3():
    Definition: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class BuildingClient(BuildingCommon):
    pass

class ChangeMissileWidth(MissileTriggeredActionSpec):
    WidthChangeType: (U32, 0x0, 0x0, 0x0)
    WidthValue: (F32, 0x0, 0x0, 0x0)
    pass

class TriggerOnStart(MissileTriggerSpec):
    pass

class PerkBuff():
    mBuffScriptName: (String, 0x0, 0x0, 0x0)
    mBuffSpellObject: (Embed, 0x0, 0x0, SpellObject)
    pass

class TimeBlendData(BaseBlendData):
    mTime: (F32, 0x0, 0x0, 0x0)
    pass

class HudHealthBarFadeData():
    FadeAcceleration: (F32, 0x0, 0x0, 0x0)
    FadeHoldTime: (F32, 0x0, 0x0, 0x0)
    FadeSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class VfxShapeSphere(VfxShapeVolume):
    Radius: (F32, 0x0, 0x0, 0x0)
    pass

class 0x3dc0ea14(ISequenceAction):
    DisableOnEnd: (Bool, 0x0, 0x0, 0x0)
    Element: (Pointer, 0x0, 0x0, 0xc06f5f6a)
    Text: (Pointer, 0x0, 0x0, 0xa8a6ac21)
    EnableOnStart: (Bool, 0x0, 0x0, 0x0)
    pass

class UiMetricLaneMinionPercentIncreasedDamageToMinion(UiMetricLaneMinionI):
    pass

class 0x3e02c8d9():
    Name: (String, 0x0, 0x0, 0x0)
    pass

class MissileGroupSpawnerSpec():
    mChildMissileSpell: (Link, 0x0, 0x0, SpellObject)
    pass

class 0x3e265091():
    pass

class IGameModeConfigBase():
    pass

class OptionItemFilter_HwRequirement(IOptionItemFilter):
    RequiresAlienware: (Bool, 0x0, 0x0, 0x0)
    RequiresMrtSupport: (Bool, 0x0, 0x0, 0x0)
    RequiresShaderModel3: (Bool, 0x0, 0x0, 0x0)
    pass

class FxActionContinueInstance(IFxActionInstance):
    pass

class SetRespawnTimerCheat(Cheat):
    mTimerValue: (F32, 0x0, 0x0, 0x0)
    mTarget: (U32, 0x0, 0x0, 0x0)
    pass

class RotatingBannerSet():
    BannerEntries: (List, 0x0, Embed, RotatingBannerEntry)
    pass

class 0x3eed1ba8(0xe561be2e):
    KeyType: (Pointer, 0x0, 0x0, 0xed4b858b)
    pass

class StrawberryLoadoutItem(BaseLoadoutData):
    pass

class 0x3f1c01bb():
    0x2f7e46c8: (F32, 0x0, 0x0, 0x0)
    QualitySetting: (Link, 0x0, 0x0, QualitySetting)
    0xc58ea052: (F32, 0x0, 0x0, 0x0)
    pass

class RadialMenuViewController(ViewController):
    MinimapSelectionRotatingIcon: (Hash, 0x0, 0x0, 0x0)
    MinimapSelectionLine: (Hash, 0x0, 0x0, 0x0)
    MinimapRadialButtons: (List, 0x0, Embed, RadialMenuButtonDefinitionBase)
    MinimapRadialButtons: (List, 0x5, Embed, RadialMenuButtonDefinitionBase)
    HorizontallyCenterFirstWedge: (Bool, 0x0, 0x0, 0x0)
    WeightedSelectionCalculator: (Pointer, 0x0, 0x0, WeightedSelectionCalculator)
    RadialButtons: (List, 0x0, Embed, RadialMenuHoverButtonDefinition)
    RadialButtons: (List, 0x5, Embed, RadialMenuHoverButtonDefinition)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    ActiveWheelButtonHoverOutroScene: (Hash, 0x0, 0x0, 0x0)
    SelectionRotatingIcon: (Hash, 0x0, 0x0, 0x0)
    MinimapActiveWheelScene: (Hash, 0x0, 0x0, 0x0)
    OverrideMinimapCenterButtonRegion: (Hash, 0x0, 0x0, 0x0)
    ActiveWheelButtonHoverIntroScene: (Hash, 0x0, 0x0, 0x0)
    ActivateWheelDelayTime: (F32, 0x0, 0x0, 0x0)
    SelectionLine: (Hash, 0x0, 0x0, 0x0)
    OverrideCenterButtonRegion: (Hash, 0x0, 0x0, 0x0)
    MinimapBackgroundCooldownEffect: (Hash, 0x0, 0x0, 0x0)
    ActiveWheelScene: (Hash, 0x0, 0x0, 0x0)
    BackgroundCooldownEffect: (Hash, 0x0, 0x0, 0x0)
    pass

class FloatingTextOverride():
    OverriddenFloatingTextTypes: (Map, U32, Bool, 0x0)
    pass

class VfxAnimatedVector2f(VfxVector2fBase):
    Values: (List, 0x0, Vec2, 0x0)
    Values: (List2, 0x0, Vec2, 0x0)
    Times: (List, 0x0, F32, 0x0)
    Times: (List2, 0x0, F32, 0x0)
    0x7c9bcfd5: (List, 0x0, U32, 0x0)
    Modes: (List2, 0x0, U8, 0x0)
    ProbabilityTables: (List, 0x2, Pointer, VfxProbabilityTableData)
    pass

class MapGraphicsFeature(MapComponent):
    pass

class IndicatorTypeLocal(ILineIndicatorType):
    pass

class ItemSelectionBaseViewController(ViewController):
    ItemSlots: (List, 0x0, Embed, UiItemSelectionSlotData)
    Scene: (Hash, 0x0, 0x0, 0x0)
    Loadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    pass

class LoadoutItemListPanelData():
    ButtonArea: (Hash, 0x0, 0x0, 0x0)
    TitleTextTemplate: (Hash, 0x0, 0x0, 0x0)
    TitleTemplate: (Hash, 0x0, 0x0, 0x0)
    PanelScene: (Hash, 0x0, 0x0, 0x0)
    ViewPanelScene: (Hash, 0x0, 0x0, 0x0)
    TitleArea: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x3ff7df39(SocialPanelViewController):
    pass

class IContextualAction():
    mMaxOccurences: (U32, 0x0, 0x0, 0x0)
    mHashedSituationTrigger: (Hash, 0x0, 0x0, 0x0)
    pass

class CommentBlock(IBlock):
    Sequence: (Embed, 0x0, 0x0, Sequence)
    pass

class 0x4008de72(TargetingTypeData):
    pass

class LogicDriverFloatParametricUpdater(IFloatParametricUpdater):
    Driver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class GameModeConstantInteger(GameModeConstant):
    mValue: (I32, 0x0, 0x0, 0x0)
    pass

class ProgressBarDisplayData():
    TimerText: (Hash, 0x0, 0x0, 0x0)
    Meter: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class LobbyBottomButtons():
    RankedInfo: (Hash, 0x0, 0x0, 0x0)
    RankedInfoButton: (Hash, 0x0, 0x0, 0x0)
    Warning: (Hash, 0x0, 0x0, 0x0)
    VietnameseRatingLabel: (Hash, 0x0, 0x0, 0x0)
    RankedTooltipTraKey: (String, 0x0, 0x0, 0x0)
    WarningText: (Hash, 0x0, 0x0, 0x0)
    TeamPlannerButton: (Hash, 0x0, 0x0, 0x0)
    InfoText: (Hash, 0x0, 0x0, 0x0)
    CloseButton: (Hash, 0x0, 0x0, 0x0)
    InfoIcon: (Hash, 0x0, 0x0, 0x0)
    UnrankedTraKey: (String, 0x0, 0x0, 0x0)
    RankedTraKey: (String, 0x0, 0x0, 0x0)
    RankedInfoText: (Hash, 0x0, 0x0, 0x0)
    StartButton: (Hash, 0x0, 0x0, 0x0)
    InviteButton: (Hash, 0x0, 0x0, 0x0)
    Info: (Hash, 0x0, 0x0, 0x0)
    pass

class ChampionGoldUiData():
    ChampionGoldText: (Hash, 0x0, 0x0, 0x0)
    pass

class MaterialInstanceDynamicTexture():
    Enabled: (Bool, 0x0, 0x0, 0x0)
    Options: (List, 0x0, Embed, DynamicMaterialTextureSwapOption)
    pass

class 0x409a5657(IGameModeConfig):
    0x6575891f: (Map, U8, U8, 0x0)
    0x857c9848: (List2, 0x0, Embed, AugmentFallbackPool)
    0x8794a0e6: (Map, U8, U8, 0x0)
    0xba9783c7: (U8, 0x0, 0x0, 0x0)
    pass

class TftBoardPosition():
    Row: (I32, 0x0, 0x0, 0x0)
    Row: (U32, 0x0, 0x0, 0x0)
    Col: (I32, 0x0, 0x0, 0x0)
    Col: (U32, 0x0, 0x0, 0x0)
    pass

class TftUnitPropertyValueString(TftUnitPropertyValue):
    Value: (String, 0x0, 0x0, 0x0)
    pass

class SyncedAnimationRigPoseModifierData(BaseRigPoseModifierData):
    pass

class TftCutsceneMapPropAnimClip(TftCutsceneClip):
    AnimationName: (String, 0x0, 0x0, 0x0)
    BlackboardGameObjectName: (String, 0x0, 0x0, 0x0)
    Loop: (Bool, 0x0, 0x0, 0x0)
    pass

class ContextualConditionItemId(IContextualCondition):
    mItems: (List, 0x0, Hash, 0x0)
    mItemIds: (List, 0x0, I32, 0x0)
    pass

class IDynamicMaterialFloatDriver(IDynamicMaterialDriver):
    pass

class VfxReflectionDefinitionData():
    ReflectionOpacityDirect: (F32, 0x0, 0x0, 0x0)
    ReflectionFresnel: (F32, 0x0, 0x0, 0x0)
    ReflectionOpacityGlancing: (F32, 0x0, 0x0, 0x0)
    FresnelColor: (Vec4, 0x0, 0x0, 0x0)
    ReflectionFresnelColor: (Vec4, 0x0, 0x0, 0x0)
    ReflectionMapTexture: (String, 0x0, 0x0, 0x0)
    Fresnel: (F32, 0x0, 0x0, 0x0)
    pass

class INeutralCampSpawnBehavior():
    pass

class LookAtSpellTargetAngleParametricUpdater(IFloatParametricUpdater):
    pass

class 0x4142edcd(IEnabler):
    Enablers: (List2, 0x0, Pointer, IEnabler)
    pass

class FlexValueVector2():
    mValue: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    mValue: (Embed, 0x0, 0x0, ValueVector2)
    mFlexId: (U32, 0x0, 0x0, 0x0)
    mIsUsed: (Bool, 0x0, 0x0, 0x0)
    mTypeValue: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    mFlexValueId: (U32, 0x0, 0x0, 0x0)
    pass

class 0x418af145(IScriptCondition):
    Position: (Pointer, 0x0, 0x0, IIntGet)
    BitField: (Pointer, 0x0, 0x0, IIntGet)
    pass

class ContextualConditionBuffCounterSetToZeroAfterLimitReached(IContextualConditionBuff):
    mCounterHighestReached: (U8, 0x0, 0x0, 0x0)
    mBuff: (Hash, 0x0, 0x0, 0x0)
    pass

class HealthbarTemplate():
    Self: (Pointer, 0x0, 0x0, HealthbarStyleTemplate)
    Enemy: (Pointer, 0x0, 0x0, HealthbarStyleTemplate)
    Neutral: (Pointer, 0x0, 0x0, HealthbarStyleTemplate)
    Ally: (Pointer, 0x0, 0x0, HealthbarStyleTemplate)
    pass

class FxActionSfxStaticInstance(IFxActionInstance):
    pass

class BaseItemAdviceSet():
    mAdvices: (List, 0x0, Embed, BaseItemAdvice)
    pass

class VfxPrimitiveCameraSegmentSeriesBeam():
    VfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    Name: (String, 0x0, 0x0, 0x0)
    VfxMask: (Color, 0x0, 0x0, 0x0)
    pass

class ScoreboardTeamScoresDefinitions():
    ChampionKillsUiData: (Embed, 0x0, 0x0, TeamScoreUiData)
    TowerKillsUiData: (Embed, 0x0, 0x0, TeamScoreUiData)
    DragonTracker: (Embed, 0x0, 0x0, UiMetricMultiDragonKillsSrX)
    TowerKills: (Embed, 0x0, 0x0, UiMetricTeamTowerKills)
    TrackerData: (Embed, 0x0, 0x0, 0xa44b28c0)
    ChampionKills: (Embed, 0x0, 0x0, UiMetricTeamKills)
    pass

class ContextualConditionNegation(IContextualCondition):
    mChildCondition: (Pointer, 0x0, 0x0, IContextualCondition)
    pass

class HudLoadingScreenWidgetClash(IHudLoadingScreenWidget):
    pass

class UiElementEffectGlowingRotatingIconData(UiElementEffectRotatingIconData):
    BrightnessMod: (F32, 0x0, 0x0, 0x0)
    CycleTime: (F32, 0x0, 0x0, 0x0)
    pass

class ISkinUpgradeObject(BaseLoadoutData):
    mCost: (U32, 0x0, 0x0, 0x0)
    pass

class EnabledRegionData(RegionDataBase):
    pass

class AiGenericCommon(AiBaseClient):
    pass

class FlexValueVector3():
    mValue: (Embed, 0x0, 0x0, ValueVector3)
    mValue: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    mFlexId: (U32, 0x0, 0x0, 0x0)
    mIsUsed: (Bool, 0x0, 0x0, 0x0)
    mTypeValue: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    mFlexValueId: (U32, 0x0, 0x0, 0x0)
    pass

class SkinAnimationProperties():
    AnmFiles: (List, 0x0, String, 0x0)
    AnimationGraphData: (Link, 0x0, 0x0, AnimationGraphData)
    pass

class MutatorMapVisibilityController(IMapVisibilityController):
    MutatorName: (String, 0x0, 0x0, 0x0)
    pass

class LoadScreenTip():
    mLocalizationKey: (String, 0x0, 0x0, 0x0)
    mMaximumSummonerLevel: (Option, 0x0, U32, 0x0)
    mHeaderLocalizationKey: (String, 0x0, 0x0, 0x0)
    mId: (U16, 0x0, 0x0, 0x0)
    mMinimumSummonerLevel: (Option, 0x0, U32, 0x0)
    pass

class MapStaticPointLightBase(MapPointLightBase):
    pass

class LookAtInterestDistanceParametricUpdater(IFloatParametricUpdater):
    pass

class EmoteConfigData():
    Scale: (F32, 0x0, 0x0, 0x0)
    FloatingDistancePerSecond: (F32, 0x0, 0x0, 0x0)
    RespoitionMovementTime: (F32, 0x0, 0x0, 0x0)
    TotalDisplayTime: (F32, 0x0, 0x0, 0x0)
    InitialAlpha: (F32, 0x0, 0x0, 0x0)
    UiSound: (String, 0x0, 0x0, 0x0)
    FadeTransisionTime: (F32, 0x0, 0x0, 0x0)
    MaxDisplayedEmotes: (U8, 0x0, 0x0, 0x0)
    HeightMultiplier: (F32, 0x0, 0x0, 0x0)
    pass

class 0x42be4a07(TargetingTypeData):
    pass

class 0x42c94584():
    0x3ce127e2: (List2, 0x0, Embed, 0x2b6fac9a)
    0x72a9c287: (F32, 0x0, 0x0, 0x0)
    0x78442b2f: (List2, 0x0, Embed, 0x2b6fac9a)
    0x8b21d9dc: (List2, 0x0, I32, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    0xb6460367: (List2, 0x0, I32, 0x0)
    0xb6f73c55: (List2, 0x0, Embed, 0x2b6fac9a)
    pass

class DrawFx(GameObject):
    pass

class 0x42d18dab(IScriptBlock, IBehaviorScriptBlock):
    pass

class VfxVector2fBase():
    pass

class 0x42dcedbc():
    Border: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    StaticIcon: (Hash, 0x0, 0x0, 0x0)
    TimerVfx: (Hash, 0x0, 0x0, 0x0)
    pass

class AudioTagListProperties():
    Key: (String, 0x0, 0x0, 0x0)
    Tags: (List, 0x0, String, 0x0)
    pass

class ValueFloat():
    ConstantValue: (F32, 0x0, 0x0, 0x0)
    Dynamics: (Pointer, 0x0, 0x0, VfxFloatBase)
    Dynamics: (Pointer, 0x0, 0x0, VfxAnimatedFloatVariableData)
    pass

class OptionItemSecondaryHotkeys2Column_Row():
    EventName: (String, 0x0, 0x0, 0x0)
    Filter: (Pointer, 0x0, 0x0, IOptionItemFilter)
    LabelTraKey: (String, 0x0, 0x0, 0x0)
    pass

class VectorValueGet(DirectValueGet):
    Value: (Vec3, 0x0, 0x0, 0x0)
    pass

class DesignerEvent():
    Name: (String, 0x0, 0x0, 0x0)
    EventParameters: (Map, Hash, Pointer, IScriptValueGet)
    pass

class SpellDataResource():
    mDoesntBreakChannels: (Bool, 0x0, 0x0, 0x0)
    mMissilePerceptionBubbleRadius: (F32, 0x0, 0x0, 0x0)
    mCursorChangesInTerrain: (Bool, 0x0, 0x0, 0x0)
    mSpellPassives: (List, 0x0, Pointer, SpellPassiveData)
    MissileSpeed: (F32, 0x0, 0x0, 0x0)
    mCastRangeGrowthDuration: (List, 0x7, F32, 0x0)
    mBelongsToAvatar: (Bool, 0x0, 0x0, 0x0)
    DelayCastOffsetPercent: (F32, 0x0, 0x0, 0x0)
    mCircleMissileAngularVelocity: (F32, 0x0, 0x0, 0x0)
    mChannelDuration: (List, 0x7, F32, 0x0)
    mLineWidth: (F32, 0x0, 0x0, 0x0)
    mFloatVarsDecimals: (List, 0x10, I32, 0x0)
    CastRange: (List, 0x7, F32, 0x0)
    mUseAutoattackCastTime: (Bool, 0x0, 0x0, 0x0)
    CanCastOrQueueWhileCasting: (Bool, 0x0, 0x0, 0x0)
    mDataValues: (List, 0x0, Embed, SpellDataValue)
    ImgIconPath: (String, 0x0, 0x0, 0x0)
    mIsDelayedByCastLocked: (Bool, 0x0, 0x0, 0x0)
    mHitEffectOrientType: (U32, 0x0, 0x0, 0x0)
    mMissileEffectEnemyName: (String, 0x0, 0x0, 0x0)
    mCastingRevealsCasterWhileAttached: (Bool, 0x0, 0x0, 0x0)
    mEffectAmount: (List, 0xa, Embed, SpellEffectAmount)
    ShouldReceiveInputEvents: (Bool, 0x0, 0x0, 0x0)
    mProjectTargetToCastRange: (Bool, 0x0, 0x0, 0x0)
    0x288b8edc: (Pointer, 0x0, 0x0, 0x288b8edc)
    mCoefficient: (F32, 0x0, 0x0, 0x0)
    mMaxHighlightTargets: (I32, 0x0, 0x0, 0x0)
    mDynamicExtended: (String, 0x0, 0x0, 0x0)
    0x338e3aed: (Bool, 0x0, 0x0, 0x0)
    mLineMissileTrackUnits: (Bool, 0x0, 0x0, 0x0)
    mCastRequirementsCaster: (List, 0x0, Pointer, ICastRequirement)
    mMissileBoneName: (String, 0x0, 0x0, 0x0)
    mCastingRevealsCasterStealth: (Bool, 0x0, 0x0, 0x0)
    mPhysicalDamageRatio: (F32, 0x0, 0x0, 0x0)
    DelayTotalTimePercent: (F32, 0x0, 0x0, 0x0)
    mIgnoreRangeCheck: (Bool, 0x0, 0x0, 0x0)
    mCastType: (U32, 0x0, 0x0, 0x0)
    mRequiredUnitTags: (Embed, 0x0, 0x0, ObjectTags)
    AudioBankPaths: (List, 0x0, String, 0x0)
    mCasterPositionEndOfCastUpdate: (U8, 0x0, 0x0, 0x0)
    mHitEffectPlayerKey: (Hash, 0x0, 0x0, 0x0)
    mSpellTags: (List, 0x0, String, 0x0)
    mMinimapIconDisplayFlag: (U16, 0x0, 0x0, 0x0)
    mDimensionBehavior: (U8, 0x0, 0x0, 0x0)
    mDoNotNeedToFaceTarget: (Bool, 0x0, 0x0, 0x0)
    mCanMoveWhileChanneling: (Bool, 0x0, 0x0, 0x0)
    MissileAccel: (F32, 0x0, 0x0, 0x0)
    mSummonerSpellUpgradeDescription: (Embed, 0x0, 0x0, SummonerSpellUpgradeDescription)
    CanOnlyCastWhileDisabled: (Bool, 0x0, 0x0, 0x0)
    0x43b514b6: (Bool, 0x0, 0x0, 0x0)
    mAlternateName: (String, 0x0, 0x0, 0x0)
    MissileMinSpeed: (Option, 0x0, F32, 0x0)
    SpellEventToAudioEventSuffix: (Map, U32, String, 0x0)
    0x48201b0d: (F32, 0x0, 0x0, 0x0)
    mClientData: (Embed, 0x0, 0x0, SpellDataResourceClient)
    mDisableChannelBar: (Bool, 0x0, 0x0, 0x0)
    CastRangeUseBoundingBoxes: (Bool, 0x0, 0x0, 0x0)
    CastFrame: (F32, 0x0, 0x0, 0x0)
    mDeathRecapPriority: (I32, 0x0, 0x0, 0x0)
    CastTargetAdditionalUnitsRadius: (F32, 0x0, 0x0, 0x0)
    mMissileTargetHeightAugment: (F32, 0x0, 0x0, 0x0)
    mTags: (List, 0x0, U32, 0x0)
    mMissileEffectPlayerKey: (Hash, 0x0, 0x0, 0x0)
    mTurnSpeedScalar: (F32, 0x0, 0x0, 0x0)
    mCircleMissileRadialVelocity: (F32, 0x0, 0x0, 0x0)
    mLollipopAreaRadiusEnd: (List, 0x7, F32, 0x0)
    mSpellRevealsChampion: (Bool, 0x0, 0x0, 0x0)
    LineMissileDelayDestroyAtEndSeconds: (F32, 0x0, 0x0, 0x0)
    mCantCancelWhileChanneling: (Bool, 0x0, 0x0, 0x0)
    0x5577fc76: (Bool, 0x0, 0x0, 0x0)
    ShowChannelBarPerSpellLevelOverride: (List, 0x7, Bool, 0x0)
    mMaxAmmo: (List, 0x7, I32, 0x0)
    mPostCastLockoutDeltaTimeData: (Pointer, 0x0, 0x0, SpellLockDeltaTimeData)
    mCancelChargeOnRecastTime: (F32, 0x0, 0x0, 0x0)
    CastConeDistance: (F32, 0x0, 0x0, 0x0)
    mSpellDamageRatio: (F32, 0x0, 0x0, 0x0)
    mTargetingTypeData: (Pointer, 0x0, 0x0, TargetingTypeData)
    mChannelIsInterruptedByDisables: (Bool, 0x0, 0x0, 0x0)
    AutoSpellCastInfo: (Embed, 0x0, 0x0, AutoSpellCastInfo)
    mHideRangeIndicatorWhenCasting: (Bool, 0x0, 0x0, 0x0)
    Loadable: (Link, 0x0, 0x0, PropertyLoadable)
    mHideCdOnPostSpellCast: (Bool, 0x0, 0x0, 0x0)
    mIsDisabledWhileDead: (Bool, 0x0, 0x0, 0x0)
    mMissilePerceptionBubbleRevealsStealth: (Bool, 0x0, 0x0, 0x0)
    mParticleStartOffset: (Vec3, 0x0, 0x0, 0x0)
    mPointEffectName: (String, 0x0, 0x0, 0x0)
    0x6d0c8a83: (Map, U32, String, 0x0)
    mPreCastLockoutDeltaTimeData: (Pointer, 0x0, 0x0, SpellLockDeltaTimeData)
    mDisableCastBar: (Bool, 0x0, 0x0, 0x0)
    mDisplayName: (String, 0x0, 0x0, 0x0)
    mHitBoneName: (String, 0x0, 0x0, 0x0)
    CastConeAngle: (F32, 0x0, 0x0, 0x0)
    mMissileBlockTriggersOnDestroy: (Bool, 0x0, 0x0, 0x0)
    SelectionPriority: (U32, 0x0, 0x0, 0x0)
    mStartCooldown: (F32, 0x0, 0x0, 0x0)
    TargetingForgivenessDefinitions: (List, 0x0, Embed, TargetingForgivenessDefinitions)
    mHitEffectKey: (Hash, 0x0, 0x0, 0x0)
    mSpellCooldownOrSealedQueueThreshold: (Option, 0x0, F32, 0x0)
    mVoEventCategory: (String, 0x0, 0x0, 0x0)
    mMissileEffectPlayerName: (String, 0x0, 0x0, 0x0)
    mMinimapIconName: (String, 0x0, 0x0, 0x0)
    mCantCancelWhileWindingUpTargetingChampion: (Bool, 0x0, 0x0, 0x0)
    mAmmoCountHiddenInUi: (Bool, 0x0, 0x0, 0x0)
    mMissileUnblockable: (Bool, 0x0, 0x0, 0x0)
    bHaveAfterEffect: (Bool, 0x0, 0x0, 0x0)
    mUpdateToCasterPositionAtEndOfCastTime: (Bool, 0x0, 0x0, 0x0)
    CantCastWhileRooted: (Bool, 0x0, 0x0, 0x0)
    MissileMaxSpeed: (Option, 0x0, F32, 0x0)
    LuaOnMissileUpdateDistanceInterval: (F32, 0x0, 0x0, 0x0)
    mRollForCriticalHit: (Bool, 0x0, 0x0, 0x0)
    mDoesNotConsumeMana: (Bool, 0x0, 0x0, 0x0)
    mMissileEffectKey: (Hash, 0x0, 0x0, 0x0)
    mAmmoUsed: (List, 0x7, I32, 0x0)
    bLineMissileUsesAccelerationForBounce: (Bool, 0x0, 0x0, 0x0)
    mLineMissileTrackUnitsAndContinues: (Bool, 0x0, 0x0, 0x0)
    bIsToggleSpell: (Bool, 0x0, 0x0, 0x0)
    CastRadiusSecondary: (List, 0x7, F32, 0x0)
    mTargetingType: (U8, 0x0, 0x0, 0x0)
    bHaveHitBone: (Bool, 0x0, 0x0, 0x0)
    mCastTime: (F32, 0x0, 0x0, 0x0)
    mAffectsStatusFlags: (U32, 0x0, 0x0, 0x0)
    mAvatarLevelRequired: (I32, 0x0, 0x0, 0x0)
    mResourceResolvers: (List, 0x0, Hash, 0x0)
    mResourceResolvers: (List, 0x0, Link, ResourceResolver)
    mExcludedUnitTags: (Embed, 0x0, 0x0, ObjectTags)
    mSpellCalculations: (Map, Hash, Pointer, IGameCalculation)
    mSpellCalculations: (Map, Hash, Pointer, ISpellCalculation)
    mSpellCalculations: (Map, Hash, Pointer, SpellCalculation)
    mLookAtPolicy: (U32, 0x0, 0x0, 0x0)
    mPlatformSpellInfo: (Embed, 0x0, 0x0, PlatformSpellInfo)
    mTargetBoneName: (String, 0x0, 0x0, 0x0)
    mAfterEffectName: (String, 0x0, 0x0, 0x0)
    MissileEffectMaximumAngleDegrees: (F32, 0x0, 0x0, 0x0)
    mDynamicTooltip: (String, 0x0, 0x0, 0x0)
    mUpdateRotationWhenCasting: (Bool, 0x0, 0x0, 0x0)
    CanOnlyCastWhileDead: (Bool, 0x0, 0x0, 0x0)
    Flags: (U32, 0x0, 0x0, 0x0)
    mShowChannelBar: (Bool, 0x0, 0x0, 0x0)
    0x9e2d4d0e: (Bool, 0x0, 0x0, 0x0)
    CooldownTime: (List, 0x7, F32, 0x0)
    mKeywordWhenAcquired: (String, 0x0, 0x0, 0x0)
    mNoWinddownIfCancelled: (Bool, 0x0, 0x0, 0x0)
    PassiveSpellAffectedByCooldown: (Bool, 0x0, 0x0, 0x0)
    mAmmoNotAffectedByCdr: (Bool, 0x0, 0x0, 0x0)
    mApplyMaterialOnHitSound: (Bool, 0x0, 0x0, 0x0)
    mCastRangeGrowthStartTime: (List, 0x7, F32, 0x0)
    mDoesNotConsumeCooldown: (Bool, 0x0, 0x0, 0x0)
    mChannelIsInterruptedByAttacking: (Bool, 0x0, 0x0, 0x0)
    mPostCastLockoutDeltaTime: (F32, 0x0, 0x0, 0x0)
    mMissileFollowsTerrainHeight: (Bool, 0x0, 0x0, 0x0)
    mCastingBreaksStealthWhileAttached: (Bool, 0x0, 0x0, 0x0)
    mCooldownNotAffectedByCdr: (Bool, 0x0, 0x0, 0x0)
    mMissileLifetime: (F32, 0x0, 0x0, 0x0)
    0xb08bc498: (Map, Hash, Embed, SpellEffectAmount)
    mMissileClientWaitForTargetUpdateBeforeMissileShow: (Bool, 0x0, 0x0, 0x0)
    mApplyAttackDamage: (Bool, 0x0, 0x0, 0x0)
    mUseChargeChanneling: (Bool, 0x0, 0x0, 0x0)
    mSpellShapeFlags: (U32, 0x0, 0x0, 0x0)
    mCanTriggerChargeSpellWhileDisabled: (Bool, 0x0, 0x0, 0x0)
    bLineMissileBounces: (Bool, 0x0, 0x0, 0x0)
    mMissileClientExitFowPrediction: (Bool, 0x0, 0x0, 0x0)
    mApplyAttackEffect: (Bool, 0x0, 0x0, 0x0)
    CastRadius: (List, 0x7, F32, 0x0)
    BuffEffects: (List, 0x0, Pointer, BuffEffect)
    mOrientRadiusTextureFromPlayer: (Bool, 0x0, 0x0, 0x0)
    mMinimapIconRotation: (Bool, 0x0, 0x0, 0x0)
    mCostAlwaysShownInUi: (Bool, 0x0, 0x0, 0x0)
    mCharacterPassiveBuffs: (List, 0x0, Embed, CharacterPassiveData)
    MissileGravity: (F32, 0x0, 0x0, 0x0)
    0xbb6aca93: (Bool, 0x0, 0x0, 0x0)
    mCastRangeGrowthMax: (List, 0x7, F32, 0x0)
    mAnimationWindownName: (String, 0x0, 0x0, 0x0)
    mCursorChangesInGrass: (Bool, 0x0, 0x0, 0x0)
    mHitEffectName: (String, 0x0, 0x0, 0x0)
    mAnimationLeadOutName: (String, 0x0, 0x0, 0x0)
    mCastRequirementsTarget: (List, 0x0, Pointer, ICastRequirement)
    ManaUiOverride: (List, 0x6, F32, 0x0)
    MissileEffectMaxTurnSpeedDegreesPerSecond: (F32, 0x0, 0x0, 0x0)
    BounceRadius: (F32, 0x0, 0x0, 0x0)
    mIgnoreAnimContinueUntilCastFrame: (Bool, 0x0, 0x0, 0x0)
    mUseMinimapTargeting: (Bool, 0x0, 0x0, 0x0)
    mLineDragLength: (F32, 0x0, 0x0, 0x0)
    CannotBeSuppressed: (Bool, 0x0, 0x0, 0x0)
    mAlternateSpellAssets: (List, 0x0, Embed, AlternateSpellAssets)
    UseAnimatorFramerate: (Bool, 0x0, 0x0, 0x0)
    CastRangeDisplayOverride: (List, 0x7, F32, 0x0)
    mOverrideAttackTime: (Pointer, 0x0, 0x0, OverrideAttackTimeData)
    mAfterEffectKey: (Hash, 0x0, 0x0, 0x0)
    mCoefficient2: (F32, 0x0, 0x0, 0x0)
    mUseChargeTargeting: (Bool, 0x0, 0x0, 0x0)
    Mana: (List, 0x6, F32, 0x0)
    mAmmoRechargeTime: (List, 0x7, F32, 0x0)
    LineMissileTimePulseBetweenCollisionSpellHits: (F32, 0x0, 0x0, 0x0)
    CanCastWhileDisabled: (Bool, 0x0, 0x0, 0x0)
    mAnimationLoopName: (String, 0x0, 0x0, 0x0)
    mMissileEffectEnemyKey: (Hash, 0x0, 0x0, 0x0)
    mCanQueueWhileOnCooldown: (Bool, 0x0, 0x0, 0x0)
    mConsideredAsAutoAttack: (Bool, 0x0, 0x0, 0x0)
    AlwaysSnapFacing: (Bool, 0x0, 0x0, 0x0)
    mMissileSpec: (Pointer, 0x0, 0x0, MissileSpecification)
    mHitEffectPlayerName: (String, 0x0, 0x0, 0x0)
    mLineMissileEndsAtTargetPoint: (Bool, 0x0, 0x0, 0x0)
    mCantCancelWhileWindingUp: (Bool, 0x0, 0x0, 0x0)
    bHavePointEffect: (Bool, 0x0, 0x0, 0x0)
    mAiData: (Embed, 0x0, 0x0, AiSpellData)
    mSplineInfo: (Pointer, 0x0, 0x0, ISplineInfo)
    mSplineInfo: (Pointer, 0x0, 0x0, SplineInfo)
    MissileFixedTravelTime: (F32, 0x0, 0x0, 0x0)
    mAffectsTypeFlags: (U32, 0x0, 0x0, 0x0)
    mSpellId: (I32, 0x0, 0x0, 0x0)
    mImgIconName: (List, 0x0, String, 0x0)
    mImgIconName: (List, 0x2, String, 0x0)
    mAnimationWinddownName: (String, 0x0, 0x0, 0x0)
    mLockedSpellOriginationCastId: (Bool, 0x0, 0x0, 0x0)
    mPreCastLockoutDeltaTime: (F32, 0x0, 0x0, 0x0)
    mDescription: (String, 0x0, 0x0, 0x0)
    mSpellCooldownQueueThreshold: (Option, 0x0, F32, 0x0)
    mPingableWhileDisabled: (Bool, 0x0, 0x0, 0x0)
    mMissileEffectName: (String, 0x0, 0x0, 0x0)
    bHaveHitEffect: (Bool, 0x0, 0x0, 0x0)
    mUseAutoattackCastTimeData: (Pointer, 0x0, 0x0, UseAutoattackCastTimeData)
    mBuffTimerSimulationType: (U32, 0x0, 0x0, 0x0)
    mChargeUpdateInterval: (F32, 0x0, 0x0, 0x0)
    mCastingBreaksStealth: (Bool, 0x0, 0x0, 0x0)
    0xf9c2333e: (Map, Hash, Embed, SpellEffectAmount)
    DataValuesModeOverride: (Map, Hash, Embed, SpellDataValueVector)
    mLineMissileTargetHeightAugment: (F32, 0x0, 0x0, 0x0)
    mPlatformEnabled: (Bool, 0x0, 0x0, 0x0)
    mAnimationName: (String, 0x0, 0x0, 0x0)
    mMissileVisibleToOwnerTeamOnly: (Bool, 0x0, 0x0, 0x0)
    mLollipopAreaRadiusBegin: (List, 0x7, F32, 0x0)
    pass

class OptionItemDropdownItem():
    Value: (I32, 0x0, 0x0, 0x0)
    TraKey: (String, 0x0, 0x0, 0x0)
    pass

class VfxAnimatedColorVariableData(VfxColorBase):
    Values: (List, 0x0, Vec4, 0x0)
    Times: (List, 0x0, F32, 0x0)
    ProbabilityTables: (List, 0x4, Pointer, VfxProbabilityTableData)
    pass

class ILoopScriptBlock(IScriptBlock):
    Sequence: (Embed, 0x0, 0x0, ScriptSequence)
    pass

class ModifierAddedCalculationPart():
    Parts: (List, 0x0, Pointer, IGameCalculationPart)
    RequiredStat: (U8, 0x0, 0x0, 0x0)
    RequiredStatFormula: (U8, 0x0, 0x0, 0x0)
    pass

class TftSetData():
    AugmentContainerName: (String, 0x0, 0x0, 0x0)
    Number: (U32, 0x0, 0x0, 0x0)
    0x250b81df: (Pointer, 0x0, 0x0, 0x2483c715)
    UnitShopUiOverride: (Pointer, 0x0, 0x0, 0x2483c715)
    DropRateTables: (Map, String, Link, TftDropRateTable)
    StageRoundData: (Link, 0x0, 0x0, TftStageRoundData)
    BotSkillData: (Link, 0x0, 0x0, TftBotSkillData)
    BotSkillData: (Map, U8, Link, TftBotSkillData)
    Items: (List, 0x0, Link, TftItemData)
    0x412bcd03: (Link, 0x0, 0x0, 0x34d37457)
    0x46bf1dcb: (Link, 0x0, 0x0, 0xa5f064ff)
    Stages: (List, 0x0, Embed, TftStageData)
    Stages: (List2, 0x0, Embed, TftStageData)
    TooltipList: (Link, 0x0, 0x0, TftTooltipList)
    ItemLists: (List, 0x0, Link, TftItemList)
    ItemLists: (List2, 0x0, Link, TftItemList)
    CompanionHealthPerTickMark: (U32, 0x0, 0x0, 0x0)
    DisplayName: (String, 0x0, 0x0, 0x0)
    UnitUpgrades: (List, 0x0, Link, TftUnitUpgradeData)
    UnitUpgrades: (List2, 0x0, Link, TftUnitUpgradeData)
    InfoNubData: (Pointer, 0x0, 0x0, TftInfoNubData)
    DebugCharacterLists: (List, 0x0, Link, MapCharacterList)
    DebugCharacterLists: (List2, 0x0, Link, MapCharacterList)
    GameStartSequenceOverride: (Hash, 0x0, 0x0, 0x0)
    GameStartSequenceOverride: (Link, 0x0, 0x0, TftGameStartSequence)
    CharacterLists: (List, 0x0, Link, MapCharacterList)
    CharacterLists: (List2, 0x0, Link, MapCharacterList)
    UnitPropertyLists: (List, 0x0, Link, TftUnitProperties)
    Traits: (List, 0x0, Link, TftTraitData)
    ScriptDataObjectLists: (List, 0x0, Link, ScriptDataObjectList)
    ScriptDataObjectLists: (List2, 0x0, Link, ScriptDataObjectList)
    0x8876469a: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    ShopDataLists: (List, 0x0, Link, TftShopDataList)
    ShopDataLists: (List2, 0x0, Link, TftShopDataList)
    CoreName: (String, 0x0, 0x0, 0x0)
    TraitUnitProperties: (List2, 0x0, String, 0x0)
    VfxResourceResolver: (Link, 0x0, 0x0, ResourceResolver)
    0x9fd292f5: (String, 0x0, 0x0, 0x0)
    TierBagList: (Link, 0x0, 0x0, ScriptDataObjectList)
    0xa8ae70b: (List2, 0x0, Link, TftTraitAssignmentVariation)
    TftGameType: (U32, 0x0, 0x0, 0x0)
    TraitList: (Link, 0x0, 0x0, TftTraitList)
    AugmentUiOverride: (Pointer, 0x0, 0x0, 0x2483c715)
    FloatingInfoOverride: (Pointer, 0x0, 0x0, 0x2483c715)
    ItemUnitProperties: (List2, 0x0, String, 0x0)
    Mutator: (String, 0x0, 0x0, 0x0)
    AugmentContainerTexture: (String, 0x0, 0x0, 0x0)
    ScriptData: (Map, String, Pointer, GameModeConstant)
    EncounterList: (Link, 0x0, 0x0, TftEncounterList)
    0xdacd2fc1: (Pointer, 0x0, 0x0, 0x252c22fd)
    0xe081f469: (I8, 0x0, 0x0, 0x0)
    TftCharacterLists: (List2, 0x0, Link, TftCharacterList)
    0xecb7a24b: (Link, 0x0, 0x0, TftUnitPropertyDefinition)
    ArmoryUiOverride: (Pointer, 0x0, 0x0, 0x2483c715)
    0xf5c7941: (Pointer, 0x0, 0x0, 0x2483c715)
    ShopDropRates: (Map, U8, Embed, 0x6db4b328)
    TraitLists: (List, 0x0, Link, TftTraitList)
    TraitLists: (List2, 0x0, Link, TftTraitList)
    ShopContentData: (Link, 0x0, 0x0, TftShopContentData)
    pass

class LinearTransformProcessorData(ValueProcessorData):
    mMultiplier: (F32, 0x0, 0x0, 0x0)
    mIncrement: (F32, 0x0, 0x0, 0x0)
    pass

class 0x43985a14(IFxActionInstance):
    pass

class TftCutsceneVfxClip(TftCutsceneClip):
    0x30c747df: (Bool, 0x0, 0x0, 0x0)
    EffectKey: (String, 0x0, 0x0, 0x0)
    BlackboardVfxSource: (String, 0x0, 0x0, 0x0)
    BlackboardAssociatedPlayers: (List2, 0x0, String, 0x0)
    pass

class PfxFieldNoiseDefinitionData():
    Position: (Embed, 0x0, 0x0, PfxAnimatedVector3fVariableData)
    Period: (Embed, 0x0, 0x0, PfxAnimatedFloatVariableData)
    VelocityDelta: (Embed, 0x0, 0x0, PfxAnimatedFloatVariableData)
    AxisFraction: (Vec3, 0x0, 0x0, 0x0)
    Radius: (Embed, 0x0, 0x0, PfxAnimatedFloatVariableData)
    pass

class 0x43aaf187():
    0x39b2057a: (Hash, 0x0, 0x0, 0x0)
    PhaseIcon: (Hash, 0x0, 0x0, 0x0)
    PhaseHitRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class ScriptContext():
    pass

class TftItemCodexViewController(ViewController):
    MobileBinPath: (String, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    PcMouseOffsetX: (I32, 0x0, 0x0, 0x0)
    PcMouseOffsetY: (I32, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    HeaderData: (Embed, 0x0, 0x0, TftItemCodexHeaderData)
    BaseBinPath: (String, 0x0, 0x0, 0x0)
    HorizontalRule: (Hash, 0x0, 0x0, 0x0)
    TftItemCodexEntryData: (Embed, 0x0, 0x0, TftItemCodexViewEntryData)
    GroupFramed: (Hash, 0x0, 0x0, 0x0)
    CondensedItemCombineTooltipData: (Embed, 0x0, 0x0, TftCondensedItemCombineTooltipData)
    ItemCombineTooltipData: (Embed, 0x0, 0x0, TftItemCombineTooltipData)
    LayoutRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x43e9418e(GameModeConstant):
    Trait: (Link, 0x0, 0x0, TftTraitData)
    pass

class SwitchBlock(IBlock):
    Cases: (List, 0x0, Embed, SwitchCase)
    Cases: (List, 0x0, Pointer, RsCase)
    Cases: (List, 0x0, Pointer, SwitchCase)
    pass

class SelectSmiteSpellBlock(SelectSpellBlock):
    pass

class ClearTargetAndKeepMovingOnMovementCompleteSpec(MissileBehaviorSpec):
    mReplacementHeightAugment: (F32, 0x0, 0x0, 0x0)
    pass

class StoreViewController(ViewController):
    CatalogBackground: (Hash, 0x0, 0x0, 0x0)
    0x11fe3ab2: (Hash, 0x0, 0x0, 0x0)
    0x1c69d900: (String, 0x0, 0x0, 0x0)
    0x1d9b78e8: (Pointer, 0x0, 0x0, 0xb2430347)
    StoreScene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    FilterArenaToggle: (Hash, 0x0, 0x0, 0x0)
    MythicView: (Pointer, 0x0, 0x0, StoreViewMythic)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    StoreCategoryButtonDefinitions: (List, 0x0, Embed, StoreCategoryButtonDefinition)
    FooterHyperlinks: (List, 0x0, Embed, UiHyperlink)
    0x7b557bdc: (Hash, 0x0, 0x0, 0x0)
    0x834e2e8d: (Embed, 0x0, 0x0, 0x834e2e8d)
    OfferGrid: (Hash, 0x0, 0x0, 0x0)
    0x9eae8cc2: (Hash, 0x0, 0x0, 0x0)
    FilterFeaturedToggle: (Hash, 0x0, 0x0, 0x0)
    0xac62d69a: (String, 0x0, 0x0, 0x0)
    FilterTacticianToggle: (Hash, 0x0, 0x0, 0x0)
    PurchasesView: (Pointer, 0x0, 0x0, StoreViewPurchases)
    MainViewPaneDefinition: (Pointer, 0x0, 0x0, ViewPaneDefinition)
    UiStoreItemTileData: (Embed, 0x0, 0x0, UiStoreItemTileData)
    FooterGrid: (Hash, 0x0, 0x0, 0x0)
    0xd2cc0cdf: (Hash, 0x0, 0x0, 0x0)
    ViewPaneLink: (Hash, 0x0, 0x0, 0x0)
    StoreCategoryButtons: (List, 0x0, Embed, StoreCategoryButtonDefinition)
    pass

class UiPositionRect(UiPositionBase):
    Anchors: (Pointer, 0x0, 0x0, AnchorBase)
    UiRect: (Embed, 0x0, 0x0, UiElementRect)
    IgnoreGlobalScale: (Bool, 0x0, 0x0, 0x0)
    RectSourceResolutionHeight: (U16, 0x0, 0x0, 0x0)
    0x981fbd00: (Bool, 0x0, 0x0, 0x0)
    DisablePixelSnappingY: (Bool, 0x0, 0x0, 0x0)
    DisablePixelSnappingX: (Bool, 0x0, 0x0, 0x0)
    RectSourceResolutionWidth: (U16, 0x0, 0x0, 0x0)
    DisableResolutionDownscale: (Bool, 0x0, 0x0, 0x0)
    Rect: (Vec4, 0x0, 0x0, 0x0)
    pass

class TrophyGemData():
    mName: (String, 0x0, 0x0, 0x0)
    mSkinMeshProperties: (Embed, 0x0, 0x0, SkinMeshDataProperties)
    mGemId: (U32, 0x0, 0x0, 0x0)
    mAnimationGraphData: (Link, 0x0, 0x0, AnimationGraphData)
    mImage: (String, 0x0, 0x0, 0x0)
    pass

class PerkSummonerSpecialistChoices():
    mSpells: (List, 0x0, Hash, 0x0)
    pass

class ScriptTargetingRangeValue(ITargetingRangeValue):
    TargetingParamName: (String, 0x0, 0x0, 0x0)
    pass

class CharacterVarsTable(ScriptTable):
    pass

class MapComponent():
    pass

class MinimapIconScale(MinimapIconBehavior):
    StartScale: (Vec2, 0x0, 0x0, 0x0)
    TargetScale: (Vec2, 0x0, 0x0, 0x0)
    EaseType: (U8, 0x0, 0x0, 0x0)
    pass

class BoolGet(IBoolGet, IScriptValueGet):
    Value: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x4527cab3():
    Groups: (List2, 0x0, Embed, 0x6b37502b)
    pass

class 0x45471b1e(IBehaviorScriptBlock):
    pass

class PassDef():
    SrcColorBlendFactor: (U32, 0x0, 0x0, 0x0)
    FogColor: (Color, 0x0, 0x0, 0x0)
    BlendEnable: (Bool, 0x0, 0x0, 0x0)
    FogColorG: (F32, 0x0, 0x0, 0x0)
    FogColorB: (F32, 0x0, 0x0, 0x0)
    FogColorA: (F32, 0x0, 0x0, 0x0)
    FogColorR: (F32, 0x0, 0x0, 0x0)
    StencilEnable: (Bool, 0x0, 0x0, 0x0)
    AlphaTestCompareFunc: (U32, 0x0, 0x0, 0x0)
    CullEnable: (Bool, 0x0, 0x0, 0x0)
    WindingToCull: (U32, 0x0, 0x0, 0x0)
    VertexShader: (String, 0x0, 0x0, 0x0)
    StencilPassDepthPassOp: (U32, 0x0, 0x0, 0x0)
    FragmentShader: (String, 0x0, 0x0, 0x0)
    WriteDepth: (Bool, 0x0, 0x0, 0x0)
    DstAlphaBlendFactor: (U32, 0x0, 0x0, 0x0)
    WriteStencil: (Bool, 0x0, 0x0, 0x0)
    WriteR: (Bool, 0x0, 0x0, 0x0)
    BlendEquation: (U32, 0x0, 0x0, 0x0)
    WriteG: (Bool, 0x0, 0x0, 0x0)
    WriteA: (Bool, 0x0, 0x0, 0x0)
    WriteB: (Bool, 0x0, 0x0, 0x0)
    StencilCompareFunc: (U32, 0x0, 0x0, 0x0)
    SrcAlphaBlendFactor: (U32, 0x0, 0x0, 0x0)
    DepthCompareFunc: (U32, 0x0, 0x0, 0x0)
    SamplerValues: (List, 0x0, Embed, ShaderSamplerDef)
    StencilPassDepthFailOp: (U32, 0x0, 0x0, 0x0)
    StencilMask: (U32, 0x0, 0x0, 0x0)
    WriteMask: (U32, 0x0, 0x0, 0x0)
    DstColorBlendFactor: (U32, 0x0, 0x0, 0x0)
    FogEnable: (Bool, 0x0, 0x0, 0x0)
    StencilReferenceVal: (U32, 0x0, 0x0, 0x0)
    AlphaTestNormalizedReferenceValue: (F32, 0x0, 0x0, 0x0)
    AlphaTestEnable: (Bool, 0x0, 0x0, 0x0)
    ParamValues: (List, 0x0, Embed, ShaderParamDef)
    DepthEnable: (Bool, 0x0, 0x0, 0x0)
    StencilFailOp: (U32, 0x0, 0x0, 0x0)
    ShaderMacros: (List, 0x0, Embed, ShaderMacroDef)
    ShaderMacros: (Map, String, String, 0x0)
    pass

class DeathRecapShowcaseSlotStatStoneData(DeathRecapShowcaseSlotData):
    Icon: (Hash, 0x0, 0x0, 0x0)
    DetailsText: (Hash, 0x0, 0x0, 0x0)
    HitRegion: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class CheatSet():
    mName: (String, 0x0, 0x0, 0x0)
    mAssociatedChampion: (Link, 0x0, 0x0, Champion)
    mIsPlayerFacing: (Bool, 0x0, 0x0, 0x0)
    mCheats: (List, 0x0, Link, Cheat)
    mCheatPages: (List, 0x0, Embed, CheatPage)
    mUseIconsForButtons: (Bool, 0x0, 0x0, 0x0)
    mGameMutator: (String, 0x0, 0x0, 0x0)
    mGameModeName: (Hash, 0x0, 0x0, 0x0)
    AssociatedChampions: (List2, 0x0, Embed, 0x9d79fb9f)
    mIsUiAlwaysShown: (Bool, 0x0, 0x0, 0x0)
    mGameMode: (U32, 0x0, 0x0, 0x0)
    pass

class IStringGet(IRsValueGet, IScriptValueGet):
    pass

class 0x45a556cd(0x26d26471):
    AndConditions: (List2, 0x0, Pointer, 0x26d26471)
    pass

class VfxSystemDefinitionData(IResource):
    SelfIllumination: (F32, 0x0, 0x0, 0x0)
    AssetCategory: (String, 0x0, 0x0, 0x0)
    MaterialOverrideDefinitions: (List, 0x0, Embed, VfxMaterialOverrideDefinitionData)
    MaterialOverrideDefinitions: (List, 0x0, Pointer, VfxMaterialOverrideDefinitionData)
    ScaleCap: (F32, 0x0, 0x0, 0x0)
    OverrideScaleCap: (Option, 0x0, F32, 0x0)
    VoiceOverOnCreateDefault: (String, 0x0, 0x0, 0x0)
    AudioParameterFlexId: (I32, 0x0, 0x0, 0x0)
    AudioParameterFlexId: (U32, 0x0, 0x0, 0x0)
    SoundPersistentDefault: (String, 0x0, 0x0, 0x0)
    SystemTranslation: (Vec3, 0x0, 0x0, 0x0)
    SimpleEmitterDefinitionData: (List, 0x0, Pointer, VfxEmitterDefinitionData)
    SimpleEmitterDefinitionData: (List, 0x0, Pointer, VfxSimpleEmitterDefinitionData)
    mEyeCandy: (Bool, 0x0, 0x0, 0x0)
    ComplexEmitterDefinitionData: (List, 0x0, Pointer, VfxComplexEmitterDefinitionData)
    ComplexEmitterDefinitionData: (List, 0x0, Pointer, VfxEmitterDefinitionData)
    Flags: (U16, 0x0, 0x0, 0x0)
    Flags: (U32, 0x0, 0x0, 0x0)
    Flags: (U8, 0x0, 0x0, 0x0)
    AudioParameterTimeScaledDuration: (F32, 0x0, 0x0, 0x0)
    ClockToUse: (U8, 0x0, 0x0, 0x0)
    HudLayerAspect: (F32, 0x0, 0x0, 0x0)
    HudLayerStretchFullscreen: (Bool, 0x0, 0x0, 0x0)
    DrawingLayer: (U32, 0x0, 0x0, 0x0)
    DrawingLayer: (U8, 0x0, 0x0, 0x0)
    mIsPoseAfterimage: (Bool, 0x0, 0x0, 0x0)
    AssetRemappingTable: (List, 0x0, Embed, VfxAssetRemap)
    HudAnchorPositionFromWorldProjection: (Bool, 0x0, 0x0, 0x0)
    VoiceOverPersistentDefault: (String, 0x0, 0x0, 0x0)
    SoundOnCreateDefault: (String, 0x0, 0x0, 0x0)
    Transform: (Mtx44, 0x0, 0x0, 0x0)
    SystemScale: (Vec3, 0x0, 0x0, 0x0)
    ParticlePath: (String, 0x0, 0x0, 0x0)
    BuildUpTime: (F32, 0x0, 0x0, 0x0)
    ParticleName: (String, 0x0, 0x0, 0x0)
    AudioFlexValueParameterName: (String, 0x0, 0x0, 0x0)
    ScaleDynamicallyWithAttachedBone: (Bool, 0x0, 0x0, 0x0)
    HudLayerDimension: (F32, 0x0, 0x0, 0x0)
    0xf97b1289: (Pointer, 0x0, 0x0, 0x7fb92f53)
    VisibilityRadius: (F32, 0x0, 0x0, 0x0)
    pass

class MaterialInstanceDynamicSwitch():
    Enabled: (Bool, 0x0, 0x0, 0x0)
    Driver: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    Driver: (Pointer, 0x0, 0x0, IDynamicMaterialBoolDriver)
    pass

class LobbyFriendPortraitData():
    SummonerIcon: (Hash, 0x0, 0x0, 0x0)
    ArenaSkinIcon: (Hash, 0x0, 0x0, 0x0)
    PartyLeaderIcon: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    LoadoutsFrame: (Hash, 0x0, 0x0, 0x0)
    SummonerIconFrame: (Hash, 0x0, 0x0, 0x0)
    RankText: (Hash, 0x0, 0x0, 0x0)
    LittleLegendIcon: (Hash, 0x0, 0x0, 0x0)
    EditButton: (Hash, 0x0, 0x0, 0x0)
    NameText: (Hash, 0x0, 0x0, 0x0)
    InviteButton: (Hash, 0x0, 0x0, 0x0)
    RankTextLine2: (Hash, 0x0, 0x0, 0x0)
    pass

class SwitchMaterialDriverElement():
    mValue: (Pointer, 0x0, 0x0, IDynamicMaterialDriver)
    mValue: (Pointer, 0x0, 0x0, ILogicDriver)
    mCondition: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    mCondition: (Pointer, 0x0, 0x0, IDynamicMaterialBoolDriver)
    pass

class 0x45f140fc():
    0x10074827: (String, 0x0, 0x0, 0x0)
    TitleVictoryTra: (String, 0x0, 0x0, 0x0)
    0x3fca802: (String, 0x0, 0x0, 0x0)
    TitleDefeatTra: (String, 0x0, 0x0, 0x0)
    0x4c453e79: (String, 0x0, 0x0, 0x0)
    TitleNextTra: (String, 0x0, 0x0, 0x0)
    0x8e3d338b: (String, 0x0, 0x0, 0x0)
    TitleFutureTra: (String, 0x0, 0x0, 0x0)
    0xd0133f4a: (String, 0x0, 0x0, 0x0)
    0xe130f1de: (String, 0x0, 0x0, 0x0)
    pass

class MapPrefabInstance(MapPlaceable):
    Prefab: (Link, 0x0, 0x0, MapPlaceableContainer)
    PrefabDefinition: (Link, 0x0, 0x0, MapPlaceableContainer)
    pass

class ContextualConditionGlobalObjectiveBountyFirstActivation(IContextualCondition):
    pass

class LuaPropertyDataFloat(LuaPropertyData):
    Value: (F32, 0x0, 0x0, 0x0)
    pass

class TrophyData(BaseLoadoutData):
    mPerceptionBubbleRadius: (F32, 0x0, 0x0, 0x0)
    SkinMeshProperties: (Embed, 0x0, 0x0, SkinMeshDataProperties)
    mBracketTraKey: (String, 0x0, 0x0, 0x0)
    mSkinMeshProperties: (Embed, 0x0, 0x0, SkinMeshDataProperties)
    mVfxResourceResolver: (Pointer, 0x0, 0x0, ResourceResolver)
    mAnimationGraphData: (Link, 0x0, 0x0, AnimationGraphData)
    AnimationGraphData: (Link, 0x0, 0x0, AnimationGraphData)
    pass

class JunglePathRecommendations():
    DesignerOverridePath: (Hash, 0x0, 0x0, 0x0)
    DataDrivenPath: (Hash, 0x0, 0x0, 0x0)
    pass

class BuffData():
    mName: (String, 0x0, 0x0, 0x0)
    mFloatVarsDecimals: (List, 0x10, I32, 0x0)
    mTooltipData: (Pointer, 0x0, 0x0, TooltipInstanceBuff)
    mBuffVfxSpawnConditions: (List, 0x0, Pointer, IVfxSpawnConditions)
    mBuffAttributeFlags: (U8, 0x0, 0x0, 0x0)
    mShowDurationOnSpellSlot: (U32, 0x0, 0x0, 0x0)
    mDeathRecapPriority: (I32, 0x0, 0x0, 0x0)
    CanTimeoutWhileCasting: (Bool, 0x0, 0x0, 0x0)
    PersistentEffectConditions: (List, 0x0, Pointer, PersistentEffectConditionData)
    PersistentEffectConditions: (List2, 0x0, Pointer, PersistentEffectConditionData)
    mVfxSpawnConditions: (List, 0x0, Pointer, VfxSpawnConditions)
    mShowInTrackerUi: (Bool, 0x0, 0x0, 0x0)
    BuffEffects: (List, 0x0, Pointer, BuffEffect)
    mShowDuration: (Bool, 0x0, 0x0, 0x0)
    mShowAccumulatedDuration: (Bool, 0x0, 0x0, 0x0)
    mBuffAttributeFlag: (U8, 0x0, 0x0, 0x0)
    mPersistentVfxs: (List, 0x0, Embed, EffectCreationData)
    mDescription: (String, 0x0, 0x0, 0x0)
    pass

class AvailableQuestList():
    SecondaryQuest: (Embed, 0x0, 0x0, QuestDefinition)
    CorkiCharacterQuest: (Embed, 0x0, 0x0, QuestDefinition)
    PrimaryQuest: (Embed, 0x0, 0x0, QuestDefinition)
    NewContentNotificationQuest: (Embed, 0x0, 0x0, QuestDefinition)
    ScoreDisplayQuest: (Embed, 0x0, 0x0, QuestDefinition)
    ObjectiveQuest: (Embed, 0x0, 0x0, QuestDefinition)
    pass

class PlaybookGridButtonData():
    Scene: (Hash, 0x0, 0x0, 0x0)
    EquippedIcon: (Hash, 0x0, 0x0, 0x0)
    Name: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x4664ae0a():
    pass

class SpecificColorMaterialDriver(IDynamicMaterialDriver, ILogicDriver):
    mColor: (Vec4, 0x0, 0x0, 0x0)
    pass

class ItemRecommendationItemList():
    mItemList: (List, 0x0, U32, 0x0)
    pass

class UiStatStonesStats():
    StatStoneTitle: (Hash, 0x0, 0x0, 0x0)
    StatStoneTemplateScene: (Hash, 0x0, 0x0, 0x0)
    StatStoneCount: (Hash, 0x0, 0x0, 0x0)
    AnimationDelaySecs: (F32, 0x0, 0x0, 0x0)
    SeriesTitleHandle: (Hash, 0x0, 0x0, 0x0)
    MinAlpha: (U8, 0x0, 0x0, 0x0)
    ButtonNext: (Hash, 0x0, 0x0, 0x0)
    StatStoneHoverTargets: (List, 0x3, Hash, 0x0)
    TextFadeTransitionSecs: (F32, 0x0, 0x0, 0x0)
    StatStoneIcon: (Hash, 0x0, 0x0, 0x0)
    MaxAlpha: (U8, 0x0, 0x0, 0x0)
    ButtonPrev: (Hash, 0x0, 0x0, 0x0)
    SlideTransitionSecs: (F32, 0x0, 0x0, 0x0)
    pass

class FxActionSfxAttachInstance(IFxActionInstance):
    pass

class 0x46ebf194(ICatalogEntryOwner, BaseLoadoutData):
    CatalogEntry: (Embed, 0x0, 0x0, CatalogEntry)
    NameTraKey: (String, 0x0, 0x0, 0x0)
    pass

class CharacterVars(ScriptTable):
    pass

class TftOutOfGameCharData():
    Name: (String, 0x0, 0x0, 0x0)
    SquareIconTexturePath: (String, 0x0, 0x0, 0x0)
    pass

class UiElementGroupSliderData(UiElementGroupData):
    SliderClickedState: (Embed, 0x0, 0x0, UiElementGroupSliderState)
    SliderHitRegion: (Link, 0x0, 0x0, RegionElementData)
    SliderHitRegion: (Link, 0x0, 0x0, UiElementRegionData)
    SliderHoveredState: (Embed, 0x0, 0x0, UiElementGroupSliderState)
    SoundEvents: (Pointer, 0x0, 0x0, UiElementGroupSliderSoundEvents)
    BarHoveredState: (Embed, 0x0, 0x0, UiElementGroupSliderState)
    DefaultState: (Embed, 0x0, 0x0, UiElementGroupSliderState)
    IsEnabled: (Bool, 0x0, 0x0, 0x0)
    Direction: (U8, 0x0, 0x0, 0x0)
    BarHitRegion: (Link, 0x0, 0x0, RegionElementData)
    BarHitRegion: (Link, 0x0, 0x0, UiElementRegionData)
    pass

class 0x4750ceb6(IStringCalculation):
    RangedResult: (String, 0x0, 0x0, 0x0)
    DefaultResult: (String, 0x0, 0x0, 0x0)
    MeleeResult: (String, 0x0, 0x0, 0x0)
    pass

class QualitySetting():
    mName: (String, 0x0, 0x0, 0x0)
    mFxAa: (Bool, 0x0, 0x0, 0x0)
    mFrameCap: (U32, 0x0, 0x0, 0x0)
    mBackBufferScale: (F32, 0x0, 0x0, 0x0)
    mShadowQuality: (U32, 0x0, 0x0, 0x0)
    mCharaterQuality: (U32, 0x0, 0x0, 0x0)
    mEffectsQuality: (U32, 0x0, 0x0, 0x0)
    mEnvironmentQuality: (U32, 0x0, 0x0, 0x0)
    pass

class StrawberryAugmentDisplayTagData():
    AugmentDisplayTagSpacer: (Hash, 0x0, 0x0, 0x0)
    AugmentDisplayTagRow: (Hash, 0x0, 0x0, 0x0)
    AugmentDisplayTagFrame: (Hash, 0x0, 0x0, 0x0)
    AugmentDisplayTagText: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x47884d9d(IBooleanParametricUpdater):
    BuffName: (Hash, 0x0, 0x0, 0x0)
    pass

class UiMilestoneTimelineEnd():
    MilestoneRegion: (Hash, 0x0, 0x0, 0x0)
    MeterAvailable: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    MeterComplete: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    TextAvailable: (Hash, 0x0, 0x0, 0x0)
    FrameComplete: (Hash, 0x0, 0x0, 0x0)
    PipComplete: (Hash, 0x0, 0x0, 0x0)
    PipAvailable: (Hash, 0x0, 0x0, 0x0)
    TextComplete: (Hash, 0x0, 0x0, 0x0)
    FrameAvailable: (Hash, 0x0, 0x0, 0x0)
    pass

class SyncCircleMovementSpec(MissileMovementSpec):
    mAngularVelocity: (F32, 0x0, 0x0, 0x0)
    mLifetime: (F32, 0x0, 0x0, 0x0)
    pass

class TargeterDefinitionRange(TargeterDefinition):
    TextureOrientation: (U32, 0x0, 0x0, 0x0)
    RangeGrowthMax: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    TextureMaxGrowName: (String, 0x0, 0x0, 0x0)
    RangeGrowthDuration: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    TextureOverrideName: (String, 0x0, 0x0, 0x0)
    RangeGrowthStartTime: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    UseCasterBoundingBox: (Bool, 0x0, 0x0, 0x0)
    UseCasterBoundingBox: (Option, 0x0, Bool, 0x0)
    HideWithLineIndicator: (Bool, 0x0, 0x0, 0x0)
    CenterLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    OverrideBaseRange: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    HasMaxGrowRange: (Bool, 0x0, 0x0, 0x0)
    pass

class TurretFirstBloodLogic(IStatStoneLogicDriver):
    pass

class HeroFloatingInfoCharacterStateIndicatorList():
    StateIndicatorList: (List, 0x0, Hash, 0x0)
    pass

class CameraTrapezoid():
    mMaxXTop: (F32, 0x0, 0x0, 0x0)
    mMaxZUp: (F32, 0x0, 0x0, 0x0)
    mMaxZDown: (F32, 0x0, 0x0, 0x0)
    mMaxXBottom: (F32, 0x0, 0x0, 0x0)
    pass

class ChampionNameUiData():
    ChampionNameText: (Hash, 0x0, 0x0, 0x0)
    pass

class HeroFloatingInfoIconsData():
    Icons: (List, 0x0, Embed, HeroFloatingInfoIconData)
    pass

class TargetIsWithinNDistanceOfCaster(ICastRequirement):
    Distance: (F32, 0x0, 0x0, 0x0)
    pass

class 0x483e0716():
    VfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    RegionName: (Hash, 0x0, 0x0, 0x0)
    pass

class UiMetricUnitTypeI():
    pass

class TftHudUnitShopDropRate():
    DropRateSlots: (List, 0x5, Embed, DropRateSlot)
    DropRateSlots: (List, 0x5, Embed, TftDropRateSlot)
    DropRateSlotsList: (List2, 0x0, Embed, TftDropRateSlot)
    0xe2c6ffc9: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x487b1677():
    0x4d8cab3e: (List2, 0x0, Pointer, 0xa50ab26)
    0x4f199fc3: (List2, 0x0, Pointer, 0x48b2d5fb)
    0x6406d8f7: (List2, 0x0, Pointer, 0xa50ab26)
    pass

class ChampionAugmentTags():
    mBuildTags: (U32, 0x0, 0x0, 0x0)
    mExcludedTags: (U32, 0x0, 0x0, 0x0)
    ChampionName: (String, 0x0, 0x0, 0x0)
    Champion: (Link, 0x0, 0x0, Champion)
    pass

class UiTextureProviderBase():
    pass

class 0x48b2d5fb():
    RelationshipType: (U8, 0x0, 0x0, 0x0)
    0xa02845e3: (Hash, 0x0, 0x0, 0x0)
    0xa02845e3: (Link, 0x0, 0x0, Champion)
    0xa1284776: (Hash, 0x0, 0x0, 0x0)
    0xa1284776: (Link, 0x0, 0x0, Champion)
    pass

class EsportLeagueEntry():
    LeagueName: (String, 0x0, 0x0, 0x0)
    TextureName: (String, 0x0, 0x0, 0x0)
    pass

class FxActionVfxAttachInstance(IFxActionInstance):
    pass

class AnnouncementStyleOneIcon(AnnouncementStyleBasic):
    SourceIcon: (Link, 0x0, 0x0, AnnouncementIcon)
    pass

class MapParticleGroups():
    Groups: (List, 0x0, String, 0x0)
    pass

class EventConfig():
    mDeathRecapBasePriorityFactorPerLevel: (F32, 0x0, 0x0, 0x0)
    mLogCombatEvents: (Bool, 0x0, 0x0, 0x0)
    mDeathRecapExtensionTimeWindow: (F32, 0x0, 0x0, 0x0)
    mDeathRecapMinimumTimeWindow: (F32, 0x0, 0x0, 0x0)
    pass

class GdsMapObjectExtraInfo():
    pass

class ElementalSelectionViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    FirstSelectionAnimationDelay: (F32, 0x0, 0x0, 0x0)
    ElementMeters: (List, 0xa, Hash, 0x0)
    GlowingRingCycleTime: (F32, 0x0, 0x0, 0x0)
    InnerRing: (Hash, 0x0, 0x0, 0x0)
    FadingScene: (Hash, 0x0, 0x0, 0x0)
    MeterFilledButtonFadeInDelay: (F32, 0x0, 0x0, 0x0)
    ElementTransformButtons: (List, 0x4, Hash, 0x0)
    PortraitScene: (Hash, 0x0, 0x0, 0x0)
    TransformScene: (Hash, 0x0, 0x0, 0x0)
    ElementColors: (List, 0xa, Color, 0x0)
    Loadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    FinalFormLeftFx: (Hash, 0x0, 0x0, 0x0)
    FinalFormRightFx: (Hash, 0x0, 0x0, 0x0)
    SecondElementSelectedDelayedAnimations: (List, 0x0, Hash, 0x0)
    FirstElementSelectedAnimations: (List, 0x0, Hash, 0x0)
    MeterScene: (Hash, 0x0, 0x0, 0x0)
    ThickOuterRing: (Hash, 0x0, 0x0, 0x0)
    AnimScene: (Hash, 0x0, 0x0, 0x0)
    FirstElementSelectedDelayedAnimations: (List, 0x0, Hash, 0x0)
    ElementIconsFullButtons: (List, 0xa, Hash, 0x0)
    ElementIconsSmall: (List, 0xa, Hash, 0x0)
    CloseButton: (Hash, 0x0, 0x0, 0x0)
    SecondSelectionAnimationDelay: (F32, 0x0, 0x0, 0x0)
    DelayedCharacterPortrait: (Hash, 0x0, 0x0, 0x0)
    SecondElementSelectedAnimations: (List, 0x0, Hash, 0x0)
    MeterFullAnimations: (List, 0x0, Hash, 0x0)
    GlowingRing: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x48eb8d47():
    pass

class ViewControllerListFilter_Champion(ViewControllerListFilterI):
    Relationship: (U8, 0x0, 0x0, 0x0)
    ChampionSkinDataLink: (String, 0x0, 0x0, 0x0)
    pass

class 0x48f3fe52():
    0xb9cb9ce8: (List2, 0x0, Embed, 0x7084628f)
    0xb9cb9ce8: (List2, 0x0, Embed, 0xdf694fb2)
    pass

class JungleLocationMapInformation():
    Name: (String, 0x0, 0x0, 0x0)
    Index: (U8, 0x0, 0x0, 0x0)
    Position: (Vec3, 0x0, 0x0, 0x0)
    Location: (U8, 0x0, 0x0, 0x0)
    pass

class OptionTemplateButton(IOptionTemplate):
    DescriptionDefinition: (Hash, 0x0, 0x0, 0x0)
    ButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class TftScoreboardViewController(ViewController):
    OverrideFillMeterSelfColor: (Color, 0x0, 0x0, 0x0)
    ViewingIcon: (Hash, 0x0, 0x0, 0x0)
    NotificationTemplate: (Embed, 0x0, 0x0, TftScoreboardNotificationTemplate)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    FillMeterOpponentColor: (Color, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    ToggleButton: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideBinName: (String, 0x0, 0x0, 0x0)
    PlayerSelfTemplate: (Embed, 0x0, 0x0, TftScoreboardPlayerTemplate)
    OverrideFillMeterOpponentColor: (Color, 0x0, 0x0, 0x0)
    ActivateScoreboardButton: (Hash, 0x0, 0x0, 0x0)
    FillMeterSelfColor: (Color, 0x0, 0x0, 0x0)
    PlayerOpponentTemplate: (Embed, 0x0, 0x0, TftScoreboardPlayerTemplate)
    OpponentBounds: (Hash, 0x0, 0x0, 0x0)
    ActivateCombatRecapButton: (Hash, 0x0, 0x0, 0x0)
    0xe26f4055: (Embed, 0x0, 0x0, 0x138c3d23)
    BaseBinName: (String, 0x0, 0x0, 0x0)
    0xfbefff74: (Hash, 0x0, 0x0, 0x0)
    pass

class RelicDropConfig():
    0x6adb7681: (F32, 0x0, 0x0, 0x0)
    0x7441d8a8: (F32, 0x0, 0x0, 0x0)
    0x7741dd61: (F32, 0x0, 0x0, 0x0)
    0x911425e9: (List, 0x0, Link, RelicDropScenario)
    0xd37868f: (F32, 0x0, 0x0, 0x0)
    0xe378822: (F32, 0x0, 0x0, 0x0)
    pass

class 0x49cb6889(MapGraphicsFeature):
    CubemapProbePrefix: (String, 0x0, 0x0, 0x0)
    Constants: (List2, 0x0, Embed, 0xc668ae80)
    ProbeA: (Hash, 0x0, 0x0, 0x0)
    ProbeB: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxDistortionDefinitionData():
    DistortionMode: (U32, 0x0, 0x0, 0x0)
    DistortionMode: (U8, 0x0, 0x0, 0x0)
    Distortion: (F32, 0x0, 0x0, 0x0)
    NormalMapTexture: (String, 0x0, 0x0, 0x0)
    pass

class TftCharacterPositioningData():
    TextTra: (String, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class MapActionSetMaterialFloat(MapAction):
    Value: (F32, 0x0, 0x0, 0x0)
    PropName: (String, 0x0, 0x0, 0x0)
    Key: (String, 0x0, 0x0, 0x0)
    pass

class InputEventFloat(InputEventBase):
    QuantizationScale: (F32, 0x0, 0x0, 0x0)
    DeadZone: (F32, 0x0, 0x0, 0x0)
    Sources: (List, 0x0, Pointer, IInputSourceFloat)
    FireOnReturningToDeadZone: (Bool, 0x0, 0x0, 0x0)
    CombineMode: (U32, 0x0, 0x0, 0x0)
    pass

class ISecondaryResourceDisplayData():
    pass

class SelectorClipData(ClipBaseData):
    mSelectorPairDataList: (List, 0x0, Embed, SelectorClipPairData)
    mSelectorPairDataList: (List, 0x0, Embed, SelectorPairData)
    mTrackIndex: (U32, 0x0, 0x0, 0x0)
    pass

class CharacterPreloadList():
    mCharacters: (List, 0x0, Embed, CharacterPreloadData)
    pass

class ItemSlotDetailedUiData():
    AmmoFx: (Hash, 0x0, 0x0, 0x0)
    OverlayDisabled: (Hash, 0x0, 0x0, 0x0)
    MajorActiveMythic: (Hash, 0x0, 0x0, 0x0)
    CompleteFx: (Hash, 0x0, 0x0, 0x0)
    ToggleFx: (Hash, 0x0, 0x0, 0x0)
    BorderMythic: (Hash, 0x0, 0x0, 0x0)
    HotkeyText: (Hash, 0x0, 0x0, 0x0)
    BorderEnabled: (Hash, 0x0, 0x0, 0x0)
    BorderDisabled: (Hash, 0x0, 0x0, 0x0)
    OverlayOom: (Hash, 0x0, 0x0, 0x0)
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    BorderDefault: (Hash, 0x0, 0x0, 0x0)
    HitArea: (Hash, 0x0, 0x0, 0x0)
    BorderSelected: (Hash, 0x0, 0x0, 0x0)
    NewItemFx: (Hash, 0x0, 0x0, 0x0)
    OverlayLoc: (Hash, 0x0, 0x0, 0x0)
    StackText: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    OverlayHover: (Hash, 0x0, 0x0, 0x0)
    CooldownEffects: (Embed, 0x0, 0x0, CooldownEffectUiData)
    MajorActive: (Hash, 0x0, 0x0, 0x0)
    pass

class DestroyChildrenOnMovementComplete(MissileBehaviorSpec):
    mDelay: (I32, 0x0, 0x0, 0x0)
    pass

class 0x4a4575a8(MapAction):
    MapParticleNames: (List2, 0x0, String, 0x0)
    TextureOverride: (Pointer, 0x0, 0x0, 0x3e265091)
    pass

class 0x4a70b12c():
    AugmentGroup: (List2, 0x0, Link, BorderSkinAugment)
    pass

class 0x4a7922fb():
    AugmentSlots: (Embed, 0x0, 0x0, 0xfc331f53)
    pass

class StatFormulaDataList():
    StatFormulas: (Map, U32, Embed, StatFormulaData)
    StatFormulas: (Map, U8, Embed, StatFormulaData)
    pass

class InteractionData():
    DoubleSided: (Bool, 0x0, 0x0, 0x0)
    IdleAnim: (String, 0x0, 0x0, 0x0)
    ShouldRandomizeIdleAnimPhase: (Bool, 0x0, 0x0, 0x0)
    pass

class RotatingBanner():
    Banner: (Link, 0x0, 0x0, EsportsBannerData)
    TextureDefinitions: (List, 0x0, Embed, RotatingBannerEntry)
    BannerSet: (Link, 0x0, 0x0, RotatingBannerSet)
    pass

class CircleMovementSpec(MissileMovementSpec):
    mAngularVelocity: (F32, 0x0, 0x0, 0x0)
    mLinearVelocity: (F32, 0x0, 0x0, 0x0)
    mRadialVelocity: (F32, 0x0, 0x0, 0x0)
    mLifetime: (F32, 0x0, 0x0, 0x0)
    pass

class ParametricMovementType():
    pass

class BuffCounterByCoefficientCalculationPart(IGameCalculationPartWithBuffCounter, ISpellCalculationPartWithBuffCounter, ISpellCalculationPart):
    mBuffName: (Hash, 0x0, 0x0, 0x0)
    mCoefficient: (F32, 0x0, 0x0, 0x0)
    mIconKey: (String, 0x0, 0x0, 0x0)
    mScalingTagKey: (String, 0x0, 0x0, 0x0)
    pass

class QuestTrackerViewController(ViewController):
    GroupFadeTransitionTimeSec: (F32, 0x0, 0x0, 0x0)
    PulseTimeSec: (F32, 0x0, 0x0, 0x0)
    MessageTemplate: (Embed, 0x0, 0x0, QuestTrackerMessageTemplate)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    BetweenGroupSpacing: (U32, 0x0, 0x0, 0x0)
    MessageDisplayData: (Embed, 0x0, 0x0, HudMessageDisplayData)
    PulseStartDelaySec: (F32, 0x0, 0x0, 0x0)
    FullBrightnessDurationSec: (F32, 0x0, 0x0, 0x0)
    DuckedAlphaValue: (F32, 0x0, 0x0, 0x0)
    HeaderTextTemplate: (Hash, 0x0, 0x0, 0x0)
    QuestLingerDurationSec: (F32, 0x0, 0x0, 0x0)
    SceneTemplate: (Hash, 0x0, 0x0, 0x0)
    ItemSceneTemplate: (Hash, 0x0, 0x0, 0x0)
    pass

class ColorChooserMaterialDriver(IDynamicMaterialDriver, ILogicDriver):
    mColorOn: (Vec4, 0x0, 0x0, 0x0)
    mColorOff: (Vec4, 0x0, 0x0, 0x0)
    mBoolDriver: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    mBoolDriver: (Pointer, 0x0, 0x0, IDynamicMaterialBoolDriver)
    pass

class OptionItemResolutionDropdown(OptionItemDropdown):
    pass

class 0x4b26ffad(0x27071fbd):
    Value: (Map, U32, Hash, 0x0)
    pass

class FunctionTableSet(ScriptTableSet):
    pass

class 0x4b3c671d(IScriptBlock, IBehaviorScriptBlock):
    pass

class TftTrovesBannerTable(TftTrovesBannerNode):
    NameTraKey: (String, 0x0, 0x0, 0x0)
    Children: (List, 0x0, Embed, TftTrovesBannerTableEntry)
    DisplayPriority: (U32, 0x0, 0x0, 0x0)
    pass

class 0x4b7bc412(ILolSpellScriptEvent):
    pass

class VfxBeamParticleDefinitionData():
    AnimatedColorWithDistance: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    AnimatedColorWithDistance: (Embed, 0x0, 0x0, ValueColor)
    IsColorBindedWithDistance: (Bool, 0x0, 0x0, 0x0)
    pass

class HudMessageDisplayData():
    MessageCount: (U32, 0x0, 0x0, 0x0)
    MessageDurationSecs: (F32, 0x0, 0x0, 0x0)
    TransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    MessageDuration: (F32, 0x0, 0x0, 0x0)
    0xf13367cf: (Bool, 0x0, 0x0, 0x0)
    pass

class TreatAutoAttacksAsNormalSpells():
    AutoAttackSpellsUseSpellSource: (Bool, 0x0, 0x0, 0x0)
    SkipSequencedAttackEvents: (Bool, 0x0, 0x0, 0x0)
    OverrideQueryableAttackRange: (Pointer, 0x0, 0x0, IGameCalculation)
    pass

class RandomFloatMaterialDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    pass

class VfxPrimitiveArbitraryQuad(VfxPrimitiveBase):
    pass

class UnitStatusData():
    AttackableUnitStatusType: (U32, 0x0, 0x0, 0x0)
    StatusName: (String, 0x0, 0x0, 0x0)
    TextColor: (Option, 0x0, Color, 0x0)
    TextureUvs: (Vec4, 0x0, 0x0, 0x0)
    ImageInfo: (Embed, 0x0, 0x0, HealthbarImageInfo)
    LocType: (U32, 0x0, 0x0, 0x0)
    pass

class ConfigInt():
    Enabler: (Link, 0x0, 0x0, IEnabler)
    Value: (I32, 0x0, 0x0, 0x0)
    pass

class UiHyperlink():
    DisplayText: (Hash, 0x0, 0x0, 0x0)
    UrlTraKey: (String, 0x0, 0x0, 0x0)
    pass

class OffScreenPoiItemData():
    Portrait: (Hash, 0x0, 0x0, 0x0)
    Region: (Hash, 0x0, 0x0, 0x0)
    RotatingFrame: (Hash, 0x0, 0x0, 0x0)
    RenderRegion: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x4c1fe46e(0x7319918a):
    Source: (Link, 0x0, 0x0, SequenceObjectSelector)
    DebugOverride: (List2, 0x0, Hash, 0x0)
    pass

class TroveElementData(ElementDataBase):
    InstanceData: (List2, 0x0, Embed, TroveInstanceData)
    pass

class TargeterDefinition():
    mFadeTimeStart: (F32, 0x0, 0x0, 0x0)
    mFadeTimeStartAlpha: (F32, 0x0, 0x0, 0x0)
    mFadeTimeEndAlpha: (F32, 0x0, 0x0, 0x0)
    mFadeTimeEnd: (F32, 0x0, 0x0, 0x0)
    mFadeBehavior: (Pointer, 0x0, 0x0, ITargeterFadeBehavior)
    pass

class FadeEventData(BaseEventData):
    mTargetAlpha: (F32, 0x0, 0x0, 0x0)
    mTimeToFade: (F32, 0x0, 0x0, 0x0)
    pass

class NeutralTimers():
    Scene: (Hash, 0x0, 0x0, 0x0)
    NeutralTimerStateManager: (Pointer, 0x0, 0x0, NeutralTimerStateManager)
    Timers: (List, 0x0, Embed, NeutralTimerData)
    mTimers: (Map, Hash, Embed, NeutralTimerData)
    mSceneName: (String, 0x0, 0x0, 0x0)
    mOptionalBinName: (String, 0x0, 0x0, 0x0)
    pass

class TftHudStreakUi():
    Scene: (Hash, 0x0, 0x0, 0x0)
    StreakIcons: (List, 0x5, Hash, 0x0)
    StreakHitTarget: (Hash, 0x0, 0x0, 0x0)
    StreakText: (Hash, 0x0, 0x0, 0x0)
    pass

class IScriptEvent():
    pass

class RespawnPointDataList():
    RespawnPoints: (List, 0x0, Embed, RespawnPointData)
    pass

class HudGearSelectionUiData():
    TimerEnabled: (Bool, 0x0, 0x0, 0x0)
    mGearSelectionTransitionIntro: (Embed, 0x0, 0x0, HudMenuTransitionData)
    TimerCountdownWarningStart: (F32, 0x0, 0x0, 0x0)
    SelectionButtonDelayTime: (F32, 0x0, 0x0, 0x0)
    mGearSelectionTransitionOutro: (Embed, 0x0, 0x0, HudMenuTransitionData)
    TimerCountdownDuration: (F32, 0x0, 0x0, 0x0)
    pass

class FacingAndMovementAngleParametricUpdater(IFloatParametricUpdater):
    pass

class BeforeTimeConstraintInfo(ListenerConstraintInfo):
    CutoffTimeSeconds: (F32, 0x0, 0x0, 0x0)
    pass

class 0x4d2d2581(IFxActionInstance):
    pass

class StoreListingData():
    mCatalogEntry: (Embed, 0x0, 0x0, CatalogEntry)
    MobileCatalogData: (Embed, 0x0, 0x0, MobileCatalogData)
    mIdentityInstance: (Embed, 0x0, 0x0, IdentityInstance)
    pass

class VfxAnimatedVector3f(VfxVector3fBase):
    Values: (List, 0x0, Vec3, 0x0)
    Values: (List2, 0x0, Vec3, 0x0)
    Times: (List, 0x0, F32, 0x0)
    Times: (List2, 0x0, F32, 0x0)
    0x7c9bcfd5: (List, 0x0, U32, 0x0)
    Modes: (List2, 0x0, U8, 0x0)
    ProbabilityTables: (List, 0x3, Pointer, VfxProbabilityTableData)
    pass

class LeagueRotatingFlavor():
    IndividualBannerOverrides: (List, 0x0, Embed, RotatingBanner)
    FlavorName: (String, 0x0, 0x0, 0x0)
    pass

class LevelPropSpawnerPoint(GameObject):
    pass

class DynamicMaterialTextureSwapDef():
    Enabled: (Bool, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    Options: (List, 0x0, Embed, DynamicMaterialTextureSwapOption)
    pass

class MaterialInstanceTextureDef():
    UncensoredTextures: (Map, Hash, String, 0x0)
    TexturePath: (String, 0x0, 0x0, 0x0)
    pass

class MinimapIconChangeOpacity(MinimapIconBehavior):
    TargetAlpha: (F32, 0x0, 0x0, 0x0)
    StartAlpha: (F32, 0x0, 0x0, 0x0)
    EaseType: (U8, 0x0, 0x0, 0x0)
    pass

class ObjectiveVotePanelData():
    ForButton: (Hash, 0x0, 0x0, 0x0)
    VoteHolderGroup: (Hash, 0x0, 0x0, 0x0)
    ObjectiveText: (Hash, 0x0, 0x0, 0x0)
    ForIcon: (Hash, 0x0, 0x0, 0x0)
    RejectButton: (Hash, 0x0, 0x0, 0x0)
    PendingIcon: (Hash, 0x0, 0x0, 0x0)
    VotesLayout: (Hash, 0x0, 0x0, 0x0)
    ObjectiveTextTraKey: (String, 0x0, 0x0, 0x0)
    PlayerRejectIcon: (Hash, 0x0, 0x0, 0x0)
    VfxPlayerReject: (Hash, 0x0, 0x0, 0x0)
    DisplayGroup: (Hash, 0x0, 0x0, 0x0)
    RejectIcon: (Hash, 0x0, 0x0, 0x0)
    PlayerForIcon: (Hash, 0x0, 0x0, 0x0)
    VfxPlayerFor: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x4e16b860():
    DescriptionText: (Hash, 0x0, 0x0, 0x0)
    HolderIcon: (Hash, 0x0, 0x0, 0x0)
    ProgressText: (Hash, 0x0, 0x0, 0x0)
    ExpandedHolderIcon: (Hash, 0x0, 0x0, 0x0)
    0x3a95996f: (List2, 0x0, Hash, 0x0)
    MissionGroup: (Hash, 0x0, 0x0, 0x0)
    0x51e9dd09: (List2, 0x0, Hash, 0x0)
    RewardText: (Hash, 0x0, 0x0, 0x0)
    ProgressIcons: (List2, 0x0, Embed, 0xb4517220)
    ManagedLayout: (Hash, 0x0, 0x0, 0x0)
    SecondaryMission: (Embed, 0x0, 0x0, 0xd19d72ee)
    CosmeticIcons: (List2, 0x0, Hash, 0x0)
    PrimaryMission: (Embed, 0x0, 0x0, 0xd19d72ee)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class ReconnectDialogViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    Meter: (Hash, 0x0, 0x0, 0x0)
    MobileOverride: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    pass

class 0x4e4e17(IBehaviorScriptBlock):
    Position: (Pointer, 0x0, 0x0, IVectorGet)
    pass

class PlayGameViewController(ViewController):
    pass

class 0x4e590cfd(ISequenceAction):
    DisableOnEnd: (Bool, 0x0, 0x0, 0x0)
    Element: (Hash, 0x0, 0x0, 0x0)
    EnableOnStart: (Bool, 0x0, 0x0, 0x0)
    pass

class MapCamera(MapPlaceable):
    MaxArmLength: (F32, 0x0, 0x0, 0x0)
    Yaw: (F32, 0x0, 0x0, 0x0)
    MinArmLength: (F32, 0x0, 0x0, 0x0)
    FieldOfView: (F32, 0x0, 0x0, 0x0)
    Pitch: (F32, 0x0, 0x0, 0x0)
    pass

class FollowTerrainHeightSolver(HeightSolverType):
    mMaxSlope: (F32, 0x0, 0x0, 0x0)
    mHeightOffset: (F32, 0x0, 0x0, 0x0)
    pass

class DeathRecapShowcaseSlotKdaData(DeathRecapShowcaseSlotData):
    BountyText: (Hash, 0x0, 0x0, 0x0)
    Bounty: (Embed, 0x0, 0x0, UiMetricUnitBounty)
    Kda: (Embed, 0x0, 0x0, UiMetricUnitKda)
    KdaText: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    BountyIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class UiElementRect():
    Size: (Vec2, 0x0, 0x0, 0x0)
    Position: (Vec2, 0x0, 0x0, 0x0)
    Width: (F32, 0x0, 0x0, 0x0)
    SourceResolutionHeight: (U16, 0x0, 0x0, 0x0)
    Height: (F32, 0x0, 0x0, 0x0)
    SourceResolutionWidth: (U16, 0x0, 0x0, 0x0)
    LeftTop: (Vec2, 0x0, 0x0, 0x0)
    pass

class ScriptPreloadModule():
    PreloadResourceName: (String, 0x0, 0x0, 0x0)
    pass

class HudSpellSlotResetFeedbackData():
    SpellResetFlashFadeDuration: (F32, 0x0, 0x0, 0x0)
    SpellResetFlashScaleDownDuration: (F32, 0x0, 0x0, 0x0)
    SpellResetScaleMultiplier: (F32, 0x0, 0x0, 0x0)
    pass

class FxActionScale(IFxAction):
    EasingType: (U8, 0x0, 0x0, 0x0)
    TargetScale: (F32, 0x0, 0x0, 0x0)
    TargetObject: (Embed, 0x0, 0x0, FxTarget)
    TargetObject: (Embed, 0x0, 0x0, FxObjectSelector)
    ResetOnEnd: (Bool, 0x0, 0x0, 0x0)
    pass

class IsSkinSpawnConditionData(VfxSpawnConditionData):
    mSkinId: (U32, 0x0, 0x0, 0x0)
    UseValidParentForChroma: (Bool, 0x0, 0x0, 0x0)
    pass

class JungleMonsterKillsTypeConstraintInfo(ListenerConstraintInfo):
    TeamToCheck: (U32, 0x0, 0x0, 0x0)
    pass

class 0x4f0aa8a0():
    TooltipText: (Pointer, 0x0, 0x0, 0x6ca3cfd)
    TooltipText: (String, 0x0, 0x0, 0x0)
    Element: (Hash, 0x0, 0x0, 0x0)
    ElementAnchor: (U8, 0x0, 0x0, 0x0)
    0xa620b98f: (List2, 0x0, Embed, 0xd5c5318a)
    TooltipAnchor: (U8, 0x0, 0x0, 0x0)
    TooltipLocalizedText: (String, 0x0, 0x0, 0x0)
    pass

class MaterialSwitchData():
    On: (Bool, 0x0, 0x0, 0x0)
    pass

class LoadingScreenClashTeam():
    TeamtagText: (Hash, 0x0, 0x0, 0x0)
    TeamLogoIcon: (Hash, 0x0, 0x0, 0x0)
    TeamNameText: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x4f4c4ffc():
    CharacterRecord: (Link, 0x0, 0x0, CharacterRecord)
    RandomWeight: (F32, 0x0, 0x0, 0x0)
    SkinId: (U32, 0x0, 0x0, 0x0)
    pass

class VfxShapeLegacy(IVfxShape):
    EmitRotationAngles: (List, 0x0, Embed, ValueFloat)
    EmitRotationAxes: (List, 0x0, Vec3, 0x0)
    EmitOffset: (Embed, 0x0, 0x0, ValueVector3)
    pass

class FxActionMoveToInstance(IFxActionInstance):
    pass

class 0x4f92775c(ILogicVector3Driver):
    pass

class 0x4f983e1d(0xd97f9bd3):
    MissileSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class EffectDesaturateElementData(EffectElementData):
    0x16252f7: (F32, 0x0, 0x0, 0x0)
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    0x57744c99: (F32, 0x0, 0x0, 0x0)
    MaximumSaturation: (F32, 0x0, 0x0, 0x0)
    MinimumSaturation: (F32, 0x0, 0x0, 0x0)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    pass

class MasteryBadgeData():
    mName: (Hash, 0x0, 0x0, 0x0)
    mVerticalOffset: (F32, 0x0, 0x0, 0x0)
    mMasteryLevel: (U32, 0x0, 0x0, 0x0)
    mSummonerIconId: (I32, 0x0, 0x0, 0x0)
    mRenderScale: (F32, 0x0, 0x0, 0x0)
    mParticleName: (String, 0x0, 0x0, 0x0)
    pass

class PlaybookAugmentItemData():
    Description: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    Name: (Hash, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x4fbb3f5d():
    HolderIcon: (Hash, 0x0, 0x0, 0x0)
    0x25a7b1dc: (Bool, 0x0, 0x0, 0x0)
    ExpandedHolderIcon: (Hash, 0x0, 0x0, 0x0)
    0x3a95996f: (List2, 0x0, Hash, 0x0)
    MissionGroup: (Hash, 0x0, 0x0, 0x0)
    0x51e9dd09: (List2, 0x0, Hash, 0x0)
    ProgressIcons: (List2, 0x0, Embed, 0xc0bb891d)
    ManagedLayout: (Hash, 0x0, 0x0, 0x0)
    SecondaryMission: (Embed, 0x0, 0x0, 0xece8d41b)
    CosmeticIcons: (List2, 0x0, Hash, 0x0)
    TrackerIconTemplate: (Embed, 0x0, 0x0, 0xd65c937c)
    PrimaryMission: (Embed, 0x0, 0x0, 0xece8d41b)
    pass

class BarracksConfig():
    MoveSpeedIncreaseIntervalSecs: (F32, 0x0, 0x0, 0x0)
    InitialSpawnTimeSecs: (F32, 0x0, 0x0, 0x0)
    GoldRadius: (F32, 0x0, 0x0, 0x0)
    MoveSpeedIncreaseMaxTimes: (I32, 0x0, 0x0, 0x0)
    ExpRadius: (F32, 0x0, 0x0, 0x0)
    MoveSpeedIncreaseIncrement: (I32, 0x0, 0x0, 0x0)
    UpgradesBeforeLateGameScaling: (I32, 0x0, 0x0, 0x0)
    MinionSpawnIntervalSecs: (F32, 0x0, 0x0, 0x0)
    WaveSpawnIntervalSecs: (F32, 0x0, 0x0, 0x0)
    UpgradeIntervalSecs: (F32, 0x0, 0x0, 0x0)
    Units: (List2, 0x0, Embed, BarracksMinionConfig)
    MoveSpeedIncreaseInitialDelaySecs: (F32, 0x0, 0x0, 0x0)
    pass

class SkinnedMeshHelper(SkinMeshDataProperties):
    pass

class 0x4fd53cef(0x2515101c):
    pass

class ChangeMovementSpeedCheat(Cheat):
    Target: (U32, 0x0, 0x0, 0x0)
    MoveDelta: (F32, 0x0, 0x0, 0x0)
    ResetToBaseSpeed: (Bool, 0x0, 0x0, 0x0)
    pass

class TftHudTunables():
    mStageData: (Embed, 0x0, 0x0, TftHudStageData)
    mCombatRecapData: (Embed, 0x0, 0x0, TftHudCombatRecapData)
    0x249fe588: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mMobileDownscaleData: (Embed, 0x0, 0x0, TftHudMobileDownscaleData)
    mScoreboardData: (Embed, 0x0, 0x0, TftHudScoreboardData)
    mAnnouncementData: (Embed, 0x0, 0x0, TftHudAnnouncementData)
    mUnitShopData: (Embed, 0x0, 0x0, TftHudUnitShopData)
    mZoomTransitionData: (Embed, 0x0, 0x0, 0xda3c6dc6)
    mNotificationsData: (Embed, 0x0, 0x0, TftHudNotificationsData)
    pass

class SpellDataValue():
    mName: (String, 0x0, 0x0, 0x0)
    mValues: (List, 0x7, F32, 0x0)
    pass

class UnitStatUiData():
    HoverTarget: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x502b0c72():
    BlurQuality: (U32, 0x0, 0x0, 0x0)
    SampleQuality: (U32, 0x0, 0x0, 0x0)
    SampleRadius: (F32, 0x0, 0x0, 0x0)
    BufferScale: (F32, 0x0, 0x0, 0x0)
    Power: (F32, 0x0, 0x0, 0x0)
    pass

class Hq(HqCommon):
    pass

class LevelControlScript(Rscript):
    Guid: (String, 0x0, 0x0, 0x0)
    Functions: (Map, Hash, Embed, ScriptFunction)
    CustomSequences: (Map, Hash, Link, ScriptSequence)
    Sequences: (Map, Hash, Embed, RootScriptSequence)
    Sequences: (Map, Hash, Embed, ScriptSequence)
    Sequences: (Map, U32, Embed, ScriptSequence)
    pass

class TftHudTraitUnitPortraitSection():
    UnitGridLink: (Hash, 0x0, 0x0, 0x0)
    UnitSlotRegions: (List, 0xc, Hash, 0x0)
    PortraitRegion: (Hash, 0x0, 0x0, 0x0)
    UnitInfoPortraitTooltipRegion: (Hash, 0x0, 0x0, 0x0)
    TraitTrackerPortraitTooltipRegion: (Hash, 0x0, 0x0, 0x0)
    PortraitTooltipRegion: (Hash, 0x0, 0x0, 0x0)
    HudTraitUnitSlotTemplate: (Embed, 0x0, 0x0, TftHudTraitUnitSlotData)
    UnitPortraitScene: (Hash, 0x0, 0x0, 0x0)
    HudTraitUnitSlotBorders: (Embed, 0x0, 0x0, TftHudTraitUnitSlotBorders)
    pass

class BlendableClipData(ClipBaseData):
    mMaskDataName: (Hash, 0x0, 0x0, 0x0)
    mEventDataList: (List, 0x0, Pointer, BaseEventData)
    mSyncGroupDataName: (Hash, 0x0, 0x0, 0x0)
    mTrackDataName: (Hash, 0x0, 0x0, 0x0)
    mEventDataMap: (Map, Hash, Pointer, BaseEventData)
    pass

class ITargeterFadeBehavior():
    pass

class FloatingInfoBarData():
    Scene: (Hash, 0x0, 0x0, 0x0)
    Anchor: (Hash, 0x0, 0x0, 0x0)
    ResurrectingAlpha: (F32, 0x0, 0x0, 0x0)
    ScriptedThresholdTypes: (Map, Hash, Hash, 0x0)
    UntargetableAlpha: (F32, 0x0, 0x0, 0x0)
    CameraMask: (U32, 0x0, 0x0, 0x0)
    pass

class 0x50714aa1():
    Trait: (Link, 0x0, 0x0, TftTraitData)
    Item: (Link, 0x0, 0x0, TftItemData)
    pass

class HasBuffNameSpawnConditions(IVfxSpawnConditions):
    mConditions: (List, 0x0, Embed, HasBuffSpawnConditionData)
    mDefaultVfxData: (Embed, 0x0, 0x0, VfxDefaultSpawnConditionData)
    pass

class IsLocalPlayerBoolDriver(ILogicBoolDriver):
    pass

class FxActionSfxInstance(IFxActionInstance):
    pass

class NotificationDialogOption():
    Scene: (Hash, 0x0, 0x0, 0x0)
    SceneTexts: (List2, 0x0, Hash, 0x0)
    SceneIcons: (List2, 0x0, Hash, 0x0)
    SceneButtons: (List2, 0x0, Hash, 0x0)
    pass

class AnnouncementsViewController(ViewController):
    MainBannerScene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    pass

class EventControlledSelectorPairData():
    StateEventId: (Hash, 0x0, 0x0, 0x0)
    ClipName: (Hash, 0x0, 0x0, 0x0)
    pass

class StringValueGet(DirectValueGet):
    Value: (String, 0x0, 0x0, 0x0)
    pass

class AbilityResourceBarTextData():
    ValueText: (Hash, 0x0, 0x0, 0x0)
    RegenText: (Hash, 0x0, 0x0, 0x0)
    pass

class CallOnMissileBounceOnMovementCompleteSpec(MissileBehaviorSpec):
    pass

class ClearTargetCooldownCheat(Cheat):
    mTarget: (U32, 0x0, 0x0, 0x0)
    pass

class TftCutsceneAnimClip(TftCutsceneClip):
    PostStartModifiers: (List2, 0x0, Pointer, TftAnimClipModifier)
    0x55eb4ac7: (Bool, 0x0, 0x0, 0x0)
    StartPaused: (Bool, 0x0, 0x0, 0x0)
    BlackboardWorldTransformName: (String, 0x0, 0x0, 0x0)
    ReportBone: (List2, 0x0, Embed, TftCutsceneReportBone)
    PauseOnEnd: (Bool, 0x0, 0x0, 0x0)
    StartSkipToTime: (F32, 0x0, 0x0, 0x0)
    BlackboardGameObjectName: (String, 0x0, 0x0, 0x0)
    SpeedRatio: (F32, 0x0, 0x0, 0x0)
    Blend: (Bool, 0x0, 0x0, 0x0)
    Loop: (Bool, 0x0, 0x0, 0x0)
    Animation: (String, 0x0, 0x0, 0x0)
    pass

class 0x50f553aa(0xb639bddc):
    CurrencyInfo: (Link, 0x0, 0x0, 0x37ccf49)
    pass

class ChallengeTitleData():
    CatalogEntry: (Embed, 0x0, 0x0, CatalogEntry)
    TitleAcquisitionRequirementTrakey: (String, 0x0, 0x0, 0x0)
    BackgroundImagePath: (String, 0x0, 0x0, 0x0)
    TitleAcquisitionTrakey: (String, 0x0, 0x0, 0x0)
    IconPath: (String, 0x0, 0x0, 0x0)
    TitleAcquisitionType: (U8, 0x0, 0x0, 0x0)
    LocalizedName: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    0x9b72d4a4: (U8, 0x0, 0x0, 0x0)
    0xc7f06b74: (String, 0x0, 0x0, 0x0)
    0xd37f09b9: (Bool, 0x0, 0x0, 0x0)
    pass

class ItemGridSection():
    mShowLabel: (Bool, 0x0, 0x0, 0x0)
    Mrows: (List, 0x0, Embed, ItemGridRow)
    mLabel: (String, 0x0, 0x0, 0x0)
    pass

class InvertFloatMaterialDriver(ILogicFloatDriver):
    Driver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class HermiteSplineInfo(ISplineInfo):
    mControlPoint1: (Vec3, 0x0, 0x0, 0x0)
    mControlPoint2: (Vec3, 0x0, 0x0, 0x0)
    pass

class DirectValueGet(RsValueGet):
    pass

class OptionItemSecondaryHotkeys1Column_Row():
    EventName: (String, 0x0, 0x0, 0x0)
    LabelTraKey: (String, 0x0, 0x0, 0x0)
    pass

class HudHealthBarData():
    ChampionProgressiveTickData: (Embed, 0x0, 0x0, HudHealthBarProgressiveTickData)
    BurstHealData: (Embed, 0x0, 0x0, HudHealthBarBurstHealData)
    BurstData: (Embed, 0x0, 0x0, HudHealthBarBurstData)
    ResurrectingAlpha: (F32, 0x0, 0x0, 0x0)
    DefenseIconData: (Embed, 0x0, 0x0, HudHealthBarDefenseIconData)
    TowerBurstData: (Embed, 0x0, 0x0, HudHealthBarBurstData)
    DefenseModifierData: (Embed, 0x0, 0x0, HudHealthBarDefenseModifierData)
    UntargetableAlpha: (F32, 0x0, 0x0, 0x0)
    FadeData: (Embed, 0x0, 0x0, HudHealthBarFadeData)
    pass

class FlexValueFloat():
    mValue: (Embed, 0x0, 0x0, ValueFloat)
    mValue: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    mFlexId: (U32, 0x0, 0x0, 0x0)
    mIsUsed: (Bool, 0x0, 0x0, 0x0)
    mTypeValue: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    mFlexValueId: (U32, 0x0, 0x0, 0x0)
    pass

class DefenseModifierIcons():
    mArmorShred: (Pointer, 0x0, 0x0, HealthbarImageInfo)
    mMagicShred: (Pointer, 0x0, 0x0, HealthbarImageInfo)
    pass

class IAugment():
    RootSpell: (Hash, 0x0, 0x0, 0x0)
    RootSpell: (Link, 0x0, 0x0, SpellObject)
    AugmentNameId: (String, 0x0, 0x0, 0x0)
    NameTra: (String, 0x0, 0x0, 0x0)
    Enabled: (Bool, 0x0, 0x0, 0x0)
    AugmentTooltipTra: (String, 0x0, 0x0, 0x0)
    AugmentSmallIconPath: (String, 0x0, 0x0, 0x0)
    mBuildTags: (U32, 0x0, 0x0, 0x0)
    AugmentDisplayTags: (List, 0x0, U32, 0x0)
    mAugmentTags: (U32, 0x0, 0x0, 0x0)
    AugmentLargeIconPath: (String, 0x0, 0x0, 0x0)
    DescriptionTra: (String, 0x0, 0x0, 0x0)
    pass

class 0x51c026b9(0xc10d4fdc):
    Waves: (List2, 0x0, Link, 0xe75aad84)
    pass

class HealthBarData():
    ExtraBars: (Pointer, 0x0, 0x0, HealthBarExtraBarsData)
    MaxHpPenaltyBar: (Hash, 0x0, 0x0, 0x0)
    MaxHpPenaltyDivider: (Hash, 0x0, 0x0, 0x0)
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    IncomingDamageBar: (Hash, 0x0, 0x0, 0x0)
    TextData: (Pointer, 0x0, 0x0, HealthBarTextData)
    Healthbar: (Embed, 0x0, 0x0, BarTypeMap)
    FadeData: (Pointer, 0x0, 0x0, HealthBarFadeData)
    TickStyle: (Pointer, 0x0, 0x0, HealthBarTickStyleBase)
    Frame: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxFloatOverLifeMaterialDriver(IVfxMaterialDriver):
    Frequency: (U8, 0x0, 0x0, 0x0)
    Graph: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    pass

class LuaPropertyDataString(LuaPropertyData):
    Value: (String, 0x0, 0x0, 0x0)
    pass

class 0x51db35d3():
    LockedHoverIcon: (Hash, 0x0, 0x0, 0x0)
    LockedHoverIcon: (String, 0x0, 0x0, 0x0)
    CompleteDefaultIcon: (Hash, 0x0, 0x0, 0x0)
    CompleteDefaultIcon: (String, 0x0, 0x0, 0x0)
    ClaimableHoverIcon: (Hash, 0x0, 0x0, 0x0)
    ClaimableHoverIcon: (String, 0x0, 0x0, 0x0)
    CompleteHoverIcon: (Hash, 0x0, 0x0, 0x0)
    CompleteHoverIcon: (String, 0x0, 0x0, 0x0)
    LockedDefaultIcon: (Hash, 0x0, 0x0, 0x0)
    LockedDefaultIcon: (String, 0x0, 0x0, 0x0)
    ClaimableDefaultIcon: (Hash, 0x0, 0x0, 0x0)
    ClaimableDefaultIcon: (String, 0x0, 0x0, 0x0)
    pass

class UiElementGroupSlider(UiElementGroup):
    pass

class 0x51f54b8e():
    pass

class TftHudTraitUnitSlotBorders():
    ItemSlotBorder: (Hash, 0x0, 0x0, 0x0)
    UnitSlotBorders: (Map, U8, Hash, 0x0)
    pass

class 0x5206ee88(0x6653bfda):
    0xf054015a: (Bool, 0x0, 0x0, 0x0)
    pass

class PlayerCardWidgetConfig():
    mCardType: (U8, 0x0, 0x0, 0x0)
    EnabledWidgets: (U32, 0x0, 0x0, 0x0)
    mTeamBased: (Bool, 0x0, 0x0, 0x0)
    pass

class MicroTicksPerStandardTickData():
    MinHealth: (F32, 0x0, 0x0, 0x0)
    MicroTicksBetween: (U32, 0x0, 0x0, 0x0)
    pass

class HealthbarBreakpoint():
    Offset: (Vec2, 0x0, 0x0, 0x0)
    IconSize: (Vec2, 0x0, 0x0, 0x0)
    BreakpointAmount: (F32, 0x0, 0x0, 0x0)
    Icon: (String, 0x0, 0x0, 0x0)
    pass

class IX3dShadingModel():
    ObjectPath: (Hash, 0x0, 0x0, 0x0)
    SharedTextures: (List, 0x0, Embed, X3dSharedTextureDef)
    SharedConstantBuffers: (List, 0x0, Link, X3dSharedConstantBufferDef)
    pass

class SetVarInPtp(IBlock):
    mValue: (F32, 0x0, 0x0, 0x0)
    mKey: (String, 0x0, 0x0, 0x0)
    pass

class 0x527e0256(IFxAction):
    Priority: (U8, 0x0, 0x0, 0x0)
    Material: (Link, 0x0, 0x0, StaticMaterialDef)
    pass

class MapDynamicPointLight(MapPointLightBase):
    Impact: (I32, 0x0, 0x0, 0x0)
    Impact: (U8, 0x0, 0x0, 0x0)
    IntensityScale: (F32, 0x0, 0x0, 0x0)
    Type: (U8, 0x0, 0x0, 0x0)
    VisibilityController: (Link, 0x0, 0x0, IMapVisibilityController)
    UpdaterType: (Link, 0x0, 0x0, MapLightUpdaterType)
    LightColor: (Vec4, 0x0, 0x0, 0x0)
    HdrScale: (F32, 0x0, 0x0, 0x0)
    Radius: (F32, 0x0, 0x0, 0x0)
    pass

class ChampSelectSummonerSpellData():
    SummonerLevelRequired: (I32, 0x0, 0x0, 0x0)
    Id: (I32, 0x0, 0x0, 0x0)
    GameModes: (List, 0x0, String, 0x0)
    IconPath: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    NameLocKey: (String, 0x0, 0x0, 0x0)
    DescriptionLocKey: (String, 0x0, 0x0, 0x0)
    pass

class LogicDriverViewEntry():
    Scene: (Hash, 0x0, 0x0, 0x0)
    0x40c7c429: (List2, 0x0, Pointer, 0x4f0aa8a0)
    ConditionalElementsEntries: (List, 0x0, Embed, LogicDriverConditionalElementsEntry)
    0x8d424715: (List2, 0x0, Pointer, 0x30aa7360)
    0x8f4f63ee: (List, 0x0, Embed, TextGimmeDataInstance)
    TransitionOnState: (Hash, 0x0, 0x0, 0x0)
    EnableCondition: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    TransitionOffState: (Hash, 0x0, 0x0, 0x0)
    pass

class UiRotationalStoreItemTileData():
    OwnedIcon: (Hash, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    Timer: (Pointer, 0x0, 0x0, TftEventTimer)
    Group: (Hash, 0x0, 0x0, 0x0)
    Vfx: (Hash, 0x0, 0x0, 0x0)
    PriceText: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionShopCloseCount(IContextualCondition):
    mShopCloseCount: (U32, 0x0, 0x0, 0x0)
    pass

class 0x52d07f9c(IScriptBlock, IBehaviorScriptBlock):
    Sequence: (Embed, 0x0, 0x0, ScriptBtInverter)
    pass

class ObjectiveVoteResultsViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    AltLayoutRegion: (Hash, 0x0, 0x0, 0x0)
    VoteTallyTemplate: (Embed, 0x0, 0x0, ObjectiveVotetTallyData)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    DisabledTimeBeforeSpawn: (F32, 0x0, 0x0, 0x0)
    BonusVotesForJungler: (U32, 0x0, 0x0, 0x0)
    ResultVerticalTransitionTime: (F32, 0x0, 0x0, 0x0)
    0x63b08b82: (Map, Hash, Hash, 0x0)
    TallyAutoCloseDelay: (F32, 0x0, 0x0, 0x0)
    ResultTransitionScene: (Hash, 0x0, 0x0, 0x0)
    0x77b37382: (Bool, 0x0, 0x0, 0x0)
    VotePanelTemplate: (Embed, 0x0, 0x0, ObjectiveVotePanelData)
    VoteResultTemplate: (Embed, 0x0, 0x0, ObjectiveVoteResultData)
    VoteAutoCloseDelay: (F32, 0x0, 0x0, 0x0)
    AutoActivateTimeBeforeSpawn: (F32, 0x0, 0x0, 0x0)
    ResultScene: (Hash, 0x0, 0x0, 0x0)
    NumVoters: (U32, 0x0, 0x0, 0x0)
    Layout: (Hash, 0x0, 0x0, 0x0)
    ConsensusVotesRequired: (U32, 0x0, 0x0, 0x0)
    ObjectiveCampInfo: (List, 0x0, Embed, ObjectiveCampDefinition)
    LayoutRegion: (Hash, 0x0, 0x0, 0x0)
    ObjectiveMonsterIcons: (Map, Hash, Embed, ObjectiveIconDefinition)
    FlippedOverride: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    pass

class SkinCharacterMetaDataProperties_SpawningSkinOffset():
    Offset: (I32, 0x0, 0x0, 0x0)
    Tag: (String, 0x0, 0x0, 0x0)
    pass

class AnchorSingle(AnchorBase):
    Anchor: (Vec2, 0x0, 0x0, 0x0)
    pass

class FxTarget():
    Type: (U32, 0x0, 0x0, 0x0)
    Index: (I32, 0x0, 0x0, 0x0)
    pass

class 0x534e00eb():
    BannerTexturePath: (String, 0x0, 0x0, 0x0)
    PityThreshold: (U32, 0x0, 0x0, 0x0)
    Id: (String, 0x0, 0x0, 0x0)
    ChaseTable: (Link, 0x0, 0x0, 0xb0617ced)
    ActivationDateTime: (String, 0x0, 0x0, 0x0)
    DeactivationDateTime: (String, 0x0, 0x0, 0x0)
    BannerCurrencyId: (String, 0x0, 0x0, 0x0)
    NameTraKey: (String, 0x0, 0x0, 0x0)
    PityCounterId: (String, 0x0, 0x0, 0x0)
    RootTable: (Link, 0x0, 0x0, 0xb0617ced)
    DescriptionTraKey: (String, 0x0, 0x0, 0x0)
    MythicTokenOfferId: (String, 0x0, 0x0, 0x0)
    pass

class IRsValueGet():
    pass

class IntCast(ScriptTableGet, IIntGet):
    pass

class ParametricMovement(MissileMovementSpec):
    ParametricMovementType: (Pointer, 0x0, 0x0, ParametricMovementType)
    MovementEntries: (List, 0x0, Embed, ParametricMovementEntry)
    pass

class StatFilterDefinition():
    MatchingCategories: (List, 0x0, Hash, 0x0)
    ButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxProbabilityTableData():
    KeyTimes: (List, 0x0, F32, 0x0)
    SingleValue: (F32, 0x0, 0x0, 0x0)
    KeyValues: (List, 0x0, F32, 0x0)
    pass

class RadialMenuHoverButtonDefinition(RadialMenuButtonDefinitionBase):
    HoverIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class LossOfControlIndicator():
    mOffset: (Vec2, 0x0, 0x0, 0x0)
    mTemplate: (Link, 0x0, 0x0, LossOfControlTemplate)
    pass

class MissileTriggeredActionSpec():
    pass

class 0x53cfbd4c(ISequenceActionInstance):
    pass

class 0x53de4f74():
    pass

class MaterialParameterData():
    Type: (U8, 0x0, 0x0, 0x0)
    DefaultValue: (Vec4, 0x0, 0x0, 0x0)
    pass

class 0x53dfc5b5(0xf9e5b8b9):
    Subtract: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class MapTransitionPositions(MapGraphicsFeature):
    PositionLocators: (List2, 0x0, Hash, 0x0)
    pass

class 0x54019489(0x38749c0a):
    ReverseScale: (Bool, 0x0, 0x0, 0x0)
    MaxAddedSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class PassThroughParamsTable(ScriptTable, RsTable):
    pass

class ParticleEventData(BaseEventData):
    mIsDetachable: (Bool, 0x0, 0x0, 0x0)
    mEffectName: (String, 0x0, 0x0, 0x0)
    mParticleEventDataPairList: (List, 0x0, Embed, ParticleEventDataPair)
    mIsKillEvent: (Bool, 0x0, 0x0, 0x0)
    Scale: (F32, 0x0, 0x0, 0x0)
    mScalePlaySpeedWithAnimation: (Bool, 0x0, 0x0, 0x0)
    mTargetBoneName: (String, 0x0, 0x0, 0x0)
    mEnemyEffectKey: (Hash, 0x0, 0x0, 0x0)
    SkipIfPastEndFrame: (Bool, 0x0, 0x0, 0x0)
    mIsPoseAfterimage: (Bool, 0x0, 0x0, 0x0)
    mIsLoop: (Bool, 0x0, 0x0, 0x0)
    mBoneName: (String, 0x0, 0x0, 0x0)
    mEffectKey: (Hash, 0x0, 0x0, 0x0)
    pass

class CharacterQuestListConfig(IGameModeConfig):
    CharacterQuestDefinitionsList: (List2, 0x0, Pointer, CharacterQuestDefinitionsData)
    CharacterQuestList: (List2, 0x0, Pointer, 0xe2ff8b22)
    0x5f1426cf: (Bool, 0x0, 0x0, 0x0)
    0x702d99a3: (I32, 0x0, 0x0, 0x0)
    pass

class RelicList():
    mRelicSubLists: (List, 0x0, Embed, RelicSubList)
    mRelicSubLists: (List, 0x0, Link, RelicSubList)
    pass

class EpicMinionFilter(IStatStoneLogicDriver):
    pass

class FxLocationObject(IFxLocation):
    Object: (Embed, 0x0, 0x0, FxTarget)
    Object: (Embed, 0x0, 0x0, FxObjectSelector)
    pass

class TftDragData():
    mDragSoundEvent: (String, 0x0, 0x0, 0x0)
    mTapToDrag: (Bool, 0x0, 0x0, 0x0)
    mDragReleaseDuration: (F32, 0x0, 0x0, 0x0)
    mDragPickupHeight: (F32, 0x0, 0x0, 0x0)
    mClickDistanceDiv: (F32, 0x0, 0x0, 0x0)
    mDropSoundEvent: (String, 0x0, 0x0, 0x0)
    mDragOvershootHeight: (F32, 0x0, 0x0, 0x0)
    mClickDistanceMul: (F32, 0x0, 0x0, 0x0)
    mDragOvershootDuration: (F32, 0x0, 0x0, 0x0)
    mDragPickupDuration: (F32, 0x0, 0x0, 0x0)
    mDragBlendTime: (F32, 0x0, 0x0, 0x0)
    mHoldToDrag: (Bool, 0x0, 0x0, 0x0)
    mClickTimeMul: (F32, 0x0, 0x0, 0x0)
    mClickDistanceExp: (F32, 0x0, 0x0, 0x0)
    mHoldToHover: (Bool, 0x0, 0x0, 0x0)
    mGroupProperties: (List, 0x0, Embed, TftDragDropGroupProperty)
    pass

class TrackMouseMovement(MissileMovementSpec):
    mProjectTargetToCastRange: (Bool, 0x0, 0x0, 0x0)
    mSpeed: (F32, 0x0, 0x0, 0x0)
    mAntiLagDelay: (F32, 0x0, 0x0, 0x0)
    mUseGroundHeightAtTarget: (Bool, 0x0, 0x0, 0x0)
    mInferDirectionFromFacingIfNeeded: (Bool, 0x0, 0x0, 0x0)
    mInitialSpeed: (F32, 0x0, 0x0, 0x0)
    mAcceleration: (F32, 0x0, 0x0, 0x0)
    mTurnRadiusByLevel: (List, 0x7, F32, 0x0)
    AddBonusAttackRangeToCastRange: (Bool, 0x0, 0x0, 0x0)
    mTurnRadius: (F32, 0x0, 0x0, 0x0)
    mMinSpeed: (F32, 0x0, 0x0, 0x0)
    mMaxSpeed: (F32, 0x0, 0x0, 0x0)
    mAntiLagTrackingDelay: (F32, 0x0, 0x0, 0x0)
    pass

class WorldVarsTable(ScriptTable):
    pass

class ContextualConditionHasGold(IContextualCondition):
    mGold: (F32, 0x0, 0x0, 0x0)
    pass

class IconData():
    IconsForCurrency: (Map, U8, Embed, IconLink)
    BaseIcon: (Embed, 0x0, 0x0, IconLink)
    pass

class UpdaterResourceData():
    mUpdaterDataList: (List, 0x0, Embed, UpdaterData)
    mVersion: (U32, 0x0, 0x0, 0x0)
    pass

class RigResource():
    mAssetName: (String, 0x0, 0x0, 0x0)
    mName: (String, 0x0, 0x0, 0x0)
    mShaderJointList: (List, 0x0, U16, 0x0)
    mJointList: (List, 0x0, Embed, Joint)
    mFlags: (U16, 0x0, 0x0, 0x0)
    pass

class OptionItemSecondaryHotkeys1Column_Header():
    Column0LabelTraKey: (String, 0x0, 0x0, 0x0)
    Column1LabelTraKey: (String, 0x0, 0x0, 0x0)
    pass

class 0x554b7346(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    FullDescriptionTraKey: (String, 0x0, 0x0, 0x0)
    MaxItemSlot: (U32, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    RecipeHintTraKey: (String, 0x0, 0x0, 0x0)
    MobileOverrideBinName: (String, 0x0, 0x0, 0x0)
    ItemSpace: (Hash, 0x0, 0x0, 0x0)
    BaseBinName: (String, 0x0, 0x0, 0x0)
    ItemSlotData: (Embed, 0x0, 0x0, 0xc0fd6b7b)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class FxActionSfxAttach(FxActionSfxBase):
    Location: (Pointer, 0x0, 0x0, IFxLocation)
    pass

class OptionTemplateHotkeysLabel():
    Label: (Hash, 0x0, 0x0, 0x0)
    pass

class TftCustomAnnouncementData():
    Subtitle: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    Player: (Hash, 0x0, 0x0, 0x0)
    Title: (Hash, 0x0, 0x0, 0x0)
    0xbf98d308: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class SmartPingData(IGameModeConfig):
    0x1e98bb0e: (Map, U8, U8, 0x0)
    0x5aa830e8: (F32, 0x0, 0x0, 0x0)
    0xaa8eb438: (F32, 0x0, 0x0, 0x0)
    pass

class TftHudExpBar():
    0x234f4a0c: (String, 0x0, 0x0, 0x0)
    ExpScene: (Hash, 0x0, 0x0, 0x0)
    ExpBar: (Hash, 0x0, 0x0, 0x0)
    LinearOverlays: (List, 0x3, Hash, 0x0)
    RadialExpBar: (Hash, 0x0, 0x0, 0x0)
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    ValueText: (Hash, 0x0, 0x0, 0x0)
    ExpBarDivider: (Hash, 0x0, 0x0, 0x0)
    RadialOverlays: (List, 0x3, Hash, 0x0)
    RadialBackdrop: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x55d03617(IFxAction):
    Position: (Embed, 0x0, 0x0, FxTransform)
    Location: (Pointer, 0x0, 0x0, IFxLocation)
    pass

class ProgressTrack():
    Id: (String, 0x0, 0x0, 0x0)
    CounterDefinitions: (List, 0x0, Link, CounterDefinition)
    PremiumEntitlementId: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    ProductId: (String, 0x0, 0x0, 0x0)
    MilestoneDefinitions: (List, 0x0, Link, MilestoneDefinition)
    Repeat: (Embed, 0x0, 0x0, GroupRepeat)
    pass

class MaterialOverrideCallbackDynamicMaterial():
    pass

class UiElementAsset(UiElement):
    pass

class 0x55f603e4(0x48eb8d47):
    OrEqualTo: (Bool, 0x0, 0x0, 0x0)
    GreaterThan: (I32, 0x0, 0x0, 0x0)
    pass

class 0x55f6bf86():
    EffectKey: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionMarkerName(IContextualCondition):
    mMarkerNames: (List, 0x0, String, 0x0)
    pass

class SourceTypeFilter(IStatStoneLogicDriver):
    MinionsAreValid: (Bool, 0x0, 0x0, 0x0)
    ChampionsAreValid: (Bool, 0x0, 0x0, 0x0)
    TurretsAreValid: (Bool, 0x0, 0x0, 0x0)
    pass

class UiElementGroupSliderSoundEvents():
    OnBarClickedEvent: (String, 0x0, 0x0, 0x0)
    OnDragEndEvent: (String, 0x0, 0x0, 0x0)
    OnDragStartEvent: (String, 0x0, 0x0, 0x0)
    pass

class LevelScriptOnUpdate(ILevelScriptEvent):
    pass

class 0x563a9d91(IFxAction):
    EventName: (String, 0x0, 0x0, 0x0)
    pass

class TurnAngleParametricUpdater(IFloatParametricUpdater):
    pass

class LooseUiTextureDataBase(IUiTextureDataProvider):
    TextureName: (String, 0x0, 0x0, 0x0)
    pass

class RoleSelfConstraintInfo(ListenerConstraintInfo):
    RequiredRole: (U32, 0x0, 0x0, 0x0)
    pass

class TftSkinCharacterDataProperties(SkinCharacterDataProperties):
    pass

class ContextualConditionCharacterLevel(IContextualCondition):
    mCompareOp: (U8, 0x0, 0x0, 0x0)
    mCharacterLevel: (U8, 0x0, 0x0, 0x0)
    pass

class ChampionRuneRecommendationsContext():
    pass

class ToggleAfkDetectionCheat(Cheat):
    pass

class BlendingSwitchMaterialDriver(SwitchMaterialDriver):
    mOverrideBlendTimes: (List, 0x0, F32, 0x0)
    mBlendTime: (F32, 0x0, 0x0, 0x0)
    pass

class VfxPrimitiveArbitraryTrail(VfxPrimitiveTrailBase):
    pass

class CssStyle():
    FontSize: (Option, 0x0, U32, 0x0)
    Color: (Option, 0x0, Color, 0x0)
    Italics: (Option, 0x0, Bool, 0x0)
    Bold: (Option, 0x0, Bool, 0x0)
    Underline: (Option, 0x0, Bool, 0x0)
    pass

class HasUnitTagsCastRequirement(ICastRequirement):
    mUnitTags: (Embed, 0x0, 0x0, ObjectTags)
    pass

class 0x5727ed42(IScriptCondition):
    Key: (Pointer, 0x0, 0x0, IScriptValueGet)
    CustomTable: (Embed, 0x0, 0x0, CustomTableGet)
    pass

class BehaviorLevelController(ILevelController, BaseLevelController):
    LevelBehaviors: (Map, Hash, Pointer, ILevelBehavior)
    LevelBehaviors: (Map, U32, Pointer, ILevelBehavior)
    pass

class BuffCounterDynamicMaterialFloatDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    Spell: (Hash, 0x0, 0x0, 0x0)
    mScriptName: (String, 0x0, 0x0, 0x0)
    pass

class TftPassData():
    MinimumVersionForContent: (String, 0x0, 0x0, 0x0)
    0x36d50b23: (U64, 0x0, 0x0, 0x0)
    Id: (String, 0x0, 0x0, 0x0)
    0x39095266: (String, 0x0, 0x0, 0x0)
    0x60c41330: (String, 0x0, 0x0, 0x0)
    PremiumEntitlementId: (String, 0x0, 0x0, 0x0)
    InternalName: (String, 0x0, 0x0, 0x0)
    AssetListId: (String, 0x0, 0x0, 0x0)
    PremiumTitleTraKey: (String, 0x0, 0x0, 0x0)
    ProgressionId: (String, 0x0, 0x0, 0x0)
    0x890c336a: (String, 0x0, 0x0, 0x0)
    PassItemId: (U32, 0x0, 0x0, 0x0)
    ProductId: (String, 0x0, 0x0, 0x0)
    TitleTrakey: (String, 0x0, 0x0, 0x0)
    Levels: (List2, 0x0, Pointer, TftPassRewardBase)
    TftPassLevels: (List2, 0x0, Embed, TftPassLevel)
    DescriptionTraKey: (String, 0x0, 0x0, 0x0)
    0xc119fe2a: (U64, 0x0, 0x0, 0x0)
    CounterId: (String, 0x0, 0x0, 0x0)
    pass

class OverrideAttackTimeData():
    mTotalAttackTimeSecs: (Pointer, 0x0, 0x0, IGameCalculation)
    mTotalAttackTimeSecs: (Pointer, 0x0, 0x0, ISpellCalculation)
    SetOverrideAttackDelay: (Bool, 0x0, 0x0, 0x0)
    mCastTimePercent: (F32, 0x0, 0x0, 0x0)
    pass

class ShopCommon(BuildingClient):
    pass

class UiMetricKda(UiMetricTypeI, UiMetricTypeSimpleI):
    KdaText: (Hash, 0x0, 0x0, 0x0)
    KdaIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class ConstantWaveBehavior(IMinionWaveBehavior):
    SpawnCount: (I32, 0x0, 0x0, 0x0)
    pass

class EventCardDefinition():
    Description: (String, 0x0, 0x0, 0x0)
    TitleForSameTeam: (String, 0x0, 0x0, 0x0)
    DescriptionForSameTeam: (String, 0x0, 0x0, 0x0)
    DescriptionForOtherTeam: (String, 0x0, 0x0, 0x0)
    TitleForOtherTeam: (String, 0x0, 0x0, 0x0)
    Title: (String, 0x0, 0x0, 0x0)
    EventIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class PlayerStatsPanelViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    FlippedMinimapOverride: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    pass

class StatByCoefficientCalculationPart(IGameCalculationPartWithStats, ISpellCalculationPartWithStats, ISpellCalculationPart):
    mCoefficient: (F32, 0x0, 0x0, 0x0)
    mStat: (U8, 0x0, 0x0, 0x0)
    mStatFormula: (U8, 0x0, 0x0, 0x0)
    pass

class HudEncounterData():
    mProgressBarEaseRate: (F32, 0x0, 0x0, 0x0)
    mSceneTransition: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mUnitBarFadeSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class 0x5835d0f2(IFxActionInstance):
    pass

class TftGameStartSequenceScene(TftGameStartSequenceSimpleObject):
    UiScene: (Hash, 0x0, 0x0, 0x0)
    pass

class UpgradeItemSelectionViewController(ItemSelectionBaseViewController):
    pass

class 0x58622c03(BuffEffect):
    mBlockedSpells: (U32, 0x0, 0x0, 0x0)
    pass

class ContextualConditionNeutralMinionMapSide(IContextualCondition):
    mTeamCompareOp: (U8, 0x0, 0x0, 0x0)
    pass

class AugmentFallbackPool():
    AugmentPool: (List2, 0x0, Link, AugmentData)
    Rarity: (U8, 0x0, 0x0, 0x0)
    pass

class MapVisibilityFlagDefinitions():
    FlagDefinitions: (List, 0x0, Embed, MapVisibilityFlagDefinition)
    FilterMaterialLoadingByVisibility: (Bool, 0x0, 0x0, 0x0)
    0x70b70215: (Bool, 0x0, 0x0, 0x0)
    FlagRange: (Embed, 0x0, 0x0, MapVisibilityFlagRange)
    SelectRandomVisibilityFlagForMap: (Bool, 0x0, 0x0, 0x0)
    pass

class UiMetricGameTime(UiMetricTypeI):
    TimeText: (Hash, 0x0, 0x0, 0x0)
    pass

class TransitionToData():
    mTransitionAnimId: (U32, 0x0, 0x0, 0x0)
    mToAnimId: (U32, 0x0, 0x0, 0x0)
    pass

class 0x58c2dd4f(0x4664ae0a):
    Material: (Link, 0x0, 0x0, IMaterialDef)
    pass

class TftUnitProperties():
    UnitPropertyDefinitions: (Map, Hash, Embed, TftUnitPropertyDefinition)
    pass

class PlayerPerksViewController(PlayerStatsPanelViewController, ViewController):
    PanelBgAltTop: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    PanelBg: (Hash, 0x0, 0x0, 0x0)
    PanelBgAltSide: (Hash, 0x0, 0x0, 0x0)
    ObjectName: (String, 0x0, 0x0, 0x0)
    PlayerPerksStats: (Embed, 0x0, 0x0, UiPerksStats)
    pass

class ViewControllerFilter_Mobile(ViewControllerFilterI):
    pass

class HudRadialWheelData():
    mRadialWheelButtonTransitionOutro: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mRadialWheelUiTransitionData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    ActivateWheelDelayTime: (F32, 0x0, 0x0, 0x0)
    mRadialWheelButtonTransitionIntro: (Embed, 0x0, 0x0, HudMenuTransitionData)
    pass

class TftTrovesCelebrationViewControllerV2(ViewController):
    0x104fe04e: (Link, 0x0, 0x0, SequenceObjectSelector)
    0x108492b7: (String, 0x0, 0x0, 0x0)
    DefaultStandardItemRarityTexturePath: (String, 0x0, 0x0, 0x0)
    SingleStandardQuantityText: (Hash, 0x0, 0x0, 0x0)
    StandardItemStarLevelTexturePaths: (List, 0x3, String, 0x0)
    0x27edf69a: (List2, 0x0, Link, SequenceObjectSelector)
    0x2e05d5a9: (Link, 0x0, 0x0, SequenceObjectSelector)
    DefaultStandardItemThumbnailTexturePath: (String, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    0x3fdcfd10: (Map, String, Embed, 0xbaf9ac75)
    0x52fa1831: (Link, 0x0, 0x0, SequenceObjectSelector)
    0x58134905: (Link, 0x0, 0x0, SequenceObjectSelector)
    0x5db7f820: (Map, String, Embed, 0x9ab8b8e6)
    0x629d7fe5: (Link, 0x0, 0x0, SequenceObjectSelector)
    DefaultTheme: (Link, 0x0, 0x0, TftTrovesCelebrationThemeData)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    SingleStandardItemLegendaryVfx: (Hash, 0x0, 0x0, 0x0)
    SingleStandardItemVfx: (Hash, 0x0, 0x0, 0x0)
    StandardItemRarityTexturePaths: (Map, U32, String, 0x0)
    0x783a2d93: (Hash, 0x0, 0x0, 0x0)
    0x7b14669a: (Hash, 0x0, 0x0, 0x0)
    0x7e6bb126: (Link, 0x0, 0x0, SequenceObjectSelector)
    StandardContentLayout: (Hash, 0x0, 0x0, 0x0)
    0x880040f3: (Link, 0x0, 0x0, SequenceObjectSelector)
    VignetteTitle: (Hash, 0x0, 0x0, 0x0)
    ContinueButton: (Hash, 0x0, 0x0, 0x0)
    StandardItemTemplate: (Embed, 0x0, 0x0, 0x8190bc9f)
    SingleStandardCurrencyVfx: (Hash, 0x0, 0x0, 0x0)
    0xa3021f81: (Link, 0x0, 0x0, SequenceObjectSelector)
    0xa7b45c64: (Link, 0x0, 0x0, SequenceObjectSelector)
    0xaad46f66: (Hash, 0x0, 0x0, 0x0)
    CommonScene: (Hash, 0x0, 0x0, 0x0)
    DefaultStandardItemStarLevelTexturePath: (String, 0x0, 0x0, 0x0)
    0xc1d80535: (Link, 0x0, 0x0, SequenceObjectSelector)
    0xc91cc065: (Link, 0x0, 0x0, SequenceObjectSelector)
    0xd7ce36cb: (Link, 0x0, 0x0, SequenceObjectSelector)
    0xdf4d96db: (Link, 0x0, 0x0, Sequence)
    ParentScene: (Hash, 0x0, 0x0, 0x0)
    0xeed1cb06: (Link, 0x0, 0x0, SequenceObjectSelector)
    SingleStandardItemText: (Hash, 0x0, 0x0, 0x0)
    0xf9787c06: (Map, String, Hash, 0x0)
    0xf9ae2168: (Link, 0x0, 0x0, SequenceObjectSelector)
    VignetteTitleTraKey: (String, 0x0, 0x0, 0x0)
    pass

class MapParticle(MapPlaceable):
    TextureOverride: (Pointer, 0x0, 0x0, 0x3e265091)
    AllDimensions: (Bool, 0x0, 0x0, 0x0)
    StartDisabled: (Bool, 0x0, 0x0, 0x0)
    System: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    VisibilityController: (Link, 0x0, 0x0, IMapVisibilityController)
    EyeCandy: (Bool, 0x0, 0x0, 0x0)
    Transitional: (Bool, 0x0, 0x0, 0x0)
    Quality: (I32, 0x0, 0x0, 0x0)
    ColorModulate: (Vec4, 0x0, 0x0, 0x0)
    GroupName: (String, 0x0, 0x0, 0x0)
    VisibilityMode: (U32, 0x0, 0x0, 0x0)
    pass

class RecSpellRankUpInfoList():
    RecSpellRankUpInfos: (List, 0x0, Embed, RecSpellRankUpInfo)
    pass

class MaterialInstanceParamDef():
    Value: (Vec4, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class 0x597c4a9d(IFxAction):
    Target: (Embed, 0x0, 0x0, FxTarget)
    Target: (Embed, 0x0, 0x0, FxObjectSelector)
    ResetOnEnd: (Bool, 0x0, 0x0, 0x0)
    Overrides: (Link, 0x0, 0x0, CharacterOverrides)
    pass

class MapPlaceable(MapPlaceableBase):
    Name: (Hash, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    mVisibilityFlags: (U8, 0x0, 0x0, 0x0)
    Transform: (Mtx44, 0x0, 0x0, 0x0)
    pass

class TftCutscenePosVfxClip(TftCutsceneVfxClip):
    HideWhenNotViewed: (Bool, 0x0, 0x0, 0x0)
    0x6230e799: (String, 0x0, 0x0, 0x0)
    0x82ea4a57: (Bool, 0x0, 0x0, 0x0)
    pass

class UiPerksStats():
    Stats: (List, 0x0, Embed, UiPerksStatData)
    pass

class AnnouncementDefinition():
    ChatAnnouncementOnly: (Bool, 0x0, 0x0, 0x0)
    CommonElements: (Hash, 0x0, 0x0, 0x0)
    MakeLowerPriorityEventsObsolete: (Bool, 0x0, 0x0, 0x0)
    AlliedElements: (Hash, 0x0, 0x0, 0x0)
    CanBeMadeObsolete: (Bool, 0x0, 0x0, 0x0)
    TextKey: (String, 0x0, 0x0, 0x0)
    SoundKey: (String, 0x0, 0x0, 0x0)
    ChatMessageKey: (String, 0x0, 0x0, 0x0)
    MutatorOverrides: (Map, String, Embed, AnnouncementDefinitionData)
    DefaultData: (Embed, 0x0, 0x0, AnnouncementDefinitionData)
    Priority: (U16, 0x0, 0x0, 0x0)
    SpectatorSoundKey: (String, 0x0, 0x0, 0x0)
    Style: (Link, 0x0, 0x0, AnnouncementStyleBasic)
    EnemyElements: (Hash, 0x0, 0x0, 0x0)
    pass

class TftBattlepassSelectedRewardBannerUiData():
    LockGroup: (Hash, 0x0, 0x0, 0x0)
    ClaimReadyGroup: (Hash, 0x0, 0x0, 0x0)
    LockText: (Hash, 0x0, 0x0, 0x0)
    ClaimText: (Hash, 0x0, 0x0, 0x0)
    pass

class UiElementText(UiElement):
    pass

class TftUnitPropertyOverride():
    Value: (Pointer, 0x0, 0x0, TftUnitPropertyValue)
    Definition: (Link, 0x0, 0x0, TftUnitPropertyDefinition)
    pass

class LobbyReadyCheck():
    TimerText: (Hash, 0x0, 0x0, 0x0)
    DefaultQueueIdTitleTraKey: (String, 0x0, 0x0, 0x0)
    MatchFoundText: (Hash, 0x0, 0x0, 0x0)
    AcceptedVfx: (Hash, 0x0, 0x0, 0x0)
    MatchInfoText: (Hash, 0x0, 0x0, 0x0)
    DeclineButton: (Hash, 0x0, 0x0, 0x0)
    TimerVfx: (Hash, 0x0, 0x0, 0x0)
    QueueIdTitleTraKeys: (Map, I64, String, 0x0)
    AcceptButton: (Hash, 0x0, 0x0, 0x0)
    SceneHandle: (Hash, 0x0, 0x0, 0x0)
    pass

class ItemRecOverrideRange():
    Items: (List, 0x0, Hash, 0x0)
    MaxCompletedItems: (U32, 0x0, 0x0, 0x0)
    pass

class SelectorClipPairData():
    mClipId: (U32, 0x0, 0x0, 0x0)
    mProbability: (F32, 0x0, 0x0, 0x0)
    pass

class HomeViewPromoBanner():
    Scene: (Hash, 0x0, 0x0, 0x0)
    FadeEasing: (U8, 0x0, 0x0, 0x0)
    SceneViewPane: (Hash, 0x0, 0x0, 0x0)
    PaginationEasing: (U8, 0x0, 0x0, 0x0)
    0x557095fe: (Embed, 0x0, 0x0, 0x42dcedbc)
    Elements: (List2, 0x0, Embed, PromoBannerElement)
    Elements: (List2, 0x0, Pointer, ElementDataBase)
    0x7099ea0e: (U8, 0x0, 0x0, 0x0)
    FadeDuration: (F32, 0x0, 0x0, 0x0)
    0x8190d5ac: (F32, 0x0, 0x0, 0x0)
    0x82ee166: (Hash, 0x0, 0x0, 0x0)
    0xa3e52539: (U8, 0x0, 0x0, 0x0)
    0xa658987c: (Map, U32, Embed, 0xc3737f3e)
    0xa81cb29a: (Hash, 0x0, 0x0, 0x0)
    Layout: (Hash, 0x0, 0x0, 0x0)
    0xd81ce014: (F32, 0x0, 0x0, 0x0)
    0xe603ebc2: (F32, 0x0, 0x0, 0x0)
    0xeb49eb3f: (F32, 0x0, 0x0, 0x0)
    pass

class InputEventBool(InputEventBase):
    RepeatRate: (F32, 0x0, 0x0, 0x0)
    Sources: (List, 0x0, Pointer, IInputSourceBool)
    pass

class ContextualConditionCastTarget(IContextualCondition):
    IsAlly: (Bool, 0x0, 0x0, 0x0)
    IsSelf: (Bool, 0x0, 0x0, 0x0)
    ConditionRelationship: (U32, 0x0, 0x0, 0x0)
    IsEnemy: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x5a6e59eb(IScriptBlock, IBehaviorScriptBlock):
    pass

class PerkReplacement():
    mReplaceWith: (Hash, 0x0, 0x0, 0x0)
    mReplaceWith: (Link, 0x0, 0x0, Perk)
    mReplaceTarget: (Hash, 0x0, 0x0, 0x0)
    mReplaceTarget: (Link, 0x0, 0x0, Perk)
    pass

class LevelPropGameObject(LevelPropGameObjectCommon):
    pass

class 0x5a8ba29d():
    pass

class SpawnSkinUpgrade(ISkinUpgradeObject):
    mBuffName: (String, 0x0, 0x0, 0x0)
    mVfxName: (String, 0x0, 0x0, 0x0)
    pass

class StatEfficiencyPerHundred(IGameCalculationPart):
    mStat: (U8, 0x0, 0x0, 0x0)
    mStatFormula: (U8, 0x0, 0x0, 0x0)
    StatType: (U8, 0x0, 0x0, 0x0)
    OutputType: (U8, 0x0, 0x0, 0x0)
    UseNewStats: (Bool, 0x0, 0x0, 0x0)
    0xae2f576: (F32, 0x0, 0x0, 0x0)
    mDataValue: (Hash, 0x0, 0x0, 0x0)
    mBonusStatForEfficiency: (F32, 0x0, 0x0, 0x0)
    pass

class PlatformSpellInfo():
    mGameModes: (List, 0x0, String, 0x0)
    mAvatarLevelRequired: (I32, 0x0, 0x0, 0x0)
    mSpellId: (I32, 0x0, 0x0, 0x0)
    mPlatformEnabled: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x5ad4a256():
    ClickRegion: (Hash, 0x0, 0x0, 0x0)
    IconHover: (Hash, 0x0, 0x0, 0x0)
    IconLeft: (Hash, 0x0, 0x0, 0x0)
    SlotArea: (Hash, 0x0, 0x0, 0x0)
    MessageTitleText: (Hash, 0x0, 0x0, 0x0)
    MessageBodyText: (Hash, 0x0, 0x0, 0x0)
    BackgroundDefault: (Hash, 0x0, 0x0, 0x0)
    IconDefault: (Hash, 0x0, 0x0, 0x0)
    IconRight: (Hash, 0x0, 0x0, 0x0)
    BackgroundHover: (Hash, 0x0, 0x0, 0x0)
    pass

class OptionItemSliderGraphicsQuality(OptionItemSlider):
    pass

class PerkConfig():
    mSchemaVersion: (U32, 0x0, 0x0, 0x0)
    mPerkReplacements: (Embed, 0x0, 0x0, PerkReplacementList)
    mSummonerSpecialistChoices: (Embed, 0x0, 0x0, PerkSummonerSpecialistChoices)
    mBotOverrideSet: (Link, 0x0, 0x0, OverridePerkSelectionSet)
    pass

class TftTraitVariationInfoNubData(TftInfoNubData):
    TemplateKey: (String, 0x0, 0x0, 0x0)
    Trait: (Link, 0x0, 0x0, TftTraitData)
    TextStyles: (Map, U8, String, 0x0)
    BodyKey: (String, 0x0, 0x0, 0x0)
    TitleKey: (String, 0x0, 0x0, 0x0)
    pass

class HasBuffCastRequirement(ICastRequirement):
    mBuffName: (Hash, 0x0, 0x0, 0x0)
    mFromAnyone: (Bool, 0x0, 0x0, 0x0)
    pass

class GameModeContentManager():
    mGameModeContentList: (List, 0x0, Embed, GameModeContent)
    pass

class 0x5b2fdd66(0xf9e5b8b9):
    Add: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class 0x5b49a915(TargetingTypeData):
    CanCompleteCastWithoutTarget: (Bool, 0x0, 0x0, 0x0)
    0xfb5bbd7: (Bool, 0x0, 0x0, 0x0)
    pass

class TftHintUiData():
    Message: (Pointer, 0x0, 0x0, TftHintMessageData)
    Vfx: (Pointer, 0x0, 0x0, TftHintVfxData)
    pass

class QueueDisplayData():
    QueueIconElementHover: (Hash, 0x0, 0x0, 0x0)
    IllustrationIconPath: (String, 0x0, 0x0, 0x0)
    QueueIconElementClicked: (Hash, 0x0, 0x0, 0x0)
    IllustrationIconElement: (Hash, 0x0, 0x0, 0x0)
    IllustrationIconPathDisabled: (String, 0x0, 0x0, 0x0)
    0xbcfe4458: (Pointer, 0x0, 0x0, TftHintUiData)
    DisplayNameTraKey: (String, 0x0, 0x0, 0x0)
    QueueIconElementDefault: (Hash, 0x0, 0x0, 0x0)
    QueueId: (I64, 0x0, 0x0, 0x0)
    QueueId: (U16, 0x0, 0x0, 0x0)
    QueueIconElementInactive: (Hash, 0x0, 0x0, 0x0)
    Queue: (Link, 0x0, 0x0, MatchmakingQueue)
    pass

class 0x5b5e6994():
    TimerDefaultFill: (Hash, 0x0, 0x0, 0x0)
    0x81cbec5f: (Hash, 0x0, 0x0, 0x0)
    0x9ba9ed34: (Hash, 0x0, 0x0, 0x0)
    0xbcde5149: (Hash, 0x0, 0x0, 0x0)
    pass

class IntOffsetTableGet(ScriptTableGet, IIntGet):
    Offset: (I32, 0x0, 0x0, 0x0)
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Table: (Pointer, 0x0, 0x0, RsTable)
    Var: (Hash, 0x0, 0x0, 0x0)
    Var: (String, 0x0, 0x0, 0x0)
    pass

class PreloadCharacterWithSkinId(LevelScriptBlock):
    CharacterName: (Pointer, 0x0, 0x0, IStringGet)
    SkinId: (Pointer, 0x0, 0x0, IIntGet)
    pass

class WallDetection(TargetingTypeData):
    DashRange: (F32, 0x0, 0x0, 0x0)
    DetectionRange: (F32, 0x0, 0x0, 0x0)
    pass

class TftHintVfxData():
    TargetElement: (Hash, 0x0, 0x0, 0x0)
    VfxScale: (F32, 0x0, 0x0, 0x0)
    pass

class TftTraitList():
    mTraits: (List, 0x0, Link, TftTraitData)
    VfxResourceResolver: (Link, 0x0, 0x0, ResourceResolver)
    pass

class AtomicClipData(BlendableClipData, ClipBaseData):
    mTickDuration: (F32, 0x0, 0x0, 0x0)
    mMaskData: (Link, 0x0, 0x0, MaskData)
    mSyncGroupData: (Link, 0x0, 0x0, SyncGroupData)
    mMaskDataName: (Hash, 0x0, 0x0, 0x0)
    mTrackData: (Link, 0x0, 0x0, TrackData)
    StartFrame: (F32, 0x0, 0x0, 0x0)
    mEventResourceData: (Pointer, 0x0, 0x0, EventResourceData)
    mEventDataList: (List, 0x0, Pointer, BaseEventData)
    mUpdaterResourceData: (Pointer, 0x0, 0x0, UpdaterResourceData)
    mSyncGroupDataName: (Hash, 0x0, 0x0, 0x0)
    mAnimationResourceData: (Embed, 0x0, 0x0, AnimationResourceData)
    mAnimationResourceData: (Link, 0x0, 0x0, AnimationResourceData)
    EndFrame: (F32, 0x0, 0x0, 0x0)
    mTrackDataName: (Hash, 0x0, 0x0, 0x0)
    mEndTick: (U32, 0x0, 0x0, 0x0)
    mStartTick: (U32, 0x0, 0x0, 0x0)
    pass

class ViewControllerFilter_Map(ViewControllerFilterI):
    Map: (String, 0x0, 0x0, 0x0)
    pass

class FxObjectSelector():
    Type: (U32, 0x0, 0x0, 0x0)
    pass

class ILolSpellScriptEvent(IScriptEvent):
    pass

class LootItem(LootOutputBase):
    mName: (String, 0x0, 0x0, 0x0)
    mHoverDescription: (String, 0x0, 0x0, 0x0)
    mDetails: (Embed, 0x0, 0x0, LootItemDetails)
    mAdminDescription: (String, 0x0, 0x0, 0x0)
    mInternalName: (String, 0x0, 0x0, 0x0)
    mStatus: (Embed, 0x0, 0x0, LootStatus)
    pass

class BorderPropertyData():
    BorderTreatment: (Link, 0x0, 0x0, StaticMaterialDef)
    BorderPath: (String, 0x0, 0x0, 0x0)
    pass

class VfxFloatBase():
    pass

class ICastRequirement():
    mInvertResult: (Bool, 0x0, 0x0, 0x0)
    pass

class PreloadCharacter(LevelScriptBlock):
    CharacterName: (Pointer, 0x0, 0x0, IStringGet)
    pass

class ILogicIntDriver(ILogicFloatDriver):
    pass

class LobbyLayout():
    SlotHandles: (List, 0x0, Hash, 0x0)
    SelfPortrait: (Embed, 0x0, 0x0, LobbySelfPortrait)
    CustomButtonPopupAnchor: (Hash, 0x0, 0x0, 0x0)
    SelfSwappable: (Bool, 0x0, 0x0, 0x0)
    FriendSlotHandles: (List, 0x0, Hash, 0x0)
    TeamBorders: (List, 0x0, Hash, 0x0)
    MaxPlayerCount: (U32, 0x0, 0x0, 0x0)
    FriendPortraitData: (Embed, 0x0, 0x0, LobbyFriendPortraitData)
    TeamSize: (U32, 0x0, 0x0, 0x0)
    OtherPlayerPortraitData: (Embed, 0x0, 0x0, LobbyPlayerData)
    MaxInviteCount: (U32, 0x0, 0x0, 0x0)
    SelfPortraitData: (Embed, 0x0, 0x0, LobbyPlayerData)
    pass

class AiBaseCommon(AttackableUnit):
    pass

class KeywordData():
    TitleTra: (String, 0x0, 0x0, 0x0)
    DescriptionTra: (String, 0x0, 0x0, 0x0)
    pass

class TftArenaOwnerLevelParametricUpdater(IFloatParametricUpdater):
    pass

class 0x5cb6b755():
    0x16e21209: (String, 0x0, 0x0, 0x0)
    0x20b77151: (String, 0x0, 0x0, 0x0)
    0x2abb026a: (String, 0x0, 0x0, 0x0)
    0x2e09a7c: (String, 0x0, 0x0, 0x0)
    0x2ee329e: (String, 0x0, 0x0, 0x0)
    0x314a63bb: (String, 0x0, 0x0, 0x0)
    0x3392c041: (String, 0x0, 0x0, 0x0)
    0x34276276: (String, 0x0, 0x0, 0x0)
    0x36b9f511: (String, 0x0, 0x0, 0x0)
    0x4026cb15: (String, 0x0, 0x0, 0x0)
    0x414d5717: (String, 0x0, 0x0, 0x0)
    0x4cbd596a: (String, 0x0, 0x0, 0x0)
    0x58766309: (String, 0x0, 0x0, 0x0)
    0x63d105a5: (String, 0x0, 0x0, 0x0)
    0x7e458980: (String, 0x0, 0x0, 0x0)
    BackgroundTexturePath: (String, 0x0, 0x0, 0x0)
    0x96349f57: (String, 0x0, 0x0, 0x0)
    0x9a0caad2: (String, 0x0, 0x0, 0x0)
    0xa807a4b2: (String, 0x0, 0x0, 0x0)
    0xc1d8474a: (String, 0x0, 0x0, 0x0)
    0xd0666cc4: (String, 0x0, 0x0, 0x0)
    BackgroundVfx: (Hash, 0x0, 0x0, 0x0)
    0xde84022d: (String, 0x0, 0x0, 0x0)
    0xdf83f0d3: (String, 0x0, 0x0, 0x0)
    0xe98a6e08: (String, 0x0, 0x0, 0x0)
    0xf1cfe676: (String, 0x0, 0x0, 0x0)
    0xfa3657e2: (String, 0x0, 0x0, 0x0)
    pass

class 0x5cc13029(ISequenceAction):
    DisableOnEnd: (Bool, 0x0, 0x0, 0x0)
    Index: (U32, 0x0, 0x0, 0x0)
    0xd07dcd34: (Link, 0x0, 0x0, SequenceObjectSelector)
    EnableOnStart: (Bool, 0x0, 0x0, 0x0)
    pass

class IsOwnerHeroSpawnConditions(IVfxSpawnConditions):
    mConditions: (List, 0x0, Embed, IsOwnerHeroConditionData)
    mDefaultVfxData: (Embed, 0x0, 0x0, VfxDefaultSpawnConditionData)
    pass

class UiMetricBounty(UiMetricTypeSimpleI):
    pass

class ModalShroudManager():
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    InputHandler: (Hash, 0x0, 0x0, 0x0)
    pass

class ByCharLevelBreakpointsCalculationPart(IGameCalculationPartByCharLevel, ISpellCalculationPartByCharLevel, ISpellCalculationPart):
    mInitialBonusPerLevel: (F32, 0x0, 0x0, 0x0)
    mBreakpoints: (List, 0x0, Embed, Breakpoint)
    mLevel1Value: (F32, 0x0, 0x0, 0x0)
    pass

class IMilestoneProperty():
    pass

class 0x5cfe6ce7(TftCutsceneInitializer, TftCutsceneArenaLocatorInitializer):
    0x220cba44: (String, 0x0, 0x0, 0x0)
    0x317471c2: (String, 0x0, 0x0, 0x0)
    0x61e7d1d5: (String, 0x0, 0x0, 0x0)
    0xbd8f19: (String, 0x0, 0x0, 0x0)
    pass

class 0x5d3f0253(MapGraphicsFeature):
    0x93ab957c: (Bool, 0x0, 0x0, 0x0)
    pass

class TftCutsceneCamVfxClip(TftCutsceneVfxClip):
    AssociatedPlayers: (List2, 0x0, String, 0x0)
    0x4935e06f: (Bool, 0x0, 0x0, 0x0)
    VisibleFilter: (U32, 0x0, 0x0, 0x0)
    BlackboardAssociatedPlayers: (List2, 0x0, String, 0x0)
    pass

class IEnabler():
    pass

class SequenceTable():
    ParentTables: (List, 0x0, Link, SequenceTable)
    Entries: (List, 0x0, Embed, SequenceTableEntry)
    pass

class CustomNeutralCampSpawnBehavior(INeutralCampSpawnBehavior):
    Callback: (Embed, 0x0, 0x0, LevelScriptFunctionLink)
    Callback: (Link, 0x0, 0x0, ScriptFunction)
    pass

class GetKeyValueInCustomTableBlock(IScriptBlock):
    SrcTable: (Embed, 0x0, 0x0, CustomTableGet)
    Key: (Pointer, 0x0, 0x0, IScriptValueGet)
    Dest: (Embed, 0x0, 0x0, ScriptTableSet)
    OutValue: (Embed, 0x0, 0x0, ScriptTableSet)
    CustomTable: (Embed, 0x0, 0x0, CustomTableGet)
    SrcKey: (Pointer, 0x0, 0x0, IScriptValueGet)
    pass

class FxActionVfxStaticInstance(IFxActionInstance):
    pass

class EmblemPosition():
    mHorizontal: (String, 0x0, 0x0, 0x0)
    mVertical: (String, 0x0, 0x0, 0x0)
    pass

class MapClouds(MapGraphicsFeature):
    IsEyeCandy: (Bool, 0x0, 0x0, 0x0)
    CloudsTexturePath: (String, 0x0, 0x0, 0x0)
    CloudShadowSunLightColor: (Vec4, 0x0, 0x0, 0x0)
    Layers: (List, 0x3, Embed, MapCloudsLayer)
    pass

class TftHudCombatRecapData():
    0x4544719b: (F32, 0x0, 0x0, 0x0)
    mPanelTransition: (Embed, 0x0, 0x0, HudMenuTransitionData)
    pass

class ParticleEventDataPair():
    mTargetBoneName: (Hash, 0x0, 0x0, 0x0)
    mBoneName: (Hash, 0x0, 0x0, 0x0)
    pass

class TftCutsceneEntry():
    Priority: (U32, 0x0, 0x0, 0x0)
    TriggerTime: (F32, 0x0, 0x0, 0x0)
    pass

class ChampSelectCharacterSkinData():
    ChromaColor: (Color, 0x0, 0x0, 0x0)
    Id: (I32, 0x0, 0x0, 0x0)
    AvatarIconPath: (String, 0x0, 0x0, 0x0)
    SquareIconPath: (String, 0x0, 0x0, 0x0)
    SkinParent: (I32, 0x0, 0x0, 0x0)
    0x51f324f4: (Bool, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    Index: (U32, 0x0, 0x0, 0x0)
    pass

class SourceLessThanHealthPercentageFilter(IStatStoneLogicDriver):
    HealthPercentage: (F32, 0x0, 0x0, 0x0)
    pass

class KillsOnOpponentRoleConstraintInfo(ListenerConstraintInfo):
    RoleToCheck: (U32, 0x0, 0x0, 0x0)
    pass

class 0x5e416660():
    Offset: (U32, 0x0, 0x0, 0x0)
    Values: (List, 0x0, Vec4, 0x0)
    0x95f84cd9: (String, 0x0, 0x0, 0x0)
    pass

class UiElementEffectGlowData(UiElementEffectData):
    BaseScale: (F32, 0x0, 0x0, 0x0)
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    MinimumAlpha: (F32, 0x0, 0x0, 0x0)
    CycleBasedScaleAddition: (F32, 0x0, 0x0, 0x0)
    TextureData: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    CycleTime: (F32, 0x0, 0x0, 0x0)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mAtlas: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    pass

class EffectLineElementData(EffectElementData):
    mThickness: (F32, 0x0, 0x0, 0x0)
    mRightSlicePercentage: (F32, 0x0, 0x0, 0x0)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    pass

class EventCardViewController(ViewController):
    DescriptionText: (Hash, 0x0, 0x0, 0x0)
    Highlight: (Hash, 0x0, 0x0, 0x0)
    TransitionTime: (F32, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    CountdownText: (Hash, 0x0, 0x0, 0x0)
    EasingType: (U8, 0x0, 0x0, 0x0)
    MinAlpha: (U8, 0x0, 0x0, 0x0)
    CountdownBackground: (Hash, 0x0, 0x0, 0x0)
    MaxAlpha: (U8, 0x0, 0x0, 0x0)
    SceneHandle: (Hash, 0x0, 0x0, 0x0)
    CardBackground: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class ColorLiteralMaterialDriver(IDynamicMaterialDriver):
    Value: (Vec4, 0x0, 0x0, 0x0)
    pass

class TableGet(IRsValueGet):
    Table: (Pointer, 0x0, 0x0, RsTable)
    Var: (String, 0x0, 0x0, 0x0)
    pass

class SpellObject():
    CcBehaviorData: (Pointer, 0x0, 0x0, ICcBehaviorData)
    BotData: (Pointer, 0x0, 0x0, BotsSpellData)
    mScript: (Pointer, 0x0, 0x0, LolSpellScript)
    mSpell: (Pointer, 0x0, 0x0, SpellDataResource)
    mBuff: (Pointer, 0x0, 0x0, BuffData)
    mScriptName: (String, 0x0, 0x0, 0x0)
    pass

class VfxAlphaErosionDefinitionData():
    ErosionFeatherOut: (F32, 0x0, 0x0, 0x0)
    UseLingerErosionDriveCurve: (Bool, 0x0, 0x0, 0x0)
    ErosionMapAddressMode: (U32, 0x0, 0x0, 0x0)
    ErosionMapAddressMode: (U8, 0x0, 0x0, 0x0)
    ErosionFeatherIn: (F32, 0x0, 0x0, 0x0)
    ErosionMapName: (String, 0x0, 0x0, 0x0)
    ErosionSliceWidth: (F32, 0x0, 0x0, 0x0)
    LingerErosionDriveCurve: (Embed, 0x0, 0x0, ValueFloat)
    ErosionMapChannelMixer: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    ErosionMapChannelMixer: (Embed, 0x0, 0x0, ValueColor)
    ErosionDriveCurve: (Embed, 0x0, 0x0, ValueFloat)
    ErosionDriveCurve: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    ErosionDriveSource: (U32, 0x0, 0x0, 0x0)
    ErosionDriveSource: (U8, 0x0, 0x0, 0x0)
    pass

class TooltipInstanceBuff(TooltipInstance):
    mEnableExtendedTooltip: (Bool, 0x0, 0x0, 0x0)
    EnableExtendedTooltip: (Bool, 0x0, 0x0, 0x0)
    pass

class BehaviorScript(Rscript):
    Sequences: (Map, Hash, Embed, ScriptBtRootSequence)
    Sequences: (Map, Hash, Embed, ScriptBtSequence)
    Sequences: (Map, U32, Embed, ScriptBtSequence)
    Sequences: (Map, U32, Embed, ScriptSequence)
    pass

class ItemRecommendationChoices():
    mChoices: (List, 0x0, I32, 0x0)
    mChoices: (List, 0x0, U32, 0x0)
    pass

class ISpellCalculationPartByCharLevel(ISpellCalculationPart):
    pass

class AbilityPrompt():
    AnimLink: (Hash, 0x0, 0x0, 0x0)
    TextLink: (Hash, 0x0, 0x0, 0x0)
    pass

class PlayerProfileViewController(ViewController):
    0x28dee5e9: (Embed, 0x0, 0x0, 0x28dee5e9)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    PlayerProfileCategoryButtons: (List, 0x0, Embed, PlayerProfileCategoryButtonDefinition)
    MatchHistoryView: (Embed, 0x0, 0x0, PlayerProfileMatchHistoryView)
    PlayerProfileScene: (Hash, 0x0, 0x0, 0x0)
    0xf9c23e6f: (Embed, 0x0, 0x0, 0xc00f3a0f)
    pass

class 0x5ee39f14():
    Modes: (List2, 0x0, U8, 0x0)
    pass

class ShadowOverrideSettings():
    FreeCameraShadowExtentXz: (F32, 0x0, 0x0, 0x0)
    FreeCamShadowNearClipDistance: (F32, 0x0, 0x0, 0x0)
    ShadowBias: (F32, 0x0, 0x0, 0x0)
    FreeCamShadowFarClipDistance: (F32, 0x0, 0x0, 0x0)
    TopDownCamNearClipDistance: (F32, 0x0, 0x0, 0x0)
    pass

class 0x5ee7c71f(BuffEffect):
    0x47c120b7: (List, 0x0, U8, 0x0)
    0x68aa7f75: (Bool, 0x0, 0x0, 0x0)
    CleanseOnActivate: (Bool, 0x0, 0x0, 0x0)
    pass

class UnitStatusIconData():
    InterruptibleImmobilize: (Embed, 0x0, 0x0, HealthbarImageInfo)
    InterruptibleImmobilize: (String, 0x0, 0x0, 0x0)
    Charmed: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Charmed: (String, 0x0, 0x0, 0x0)
    Grounded: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Grounded: (String, 0x0, 0x0, 0x0)
    InterruptibleDisable: (Embed, 0x0, 0x0, HealthbarImageInfo)
    InterruptibleDisable: (String, 0x0, 0x0, 0x0)
    Disarmed: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Disarmed: (String, 0x0, 0x0, 0x0)
    Stunned: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Stunned: (String, 0x0, 0x0, 0x0)
    Taunted: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Taunted: (String, 0x0, 0x0, 0x0)
    Suppressed: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Suppressed: (String, 0x0, 0x0, 0x0)
    Rooted: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Rooted: (String, 0x0, 0x0, 0x0)
    Blinded: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Blinded: (String, 0x0, 0x0, 0x0)
    Nearsighted: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Nearsighted: (String, 0x0, 0x0, 0x0)
    Drowsy: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Silenced: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Silenced: (String, 0x0, 0x0, 0x0)
    Polymorphed: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Polymorphed: (String, 0x0, 0x0, 0x0)
    InterruptibleDamage: (Embed, 0x0, 0x0, HealthbarImageInfo)
    InterruptibleDamage: (String, 0x0, 0x0, 0x0)
    Airborne: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Airborne: (String, 0x0, 0x0, 0x0)
    Fleeing: (Embed, 0x0, 0x0, HealthbarImageInfo)
    Fleeing: (String, 0x0, 0x0, 0x0)
    Asleep: (Embed, 0x0, 0x0, HealthbarImageInfo)
    pass

class 0x5f1e2b9(TargetingTypeData):
    pass

class 0x5f31ea63(0xb639bddc):
    LoadoutData: (Link, 0x0, 0x0, BaseLoadoutData)
    pass

class EvoSettings():
    mOrderAckSilenceRequirement: (F32, 0x0, 0x0, 0x0)
    mEnableAnnouncerVoReplacement: (Bool, 0x0, 0x0, 0x0)
    mEnableChatVo: (Bool, 0x0, 0x0, 0x0)
    mPingVoThrottleThreshold: (F32, 0x0, 0x0, 0x0)
    mCharacterVoGlobalCooldown: (F32, 0x0, 0x0, 0x0)
    mChatVoThrottleCounterThreshold: (I32, 0x0, 0x0, 0x0)
    mChatVoThrottleCounterDecayTime: (F32, 0x0, 0x0, 0x0)
    pass

class 0x5f5925f1():
    TierBagEntries: (List2, 0x0, Embed, TftTierEntry)
    pass

class StatByNamedDataValueCalculationPart(IGameCalculationPartWithStats, ISpellCalculationPartWithStats, ISpellCalculationPart):
    mStat: (U8, 0x0, 0x0, 0x0)
    mStatFormula: (U8, 0x0, 0x0, 0x0)
    mDataValue: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionMoveDistance(IContextualCondition):
    mCompareOp: (U8, 0x0, 0x0, 0x0)
    mSquaredDistance: (F32, 0x0, 0x0, 0x0)
    mDistance: (F32, 0x0, 0x0, 0x0)
    pass

class TftInfoNubData():
    0xeb74e3c6: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x5fcc19f1(TargetingTypeData):
    pass

class SpawningUiDefinition():
    BuffNameFilter: (String, 0x0, 0x0, 0x0)
    MaxNumberOfUnits: (I32, 0x0, 0x0, 0x0)
    pass

class GetSequenceObjectDynamicMaterialBoolDriver(ILogicBoolDriver):
    mKeyName: (String, 0x0, 0x0, 0x0)
    pass

class FloatGet(IFloatGet, IScriptValueGet):
    Value: (F32, 0x0, 0x0, 0x0)
    pass

class LoadingScreenLatency():
    Text: (Hash, 0x0, 0x0, 0x0)
    Thresholds: (List, 0x0, Embed, LoadingScreenLatencyThreshold)
    pass

class 0x6055e037(0xd866344b):
    Source: (Link, 0x0, 0x0, SequenceObjectSelector)
    pass

class ContextualConditionSpellName(IContextualConditionSpell, IContextualCondition):
    mSpell: (Hash, 0x0, 0x0, 0x0)
    mSpellName: (Hash, 0x0, 0x0, 0x0)
    pass

class ILogicVector3Driver(ILogicDriver):
    pass

class TftTeamPlannerActiveTraitData():
    TraitLevelIconTemplates: (List, 0x0, Hash, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    TraitIcon: (Hash, 0x0, 0x0, 0x0)
    SelectionOutlineTemplate: (Hash, 0x0, 0x0, 0x0)
    HighlightOutlineTemplate: (Hash, 0x0, 0x0, 0x0)
    LevelIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionCharacterIsCastingRecall(ICharacterSubcondition):
    pass

class 0x607ade7e(TftCutsceneMissileClip):
    TimeToTarget: (F32, 0x0, 0x0, 0x0)
    pass

class 0x608a3ee7(ILogicIntDriver):
    pass

class ShaderStaticSwitch():
    Name: (String, 0x0, 0x0, 0x0)
    OnByDefault: (Bool, 0x0, 0x0, 0x0)
    OnByDefalt: (Bool, 0x0, 0x0, 0x0)
    pass

class StaticMaterialTechniqueDef():
    Passes: (List, 0x0, Embed, StaticMaterialPassDef)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class StrawberryAugmentSlotData():
    AugmentGroup: (Hash, 0x0, 0x0, 0x0)
    AugmentPickedVfx: (Hash, 0x0, 0x0, 0x0)
    0x4ddb7d67: (Hash, 0x0, 0x0, 0x0)
    AugmentDescription: (Hash, 0x0, 0x0, 0x0)
    AugmentRefreshVfx: (Hash, 0x0, 0x0, 0x0)
    AugmentNotPickedVfx: (Hash, 0x0, 0x0, 0x0)
    AugmentIcon: (Hash, 0x0, 0x0, 0x0)
    AugmentIdleVfx: (Hash, 0x0, 0x0, 0x0)
    AugmentName: (Hash, 0x0, 0x0, 0x0)
    AugmentLevelTitle: (Hash, 0x0, 0x0, 0x0)
    AugmentHoverVfx: (Hash, 0x0, 0x0, 0x0)
    AugmentDisplayTagData: (Embed, 0x0, 0x0, StrawberryAugmentDisplayTagData)
    AugmentRefreshOverlayVfx: (Hash, 0x0, 0x0, 0x0)
    AugmentLevelUpData: (Hash, 0x0, 0x0, 0x0)
    AugmentButton: (Hash, 0x0, 0x0, 0x0)
    pass

class SameTeamCastRequirement(ICastRequirement):
    pass

class BarracksDampener(BarracksDampenerCommon):
    pass

class MapWorldParticle():
    EffectName: (String, 0x0, 0x0, 0x0)
    State: (U8, 0x0, 0x0, 0x0)
    Particle: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    EffectKey: (String, 0x0, 0x0, 0x0)
    EffectState: (String, 0x0, 0x0, 0x0)
    pass

class PfxFieldDragDefinitionData():
    Position: (Embed, 0x0, 0x0, PfxAnimatedVector3fVariableData)
    Radius: (Embed, 0x0, 0x0, PfxAnimatedFloatVariableData)
    Strength: (Embed, 0x0, 0x0, PfxAnimatedFloatVariableData)
    pass

class ScriptDataObject():
    mName: (String, 0x0, 0x0, 0x0)
    mConstants: (Map, String, Pointer, GameModeConstant)
    mRequiredConstantsGroup: (Link, 0x0, 0x0, GameModeConstantsGroup)
    pass

class 0x60e2ec74(IGameModeConfigClient):
    MutatorControlledLoadingScreenBackgrounds: (List2, 0x0, String, 0x0)
    LoadingScreenBackground: (String, 0x0, 0x0, 0x0)
    LoadScreenTipConfiguration: (Link, 0x0, 0x0, LoadScreenTipConfiguration)
    LoadingScreenBackgroundOverride: (Map, String, String, 0x0)
    pass

class 0x60fea92f(ISequenceActionInstance):
    pass

class SkinMeshDataProperties():
    ReflectionOpacityDirect: (F32, 0x0, 0x0, 0x0)
    ReflectionFresnel: (F32, 0x0, 0x0, 0x0)
    AllowCharacterInking: (Bool, 0x0, 0x0, 0x0)
    ReflectionOpacityGlancing: (F32, 0x0, 0x0, 0x0)
    RoughnessMetallicAoTexture: (String, 0x0, 0x0, 0x0)
    MaterialOverride: (List, 0x0, Embed, SkinMeshDataProperties_MaterialOverride)
    SelfIllumination: (F32, 0x0, 0x0, 0x0)
    ForceDrawLast: (Bool, 0x0, 0x0, 0x0)
    FresnelBlue: (F32, 0x0, 0x0, 0x0)
    ReflectionFresnelRed: (F32, 0x0, 0x0, 0x0)
    SubmeshRenderOrder: (String, 0x0, 0x0, 0x0)
    VintageCutoffDate: (String, 0x0, 0x0, 0x0)
    EmitterSubmeshAvatarToHide: (String, 0x0, 0x0, 0x0)
    InitialSubmeshMouseOversToHide: (String, 0x0, 0x0, 0x0)
    FresnelColor: (Color, 0x0, 0x0, 0x0)
    Texture: (String, 0x0, 0x0, 0x0)
    BoundingCylinderRadius: (F32, 0x0, 0x0, 0x0)
    ReflectionFresnelColor: (Color, 0x0, 0x0, 0x0)
    EndingJointForTrailFollowTemp: (I32, 0x0, 0x0, 0x0)
    OverrideBoundingBox: (Option, 0x0, Vec3, 0x0)
    OverrideBoundingBox: (Vec3, 0x0, 0x0, 0x0)
    StartingJointForTrailFollowTemp: (I32, 0x0, 0x0, 0x0)
    BoundingCylinderHeight: (F32, 0x0, 0x0, 0x0)
    TextureLow: (String, 0x0, 0x0, 0x0)
    FresnelRed: (F32, 0x0, 0x0, 0x0)
    MaterialController: (Pointer, 0x0, 0x0, SkinnedMeshDataMaterialController)
    InitialSubmeshToHide: (String, 0x0, 0x0, 0x0)
    Fresnel: (F32, 0x0, 0x0, 0x0)
    BoundingSphereRadius: (F32, 0x0, 0x0, 0x0)
    BoundingSphereRadius: (Option, 0x0, F32, 0x0)
    Temp_RenderThisSkinWithMaterials: (Bool, 0x0, 0x0, 0x0)
    EmissiveTexture: (String, 0x0, 0x0, 0x0)
    SkinScale: (F32, 0x0, 0x0, 0x0)
    CastShadows: (Bool, 0x0, 0x0, 0x0)
    Skeleton: (String, 0x0, 0x0, 0x0)
    EnablePicking: (Bool, 0x0, 0x0, 0x0)
    MaxNumBlendWeights: (I32, 0x0, 0x0, 0x0)
    InitialSubmeshAvatarToHide: (String, 0x0, 0x0, 0x0)
    BrushAlphaOverride: (F32, 0x0, 0x0, 0x0)
    ReflectionFresnelBlue: (F32, 0x0, 0x0, 0x0)
    ReflectionFresnelGreen: (F32, 0x0, 0x0, 0x0)
    Material: (Link, 0x0, 0x0, MaterialDef)
    Material: (Link, 0x0, 0x0, IMaterialDef)
    Material: (String, 0x0, 0x0, 0x0)
    ReducedBoneSkinning: (Bool, 0x0, 0x0, 0x0)
    SimpleSkin: (String, 0x0, 0x0, 0x0)
    FresnelGreen: (F32, 0x0, 0x0, 0x0)
    ReflectionMap: (String, 0x0, 0x0, 0x0)
    GlossTexture: (String, 0x0, 0x0, 0x0)
    UsesSkinVo: (Bool, 0x0, 0x0, 0x0)
    NormalMapTexture: (String, 0x0, 0x0, 0x0)
    RigPoseModifierData: (List, 0x0, Pointer, BaseRigPoseModifierData)
    InitialSubmeshShadowsToHide: (String, 0x0, 0x0, 0x0)
    pass

class 0x6136d145(0x64c18f7d):
    TargetSkinScale: (F32, 0x0, 0x0, 0x0)
    pass

class HealthBarExtraBarsData():
    PhysicalShieldBar: (Hash, 0x0, 0x0, 0x0)
    IncomingHealBar: (Pointer, 0x0, 0x0, BarTypeMap)
    DisguiseHealthBar: (Hash, 0x0, 0x0, 0x0)
    AllShieldBar: (Hash, 0x0, 0x0, 0x0)
    ChampSpecificBar: (Pointer, 0x0, 0x0, BarTypeMap)
    MagicShieldBar: (Hash, 0x0, 0x0, 0x0)
    pass

class ModeSelectQueueButtonData():
    SubtitleText: (Hash, 0x0, 0x0, 0x0)
    0x38a08ce2: (Hash, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    IllustrationIcon: (Hash, 0x0, 0x0, 0x0)
    ButtonDisabledIcon: (Hash, 0x0, 0x0, 0x0)
    ButtonClickedIcon: (Hash, 0x0, 0x0, 0x0)
    ButtonHoverIcon: (Hash, 0x0, 0x0, 0x0)
    NewPip: (Embed, 0x0, 0x0, 0x6241da2)
    RestrictionIcon: (Hash, 0x0, 0x0, 0x0)
    ButtonDefaultIcon: (Hash, 0x0, 0x0, 0x0)
    IllustrationIconDisabled: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionOwnerTeamNetChampionKills(IContextualCondition):
    mTimeFrameSeconds: (F32, 0x0, 0x0, 0x0)
    mOwnerTeamNetKillAdvantage: (I32, 0x0, 0x0, 0x0)
    mKillAdvantageCompareOp: (U8, 0x0, 0x0, 0x0)
    pass

class TftCutsceneInitializer():
    pass

class 0x61902388():
    0xc70f6a1e: (Link, 0x0, 0x0, 0xb7b2875)
    0xea27ff5b: (Embed, 0x0, 0x0, 0xf1fd1323)
    pass

class SpellPickChoiceViewController(ViewController):
    TimeoutWarningThrobEaseType: (U8, 0x0, 0x0, 0x0)
    SpellChoiceTemplate: (Embed, 0x0, 0x0, SpellChoiceTemplate)
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TimeoutWarningThrobDuration: (F32, 0x0, 0x0, 0x0)
    Grid: (Hash, 0x0, 0x0, 0x0)
    TimeoutWarningDuration: (F32, 0x0, 0x0, 0x0)
    ConfirmButton: (Hash, 0x0, 0x0, 0x0)
    MaxNumChoices: (U32, 0x0, 0x0, 0x0)
    CountdownMeter: (Hash, 0x0, 0x0, 0x0)
    pass

class FxTable():
    ParentTables: (List, 0x0, Link, FxTable)
    Entries: (List, 0x0, Embed, FxTableEntry)
    pass

class DeathRecapShowcaseSlotData():
    SlotGroup: (Hash, 0x0, 0x0, 0x0)
    pass

class TftCutscenePosProviderVfxClip(TftCutsceneVfxClip):
    HideWhenNotViewed: (Bool, 0x0, 0x0, 0x0)
    Position: (Pointer, 0x0, 0x0, TftCutscenePositionProvider)
    pass

class ItemDataValues():
    DataValues: (List, 0x0, Embed, ItemDataValue)
    pass

class HudDamageDisplayData():
    0xdfcea7db: (F32, 0x0, 0x0, 0x0)
    pass

class VisionConfig(IGameModeConfig):
    0x667106f9: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x6222096a():
    pass

class 0x6241da2():
    0x114ce1e2: (Hash, 0x0, 0x0, 0x0)
    NewPipVfx: (Hash, 0x0, 0x0, 0x0)
    pass

class PlaybookInfoPanel():
    Subtitle: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    Description: (Hash, 0x0, 0x0, 0x0)
    EquippedIcon: (Hash, 0x0, 0x0, 0x0)
    Name: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    ViewPaneLink: (Hash, 0x0, 0x0, 0x0)
    pass

class UiMilestoneProgressMeter():
    ProgressBarDelayTime: (F32, 0x0, 0x0, 0x0)
    MeterEasingType: (U8, 0x0, 0x0, 0x0)
    ExpText: (Hash, 0x0, 0x0, 0x0)
    NormalSkin: (Embed, 0x0, 0x0, UiElementMeterSkin)
    XpValueToSegmentIndex: (List2, 0x0, U16, 0x0)
    LevelText: (Hash, 0x0, 0x0, 0x0)
    ShowLevelUp: (Bool, 0x0, 0x0, 0x0)
    BarVfxGroup: (Hash, 0x0, 0x0, 0x0)
    LevelUpVfxGroup: (Hash, 0x0, 0x0, 0x0)
    ProgressMeterSegments: (List2, 0x0, Hash, 0x0)
    LevelUpVfx: (Hash, 0x0, 0x0, 0x0)
    ProgressMeter: (Hash, 0x0, 0x0, 0x0)
    BonusSkin: (Embed, 0x0, 0x0, UiElementMeterSkin)
    MeterTransitionTimeSecs: (F32, 0x0, 0x0, 0x0)
    pass

class TargeterDefinitionWall(TargeterDefinition):
    WallOrientation: (U32, 0x0, 0x0, 0x0)
    Thickness: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    WallRotation: (F32, 0x0, 0x0, 0x0)
    Length: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    TextureWallOverrideName: (String, 0x0, 0x0, 0x0)
    CenterLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    pass

class 0x629f5938():
    UiElement: (Hash, 0x0, 0x0, 0x0)
    UnitPropertyToggle: (Hash, 0x0, 0x0, 0x0)
    pass

class AutoSpellCastInfo():
    AutoSpellCast: (Bool, 0x0, 0x0, 0x0)
    pass

class HybridMaterialDefPreset():
    SrcColorBlendFactor: (U8, 0x0, 0x0, 0x0)
    BlendEnable: (Bool, 0x0, 0x0, 0x0)
    DepthOffsetSlope: (F32, 0x0, 0x0, 0x0)
    StencilEnable: (Bool, 0x0, 0x0, 0x0)
    CullEnable: (Bool, 0x0, 0x0, 0x0)
    WindingToCull: (U8, 0x0, 0x0, 0x0)
    StencilPassDepthPassOp: (U8, 0x0, 0x0, 0x0)
    DstAlphaBlendFactor: (U8, 0x0, 0x0, 0x0)
    BlendEquation: (U8, 0x0, 0x0, 0x0)
    StencilCompareFunc: (U8, 0x0, 0x0, 0x0)
    SrcAlphaBlendFactor: (U8, 0x0, 0x0, 0x0)
    DepthCompareFunc: (U8, 0x0, 0x0, 0x0)
    PolygonDepthBiasEnable: (Bool, 0x0, 0x0, 0x0)
    StencilPassDepthFailOp: (U8, 0x0, 0x0, 0x0)
    StencilMask: (U32, 0x0, 0x0, 0x0)
    WriteMask: (U8, 0x0, 0x0, 0x0)
    DstColorBlendFactor: (U8, 0x0, 0x0, 0x0)
    StencilReferenceVal: (U32, 0x0, 0x0, 0x0)
    DepthEnable: (Bool, 0x0, 0x0, 0x0)
    StencilFailOp: (U8, 0x0, 0x0, 0x0)
    ShaderMacros: (Map, String, String, 0x0)
    DepthOffsetBias: (F32, 0x0, 0x0, 0x0)
    pass

class GenericSplineMovementSpec(MissileMovementSpec):
    mUseMissilePositionAsOrigin: (Bool, 0x0, 0x0, 0x0)
    mSplineInfo: (Pointer, 0x0, 0x0, ISplineInfo)
    0xff738f10: (U8, 0x0, 0x0, 0x0)
    pass

class UiElementData(UiElementIData):
    mBlockInputEvents: (Bool, 0x0, 0x0, 0x0)
    mRectSourceResolutionWidth: (U16, 0x0, 0x0, 0x0)
    Enabled: (Bool, 0x0, 0x0, 0x0)
    mRectSourceResolutionHeight: (U16, 0x0, 0x0, 0x0)
    mDraggable: (U32, 0x0, 0x0, 0x0)
    mEnabled: (Bool, 0x0, 0x0, 0x0)
    StickyDrag: (Bool, 0x0, 0x0, 0x0)
    Layer: (U32, 0x0, 0x0, 0x0)
    mLayer: (U32, 0x0, 0x0, 0x0)
    mKeepMaxScale: (Bool, 0x0, 0x0, 0x0)
    DragType: (Pointer, 0x0, 0x0, UiDraggableBasic)
    mHitTestPolygon: (List, 0x0, Vec2, 0x0)
    mRect: (Vec4, 0x0, 0x0, 0x0)
    mUseRectSourceResolutionAsFloor: (Bool, 0x0, 0x0, 0x0)
    Position: (Pointer, 0x0, 0x0, UiPositionRect)
    Position: (Pointer, 0x0, 0x0, UiPositionBase)
    BlockInputEvents: (Bool, 0x0, 0x0, 0x0)
    mFullscreen: (Bool, 0x0, 0x0, 0x0)
    mNoPixelSnappingY: (Bool, 0x0, 0x0, 0x0)
    mNoPixelSnappingX: (Bool, 0x0, 0x0, 0x0)
    mAnchors: (Pointer, 0x0, 0x0, AnchorBase)
    pass

class TftEffectAmount():
    FormatString: (String, 0x0, 0x0, 0x0)
    Value: (F32, 0x0, 0x0, 0x0)
    Name: (Hash, 0x0, 0x0, 0x0)
    pass

class ItemRecommendationOverride():
    mStartingItemSets: (List, 0x0, Embed, ItemRecommendationOverrideStartingItemSet)
    mCoreItems: (List, 0x0, Hash, 0x0)
    mRecItemRanges: (List, 0x0, Embed, ItemRecOverrideRange)
    mRecommendedItems: (List, 0x0, Embed, ItemRecommendationCondition)
    mForceOverride: (Bool, 0x0, 0x0, 0x0)
    mOverrideContexts: (List, 0x0, Embed, ItemRecommendationOverrideContext)
    StartingItemBundles: (List, 0x0, Embed, ItemRecommendationOverrideStartingItemBundle)
    pass

class FixedSpeedMovement(MissileMovementSpec):
    mProjectTargetToCastRange: (Bool, 0x0, 0x0, 0x0)
    mSpeed: (F32, 0x0, 0x0, 0x0)
    mUseGroundHeightAtTarget: (Bool, 0x0, 0x0, 0x0)
    mInferDirectionFromFacingIfNeeded: (Bool, 0x0, 0x0, 0x0)
    AddBonusAttackRangeToCastRange: (Bool, 0x0, 0x0, 0x0)
    pass

class TempTable3Table(ScriptTable):
    pass

class TftOutOfGameItemData():
    ItemId: (I32, 0x0, 0x0, 0x0)
    IconPath: (String, 0x0, 0x0, 0x0)
    pass

class EndGameBlock(IScriptBlock):
    pass

class UiElementGroupButtonAdditionalElements():
    DefaultStateElements: (List, 0x0, Hash, 0x0)
    DefaultStateElements: (List2, 0x0, Hash, 0x0)
    SelectedStateElements: (List, 0x0, Hash, 0x0)
    SelectedStateElements: (List2, 0x0, Hash, 0x0)
    SelectedClickedStateElements: (List, 0x0, Hash, 0x0)
    SelectedClickedStateElements: (List2, 0x0, Hash, 0x0)
    InactiveStateElements: (List, 0x0, Hash, 0x0)
    InactiveStateElements: (List2, 0x0, Hash, 0x0)
    ClickedStateElements: (List, 0x0, Hash, 0x0)
    ClickedStateElements: (List2, 0x0, Hash, 0x0)
    SelectedHoverStateElements: (List, 0x0, Hash, 0x0)
    SelectedHoverStateElements: (List2, 0x0, Hash, 0x0)
    HoverStateElements: (List, 0x0, Hash, 0x0)
    HoverStateElements: (List2, 0x0, Hash, 0x0)
    pass

class RootCrowdControlFilter(IStatStoneLogicDriver):
    pass

class LootItemDetails():
    mRarity: (U32, 0x0, 0x0, 0x0)
    mValue: (U32, 0x0, 0x0, 0x0)
    mStoreId: (U32, 0x0, 0x0, 0x0)
    pass

class VfxFieldNoiseDefinitionData():
    Frequency: (Embed, 0x0, 0x0, ValueFloat)
    Position: (Embed, 0x0, 0x0, ValueVector3)
    Position: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    Period: (Embed, 0x0, 0x0, ValueFloat)
    Period: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    VelocityDelta: (Embed, 0x0, 0x0, ValueFloat)
    VelocityDelta: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    AxisFraction: (Vec3, 0x0, 0x0, 0x0)
    Radius: (Embed, 0x0, 0x0, ValueFloat)
    Radius: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    pass

class ContextualActionPlayAudio(IContextualAction):
    mWaitForAnnouncerQueue: (Bool, 0x0, 0x0, 0x0)
    mWaitTimeout: (F32, 0x0, 0x0, 0x0)
    mEnemyEventName: (String, 0x0, 0x0, 0x0)
    mResolveEventUsingStolenLines: (Bool, 0x0, 0x0, 0x0)
    mAuxBusName: (String, 0x0, 0x0, 0x0)
    mAllyEventName: (String, 0x0, 0x0, 0x0)
    mActionName: (String, 0x0, 0x0, 0x0)
    mResolveEventAsTarget: (Bool, 0x0, 0x0, 0x0)
    mSelfEventName: (String, 0x0, 0x0, 0x0)
    mSpectatorEventName: (String, 0x0, 0x0, 0x0)
    pass

class GameModeConstant():
    pass

class StoreViewPurchases():
    PurchaseFooter: (Hash, 0x0, 0x0, 0x0)
    PurchaseHeader: (Hash, 0x0, 0x0, 0x0)
    NoPurchasesText: (Hash, 0x0, 0x0, 0x0)
    UiStorePurchaseRowData: (Embed, 0x0, 0x0, UiStorePurchaseRowData)
    PurchaseGrid: (Hash, 0x0, 0x0, 0x0)
    PurchasesLoadingVfx: (Hash, 0x0, 0x0, 0x0)
    pass

class ConditionFloatPairData():
    mValue: (F32, 0x0, 0x0, 0x0)
    mHoldAnimationToLower: (F32, 0x0, 0x0, 0x0)
    mClipId: (U32, 0x0, 0x0, 0x0)
    mHoldAnimationToHigher: (F32, 0x0, 0x0, 0x0)
    mClipName: (Hash, 0x0, 0x0, 0x0)
    mFloatValue: (F32, 0x0, 0x0, 0x0)
    pass

class GameModeConstantBool(GameModeConstant):
    mValue: (Bool, 0x0, 0x0, 0x0)
    pass

class ContextualConditionCharacterDistance(ICharacterSubcondition):
    mDistanceTarget: (U8, 0x0, 0x0, 0x0)
    mCompareOp: (U8, 0x0, 0x0, 0x0)
    mDistance: (F32, 0x0, 0x0, 0x0)
    pass

class MapContainsOtherMaps(MapComponent):
    MapContainerLocations: (Link, 0x0, 0x0, MapPlaceableContainer)
    pass

class HudReplayEventLineBaseIcons():
    FrameLeft: (Hash, 0x0, 0x0, 0x0)
    TeamHighlight0: (Hash, 0x0, 0x0, 0x0)
    TeamHighlight1: (Hash, 0x0, 0x0, 0x0)
    IconLeft: (Hash, 0x0, 0x0, 0x0)
    FrameCenter: (Hash, 0x0, 0x0, 0x0)
    IconCenter: (Hash, 0x0, 0x0, 0x0)
    IconKill: (Hash, 0x0, 0x0, 0x0)
    IconRight: (Hash, 0x0, 0x0, 0x0)
    FrameRight: (Hash, 0x0, 0x0, 0x0)
    pass

class Self(TargetingTypeData):
    pass

class ChildMissileRepulsion(MissileBehaviorSpec):
    mSiblingRepulsion: (F32, 0x0, 0x0, 0x0)
    pass

class BasicSkinAugment(ISkinAugment):
    Modifiers: (List2, 0x0, Pointer, ISkinAugmentModifier)
    pass

class QuestTrackerMessageTemplate():
    BodyIcon: (Hash, 0x0, 0x0, 0x0)
    SlotArea: (Hash, 0x0, 0x0, 0x0)
    SwoshAnim: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    TextByIcon: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    PulseBackground: (Hash, 0x0, 0x0, 0x0)
    pass

class MicroTicksPerTickData():
    MinHealth: (F32, 0x0, 0x0, 0x0)
    MicroTicksBetween: (U32, 0x0, 0x0, 0x0)
    pass

class 0x64c18f7d():
    pass

class AddLevelTimer(LevelScriptBlock):
    PassThroughParameters: (Map, Hash, Pointer, IScriptValueGet)
    Callback: (Embed, 0x0, 0x0, LevelScriptFunctionLink)
    Callback: (Link, 0x0, 0x0, ScriptFunction)
    PeriodicFrequencySecs: (Pointer, 0x0, 0x0, IFloatGet)
    InitialDelaySecs: (Pointer, 0x0, 0x0, IFloatGet)
    pass

class TftTraitAssignmentVariation():
    TraitAssignments: (List2, 0x0, Embed, TftTraitAssignment)
    0xd009f732: (Link, 0x0, 0x0, TftTraitData)
    pass

class SponsoredBanner():
    SponsorMaterial: (Link, 0x0, 0x0, IMaterialDef)
    Banner: (Link, 0x0, 0x0, BannerData)
    Banner: (Link, 0x0, 0x0, EsportsBannerData)
    SponsorTexturePath: (File, 0x0, 0x0, 0x0)
    SponsorTexturePath: (String, 0x0, 0x0, 0x0)
    pass

class 0x64e7b9e1(0xa24429bf):
    Animation: (Hash, 0x0, 0x0, 0x0)
    pass

class MapContextualClick(MapComponent):
    ClickParticles: (Map, String, Link, VfxSystemDefinitionData)
    pass

class 0x6515c276(IScriptBlock, IBehaviorScriptBlock):
    pass

class MaxMaterialDriver(IDynamicMaterialDriver, ILogicDriver):
    mDrivers: (List, 0x0, Pointer, IDynamicMaterialDriver)
    mDrivers: (List, 0x0, Pointer, ILogicDriver)
    pass

class TftCombatRecapPanelTemplate():
    Scene: (Hash, 0x0, 0x0, 0x0)
    OpponentHealthText: (Hash, 0x0, 0x0, 0x0)
    OpponentIcon: (Hash, 0x0, 0x0, 0x0)
    LeftViewPaneDefinition: (Embed, 0x0, 0x0, ViewPaneDefinition)
    ModeLabel: (Hash, 0x0, 0x0, 0x0)
    OpponentFrame: (Hash, 0x0, 0x0, 0x0)
    ViewPaneDefinition: (Embed, 0x0, 0x0, ViewPaneDefinition)
    OpponentBackground: (Hash, 0x0, 0x0, 0x0)
    PlayerName: (Hash, 0x0, 0x0, 0x0)
    ViewPaneLink: (Hash, 0x0, 0x0, 0x0)
    OpponentFillMeter: (Hash, 0x0, 0x0, 0x0)
    LeftViewPanelink: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x65597744(IBehaviorScriptBlock):
    pass

class 0x6560a660(ILolSpellScriptEvent):
    pass

class LoadingScreenRankedProperties():
    mDescriptor: (String, 0x0, 0x0, 0x0)
    mDivision: (U8, 0x0, 0x0, 0x0)
    pass

class UiTextureProviderMesh(UiTextureProviderBase):
    pass

class 0x658ecca7(IBehaviorScriptBlock):
    pass

class PlaybookAugmentPanelData():
    0x454175b4: (U8, 0x0, 0x0, 0x0)
    0x87ff6cbc: (U8, 0x0, 0x0, 0x0)
    MidAugmentGrid: (Hash, 0x0, 0x0, 0x0)
    LateAugmentGrid: (Hash, 0x0, 0x0, 0x0)
    0xa233b0ab: (Hash, 0x0, 0x0, 0x0)
    ViewPanelScene: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x65a1bb16(0x9a573886):
    Easing: (U8, 0x0, 0x0, 0x0)
    pass

class PlayerFields():
    SummonerIcon: (Hash, 0x0, 0x0, 0x0)
    NameTag: (Hash, 0x0, 0x0, 0x0)
    PlacementText: (Hash, 0x0, 0x0, 0x0)
    SummonerIconFrame: (Hash, 0x0, 0x0, 0x0)
    HiddenUnitCountText: (Hash, 0x0, 0x0, 0x0)
    pass

class TftItemComposition():
    mComponents: (List, 0x0, Link, TftItemData)
    pass

class 0x65c4db8f(0x6c7a6a03):
    Source: (Link, 0x0, 0x0, SequenceObjectSelector)
    pass

class ISpellRankUpRequirement():
    pass

class MaterialSamplerData():
    AddressV: (U8, 0x0, 0x0, 0x0)
    AddressU: (U8, 0x0, 0x0, 0x0)
    FilterMin: (U8, 0x0, 0x0, 0x0)
    FilterMip: (U8, 0x0, 0x0, 0x0)
    FilterMag: (U8, 0x0, 0x0, 0x0)
    DefaultTextureName: (String, 0x0, 0x0, 0x0)
    AddressW: (U8, 0x0, 0x0, 0x0)
    pass

class InputSourceFloatAsBool(IInputSourceBool):
    Threshold: (F32, 0x0, 0x0, 0x0)
    FloatSource: (Pointer, 0x0, 0x0, IInputSourceFloat)
    pass

class FxActionTftCameraAnimation(IFxAction, ISequenceAction):
    CameraBone: (String, 0x0, 0x0, 0x0)
    CameraView: (U32, 0x0, 0x0, 0x0)
    SkinId: (U32, 0x0, 0x0, 0x0)
    Character: (Link, 0x0, 0x0, Character)
    Priority: (U8, 0x0, 0x0, 0x0)
    Location: (Pointer, 0x0, 0x0, IFxLocation)
    Location: (Pointer, 0x0, 0x0, ISequenceLocation)
    CameraAnimation: (String, 0x0, 0x0, 0x0)
    pass

class RandomChanceCondition(IRsCondition):
    PercentageChance: (Pointer, 0x0, 0x0, IFloatGet)
    pass

class EmblemData():
    mName: (String, 0x0, 0x0, 0x0)
    mPosition: (Map, String, Embed, EmblemPosition)
    mHasSmallImage: (Bool, 0x0, 0x0, 0x0)
    mRarityGemId: (U32, 0x0, 0x0, 0x0)
    mShowOnLoadingScreen: (Bool, 0x0, 0x0, 0x0)
    mLoadingScreenScale: (F32, 0x0, 0x0, 0x0)
    mEmblemId: (I32, 0x0, 0x0, 0x0)
    mEmblemId: (U32, 0x0, 0x0, 0x0)
    mImagePath: (String, 0x0, 0x0, 0x0)
    pass

class MusicAudioDataProperties():
    DefeatBannerSound: (String, 0x0, 0x0, 0x0)
    AmbientEvent: (String, 0x0, 0x0, 0x0)
    DefeatMusicId: (String, 0x0, 0x0, 0x0)
    LegacyThemeMusicTransitionId: (String, 0x0, 0x0, 0x0)
    VictoryBannerSound: (String, 0x0, 0x0, 0x0)
    ThemeMusicTransitionId: (String, 0x0, 0x0, 0x0)
    ReverbPreset: (String, 0x0, 0x0, 0x0)
    VictoryMusicId: (String, 0x0, 0x0, 0x0)
    GameQuitEvent: (String, 0x0, 0x0, 0x0)
    LegacyThemeMusicId: (String, 0x0, 0x0, 0x0)
    ThemeMusicId: (String, 0x0, 0x0, 0x0)
    GameStartEvent: (String, 0x0, 0x0, 0x0)
    pass

class UiElementGroupMeter(UiElementGroup):
    pass

class CherrySpectateMatchDialogText():
    0x14810744: (String, 0x0, 0x0, 0x0)
    0x270bd9c2: (String, 0x0, 0x0, 0x0)
    0x9e7b5cd7: (String, 0x0, 0x0, 0x0)
    0xd9e1766a: (String, 0x0, 0x0, 0x0)
    0xdecfb3d8: (String, 0x0, 0x0, 0x0)
    pass

class TeamScoreUiData():
    Team2Text: (Hash, 0x0, 0x0, 0x0)
    Team1Icon: (Hash, 0x0, 0x0, 0x0)
    Team2Icon: (Hash, 0x0, 0x0, 0x0)
    Team1Text: (Hash, 0x0, 0x0, 0x0)
    pass

class ByItemEpicnessCountCalculationPart(IGameCalculationPart):
    Epicness: (U8, 0x0, 0x0, 0x0)
    Coefficient: (F32, 0x0, 0x0, 0x0)
    pass

class 0x6653bfda(0x304e703f):
    Spell: (Hash, 0x0, 0x0, 0x0)
    pass

class AiHero(AiBaseClient):
    pass

class SyncGroupData():
    mName: (Hash, 0x0, 0x0, 0x0)
    mType: (U32, 0x0, 0x0, 0x0)
    pass

class CcBehaviorsConfig():
    ExperimentalBehaviors: (List2, 0x0, Hash, 0x0)
    BerserkTargetingParametersMap: (Map, Hash, Embed, BerserkTargetingPriorityList)
    BerserkTargetingParameters: (List, 0x0, Embed, BerserkTargetingParameters)
    TargetingParametersMap: (Map, Hash, Embed, TargetingPriorityList)
    pass

class 0x6693bb9(0x2b00c366):
    0x2484d6c3: (Bool, 0x0, 0x0, 0x0)
    Arena: (Link, 0x0, 0x0, TftMapSkin)
    pass

class ChangeTurnRadius(MissileTriggeredActionSpec):
    mTurnRadiusByLevel: (List, 0x7, F32, 0x0)
    pass

class 0x66b38743():
    PathHash: (Hash, 0x0, 0x0, 0x0)
    pass

class DestroyOnHit(MissileBehaviorSpec):
    pass

class TftCharacter(ICharacter, BinFileContainer):
    Name: (String, 0x0, 0x0, 0x0)
    pass

class 0x66be4e7d():
    mActionFxTable: (Link, 0x0, 0x0, FxTable)
    mUiFxTable: (Link, 0x0, 0x0, FxTable)
    pass

class RsOrCondition(IRsCondition):
    Conditions: (List, 0x0, Pointer, IRsCondition)
    pass

class BrowserInstanceData(InstanceDataBase):
    Url: (String, 0x0, 0x0, 0x0)
    ForegroundImage: (Embed, 0x0, 0x0, TextureOverride)
    pass

class 0x671b7351(0x1519e8d2):
    VfxGroupName: (String, 0x0, 0x0, 0x0)
    pass

class 0x67406e7f(0xbc280d0a):
    Value: (String, 0x0, 0x0, 0x0)
    pass

class OptionTemplateGroup(IOptionTemplate):
    ExpandButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    IndentScale: (F32, 0x0, 0x0, 0x0)
    LabelHoverColor: (Color, 0x0, 0x0, 0x0)
    PostGroupPaddingRegion: (Hash, 0x0, 0x0, 0x0)
    LabelElement: (Hash, 0x0, 0x0, 0x0)
    pass

class UiElementGroupButtonState():
    DisplayElements: (List, 0x0, Link, ElementDataI)
    DisplayElements: (List, 0x0, Link, UiElementIData)
    DisplayElementList: (List2, 0x0, Link, UiElementIData)
    TextElement: (Link, 0x0, 0x0, TextElementData)
    TextElement: (Link, 0x0, 0x0, UiElementTextData)
    TextFrameElement: (Link, 0x0, 0x0, UiElementIconData)
    pass

class PersistentEffectConditionData():
    OwnerCondition: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    PersistentVfxs: (List, 0x0, Embed, PersistentVfxData)
    PersistentVfxs: (List2, 0x0, Embed, PersistentVfxData)
    SourceCondition: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    ForceRenderVfx: (Bool, 0x0, 0x0, 0x0)
    SubmeshesToShow: (List, 0x0, Hash, 0x0)
    SubmeshesToShow: (List2, 0x0, Hash, 0x0)
    SubmeshesToHide: (List, 0x0, Hash, 0x0)
    SubmeshesToHide: (List2, 0x0, Hash, 0x0)
    pass

class MapPlaceableLinkGroup():
    Chunk: (Link, 0x0, 0x0, MapPlaceableContainer)
    Placeables: (List, 0x0, Embed, MapPlaceableName)
    pass

class 0x67c526d3(ILogicFloatDriver):
    Spell: (Hash, 0x0, 0x0, 0x0)
    ScriptName: (String, 0x0, 0x0, 0x0)
    pass

class HealthbarImageInfo():
    mOffset: (Vec2, 0x0, 0x0, 0x0)
    mTextureUvs: (Vec4, 0x0, 0x0, 0x0)
    mTextureName: (String, 0x0, 0x0, 0x0)
    pass

class TempTable1Table(ScriptTable):
    pass

class ViewControllerFilter_Champion(ViewControllerFilterI):
    Relationship: (U8, 0x0, 0x0, 0x0)
    ChampionSkinDataLink: (String, 0x0, 0x0, 0x0)
    pass

class LoadingScreenPlayerCardTabData():
    CardTab: (U32, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    HoverText: (String, 0x0, 0x0, 0x0)
    pass

class ContextualConditionGlobalObjectiveBountyState(IContextualCondition):
    TargetGlobalBountyState: (U8, 0x0, 0x0, 0x0)
    pass

class MissileVisibilitySpec():
    mPerceptionBubbleRadius: (F32, 0x0, 0x0, 0x0)
    mTargetControlsVisibility: (Bool, 0x0, 0x0, 0x0)
    mVisibleToOwnerTeamOnly: (Bool, 0x0, 0x0, 0x0)
    mVisibileToOwnerTeamOnly: (Bool, 0x0, 0x0, 0x0)
    TrailTimeToConsiderForVisibility: (F32, 0x0, 0x0, 0x0)
    pass

class MaterialTextureDataCollection():
    Entries: (Map, String, Embed, IdMappingEntry)
    NextId: (U16, 0x0, 0x0, 0x0)
    Data: (Map, U16, Embed, MaterialTextureData)
    0xea57bf12: (String, 0x0, 0x0, 0x0)
    pass

class VfxPrimitiveBeam(VfxPrimitiveBase):
    mBeam: (Embed, 0x0, 0x0, VfxBeamDefinitionData)
    mMesh: (Embed, 0x0, 0x0, VfxMeshDefinitionData)
    pass

class VfxAnimatedColor(VfxColorBase):
    Values: (List, 0x0, Vec4, 0x0)
    Values: (List2, 0x0, Vec4, 0x0)
    Times: (List, 0x0, F32, 0x0)
    Times: (List2, 0x0, F32, 0x0)
    0x7c9bcfd5: (List, 0x0, U32, 0x0)
    Modes: (List2, 0x0, U8, 0x0)
    ProbabilityTables: (List, 0x4, Pointer, VfxProbabilityTableData)
    pass

class Pawn(GameObject):
    pass

class 0x6897155d(VfxSpawnConditionData):
    0x889e41d1: (Pointer, 0x0, 0x0, 0xc9dd46d2)
    0xea02af5c: (Pointer, 0x0, 0x0, 0x48eb8d47)
    pass

class VectorGet(IVectorGet, IScriptValueGet):
    Value: (Vec3, 0x0, 0x0, 0x0)
    pass

class IBaseParametricUpdater():
    pass

class ValueVector3():
    ConstantValue: (Vec3, 0x0, 0x0, 0x0)
    Dynamics: (Pointer, 0x0, 0x0, VfxVector3fBase)
    Dynamics: (Pointer, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    pass

class SkinUpgradeData():
    mRecallSkinUpgrades: (List, 0x0, Link, RecallSkinUpgrade)
    SkinAugmentCategories: (Embed, 0x0, 0x0, SkinAugmentCategories)
    mSpawnSkinUpgrades: (List, 0x0, Link, SpawnSkinUpgrade)
    mGearSkinUpgrades: (List, 0x0, Link, GearSkinUpgrade)
    mHomeguardSkinUpgrades: (List, 0x0, Link, HomeguardSkinUpgrade)
    pass

class 0x69057401():
    Divider: (Hash, 0x0, 0x0, 0x0)
    TeamName: (Hash, 0x0, 0x0, 0x0)
    TeamBanner: (Hash, 0x0, 0x0, 0x0)
    TeamByeText: (Hash, 0x0, 0x0, 0x0)
    0xf933c90d: (Hash, 0x0, 0x0, 0x0)
    TeamPosition: (Hash, 0x0, 0x0, 0x0)
    pass

class PurchaseDialogBase(ModalDialogViewController):
    PurchaseButton: (Hash, 0x0, 0x0, 0x0)
    StoreDialog: (Hash, 0x0, 0x0, 0x0)
    ResizableBackdrop: (Hash, 0x0, 0x0, 0x0)
    pass

class PlayerAugmentsViewController(PlayerStatsPanelViewController):
    PanelBgAltTop: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    PanelBg: (Hash, 0x0, 0x0, 0x0)
    0x73dd5ab3: (Pointer, 0x0, 0x0, 0x4a7922fb)
    PanelBgAltSide: (Hash, 0x0, 0x0, 0x0)
    ObjectName: (String, 0x0, 0x0, 0x0)
    pass

class UiUnitStatusData():
    StatusIcon: (Hash, 0x0, 0x0, 0x0)
    StatusDurationBarData: (Pointer, 0x0, 0x0, UiUnitStatusDurationBarData)
    StatusText: (Hash, 0x0, 0x0, 0x0)
    NameText: (Hash, 0x0, 0x0, 0x0)
    CenterJustifyStatusIconAndText: (Bool, 0x0, 0x0, 0x0)
    pass

class TftEventHubLargeViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    EventPassThumbnail: (Embed, 0x0, 0x0, 0xbf5c4715)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    EventTimer: (Pointer, 0x0, 0x0, TftEventTimer)
    InfoButton: (Hash, 0x0, 0x0, 0x0)
    0x7d200cc1: (Embed, 0x0, 0x0, 0x61902388)
    MissionScroller: (Embed, 0x0, 0x0, 0xdd8ea5ae)
    0x96dd8579: (Link, 0x0, 0x0, ModalDialogViewController)
    SceneRoot: (Hash, 0x0, 0x0, 0x0)
    CloseButton: (Hash, 0x0, 0x0, 0x0)
    TrovesThumbnail: (Embed, 0x0, 0x0, 0x22dd5ebf)
    0xe5388f19: (Hash, 0x0, 0x0, 0x0)
    pass

class TftTrovesBannerLoadoutReward(TftTrovesBannerReward):
    NameTraKey: (String, 0x0, 0x0, 0x0)
    LoadoutsItem: (Link, 0x0, 0x0, BaseLoadoutData)
    pass

class IMinionWaveBehavior():
    pass

class LoadingScreenRegaliaData():
    CrestBase: (Hash, 0x0, 0x0, 0x0)
    BannerTrim: (Hash, 0x0, 0x0, 0x0)
    PrestigeCrestBase: (Hash, 0x0, 0x0, 0x0)
    RankedCrestBase: (Hash, 0x0, 0x0, 0x0)
    SummonerLevelText: (Hash, 0x0, 0x0, 0x0)
    Addons: (List, 0x3, Hash, 0x0)
    CrestTier: (List, 0x0, Hash, 0x0)
    LoadingScreenRegaliaflags: (I32, 0x0, 0x0, 0x0)
    BannerFlag: (Hash, 0x0, 0x0, 0x0)
    RankedRegaliaLevelText: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x69b74614():
    TooltipOffsetY: (F32, 0x0, 0x0, 0x0)
    TooltipOffsetX: (F32, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    TooltipTitleTra: (String, 0x0, 0x0, 0x0)
    TooltipDescriptionTra: (String, 0x0, 0x0, 0x0)
    pass

class GameModeAutoItemPurchasingConfig():
    mItemGroupToAvoidSellingAndSetCostCeiling: (Hash, 0x0, 0x0, 0x0)
    mMaxPurchaseAttemptsPerSession: (I32, 0x0, 0x0, 0x0)
    mSituationalPurchasedRecItemBlockTypes: (List, 0x0, String, 0x0)
    mRandomlyPurchasedRecItemBlockTypes: (List, 0x0, String, 0x0)
    mSequentiallyPurchasedRecItemBlockTypes: (List, 0x0, String, 0x0)
    pass

class GetGameStartCountdownTime(LevelScriptBlock):
    Dest: (Embed, 0x0, 0x0, FloatTableSet)
    pass

class 0x69cdddcc(TftCutscenePositionProvider):
    HasOffset: (Bool, 0x0, 0x0, 0x0)
    0x1ec4c9b5: (String, 0x0, 0x0, 0x0)
    OffsetVector: (Vec3, 0x0, 0x0, 0x0)
    0x88034173: (String, 0x0, 0x0, 0x0)
    0xcbbb27a5: (Bool, 0x0, 0x0, 0x0)
    Bone: (String, 0x0, 0x0, 0x0)
    pass

class LolSpellScript(GameScript, Rscript):
    CastingBreaksStealth: (Bool, 0x0, 0x0, 0x0)
    PreloadData: (Embed, 0x0, 0x0, LolSpellPreloadData)
    mSequences: (Map, U32, Embed, Sequence)
    mSequences: (Map, U32, Pointer, Sequence)
    0x532c1075: (Bool, 0x0, 0x0, 0x0)
    0x77e82748: (Bool, 0x0, 0x0, 0x0)
    CustomSequences: (Map, Hash, Embed, ScriptSequence)
    CustomSequences: (Map, String, Embed, ScriptSequence)
    IsEnabled: (Bool, 0x0, 0x0, 0x0)
    0xf491308f: (Bool, 0x0, 0x0, 0x0)
    GlobalProperties: (Embed, 0x0, 0x0, ScriptGlobalProperties)
    Sequences: (Map, Hash, Embed, ScriptSequence)
    Sequences: (Map, U32, Embed, ScriptSequence)
    pass

class ValueVector2():
    ConstantValue: (Vec2, 0x0, 0x0, 0x0)
    Dynamics: (Pointer, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    Dynamics: (Pointer, 0x0, 0x0, VfxVector2fBase)
    pass

class GdsMapObjectBannerInfo(GdsMapObjectExtraInfo):
    BannerData: (Link, 0x0, 0x0, BannerData)
    BannerData: (Link, 0x0, 0x0, EsportsBannerData)
    pass

class RegaliaLookup():
    RegaliaTrim: (Link, 0x0, 0x0, RegaliaData)
    RegaliaCrest: (Link, 0x0, 0x0, RegaliaData)
    Tier: (String, 0x0, 0x0, 0x0)
    RegaliaCrown1: (Link, 0x0, 0x0, RegaliaData)
    RegaliaCrown3: (Link, 0x0, 0x0, RegaliaData)
    RegaliaCrown2: (Link, 0x0, 0x0, RegaliaData)
    RegaliaCrown4: (Link, 0x0, 0x0, RegaliaData)
    RegaliaSplit2: (Link, 0x0, 0x0, RegaliaData)
    RegaliaSplit3: (Link, 0x0, 0x0, RegaliaData)
    RegaliaSplit1: (Link, 0x0, 0x0, RegaliaData)
    pass

class UiMetricLaneMinionIncreasedMoveSpeed(UiMetricLaneMinionI):
    pass

class IsMovingBoolDriver(ILogicBoolDriver):
    pass

class MapBakeProperties(MapComponent, 0x8e8282a9):
    LightgridOverallScale: (F32, 0x0, 0x0, 0x0)
    LightgridScaleBounceContribution: (F32, 0x0, 0x0, 0x0)
    LightGridSize: (U32, 0x0, 0x0, 0x0)
    LightGridCharacterFullBrightIntensity: (F32, 0x0, 0x0, 0x0)
    LightGridCharacterIntensity: (F32, 0x0, 0x0, 0x0)
    LightGridFileName: (String, 0x0, 0x0, 0x0)
    RmaStaticLightGridIntensityScale: (F32, 0x0, 0x0, 0x0)
    RmaStaticLightGridTexturePath: (String, 0x0, 0x0, 0x0)
    0xbc248312: (Bool, 0x0, 0x0, 0x0)
    LightgridBounceFalloffDistance: (F32, 0x0, 0x0, 0x0)
    StationaryLightChannelAssignments: (Map, Hash, U8, 0x0)
    pass

class TftCompanionEvolutionViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    Buttons: (List, 0x0, Hash, 0x0)
    BaseBinName: (String, 0x0, 0x0, 0x0)
    MetadataTagToDetect: (String, 0x0, 0x0, 0x0)
    pass

class SetTargetableBlock(IScriptBlock):
    Value: (Pointer, 0x0, 0x0, IBoolGet)
    pass

class 0x6a68b4f1():
    Victory: (Hash, 0x0, 0x0, 0x0)
    Defeat: (Hash, 0x0, 0x0, 0x0)
    Bye: (Hash, 0x0, 0x0, 0x0)
    DefeatFx: (Hash, 0x0, 0x0, 0x0)
    ByeFx: (Hash, 0x0, 0x0, 0x0)
    FightingFx: (Hash, 0x0, 0x0, 0x0)
    VictoryFx: (Hash, 0x0, 0x0, 0x0)
    Fighting: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x6a694f75(IFxAction):
    pass

class 0x6a6e3b03():
    pass

class ReplayControlsButton():
    Button: (Hash, 0x0, 0x0, 0x0)
    DefaultTooltipKey: (String, 0x0, 0x0, 0x0)
    SelectedTooltipKey: (String, 0x0, 0x0, 0x0)
    HotkeyEventString: (String, 0x0, 0x0, 0x0)
    pass

class MultiPullStandardItemData():
    ItemTemplate: (Hash, 0x0, 0x0, 0x0)
    LegendaryVfx: (Hash, 0x0, 0x0, 0x0)
    Parent: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxMeshDefinitionData():
    mAnimationVariants: (List, 0x0, String, 0x0)
    mMeshName: (String, 0x0, 0x0, 0x0)
    mMeshSkeletonName: (String, 0x0, 0x0, 0x0)
    mSubmeshesToDrawAlways: (List, 0x0, Hash, 0x0)
    mSubmeshesToDrawAlways: (List, 0x0, U32, 0x0)
    mSimpleMeshName: (String, 0x0, 0x0, 0x0)
    mSubmeshesToDraw: (List, 0x0, Hash, 0x0)
    mSubmeshesToDraw: (List, 0x0, U32, 0x0)
    mLockMeshToAttachment: (Bool, 0x0, 0x0, 0x0)
    mAnimationName: (String, 0x0, 0x0, 0x0)
    pass

class 0x6a97ad3(ILogicVector3Driver):
    pass

class OptionItemSecondaryHotkeys2Column(IOptionItem):
    Rows: (List, 0x0, Embed, OptionItemSecondaryHotkeys2Column_Row)
    Template: (Hash, 0x0, 0x0, 0x0)
    Header: (Embed, 0x0, 0x0, OptionItemSecondaryHotkeys2Column_Header)
    pass

class TftFloatingInfoBarViewController(FloatingInfoBarViewController):
    pass

class TftTraitInfoCardViewController(ViewController):
    TraitTrackerAnchor: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    TraitTooltipTopHandle: (Hash, 0x0, 0x0, 0x0)
    TraitTooltipTopIcon: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    UnitPortraitSection: (Pointer, 0x0, 0x0, TftHudTraitUnitPortraitSection)
    TraitName: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    0x6de5e0b8: (Map, U8, Pointer, TftTraitInfoCard)
    TraitIcon: (Hash, 0x0, 0x0, 0x0)
    SceneRegion: (Hash, 0x0, 0x0, 0x0)
    ResizableBackdrop: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideBinName: (String, 0x0, 0x0, 0x0)
    UnitInfoTraitAnchor: (Hash, 0x0, 0x0, 0x0)
    TraitDescription: (Hash, 0x0, 0x0, 0x0)
    UnitInfoCardAnchor: (Hash, 0x0, 0x0, 0x0)
    BaseBinName: (String, 0x0, 0x0, 0x0)
    TraitTooltipTopName: (Hash, 0x0, 0x0, 0x0)
    pass

class IdentityInstance():
    Id: (String, 0x0, 0x0, 0x0)
    OfferId: (String, 0x0, 0x0, 0x0)
    mItemTexturePath: (String, 0x0, 0x0, 0x0)
    ItemVfx: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    pass

class HasBuffRequirement(ISpellRankUpRequirement):
    mBuffName: (Hash, 0x0, 0x0, 0x0)
    mFromAnyone: (Bool, 0x0, 0x0, 0x0)
    pass

class AttackSlotData():
    mAttackName: (Option, 0x0, String, 0x0)
    mOverrideAutoattackCastTime: (Pointer, 0x0, 0x0, OverrideAutoAttackCastTimeData)
    mAttackCastTime: (Option, 0x0, F32, 0x0)
    mAttackProbability: (Option, 0x0, F32, 0x0)
    mAttackDelayOffsetPercent: (Option, 0x0, F32, 0x0)
    mAttackTotalTime: (Option, 0x0, F32, 0x0)
    mAttackDelayCastOffsetPercentAttackSpeedRatio: (Option, 0x0, F32, 0x0)
    mAttackDelayCastOffsetPercent: (Option, 0x0, F32, 0x0)
    pass

class IsOptionEnabledBoolDriver(ILogicBoolDriver):
    Option: (U16, 0x0, 0x0, 0x0)
    pass

class ScriptBtContext(ScriptContext):
    pass

class AndScriptCondition(IScriptCondition):
    Conditions: (List, 0x0, Pointer, IScriptCondition)
    pass

class LolModesSubphaseData():
    Duration: (F32, 0x0, 0x0, 0x0)
    FlashOnTimeRemaining: (F32, 0x0, 0x0, 0x0)
    Type: (U8, 0x0, 0x0, 0x0)
    TimerBarDefaultColor: (Color, 0x0, 0x0, 0x0)
    SecondFlashOnTimeRemaining: (F32, 0x0, 0x0, 0x0)
    0xa42117a5: (List2, 0x0, Link, 0xc10d4fdc)
    TimerBarColor: (Color, 0x0, 0x0, 0x0)
    pass

class SequenceType():
    Name: (String, 0x0, 0x0, 0x0)
    Hash: (Hash, 0x0, 0x0, 0x0)
    pass

class MissileMovementSpec():
    mTracksTarget: (Bool, 0x0, 0x0, 0x0)
    mTargetHeightAugment: (F32, 0x0, 0x0, 0x0)
    mTargetBoneName: (String, 0x0, 0x0, 0x0)
    mStartBoneSkinOverrides: (Map, U32, String, 0x0)
    mStartDelay: (F32, 0x0, 0x0, 0x0)
    mVisualsTrackHiddenTargets: (Bool, 0x0, 0x0, 0x0)
    mStartBoneName: (String, 0x0, 0x0, 0x0)
    mUseHeightOffsetAtEnd: (Bool, 0x0, 0x0, 0x0)
    mOffsetInitialTargetHeight: (F32, 0x0, 0x0, 0x0)
    pass

class SpellDataValueVector():
    SpellDataValues: (List, 0x0, Embed, SpellDataValue)
    pass

class 0x6b37502b():
    SpeciesIds: (List2, 0x0, U32, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class 0x6b3ef1bd(IGameModeConfig):
    SurrenderVoteCompleteDialogPersistsSec: (F32, 0x0, 0x0, 0x0)
    SurrenderAfkAutoVoteThresholdSec: (F32, 0x0, 0x0, 0x0)
    SurrenderRetryDelaySec: (F32, 0x0, 0x0, 0x0)
    TeamSurrenderVoterCount: (U32, 0x0, 0x0, 0x0)
    0x9077ce38: (F32, 0x0, 0x0, 0x0)
    SurrenderVoteDurationSec: (F32, 0x0, 0x0, 0x0)
    SurrenderVoteCompleteEliminateDelaySec: (F32, 0x0, 0x0, 0x0)
    pass

class ScriptBtFailure(IScriptSequence):
    Blocks: (List2, 0x0, Pointer, IScriptBlock)
    pass

class TftBlendedLinearHeightSolver(TftHeightSolverType):
    pass

class 0x6b6ada59(IScriptBlock, IBehaviorScriptBlock):
    pass

class MinimapPingEffectDefinition():
    StartDelay: (F32, 0x0, 0x0, 0x0)
    RepeatCount: (U32, 0x0, 0x0, 0x0)
    ScaleSpeed: (F32, 0x0, 0x0, 0x0)
    ScaleStart: (F32, 0x0, 0x0, 0x0)
    BlendWithAlpha: (Bool, 0x0, 0x0, 0x0)
    AlphaStart: (U32, 0x0, 0x0, 0x0)
    OnDeathFadeSpeed: (F32, 0x0, 0x0, 0x0)
    Life: (F32, 0x0, 0x0, 0x0)
    AlphaFadeSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class 0x6b863734(IMapVisibilityController):
    VisFlags: (U8, 0x0, 0x0, 0x0)
    pass

class 0x6b91544a(IGameModeConfigClient):
    0x46edf5aa: (F32, 0x0, 0x0, 0x0)
    BlurTextures: (Bool, 0x0, 0x0, 0x0)
    FadeInRate: (F32, 0x0, 0x0, 0x0)
    BlurKernelSigma: (F32, 0x0, 0x0, 0x0)
    VfxSystems: (List2, 0x0, Embed, VfxPrimitiveCameraSegmentSeriesBeam)
    VfxSystems: (Map, Hash, Link, VfxSystemDefinitionData)
    FadeOutRate: (F32, 0x0, 0x0, 0x0)
    UpscaleTextures: (Bool, 0x0, 0x0, 0x0)
    pass

class ReciprocityConfigData():
    UseCharacter: (Bool, 0x0, 0x0, 0x0)
    CharacterOffset: (Vec3, 0x0, 0x0, 0x0)
    0x289c2d47: (F32, 0x0, 0x0, 0x0)
    0x376cc7a8: (F32, 0x0, 0x0, 0x0)
    CharacterName: (String, 0x0, 0x0, 0x0)
    DecayTimer: (F32, 0x0, 0x0, 0x0)
    0x804e130b: (F32, 0x0, 0x0, 0x0)
    0x8c0e1f6b: (Color, 0x0, 0x0, 0x0)
    0x9783708b: (F32, 0x0, 0x0, 0x0)
    CooldownTimer: (F32, 0x0, 0x0, 0x0)
    pass

class TextGimmeDataInstance():
    ValueDriver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    LocalizedTextFormat: (String, 0x0, 0x0, 0x0)
    TextFormat: (String, 0x0, 0x0, 0x0)
    TextElement: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x6bbc3db6(0x288b8edc):
    SpellObjects: (List, 0x4, Link, SpellObject)
    0xda28e4c: (Color, 0x0, 0x0, 0x0)
    pass

class IntegratedValueVector2(ValueVector2):
    pass

class ParBarPercentParametricUpdater(IFloatParametricUpdater):
    pass

class ShData():
    BandData: (List, 0x9, Vec3, 0x0)
    pass

class InvalidDeviceViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    pass

class LoadoutScript(Rscript):
    Sequences: (Map, U32, Embed, ScriptSequence)
    pass

class UiButtonAdditionalState():
    DisplayElements: (List, 0x0, Link, BaseElementData)
    pass

class UiButtonDefinition():
    DefaultStateElements: (Embed, 0x0, 0x0, UiButtonState)
    ObjectPath: (Hash, 0x0, 0x0, 0x0)
    SelectedStateElements: (Embed, 0x0, 0x0, UiButtonState)
    InactiveTooltipTraKey: (String, 0x0, 0x0, 0x0)
    SelectedClickedStateElements: (Embed, 0x0, 0x0, UiButtonState)
    HitRegionElement: (Link, 0x0, 0x0, RegionElementData)
    InactiveStateElements: (Embed, 0x0, 0x0, UiButtonState)
    ClickReleaseParticleElement: (Link, 0x0, 0x0, ParticleSystemElementData)
    ActiveTooltipTraKey: (String, 0x0, 0x0, 0x0)
    SoundEvents: (Pointer, 0x0, 0x0, UiButtonSoundEvents)
    ClickedStateElements: (Embed, 0x0, 0x0, UiButtonState)
    SelectedHoverStateElements: (Embed, 0x0, 0x0, UiButtonState)
    HoverStateElements: (Embed, 0x0, 0x0, UiButtonState)
    TextTraKey: (String, 0x0, 0x0, 0x0)
    pass

class 0x6c7a6a03():
    pass

class IsMovingParametricUpdater(IBooleanParametricUpdater):
    pass

class TftMapCharacterLists():
    MapName: (String, 0x0, 0x0, 0x0)
    CharacterLists: (List, 0x0, Embed, TftMapCharacterList)
    CharacterLists: (List2, 0x0, Embed, TftMapCharacterList)
    pass

class 0x6c84152e():
    ForVote: (Hash, 0x0, 0x0, 0x0)
    AgainstVote: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x6ca013c9(IFxActionInstance):
    pass

class 0x6ca3cfd():
    pass

class DelayInputSourceBool(IInputSourceBool):
    Source: (Pointer, 0x0, 0x0, IInputSourceBool)
    DelayTurningOff: (F32, 0x0, 0x0, 0x0)
    DelayTurningOn: (F32, 0x0, 0x0, 0x0)
    pass

class TftEliminationViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    VictoryHighlightVfx: (Hash, 0x0, 0x0, 0x0)
    WaitingHighlightVfx: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    EliminationHighlightVfx: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    LeaveButton: (Hash, 0x0, 0x0, 0x0)
    SpectateButton: (Hash, 0x0, 0x0, 0x0)
    RankText: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class IntegratedValueVector3(ValueVector3):
    pass

class MapActionFollowPath(MapAction):
    Pathname: (String, 0x0, 0x0, 0x0)
    Duration: (F32, 0x0, 0x0, 0x0)
    Velocity: (F32, 0x0, 0x0, 0x0)
    UseVelocityOverDuration: (Bool, 0x0, 0x0, 0x0)
    TargetName: (String, 0x0, 0x0, 0x0)
    RotateWithSpline: (Bool, 0x0, 0x0, 0x0)
    pass

class SceneScreenEdgeTransitionData(SceneBaseTransitionData):
    Edge: (U8, 0x0, 0x0, 0x0)
    pass

class 0x6cfd4c2(IBehaviorScriptBlock):
    pass

class ConfigBool():
    Enabler: (Link, 0x0, 0x0, IEnabler)
    Value: (Bool, 0x0, 0x0, 0x0)
    pass

class SetBit(IScriptBlock):
    BitIndex: (Pointer, 0x0, 0x0, IIntGet)
    BitField: (Embed, 0x0, 0x0, IntTableSet)
    pass

class LoginViewController(ViewController):
    LoginProviderButtonMapping: (List, 0x0, Embed, TftMobileLoginButtonData)
    LoginProviderButtonMapping: (List2, 0x0, Embed, TftMobileLoginButtonData)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    LoginQueueData: (Embed, 0x0, 0x0, TftMobileLoginQueueData)
    0x60a8380: (Map, U32, Hash, 0x0)
    LoginData: (Embed, 0x0, 0x0, TftMobileLoginData)
    ButtonLayout: (Hash, 0x0, 0x0, 0x0)
    BuildVersionText: (Hash, 0x0, 0x0, 0x0)
    LoginLogoMapping: (Map, U32, Hash, 0x0)
    Buttons: (List, 0x4, Hash, 0x0)
    Buttons: (List, 0x5, Hash, 0x0)
    LoginProviderButtons: (List, 0x5, Hash, 0x0)
    pass

class ILevelController():
    Guid: (String, 0x0, 0x0, 0x0)
    0x3749ad96: (Hash, 0x0, 0x0, 0x0)
    pass

class JunglePath():
    RecommendationIcons: (List, 0x0, Embed, RecommendedJunglePathIcons)
    pass

class VectorOffsetTableGet(IVectorGet):
    Offset: (Vec3, 0x0, 0x0, 0x0)
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Table: (Pointer, 0x0, 0x0, RsTable)
    Var: (String, 0x0, 0x0, 0x0)
    pass

class LoadingScreenRankedFrames():
    DefaultFrame: (Hash, 0x0, 0x0, 0x0)
    ChaosFrame: (Hash, 0x0, 0x0, 0x0)
    FrameElementMap: (Map, String, Hash, 0x0)
    OrderFrame: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x6d8274d(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    EyeCandy: (Bool, 0x0, 0x0, 0x0)
    Loadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    SceneTransitionElements: (Embed, 0x0, 0x0, UiElementToggle)
    pass

class DefaultVerticalFacing(VerticalFacingType):
    pass

class SelectorPairData():
    mProbability: (F32, 0x0, 0x0, 0x0)
    mClipName: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x6d8a849f(IFxActionInstance):
    pass

class PurchaseDialogSubPurchaseElements():
    SubPurchaseIconFrame: (Hash, 0x0, 0x0, 0x0)
    SubPurchaseTitle: (Hash, 0x0, 0x0, 0x0)
    SubPurchaseGroup: (Hash, 0x0, 0x0, 0x0)
    SubPurchaseDesc: (Hash, 0x0, 0x0, 0x0)
    SubPurchaseIcon: (Hash, 0x0, 0x0, 0x0)
    SubPurchaseDivider: (Hash, 0x0, 0x0, 0x0)
    pass

class TftHudStageData():
    0xa11246b8: (F32, 0x0, 0x0, 0x0)
    pass

class 0x6db4b328():
    mDropRatesByLevel: (List, 0x0, Embed, TftShopDropRates)
    pass

class GetFloatOptionFloatDriver(ILogicFloatDriver):
    Option: (U16, 0x0, 0x0, 0x0)
    pass

class MapProjectedTexture(MapFrustum):
    ProjectedTexture: (String, 0x0, 0x0, 0x0)
    AdditionalTextures: (Map, U32, String, 0x0)
    FalloffTexture: (String, 0x0, 0x0, 0x0)
    pass

class 0x6de4753e():
    SkillLevels: (List2, 0x0, Embed, 0xffcac16f)
    pass

class 0x6de65881(TableValue):
    pass

class InfoNubData():
    pass

class AugmentData(IAugment):
    RootSpell: (Link, 0x0, 0x0, SpellObject)
    AugmentNameId: (String, 0x0, 0x0, 0x0)
    NameTra: (String, 0x0, 0x0, 0x0)
    Enabled: (Bool, 0x0, 0x0, 0x0)
    AugmentTooltipTra: (String, 0x0, 0x0, 0x0)
    AugmentSmallIconPath: (String, 0x0, 0x0, 0x0)
    Rarity: (U8, 0x0, 0x0, 0x0)
    mBuildTags: (U32, 0x0, 0x0, 0x0)
    AugmentPlatformId: (I32, 0x0, 0x0, 0x0)
    TooltipTra: (String, 0x0, 0x0, 0x0)
    AugmentDisplayTags: (List, 0x0, U32, 0x0)
    mAugmentTags: (U32, 0x0, 0x0, 0x0)
    AugmentLargeIconPath: (String, 0x0, 0x0, 0x0)
    DescriptionTra: (String, 0x0, 0x0, 0x0)
    pass

class HeroFloatingInfoBorderDefenseIconThresholdData():
    ArmorIcon: (Hash, 0x0, 0x0, 0x0)
    ComboIcon: (Hash, 0x0, 0x0, 0x0)
    MagicResistIcon: (Hash, 0x0, 0x0, 0x0)
    DefenseModifierThreshold: (F32, 0x0, 0x0, 0x0)
    pass

class TftHudScoreboardData():
    mWinStreakLevel2LoopStartDelaySecs: (F32, 0x0, 0x0, 0x0)
    mWinStreakLevel1LoopStartDelaySecs: (F32, 0x0, 0x0, 0x0)
    mCombatStateSlideInTimeSecs: (F32, 0x0, 0x0, 0x0)
    pass

class UiMetricVisionScore(UiMetricTypeSimpleI):
    pass

class BuffStackingSettings():
    TemplateDefinition: (List, 0x0, Embed, BuffStackingTemplate)
    pass

class MissileRenderSpec():
    DrawType: (U32, 0x0, 0x0, 0x0)
    pass

class SurrenderViewController(VotePanelViewController):
    EarlyText: (Hash, 0x0, 0x0, 0x0)
    RemakeText: (Hash, 0x0, 0x0, 0x0)
    DefaultText: (Hash, 0x0, 0x0, 0x0)
    pass

class UiTeamIdentityData():
    LogoLink: (Hash, 0x0, 0x0, 0x0)
    NameLink: (Hash, 0x0, 0x0, 0x0)
    TagLink: (Hash, 0x0, 0x0, 0x0)
    pass

class RegionElementData(UiElementData, BaseElementData):
    pass

class LogicDriverButtonViewController(LogicDriverViewController):
    0xc7e51dac: (List2, 0x0, Embed, 0x26949c34)
    pass

class MapPathCurveSegment(MapPathSegment):
    ControlPoint1: (Vec3, 0x0, 0x0, 0x0)
    ControlPoint2: (Vec3, 0x0, 0x0, 0x0)
    pass

class UiItemSelectionSlotData():
    Button: (Hash, 0x0, 0x0, 0x0)
    ItemIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class DelayStart(MissileBehaviorSpec):
    mDelayTime: (F32, 0x0, 0x0, 0x0)
    pass

class NotificationsViewController(ViewController):
    pass

class AugmentSlot():
    PenetrationRecently: (Hash, 0x0, 0x0, 0x0)
    AugmentGridItem: (Hash, 0x0, 0x0, 0x0)
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    HitArea: (Hash, 0x0, 0x0, 0x0)
    0xbbebf3d: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionSpellLevel(IContextualConditionSpell, IContextualCondition):
    mCompareOp: (U8, 0x0, 0x0, 0x0)
    mSpellLevel: (U8, 0x0, 0x0, 0x0)
    pass

class Obj_LevelSizer(BuildingClient):
    pass

class 0x6f31ebae(IScriptBlock, IBehaviorScriptBlock):
    Sequence: (Embed, 0x0, 0x0, ScriptBtSequence)
    pass

class TftTraitData():
    mName: (String, 0x0, 0x0, 0x0)
    ShowTraitContribution: (Bool, 0x0, 0x0, 0x0)
    InnateTraitSets: (List, 0x0, Embed, TftBaseTraitSetData)
    0x741575c2: (String, 0x0, 0x0, 0x0)
    mDescriptionNameTra: (String, 0x0, 0x0, 0x0)
    TraitType: (U8, 0x0, 0x0, 0x0)
    mIconPath: (String, 0x0, 0x0, 0x0)
    IconDisplayStyle: (U32, 0x0, 0x0, 0x0)
    mConditionalTraitSets: (List, 0x0, Embed, TftConditionalTraitSetData)
    TraitProgressionDisplay: (U8, 0x0, 0x0, 0x0)
    mTraitSets: (List, 0x0, Embed, TftTraitSetData)
    VfxResourceResolver: (Link, 0x0, 0x0, ResourceResolver)
    mDisplayNameIcon: (String, 0x0, 0x0, 0x0)
    mDisplayNameTra: (String, 0x0, 0x0, 0x0)
    mId: (U32, 0x0, 0x0, 0x0)
    ActiveIconColor: (Color, 0x0, 0x0, 0x0)
    mUnitSectionTra: (String, 0x0, 0x0, 0x0)
    Keywords: (List2, 0x0, Hash, 0x0)
    pass

class 0x6f9b77c6():
    TftBattlepassLevels: (List2, 0x0, Embed, 0x1d54119c)
    MinimumVersionForContent: (String, 0x0, 0x0, 0x0)
    Id: (String, 0x0, 0x0, 0x0)
    AssetListId: (String, 0x0, 0x0, 0x0)
    PremiumTitleTraKey: (String, 0x0, 0x0, 0x0)
    PassItemId: (U32, 0x0, 0x0, 0x0)
    TitleTrakey: (String, 0x0, 0x0, 0x0)
    pass

class FxActionMoveReset(FxActionMoveBase):
    pass

class SpellLevelUpUiData():
    EvoIcon: (Hash, 0x0, 0x0, 0x0)
    ButtonFxOutSelected: (Hash, 0x0, 0x0, 0x0)
    ButtonPostFxIn: (Hash, 0x0, 0x0, 0x0)
    AbilityFxIn: (Hash, 0x0, 0x0, 0x0)
    ButtonIdleGlowFx: (Hash, 0x0, 0x0, 0x0)
    ButtonFxOutUnselected: (Hash, 0x0, 0x0, 0x0)
    ButtonIdleSheenFx: (Hash, 0x0, 0x0, 0x0)
    Evolution: (Pointer, 0x0, 0x0, SpellEvolutionUiData)
    SkillUpButton: (Hash, 0x0, 0x0, 0x0)
    EvolveButton: (Hash, 0x0, 0x0, 0x0)
    ButtonFxIn: (Hash, 0x0, 0x0, 0x0)
    pass

class TeamFightViewController(ViewController):
    OffscreenDifferentiation: (Pointer, 0x0, 0x0, UiTeamFightOffScreenDifferentiationData)
    TooltipPosition: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    ResizingBackdrop: (Hash, 0x0, 0x0, 0x0)
    SceneTransition: (Embed, 0x0, 0x0, HudMenuTransitionData)
    ObjectName: (String, 0x0, 0x0, 0x0)
    ParentScene: (Hash, 0x0, 0x0, 0x0)
    TeamData: (List, 0x2, Embed, UiTeamFightTeamData)
    pass

class MaterialDataCollections():
    ParameterData: (Embed, 0x0, 0x0, MaterialParameterDataCollection)
    SwitchData: (Embed, 0x0, 0x0, MaterialSwitchDataCollection)
    SamplerData: (Embed, 0x0, 0x0, MaterialSamplerDataCollection)
    TextureData: (Embed, 0x0, 0x0, MaterialTextureDataCollection)
    pass

class LuaPropertyDataFloatArray(LuaPropertyData):
    Values: (List, 0x0, F32, 0x0)
    pass

class VectorDefaultTableGet(IVectorGet):
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Table: (Pointer, 0x0, 0x0, RsTable)
    Var: (String, 0x0, 0x0, 0x0)
    Default: (Vec3, 0x0, 0x0, 0x0)
    pass

class SpellSlotBasicUiDefinition():
    ContentElement: (Hash, 0x0, 0x0, 0x0)
    MouseoverRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class IsTurningParametricUpdater(IBooleanParametricUpdater):
    pass

class TftUnitPropertyDefinition():
    IsCloneable: (Bool, 0x0, 0x0, 0x0)
    CombinationRule: (U32, 0x0, 0x0, 0x0)
    Lifetime: (U32, 0x0, 0x0, 0x0)
    DefaultValue: (Pointer, 0x0, 0x0, TftUnitPropertyValue)
    ReplicationRule: (U32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class UnitFloatingInfoBarData(FloatingInfoBarData):
    DeathAnimAlly: (Hash, 0x0, 0x0, 0x0)
    Highlight: (Hash, 0x0, 0x0, 0x0)
    Border: (Hash, 0x0, 0x0, 0x0)
    Aggro: (Hash, 0x0, 0x0, 0x0)
    ObjectiveBountyAlly: (Hash, 0x0, 0x0, 0x0)
    ObjectiveBountyEnemy: (Hash, 0x0, 0x0, 0x0)
    DeathAnimEnemy: (Hash, 0x0, 0x0, 0x0)
    Healthbar: (Embed, 0x0, 0x0, HealthBarData)
    ParBar: (Pointer, 0x0, 0x0, AbilityResourceBarData)
    Icons: (Pointer, 0x0, 0x0, HeroFloatingInfoIconsData)
    pass

class VectorArrayTableSet(ScriptTableSet):
    pass

class 0x70670a5f(0x7546469c):
    pass

class AiTurretCommon(AiBaseClient):
    pass

class SwapChampionCheat(Cheat):
    pass

class 0x7084628f(0x18871c61):
    CustomAnnouncementStyle: (Link, 0x0, 0x0, AnnouncementStyleBasic)
    pass

class HudStatStoneDeathRecapData():
    0x24dcd885: (F32, 0x0, 0x0, 0x0)
    MinDisplayTime: (F32, 0x0, 0x0, 0x0)
    mChampIconNativeOffset: (F32, 0x0, 0x0, 0x0)
    mDeathRecapMinDisplayTime: (F32, 0x0, 0x0, 0x0)
    MaxDisplayTime: (F32, 0x0, 0x0, 0x0)
    mDeathRecapTransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    DeathRecapTransitionOut: (Embed, 0x0, 0x0, HudMenuTransitionData)
    DetailsTransitionData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mDeathRecapMaxDisplayTime: (F32, 0x0, 0x0, 0x0)
    mDeathRecapTransitionOut: (Embed, 0x0, 0x0, HudMenuTransitionData)
    0xaab9e2ea: (Embed, 0x0, 0x0, HudMenuTransitionData)
    DeathRecapTransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    pass

class 0x709bc2e4():
    0xa9db704: (List2, 0x0, Embed, 0x87ef793c)
    pass

class TableValueExistsScriptCondition(IScriptCondition):
    TableValue: (Embed, 0x0, 0x0, ScriptTableGet)
    pass

class HudLoadingScreenWidgetMapInfo(IHudLoadingScreenWidget):
    pass

class GameCalculationModified(IGameCalculation):
    mModifiedGameCalculation: (Hash, 0x0, 0x0, 0x0)
    mOverrideSpellLevel: (Option, 0x0, I32, 0x0)
    pass

class TftCraftingViewController(ViewController):
    CraftingContinueButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    DescriptionText: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    CraftingSequence: (Link, 0x0, 0x0, Sequence)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    DisabledText: (Hash, 0x0, 0x0, 0x0)
    PriceText: (Hash, 0x0, 0x0, 0x0)
    ContentScene: (Hash, 0x0, 0x0, 0x0)
    0xbcbb9921: (Hash, 0x0, 0x0, 0x0)
    ConfirmButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    BackgroundMissingTexture: (Hash, 0x0, 0x0, 0x0)
    NameText: (Hash, 0x0, 0x0, 0x0)
    BackgroundTexture: (Hash, 0x0, 0x0, 0x0)
    pass

class FloatLiteralMaterialDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    mValue: (F32, 0x0, 0x0, 0x0)
    pass

class IsInTerrainParametricUpdater(IBooleanParametricUpdater):
    pass

class StoreInstanceData(InstanceDataBase):
    StoreCategory: (U32, 0x0, 0x0, 0x0)
    StoreData: (Link, 0x0, 0x0, StoreListingData)
    ForegroundVfx: (Embed, 0x0, 0x0, TextureOverride)
    BackgroundVfx: (Embed, 0x0, 0x0, TextureOverride)
    pass

class JointOrientationEventData(BaseEventData):
    OrientationType: (U8, 0x0, 0x0, 0x0)
    OrientationSource: (Pointer, 0x0, 0x0, ILogicVector3Driver)
    pass

class TransitionClipData():
    mTransitionToList: (List, 0x0, Embed, TransitionToData)
    mFromAnimId: (U32, 0x0, 0x0, 0x0)
    pass

class ContextualConditionCustomTimer(IContextualCondition):
    mCustomTimer: (F32, 0x0, 0x0, 0x0)
    pass

class IFunctionalScriptBlock(IScriptBlock):
    pass

class AtlasData(AtlasDataBase, IUiEffectTextureDataProvider):
    mTextureUv: (Vec4, 0x0, 0x0, 0x0)
    mTextureSourceResolutionHeight: (U16, 0x0, 0x0, 0x0)
    mTextureSourceResolutionHeight: (U32, 0x0, 0x0, 0x0)
    mTextureSourceResolutionWidth: (U16, 0x0, 0x0, 0x0)
    mTextureSourceResolutionWidth: (U32, 0x0, 0x0, 0x0)
    mTextureName: (String, 0x0, 0x0, 0x0)
    pass

class GlobalPerLevelStatsFactor():
    mPerLevelStatsFactor: (List, 0x0, F32, 0x0)
    pass

class 0x71e690a9(ClipBaseData):
    mUpdaterType: (U32, 0x0, 0x0, 0x0)
    mPlayAnimChangeFromBeginning: (Bool, 0x0, 0x0, 0x0)
    mChangeAnimationMidPlay: (Bool, 0x0, 0x0, 0x0)
    DontStompTransitionClip: (Bool, 0x0, 0x0, 0x0)
    SyncFrameOnChangeAnim: (Bool, 0x0, 0x0, 0x0)
    mChildAnimDelaySwitchTime: (F32, 0x0, 0x0, 0x0)
    0xe526b8f4: (List, 0x0, Embed, 0x7e59037)
    pass

class ISkinAugment(BaseLoadoutData):
    pass

class EffectAnimationElementData(EffectElementData):
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    mLooping: (Bool, 0x0, 0x0, 0x0)
    0x750db24a: (F32, 0x0, 0x0, 0x0)
    NumberOfFramesPerRowInAtlas: (F32, 0x0, 0x0, 0x0)
    TotalNumberOfFrames: (F32, 0x0, 0x0, 0x0)
    0xd6b0a60b: (F32, 0x0, 0x0, 0x0)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFinishBehavior: (U8, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    0xf346b010: (F32, 0x0, 0x0, 0x0)
    FramesPerSecond: (F32, 0x0, 0x0, 0x0)
    pass

class HasGearDynamicMaterialBoolDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    mGearIndex: (U8, 0x0, 0x0, 0x0)
    pass

class FloatCast(ScriptTableGet, IFloatGet):
    pass

class 0x72553f91():
    Enabled: (Bool, 0x0, 0x0, 0x0)
    0x52b59840: (Bool, 0x0, 0x0, 0x0)
    0x6b2944: (Bool, 0x0, 0x0, 0x0)
    SpeakerIcon: (Hash, 0x0, 0x0, 0x0)
    ShowCountdown: (Bool, 0x0, 0x0, 0x0)
    TitleTra: (String, 0x0, 0x0, 0x0)
    TimeLength: (F32, 0x0, 0x0, 0x0)
    DescriptionTra: (String, 0x0, 0x0, 0x0)
    pass

class TurnAngleRemainingParametricUpdater(IFloatParametricUpdater):
    pass

class DeathRecapViewController(ViewController):
    DamagersCondensedView: (Embed, 0x0, 0x0, DeathRecapDamagerCondensedList)
    DamagerDetailedLayout: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    MinimumScale: (F32, 0x0, 0x0, 0x0)
    ToggleButton: (Hash, 0x0, 0x0, 0x0)
    CondensedScene: (Hash, 0x0, 0x0, 0x0)
    ShowcaseView: (Embed, 0x0, 0x0, DeathRecapShowcase)
    DamageOverview: (Embed, 0x0, 0x0, DeathRecapDamageOverview)
    DamagerDetailedTemplate: (Embed, 0x0, 0x0, DeathRecapDamagerDetailedDisplayData)
    DetailsScene: (Hash, 0x0, 0x0, 0x0)
    MaximumScale: (F32, 0x0, 0x0, 0x0)
    pass

class RerollButtonData():
    RerollButtonText: (Hash, 0x0, 0x0, 0x0)
    RerollButtonTextDisabledColor: (Color, 0x0, 0x0, 0x0)
    RerollButton: (Hash, 0x0, 0x0, 0x0)
    RerollButtonTextColor: (Color, 0x0, 0x0, 0x0)
    pass

class BaseResourceResolver(IResourceResolver):
    ResourceMap: (Map, Hash, Link, IResource)
    pass

class MissionAsset():
    mIconTexturePath: (String, 0x0, 0x0, 0x0)
    mInternalName: (String, 0x0, 0x0, 0x0)
    IconNeedsFrame: (Bool, 0x0, 0x0, 0x0)
    pass

class TargeterDefinitionMultiAoe(TargeterDefinition):
    AngelOffsetRadian: (F32, 0x0, 0x0, 0x0)
    OverrideMinCastRange: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    InnerTextureName: (String, 0x0, 0x0, 0x0)
    RightTextureName: (String, 0x0, 0x0, 0x0)
    LeftTextureName: (String, 0x0, 0x0, 0x0)
    OverrideAoeRadius: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    CenterLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    OverrideMaxCastRange: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    NumOfInnerAoe: (U32, 0x0, 0x0, 0x0)
    pass

class 0x72c992e3(0xc9dd46d2):
    pass

class ContextualConditionShopOpenCount(IContextualCondition):
    mShopOpenCount: (U32, 0x0, 0x0, 0x0)
    pass

class HudLoadingScreenWidgetChat(IHudLoadingScreenWidget):
    pass

class 0x7305ae32(ISequenceActionInstance):
    pass

class 0x7319918a():
    pass

class MinimapIconBehaviorSet():
    MinimapBehaviors: (List, 0x0, Pointer, MinimapIconBehavior)
    pass

class LoadingScreenChallengesData():
    ChallengesTokenLayout: (Hash, 0x0, 0x0, 0x0)
    ChallengeTokenData: (Embed, 0x0, 0x0, LoadingScreenChallengeTokenData)
    ChallengeBorderCrystalsData: (Map, U32, String, 0x0)
    SummonerChallengeCrystal: (List, 0x0, Hash, 0x0)
    ChallengeCrystalsData: (Map, U32, String, 0x0)
    SummonerChallengeBorderCrystal: (List, 0x0, Hash, 0x0)
    pass

class StaticMaterialChildTechniqueDef():
    Name: (String, 0x0, 0x0, 0x0)
    ParentName: (String, 0x0, 0x0, 0x0)
    ShaderMacros: (Map, String, String, 0x0)
    pass

class IHudLoadingScreenWidget():
    mSceneName: (String, 0x0, 0x0, 0x0)
    pass

class TftCombatRecapLineTemplate():
    MeterFillTotal: (Hash, 0x0, 0x0, 0x0)
    UnitIcon: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    UnitEmptySlot: (Hash, 0x0, 0x0, 0x0)
    TransitionTime: (F32, 0x0, 0x0, 0x0)
    MeterFillShieldGranted: (Hash, 0x0, 0x0, 0x0)
    UnitSlotRegions: (List, 0xc, Hash, 0x0)
    TextAmountTotal: (Hash, 0x0, 0x0, 0x0)
    StarBadges: (List, 0x4, Hash, 0x0)
    MeterFillTrueDealt: (Hash, 0x0, 0x0, 0x0)
    MeterFillPhysicalBlocked: (Hash, 0x0, 0x0, 0x0)
    SelectedIcon: (Hash, 0x0, 0x0, 0x0)
    TooltipRegion: (Hash, 0x0, 0x0, 0x0)
    MeterFillPhysicalDealt: (Hash, 0x0, 0x0, 0x0)
    MeterFillMagicBlocked: (Hash, 0x0, 0x0, 0x0)
    MeterFillHealCasted: (Hash, 0x0, 0x0, 0x0)
    HitRegion: (Hash, 0x0, 0x0, 0x0)
    MeterFillTrueBlocked: (Hash, 0x0, 0x0, 0x0)
    MeterFillMagicDealt: (Hash, 0x0, 0x0, 0x0)
    StarBorders: (List, 0x4, Hash, 0x0)
    pass

class RunFunctionBlock(IRunFunctionBlock):
    Function: (Embed, 0x0, 0x0, FunctionTableGet)
    pass

class ContextualConditionWinningTeam(IContextualCondition):
    IsSameTeam: (Bool, 0x0, 0x0, 0x0)
    pass

class TechniqueDef():
    Passes: (List, 0x0, Embed, PassDef)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class DynamicMaterialParameterDef():
    Enabled: (Bool, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    Driver: (Pointer, 0x0, 0x0, IDynamicMaterialDriver)
    Driver: (Pointer, 0x0, 0x0, ILogicDriver)
    pass

class GetSequenceObjectDynamicMaterialFloatDriver(ILogicFloatDriver):
    mKeyName: (String, 0x0, 0x0, 0x0)
    pass

class FontColors():
    OutlineColor: (Color, 0x0, 0x0, 0x0)
    Color: (Color, 0x0, 0x0, 0x0)
    ShadowColor: (Color, 0x0, 0x0, 0x0)
    pass

class SummonerEmote():
    VfxSystem: (Hash, 0x0, 0x0, 0x0)
    VfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    AnnouncementIcon: (String, 0x0, 0x0, 0x0)
    UiScale: (F32, 0x0, 0x0, 0x0)
    SelectionIcon: (String, 0x0, 0x0, 0x0)
    RenderScale: (F32, 0x0, 0x0, 0x0)
    mFacingOption: (U8, 0x0, 0x0, 0x0)
    mReadyForPlaytest: (Bool, 0x0, 0x0, 0x0)
    SummonerEmoteId: (U32, 0x0, 0x0, 0x0)
    VisibleSelectionName: (String, 0x0, 0x0, 0x0)
    SummonerEmoteTroyFile: (String, 0x0, 0x0, 0x0)
    VerticalOffset: (F32, 0x0, 0x0, 0x0)
    pass

class ClashLogo():
    mLogoPath: (String, 0x0, 0x0, 0x0)
    mClashLogoColorId: (U32, 0x0, 0x0, 0x0)
    mClashLogoId: (U32, 0x0, 0x0, 0x0)
    pass

class TftAugmentDisplayData():
    Texts: (List, 0x0, Hash, 0x0)
    Type: (U8, 0x0, 0x0, 0x0)
    Placeholder: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    AugmentButton: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class HeroFloatingInfoBountyData():
    TierOneThreshold: (F32, 0x0, 0x0, 0x0)
    TierTwoIcon: (Hash, 0x0, 0x0, 0x0)
    0x9026ab9e: (Color, 0x0, 0x0, 0x0)
    TierTwoThreshold: (F32, 0x0, 0x0, 0x0)
    0xd2e55900: (Color, 0x0, 0x0, 0x0)
    TierOneIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class LevelScriptControllerFunctionLink():
    LevelControllerLink: (Link, 0x0, 0x0, LevelScriptController)
    FunctionName: (Hash, 0x0, 0x0, 0x0)
    pass

class TftUnitInfoCustomButtonData():
    TooltipUpperRightAnchor: (Hash, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    ItemTooltipData: (Embed, 0x0, 0x0, TftUnitInfoCustomButtonItemTooltipData)
    SelectedUnitProperty: (Hash, 0x0, 0x0, 0x0)
    ActivateUnitProperty: (Hash, 0x0, 0x0, 0x0)
    PlainTextTooltipData: (Embed, 0x0, 0x0, TftUnitInfoCustomButtonPlainTextTooltipData)
    EnabledUnitProperty: (Hash, 0x0, 0x0, 0x0)
    pass

class ValueColor():
    ConstantValue: (Vec4, 0x0, 0x0, 0x0)
    Dynamics: (Pointer, 0x0, 0x0, VfxAnimatedColorVariableData)
    Dynamics: (Pointer, 0x0, 0x0, VfxColorBase)
    pass

class HudAbilityResourceThresholdIndicator():
    ThresholdIndicatorElements: (List, 0xa, Hash, 0x0)
    pass

class TftUnitUpgradeData():
    Name: (String, 0x0, 0x0, 0x0)
    UpgradeEnum: (U8, 0x0, 0x0, 0x0)
    pass

class LoadoutGridButtonData():
    Scene: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    GamePass: (Hash, 0x0, 0x0, 0x0)
    Check: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    Lock: (Hash, 0x0, 0x0, 0x0)
    pass

class MaterialInstanceDynamicParam():
    Enabled: (Bool, 0x0, 0x0, 0x0)
    Driver: (Pointer, 0x0, 0x0, IDynamicMaterialDriver)
    Driver: (Pointer, 0x0, 0x0, ILogicDriver)
    pass

class UiClashTeam():
    TagText: (Hash, 0x0, 0x0, 0x0)
    LogoIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class CharacterQuestListData():
    CharacterQuestList: (List2, 0x0, Pointer, 0xe2ff8b22)
    0x5f1426cf: (Bool, 0x0, 0x0, 0x0)
    0x702d99a3: (I32, 0x0, 0x0, 0x0)
    pass

class ModalDialogViewController(ViewController):
    CloseButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    0x38eaaebf: (Bool, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    CancelButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    ViewPaneDefinition: (Pointer, 0x0, 0x0, ViewPaneDefinition)
    ContentScene: (Hash, 0x0, 0x0, 0x0)
    ConfirmButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x7546469c():
    pass

class 0x755cf26f(ISequenceAction):
    SoundEvent: (Pointer, 0x0, 0x0, 0xbc280d0a)
    pass

class LoadoutUpgradeDialogViewController(ModalDialogViewController):
    ErrorText: (Hash, 0x0, 0x0, 0x0)
    RarityFrameCommon: (Hash, 0x0, 0x0, 0x0)
    StarLevel3Vfx: (Hash, 0x0, 0x0, 0x0)
    RarityFrameEpic: (Hash, 0x0, 0x0, 0x0)
    ItemFrame: (Hash, 0x0, 0x0, 0x0)
    UpgradeText: (Hash, 0x0, 0x0, 0x0)
    RarityFrameLegendary: (Hash, 0x0, 0x0, 0x0)
    StarLevel2Vfx: (Hash, 0x0, 0x0, 0x0)
    ItemIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class FxActionAlphaInstance(IFxActionInstance):
    pass

class LargeMinionFilter(IStatStoneLogicDriver):
    pass

class ContextualConditionEnemyDeathsNearby(IContextualCondition, ICharacterSubcondition):
    mEnemyDeaths: (U32, 0x0, 0x0, 0x0)
    pass

class AiMinionCommon(AiBaseClient):
    pass

class DeathRecapDamagerDetailedDisplayData():
    BountyText: (Hash, 0x0, 0x0, 0x0)
    Portrait: (Hash, 0x0, 0x0, 0x0)
    SpellLayout: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    KillerIcon: (Hash, 0x0, 0x0, 0x0)
    SpellDisplayTemplate: (Embed, 0x0, 0x0, DamageSpellDisplayData)
    KdaText: (Hash, 0x0, 0x0, 0x0)
    DamageText: (Hash, 0x0, 0x0, 0x0)
    DamageMeter: (Embed, 0x0, 0x0, DamageTypeMeterData)
    Metrics: (List2, 0x0, Pointer, UiMetricUnitTypeI)
    BountyIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class ObjectiveCampDefinition():
    VfxAlignmentTake: (Hash, 0x0, 0x0, 0x0)
    ObjectiveCampName: (Hash, 0x0, 0x0, 0x0)
    VfxNoneToExpanded: (Hash, 0x0, 0x0, 0x0)
    VfxAlignmentGive: (Hash, 0x0, 0x0, 0x0)
    VfxExpandedToCollapsed: (Hash, 0x0, 0x0, 0x0)
    VfxCollapsedToExpanded: (Hash, 0x0, 0x0, 0x0)
    ObjectiveCampIndex: (U32, 0x0, 0x0, 0x0)
    VfxNoneToCollapsed: (Hash, 0x0, 0x0, 0x0)
    VfxPortraitLooping: (Hash, 0x0, 0x0, 0x0)
    PortraitIcon: (Hash, 0x0, 0x0, 0x0)
    ObjectiveName: (String, 0x0, 0x0, 0x0)
    pass

class PingRadialBaseDefaultCommandDefinition():
    CommandCenterIcon: (Hash, 0x0, 0x0, 0x0)
    CommandCenterMinimapIcon: (Hash, 0x0, 0x0, 0x0)
    PingCategory: (U8, 0x0, 0x0, 0x0)
    CommandText: (String, 0x0, 0x0, 0x0)
    pass

class TableValueExistsCondition(IRsCondition):
    TableValue: (Embed, 0x0, 0x0, TableGet)
    pass

class OptionItemLabel(IOptionItem):
    Label2TraKey: (String, 0x0, 0x0, 0x0)
    Template: (Hash, 0x0, 0x0, 0x0)
    Label1TraKey: (String, 0x0, 0x0, 0x0)
    pass

class 0x7634a32e(IBehaviorScriptBlock):
    pass

class 0x7638f87c():
    RewardIconFrame: (Embed, 0x0, 0x0, 0x51db35d3)
    RewardFrame: (Hash, 0x0, 0x0, 0x0)
    RewardBackground: (Hash, 0x0, 0x0, 0x0)
    RewardIcon: (Hash, 0x0, 0x0, 0x0)
    RewardHitRegion: (Hash, 0x0, 0x0, 0x0)
    RewardDayText: (Hash, 0x0, 0x0, 0x0)
    Parent: (Hash, 0x0, 0x0, 0x0)
    pass

class AbilityResourceByCoefficientCalculationPart(IGameCalculationPart, ISpellCalculationPart):
    mCoefficient: (F32, 0x0, 0x0, 0x0)
    mAbilityResource: (U8, 0x0, 0x0, 0x0)
    mStatFormula: (U8, 0x0, 0x0, 0x0)
    pass

class SpellModifier():
    mCalculationStatConversions: (List, 0x0, Embed, RatioConversion)
    mCalculationModificationPriority: (U32, 0x0, 0x0, 0x0)
    mModifierId: (Hash, 0x0, 0x0, 0x0)
    DescriptionAppendPriority: (U32, 0x0, 0x0, 0x0)
    mSpellDoesNotIncludeStatScaling: (U8, 0x0, 0x0, 0x0)
    DescriptionAppendTra: (String, 0x0, 0x0, 0x0)
    mSpellIncludesStatScaling: (U8, 0x0, 0x0, 0x0)
    AddedCalculationParts: (List, 0x0, Embed, ModifierAddedCalculationPart)
    PickDescriptionAppendTra: (String, 0x0, 0x0, 0x0)
    pass

class EnvironmentPbrShadingModel(IEnvironmentShadingModel):
    pass

class 0x76621fa6():
    TargetUnitsToBuff: (Option, 0x0, U32, 0x0)
    TargetStrategy: (U8, 0x0, 0x0, 0x0)
    TeamToBuff: (U8, 0x0, 0x0, 0x0)
    BuffName: (String, 0x0, 0x0, 0x0)
    pass

class LocationClamped(TargetingTypeData):
    pass

class HasNNearbyUnitsRequirement(ICastRequirement):
    mUnitsRequirements: (List, 0x0, Pointer, ICastRequirement)
    mDistanceType: (U32, 0x0, 0x0, 0x0)
    mRange: (F32, 0x0, 0x0, 0x0)
    mUnitsRequired: (U32, 0x0, 0x0, 0x0)
    pass

class IGameCalculationPartWithBuffCounter(IGameCalculationPart):
    mBuffName: (Hash, 0x0, 0x0, 0x0)
    mIconKey: (String, 0x0, 0x0, 0x0)
    mScalingTagKey: (String, 0x0, 0x0, 0x0)
    pass

class 0x769171e6(IFxAction):
    Location: (Pointer, 0x0, 0x0, IFxLocation)
    pass

class OptionItemSlider(IOptionItem):
    TooltipTraKey: (String, 0x0, 0x0, 0x0)
    Template: (Hash, 0x0, 0x0, 0x0)
    LabelTraKey: (String, 0x0, 0x0, 0x0)
    pass

class FaceCameraEventData(BaseEventData):
    BlendOutTime: (F32, 0x0, 0x0, 0x0)
    FaceTarget: (U8, 0x0, 0x0, 0x0)
    BlendInTime: (F32, 0x0, 0x0, 0x0)
    YRotationDegrees: (F32, 0x0, 0x0, 0x0)
    pass

class 0x76bc0857():
    pass

class ContextualConditionCharacterRole(ICharacterSubcondition):
    mRole: (U8, 0x0, 0x0, 0x0)
    pass

class UiStorePurchaseRowData():
    ActionButton: (Hash, 0x0, 0x0, 0x0)
    BundleIconPath: (String, 0x0, 0x0, 0x0)
    Divider: (Hash, 0x0, 0x0, 0x0)
    Quantity: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    TreasureTroveTokenIconPath: (String, 0x0, 0x0, 0x0)
    MiscIconPath: (String, 0x0, 0x0, 0x0)
    Item: (Hash, 0x0, 0x0, 0x0)
    TransactionId: (Hash, 0x0, 0x0, 0x0)
    Date: (Hash, 0x0, 0x0, 0x0)
    ActionText: (Hash, 0x0, 0x0, 0x0)
    TacticianIconPath: (String, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    Amount: (Hash, 0x0, 0x0, 0x0)
    ArenaIconPath: (String, 0x0, 0x0, 0x0)
    pass

class 0x7709fefa(0xe561be2e):
    Index: (Pointer, 0x0, 0x0, 0x8b33cf88)
    0xb848c7d8: (Bool, 0x0, 0x0, 0x0)
    Data: (Pointer, 0x0, 0x0, 0x7319918a)
    pass

class SkinAugmentCategories():
    BorderAugments: (List2, 0x0, Embed, 0x4a70b12c)
    BasicAugments: (List2, 0x0, Embed, 0xe1555e0a)
    pass

class OptionItemFilter_PromoteAccount(IOptionItemFilter):
    pass

class 0x7730763b(0x64c18f7d):
    pass

class AbilityResourceStateData():
    AnimationSuffix: (String, 0x0, 0x0, 0x0)
    ColorblindPalette: (Pointer, 0x0, 0x0, AbilityResourceStateColorOptions)
    TextureSuffix: (String, 0x0, 0x0, 0x0)
    Color: (Color, 0x0, 0x0, 0x0)
    DefaultPalette: (Pointer, 0x0, 0x0, AbilityResourceStateColorOptions)
    FadeColor: (Color, 0x0, 0x0, 0x0)
    pass

class StatFilterButtonDefinitions():
    Health: (Embed, 0x0, 0x0, StatFilterDefinition)
    MagicPenetration: (Embed, 0x0, 0x0, StatFilterDefinition)
    AttackSpeed: (Embed, 0x0, 0x0, StatFilterDefinition)
    AbilityPower: (Embed, 0x0, 0x0, StatFilterDefinition)
    DisableStatFilters: (Embed, 0x0, 0x0, StatFilterDefinition)
    MoveSpeed: (Embed, 0x0, 0x0, StatFilterDefinition)
    MagicResist: (Embed, 0x0, 0x0, StatFilterDefinition)
    ArmorPenetration: (Embed, 0x0, 0x0, StatFilterDefinition)
    LifeStealAndVamp: (Embed, 0x0, 0x0, StatFilterDefinition)
    Mana: (Embed, 0x0, 0x0, StatFilterDefinition)
    CriticalStrike: (Embed, 0x0, 0x0, StatFilterDefinition)
    AbilityHaste: (Embed, 0x0, 0x0, StatFilterDefinition)
    OnHit: (Embed, 0x0, 0x0, StatFilterDefinition)
    PhysicalDamage: (Embed, 0x0, 0x0, StatFilterDefinition)
    Armor: (Embed, 0x0, 0x0, StatFilterDefinition)
    pass

class FixedSpeedSplineMovement(GenericSplineMovementSpec):
    mSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class CcScoreMultipliers():
    Blind: (F32, 0x0, 0x0, 0x0)
    Root: (F32, 0x0, 0x0, 0x0)
    Knockup: (F32, 0x0, 0x0, 0x0)
    Nearsight: (F32, 0x0, 0x0, 0x0)
    Grounded: (F32, 0x0, 0x0, 0x0)
    AttackSpeedSlow: (F32, 0x0, 0x0, 0x0)
    Charm: (F32, 0x0, 0x0, 0x0)
    Slow: (F32, 0x0, 0x0, 0x0)
    Berserk: (F32, 0x0, 0x0, 0x0)
    Drowsy: (F32, 0x0, 0x0, 0x0)
    Disarm: (F32, 0x0, 0x0, 0x0)
    Silence: (F32, 0x0, 0x0, 0x0)
    Taunt: (F32, 0x0, 0x0, 0x0)
    Knockback: (F32, 0x0, 0x0, 0x0)
    Fear: (F32, 0x0, 0x0, 0x0)
    Stun: (F32, 0x0, 0x0, 0x0)
    Polymorph: (F32, 0x0, 0x0, 0x0)
    Flee: (F32, 0x0, 0x0, 0x0)
    Asleep: (F32, 0x0, 0x0, 0x0)
    Suppression: (F32, 0x0, 0x0, 0x0)
    pass

class IdleParticlesVisibilityEventData(BaseEventData):
    mShow: (Bool, 0x0, 0x0, 0x0)
    pass

class VfxShape():
    EmitRotationAngles: (List, 0x0, Embed, ValueFloat)
    FlexBirthTranslation: (Pointer, 0x0, 0x0, FlexValueVector3)
    EmitRotationAxes: (List, 0x0, Vec3, 0x0)
    FlexOffset: (Pointer, 0x0, 0x0, FlexValueVector3)
    EmitOffset: (Embed, 0x0, 0x0, ValueVector3)
    BirthTranslation: (Embed, 0x0, 0x0, ValueVector3)
    pass

class ToggleBarracksCheat(Cheat):
    mKillExistingMinions: (Bool, 0x0, 0x0, 0x0)
    mKillWards: (Bool, 0x0, 0x0, 0x0)
    pass

class NextSpellVarsTable(ScriptTable):
    pass

class 0x77fb37dd():
    Divider: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    TeamOneIcon: (Hash, 0x0, 0x0, 0x0)
    TeamTwoIcon: (Hash, 0x0, 0x0, 0x0)
    SpectateButton: (Hash, 0x0, 0x0, 0x0)
    pass

class PoiScalingData():
    MinDistanceScale: (F32, 0x0, 0x0, 0x0)
    MinDistance: (U32, 0x0, 0x0, 0x0)
    MaxDistanceScale: (F32, 0x0, 0x0, 0x0)
    MaxDistance: (U32, 0x0, 0x0, 0x0)
    pass

class ChatOnlyAnnouncementDefinition_Deprecated(AnnouncementDefinition):
    pass

class DelayChildrenOnMovementCompleteSpec(MissileBehaviorSpec):
    mDelay: (I32, 0x0, 0x0, 0x0)
    mDelayTime: (F32, 0x0, 0x0, 0x0)
    pass

class UiMetricUnitTypeSimpleI(UiMetricUnitTypeI):
    Text: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x786113b8(0x24f4a711, SelectSpellBlock):
    pass

class EnableLookAtEventData(BaseEventData):
    mEnableLookAt: (Bool, 0x0, 0x0, 0x0)
    mLockCurrentValues: (Bool, 0x0, 0x0, 0x0)
    pass

class BuffScript(GameScript):
    pass

class 0x7896c78b(ILolSpellScriptEvent):
    pass

class BannerFlagData():
    BannerFlagId: (U32, 0x0, 0x0, 0x0)
    NameTranslationKey: (String, 0x0, 0x0, 0x0)
    CollectionsIcon: (String, 0x0, 0x0, 0x0)
    VfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    Skin: (String, 0x0, 0x0, 0x0)
    Texture: (String, 0x0, 0x0, 0x0)
    SkinMeshProperties: (Embed, 0x0, 0x0, SkinMeshDataProperties)
    ProfileIcon: (String, 0x0, 0x0, 0x0)
    BannerTheme: (String, 0x0, 0x0, 0x0)
    Theme: (String, 0x0, 0x0, 0x0)
    Skeleton: (String, 0x0, 0x0, 0x0)
    InventoryIcon: (String, 0x0, 0x0, 0x0)
    AnimationGraphData: (Link, 0x0, 0x0, AnimationGraphData)
    pass

class 0x78ea58c3(0x26d26471):
    OrConditions: (List2, 0x0, Pointer, 0x26d26471)
    pass

class FloatingHealthBarBurstHealData():
    HealFadeDuration: (F32, 0x0, 0x0, 0x0)
    HealTimeWindow: (F32, 0x0, 0x0, 0x0)
    HealTriggerPercent: (F32, 0x0, 0x0, 0x0)
    pass

class FxPhaseOverride():
    Duration: (F32, 0x0, 0x0, 0x0)
    OverrideDuration: (Bool, 0x0, 0x0, 0x0)
    OverrideType: (Bool, 0x0, 0x0, 0x0)
    Type: (U32, 0x0, 0x0, 0x0)
    pass

class TargetFrameViewController(ViewController):
    HealthMeter: (Embed, 0x0, 0x0, HealthMeter)
    Scene: (Hash, 0x0, 0x0, 0x0)
    LevelData: (Embed, 0x0, 0x0, UnitLevelUiData)
    Portrait: (Hash, 0x0, 0x0, 0x0)
    ParBarData: (Embed, 0x0, 0x0, AbilityResourceBarData)
    DrawAreaList: (Embed, 0x0, 0x0, DrawAreaList)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    NegativeBuffs: (Embed, 0x0, 0x0, BuffDisplayList)
    UseSquarePortrait: (Bool, 0x0, 0x0, 0x0)
    ExperienceMeter: (Hash, 0x0, 0x0, 0x0)
    TargetStatsMenu: (Pointer, 0x0, 0x0, UiTargetStatsMenu)
    AbilitiesData: (Pointer, 0x0, 0x0, AbilitiesUiData)
    InventoryData: (Pointer, 0x0, 0x0, SimpleItemSlots)
    TargetClosedScene: (Hash, 0x0, 0x0, 0x0)
    TooltipRegion: (Hash, 0x0, 0x0, 0x0)
    HealthMeterSkins: (Pointer, 0x0, 0x0, TargetFrameMeterSkinData)
    ObjectName: (String, 0x0, 0x0, 0x0)
    PositiveBuffs: (Embed, 0x0, 0x0, BuffDisplayList)
    TooltipAnchor: (Hash, 0x0, 0x0, 0x0)
    Metrics: (List2, 0x0, Pointer, UiMetricUnitTypeI)
    GeneralMetrics: (List2, 0x0, Pointer, UiMetricTypeI)
    StatsUiData: (Embed, 0x0, 0x0, UnitStatsUiData)
    pass

class HudCheatMenuData():
    TooltipDelay: (F32, 0x0, 0x0, 0x0)
    GroupDividerIndex: (U8, 0x0, 0x0, 0x0)
    GroupDividerGapSize: (F32, 0x0, 0x0, 0x0)
    pass

class ModeSelectViewController(ViewController):
    0x175bb989: (String, 0x0, 0x0, 0x0)
    PageRightButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    SoundOnDeActivate: (String, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    Queues: (List2, 0x0, Link, MatchmakingQueue)
    QueueDisplayData: (List, 0x0, Embed, QueueDisplayData)
    ModeSelectQueueButtonData: (Embed, 0x0, 0x0, ModeSelectQueueButtonData)
    DisabledIconColor: (Color, 0x0, 0x0, 0x0)
    EventTimer: (Pointer, 0x0, 0x0, TftEventTimer)
    DefaultIconColor: (Color, 0x0, 0x0, 0x0)
    PageRightButton: (Hash, 0x0, 0x0, 0x0)
    QueueSelectDisplaySlots: (List, 0x0, Hash, 0x0)
    PageLeftButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    DisabledIconTexture: (String, 0x0, 0x0, 0x0)
    EventTimerDefinition: (Pointer, 0x0, 0x0, TftEventTimer)
    0x9e4be5ed: (Hash, 0x0, 0x0, 0x0)
    SoundOnActivate: (String, 0x0, 0x0, 0x0)
    HoverIconColor: (Color, 0x0, 0x0, 0x0)
    IconBackground: (Hash, 0x0, 0x0, 0x0)
    Layout: (Hash, 0x0, 0x0, 0x0)
    ClickedIconColor: (Color, 0x0, 0x0, 0x0)
    PageLeftButton: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x79632a57(IScriptBlock, IBehaviorScriptBlock):
    pass

class VideoDefinition():
    Filename: (String, 0x0, 0x0, 0x0)
    Looping: (Bool, 0x0, 0x0, 0x0)
    pass

class ReciprocityController():
    ConfigData: (Embed, 0x0, 0x0, ReciprocityConfigData)
    InteractionEmoteIds: (List2, 0x0, U32, 0x0)
    CelebrationEmoteIds: (List2, 0x0, U32, 0x0)
    PlayerFrameButton: (Hash, 0x0, 0x0, 0x0)
    CelebrationEmote: (Hash, 0x0, 0x0, 0x0)
    IntroEmote: (Hash, 0x0, 0x0, 0x0)
    PlayerFrameButtonFill: (Hash, 0x0, 0x0, 0x0)
    pass

class IOptionItem():
    LiveUpdate: (Bool, 0x0, 0x0, 0x0)
    ShowOnPlatform: (U8, 0x0, 0x0, 0x0)
    Filter: (Pointer, 0x0, 0x0, IOptionItemFilter)
    pass

class ResimulateTrailVfxOnEnterVisibility(MissileBehaviorSpec):
    TimeToResimulate: (F32, 0x0, 0x0, 0x0)
    SimulationFrames: (U32, 0x0, 0x0, 0x0)
    Cycles: (U32, 0x0, 0x0, 0x0)
    pass

class ChatViewController(ViewController):
    ChatFrameBounds: (Hash, 0x0, 0x0, 0x0)
    DefaultWordWrapMargin: (U8, 0x0, 0x0, 0x0)
    AnchorSpectatorUpdate: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    SceneChatChannelSelectView: (Hash, 0x0, 0x0, 0x0)
    MinimumScale: (F32, 0x0, 0x0, 0x0)
    AnchorFlippedMinimap: (Hash, 0x0, 0x0, 0x0)
    ChatHudText: (Hash, 0x0, 0x0, 0x0)
    SceneChat: (Hash, 0x0, 0x0, 0x0)
    ChatHudRestrictionText: (Hash, 0x0, 0x0, 0x0)
    ChatTextEdit: (Hash, 0x0, 0x0, 0x0)
    AnchorBase: (Hash, 0x0, 0x0, 0x0)
    AnchorTft: (Hash, 0x0, 0x0, 0x0)
    SceneChatTextArea: (Hash, 0x0, 0x0, 0x0)
    ExpandedChatElement: (Hash, 0x0, 0x0, 0x0)
    ViewPaneDefinition: (Embed, 0x0, 0x0, ViewPaneDefinition)
    ChatInputCenter: (Hash, 0x0, 0x0, 0x0)
    HideAfterSeconds: (F32, 0x0, 0x0, 0x0)
    SceneChatTextEditBg: (Hash, 0x0, 0x0, 0x0)
    ChatHudTextBackground: (Hash, 0x0, 0x0, 0x0)
    ChatInputIndicatorTooltips: (Hash, 0x0, 0x0, 0x0)
    ViewPaneLink: (Hash, 0x0, 0x0, 0x0)
    MaximumScale: (F32, 0x0, 0x0, 0x0)
    ComboBoxDefinition: (Embed, 0x0, 0x0, ChatChannelSelectionComboBoxDefinition)
    pass

class BaseEventData():
    mName: (Hash, 0x0, 0x0, 0x0)
    mName: (String, 0x0, 0x0, 0x0)
    mStartFrame: (F32, 0x0, 0x0, 0x0)
    mIsDetachable: (Bool, 0x0, 0x0, 0x0)
    mIsSelfOnly: (Bool, 0x0, 0x0, 0x0)
    mIsKillEvent: (Bool, 0x0, 0x0, 0x0)
    mFireIfAnimationEndsEarly: (Bool, 0x0, 0x0, 0x0)
    mEndFrame: (F32, 0x0, 0x0, 0x0)
    mIsLoop: (Bool, 0x0, 0x0, 0x0)
    pass

class FxActionSfxStatic(FxActionSfxBase):
    Location: (Pointer, 0x0, 0x0, IFxLocation)
    pass

class 0x79ca73e7():
    0x1ef5b158: (String, 0x0, 0x0, 0x0)
    0x20e0b520: (String, 0x0, 0x0, 0x0)
    0x7dbd6ef1: (String, 0x0, 0x0, 0x0)
    0x9290be1: (String, 0x0, 0x0, 0x0)
    0xb94c1f8e: (String, 0x0, 0x0, 0x0)
    0xbfdc3540: (String, 0x0, 0x0, 0x0)
    0xf4186080: (String, 0x0, 0x0, 0x0)
    pass

class KeyInputSourceBool(IInputSourceBool):
    KeySequence: (String, 0x0, 0x0, 0x0)
    IniKeyValue: (String, 0x0, 0x0, 0x0)
    pass

class TftTrovesCelebrationChestSegmentData():
    ChestBackgroundTimingOffset: (F32, 0x0, 0x0, 0x0)
    SinglePullTierHintOffset: (F32, 0x0, 0x0, 0x0)
    SingleSequence: (Link, 0x0, 0x0, Sequence)
    MultiSequence: (Link, 0x0, 0x0, Sequence)
    MultiPullPrimaryTierHintStagger: (F32, 0x0, 0x0, 0x0)
    TotalDuration: (F32, 0x0, 0x0, 0x0)
    SinglePullTierHintVfx: (Map, U32, Hash, 0x0)
    MultiPullTierHintOffset: (F32, 0x0, 0x0, 0x0)
    MultiPullSecondaryTierHintVfx: (Map, U32, Hash, 0x0)
    ChestAssetMultiVfx: (Hash, 0x0, 0x0, 0x0)
    MultiPullSecondaryHintCount: (U8, 0x0, 0x0, 0x0)
    MultiPullPrimaryTierHintVfx: (Map, U32, Hash, 0x0)
    MultiPullSecondaryTierHintStagger: (F32, 0x0, 0x0, 0x0)
    ChestBackgroundAssetVfx: (Hash, 0x0, 0x0, 0x0)
    ChestTimingOffset: (F32, 0x0, 0x0, 0x0)
    ChestAssetSingleVfx: (Hash, 0x0, 0x0, 0x0)
    pass

class TftPlayerChoiceViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    OptionModalData: (Embed, 0x0, 0x0, 0xf3cf86a3)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    OptionDisplayData: (Embed, 0x0, 0x0, 0x34cca270)
    OptionRegion: (Hash, 0x0, 0x0, 0x0)
    OptionHoverRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x7a19656():
    TimerText: (Hash, 0x0, 0x0, 0x0)
    DetailPanel: (Hash, 0x0, 0x0, 0x0)
    0x6188e7b7: (Hash, 0x0, 0x0, 0x0)
    TimerPanel: (Hash, 0x0, 0x0, 0x0)
    DetailTextT1: (Hash, 0x0, 0x0, 0x0)
    DetailTextT2: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x7a1a2d27():
    CombinableDamageFormat: (Link, 0x0, 0x0, FloatTextFormattingData)
    AbsorbedDamageFormat: (Link, 0x0, 0x0, FloatTextFormattingData)
    DefaultTrueDamageFormat: (Link, 0x0, 0x0, FloatTextFormattingData)
    CriticalMagicalDamageFormat: (Link, 0x0, 0x0, FloatTextFormattingData)
    CriticalPhysicalDamageFormat: (Link, 0x0, 0x0, FloatTextFormattingData)
    DefaultMagicalDamageFormat: (Link, 0x0, 0x0, FloatTextFormattingData)
    CriticalTrueDamageFormat: (Link, 0x0, 0x0, FloatTextFormattingData)
    DefaultPhysicalDamageFormat: (Link, 0x0, 0x0, FloatTextFormattingData)
    pass

class PostGameUnitTemplate():
    0x49bd8929: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    OneStar: (Hash, 0x0, 0x0, 0x0)
    TwoStar: (Hash, 0x0, 0x0, 0x0)
    ThreeStar: (Hash, 0x0, 0x0, 0x0)
    IconFrame: (Hash, 0x0, 0x0, 0x0)
    ItemIcons: (List, 0x0, Hash, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    TooltipButton: (Hash, 0x0, 0x0, 0x0)
    pass

class TftUnitAttachmentStandardSlotData():
    Overlay: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class StoreViewMythic():
    ManagedLayout: (Hash, 0x0, 0x0, 0x0)
    BackgroundTexture: (Hash, 0x0, 0x0, 0x0)
    pass

class NullMovement(MissileMovementSpec):
    mDelayTime: (F32, 0x0, 0x0, 0x0)
    mWaitForChildren: (Bool, 0x0, 0x0, 0x0)
    pass

class SequenceObjectSelector():
    Type: (U32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    Hash: (Hash, 0x0, 0x0, 0x0)
    pass

class HappenedNearTurretConstraintInfo(ListenerConstraintInfo):
    TeamToCheck: (U32, 0x0, 0x0, 0x0)
    DistanceRequired: (F32, 0x0, 0x0, 0x0)
    ParticipantLocation: (U32, 0x0, 0x0, 0x0)
    pass

class ILogicBoolDriver(ILogicIntDriver, ILogicFloatDriver):
    pass

class CooldownEffectUiData():
    RadialEffect: (Hash, 0x0, 0x0, 0x0)
    CooldownJumpEffect: (Hash, 0x0, 0x0, 0x0)
    CooldownText: (Hash, 0x0, 0x0, 0x0)
    CooldownCompleteEffect: (Hash, 0x0, 0x0, 0x0)
    pass

class TargetingForgivenessDefinitions():
    TargetForgivenessDefinitions: (List, 0x0, Pointer, ICastRequirement)
    CasterForgivenessDefinitions: (List, 0x0, Pointer, ICastRequirement)
    mAffectsStatusOverride: (U32, 0x0, 0x0, 0x0)
    ForgivenessRange: (F32, 0x0, 0x0, 0x0)
    mAffectsTypeOverride: (U32, 0x0, 0x0, 0x0)
    OverrideAffectsFlags: (Bool, 0x0, 0x0, 0x0)
    pass

class LuaPropertyDataStringArray(LuaPropertyData):
    Values: (List, 0x0, String, 0x0)
    pass

class HudTunables():
    mGameScoreboardTransitionData: (Embed, 0x0, 0x0, HudScoreboardTransitionData)
    mGameScoreboardTransitionData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mReplayData: (Embed, 0x0, 0x0, HudReplayData)
    mRadailWheelData: (Embed, 0x0, 0x0, HudRadialWheelData)
    mHealthBarData: (Embed, 0x0, 0x0, HudHealthBarData)
    mScaleSettings: (Embed, 0x0, 0x0, HudScaleSettingsData)
    mLevelUpTransitionData: (Embed, 0x0, 0x0, HudLevelUpData)
    mEmotePopupData: (Embed, 0x0, 0x0, HudEmotePopupData)
    mReplayTeamFramesTransitionData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    DamageDisplayData: (Embed, 0x0, 0x0, HudDamageDisplayData)
    mReplayTeamFightTransitionData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    TipTrackerData: (Embed, 0x0, 0x0, HudMessageDisplayData)
    mAbilityPromptAnimData: (Embed, 0x0, 0x0, HudAbilityPromptData)
    StatStoneMilestoneData: (Embed, 0x0, 0x0, HudStatStoneMilestoneData)
    mStatPanelStatStoneData: (Embed, 0x0, 0x0, HudStatPanelStatStoneData)
    mReplayGameStatsTransitionData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    KillCalloutData: (Embed, 0x0, 0x0, HudMessageDisplayData)
    KillCalloutData: (Embed, 0x0, 0x0, HudKillCalloutData)
    0x9cec9ff0: (Embed, 0x0, 0x0, HudBannerData)
    mEncounterUiData: (Embed, 0x0, 0x0, HudEncounterData)
    mVoiceChatData: (Embed, 0x0, 0x0, HudVoiceChatData)
    mElementalSelectionAnimationData: (Embed, 0x0, 0x0, HudElementalSectionUiData)
    mPingData: (Embed, 0x0, 0x0, HudPingData)
    mTooltipDisplayData: (Embed, 0x0, 0x0, HudTooltipDisplayData)
    mStatStoneDeathRecapData: (Embed, 0x0, 0x0, HudStatStoneDeathRecapData)
    mEndOfGameData: (Embed, 0x0, 0x0, HudEndOfGameData)
    mReplayScoreboardTransitionData: (Embed, 0x0, 0x0, HudScoreboardTransitionData)
    mReplayScoreboardTransitionData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mGearSelectionData: (Embed, 0x0, 0x0, HudGearSelectionUiData)
    mChatData: (Embed, 0x0, 0x0, HudChatData)
    mLoadingScreenData: (Embed, 0x0, 0x0, HudLoadingScreenData)
    mCheatMenuData: (Embed, 0x0, 0x0, HudCheatMenuData)
    mHudSpellSlotResetFeedbackData: (Embed, 0x0, 0x0, HudSpellSlotResetFeedbackData)
    FightRecapUiData: (Embed, 0x0, 0x0, HudFightRecapUiData)
    mInputBoxData: (Embed, 0x0, 0x0, HudInputBoxData)
    mStatStoneData: (Embed, 0x0, 0x0, HudStatStoneData)
    WindowPlacementData: (List, 0x0, Embed, HudWindowPlacementData)
    pass

class MapMotionPath(MapPlaceable):
    Segments: (List, 0x0, Pointer, MapPathSegment)
    pass

class ContextualConditionSpell(IContextualCondition):
    mSpellSlot: (U32, 0x0, 0x0, 0x0)
    mSpellSlot: (U8, 0x0, 0x0, 0x0)
    mChildConditions: (List, 0x0, Pointer, IContextualConditionSpell)
    pass

class PfxAnimatedFloatVariableData():
    Values: (List, 0x0, F32, 0x0)
    Times: (List, 0x0, F32, 0x0)
    ProbabilityTables: (List, 0x1, Pointer, PfxProbabilityTableData)
    pass

class MinimapPingData():
    mOmwPingRangeCutoffs: (Map, U8, F32, 0x0)
    mOmwPingRanges: (List, 0x0, Embed, OmwPingRange)
    mPings: (List, 0x0, Embed, MinimapPingTypeContainer)
    pass

class 0x7af6df8b(0x64c18f7d):
    TeleportInnerRadius: (F32, 0x0, 0x0, 0x0)
    Debug: (Bool, 0x0, 0x0, 0x0)
    TeleportDistance: (F32, 0x0, 0x0, 0x0)
    MaxAngle: (F32, 0x0, 0x0, 0x0)
    TeleportOuterRadius: (F32, 0x0, 0x0, 0x0)
    MaxDistance: (F32, 0x0, 0x0, 0x0)
    MinAngle: (F32, 0x0, 0x0, 0x0)
    pass

class BuffCounterByNamedDataValueCalculationPart(IGameCalculationPartWithBuffCounter, ISpellCalculationPartWithBuffCounter, ISpellCalculationPart):
    mBuffName: (Hash, 0x0, 0x0, 0x0)
    mIconKey: (String, 0x0, 0x0, 0x0)
    mDataValue: (Hash, 0x0, 0x0, 0x0)
    mScalingTagKey: (String, 0x0, 0x0, 0x0)
    pass

class HealthBarIconSettings():
    FarRightIconSize: (Vec2, 0x0, 0x0, 0x0)
    CharacterIconPositionOffset: (Vec2, 0x0, 0x0, 0x0)
    SpaceBetweenIcons: (F32, 0x0, 0x0, 0x0)
    TopIconSize: (Vec2, 0x0, 0x0, 0x0)
    FarLeftOffset: (Vec2, 0x0, 0x0, 0x0)
    BotIconSize: (Vec2, 0x0, 0x0, 0x0)
    FarRightOffset: (Vec2, 0x0, 0x0, 0x0)
    FarLeftIconSize: (Vec2, 0x0, 0x0, 0x0)
    CharacterIconSize: (Vec2, 0x0, 0x0, 0x0)
    TopCenterOffset: (Vec2, 0x0, 0x0, 0x0)
    BotLeftOffset: (Vec2, 0x0, 0x0, 0x0)
    pass

class 0x7b40445f():
    ParticipantChampion: (Hash, 0x0, 0x0, 0x0)
    QuestObjectiveList: (List2, 0x0, Pointer, CharacterQuestObjective)
    IsOptional: (Bool, 0x0, 0x0, 0x0)
    0xa62e6d72: (List2, 0x0, Pointer, CharacterInitRequirement)
    Tooltip: (String, 0x0, 0x0, 0x0)
    pass

class TftHudNotificationsData():
    mSceneTransition: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mSceneTransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mSceneTransitionOut: (Embed, 0x0, 0x0, HudMenuTransitionData)
    pass

class FxActionVfxMissile(FxActionVfxBase):
    Target: (Embed, 0x0, 0x0, FxTransform)
    Target: (Pointer, 0x0, 0x0, IFxLocation)
    SplineInfo: (Pointer, 0x0, 0x0, ISplineInfo)
    pass

class AtlasDataBase(IUiTextureDataProvider):
    mTextureSourceResolutionHeight: (U32, 0x0, 0x0, 0x0)
    mTextureSourceResolutionWidth: (U32, 0x0, 0x0, 0x0)
    mTextureName: (String, 0x0, 0x0, 0x0)
    pass

class CelebrationViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    GenericBackgroundTexture: (Hash, 0x0, 0x0, 0x0)
    SubtitleTextHandle: (Hash, 0x0, 0x0, 0x0)
    ClaimedRewardLayout: (Hash, 0x0, 0x0, 0x0)
    CelebrationCompanionForegroundVfx: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    RarityIcons: (Map, U32, Hash, 0x0)
    ClaimedRewardTemplate: (Embed, 0x0, 0x0, 0x82ece567)
    DefaultRatedTierTraKey: (String, 0x0, 0x0, 0x0)
    RankedBackgroundTexture: (Hash, 0x0, 0x0, 0x0)
    DelayedIconWaitTimeSec: (F32, 0x0, 0x0, 0x0)
    Labs: (Map, U32, Embed, CelebrationLabFields)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    IconHandle: (Hash, 0x0, 0x0, 0x0)
    BodyTextHandle: (Hash, 0x0, 0x0, 0x0)
    CelebrationVignetteVfx: (Hash, 0x0, 0x0, 0x0)
    CelebrationVignetteAssetVfx: (Hash, 0x0, 0x0, 0x0)
    ContinueButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    CelebrationTier2StarVfx: (Hash, 0x0, 0x0, 0x0)
    0xb72f9920: (Hash, 0x0, 0x0, 0x0)
    0xb9524edd: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    CelebrationCompanionBackgroundVfx: (Hash, 0x0, 0x0, 0x0)
    0xbc4102dc: (String, 0x0, 0x0, 0x0)
    RatedTierTraKeys: (Map, String, String, 0x0)
    CelebrationTier3StarVfx: (Hash, 0x0, 0x0, 0x0)
    RankedTierVfx: (Map, U32, Hash, 0x0)
    EggTierVfx: (Map, U32, Hash, 0x0)
    IconFrameHandle: (Hash, 0x0, 0x0, 0x0)
    TitleTextHandle: (Hash, 0x0, 0x0, 0x0)
    IconHandleDelayed: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x7b635114(ISequenceAction):
    ParticleEffects: (List2, 0x0, Hash, 0x0)
    0x5af11142: (Link, 0x0, 0x0, SequenceObjectSelector)
    TierIndex: (U32, 0x0, 0x0, 0x0)
    pass

class VoMarkerEvent():
    mVoEvent: (String, 0x0, 0x0, 0x0)
    mVfxKey: (Hash, 0x0, 0x0, 0x0)
    mTargetConditions: (List, 0x0, Pointer, ICharacterSubcondition)
    pass

class SkinEmblem():
    mLoadingScreenAnchor: (U32, 0x0, 0x0, 0x0)
    mEmblemData: (Link, 0x0, 0x0, EmblemData)
    pass

class ContextualConditionGlobalObjectiveBountyForTeam(IContextualCondition):
    TeamCompareOp: (U8, 0x0, 0x0, 0x0)
    pass

class 0x7c02b00b():
    Id: (String, 0x0, 0x0, 0x0)
    Weight: (U32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    BannerNode: (Link, 0x0, 0x0, 0xac83c7b)
    pass

class 0x7c118855():
    Count: (I32, 0x0, 0x0, 0x0)
    RepeatLevels: (List2, 0x0, Embed, 0x1d54119c)
    Multiplier: (F32, 0x0, 0x0, 0x0)
    pass

class NextSpellVars(ScriptTable):
    pass

class CharacterLevelRequirement(ISpellRankUpRequirement):
    mLevel: (U32, 0x0, 0x0, 0x0)
    pass

class 0x7c3f9d36(ISequenceActionInstance):
    pass

class FloatingHealthBarBurstData():
    BurstTriggerPercent: (F32, 0x0, 0x0, 0x0)
    FadeAcceleration: (F32, 0x0, 0x0, 0x0)
    FlashTriggerPercent: (F32, 0x0, 0x0, 0x0)
    FadeHoldTime: (F32, 0x0, 0x0, 0x0)
    FlashDuration: (F32, 0x0, 0x0, 0x0)
    ShakeTriggerPercent: (F32, 0x0, 0x0, 0x0)
    BurstTimeWindow: (F32, 0x0, 0x0, 0x0)
    ShakeDuration: (F32, 0x0, 0x0, 0x0)
    ShakeFrequency: (F32, 0x0, 0x0, 0x0)
    ShakeBox: (Vec2, 0x0, 0x0, 0x0)
    ShakeReferenceResolution: (Vec2, 0x0, 0x0, 0x0)
    FadeSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class CherryUiPlayerPortraitData():
    PortraitUv: (Vec4, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    PortraitIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class PfxFieldCollectionDefinitionData():
    FieldAccelerationDefinitions: (List, 0x0, Embed, PfxFieldAccelerationDefinitionData)
    FieldOrbitalDefinitions: (List, 0x0, Embed, PfxFieldOrbitalDefinitionData)
    FieldDragDefinitions: (List, 0x0, Embed, PfxFieldDragDefinitionData)
    FieldAttractionDefinitions: (List, 0x0, Embed, PfxFieldAttractionDefinitionData)
    FieldNoiseDefinitions: (List, 0x0, Embed, PfxFieldNoiseDefinitionData)
    pass

class UiElementGroup(UiElementI):
    pass

class UiButtonAdditionalElements():
    DefaultStateElements: (Embed, 0x0, 0x0, UiButtonAdditionalState)
    SelectedStateElements: (Embed, 0x0, 0x0, UiButtonAdditionalState)
    SelectedClickedStateElements: (Embed, 0x0, 0x0, UiButtonAdditionalState)
    InactiveStateElements: (Embed, 0x0, 0x0, UiButtonAdditionalState)
    ClickedStateElements: (Embed, 0x0, 0x0, UiButtonAdditionalState)
    SelectedHoverStateElements: (Embed, 0x0, 0x0, UiButtonAdditionalState)
    HoverStateElements: (Embed, 0x0, 0x0, UiButtonAdditionalState)
    pass

class VfxColorBase():
    pass

class 0x7c8b2cd8(0x26d26471):
    pass

class TeamBuffData():
    mBuffName: (String, 0x0, 0x0, 0x0)
    mGloballyVisible: (Bool, 0x0, 0x0, 0x0)
    mUiName: (String, 0x0, 0x0, 0x0)
    pass

class CompanionData(BaseLoadoutData):
    SpeciesLink: (String, 0x0, 0x0, 0x0)
    Rarity: (U32, 0x0, 0x0, 0x0)
    mDisabled: (Bool, 0x0, 0x0, 0x0)
    WinStreakListForEvolution: (List, 0x0, U32, 0x0)
    mCharacter: (Hash, 0x0, 0x0, 0x0)
    TrovesHighlightVfx: (Hash, 0x0, 0x0, 0x0)
    mStandaloneLoadoutsIcon: (String, 0x0, 0x0, 0x0)
    0x8e2a4357: (Hash, 0x0, 0x0, 0x0)
    mStandaloneLoadoutsLargeIcon: (String, 0x0, 0x0, 0x0)
    Level: (U32, 0x0, 0x0, 0x0)
    TftOnly: (Bool, 0x0, 0x0, 0x0)
    Finisher: (Pointer, 0x0, 0x0, TftFinisherData)
    mSkinId: (U32, 0x0, 0x0, 0x0)
    mStandaloneCircleIcon: (String, 0x0, 0x0, 0x0)
    FinisherCutscene: (Pointer, 0x0, 0x0, TftCutscene)
    FinisherCutscene: (Pointer, 0x0, 0x0, TftFinisherCutscene)
    CompanionType: (U8, 0x0, 0x0, 0x0)
    mLoadScreen: (String, 0x0, 0x0, 0x0)
    RotationalShopItemData: (Embed, 0x0, 0x0, TftRotationalShopItemData)
    pass

class GammaParameters():
    Contrast: (F32, 0x0, 0x0, 0x0)
    Brightness: (F32, 0x0, 0x0, 0x0)
    Level: (F32, 0x0, 0x0, 0x0)
    Gamma: (F32, 0x0, 0x0, 0x0)
    pass

class PfxAnimatedColorVariableData():
    Values: (List, 0x0, Vec4, 0x0)
    Times: (List, 0x0, F32, 0x0)
    ProbabilityTables: (List, 0x4, Pointer, PfxProbabilityTableData)
    pass

class ContextualConditionObjectiveTakeByMyTeam(IContextualCondition):
    mTakenObjective: (U32, 0x0, 0x0, 0x0)
    pass

class EndGameForLevelBlock(IScriptBlock):
    pass

class TftBotLoadoutConfiguration():
    MapSkins: (List, 0x0, Hash, 0x0)
    CompanionBuckets: (List, 0x0, Embed, TftCompanionBucket)
    pass

class SocialStatusIcons():
    OpenPartyStatusIcon: (Hash, 0x0, 0x0, 0x0)
    OnlineStatusIcon: (Hash, 0x0, 0x0, 0x0)
    MobileAppStatusIcon: (Hash, 0x0, 0x0, 0x0)
    OfflineStatusIcon: (Hash, 0x0, 0x0, 0x0)
    IngameStatusIcon: (Hash, 0x0, 0x0, 0x0)
    AwayStatusIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x7d09e1d2(TftInfoNubData):
    InactiveTitleKey: (String, 0x0, 0x0, 0x0)
    ActiveTitleKey: (String, 0x0, 0x0, 0x0)
    UnitProperty: (Link, 0x0, 0x0, TftUnitPropertyDefinition)
    InactiveBodyKey: (String, 0x0, 0x0, 0x0)
    ActiveBodyKey: (String, 0x0, 0x0, 0x0)
    pass

class TftStatData():
    mName: (String, 0x0, 0x0, 0x0)
    mType: (U32, 0x0, 0x0, 0x0)
    mLifetime: (U32, 0x0, 0x0, 0x0)
    mCollectors: (I32, 0x0, 0x0, 0x0)
    mContext: (U32, 0x0, 0x0, 0x0)
    pass

class SpellSlotBuffTimerData():
    TimerBorderBg: (Hash, 0x0, 0x0, 0x0)
    TimerBorderFx: (Hash, 0x0, 0x0, 0x0)
    TimerBarFill: (Hash, 0x0, 0x0, 0x0)
    TimerBarBg: (Hash, 0x0, 0x0, 0x0)
    pass

class TftNotificationData():
    mName: (String, 0x0, 0x0, 0x0)
    mBottomLineIcon1Path: (String, 0x0, 0x0, 0x0)
    mDurationSeconds: (F32, 0x0, 0x0, 0x0)
    mIconPath: (String, 0x0, 0x0, 0x0)
    mBottomLineIcon3Path: (String, 0x0, 0x0, 0x0)
    mBottomLineIcon2Path: (String, 0x0, 0x0, 0x0)
    mToplineTra: (String, 0x0, 0x0, 0x0)
    mBottomlineTra: (String, 0x0, 0x0, 0x0)
    pass

class IVfxShape():
    pass

class EmoteItemData():
    Intro: (Hash, 0x0, 0x0, 0x0)
    Portrait: (Hash, 0x0, 0x0, 0x0)
    PortraitFrame: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class TerrainLocation(TargetingTypeData):
    pass

class UiElementEffectData(UiElementAssetData):
    pass

class ItemModifier():
    mDescriptionToPrepend: (String, 0x0, 0x0, 0x0)
    0x20b65c83: (String, 0x0, 0x0, 0x0)
    mDeltaBuffCurrencyCostPercent: (F32, 0x0, 0x0, 0x0)
    mVisualPriority: (I32, 0x0, 0x0, 0x0)
    InventoryIconToOverlay: (String, 0x0, 0x0, 0x0)
    mMaximumDeltasToStack: (I32, 0x0, 0x0, 0x0)
    mDynamicTooltipToReplace: (String, 0x0, 0x0, 0x0)
    mDynamicTooltipToPrepend: (String, 0x0, 0x0, 0x0)
    mDeltaRequiredLevel: (I32, 0x0, 0x0, 0x0)
    mModifiedIfBuildsFromItem: (Link, 0x0, 0x0, ItemData)
    mModifiedGroup: (Link, 0x0, 0x0, ItemGroup)
    0x6d9d838: (Link, 0x0, 0x0, ItemData)
    mDynamicTooltipToAppend: (String, 0x0, 0x0, 0x0)
    mAddedBuildFrom: (List, 0x0, Link, ItemData)
    mIgnoreMaxGroupOwnable: (Bool, 0x0, 0x0, 0x0)
    mSpellNameToReplace: (String, 0x0, 0x0, 0x0)
    mDisplayNameToReplace: (String, 0x0, 0x0, 0x0)
    mRemovedBuildFrom: (List, 0x0, Link, ItemData)
    mModifiedItem: (Link, 0x0, 0x0, ItemData)
    mDescriptionToReplace: (String, 0x0, 0x0, 0x0)
    mDisplayNameToPrepend: (String, 0x0, 0x0, 0x0)
    mReplaceInsteadOfAddingBuildFrom: (Bool, 0x0, 0x0, 0x0)
    mModifierIsInheritedByOwnedParentItems: (Bool, 0x0, 0x0, 0x0)
    0x917537a9: (Link, 0x0, 0x0, ItemData)
    mDescriptionToAppend: (String, 0x0, 0x0, 0x0)
    mDeltaGoldCost: (F32, 0x0, 0x0, 0x0)
    mMinimumModifierInstancesToBeActive: (I32, 0x0, 0x0, 0x0)
    mDeltaGoldCostPercent: (F32, 0x0, 0x0, 0x0)
    mDeltaMaxStacks: (I32, 0x0, 0x0, 0x0)
    mMajorActiveItemToEnable: (Bool, 0x0, 0x0, 0x0)
    mDisplayNameToAppend: (String, 0x0, 0x0, 0x0)
    mItemModifierId: (Hash, 0x0, 0x0, 0x0)
    mShowAsModifiedInUi: (Bool, 0x0, 0x0, 0x0)
    mClickableToEnable: (Bool, 0x0, 0x0, 0x0)
    mMaximumModifierInstancesToBeActive: (I32, 0x0, 0x0, 0x0)
    mDeltaBuffCurrencyCost: (I32, 0x0, 0x0, 0x0)
    mIgnoreSpecificMaxGroupOwnable: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x7dc4f3ec():
    SubTeamNamePressed: (Hash, 0x0, 0x0, 0x0)
    PlayerSlotShroud: (Hash, 0x0, 0x0, 0x0)
    SubTeamNameSelected: (Hash, 0x0, 0x0, 0x0)
    SubTeamNameHovered: (Hash, 0x0, 0x0, 0x0)
    PlayerSlotTitleData: (Embed, 0x0, 0x0, LoadingScreenSummonerTitleData)
    PlayerSlotIconFrame: (Hash, 0x0, 0x0, 0x0)
    0x75ef08f0: (Hash, 0x0, 0x0, 0x0)
    PlayerSlotChampion: (Hash, 0x0, 0x0, 0x0)
    PlayerSlot: (Hash, 0x0, 0x0, 0x0)
    SubTeamPlayerRow: (Hash, 0x0, 0x0, 0x0)
    SubTeamButton: (Hash, 0x0, 0x0, 0x0)
    PlayerSlotIcon: (Hash, 0x0, 0x0, 0x0)
    SubTeam: (Hash, 0x0, 0x0, 0x0)
    PlayerSlotNameData: (Embed, 0x0, 0x0, LoadingScreenSummonerNameData)
    0xb2d1e4ec: (Hash, 0x0, 0x0, 0x0)
    PlayerSlotSplash: (Hash, 0x0, 0x0, 0x0)
    SubTeamColumn: (Hash, 0x0, 0x0, 0x0)
    SubTeamLogo: (Hash, 0x0, 0x0, 0x0)
    SubTeamPlayerColumn: (Hash, 0x0, 0x0, 0x0)
    SubTeamName: (Hash, 0x0, 0x0, 0x0)
    SubTeamNameInactive: (Hash, 0x0, 0x0, 0x0)
    pass

class SpellDataResourceClient():
    mTargeterDefinitions: (List, 0x0, Pointer, TargeterDefinition)
    mTooltipData: (Pointer, 0x0, 0x0, TooltipInstanceSpell)
    mRightClickSpellAction: (U32, 0x0, 0x0, 0x0)
    mUseTooltipFromAnotherSpell: (Hash, 0x0, 0x0, 0x0)
    mUseDeathRecapTooltipFromAnotherSpell: (Hash, 0x0, 0x0, 0x0)
    mLeftClickSpellAction: (U32, 0x0, 0x0, 0x0)
    mSpawningUiDefinition: (Pointer, 0x0, 0x0, SpawningUiDefinition)
    AddAdditionalReticleIfRequiredForGameMode: (Bool, 0x0, 0x0, 0x0)
    mCustomTargeterDefinitions: (Map, Hash, Embed, CustomTargeterDefinitions)
    mMissileTargeterDefinitions: (List, 0x0, Pointer, MissileAttachedTargetingDefinition)
    Keywords: (List2, 0x0, Hash, 0x0)
    pass

class IndividualScoreUiData():
    TooltipText: (String, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x7dfe3f97(0x26d26471):
    pass

class AnvilData(IAugment):
    ItemLink: (Hash, 0x0, 0x0, 0x0)
    AnvilTypes: (List2, 0x0, U8, 0x0)
    pass

class LoadingScreenChampionMasteryData():
    SlotHitRegion: (Hash, 0x0, 0x0, 0x0)
    SlotIcon: (Hash, 0x0, 0x0, 0x0)
    SlotGroup: (Hash, 0x0, 0x0, 0x0)
    MasteryOnlyDetailsText: (Hash, 0x0, 0x0, 0x0)
    SlotLayout: (Hash, 0x0, 0x0, 0x0)
    MasterySideIcon: (Hash, 0x0, 0x0, 0x0)
    MasteryOnlyGroup: (Hash, 0x0, 0x0, 0x0)
    0xa846c9e1: (Hash, 0x0, 0x0, 0x0)
    MasteryOnlyIcon: (Hash, 0x0, 0x0, 0x0)
    SlotDetailsText: (Hash, 0x0, 0x0, 0x0)
    SlotTitleText: (Hash, 0x0, 0x0, 0x0)
    MasteryOnlyTitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class IncrementalPurchaseDialog(PurchaseDialogBase):
    IncrementalLimitText: (Hash, 0x0, 0x0, 0x0)
    IncrementalTenUpButton: (Hash, 0x0, 0x0, 0x0)
    IncrementalCloseButtonRegion: (Hash, 0x0, 0x0, 0x0)
    IncrementalUpButtonText: (Hash, 0x0, 0x0, 0x0)
    IncrementalUpButton: (Hash, 0x0, 0x0, 0x0)
    IncrementalScene: (Hash, 0x0, 0x0, 0x0)
    IncrementalDownButtonText: (Hash, 0x0, 0x0, 0x0)
    IncrementalTenDownButtonText: (Hash, 0x0, 0x0, 0x0)
    IncrementalPurchaseItemIcon: (Hash, 0x0, 0x0, 0x0)
    IncrementalQtyText: (Hash, 0x0, 0x0, 0x0)
    IncrementalBodyText: (Hash, 0x0, 0x0, 0x0)
    IncrementalTenUpButtonText: (Hash, 0x0, 0x0, 0x0)
    IncrementalTenDownButton: (Hash, 0x0, 0x0, 0x0)
    IncrementalTitleText: (Hash, 0x0, 0x0, 0x0)
    IncrementalDownButton: (Hash, 0x0, 0x0, 0x0)
    pass

class UiSummonerSocialCardData():
    BackdropLink: (Hash, 0x0, 0x0, 0x0)
    ChampionNameLink: (Hash, 0x0, 0x0, 0x0)
    SummonerNameLink: (Hash, 0x0, 0x0, 0x0)
    SummonerIconLink: (Hash, 0x0, 0x0, 0x0)
    SceneLink: (Hash, 0x0, 0x0, 0x0)
    TaglineLink: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x7e173e2f(ILogicFloatDriver):
    VisibilityController: (Link, 0x0, 0x0, IMapVisibilityController)
    pass

class MapCharacterListContainer():
    CharacterLists: (List2, 0x0, Link, MapCharacterList)
    pass

class LoadingScreenRankedData():
    mRankedData: (Map, String, Embed, LoadingScreenRankedProperties)
    pass

class TftTrovesCelebrationCurrencySegmentData():
    GemMultiTimingOffset: (F32, 0x0, 0x0, 0x0)
    GemSingleAssetVfx: (Hash, 0x0, 0x0, 0x0)
    PortalTransitionOffset: (F32, 0x0, 0x0, 0x0)
    Sequence: (Link, 0x0, 0x0, Sequence)
    GemSingleTimingOffset: (F32, 0x0, 0x0, 0x0)
    GemMythicAssetVfx: (Hash, 0x0, 0x0, 0x0)
    GemMultiAssetVfx: (Hash, 0x0, 0x0, 0x0)
    GemMythicTimingOffset: (F32, 0x0, 0x0, 0x0)
    pass

class AiBuildingConfig(AiUnitConfigBase):
    DestroyedSkin: (String, 0x0, 0x0, 0x0)
    DestroyedCharacter: (String, 0x0, 0x0, 0x0)
    pass

class FxActionAnimate(IFxAction):
    PauseOnEnd: (Bool, 0x0, 0x0, 0x0)
    Loop: (Bool, 0x0, 0x0, 0x0)
    TargetObject: (Embed, 0x0, 0x0, FxTarget)
    TargetObject: (Embed, 0x0, 0x0, FxObjectSelector)
    AnimName: (String, 0x0, 0x0, 0x0)
    ScalePlaybackSpeedToDuration: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x7e59037():
    mValue: (Hash, 0x0, 0x0, 0x0)
    mClipName: (Hash, 0x0, 0x0, 0x0)
    pass

class FixedSpeedMovementSpec(MissileMovementSpec):
    mProjectTargetToCastRange: (Bool, 0x0, 0x0, 0x0)
    mSpeed: (F32, 0x0, 0x0, 0x0)
    mUseGroundHeightAtTarget: (Bool, 0x0, 0x0, 0x0)
    mInferDirectionFromFacingIfNeeded: (Bool, 0x0, 0x0, 0x0)
    mTargetHeightAugment: (F32, 0x0, 0x0, 0x0)
    pass

class OptionTemplateDropdown(IOptionTemplate):
    BoundsElement: (Hash, 0x0, 0x0, 0x0)
    LabelElement: (Hash, 0x0, 0x0, 0x0)
    ComboBoxBaseName: (String, 0x0, 0x0, 0x0)
    ComboBoxDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class LolModesRoundsListData(IGameModeConfig):
    Rounds: (List, 0x0, Link, LolModesRoundData)
    pass

class ContextualConditionHasItemFromVoGroup(IContextualCondition):
    mItemVoGroupHash: (Hash, 0x0, 0x0, 0x0)
    pass

class HudLevelUpData():
    IdleSheenInterval: (F32, 0x0, 0x0, 0x0)
    Delay: (F32, 0x0, 0x0, 0x0)
    MinAlpha: (F32, 0x0, 0x0, 0x0)
    MinAlpha: (U8, 0x0, 0x0, 0x0)
    AnimTime: (F32, 0x0, 0x0, 0x0)
    Overshoot: (F32, 0x0, 0x0, 0x0)
    PlayerBuffsOffeset: (F32, 0x0, 0x0, 0x0)
    MaxAlpha: (F32, 0x0, 0x0, 0x0)
    MaxAlpha: (U8, 0x0, 0x0, 0x0)
    MaxOffset: (F32, 0x0, 0x0, 0x0)
    PlayerBuffsOffset: (F32, 0x0, 0x0, 0x0)
    Inertia: (F32, 0x0, 0x0, 0x0)
    pass

class ScriptBtRootSequence(ScriptBtSequence):
    pass

class TftSurrenderViewController(VotePanelViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    DefaultTitleTra: (String, 0x0, 0x0, 0x0)
    DoneVotingTitleTra: (String, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class TftEventHubXsViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    EventTimer: (Pointer, 0x0, 0x0, TftEventTimer)
    InfoButton: (Hash, 0x0, 0x0, 0x0)
    MissionScroller: (Embed, 0x0, 0x0, 0xdd8ea5ae)
    SceneRoot: (Hash, 0x0, 0x0, 0x0)
    CloseButton: (Hash, 0x0, 0x0, 0x0)
    TrovesThumbnail: (Embed, 0x0, 0x0, 0x22dd5ebf)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x7edb8ffc(IFxActionInstance):
    pass

class DeathRecapDamagerCondensedList():
    DamagerPortraits: (List, 0x5, Hash, 0x0)
    DamagerKillerIcons: (List, 0x5, Hash, 0x0)
    pass

class AnchorBase():
    pass

class 0x7f0d46d7(TableValue):
    mValue: (F32, 0x0, 0x0, 0x0)
    Value: (F32, 0x0, 0x0, 0x0)
    pass

class HudMessageBox(ViewController):
    mLeftButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    mSoftKeyboardTransitionData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mCloseButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    mRightButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x7f2f1cd7(0x48eb8d47):
    OrEqualTo: (Bool, 0x0, 0x0, 0x0)
    LessThan: (I32, 0x0, 0x0, 0x0)
    pass

class MapActionPlaySoundAtLocation(MapAction):
    SoundEventName: (String, 0x0, 0x0, 0x0)
    LocationName: (String, 0x0, 0x0, 0x0)
    pass

class EnableAlways(IEnabler):
    pass

class ILoadoutInfoPanel():
    Scene: (Hash, 0x0, 0x0, 0x0)
    0x66b6aaa7: (F32, 0x0, 0x0, 0x0)
    0x8300af56: (I32, 0x0, 0x0, 0x0)
    ViewPaneDefinition: (Embed, 0x0, 0x0, ViewPaneDefinition)
    0xbd2f7d09: (String, 0x0, 0x0, 0x0)
    ViewPaneLink: (Hash, 0x0, 0x0, 0x0)
    pass

class MinimapPingEffectAndTextureData():
    mEnabled: (Bool, 0x0, 0x0, 0x0)
    mOrder: (Pointer, 0x0, 0x0, TextureAndColorData)
    mChaos: (Pointer, 0x0, 0x0, TextureAndColorData)
    mEffect: (Embed, 0x0, 0x0, MinimapPingEffectDefinition)
    mDefault: (Embed, 0x0, 0x0, TextureAndColorData)
    pass

class HudStatStoneData():
    mStatStoneRetiredIconName: (String, 0x0, 0x0, 0x0)
    mStatStoneRetiredIconMiniName: (String, 0x0, 0x0, 0x0)
    0x4ea59d14: (Bool, 0x0, 0x0, 0x0)
    pass

class VfxEmitterLegacySimple():
    BirthRotationalVelocity: (Embed, 0x0, 0x0, ValueFloat)
    Rotation: (Embed, 0x0, 0x0, ValueFloat)
    HasFixedOrbit: (Bool, 0x0, 0x0, 0x0)
    ScaleBias: (Vec2, 0x0, 0x0, 0x0)
    BirthScale: (Embed, 0x0, 0x0, ValueFloat)
    ParticleBind: (Vec2, 0x0, 0x0, 0x0)
    Scale: (Embed, 0x0, 0x0, ValueFloat)
    LockedToEmitter: (Bool, 0x0, 0x0, 0x0)
    BirthRotation: (Embed, 0x0, 0x0, ValueFloat)
    FixedOrbitType: (U8, 0x0, 0x0, 0x0)
    Orientation: (U8, 0x0, 0x0, 0x0)
    UvScrollRate: (Vec2, 0x0, 0x0, 0x0)
    ScaleUpFromOrigin: (Bool, 0x0, 0x0, 0x0)
    pass

class TextureResource(IResource):
    TexturePath: (String, 0x0, 0x0, 0x0)
    pass

class 0x7f8fce99(IScriptBlock, IBehaviorScriptBlock):
    pass

class GameModeEventManager():
    EventLists: (Map, String, Link, GameModeEventList)
    pass

class TftGameStartSequenceSimpleObject():
    pass

class SyncedAnimationEventData(BaseEventData):
    mGroupName: (Hash, 0x0, 0x0, 0x0)
    mLerpTime: (F32, 0x0, 0x0, 0x0)
    pass

class PlayerMuteViewController(ViewController):
    ChampionIconLink: (Hash, 0x0, 0x0, 0x0)
    ChampionNameLink: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    SummonerNameLink: (Hash, 0x0, 0x0, 0x0)
    BackgroundLink: (Hash, 0x0, 0x0, 0x0)
    MuteEmotesButton: (Hash, 0x0, 0x0, 0x0)
    MuteAllButton: (Hash, 0x0, 0x0, 0x0)
    MutePingsButton: (Hash, 0x0, 0x0, 0x0)
    MenuCloseButton: (Hash, 0x0, 0x0, 0x0)
    MuteChatButton: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x7fb92f53():
    0x28de30d6: (F32, 0x0, 0x0, 0x0)
    0x3c475337: (F32, 0x0, 0x0, 0x0)
    0x7e8cf11a: (F32, 0x0, 0x0, 0x0)
    0xc865acd9: (F32, 0x0, 0x0, 0x0)
    pass

class AnimationFractionDynamicMaterialFloatDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    mAnimationName: (Hash, 0x0, 0x0, 0x0)
    pass

class TargetingTypeData():
    pass

class ICharacter():
    pass

class ViewControllerSet():
    ListsToLoad: (List, 0x0, Link, ViewControllerList)
    ListsToLoad: (List2, 0x0, Link, ViewControllerList)
    ClientState: (String, 0x0, 0x0, 0x0)
    0x3f05d196: (Bool, 0x0, 0x0, 0x0)
    SpecifiedGameModes: (List, 0x0, String, 0x0)
    SpecifiedGameModes: (List2, 0x0, String, 0x0)
    pass

class ParTypeData():
    ShowRegen: (Bool, 0x0, 0x0, 0x0)
    States: (List, 0x0, Embed, ParStateData)
    ShowPar: (Bool, 0x0, 0x0, 0x0)
    pass

class ClampSubPartsCalculationPart(IGameCalculationPart):
    mCeiling: (Option, 0x0, F32, 0x0)
    mSubparts: (List, 0x0, Pointer, IGameCalculationPart)
    mFloor: (Option, 0x0, F32, 0x0)
    pass

class TftHudColorData():
    0x2558b51: (Color, 0x0, 0x0, 0x0)
    TftThreeStarColor: (Color, 0x0, 0x0, 0x0)
    TftActiveButtonTextColor: (Color, 0x0, 0x0, 0x0)
    0x3fdee6e4: (List, 0x4, Color, 0x0)
    0x425297af: (Color, 0x0, 0x0, 0x0)
    TftFriendlyColor: (Color, 0x0, 0x0, 0x0)
    TftInactiveButtonTextColor: (Color, 0x0, 0x0, 0x0)
    0x6b1a20e0: (Color, 0x0, 0x0, 0x0)
    0x6cfe6e40: (Color, 0x0, 0x0, 0x0)
    TftShopDropRateTextColors: (List, 0x5, Color, 0x0)
    TftActiveTextColor: (Color, 0x0, 0x0, 0x0)
    0xce60fb10: (Color, 0x0, 0x0, 0x0)
    TftShopDropRateTextColorsList: (List2, 0x0, Color, 0x0)
    TftChosenColor: (Color, 0x0, 0x0, 0x0)
    TftInactiveTextColor: (Color, 0x0, 0x0, 0x0)
    pass

class EffectGlowConstantElementData(EffectElementData):
    FlipX: (Bool, 0x0, 0x0, 0x0)
    FlipY: (Bool, 0x0, 0x0, 0x0)
    MinimumGlowMod: (F32, 0x0, 0x0, 0x0)
    MaximumGlowMod: (F32, 0x0, 0x0, 0x0)
    Atlas: (Pointer, 0x0, 0x0, AtlasData)
    PerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    pass

class TftMapCharacterData():
    SkinData: (List, 0x0, Embed, TftMapCharacterSkinData)
    Name: (String, 0x0, 0x0, 0x0)
    CharData: (List, 0x0, Embed, TftMapCharacterRecordData)
    pass

class HeroFloatingInfoBorderDefenseIconData():
    EnlargeSize: (F32, 0x0, 0x0, 0x0)
    SettleTime: (F32, 0x0, 0x0, 0x0)
    DefenseUpIcon: (Embed, 0x0, 0x0, HeroFloatingInfoBorderDefenseIconThresholdData)
    EnlargeTime: (F32, 0x0, 0x0, 0x0)
    DefenseDownIcons: (List, 0x3, Embed, HeroFloatingInfoBorderDefenseIconThresholdData)
    LeftIconRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class CinematicBarsViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    BottomBlackBar: (Hash, 0x0, 0x0, 0x0)
    BottomScene: (Hash, 0x0, 0x0, 0x0)
    TopBlackBar: (Hash, 0x0, 0x0, 0x0)
    RightScene: (Hash, 0x0, 0x0, 0x0)
    TopScene: (Hash, 0x0, 0x0, 0x0)
    RightBlackBar: (Hash, 0x0, 0x0, 0x0)
    LeftBlackBar: (Hash, 0x0, 0x0, 0x0)
    LeftScene: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionTurretPosition(IContextualCondition):
    mTurretPosition: (U8, 0x0, 0x0, 0x0)
    pass

class ProgressionGraph():
    RootNodes: (List, 0x0, Link, ProgressionNode)
    pass

class 0x810de4e7(ISequenceAction):
    ContinueAt: (U8, 0x0, 0x0, 0x0)
    pass

class FloatingTextGlobalConfig():
    mDamageDisplayTypes: (Embed, 0x0, 0x0, FloatingTextDamageDisplayTypeList)
    mTunables: (Embed, 0x0, 0x0, FloatingTextTunables)
    mFloatingTextTypes: (Embed, 0x0, 0x0, FloatingTextTypeList)
    pass

class GameStateViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    ObjectName: (String, 0x0, 0x0, 0x0)
    Metrics: (List, 0x0, Pointer, UiMetricTypeI)
    Metrics: (List2, 0x0, Pointer, UiMetricTypeI)
    pass

class BarracksMinionConfig():
    MinionType: (U8, 0x0, 0x0, 0x0)
    WaveBehavior: (Pointer, 0x0, 0x0, IMinionWaveBehavior)
    MinionUpgradeStats: (Embed, 0x0, 0x0, MinionUpgradeConfig)
    MinionConfig: (Embed, 0x0, 0x0, 0x1778b398)
    MinionConfig: (Embed, 0x0, 0x0, AiUnitConfigLink)
    pass

class EffectAnimatedRotatingIconElementData(EffectAnimationElementData):
    pass

class UiReplayTeamFramesData():
    MemberTemplate: (Embed, 0x0, 0x0, UiTeamMemberData)
    Scene: (Hash, 0x0, 0x0, 0x0)
    Layout: (Hash, 0x0, 0x0, 0x0)
    pass

class ShaderPhysicalParameter():
    LogicalParamters: (List, 0x0, Embed, ShaderLogicalParameter)
    LogicalParameters: (List, 0x0, Embed, ShaderLogicalParameter)
    Name: (String, 0x0, 0x0, 0x0)
    Data: (Vec4, 0x0, 0x0, 0x0)
    pass

class ShaderMacroDef():
    Definition: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class LookAtInterestAngleParametricUpdater(IFloatParametricUpdater):
    pass

class UiLevelUpButtonEasingData():
    AnimTimeSecs: (F32, 0x0, 0x0, 0x0)
    DelaySecs: (F32, 0x0, 0x0, 0x0)
    MinAlpha: (U8, 0x0, 0x0, 0x0)
    Overshoot: (F32, 0x0, 0x0, 0x0)
    MaxAlpha: (U8, 0x0, 0x0, 0x0)
    MaxOffset: (F32, 0x0, 0x0, 0x0)
    Inertia: (F32, 0x0, 0x0, 0x0)
    IdleSheenIntervalSecs: (F32, 0x0, 0x0, 0x0)
    pass

class 0x8190bc9f():
    QuantityText: (Hash, 0x0, 0x0, 0x0)
    ItemTemplate: (Hash, 0x0, 0x0, 0x0)
    LegendaryVfx: (Hash, 0x0, 0x0, 0x0)
    CurrencyTemplate: (Hash, 0x0, 0x0, 0x0)
    Parent: (Hash, 0x0, 0x0, 0x0)
    pass

class PlayerProfileMatchHistoryView():
    MatchHistoryTraitTemplate: (Embed, 0x0, 0x0, MatchHistoryTraitTemplate)
    NoMatchHistoryText: (Hash, 0x0, 0x0, 0x0)
    MatchHistoryScene: (Hash, 0x0, 0x0, 0x0)
    MainContentViewPane: (Hash, 0x0, 0x0, 0x0)
    LoadingSpinnerVfx: (Hash, 0x0, 0x0, 0x0)
    MatchHistoryListScene: (Hash, 0x0, 0x0, 0x0)
    MatchHistoryPlayerTemplate: (Embed, 0x0, 0x0, MatchHistoryPlayerTemplate)
    MainViewPaneDefinition: (Pointer, 0x0, 0x0, ViewPaneDefinition)
    MatchHistoryGrid: (Hash, 0x0, 0x0, 0x0)
    MatchHistoryUnitTemplate: (Embed, 0x0, 0x0, MatchHistoryUnitTemplate)
    pass

class EffectCooldownRadialElementData(EffectElementData):
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    mIsFill: (Bool, 0x0, 0x0, 0x0)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    pass

class StatStoneMilestoneVfxDefinition():
    FlameEffectElement: (Hash, 0x0, 0x0, 0x0)
    RekindledEffectElement: (Hash, 0x0, 0x0, 0x0)
    GlowEffectElement: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x81fe2d71(IBehaviorScriptBlock):
    pass

class 0x820c053(ILogicBoolDriver):
    SkinAugment: (Hash, 0x0, 0x0, 0x0)
    pass

class ConformToPathEventData(BaseEventData):
    mMaskDataName: (Hash, 0x0, 0x0, 0x0)
    mBlendOutTime: (F32, 0x0, 0x0, 0x0)
    mBlendInTime: (F32, 0x0, 0x0, 0x0)
    pass

class VfxMigrationResources():
    ResourceMap: (Map, Hash, Link, VfxSystemDefinitionData)
    pass

class SelectJungleSpellBlock(SelectSpellBlock):
    pass

class 0x8263e1d():
    0x749450fd: (F32, 0x0, 0x0, 0x0)
    0x86749f57: (U8, 0x0, 0x0, 0x0)
    0xc0a408e8: (F32, 0x0, 0x0, 0x0)
    0xfb841f25: (F32, 0x0, 0x0, 0x0)
    pass

class TftMapItemData():
    ItemId: (U32, 0x0, 0x0, 0x0)
    Description: (String, 0x0, 0x0, 0x0)
    IconPath: (String, 0x0, 0x0, 0x0)
    NameId: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    EffectAmounts: (List, 0x0, Embed, TftEffectAmount)
    ArmoryIconPath: (String, 0x0, 0x0, 0x0)
    pass

class ItemRecommendationContextList():
    mAllRecommendableItemIds: (Map, U32, Embed, ItemRecommendationItemList)
    mAllStartingItemIds: (Map, U32, Embed, ItemRecommendationItemList)
    mContexts: (List, 0x0, Embed, ItemRecommendationContext)
    pass

class UiElementGroupMeterData(UiElementGroupData):
    TipStyle: (Pointer, 0x0, 0x0, TipStyleBase)
    TipStyle: (U8, 0x0, 0x0, 0x0)
    BarElements: (List, 0x0, Link, ElementDataI)
    BarElements: (List, 0x0, Link, UiElementIData)
    BarElements: (List2, 0x0, Link, UiElementIData)
    BarTipElements: (List, 0x0, Link, ElementDataI)
    FillDirection: (U8, 0x0, 0x0, 0x0)
    IsEnabled: (Bool, 0x0, 0x0, 0x0)
    StartPercentage: (F32, 0x0, 0x0, 0x0)
    pass

class 0x82b08474(BaseLoadoutData):
    mBuffName: (String, 0x0, 0x0, 0x0)
    mChampion: (Hash, 0x0, 0x0, 0x0)
    mBuffData: (Embed, 0x0, 0x0, BuffData)
    pass

class 0x82ba1aba(ILolSpellScriptEvent):
    pass

class CherryCombatInfoDisplayViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    0x28c91c47: (Hash, 0x0, 0x0, 0x0)
    CameoDisplayData: (Embed, 0x0, 0x0, 0x3519dc31)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TeamRightDisplay: (Embed, 0x0, 0x0, CherryCombatInfoDisplayTeam)
    0x493e057d: (String, 0x0, 0x0, 0x0)
    0x5c649b88: (Hash, 0x0, 0x0, 0x0)
    TeamLeftDisplay: (Embed, 0x0, 0x0, CherryCombatInfoDisplayTeam)
    0x641fb629: (String, 0x0, 0x0, 0x0)
    0x7a8c9cb1: (Hash, 0x0, 0x0, 0x0)
    SelfLifeHealthTextColor: (Color, 0x0, 0x0, 0x0)
    0x8c0f3208: (F32, 0x0, 0x0, 0x0)
    EnemyLifeHealthTextColor: (Color, 0x0, 0x0, 0x0)
    0xb620637e: (Hash, 0x0, 0x0, 0x0)
    0xc0f962db: (F32, 0x0, 0x0, 0x0)
    0xc7463e46: (String, 0x0, 0x0, 0x0)
    pass

class GameModeCharacterList():
    CharacterLists: (List, 0x0, Link, MapCharacterList)
    GameMode: (U32, 0x0, 0x0, 0x0)
    pass

class 0x82ece567():
    ItemTemplate: (Hash, 0x0, 0x0, 0x0)
    Parent: (Hash, 0x0, 0x0, 0x0)
    pass

class TftTrovesBannerReward(TftTrovesBannerNode):
    Quantity: (U32, 0x0, 0x0, 0x0)
    Rarity: (U32, 0x0, 0x0, 0x0)
    RewardTexturePath: (String, 0x0, 0x0, 0x0)
    0x8e2a4357: (Hash, 0x0, 0x0, 0x0)
    IsChaseReward: (Bool, 0x0, 0x0, 0x0)
    HighlightVfx: (Hash, 0x0, 0x0, 0x0)
    pass

class SbObjectiveBounties():
    TowersValue: (Hash, 0x0, 0x0, 0x0)
    RiftHeraldValue: (Hash, 0x0, 0x0, 0x0)
    DragonsScore: (Hash, 0x0, 0x0, 0x0)
    TowerScore: (Hash, 0x0, 0x0, 0x0)
    DragonsValue: (Hash, 0x0, 0x0, 0x0)
    BaronScore: (Hash, 0x0, 0x0, 0x0)
    BaronValue: (Hash, 0x0, 0x0, 0x0)
    0x7681fe9f: (Hash, 0x0, 0x0, 0x0)
    HordeIcon: (Hash, 0x0, 0x0, 0x0)
    RiftHeraldScore: (Hash, 0x0, 0x0, 0x0)
    RiftHeraldCampName: (Hash, 0x0, 0x0, 0x0)
    0xaec651cc: (Hash, 0x0, 0x0, 0x0)
    DragonsIcon: (Hash, 0x0, 0x0, 0x0)
    TowerIcon: (Hash, 0x0, 0x0, 0x0)
    RiftHeraldIcon: (Hash, 0x0, 0x0, 0x0)
    HordeScore: (Hash, 0x0, 0x0, 0x0)
    0xcfe173b: (Hash, 0x0, 0x0, 0x0)
    BaronIcon: (Hash, 0x0, 0x0, 0x0)
    HordeValue: (Hash, 0x0, 0x0, 0x0)
    pass

class IStringCalculation():
    pass

class VfxEmitterAudio():
    SoundPersistent: (String, 0x0, 0x0, 0x0)
    SoundOnCreate: (String, 0x0, 0x0, 0x0)
    pass

class FogOfWarProperties():
    Upscale: (Bool, 0x0, 0x0, 0x0)
    FadeToFoggedValue: (F32, 0x0, 0x0, 0x0)
    FadeFinish: (F32, 0x0, 0x0, 0x0)
    EdgeTintPoint: (F32, 0x0, 0x0, 0x0)
    FadeStart: (F32, 0x0, 0x0, 0x0)
    BlurKernelSigma: (F32, 0x0, 0x0, 0x0)
    UvAnimate: (Vec4, 0x0, 0x0, 0x0)
    MutatorToTextureMap: (Map, String, String, 0x0)
    pass

class StoreDialogViewController(ModalDialogViewController):
    0x5e4fd785: (String, 0x0, 0x0, 0x0)
    GridMaxSize: (U32, 0x0, 0x0, 0x0)
    FooterHyperlinks: (List, 0x0, Embed, UiHyperlink)
    0x8a8c8671: (Hash, 0x0, 0x0, 0x0)
    OfferGrid: (Hash, 0x0, 0x0, 0x0)
    0xab3d2798: (String, 0x0, 0x0, 0x0)
    UiStoreItemTileData: (Embed, 0x0, 0x0, UiStoreItemTileData)
    0xd42a98f8: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x834e2e8d():
    Tall: (List, 0x4, Embed, UiRotationalStoreItemTileData)
    Error: (Hash, 0x0, 0x0, 0x0)
    Region: (Hash, 0x0, 0x0, 0x0)
    Divider: (Hash, 0x0, 0x0, 0x0)
    Timer: (Pointer, 0x0, 0x0, TftEventTimer)
    Group: (Hash, 0x0, 0x0, 0x0)
    Single: (List, 0x8, Embed, UiRotationalStoreItemTileData)
    Title: (Hash, 0x0, 0x0, 0x0)
    0xbbfd8261: (String, 0x0, 0x0, 0x0)
    Long: (List, 0x6, Embed, UiRotationalStoreItemTileData)
    LargeSquare: (List, 0x3, Embed, UiRotationalStoreItemTileData)
    pass

class LolBehaviorScript(BehaviorScript):
    Sequences: (Map, U32, Embed, ScriptBtSequence)
    pass

class ReturnChildrenOnMovementCompleteSpec(MissileBehaviorSpec):
    mDelay: (I32, 0x0, 0x0, 0x0)
    mDistanceOffset: (F32, 0x0, 0x0, 0x0)
    mReturnTime: (F32, 0x0, 0x0, 0x0)
    pass

class TempTable1(ScriptTable):
    pass

class 0x839f4f73():
    BannerTexturePath: (String, 0x0, 0x0, 0x0)
    PityThreshold: (U32, 0x0, 0x0, 0x0)
    Id: (String, 0x0, 0x0, 0x0)
    ChaseTable: (Link, 0x0, 0x0, 0xb0617ced)
    ActivationDateTime: (String, 0x0, 0x0, 0x0)
    DeactivationDateTime: (String, 0x0, 0x0, 0x0)
    BannerCurrencyId: (String, 0x0, 0x0, 0x0)
    ThumbnailTexturePath: (String, 0x0, 0x0, 0x0)
    NameTraKey: (String, 0x0, 0x0, 0x0)
    PityCounterId: (String, 0x0, 0x0, 0x0)
    RootTable: (Link, 0x0, 0x0, 0xb0617ced)
    DescriptionTraKey: (String, 0x0, 0x0, 0x0)
    MythicTokenOfferId: (String, 0x0, 0x0, 0x0)
    pass

class CherryTeamFlyoutPanelViewController(ViewController):
    0x1bb70a95: (F32, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    BackgroundFrame: (Hash, 0x0, 0x0, 0x0)
    TeamOpponentTemplate: (Embed, 0x0, 0x0, CherryTeamFlyoutPanelTeamTemplate)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TeamSelfTemplate: (Embed, 0x0, 0x0, CherryTeamFlyoutPanelTeamTemplate)
    pass

class ViewControllerListFilterI():
    pass

class ContextualConditionCharacterPlayingAnimation(ICharacterSubcondition):
    mAnimationNameHash: (Hash, 0x0, 0x0, 0x0)
    pass

class IUiEffectTextureDataProvider():
    pass

class 0x8411fe45(IBehaviorScriptBlock):
    Position: (Pointer, 0x0, 0x0, IVectorGet)
    0xbf301458: (Pointer, 0x0, 0x0, IBoolGet)
    pass

class ToggleBuffCheat(Cheat):
    mBuffName: (String, 0x0, 0x0, 0x0)
    mTarget: (U32, 0x0, 0x0, 0x0)
    UseTargetAsCaster: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x8444401a():
    Scene: (Hash, 0x0, 0x0, 0x0)
    0x3bee2696: (Hash, 0x0, 0x0, 0x0)
    0x6daf08ed: (String, 0x0, 0x0, 0x0)
    0x91bad98c: (U8, 0x0, 0x0, 0x0)
    MatchupSlot: (Embed, 0x0, 0x0, 0x135a0579)
    Layout: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x84721309(0x7546469c):
    pass

class ElementSoundEvents():
    RollOutEvent: (String, 0x0, 0x0, 0x0)
    MouseDownOnInactive: (String, 0x0, 0x0, 0x0)
    MouseUpEvent: (String, 0x0, 0x0, 0x0)
    RolloverEvent: (String, 0x0, 0x0, 0x0)
    MouseUpOnInactive: (String, 0x0, 0x0, 0x0)
    MouseDownEvent: (String, 0x0, 0x0, 0x0)
    pass

class HomeViewController(ViewController):
    RewardReadyVfx: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    SpecialOfferButton: (Hash, 0x0, 0x0, 0x0)
    0x2f7e9ed: (String, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    CompleteText: (Hash, 0x0, 0x0, 0x0)
    BattlepassButton: (Hash, 0x0, 0x0, 0x0)
    0x541d4879: (Link, 0x0, 0x0, StoreListingData)
    ThemeMusicState: (String, 0x0, 0x0, 0x0)
    TeamPlannerButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    WelcomeDialogViewController: (Link, 0x0, 0x0, ModalDialogViewController)
    BattlepassSpacer: (Hash, 0x0, 0x0, 0x0)
    LevelText: (Hash, 0x0, 0x0, 0x0)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    EventTimer: (Pointer, 0x0, 0x0, TftEventTimer)
    ModeSelectButton: (Hash, 0x0, 0x0, 0x0)
    PremiumText: (Hash, 0x0, 0x0, 0x0)
    VietnameseRatingLabel: (Hash, 0x0, 0x0, 0x0)
    PlayGameButtonHint: (Pointer, 0x0, 0x0, TftHintUiData)
    PlayGameButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    RewardsMeterAnimEaseType: (U32, 0x0, 0x0, 0x0)
    RewardsMeterAnimEaseType: (U8, 0x0, 0x0, 0x0)
    ButtonVerticalLayout: (Hash, 0x0, 0x0, 0x0)
    0x8e3bfb69: (Link, 0x0, 0x0, ModalDialogViewController)
    TrovesButton: (Hash, 0x0, 0x0, 0x0)
    PromoBannerView: (Embed, 0x0, 0x0, HomeViewPromoBanner)
    RewardReadyPip: (Hash, 0x0, 0x0, 0x0)
    PromoDialogViewController: (Link, 0x0, 0x0, ModalDialogViewController)
    PassText: (Hash, 0x0, 0x0, 0x0)
    SpecialOfferView: (Embed, 0x0, 0x0, HomeViewSpecialOffer)
    SpecialOfferButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    TeamPlannerButton: (Hash, 0x0, 0x0, 0x0)
    XboxGamePassIntroDialogViewController: (Link, 0x0, 0x0, ModalDialogViewController)
    PlayGameButton: (Hash, 0x0, 0x0, 0x0)
    SpecialOfferToastScene: (Hash, 0x0, 0x0, 0x0)
    XboxGamePassEndedDialogViewController: (Link, 0x0, 0x0, ModalDialogViewController)
    StoreNewPip: (Embed, 0x0, 0x0, 0x6241da2)
    EventHubButton: (Hash, 0x0, 0x0, 0x0)
    RewardsHintMessage: (Pointer, 0x0, 0x0, TftHintUiData)
    ModeSelectCustomButtonData: (List, 0x0, Embed, ModeSelectButtonData)
    StoreButton: (Hash, 0x0, 0x0, 0x0)
    ThemeMusicStateGroup: (String, 0x0, 0x0, 0x0)
    0xd24a7af6: (Hash, 0x0, 0x0, 0x0)
    BattlepassToastView: (Embed, 0x0, 0x0, HomeViewSpecialOffer)
    StoreButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    RewardsMeterAnimTimeSecs: (F32, 0x0, 0x0, 0x0)
    NewPip: (Embed, 0x0, 0x0, 0x6241da2)
    ModeSelectDefaultButtonIcons: (Embed, 0x0, 0x0, UiElementGroupButtonAdditionalElements)
    ModeSelectDefaultButtonData: (Hash, 0x0, 0x0, 0x0)
    BattlepassButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    0xe5640335: (Link, 0x0, 0x0, ModalDialogViewController)
    RewardsMeter: (Embed, 0x0, 0x0, UiMilestoneProgressMeter)
    0xe8a2e9e9: (Hash, 0x0, 0x0, 0x0)
    0xe9431731: (Link, 0x0, 0x0, ModalDialogViewController)
    SpecialOfferController: (Embed, 0x0, 0x0, SpecialOfferController)
    pass

class HealthBarSettingsData():
    mGoTransparent: (Bool, 0x0, 0x0, 0x0)
    mMegaTickThickness: (F32, 0x0, 0x0, 0x0)
    mMaxHealthTicks: (U32, 0x0, 0x0, 0x0)
    mTickThickness: (F32, 0x0, 0x0, 0x0)
    mMicroTickThickness: (F32, 0x0, 0x0, 0x0)
    mMaxHealthMicroTicks: (U32, 0x0, 0x0, 0x0)
    mTickAlpha: (U32, 0x0, 0x0, 0x0)
    mHealthPerMicroTick: (F32, 0x0, 0x0, 0x0)
    mMegaTickAlpha: (U32, 0x0, 0x0, 0x0)
    mMicroTickHeight: (F32, 0x0, 0x0, 0x0)
    mMicroTickAlpha: (U32, 0x0, 0x0, 0x0)
    mUseCompression: (Bool, 0x0, 0x0, 0x0)
    mHealthPerMegaTick: (F32, 0x0, 0x0, 0x0)
    mHealthPerTick: (F32, 0x0, 0x0, 0x0)
    pass

class TftEncounterData(0x3e02c8d9):
    ExcludedEncounters: (List2, 0x0, Link, TftEncounterData)
    ExcludedAugments: (List2, 0x0, Link, TftItemData)
    AllowedStages: (List2, 0x0, I32, 0x0)
    ExcludedEncounterTags: (List2, 0x0, Hash, 0x0)
    EncounterTooltip: (Link, 0x0, 0x0, TftTooltipData)
    EncounterLength: (F32, 0x0, 0x0, 0x0)
    0x74cf1ad1: (String, 0x0, 0x0, 0x0)
    EncounterLocation: (U8, 0x0, 0x0, 0x0)
    ExcludedAugmentTags: (List2, 0x0, Hash, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    BuffName: (String, 0x0, 0x0, 0x0)
    VfxResourceResolver: (Hash, 0x0, 0x0, 0x0)
    SkinName: (String, 0x0, 0x0, 0x0)
    ItemList: (List2, 0x0, Link, TftItemData)
    RoundPlacement: (U8, 0x0, 0x0, 0x0)
    0xac397529: (F32, 0x0, 0x0, 0x0)
    ScriptData: (Map, String, Pointer, GameModeConstant)
    EncounterTags: (List2, 0x0, Hash, 0x0)
    ExcludedPortals: (List2, 0x0, Link, 0xb3f382ff)
    0xee030e3d: (U8, 0x0, 0x0, 0x0)
    0xf1f30bb9: (List2, 0x0, I32, 0x0)
    pass

class SumOfSubPartsCalculationPart(IGameCalculationPart, ISpellCalculationPart):
    mSubparts: (List, 0x0, Pointer, IGameCalculationPart)
    mSubparts: (List, 0x0, Pointer, ISpellCalculationPart)
    pass

class BattleBunnyMissFortuneViewController(0x6d8274d, ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BunnyElementOffStates: (List, 0x0, Hash, 0x0)
    BunnyElementOnStates: (List, 0x0, Hash, 0x0)
    EyeCandy: (Bool, 0x0, 0x0, 0x0)
    Loadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TransitionOnState: (Hash, 0x0, 0x0, 0x0)
    TransitionOffState: (Hash, 0x0, 0x0, 0x0)
    BunnyElements: (List, 0x0, Embed, UiElementToggle)
    pass

class 0x84c56837():
    Empty: (Hash, 0x0, 0x0, 0x0)
    Empty: (List2, 0x0, Hash, 0x0)
    Win: (Hash, 0x0, 0x0, 0x0)
    Win: (List2, 0x0, Hash, 0x0)
    Loss: (Hash, 0x0, 0x0, 0x0)
    Loss: (List2, 0x0, Hash, 0x0)
    pass

class ChatViewData():
    ThrottlerData: (Embed, 0x0, 0x0, ChatThrottlerData)
    ViewPaneDefinition: (Embed, 0x0, 0x0, ViewPaneDefinition)
    pass

class PfxSimpleEmitterDefinitionData():
    FluidDynamicsDefinition: (Pointer, 0x0, 0x0, 0xdb7c04f8)
    FieldCollectionDefinition: (Embed, 0x0, 0x0, PfxFieldCollectionDefinitionData)
    pass

class ItemDataClient():
    mForcePingable: (Bool, 0x0, 0x0, 0x0)
    mFloatVarsDecimals: (List, 0x10, I32, 0x0)
    InventoryIconLarge: (String, 0x0, 0x0, 0x0)
    mTooltipData: (Pointer, 0x0, 0x0, TooltipInstanceItem)
    mShopTooltip: (String, 0x0, 0x0, 0x0)
    Epicness: (U32, 0x0, 0x0, 0x0)
    Epicness: (U8, 0x0, 0x0, 0x0)
    EffectRadius: (F32, 0x0, 0x0, 0x0)
    mDeathRecapDescription: (String, 0x0, 0x0, 0x0)
    mDynamicTooltip: (String, 0x0, 0x0, 0x0)
    InventoryIcon: (String, 0x0, 0x0, 0x0)
    ShopExtendedTooltip: (String, 0x0, 0x0, 0x0)
    InventoryIconMaterial: (Link, 0x0, 0x0, StaticMaterialDef)
    InventoryIconSmall: (String, 0x0, 0x0, 0x0)
    mDescription: (String, 0x0, 0x0, 0x0)
    pass

class 0x851b8dc5(IBehaviorScriptBlock):
    Var: (Pointer, 0x0, 0x0, ScriptTableSet)
    pass

class TftMapGroupData():
    mName: (String, 0x0, 0x0, 0x0)
    mId: (U32, 0x0, 0x0, 0x0)
    pass

class StaticMaterialPassDef():
    StencilReferenceId: (Hash, 0x0, 0x0, 0x0)
    SrcColorBlendFactor: (U32, 0x0, 0x0, 0x0)
    FogColor: (Color, 0x0, 0x0, 0x0)
    BlendEnable: (Bool, 0x0, 0x0, 0x0)
    Shader: (Link, 0x0, 0x0, IShaderDef)
    DepthOffsetSlope: (F32, 0x0, 0x0, 0x0)
    StencilEnable: (Bool, 0x0, 0x0, 0x0)
    AlphaTestCompareFunc: (U32, 0x0, 0x0, 0x0)
    CullEnable: (Bool, 0x0, 0x0, 0x0)
    WindingToCull: (U32, 0x0, 0x0, 0x0)
    StencilPassDepthPassOp: (U32, 0x0, 0x0, 0x0)
    DstAlphaBlendFactor: (U32, 0x0, 0x0, 0x0)
    BlendEquation: (U32, 0x0, 0x0, 0x0)
    StencilCompareFunc: (U32, 0x0, 0x0, 0x0)
    SrcAlphaBlendFactor: (U32, 0x0, 0x0, 0x0)
    DepthCompareFunc: (U32, 0x0, 0x0, 0x0)
    PolygonDepthBiasEnable: (Bool, 0x0, 0x0, 0x0)
    StencilPassDepthFailOp: (U32, 0x0, 0x0, 0x0)
    StencilMask: (U32, 0x0, 0x0, 0x0)
    WriteMask: (U32, 0x0, 0x0, 0x0)
    DstColorBlendFactor: (U32, 0x0, 0x0, 0x0)
    FogEnable: (Bool, 0x0, 0x0, 0x0)
    StencilReferenceVal: (U32, 0x0, 0x0, 0x0)
    StencilReferenceVal: (U8, 0x0, 0x0, 0x0)
    AlphaTestNormalizedReferenceValue: (F32, 0x0, 0x0, 0x0)
    AlphaTestEnable: (Bool, 0x0, 0x0, 0x0)
    ParamValues: (List, 0x0, Embed, StaticMaterialShaderParamDef)
    DepthEnable: (Bool, 0x0, 0x0, 0x0)
    StencilFailOp: (U32, 0x0, 0x0, 0x0)
    ShaderMacros: (Map, String, String, 0x0)
    DepthOffsetBias: (F32, 0x0, 0x0, 0x0)
    pass

class RsComparisonCondition(IRsCondition):
    Operation: (U32, 0x0, 0x0, 0x0)
    Value2: (Pointer, 0x0, 0x0, IRsValueGet)
    Value1: (Pointer, 0x0, 0x0, IRsValueGet)
    pass

class StealthCharacterFade():
    FadeAmount: (F32, 0x0, 0x0, 0x0)
    OwnerOnly: (Bool, 0x0, 0x0, 0x0)
    FadeTime: (F32, 0x0, 0x0, 0x0)
    IsPersistentPacket: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x856ba9bc(ViewController):
    pass

class TempTable3(ScriptTable):
    pass

class ForceSpawnNeutralCampsCheat(Cheat):
    mSpawnBaron: (Bool, 0x0, 0x0, 0x0)
    0x3378edaf: (Bool, 0x0, 0x0, 0x0)
    pass

class VfxPrimitiveMesh(VfxPrimitiveMeshBase):
    pass

class VfxComplexEmitterDefinitionData():
    DoesParticleLifetimeScale: (Bool, 0x0, 0x0, 0x0)
    ReflectionOpacityDirect: (F32, 0x0, 0x0, 0x0)
    ReflectionFresnel: (F32, 0x0, 0x0, 0x0)
    SubmeshesToDraw: (List, 0x0, U32, 0x0)
    KeywordsRequired: (List, 0x0, String, 0x0)
    TexDivMult: (Vec2, 0x0, 0x0, 0x0)
    ReflectionOpacityGlancing: (F32, 0x0, 0x0, 0x0)
    VoiceOverPersistentName: (String, 0x0, 0x0, 0x0)
    TimeActiveDuringPeriod: (F32, 0x0, 0x0, 0x0)
    TimeActiveDuringPeriod: (Option, 0x0, F32, 0x0)
    BirthRotationalVelocity: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    UvScroll: (Vec2, 0x0, 0x0, 0x0)
    BirthTilingSize: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    ScaleEmitOffsetByBoundObjectHeight: (F32, 0x0, 0x0, 0x0)
    NumFrames: (I32, 0x0, 0x0, 0x0)
    EmissionMeshName: (String, 0x0, 0x0, 0x0)
    Rotation: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    TimeBeforeFirstEmission: (F32, 0x0, 0x0, 0x0)
    ParticleLinger: (F32, 0x0, 0x0, 0x0)
    bState: (U32, 0x0, 0x0, 0x0)
    FlexBirthUvoffset: (Embed, 0x0, 0x0, FlexValueVector2)
    ColorLookUpTypeX: (U32, 0x0, 0x0, 0x0)
    UvMode: (U32, 0x0, 0x0, 0x0)
    ColorLookUpTypeY: (U32, 0x0, 0x0, 0x0)
    ProjectionYRange: (F32, 0x0, 0x0, 0x0)
    ParticleLifetime: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    IsLocalOrientation: (Bool, 0x0, 0x0, 0x0)
    FlexScaleBirthScale: (Embed, 0x0, 0x0, FlexTypeFloat)
    SubmeshesToDrawAlways: (List, 0x0, U32, 0x0)
    TextureMult: (String, 0x0, 0x0, 0x0)
    Acceleration: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    TexAddressModeBase: (U32, 0x0, 0x0, 0x0)
    Velocity: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    MaterialOverrideDefinitions: (List, 0x0, Embed, VfxMaterialOverrideDefinitionData)
    MaterialOverrideDefinitions: (List, 0x0, Pointer, VfxMaterialOverrideDefinitionData)
    BirthRotationalAcceleration: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    ScaleBirthScaleByBoundObjectRadius: (F32, 0x0, 0x0, 0x0)
    MeshTextureName: (String, 0x0, 0x0, 0x0)
    FresnelColor: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    EmitterLinger: (F32, 0x0, 0x0, 0x0)
    Texture: (String, 0x0, 0x0, 0x0)
    EmitterName: (String, 0x0, 0x0, 0x0)
    Color: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    DistortionMode: (U32, 0x0, 0x0, 0x0)
    QuadType: (U32, 0x0, 0x0, 0x0)
    IsSingleParticle: (Bool, 0x0, 0x0, 0x0)
    KeywordsIncluded: (List, 0x0, String, 0x0)
    BirthScale: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    OffsetLifeScalingSymmetryMode: (U32, 0x0, 0x0, 0x0)
    RateByVelocityFunction: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    BirthOrbitalVelocity: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    VoiceOverOnCreateName: (String, 0x0, 0x0, 0x0)
    Lifetime: (F32, 0x0, 0x0, 0x0)
    Lifetime: (Option, 0x0, F32, 0x0)
    ReflectionFresnelColor: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    BeamMode: (U32, 0x0, 0x0, 0x0)
    TexAddressModeMult: (U32, 0x0, 0x0, 0x0)
    UvScrollRateMult: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    ModulationFactor: (Vec4, 0x0, 0x0, 0x0)
    OffsetLifetimeScaling: (Vec3, 0x0, 0x0, 0x0)
    FlexParticleLifetime: (Embed, 0x0, 0x0, FlexValueFloat)
    FluidDynamicsDefinition: (Pointer, 0x0, 0x0, 0xe6cd2142)
    ProjectionFading: (F32, 0x0, 0x0, 0x0)
    BirthUvoffsetMult: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    StartFrame: (I32, 0x0, 0x0, 0x0)
    FlexRate: (Embed, 0x0, 0x0, FlexValueFloat)
    FlexScaleEmitOffset: (Embed, 0x0, 0x0, FlexTypeFloat)
    DoesLifetimeScale: (Bool, 0x0, 0x0, 0x0)
    ScaleEmitOffsetByBoundObjectRadius: (F32, 0x0, 0x0, 0x0)
    DirectionVelocityScale: (F32, 0x0, 0x0, 0x0)
    Pass: (I32, 0x0, 0x0, 0x0)
    BeamSegments: (I32, 0x0, 0x0, 0x0)
    EmitRotationAngles: (List, 0x0, Embed, VfxAnimatedFloatVariableData)
    TrailCutoff: (F32, 0x0, 0x0, 0x0)
    BirthDrag: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    Scale: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    BirthColor: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    NumFramesMult: (I32, 0x0, 0x0, 0x0)
    ReflectionMapTexture: (String, 0x0, 0x0, 0x0)
    TexDiv: (Vec2, 0x0, 0x0, 0x0)
    CensorModulateValue: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    Name: (String, 0x0, 0x0, 0x0)
    FlexBirthTranslation: (Embed, 0x0, 0x0, FlexValueVector3)
    Fresnel: (F32, 0x0, 0x0, 0x0)
    UvScrollMult: (Vec2, 0x0, 0x0, 0x0)
    SoundOnCreateName: (String, 0x0, 0x0, 0x0)
    ScaleBirthScaleByBoundObjectSize: (F32, 0x0, 0x0, 0x0)
    AnimationName: (String, 0x0, 0x0, 0x0)
    Period: (F32, 0x0, 0x0, 0x0)
    Period: (Option, 0x0, F32, 0x0)
    SoundPersistentName: (String, 0x0, 0x0, 0x0)
    FrameRate: (F32, 0x0, 0x0, 0x0)
    BirthRotation: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    FlexBirthVelocity: (Embed, 0x0, 0x0, FlexValueVector3)
    ChildParticleSetDefinition: (Embed, 0x0, 0x0, VfxChildParticleSetDefinitionData)
    BirthAcceleration: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    StartFrameMult: (I32, 0x0, 0x0, 0x0)
    FalloffTexture: (String, 0x0, 0x0, 0x0)
    SliceTechniqueRange: (F32, 0x0, 0x0, 0x0)
    MeshDisableBackfaceCull: (Bool, 0x0, 0x0, 0x0)
    FieldCollectionDefinition: (Embed, 0x0, 0x0, VfxFieldCollectionDefinitionData)
    Rate: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    TranslationOverride: (Vec3, 0x0, 0x0, 0x0)
    ParticleColorTexture: (String, 0x0, 0x0, 0x0)
    RotationOverride: (Vec3, 0x0, 0x0, 0x0)
    Drag: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    BirthUvoffset: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    Importance: (U32, 0x0, 0x0, 0x0)
    AlphaRef: (I32, 0x0, 0x0, 0x0)
    Distortion: (F32, 0x0, 0x0, 0x0)
    EmissionMeshScale: (F32, 0x0, 0x0, 0x0)
    SoftParticleParams: (Embed, 0x0, 0x0, VfxSoftParticleDefinitionData)
    ScaleEmitOffsetByBoundObjectSize: (F32, 0x0, 0x0, 0x0)
    KeywordsExcluded: (List, 0x0, String, 0x0)
    FrameRateMult: (F32, 0x0, 0x0, 0x0)
    RenderFlags: (U32, 0x0, 0x0, 0x0)
    BirthFrameRate: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    IsTexturePixelated: (Bool, 0x0, 0x0, 0x0)
    BindWeight: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    ColorLookUpOffsets: (Vec2, 0x0, 0x0, 0x0)
    TrailMode: (U32, 0x0, 0x0, 0x0)
    UvScrollRate: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    EmitRotationAxes: (List, 0x0, Vec3, 0x0)
    ParticleDefinition: (Embed, 0x0, 0x0, VfxComplexParticleDefinitionData)
    BeamParticleDefinition: (Embed, 0x0, 0x0, VfxBeamParticleDefinitionData)
    HasDistortion: (Bool, 0x0, 0x0, 0x0)
    FlexOffset: (Embed, 0x0, 0x0, FlexValueVector3)
    ScaleOverride: (Vec3, 0x0, 0x0, 0x0)
    EmitOffset: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    ScaleBirthScaleByBoundObjectHeight: (F32, 0x0, 0x0, 0x0)
    NormalMapTexture: (String, 0x0, 0x0, 0x0)
    WorldAcceleration: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    DirectionVelocityMinScale: (F32, 0x0, 0x0, 0x0)
    TrailSmoothingOn: (Bool, 0x0, 0x0, 0x0)
    ColorLookUpScales: (Vec2, 0x0, 0x0, 0x0)
    TrailMaxAddedPerFrame: (I32, 0x0, 0x0, 0x0)
    MeshTextureMultName: (String, 0x0, 0x0, 0x0)
    UvParallaxScale: (F32, 0x0, 0x0, 0x0)
    SimpleMeshName: (String, 0x0, 0x0, 0x0)
    MeshName: (String, 0x0, 0x0, 0x0)
    BirthVelocity: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    PostRotateOrientationAxis: (Vec3, 0x0, 0x0, 0x0)
    ExcludedAttachmentTypes: (List, 0x0, String, 0x0)
    BlendMode: (I32, 0x0, 0x0, 0x0)
    BirthTranslation: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    FlexBirthRotationalVelocity: (Embed, 0x0, 0x0, FlexValueVector3)
    FluidPartName: (String, 0x0, 0x0, 0x0)
    pass

class ISkinnedShadingModel(IX3dShadingModel):
    pass

class 0x85b7fa56():
    0x5a29d54c: (F32, 0x0, 0x0, 0x0)
    SkinScale: (F32, 0x0, 0x0, 0x0)
    pass

class StatPageEntry():
    StatPageViewController: (Hash, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    ButtonElements: (Embed, 0x0, 0x0, HudButtonElements)
    ButtonSelected: (Hash, 0x0, 0x0, 0x0)
    pass

class FxActionVfxBeam(FxActionVfxBase):
    Target: (Embed, 0x0, 0x0, FxTransform)
    Target: (Pointer, 0x0, 0x0, IFxLocation)
    pass

class TftItemMaterialController(SkinnedMeshDataMaterialController):
    pass

class OffScreenPoiPing():
    TextField: (U8, 0x0, 0x0, 0x0)
    0x343fb1dd: (Bool, 0x0, 0x0, 0x0)
    ScalingData: (Embed, 0x0, 0x0, PoiScalingData)
    ShowIfOnScreen: (Bool, 0x0, 0x0, 0x0)
    MaxDistanceFromCenterOfScreen: (U32, 0x0, 0x0, 0x0)
    ParticleEffect: (Hash, 0x0, 0x0, 0x0)
    PingType: (U8, 0x0, 0x0, 0x0)
    ShowDistance: (Bool, 0x0, 0x0, 0x0)
    ShowChampionProtrait: (Bool, 0x0, 0x0, 0x0)
    FadeComponent: (Pointer, 0x0, 0x0, PoiFadeData)
    AnchorTo: (U8, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    PingCombinationRange: (F32, 0x0, 0x0, 0x0)
    DurationSecs: (F32, 0x0, 0x0, 0x0)
    pass

class 0x85ec5cc(ModalDialogViewController):
    CheckBox: (Hash, 0x0, 0x0, 0x0)
    TextButton: (Hash, 0x0, 0x0, 0x0)
    pass

class BerserkTargetingParameters():
    mAffectsStatusFlags: (U32, 0x0, 0x0, 0x0)
    Radius: (F32, 0x0, 0x0, 0x0)
    mAffectsTypeFlags: (U32, 0x0, 0x0, 0x0)
    pass

class 0x85f9f4(IGameModeConfig):
    0x68d95a00: (Map, String, String, 0x0)
    pass

class ToolPassiveData():
    Effect: (List, 0x0, String, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    Level: (List, 0x0, I32, 0x0)
    pass

class TooltipInstance():
    mLocKeys: (Map, Hash, String, 0x0)
    mLocKeys: (Map, String, String, 0x0)
    mFormat: (Link, 0x0, 0x0, TooltipFormat)
    mLists: (Map, Hash, Embed, TooltipInstanceList)
    mLists: (Map, String, Embed, TooltipInstanceList)
    mObjectName: (String, 0x0, 0x0, 0x0)
    EnableExtendedTooltip: (Bool, 0x0, 0x0, 0x0)
    pass

class VoiceChatViewPlayerSlotData():
    Portrait: (Hash, 0x0, 0x0, 0x0)
    VolumeText: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    VolumeSliderBar: (Hash, 0x0, 0x0, 0x0)
    Halo: (Hash, 0x0, 0x0, 0x0)
    NameText: (Hash, 0x0, 0x0, 0x0)
    MuteButton: (Hash, 0x0, 0x0, 0x0)
    pass

class SummonerBadge():
    AnnouncementIcon: (String, 0x0, 0x0, 0x0)
    BadgeId: (U32, 0x0, 0x0, 0x0)
    mCooldown: (F32, 0x0, 0x0, 0x0)
    SelectionIcon: (String, 0x0, 0x0, 0x0)
    RenderScale: (F32, 0x0, 0x0, 0x0)
    BadgeTroyFile: (String, 0x0, 0x0, 0x0)
    mFacingOption: (U8, 0x0, 0x0, 0x0)
    mReadyForPlaytest: (Bool, 0x0, 0x0, 0x0)
    VisibleSelectionName: (String, 0x0, 0x0, 0x0)
    VerticalOffset: (F32, 0x0, 0x0, 0x0)
    pass

class AudioStatusEvents():
    RtpcName: (String, 0x0, 0x0, 0x0)
    StopEvent: (String, 0x0, 0x0, 0x0)
    StartEvent: (String, 0x0, 0x0, 0x0)
    pass

class NullMovementSpec(MissileMovementSpec):
    mWaitForChildren: (Bool, 0x0, 0x0, 0x0)
    pass

class TempTable2(ScriptTable):
    pass

class LoadingScreenEmblemData():
    EmblemElements: (Map, U32, Hash, 0x0)
    pass

class TftBannerCurrencyReward(TftBannerReward):
    CurrencyId: (String, 0x0, 0x0, 0x0)
    pass

class MultiPurchaseDialog(PurchaseDialogBase):
    MultiTitleText: (Hash, 0x0, 0x0, 0x0)
    BodyScrollSceneViewPane: (Hash, 0x0, 0x0, 0x0)
    MultiBackgroundRegion: (Hash, 0x0, 0x0, 0x0)
    MultiPurchaseManagedLayout: (Hash, 0x0, 0x0, 0x0)
    MoreInfoButton: (Hash, 0x0, 0x0, 0x0)
    SubPurchaseElements: (Embed, 0x0, 0x0, PurchaseDialogSubPurchaseElements)
    MultiBodyText: (Hash, 0x0, 0x0, 0x0)
    HeaderElements: (Embed, 0x0, 0x0, PurchaseDialogSubPurchaseHeaderElements)
    MultiSubPurchaseSectionLabel: (Hash, 0x0, 0x0, 0x0)
    MultiPurchaseItemIcon: (Hash, 0x0, 0x0, 0x0)
    0xa567ed12: (Embed, 0x0, 0x0, ViewPaneDefinition)
    MultiScene: (Hash, 0x0, 0x0, 0x0)
    MultiCloseButtonRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x86baa4d():
    ScalingConfig: (List, 0x0, Embed, 0x1d2ea7ed)
    pass

class IsAllyParametricUpdater(IBooleanParametricUpdater):
    pass

class CandidateListViewController(ViewController):
    Highlight: (List, 0xa, Hash, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    0x55008693: (Hash, 0x0, 0x0, 0x0)
    Index: (List, 0xa, Hash, 0x0)
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    AuthoredWidth: (F32, 0x0, 0x0, 0x0)
    Text: (List, 0xa, Hash, 0x0)
    0xdee6a21c: (Hash, 0x0, 0x0, 0x0)
    SourceResolutionWidth: (F32, 0x0, 0x0, 0x0)
    pass

class RsTable():
    pass

class TeamFightUiTunables():
    mSceneTransition: (Embed, 0x0, 0x0, HudMenuTransitionData)
    0xb748fcc5: (Bool, 0x0, 0x0, 0x0)
    pass

class GlobalAudioDataProperties():
    MusicPauseFadeMs: (U32, 0x0, 0x0, 0x0)
    LocalPlayerStatusEvents: (Map, U8, Embed, AudioStatusEvents)
    CooldownVoiceOver: (F32, 0x0, 0x0, 0x0)
    Systems: (Map, Hash, Link, SystemAudioDataProperties)
    Systems: (Map, Hash, Link, AudioSystemDataProperties)
    pass

class ClearAlreadyHitTracking(MissileTriggeredActionSpec):
    pass

class SetKeyValueInCustomTableBlock(IScriptBlock):
    Value: (Pointer, 0x0, 0x0, IScriptValueGet)
    Key: (Pointer, 0x0, 0x0, IScriptValueGet)
    DestTable: (Embed, 0x0, 0x0, CustomTableGet)
    CustomTable: (Embed, 0x0, 0x0, CustomTableGet)
    pass

class SpellRankTextUiData():
    RankText: (List, 0x4, Hash, 0x0)
    pass

class 0x86f801a2(ILolSpellScriptEvent):
    pass

class TftDamageSkin(BaseLoadoutData):
    mName: (String, 0x0, 0x0, 0x0)
    VisualEffectDescriptors: (List, 0x0, Embed, TftDamageSkinDescriptor)
    Disabled: (Bool, 0x0, 0x0, 0x0)
    AudioBankPaths: (List, 0x0, String, 0x0)
    FxDataContainer: (Pointer, 0x0, 0x0, TftDamageFxContainer)
    StandaloneLoadoutsIcon: (String, 0x0, 0x0, 0x0)
    Rarity: (U32, 0x0, 0x0, 0x0)
    DamageSkinMinionCutscene: (Pointer, 0x0, 0x0, TftCutscene)
    TrovesHighlightVfx: (Hash, 0x0, 0x0, 0x0)
    SkinId: (U32, 0x0, 0x0, 0x0)
    CeremonyDurationInSeconds: (F32, 0x0, 0x0, 0x0)
    0x8e2a4357: (Hash, 0x0, 0x0, 0x0)
    Level: (U32, 0x0, 0x0, 0x0)
    VfxResourceResolver: (Hash, 0x0, 0x0, 0x0)
    VfxResourceResolver: (Link, 0x0, 0x0, ResourceResolver)
    DamageBuffName: (String, 0x0, 0x0, 0x0)
    Ceremony: (Pointer, 0x0, 0x0, TftDamageSkinCeremony)
    DamageSkinCutscene: (Pointer, 0x0, 0x0, TftCutscene)
    0xe3bee29c: (Pointer, 0x0, 0x0, TftCutscene)
    StandaloneLoadoutsLargeIcon: (String, 0x0, 0x0, 0x0)
    RotationalShopItemData: (Embed, 0x0, 0x0, TftRotationalShopItemData)
    pass

class IsAnimationPlayingDynamicMaterialBoolDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    mAnimationNames: (List, 0x0, Hash, 0x0)
    pass

class 0x872c245e():
    pass

class CounterDefinition():
    Id: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    StartValue: (I32, 0x0, 0x0, 0x0)
    Direction: (U32, 0x0, 0x0, 0x0)
    pass

class KillCalloutsViewController(ViewController):
    MessageData: (Embed, 0x0, 0x0, HudKillCalloutTemplateData)
    MessageTemplate: (Embed, 0x0, 0x0, HudKillCalloutTemplateData)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    UseMinimapScale: (Bool, 0x0, 0x0, 0x0)
    MessageDisplayData: (Embed, 0x0, 0x0, HudMessageDisplayData)
    ObjectName: (String, 0x0, 0x0, 0x0)
    ItemSceneTemplate: (Hash, 0x0, 0x0, 0x0)
    pass

class TableValue():
    mVar: (String, 0x0, 0x0, 0x0)
    mVarTable: (U32, 0x0, 0x0, 0x0)
    Var: (String, 0x0, 0x0, 0x0)
    VarTable: (U32, 0x0, 0x0, 0x0)
    pass

class 0x87a6a884():
    pass

class UiDraggableBasic():
    UseStickyDrag: (Bool, 0x0, 0x0, 0x0)
    pass

class TftCurveTheDifferenceHeightSolver(TftHeightSolverType):
    InitialTargetHeightOffset: (F32, 0x0, 0x0, 0x0)
    pass

class 0x87ef793c():
    MinStage: (U32, 0x0, 0x0, 0x0)
    MinPlayerLevel: (I32, 0x0, 0x0, 0x0)
    0x2699a1ad: (Map, String, Pointer, GameModeConstant)
    MinRound: (U32, 0x0, 0x0, 0x0)
    pass

class TargeterDefinitionCone(TargeterDefinition):
    ConeFollowsEnd: (Bool, 0x0, 0x0, 0x0)
    RangeGrowthMax: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    EndLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    RangeGrowthDuration: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    FallbackDirection: (U32, 0x0, 0x0, 0x0)
    RangeGrowthStartTime: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    StartLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    TextureConeOverrideName: (String, 0x0, 0x0, 0x0)
    HasMaxGrowRange: (Bool, 0x0, 0x0, 0x0)
    ConeRange: (F32, 0x0, 0x0, 0x0)
    ConeRange: (Option, 0x0, F32, 0x0)
    TextureConeMaxGrowName: (String, 0x0, 0x0, 0x0)
    ConeAngleDegrees: (F32, 0x0, 0x0, 0x0)
    ConeAngleDegrees: (Option, 0x0, F32, 0x0)
    pass

class 0x880c52da(0x76bc0857):
    VisibilityController: (Link, 0x0, 0x0, IMapVisibilityController)
    pass

class TftArmoryButtonStyleData():
    UseBorderedIcon: (Bool, 0x0, 0x0, 0x0)
    ItemButton: (Hash, 0x0, 0x0, 0x0)
    Description: (Hash, 0x0, 0x0, 0x0)
    pass

class RegaliaData(BaseLoadoutData):
    Texture: (String, 0x0, 0x0, 0x0)
    pass

class 0x8873e4c8(0xb72a7d67):
    pass

class TftCutsceneArenaIntroAllPlayersInitializer(TftCutsceneArenaIntroInitializer):
    BlackboardExtraPlayerName: (String, 0x0, 0x0, 0x0)
    NumExtraPlayers: (U32, 0x0, 0x0, 0x0)
    pass

class IfBlock(IBlock):
    mVar1: (String, 0x0, 0x0, 0x0)
    mVar2: (String, 0x0, 0x0, 0x0)
    mCompareOp: (U32, 0x0, 0x0, 0x0)
    mVar2Table: (String, 0x0, 0x0, 0x0)
    mVar1Table: (String, 0x0, 0x0, 0x0)
    mVar1float: (F32, 0x0, 0x0, 0x0)
    mFalseSequence: (Pointer, 0x0, 0x0, Sequence)
    mTrueSequence: (Pointer, 0x0, 0x0, Sequence)
    mVar2float: (F32, 0x0, 0x0, 0x0)
    pass

class PlaybookViewController(ViewController):
    SelectionScene: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    SoundOnDeActivate: (String, 0x0, 0x0, 0x0)
    EquipButton: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    PlaybookHelpViewController: (Link, 0x0, 0x0, ModalDialogViewController)
    InfoPanel: (Embed, 0x0, 0x0, PlaybookInfoPanel)
    SoundOnActivate: (String, 0x0, 0x0, 0x0)
    CloseButton: (Hash, 0x0, 0x0, 0x0)
    DetailsButton: (Hash, 0x0, 0x0, 0x0)
    GridItemButton: (Hash, 0x0, 0x0, 0x0)
    HelpButton: (Hash, 0x0, 0x0, 0x0)
    BackButton: (Hash, 0x0, 0x0, 0x0)
    ItemListPanelData: (Embed, 0x0, 0x0, PlaybookItemListPanelData)
    AugmentItemData: (Embed, 0x0, 0x0, PlaybookAugmentItemData)
    GridButtonData: (Embed, 0x0, 0x0, PlaybookGridButtonData)
    AugmentPanelData: (Embed, 0x0, 0x0, PlaybookAugmentPanelData)
    pass

class InputEventBase():
    Name: (Hash, 0x0, 0x0, 0x0)
    Replicated: (Bool, 0x0, 0x0, 0x0)
    pass

class GameModeConstantVector3f(GameModeConstant):
    mValue: (Vec3, 0x0, 0x0, 0x0)
    pass

class 0x88b225d6():
    Value: (F32, 0x0, 0x0, 0x0)
    KeyFrame: (F32, 0x0, 0x0, 0x0)
    pass

class LoadoutsButtonData():
    Region: (Hash, 0x0, 0x0, 0x0)
    0x4e2c59d6: (Hash, 0x0, 0x0, 0x0)
    IllustrationIcon: (Hash, 0x0, 0x0, 0x0)
    LoadoutType: (U32, 0x0, 0x0, 0x0)
    Other: (Hash, 0x0, 0x0, 0x0)
    DisplayNameTraKey: (String, 0x0, 0x0, 0x0)
    ButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxGroupDefinitionData():
    VisibilityRadius: (F32, 0x0, 0x0, 0x0)
    pass

class GameModeDefaultStats():
    DefaultCharacterStats: (Embed, 0x0, 0x0, StatFormulaDataList)
    pass

class GdsMapObjectAnimationInfo(GdsMapObjectExtraInfo):
    DestroyOnCompletion: (Bool, 0x0, 0x0, 0x0)
    Duration: (F32, 0x0, 0x0, 0x0)
    Looping: (Bool, 0x0, 0x0, 0x0)
    DefaultAnimation: (String, 0x0, 0x0, 0x0)
    pass

class CopyCustomTableBlock(IScriptBlock):
    OutTable: (Embed, 0x0, 0x0, CustomTableSet)
    Table: (Embed, 0x0, 0x0, CustomTableGet)
    pass

class MapRoundData(MapComponent):
    0x3e2cdad7: (List2, 0x0, Link, LolModesRoundsListData)
    Rounds: (List2, 0x0, Link, LolModesRoundData)
    pass

class 0x89553bc9(ISequenceActionInstance):
    pass

class 0x896a8301():
    ConfigOverrides: (List2, 0x0, Link, 0x172f5c92)
    pass

class 0x8989c373(IScriptBlock, IBehaviorScriptBlock):
    pass

class PerkReplacementList():
    mReplacements: (List, 0x0, Pointer, PerkReplacement)
    pass

class NeutralTimerStateManager():
    NeutralTimerStates: (Map, U16, Embed, NeutralTimerState)
    pass

class UiElementGroupManagedLayoutData(UiElementGroupData, ElementGroupData):
    Region: (Link, 0x0, 0x0, RegionElementData)
    Region: (Link, 0x0, 0x0, UiElementRegionData)
    IgnoreDisabledElements: (Bool, 0x0, 0x0, 0x0)
    LayoutStyle: (Pointer, 0x0, 0x0, LayoutStyleBase)
    pass

class LossOfControlIcons():
    mAdditionalIconOffset: (Vec2, 0x0, 0x0, 0x0)
    mIconData: (Link, 0x0, 0x0, LossOfControlIconData)
    mIconOffset: (Vec2, 0x0, 0x0, 0x0)
    mIconDrawSize: (Vec2, 0x0, 0x0, 0x0)
    pass

class GameModeMapData():
    0x1fb498ce: (Link, 0x0, 0x0, GameModeItemList)
    AnnouncementsMapping: (Link, 0x0, 0x0, AnnouncementMap)
    mPerkReplacements: (Embed, 0x0, 0x0, PerkReplacementList)
    mLevelScripts: (List, 0x0, String, 0x0)
    mGameModeConstants: (Link, 0x0, 0x0, GameModeConstants)
    mMinimapBackgroundConfig: (Link, 0x0, 0x0, MinimapBackgroundConfig)
    CharacterQuestList: (Link, 0x0, 0x0, CharacterQuestListData)
    mCombatTextOverride: (Link, 0x0, 0x0, CombatTextOverride)
    ItemLists: (List2, 0x0, Link, GameModeItemList)
    mMapLocators: (Link, 0x0, 0x0, MapLocatorArray)
    mStatsUiData: (Link, 0x0, 0x0, GlobalStatsUiData)
    ItemShopEnabled: (Bool, 0x0, 0x0, 0x0)
    Configs: (List, 0x0, Link, IGameModeConfig)
    mExperienceModData: (Link, 0x0, 0x0, ExperienceModData)
    mLoadScreenTipConfiguration: (Link, 0x0, 0x0, LoadScreenTipConfiguration)
    mAutoItemPurchasingConfig: (Link, 0x0, 0x0, GameModeAutoItemPurchasingConfig)
    mFloatingTextOverride: (Link, 0x0, 0x0, FloatingTextOverride)
    mLoadingScreenWidgets: (List, 0x0, Link, IHudLoadingScreenWidget)
    mRenderStyle: (Link, 0x0, 0x0, RenderStyleData)
    mChampionIndicatorEnabled: (Bool, 0x0, 0x0, 0x0)
    GameModeEventManager: (Link, 0x0, 0x0, GameModeEventManager)
    ConfigsClient: (List2, 0x0, Link, IGameModeConfigClient)
    MutatorControlledLoadingScreenBackgrounds: (List, 0x0, String, 0x0)
    mMinionsUseAttackAffectFlagsForTargeting: (Bool, 0x0, 0x0, 0x0)
    SpellPickChoiceSpellLists: (List2, 0x0, Link, GameModeSpellList)
    mNeutralTimersDisplay: (Link, 0x0, 0x0, NeutralTimers)
    AdditionalPropertyDataPaths: (List, 0x0, String, 0x0)
    0x95fa6843: (Link, 0x0, 0x0, LolModesRoundsListData)
    mItemShopData: (Link, 0x0, 0x0, ItemShopGameModeData)
    mLoadingScreenBackground: (String, 0x0, 0x0, 0x0)
    mGameModeConstantsGroups: (List, 0x0, Link, GameModeConstantsGroup)
    mModeName: (Hash, 0x0, 0x0, 0x0)
    JungleRecommendationMapInformation: (Link, 0x0, 0x0, JungleRecommendationMapInformation)
    mDeathTimes: (Link, 0x0, 0x0, DeathTimes)
    mScriptDataObjectLists: (List, 0x0, Link, ScriptDataObjectList)
    DefaultJunglePathRecommendation: (Link, 0x0, 0x0, JunglePathRecommendation)
    mMissionBuffData: (Link, 0x0, 0x0, MissionBuffData)
    LuaObjectOverrides: (Link, 0x0, 0x0, LuaObjectOverrides)
    StartupCheats: (List2, 0x0, Hash, 0x0)
    AdditionalPropertyDataPath: (String, 0x0, 0x0, 0x0)
    LevelControllers: (List2, 0x0, Link, ILevelController)
    LevelControllers: (Pointer, 0x0, 0x0, LevelControllerManager)
    mHudScoreData: (Hash, 0x0, 0x0, 0x0)
    mGameplayConfig: (Link, 0x0, 0x0, GameplayConfig)
    mPreloadList: (Link, 0x0, 0x0, CharacterPreloadList)
    mBehaviorTreeConfig: (Link, 0x0, 0x0, BehaviorTreeConfig)
    mRelativeColorization: (Bool, 0x0, 0x0, 0x0)
    DefaultRespawnPoints: (Link, 0x0, 0x0, RespawnPointDataList)
    mCursorConfig: (Hash, 0x0, 0x0, 0x0)
    mChampionLists: (List, 0x0, Link, GameModeChampionList)
    mChampionLists: (List2, 0x0, Link, GameModeChampionList)
    mSurrenderSettings: (Link, 0x0, 0x0, SurrenderData)
    mPerkSystemType: (U32, 0x0, 0x0, 0x0)
    mCursorConfigUpdate: (Hash, 0x0, 0x0, 0x0)
    mMinionAiScriptOverride: (String, 0x0, 0x0, 0x0)
    mGameMode: (U32, 0x0, 0x0, 0x0)
    mExperienceCurveData: (Link, 0x0, 0x0, ExperienceCurveData)
    pass

class SkinnedUnlitShadingModel(ISkinnedShadingModel):
    pass

class UiElementGroupData(ElementDataI, UiElementIData):
    Elements: (List, 0x0, Link, ElementDataI)
    Elements: (List, 0x0, Link, UiElementIData)
    pass

class LobbyViewController(ViewController):
    DefaultQueueIdTitleTraKey: (String, 0x0, 0x0, 0x0)
    InQueueMusicState: (String, 0x0, 0x0, 0x0)
    LobbyCloseButton: (Hash, 0x0, 0x0, 0x0)
    SelfPortrait: (Embed, 0x0, 0x0, LobbySelfPortrait)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    LoadoutsButton: (Hash, 0x0, 0x0, 0x0)
    LeaderControls: (Embed, 0x0, 0x0, LobbyLeaderControls)
    ThemeMusicState: (String, 0x0, 0x0, 0x0)
    LobbyScene: (Hash, 0x0, 0x0, 0x0)
    LobbyLayouts: (Map, U8, Pointer, LobbyLayout)
    Labs: (Map, U32, Embed, LobbyLabFields)
    ReadyCheck: (Embed, 0x0, 0x0, LobbyReadyCheck)
    PopupViewController: (Link, 0x0, 0x0, ModalDialogViewController)
    RatedOnlyTraKey: (String, 0x0, 0x0, 0x0)
    ReadyCheckDeclineButton: (Hash, 0x0, 0x0, 0x0)
    0x97969f33: (Pointer, 0x0, 0x0, LobbyLayout)
    FriendEditButton: (Hash, 0x0, 0x0, 0x0)
    0xa196aef1: (Pointer, 0x0, 0x0, LobbyLayout)
    RankOnlyTraKey: (String, 0x0, 0x0, 0x0)
    FriendPortraitData: (Embed, 0x0, 0x0, LobbyFriendPortraitData)
    PopupHitRegion: (Hash, 0x0, 0x0, 0x0)
    QueueIdTitleTraKeys: (Map, I64, String, 0x0)
    RankAndRatedTraKey: (String, 0x0, 0x0, 0x0)
    0xc4f9e37f: (Link, 0x0, 0x0, ModalDialogViewController)
    DoubleUpFullLobbyEnabled: (Bool, 0x0, 0x0, 0x0)
    ReadyCheckAcceptButton: (Hash, 0x0, 0x0, 0x0)
    ThemeMusicStateGroup: (String, 0x0, 0x0, 0x0)
    LobbyMusicState: (String, 0x0, 0x0, 0x0)
    0xd5989aae: (Hash, 0x0, 0x0, 0x0)
    GameTypeFields: (Map, U32, Embed, LobbyLabFields)
    BottomButtons: (Embed, 0x0, 0x0, LobbyBottomButtons)
    FriendInviteButton: (Hash, 0x0, 0x0, 0x0)
    pass

class BehaviorTreeConfig():
    mMissionStringVars: (Map, Hash, String, 0x0)
    mMissionIntVars: (Map, Hash, I32, 0x0)
    mMissionFloatVars: (Map, Hash, F32, 0x0)
    pass

class MapLightingVolume(MapPlaceable):
    PbrSunAdditionalScale: (F32, 0x0, 0x0, 0x0)
    0x1dfffa84: (Link, 0x0, 0x0, IMapVisibilityController)
    FogColor: (Vec4, 0x0, 0x0, 0x0)
    FogEmissiveRemap: (F32, 0x0, 0x0, 0x0)
    FogLowQualityModeEmissiveRemap: (F32, 0x0, 0x0, 0x0)
    SunIntensityScale: (F32, 0x0, 0x0, 0x0)
    FogAlternateColor: (Vec4, 0x0, 0x0, 0x0)
    GroundColor: (Vec4, 0x0, 0x0, 0x0)
    SunColor: (Vec4, 0x0, 0x0, 0x0)
    FogStartAndEnd: (Vec2, 0x0, 0x0, 0x0)
    FogEnabled: (Bool, 0x0, 0x0, 0x0)
    LightMapColorScale: (F32, 0x0, 0x0, 0x0)
    OverrideSunSpecDirection: (Option, 0x0, Vec3, 0x0)
    SkyLightColor: (Vec4, 0x0, 0x0, 0x0)
    SkyLightScale: (F32, 0x0, 0x0, 0x0)
    ScaleSunShadowIntensity: (F32, 0x0, 0x0, 0x0)
    0xc6d048fc: (F32, 0x0, 0x0, 0x0)
    ShadowBias: (F32, 0x0, 0x0, 0x0)
    SunRadiusForShadows: (F32, 0x0, 0x0, 0x0)
    SunDirection: (Vec3, 0x0, 0x0, 0x0)
    HorizonColor: (Vec4, 0x0, 0x0, 0x0)
    pass

class CharacterQuestReward(ICharacterQuestReward):
    RewardRecipient: (Hash, 0x0, 0x0, 0x0)
    Spell: (Hash, 0x0, 0x0, 0x0)
    pass

class OffScreenPoiViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    ChampionPortraitScene: (Hash, 0x0, 0x0, 0x0)
    OffScreenPoiSettings: (Embed, 0x0, 0x0, OffScreenPoiConfigData)
    ObjectName: (String, 0x0, 0x0, 0x0)
    OffScreenPoiData: (Embed, 0x0, 0x0, OffScreenPoiItemData)
    pass

class GameModeChampionList():
    mChampions: (List, 0x0, Hash, 0x0)
    mChampions: (List2, 0x0, Hash, 0x0)
    pass

class ResourceMeterIconData(ResourceMeterBaseData):
    AdditionalBarTypes: (Map, Hash, Hash, 0x0)
    DefaultBar: (Hash, 0x0, 0x0, 0x0)
    pass

class LoopBlock(IScriptBlock, ILoopScriptBlock):
    Sequence: (Embed, 0x0, 0x0, ScriptSequence)
    InclusiveIteration: (Bool, 0x0, 0x0, 0x0)
    Start: (Pointer, 0x0, 0x0, IIntGet)
    End: (Pointer, 0x0, 0x0, IIntGet)
    Dest: (Embed, 0x0, 0x0, IntTableSet)
    Step: (Pointer, 0x0, 0x0, IIntGet)
    pass

class OptionItemButton(IOptionItem):
    Template: (Hash, 0x0, 0x0, 0x0)
    DescriptionTraKey: (String, 0x0, 0x0, 0x0)
    Action: (U16, 0x0, 0x0, 0x0)
    LabelTraKey: (String, 0x0, 0x0, 0x0)
    pass

class ViewPaneDefinition():
    ObjectPath: (Hash, 0x0, 0x0, 0x0)
    SliderKey: (String, 0x0, 0x0, 0x0)
    DragRegionElement: (Hash, 0x0, 0x0, 0x0)
    ScissorRegionElement: (Hash, 0x0, 0x0, 0x0)
    SliderBarDefinition: (Hash, 0x0, 0x0, 0x0)
    Slider: (Hash, 0x0, 0x0, 0x0)
    ScrollingScene: (Hash, 0x0, 0x0, 0x0)
    ScrollDirection: (U8, 0x0, 0x0, 0x0)
    ScrollRegionElement: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x8aef29d3(IBehaviorScriptBlock):
    Sequence: (Embed, 0x0, 0x0, ScriptBtOverrideResolveState)
    ResolveState: (Pointer, 0x0, 0x0, IBoolGet)
    pass

class HasBuffDynamicMaterialBoolDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    Spell: (Hash, 0x0, 0x0, 0x0)
    mScriptName: (String, 0x0, 0x0, 0x0)
    mDeactivateEarlySeconds: (F32, 0x0, 0x0, 0x0)
    pass

class 0x8b04b4cb(IGameModeConfigClient):
    IsEnabled: (Bool, 0x0, 0x0, 0x0)
    pass

class RootScene():
    pass

class 0x8b33cf88():
    pass

class FxActionMoveTo(FxActionMoveBase):
    Destination: (Embed, 0x0, 0x0, FxTransform)
    Destination: (Pointer, 0x0, 0x0, IFxLocation)
    pass

class 0x8b38bb8d():
    Position: (Hash, 0x0, 0x0, 0x0)
    RecOverrideItem: (Hash, 0x0, 0x0, 0x0)
    pass

class Character(ICharacter):
    Name: (String, 0x0, 0x0, 0x0)
    pass

class TftPassRewardBase():
    ImageOverridePath: (String, 0x0, 0x0, 0x0)
    HasBorder: (Bool, 0x0, 0x0, 0x0)
    0x2484d6c3: (Bool, 0x0, 0x0, 0x0)
    NameTraKeyOverride: (String, 0x0, 0x0, 0x0)
    Quantity: (U32, 0x0, 0x0, 0x0)
    RewardAsset: (Link, 0x0, 0x0, TftPassAsset)
    IsKeystone: (Bool, 0x0, 0x0, 0x0)
    MilestoneId: (String, 0x0, 0x0, 0x0)
    NameTraKey: (String, 0x0, 0x0, 0x0)
    DescriptionTraKeyOverride: (String, 0x0, 0x0, 0x0)
    IsPremium: (Bool, 0x0, 0x0, 0x0)
    0x96f93ea0: (U32, 0x0, 0x0, 0x0)
    Override: (Bool, 0x0, 0x0, 0x0)
    ImageOverride: (Hash, 0x0, 0x0, 0x0)
    Quanitity: (U32, 0x0, 0x0, 0x0)
    IsBonus: (Bool, 0x0, 0x0, 0x0)
    pass

class EffectCreationData():
    0x2eb0e75a: (Bool, 0x0, 0x0, 0x0)
    mOrientTowardsTarget: (Bool, 0x0, 0x0, 0x0)
    mPlaySpeed: (F32, 0x0, 0x0, 0x0)
    mEffectName: (String, 0x0, 0x0, 0x0)
    mShowToOwnerOnly: (Bool, 0x0, 0x0, 0x0)
    0x6ba295f5: (F32, 0x0, 0x0, 0x0)
    mSendIfOnScreenOrDiscard: (Bool, 0x0, 0x0, 0x0)
    mEffectCreateFlags: (I32, 0x0, 0x0, 0x0)
    mScale: (F32, 0x0, 0x0, 0x0)
    mShowInGrass: (Bool, 0x0, 0x0, 0x0)
    mSpecificTeamOnly: (U32, 0x0, 0x0, 0x0)
    mAttachToCamera: (Bool, 0x0, 0x0, 0x0)
    mFaceTarget: (Bool, 0x0, 0x0, 0x0)
    mTargetBoneName: (String, 0x0, 0x0, 0x0)
    mEffectKeyForOtherTeam: (Hash, 0x0, 0x0, 0x0)
    0xa45eda7b: (Bool, 0x0, 0x0, 0x0)
    mFollowGroundTilt: (Bool, 0x0, 0x0, 0x0)
    mHidefromSpectator: (Bool, 0x0, 0x0, 0x0)
    mFowTeam: (U32, 0x0, 0x0, 0x0)
    mBoneName: (String, 0x0, 0x0, 0x0)
    mPlaySpeedModifier: (F32, 0x0, 0x0, 0x0)
    mEffectKey: (Hash, 0x0, 0x0, 0x0)
    mTargetPosIsOwner: (Bool, 0x0, 0x0, 0x0)
    mEffectNameForOtherTeam: (String, 0x0, 0x0, 0x0)
    pass

class SkinMeshDataProperties_MaterialOverride():
    RoughnessMetallicAoTexture: (String, 0x0, 0x0, 0x0)
    RenderingMode: (I32, 0x0, 0x0, 0x0)
    Texture: (String, 0x0, 0x0, 0x0)
    Priority: (I32, 0x0, 0x0, 0x0)
    Submesh: (String, 0x0, 0x0, 0x0)
    Material: (Link, 0x0, 0x0, MaterialDef)
    Material: (Link, 0x0, 0x0, IMaterialDef)
    GlossTexture: (String, 0x0, 0x0, 0x0)
    NormalMapTexture: (String, 0x0, 0x0, 0x0)
    pass

class FxLocationAttachment(IFxLocation):
    Attachment: (String, 0x0, 0x0, 0x0)
    Object: (Embed, 0x0, 0x0, FxTarget)
    Object: (Embed, 0x0, 0x0, FxObjectSelector)
    pass

class HudStatPanelStatStoneData():
    mSlideTransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    0x4ae65dfa: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mAnimationDelayTime: (F32, 0x0, 0x0, 0x0)
    0x77d83159: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mSlideTransitionOut: (Embed, 0x0, 0x0, HudMenuTransitionData)
    0xca84776a: (F32, 0x0, 0x0, 0x0)
    0xf675a6b7: (F32, 0x0, 0x0, 0x0)
    pass

class 0x8bb623e8():
    Offset: (Vec3, 0x0, 0x0, 0x0)
    0x1f11b7e5: (Bool, 0x0, 0x0, 0x0)
    0x1f7df8df: (Bool, 0x0, 0x0, 0x0)
    AutoOffset: (Bool, 0x0, 0x0, 0x0)
    0x2a71e3f2: (Bool, 0x0, 0x0, 0x0)
    0x2d76c615: (Bool, 0x0, 0x0, 0x0)
    0x2f493796: (Bool, 0x0, 0x0, 0x0)
    AdaptiveSkill: (Bool, 0x0, 0x0, 0x0)
    0x3c444000: (F32, 0x0, 0x0, 0x0)
    0x3e40d50c: (Bool, 0x0, 0x0, 0x0)
    0x420eed36: (Bool, 0x0, 0x0, 0x0)
    0x42abffde: (F32, 0x0, 0x0, 0x0)
    0x569afefb: (Bool, 0x0, 0x0, 0x0)
    0x57638089: (F32, 0x0, 0x0, 0x0)
    0x6a501efe: (Bool, 0x0, 0x0, 0x0)
    0x72b3e7ce: (Bool, 0x0, 0x0, 0x0)
    0x74ef37dc: (I32, 0x0, 0x0, 0x0)
    LockLeftOffset: (F32, 0x0, 0x0, 0x0)
    UpOffset: (F32, 0x0, 0x0, 0x0)
    0x7fab95cc: (F32, 0x0, 0x0, 0x0)
    ControlRatio: (F32, 0x0, 0x0, 0x0)
    0x81cbe214: (F32, 0x0, 0x0, 0x0)
    0x8b2f2060: (Bool, 0x0, 0x0, 0x0)
    OutConstantSpeed: (F32, 0x0, 0x0, 0x0)
    LockRightOffset: (F32, 0x0, 0x0, 0x0)
    0x8eb85226: (F32, 0x0, 0x0, 0x0)
    DownOffset: (F32, 0x0, 0x0, 0x0)
    0x9a7674c6: (F32, 0x0, 0x0, 0x0)
    HighlightedMovingBool: (F32, 0x0, 0x0, 0x0)
    IsLerp: (Bool, 0x0, 0x0, 0x0)
    MinOffset: (F32, 0x0, 0x0, 0x0)
    OutLerpA: (F32, 0x0, 0x0, 0x0)
    OutIsLerp: (Bool, 0x0, 0x0, 0x0)
    LockDownOffset: (F32, 0x0, 0x0, 0x0)
    0xbcf692f1: (F32, 0x0, 0x0, 0x0)
    IsConstant: (Bool, 0x0, 0x0, 0x0)
    ConstantSpeed: (F32, 0x0, 0x0, 0x0)
    0xc4122105: (Bool, 0x0, 0x0, 0x0)
    OffsetType: (U32, 0x0, 0x0, 0x0)
    LeftOffset: (F32, 0x0, 0x0, 0x0)
    IsReset: (Bool, 0x0, 0x0, 0x0)
    FollowType: (U32, 0x0, 0x0, 0x0)
    0xe29f9f32: (F32, 0x0, 0x0, 0x0)
    0xe5bed1d4: (F32, 0x0, 0x0, 0x0)
    LerpA: (F32, 0x0, 0x0, 0x0)
    RightOffset: (F32, 0x0, 0x0, 0x0)
    0xf1db58ae: (F32, 0x0, 0x0, 0x0)
    LockUpOffset: (F32, 0x0, 0x0, 0x0)
    0xfb6aa814: (F32, 0x0, 0x0, 0x0)
    OutIsConstant: (Bool, 0x0, 0x0, 0x0)
    pass

class EffectValueCalculationPart(IGameCalculationPart, ISpellCalculationPart):
    mEffectIndex: (I32, 0x0, 0x0, 0x0)
    pass

class UiMetricCreepScore(UiMetricTypeI, UiMetricTypeSimpleI):
    CsIcon: (Hash, 0x0, 0x0, 0x0)
    CsText: (Hash, 0x0, 0x0, 0x0)
    pass

class GenericMapPlaceable(MapPlaceable):
    pass

class MapActionCycleMapParticle(MapAction):
    MapParticleName: (List, 0x0, String, 0x0)
    Shuffle: (Bool, 0x0, 0x0, 0x0)
    pass

class FloatingTextTypeData():
    ComparisonByLevel: (List, 0x0, F32, 0x0)
    FontTypes: (List, 0x0, Link, FloatTextFormattingData)
    DisplayTypes: (List, 0x0, Link, FloatTextDisplayOverrides)
    pass

class StrawberryMap(BaseLoadoutData):
    MapContainers: (List2, 0x0, Embed, StrawberryMapContainer)
    MapContainer: (String, 0x0, 0x0, 0x0)
    pass

class UiElementEffectLineData(UiElementEffectData):
    mThickness: (F32, 0x0, 0x0, 0x0)
    mRightSlicePercentage: (F32, 0x0, 0x0, 0x0)
    TextureData: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mAtlas: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    pass

class IndicatorTypeGlobal(ILineIndicatorType):
    mIsFloating: (Bool, 0x0, 0x0, 0x0)
    pass

class FloatingInfoBarViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MobileLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    InfoBarStyleSourceMap: (Map, U8, Link, FloatingInfoBarData)
    ObjectName: (String, 0x0, 0x0, 0x0)
    UnitStatusPriorityList: (Link, 0x0, 0x0, UnitStatusPriorityList)
    pass

class BufferedInputData():
    InputChains: (Map, String, Embed, BufferedInputChain)
    0xd8befef3: (F32, 0x0, 0x0, 0x0)
    pass

class BountyIndicator():
    0x20d48558: (String, 0x0, 0x0, 0x0)
    mOffset: (Vec2, 0x0, 0x0, 0x0)
    LevelFourIcon: (String, 0x0, 0x0, 0x0)
    LevelOneIcon: (String, 0x0, 0x0, 0x0)
    0x554bec0e: (String, 0x0, 0x0, 0x0)
    mIconSize: (Vec2, 0x0, 0x0, 0x0)
    LevelFiveIcon: (String, 0x0, 0x0, 0x0)
    0xcffa5124: (String, 0x0, 0x0, 0x0)
    LevelTwoIcon: (String, 0x0, 0x0, 0x0)
    LevelThreeIcon: (String, 0x0, 0x0, 0x0)
    0xeaaaf26e: (String, 0x0, 0x0, 0x0)
    0xebb44d40: (String, 0x0, 0x0, 0x0)
    pass

class TftCharacterRoleCardHeader():
    Description: (Hash, 0x0, 0x0, 0x0)
    Title: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class SequencerClipData(ClipBaseData):
    mTrackIndex: (U32, 0x0, 0x0, 0x0)
    mClipNameList: (List, 0x0, Hash, 0x0)
    mClipIndexList: (List, 0x0, U32, 0x0)
    mEventDataMap: (Map, Hash, Pointer, BaseEventData)
    pass

class VoMarkerEvents():
    mMarkerEvents: (Map, Hash, Embed, VoMarkerEvent)
    pass

class 0x8d8b1535():
    0x3392c041: (String, 0x0, 0x0, 0x0)
    0x58766309: (String, 0x0, 0x0, 0x0)
    0x720e4297: (Hash, 0x0, 0x0, 0x0)
    0x96349f57: (String, 0x0, 0x0, 0x0)
    0xa807a4b2: (String, 0x0, 0x0, 0x0)
    0xd0666cc4: (String, 0x0, 0x0, 0x0)
    IconFrame: (Hash, 0x0, 0x0, 0x0)
    pass

class ChampionTransformSelectionViewController(ViewController):
    MeterVanishAnim: (Hash, 0x0, 0x0, 0x0)
    MeterInnerRing: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    MeterFill: (Hash, 0x0, 0x0, 0x0)
    TransformReadyAnim: (Hash, 0x0, 0x0, 0x0)
    TransformButtonAssassin: (Hash, 0x0, 0x0, 0x0)
    TimerTextAssassin: (Hash, 0x0, 0x0, 0x0)
    TransformReadyAttentionAnim: (Hash, 0x0, 0x0, 0x0)
    Loadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TransformCenterline: (Hash, 0x0, 0x0, 0x0)
    TransformButtonSlayer: (Hash, 0x0, 0x0, 0x0)
    TransformReadyOutAnim: (Hash, 0x0, 0x0, 0x0)
    EnergyGainAnim: (Hash, 0x0, 0x0, 0x0)
    TransformReadyIdleSlayerAnim: (Hash, 0x0, 0x0, 0x0)
    TimerTextSlayer: (Hash, 0x0, 0x0, 0x0)
    TransformReadyIdleAssassinAnim: (Hash, 0x0, 0x0, 0x0)
    MeterOuterRing: (Hash, 0x0, 0x0, 0x0)
    pass

class SkinnedStandardShadingModel(ISkinnedShadingModel):
    pass

class UiMetricLaneMinionI(UiMetricUnitTypeI, UiMetricUnitTypeSimpleI):
    Text: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class TftRegalia():
    Assets: (Map, String, String, 0x0)
    pass

class StateAnimClipData(ClipBaseData):
    Transitions: (List, 0x0, Embed, StateAnimTransitionData)
    Transitions: (List, 0x0, Embed, StateTransitionData)
    SpeedRatioDriver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    ChildClipName: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x8e30b80e(TftCutscenePositionProvider):
    BlackboardPosition: (String, 0x0, 0x0, 0x0)
    0x9e3d0a40: (String, 0x0, 0x0, 0x0)
    BlackboardOrientation: (String, 0x0, 0x0, 0x0)
    pass

class CompanionSpeciesData():
    mSpeciesId: (U32, 0x0, 0x0, 0x0)
    mSpeciesName: (String, 0x0, 0x0, 0x0)
    pass

class TftCutscene():
    Duration: (F32, 0x0, 0x0, 0x0)
    Disabled: (Bool, 0x0, 0x0, 0x0)
    Initializer: (Pointer, 0x0, 0x0, TftCutsceneInitializer)
    Entries: (List2, 0x0, Pointer, TftCutsceneEntry)
    pass

class 0x8e65fb6b(0x6ca3cfd):
    ValueDriver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    LocalizedTextFormat: (String, 0x0, 0x0, 0x0)
    TextFormat: (String, 0x0, 0x0, 0x0)
    pass

class 0x8e8282a9(MapComponent):
    MaxSize: (U32, 0x0, 0x0, 0x0)
    pass

class NotInputSourceBool(IInputSourceBool):
    Source: (Pointer, 0x0, 0x0, IInputSourceBool)
    pass

class Breakpoint():
    mBonusPerLevelAtAndAfter: (F32, 0x0, 0x0, 0x0)
    mLevel: (U32, 0x0, 0x0, 0x0)
    mAdditionalBonusAtThisLevel: (F32, 0x0, 0x0, 0x0)
    pass

class CharacterPassiveData():
    mComponentBuffs: (List, 0x0, Link, SpellObject)
    mDisplayFlags: (U8, 0x0, 0x0, 0x0)
    mAllowOnClones: (Bool, 0x0, 0x0, 0x0)
    mSlotFlags: (U8, 0x0, 0x0, 0x0)
    mSkinIds: (List, 0x0, U32, 0x0)
    SkinFilter: (Pointer, 0x0, 0x0, SkinFilterData)
    mParentPassiveBuff: (Link, 0x0, 0x0, SpellObject)
    mChildSpells: (List, 0x0, Link, SpellObject)
    0xd313216b: (Bool, 0x0, 0x0, 0x0)
    mPreloadSpells: (List, 0x0, Link, SpellObject)
    pass

class ViewControllerFilter_Mode(ViewControllerFilterI):
    Mode: (String, 0x0, 0x0, 0x0)
    pass

class TargetFrameMeterSkinData():
    MeterEnemySkin: (Embed, 0x0, 0x0, UiElementMeterSkin)
    MeterAllySkin: (Embed, 0x0, 0x0, UiElementMeterSkin)
    pass

class ConditionFloatClipData(ClipBaseData):
    Updater: (Pointer, 0x0, 0x0, IFloatParametricUpdater)
    mUpdaterType: (U32, 0x0, 0x0, 0x0)
    mConditionFloatPairDataList: (List, 0x0, Embed, ConditionFloatPairData)
    mPlayAnimChangeFromBeginning: (Bool, 0x0, 0x0, 0x0)
    mChangeAnimationMidPlay: (Bool, 0x0, 0x0, 0x0)
    mTrackIndex: (U32, 0x0, 0x0, 0x0)
    DontStompTransitionClip: (Bool, 0x0, 0x0, 0x0)
    SyncFrameOnChangeAnim: (Bool, 0x0, 0x0, 0x0)
    mChangeAnimationMidPlayback: (Bool, 0x0, 0x0, 0x0)
    mChildAnimDelaySwitchTime: (F32, 0x0, 0x0, 0x0)
    0xf88501b8: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x8ecb8976(TableValue):
    pass

class PfxProbabilityTableData():
    KeyTimes: (List, 0x0, F32, 0x0)
    KeyValues: (List, 0x0, F32, 0x0)
    pass

class BroadcastViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    EventLeagueComboBoxDefinition: (Hash, 0x0, 0x0, 0x0)
    SelectLeagueConfigComboBoxDefinition: (Hash, 0x0, 0x0, 0x0)
    SelectLeagueFlavorComboBoxDefinition: (Hash, 0x0, 0x0, 0x0)
    ObjectName: (String, 0x0, 0x0, 0x0)
    0xfc522619: (Hash, 0x0, 0x0, 0x0)
    pass

class PlayerPortraitUiData():
    VoiceChatHalo: (Hash, 0x0, 0x0, 0x0)
    LevelText: (Hash, 0x0, 0x0, 0x0)
    RespawnTimer: (Hash, 0x0, 0x0, 0x0)
    TooltipRegion: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class BarracksLink():
    Lane: (I8, 0x0, 0x0, 0x0)
    Team: (U32, 0x0, 0x0, 0x0)
    pass

class ISkinAugmentModifier():
    pass

class SceneAlphaTransitionData(SceneBaseTransitionData):
    pass

class PackFormationData():
    FormationPositions: (List, 0x0, Vec2, 0x0)
    pass

class JungleAction():
    pass

class DefaultSplashedPerkStyle():
    mPerk1: (Link, 0x0, 0x0, Perk)
    mPerk2: (Link, 0x0, 0x0, Perk)
    mStyle: (Link, 0x0, 0x0, PerkStyle)
    pass

class SkinAudioProperties():
    VoBankAssetPath: (List, 0x0, String, 0x0)
    SfxBank: (List, 0x0, String, 0x0)
    VoBank: (List, 0x0, String, 0x0)
    SfxAsyncBankPath: (List, 0x0, String, 0x0)
    SfxAsyncBank: (List, 0x0, String, 0x0)
    PlaysVo: (Bool, 0x0, 0x0, 0x0)
    VoBankPath: (List, 0x0, String, 0x0)
    UseExplicitLists: (Bool, 0x0, 0x0, 0x0)
    SfxBankPath: (List, 0x0, String, 0x0)
    TagEventList: (List, 0x0, String, 0x0)
    SfxBankAssetPath: (List, 0x0, String, 0x0)
    BankUnits: (List, 0x0, Embed, BankUnit)
    BankUnits: (List2, 0x0, Embed, BankUnit)
    SfxAsyncBankAssetPath: (List, 0x0, String, 0x0)
    pass

class AnimatedBuilding(AnimatedBuildingCommon):
    pass

class TftFinisherData():
    UiMobileHideShopButton: (Bool, 0x0, 0x0, 0x0)
    Duration: (F32, 0x0, 0x0, 0x0)
    UiHideHealthBars: (Bool, 0x0, 0x0, 0x0)
    UiHideMinimap: (Bool, 0x0, 0x0, 0x0)
    UiMobileHideItemPanel: (Bool, 0x0, 0x0, 0x0)
    UiHideFloatingText: (Bool, 0x0, 0x0, 0x0)
    UiMobileShouldClearOpenMenus: (Bool, 0x0, 0x0, 0x0)
    UiMobileHideHeaderButtons: (Bool, 0x0, 0x0, 0x0)
    UiHideScoreboard: (Bool, 0x0, 0x0, 0x0)
    UiClearTooltips: (Bool, 0x0, 0x0, 0x0)
    UiHideStage: (Bool, 0x0, 0x0, 0x0)
    UiHideTraitTracker: (Bool, 0x0, 0x0, 0x0)
    UiHideShop: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x8f92cfab(InstanceDataBase):
    ForegroundImage: (Embed, 0x0, 0x0, TextureOverride)
    UrlTra: (String, 0x0, 0x0, 0x0)
    pass

class WallFollowMovement(MissileMovementSpec):
    mProjectTargetToCastRange: (Bool, 0x0, 0x0, 0x0)
    UsePointSmoothing: (Bool, 0x0, 0x0, 0x0)
    mSpeed: (F32, 0x0, 0x0, 0x0)
    mCounterClockwise: (Bool, 0x0, 0x0, 0x0)
    mUseGroundHeightAtTarget: (Bool, 0x0, 0x0, 0x0)
    mInferDirectionFromFacingIfNeeded: (Bool, 0x0, 0x0, 0x0)
    mWallOffset: (F32, 0x0, 0x0, 0x0)
    AddBonusAttackRangeToCastRange: (Bool, 0x0, 0x0, 0x0)
    mWallLength: (F32, 0x0, 0x0, 0x0)
    mStopHalfwayAround: (Bool, 0x0, 0x0, 0x0)
    0xbeb5db5b: (Bool, 0x0, 0x0, 0x0)
    mWallSearchRadius: (F32, 0x0, 0x0, 0x0)
    pass

class 0x8fb9d292():
    ConfigTypes: (List2, 0x0, Embed, 0x896a8301)
    pass

class HasBuffSpawnConditionData(VfxSpawnConditionData):
    mBuffName: (String, 0x0, 0x0, 0x0)
    mFromAnyone: (Bool, 0x0, 0x0, 0x0)
    mFromOwner: (Bool, 0x0, 0x0, 0x0)
    mFromAttacker: (Bool, 0x0, 0x0, 0x0)
    mBuffComparisons: (Embed, 0x0, 0x0, HasBuffComparisonData)
    pass

class RegaliaRankedCrestMap():
    RankingToCrestEntryMap: (Map, String, Embed, RegaliaRankedCrestEntry)
    pass

class LevelScriptOnEnd(ILevelScriptEvent):
    pass

class EndOfGameCeremonyBehavior(ILevelBehavior):
    PanToHqTimeSecs: (F32, 0x0, 0x0, 0x0)
    FadeMinionsTimeSecs: (F32, 0x0, 0x0, 0x0)
    FadeMinionsDelaySecs: (F32, 0x0, 0x0, 0x0)
    pass

class FloorFloatMaterialDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    mDriver: (Pointer, 0x0, 0x0, IDynamicMaterialFloatDriver)
    mDriver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class FxActionMoveBaseInstance(IFxActionInstance):
    pass

class TftScoreboardPlayerTemplate():
    MatchmakingIcon: (Hash, 0x0, 0x0, 0x0)
    WinStreakOutro: (Hash, 0x0, 0x0, 0x0)
    ViewingIcon: (Hash, 0x0, 0x0, 0x0)
    ClickRegion: (Hash, 0x0, 0x0, 0x0)
    Bounds: (Hash, 0x0, 0x0, 0x0)
    WinStreakIntro: (Hash, 0x0, 0x0, 0x0)
    CustomBadgeGroup: (Hash, 0x0, 0x0, 0x0)
    CustomButton: (Hash, 0x0, 0x0, 0x0)
    FutureSightVfx: (Hash, 0x0, 0x0, 0x0)
    WinStreakLoopLevel1: (Hash, 0x0, 0x0, 0x0)
    WinStreakLoopLevel2: (Hash, 0x0, 0x0, 0x0)
    HealthText: (Hash, 0x0, 0x0, 0x0)
    CombatStateBackground: (Hash, 0x0, 0x0, 0x0)
    CombatStateLossFx: (Hash, 0x0, 0x0, 0x0)
    PlayerScene: (Hash, 0x0, 0x0, 0x0)
    NameBackdrop: (Hash, 0x0, 0x0, 0x0)
    FillMeter: (Hash, 0x0, 0x0, 0x0)
    CustomButtonIcon: (Hash, 0x0, 0x0, 0x0)
    CustomBadgeIcon: (Hash, 0x0, 0x0, 0x0)
    SharedDraftGroupText: (Hash, 0x0, 0x0, 0x0)
    Delays: (Embed, 0x0, 0x0, TftScoreboardDelays)
    CombatStateWinFx: (Hash, 0x0, 0x0, 0x0)
    CombatStateDotsFx: (Hash, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    NameText: (Hash, 0x0, 0x0, 0x0)
    MuteButton: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    SharedDraftGroupBackground: (Hash, 0x0, 0x0, 0x0)
    MatchmakingVfx: (Hash, 0x0, 0x0, 0x0)
    pass

class 0x9046d789():
    pass

class StaticMaterialShaderSamplerDef():
    AddressV: (U32, 0x0, 0x0, 0x0)
    AddressU: (U32, 0x0, 0x0, 0x0)
    FilterMin: (U32, 0x0, 0x0, 0x0)
    FilterMip: (U32, 0x0, 0x0, 0x0)
    SamplerName: (String, 0x0, 0x0, 0x0)
    FilterMag: (U32, 0x0, 0x0, 0x0)
    UncensoredTextures: (Map, Hash, String, 0x0)
    TextureName: (String, 0x0, 0x0, 0x0)
    AddressW: (U32, 0x0, 0x0, 0x0)
    pass

class CharacterInitRequirement():
    ParticipantChampion: (Hash, 0x0, 0x0, 0x0)
    RequiredChampion: (Hash, 0x0, 0x0, 0x0)
    mRelativeTeam: (U8, 0x0, 0x0, 0x0)
    pass

class MapDynamicSpotlight(MapSpotlightBase):
    Type: (U8, 0x0, 0x0, 0x0)
    VisibilityController: (Link, 0x0, 0x0, IMapVisibilityController)
    UpdaterType: (Link, 0x0, 0x0, MapLightUpdaterType)
    HdrScale: (F32, 0x0, 0x0, 0x0)
    pass

class MultiLineTextElementData(BaseElementData):
    mTextAlignmentVertical: (U8, 0x0, 0x0, 0x0)
    mFontDescription: (Link, 0x0, 0x0, GameFontDescription)
    mTextAlignment: (U8, 0x0, 0x0, 0x0)
    mTextAlignmentHorizontal: (U8, 0x0, 0x0, 0x0)
    pass

class StrawberryMapContainer():
    MapContainer: (String, 0x0, 0x0, 0x0)
    pass

class 0x90af7a04(ITftBehaviorScriptEvent):
    pass

class 0x90afdb57(TableValue):
    mValue: (I32, 0x0, 0x0, 0x0)
    Value: (I32, 0x0, 0x0, 0x0)
    pass

class FloatComparisonMaterialDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    mValueA: (Pointer, 0x0, 0x0, IDynamicMaterialFloatDriver)
    mValueA: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    mValueB: (Pointer, 0x0, 0x0, IDynamicMaterialFloatDriver)
    mValueB: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    mOperator: (U32, 0x0, 0x0, 0x0)
    pass

class 0x90f7282b(IGameModeConfig):
    IsLuaEnabled: (Bool, 0x0, 0x0, 0x0)
    pass

class FadeOverTimeBehavior(ITargeterFadeBehavior):
    mStartAlpha: (F32, 0x0, 0x0, 0x0)
    mTimeEnd: (F32, 0x0, 0x0, 0x0)
    mEndAlpha: (F32, 0x0, 0x0, 0x0)
    mTimeStart: (F32, 0x0, 0x0, 0x0)
    pass

class ChildMissileSiblingRepulsion(MissileBehaviorSpec):
    mRepulsionModel: (U32, 0x0, 0x0, 0x0)
    mSiblingRepulsion: (F32, 0x0, 0x0, 0x0)
    mMaxSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class 0x911f126a():
    Vfx: (Hash, 0x0, 0x0, 0x0)
    0xe50e4f4f: (String, 0x0, 0x0, 0x0)
    pass

class HudPurchaseDialog(ViewController):
    mConfirmButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    mCloseButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class DistanceToPlayerMaterialFloatDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    MinDistance: (F32, 0x0, 0x0, 0x0)
    MaxDistance: (F32, 0x0, 0x0, 0x0)
    pass

class RotatingBannerEntry():
    SponsorTexturePath: (File, 0x0, 0x0, 0x0)
    TimesShownPerCycle: (U32, 0x0, 0x0, 0x0)
    RelativeDisplayTime: (U32, 0x0, 0x0, 0x0)
    pass

class SummonerBadgeData():
    BadgeId: (U32, 0x0, 0x0, 0x0)
    RenderScale: (F32, 0x0, 0x0, 0x0)
    BadgeTroyFile: (String, 0x0, 0x0, 0x0)
    VerticalOffset: (F32, 0x0, 0x0, 0x0)
    pass

class MapScriptLocator(MapLocator):
    LevelScriptFunctionLink: (Pointer, 0x0, 0x0, LevelScriptFunctionLink)
    LevelScriptFunctionLink: (Pointer, 0x0, 0x0, LevelScriptControllerFunctionLink)
    ScriptName: (String, 0x0, 0x0, 0x0)
    pass

class MinimapIconBehavior():
    Duration: (F32, 0x0, 0x0, 0x0)
    pass

class HudItemShopRecItemCardDefinition(HudItemShopItemIconDefinition):
    BundleItemPrimaryIcon: (Hash, 0x0, 0x0, 0x0)
    AdviceLabel: (Hash, 0x0, 0x0, 0x0)
    AdviceLabel: (Link, 0x0, 0x0, BaseElementData)
    CardHoverMythic: (Hash, 0x0, 0x0, 0x0)
    CardHoverMythic: (Link, 0x0, 0x0, BaseElementData)
    BundleItemMoreTagHover: (Hash, 0x0, 0x0, 0x0)
    AdviceEmptyTextHover: (Hash, 0x0, 0x0, 0x0)
    AdviceEmptyTextHover: (Link, 0x0, 0x0, BaseElementData)
    CardRefreshNonMythicVfx: (Hash, 0x0, 0x0, 0x0)
    CardRefreshNonMythicVfx: (Link, 0x0, 0x0, BaseElementData)
    AdviceCharBorderHover1: (Hash, 0x0, 0x0, 0x0)
    AdviceCharBorderHover1: (Link, 0x0, 0x0, BaseElementData)
    AdviceCharBorderHover0: (Hash, 0x0, 0x0, 0x0)
    AdviceCharBorderHover0: (Link, 0x0, 0x0, BaseElementData)
    BundleItemIcon: (Link, 0x0, 0x0, BaseElementData)
    CardSelectedNonMythic: (Hash, 0x0, 0x0, 0x0)
    CardSelectedNonMythic: (Link, 0x0, 0x0, BaseElementData)
    CardHoverNonMythic: (Hash, 0x0, 0x0, 0x0)
    CardHoverNonMythic: (Link, 0x0, 0x0, BaseElementData)
    BriefText: (Hash, 0x0, 0x0, 0x0)
    BriefText: (Link, 0x0, 0x0, BaseElementData)
    BundleItemFrameUnpurchasable: (Hash, 0x0, 0x0, 0x0)
    AdviceEmptyIconMythicHover: (Hash, 0x0, 0x0, 0x0)
    AdviceEmptyIconMythicHover: (Link, 0x0, 0x0, BaseElementData)
    BundleStackText: (Link, 0x0, 0x0, BaseElementData)
    BundleItemFrameHoverIcon: (Hash, 0x0, 0x0, 0x0)
    BundleItemFrameHoverIcon: (Link, 0x0, 0x0, BaseElementData)
    BundleItemFrameIcon: (Hash, 0x0, 0x0, 0x0)
    BundleItemFrameIcon: (Link, 0x0, 0x0, BaseElementData)
    BundleItemMoreText: (Hash, 0x0, 0x0, 0x0)
    CardHoverMythicVfx: (Hash, 0x0, 0x0, 0x0)
    CardHoverMythicVfx: (Link, 0x0, 0x0, BaseElementData)
    CardDefault: (Hash, 0x0, 0x0, 0x0)
    CardDefault: (Link, 0x0, 0x0, BaseElementData)
    BundleStackSecondaryText: (Hash, 0x0, 0x0, 0x0)
    AdviceEmptyIconNonMythicHover: (Hash, 0x0, 0x0, 0x0)
    AdviceEmptyIconNonMythicHover: (Link, 0x0, 0x0, BaseElementData)
    AdviceIconHoverMythic: (Hash, 0x0, 0x0, 0x0)
    AdviceIconHoverMythic: (Link, 0x0, 0x0, BaseElementData)
    CardSelectedMythic: (Hash, 0x0, 0x0, 0x0)
    CardSelectedMythic: (Link, 0x0, 0x0, BaseElementData)
    AdviceEmptyIconDefault: (Hash, 0x0, 0x0, 0x0)
    AdviceEmptyIconDefault: (Link, 0x0, 0x0, BaseElementData)
    CardHoverNonMythicVfx: (Hash, 0x0, 0x0, 0x0)
    CardHoverNonMythicVfx: (Link, 0x0, 0x0, BaseElementData)
    PlusIcon: (Link, 0x0, 0x0, BaseElementData)
    AdviceIconDefault: (Hash, 0x0, 0x0, 0x0)
    AdviceIconDefault: (Link, 0x0, 0x0, BaseElementData)
    AdviceIconHoverNonMythic: (Hash, 0x0, 0x0, 0x0)
    AdviceIconHoverNonMythic: (Link, 0x0, 0x0, BaseElementData)
    AdviceCharBorder1: (Hash, 0x0, 0x0, 0x0)
    AdviceCharBorder1: (Link, 0x0, 0x0, BaseElementData)
    AdviceCharBorder0: (Hash, 0x0, 0x0, 0x0)
    AdviceCharBorder0: (Link, 0x0, 0x0, BaseElementData)
    BundleItemMoreTag: (Hash, 0x0, 0x0, 0x0)
    CardSelectedNonMythicVfx: (Hash, 0x0, 0x0, 0x0)
    CardSelectedNonMythicVfx: (Link, 0x0, 0x0, BaseElementData)
    CardSelectedMythicVfx: (Hash, 0x0, 0x0, 0x0)
    CardSelectedMythicVfx: (Link, 0x0, 0x0, BaseElementData)
    BriefTextBackdrop: (Hash, 0x0, 0x0, 0x0)
    BriefTextBackdrop: (Link, 0x0, 0x0, BaseElementData)
    AdviceEmptyText: (Hash, 0x0, 0x0, 0x0)
    AdviceEmptyText: (Link, 0x0, 0x0, BaseElementData)
    CardRefreshMythicVfx: (Hash, 0x0, 0x0, 0x0)
    CardRefreshMythicVfx: (Link, 0x0, 0x0, BaseElementData)
    AdviceCharIcon0: (Hash, 0x0, 0x0, 0x0)
    AdviceCharIcon0: (Link, 0x0, 0x0, BaseElementData)
    AdviceCharIcon1: (Hash, 0x0, 0x0, 0x0)
    AdviceCharIcon1: (Link, 0x0, 0x0, BaseElementData)
    BundleItemSecondaryIcon: (Hash, 0x0, 0x0, 0x0)
    BundleStackPrimaryText: (Hash, 0x0, 0x0, 0x0)
    pass

class OptionItemHotkeys(IOptionItem):
    Template: (Hash, 0x0, 0x0, 0x0)
    pass

class AllTrueMaterialDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    mDrivers: (List, 0x0, Pointer, ILogicBoolDriver)
    mDrivers: (List, 0x0, Pointer, IDynamicMaterialBoolDriver)
    pass

class MissionCategoryButtonDefinition():
    Button: (Hash, 0x0, 0x0, 0x0)
    HeaderKey: (String, 0x0, 0x0, 0x0)
    Category: (U32, 0x0, 0x0, 0x0)
    pass

class 0x92b6b7fa(IScriptBlock):
    MaxValue: (Pointer, 0x0, 0x0, IIntGet)
    0xdec56440: (List2, 0x0, Pointer, IIntGet)
    OutputTable: (Embed, 0x0, 0x0, CustomTableSet)
    MinValue: (Pointer, 0x0, 0x0, IIntGet)
    pass

class EnterFowVisibility(MissileVisibilitySpec):
    mMissileClientWaitForTargetUpdateBeforeMissileShow: (Bool, 0x0, 0x0, 0x0)
    mMissileClientExitFowPrediction: (Bool, 0x0, 0x0, 0x0)
    pass

class TotalTurnAngleParametricUpdater(IFloatParametricUpdater):
    pass

class SpellEffectAmount():
    Value: (List, 0x7, F32, 0x0)
    pass

class VectorTableSet(RsTableSet, ScriptTableSet):
    pass

class PlayGameRootScene(RootScene):
    pass

class 0x9316b8d7(GameObject):
    pass

class MapActionPlayPostEffect(MapAction):
    Duration: (F32, 0x0, 0x0, 0x0)
    BlendOutTime: (F32, 0x0, 0x0, 0x0)
    PostFxMaterial: (Link, 0x0, 0x0, StaticMaterialDef)
    Priority: (U8, 0x0, 0x0, 0x0)
    BlendInTime: (F32, 0x0, 0x0, 0x0)
    pass

class 0x93228fac():
    IllustrationIcon: (Hash, 0x0, 0x0, 0x0)
    LoadoutType: (U32, 0x0, 0x0, 0x0)
    ButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class TftHintMessageData():
    TargetElement: (Hash, 0x0, 0x0, 0x0)
    ShowArrow: (Bool, 0x0, 0x0, 0x0)
    MessageTrakey: (String, 0x0, 0x0, 0x0)
    MessageAnchor: (U8, 0x0, 0x0, 0x0)
    pass

class ViewControllerListFilter_Map(ViewControllerListFilterI):
    Map: (String, 0x0, 0x0, 0x0)
    pass

class NeutralMinionSpawnConfig():
    AiUnitName: (String, 0x0, 0x0, 0x0)
    0x96cbc77d: (Hash, 0x0, 0x0, 0x0)
    MapObjectName: (String, 0x0, 0x0, 0x0)
    SpawnAnimationName: (String, 0x0, 0x0, 0x0)
    pass

class ScoreLineSrSpectatorUiData(ScoreLineBaseUiData):
    ItemSlots: (Embed, 0x0, 0x0, DetailedItemSlots)
    ChampionGold: (Embed, 0x0, 0x0, ChampionGoldUiData)
    pass

class 0x93adc5b3(0x377491e8):
    DistanceBetween: (F32, 0x0, 0x0, 0x0)
    pass

class ICatalogEntryOwner():
    pass

class 0x93e412e0():
    MeterCompleteLeft: (Hash, 0x0, 0x0, 0x0)
    LevelPipDefault: (Hash, 0x0, 0x0, 0x0)
    FrameCompleteIcon: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    LevelText: (Hash, 0x0, 0x0, 0x0)
    QuantityText: (Hash, 0x0, 0x0, 0x0)
    MeterHolderLeft: (Hash, 0x0, 0x0, 0x0)
    ManagedLayout: (Hash, 0x0, 0x0, 0x0)
    FrameAvailableIcon: (Hash, 0x0, 0x0, 0x0)
    LevelPipActive: (Hash, 0x0, 0x0, 0x0)
    MeterHolderRight: (Hash, 0x0, 0x0, 0x0)
    MilestoneRewardsIconBackground: (Hash, 0x0, 0x0, 0x0)
    MeterCompleteRight: (Hash, 0x0, 0x0, 0x0)
    MeterHolderStart: (Hash, 0x0, 0x0, 0x0)
    LevelPipClaimed: (Hash, 0x0, 0x0, 0x0)
    HitRegion: (Hash, 0x0, 0x0, 0x0)
    MilestoneRewardsIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class ExperienceCurveData():
    mTeamRubberbandCoefficient: (F32, 0x0, 0x0, 0x0)
    mLevelDifferenceExperienceMultiplier: (F32, 0x0, 0x0, 0x0)
    mTeamRubberbandLogarithmicSteepness: (F32, 0x0, 0x0, 0x0)
    mTeamRubberbandMaxLevelGap: (I32, 0x0, 0x0, 0x0)
    mExperienceGrantedMultForSharedKillPerLevel: (List, 0x0, F32, 0x0)
    LevelDifferenceExperienceMultiplierPerLevel: (List, 0x0, F32, 0x0)
    mExperienceGrantedForKillPerLevel: (List, 0x0, F32, 0x0)
    mTeamRubberbandMaximumPercent: (F32, 0x0, 0x0, 0x0)
    mExperienceRequiredPerLevel: (List, 0x0, F32, 0x0)
    mMinimumExperienceMultiplier: (F32, 0x0, 0x0, 0x0)
    mBaseExperienceMultiplier: (F32, 0x0, 0x0, 0x0)
    DefaultMaxLevel: (U32, 0x0, 0x0, 0x0)
    pass

class 0x93f9cdb7(IScriptBlock, IBehaviorScriptBlock):
    pass

class 0x9407508d(IScriptBlock, IBehaviorScriptBlock):
    Sequence: (Embed, 0x0, 0x0, ScriptBtFailure)
    pass

class DebugPrintToChatBlock(IDebugScriptBlock, IScriptBlock):
    Color: (Color, 0x0, 0x0, 0x0)
    Value: (Embed, 0x0, 0x0, ScriptTableGet)
    Value: (Pointer, 0x0, 0x0, ScriptTableGet)
    Src: (Pointer, 0x0, 0x0, ScriptTableGet)
    ToSay: (Pointer, 0x0, 0x0, IStringGet)
    pass

class MapProp(MapPropCommon):
    pass

class TftRequiredUnitProperty():
    ActiveCondition: (Bool, 0x0, 0x0, 0x0)
    Property: (Link, 0x0, 0x0, TftUnitPropertyDefinition)
    pass

class RegionsThatAllowContent():
    mRegionList: (List, 0x0, Hash, 0x0)
    pass

class SpellPipsUiData():
    PipTargetRect: (Hash, 0x0, 0x0, 0x0)
    EmptyPips: (List, 0x6, Hash, 0x0)
    FullPips: (List, 0x6, Hash, 0x0)
    pass

class TftGameStartSequenceTutorial(TftGameStartSequence):
    GameWelcomeVfx: (Hash, 0x0, 0x0, 0x0)
    GameWelcomeLocVnVn: (Hash, 0x0, 0x0, 0x0)
    GameWelcomeVfxStartTimeSecs: (F32, 0x0, 0x0, 0x0)
    GameWelcomeScene: (Hash, 0x0, 0x0, 0x0)
    GameWelcomeLocZhCn: (Hash, 0x0, 0x0, 0x0)
    GameWelcomeLocZhTw: (Hash, 0x0, 0x0, 0x0)
    GameWelcomeLocScene: (Hash, 0x0, 0x0, 0x0)
    GameWelcomeVfxShowDurationSecs: (F32, 0x0, 0x0, 0x0)
    pass

class Cheat():
    mPage: (U32, 0x0, 0x0, 0x0)
    mName: (String, 0x0, 0x0, 0x0)
    mRecastFrequency: (F32, 0x0, 0x0, 0x0)
    mCheatMenuUiData: (Pointer, 0x0, 0x0, CheatMenuUiData)
    mIsPlayerFacing: (Bool, 0x0, 0x0, 0x0)
    mFloatingTextDisplayName: (String, 0x0, 0x0, 0x0)
    mRow: (U32, 0x0, 0x0, 0x0)
    mIsToggleCheat: (Bool, 0x0, 0x0, 0x0)
    mHotkey: (String, 0x0, 0x0, 0x0)
    mDynamicTooltipText: (String, 0x0, 0x0, 0x0)
    mTooltipText: (String, 0x0, 0x0, 0x0)
    pass

class 0x947c803c():
    0x164a7d2f: (Hash, 0x0, 0x0, 0x0)
    0x1f74ec0a: (Hash, 0x0, 0x0, 0x0)
    0x46b3cf33: (Hash, 0x0, 0x0, 0x0)
    0xa69f71da: (Hash, 0x0, 0x0, 0x0)
    0xab207fa4: (Hash, 0x0, 0x0, 0x0)
    0xfc670d7a: (Pointer, 0x0, 0x0, SpawningUiDefinition)
    0xfcf3a73d: (Pointer, 0x0, 0x0, SpawningUiDefinition)
    pass

class TftBattlepassSelectedRewardUiData():
    RewardIcon: (Hash, 0x0, 0x0, 0x0)
    PremiumBgVfx: (Hash, 0x0, 0x0, 0x0)
    FrameLocked: (Hash, 0x0, 0x0, 0x0)
    BodyText: (Hash, 0x0, 0x0, 0x0)
    FrameAvailable: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    ClaimCeremonyVfx: (Hash, 0x0, 0x0, 0x0)
    pass

class TrackerIconSlots():
    Slots: (List, 0x0, Hash, 0x0)
    pass

class TftCutsceneCamOverrideEntry():
    ValueEnd: (F32, 0x0, 0x0, 0x0)
    OverrideType: (U32, 0x0, 0x0, 0x0)
    ValueEndType: (U32, 0x0, 0x0, 0x0)
    ValueStart: (F32, 0x0, 0x0, 0x0)
    pass

class LootOutputBase():
    pass

class TftStreakData():
    mLossStreaks: (List, 0x0, Embed, TftStreak)
    mWinstreaks: (List, 0x0, Embed, TftStreak)
    pass

class FxActionAnimateInstance(IFxActionInstance):
    pass

class 0x959c604(0xb639bddc):
    LootItem: (Link, 0x0, 0x0, LootItem)
    pass

class 0x95a54f7f():
    0x11a984f4: (F32, 0x0, 0x0, 0x0)
    0x15764231: (Bool, 0x0, 0x0, 0x0)
    0x18ffad34: (F32, 0x0, 0x0, 0x0)
    0x219846ee: (Bool, 0x0, 0x0, 0x0)
    0x33e51007: (U32, 0x0, 0x0, 0x0)
    0x39b1cfd5: (List, 0x0, Embed, 0x97b4592f)
    0x3ab2e1f8: (U32, 0x0, 0x0, 0x0)
    0x3e1d2b61: (U32, 0x0, 0x0, 0x0)
    0x4907d5e4: (U32, 0x0, 0x0, 0x0)
    0x544e3630: (U32, 0x0, 0x0, 0x0)
    0x54f92210: (String, 0x0, 0x0, 0x0)
    0x5ff8f4b: (F32, 0x0, 0x0, 0x0)
    0x64cc630a: (Bool, 0x0, 0x0, 0x0)
    0x69cacfb7: (Bool, 0x0, 0x0, 0x0)
    0x6fe4a3ac: (U32, 0x0, 0x0, 0x0)
    0x71cc7781: (Bool, 0x0, 0x0, 0x0)
    0x73cc7aa7: (Bool, 0x0, 0x0, 0x0)
    0x74cc7c3a: (Bool, 0x0, 0x0, 0x0)
    0x802a3ef5: (U32, 0x0, 0x0, 0x0)
    0x83d22c28: (Bool, 0x0, 0x0, 0x0)
    0x89cd2efe: (U32, 0x0, 0x0, 0x0)
    0x8ff9404: (F32, 0x0, 0x0, 0x0)
    0x9395532: (String, 0x0, 0x0, 0x0)
    0x96f617f0: (U32, 0x0, 0x0, 0x0)
    0xb26260f5: (List, 0x0, Embed, 0x3cabf2f3)
    0xb70f6598: (List, 0x0, Embed, 0x5e416660)
    0xb8b62b19: (Bool, 0x0, 0x0, 0x0)
    0xbb706b07: (List, 0x0, Embed, 0x3cabf2f3)
    0xbe7480b4: (U32, 0x0, 0x0, 0x0)
    0xbff98bd: (F32, 0x0, 0x0, 0x0)
    0xca60a888: (Bool, 0x0, 0x0, 0x0)
    0xcc8530: (Bool, 0x0, 0x0, 0x0)
    0xd22f5547: (U32, 0x0, 0x0, 0x0)
    0xd4cb10eb: (U32, 0x0, 0x0, 0x0)
    0xe974f094: (U32, 0x0, 0x0, 0x0)
    0xeacb5cd5: (U32, 0x0, 0x0, 0x0)
    0xfbcedbdc: (Bool, 0x0, 0x0, 0x0)
    pass

class ContextualConditionCharacterMetadata(ICharacterSubcondition):
    mData: (String, 0x0, 0x0, 0x0)
    mCategory: (String, 0x0, 0x0, 0x0)
    pass

class BaseLoadoutData(CatalogEntry, ICatalogEntryOwner):
    CatalogEntry: (Embed, 0x0, 0x0, CatalogEntry)
    mContentId: (String, 0x0, 0x0, 0x0)
    mDescriptionTraKey: (String, 0x0, 0x0, 0x0)
    mNameTraKey: (String, 0x0, 0x0, 0x0)
    RotationalShopItemData: (Embed, 0x0, 0x0, TftRotationalShopItemData)
    pass

class BasicAttackSlotIntDriver(ILogicIntDriver):
    pass

class X3dSharedConstantBufferDef():
    Register: (I32, 0x0, 0x0, 0x0)
    Frequency: (U32, 0x0, 0x0, 0x0)
    Frequency: (U8, 0x0, 0x0, 0x0)
    Type: (U32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    OpenglConstantBuffer: (Bool, 0x0, 0x0, 0x0)
    Constants: (List, 0x0, Embed, X3dSharedConstantDef)
    PlatformMask: (U32, 0x0, 0x0, 0x0)
    pass

class NeutralMinionCampClearedLogic(IStatStoneLogicDriver):
    pass

class UiMetricUnitVisionScore(UiMetricUnitTypeSimpleI):
    pass

class 0x964f0775(IContextualCondition):
    mChampion: (Hash, 0x0, 0x0, 0x0)
    pass

class StatStoneSet(ICatalogEntryOwner):
    CatalogEntry: (Embed, 0x0, 0x0, CatalogEntry)
    Name: (String, 0x0, 0x0, 0x0)
    StatStones: (List, 0x0, Link, StatStoneData)
    pass

class SkipTerrain(MissileBehaviorSpec):
    mMaximumTerrainWallsToSkip: (Option, 0x0, U32, 0x0)
    pass

class 0x968ce2ad():
    WaveToSpawn: (Link, 0x0, 0x0, 0xe75aad84)
    pass

class GameModeTeamFightViewController(TeamFightViewController):
    pass

class VfxChildIdentifier():
    EffectName: (String, 0x0, 0x0, 0x0)
    Effect: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    EffectKey: (Hash, 0x0, 0x0, 0x0)
    pass

class Obj_NavPoint(BuildingClient):
    pass

class 0x96b3514(MapComponent):
    IntroMaterial: (Link, 0x0, 0x0, StaticMaterialDef)
    pass

class GravityHeightSolver(HeightSolverType):
    mGravity: (F32, 0x0, 0x0, 0x0)
    pass

class 0x96d673eb(0xc9dd46d2):
    pass

class VfxPrimitiveCameraQuad(VfxPrimitiveBase):
    pass

class ToonInkingFilterParams():
    mResultScale: (F32, 0x0, 0x0, 0x0)
    mPixelSize: (F32, 0x0, 0x0, 0x0)
    mMaxVal: (F32, 0x0, 0x0, 0x0)
    mMinVal: (F32, 0x0, 0x0, 0x0)
    pass

class CombatTextOverride():
    OverriddenToggles: (Map, U8, Bool, 0x0)
    pass

class LevelScriptOnInit(ILevelScriptEvent):
    pass

class HudCalloutIdentifier():
    Portrait: (Hash, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    pass

class ReplayCameraControlsData():
    TeamFowComboBoxDefinition: (Hash, 0x0, 0x0, 0x0)
    CameraControlsComboBoxDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class GameModeConstantFloat(GameModeConstant):
    mValue: (F32, 0x0, 0x0, 0x0)
    pass

class TftItemList():
    VfxResourceResolver: (Link, 0x0, 0x0, ResourceResolver)
    mItems: (List, 0x0, Link, TftItemData)
    mItems: (List2, 0x0, Link, TftItemData)
    pass

class 0x9784901f():
    0x2ea2ef00: (Hash, 0x0, 0x0, 0x0)
    0x39b2057a: (Hash, 0x0, 0x0, 0x0)
    PhaseIcon: (Hash, 0x0, 0x0, 0x0)
    PhaseHitRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class PromoBannerElement():
    Target: (U32, 0x0, 0x0, 0x0)
    Id: (String, 0x0, 0x0, 0x0)
    Tier: (U32, 0x0, 0x0, 0x0)
    InstanceData: (List2, 0x0, Embed, 0xa77231b9)
    PreferredOrder: (U8, 0x0, 0x0, 0x0)
    pass

class 0x97b4592f():
    0x306b1fcf: (String, 0x0, 0x0, 0x0)
    0x69c9256c: (String, 0x0, 0x0, 0x0)
    pass

class UiElementEffectAmmoData(UiElementEffectData):
    mEffectColor0: (Color, 0x0, 0x0, 0x0)
    mEffectColor1: (Color, 0x0, 0x0, 0x0)
    pass

class FxActionVfxMissileInstance(IFxActionInstance):
    pass

class StealthBreakFlags():
    OnTakeDamage: (Bool, 0x0, 0x0, 0x0)
    OnPerceptionBubbleReveal: (Bool, 0x0, 0x0, 0x0)
    OnEnemyChampionInDetectionRadius: (Bool, 0x0, 0x0, 0x0)
    InRangeOfTower: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x980af3d2(TargetingTypeData):
    pass

class ContextualConditionSpellBuffName(IContextualConditionBuff):
    SpellBuff: (Hash, 0x0, 0x0, 0x0)
    pass

class TrackData():
    mName: (Hash, 0x0, 0x0, 0x0)
    mName: (String, 0x0, 0x0, 0x0)
    mIndex: (U32, 0x0, 0x0, 0x0)
    mBlendMode: (U32, 0x0, 0x0, 0x0)
    mBlendMode: (U8, 0x0, 0x0, 0x0)
    mBlendWeight: (F32, 0x0, 0x0, 0x0)
    mPriority: (U32, 0x0, 0x0, 0x0)
    mPriority: (U8, 0x0, 0x0, 0x0)
    pass

class NotificationDialog(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    SceneOptions: (List2, 0x0, Embed, NotificationDialogOption)
    SceneRoot: (Hash, 0x0, 0x0, 0x0)
    pass

class ItemRecommendationOverrideStartingItemSet():
    mStartingItems: (List, 0x0, Hash, 0x0)
    pass

class MapWorldParticles():
    Particles: (List2, 0x0, Embed, MapWorldParticle)
    0xe21f1d86: (Bool, 0x0, 0x0, 0x0)
    EmitterBone: (String, 0x0, 0x0, 0x0)
    pass

class VelocityDynamicMaterialFloatDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    pass

class TftTraitAssignment():
    Trait: (Link, 0x0, 0x0, TftTraitData)
    CharacterList: (List2, 0x0, Hash, 0x0)
    pass

class OptionItemFilter_Ios(IOptionItemFilter):
    pass

class ContextualConditionMapId(IContextualCondition):
    mMapIds: (U32, 0x0, 0x0, 0x0)
    pass

class 0x990115ea():
    0x3392c041: (String, 0x0, 0x0, 0x0)
    0x58766309: (String, 0x0, 0x0, 0x0)
    0x720e4297: (Hash, 0x0, 0x0, 0x0)
    0x96349f57: (String, 0x0, 0x0, 0x0)
    0xa807a4b2: (String, 0x0, 0x0, 0x0)
    0xd0666cc4: (String, 0x0, 0x0, 0x0)
    IconFrame: (Hash, 0x0, 0x0, 0x0)
    pass

class IconElementCircleMaskeExtension(IconElementDataExtension):
    pass

class CreateFunctionBlock(IScriptBlock):
    Function: (Embed, 0x0, 0x0, FunctionTableSet)
    FunctionDefinition: (Embed, 0x0, 0x0, FunctionDefinition)
    pass

class DirectedTrackingElementViewController(ViewController):
    GlowingRotatingArrow: (Hash, 0x0, 0x0, 0x0)
    AnimatedRotatingArrow: (Hash, 0x0, 0x0, 0x0)
    Loadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    ArrowAnchorBase: (Hash, 0x0, 0x0, 0x0)
    pass

class ShieldParams():
    mAllShieldColor: (Color, 0x0, 0x0, 0x0)
    mMagicShieldColor: (Color, 0x0, 0x0, 0x0)
    mPhysicalShieldColor: (Color, 0x0, 0x0, 0x0)
    pass

class SubPartScaledProportionalToStat(IGameCalculationPart):
    mSubpart: (Pointer, 0x0, 0x0, IGameCalculationPart)
    mStat: (U8, 0x0, 0x0, 0x0)
    mStatFormula: (U8, 0x0, 0x0, 0x0)
    StatType: (U8, 0x0, 0x0, 0x0)
    OutputType: (U8, 0x0, 0x0, 0x0)
    mStyleTag: (String, 0x0, 0x0, 0x0)
    mStyleTagIfScaled: (String, 0x0, 0x0, 0x0)
    UseNewStats: (Bool, 0x0, 0x0, 0x0)
    mRatio: (F32, 0x0, 0x0, 0x0)
    pass

class ILogicDriver():
    pass

class Companion(Character, BaseLoadoutData):
    pass

class MapPathLineSegment(MapPathSegment):
    pass

class MinimapMissilePipSource(IPictureInPictureSource):
    pass

class CheatPage():
    mCheats: (List, 0x0, Link, Cheat)
    pass

class OptionItemFilter_Not(IOptionItemFilter):
    Filter: (Pointer, 0x0, 0x0, IOptionItemFilter)
    pass

class 0x99cce3c(IFxAction):
    ZoomEase: (U32, 0x0, 0x0, 0x0)
    ZoomEase: (U8, 0x0, 0x0, 0x0)
    pass

class NumberFormattingData():
    TrillionAbbreviationTraKey: (String, 0x0, 0x0, 0x0)
    OneHundredMillionAbbreviationTraKey: (String, 0x0, 0x0, 0x0)
    TenThousandAbbreviationTraKey: (String, 0x0, 0x0, 0x0)
    ThousandsSeparatorTraKey: (String, 0x0, 0x0, 0x0)
    SecondAbbreviationTraKey: (String, 0x0, 0x0, 0x0)
    LocalizedFormattingBehavior: (Map, Hash, Link, NumberFormattingBehavior)
    HourAbbreviationTraKey: (String, 0x0, 0x0, 0x0)
    MinuteAbbreviationTraKey: (String, 0x0, 0x0, 0x0)
    ThousandAbbreviationTraKey: (String, 0x0, 0x0, 0x0)
    PercentageFormatTraKey: (String, 0x0, 0x0, 0x0)
    DecimalSeparatorTraKey: (String, 0x0, 0x0, 0x0)
    KilometersAbbreviationTraKey: (String, 0x0, 0x0, 0x0)
    BillionAbbreviationTraKey: (String, 0x0, 0x0, 0x0)
    MillionAbbreviationTraKey: (String, 0x0, 0x0, 0x0)
    WeekAbbreviationTraKey: (String, 0x0, 0x0, 0x0)
    DayAbbreviationTraKey: (String, 0x0, 0x0, 0x0)
    MetersAbbreviationTraKey: (String, 0x0, 0x0, 0x0)
    pass

class DamageSpellTextureData():
    RuneDamageIconTextureName: (String, 0x0, 0x0, 0x0)
    ItemDamageIconTextureName: (String, 0x0, 0x0, 0x0)
    BasicAttackIconTextureName: (String, 0x0, 0x0, 0x0)
    UnknownDamageIconTextureName: (String, 0x0, 0x0, 0x0)
    pass

class 0x99f44e83(ILolSpellScriptEvent):
    pass

class DeathTimesScalingPoint():
    mPercentIncrease: (F32, 0x0, 0x0, 0x0)
    mStartTime: (U32, 0x0, 0x0, 0x0)
    pass

class UiElementGroupManagedLayout(UiElementGroup):
    pass

class ISpellCalculation():
    mMultiplier: (Pointer, 0x0, 0x0, ISpellCalculationPart)
    mExpandedTooltipCalculationDisplay: (U8, 0x0, 0x0, 0x0)
    mSimpleTooltipCalculationDisplay: (U8, 0x0, 0x0, 0x0)
    pass

class TooltipInstanceListElement():
    TypeIndex: (I32, 0x0, 0x0, 0x0)
    Type: (String, 0x0, 0x0, 0x0)
    NameOverride: (String, 0x0, 0x0, 0x0)
    Style: (U32, 0x0, 0x0, 0x0)
    Multiplier: (F32, 0x0, 0x0, 0x0)
    pass

class LuaPropertyData():
    pass

class PatchingViewController(ViewController):
    ProgressText: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    KoreanWarningText: (Hash, 0x0, 0x0, 0x0)
    ProgressBar: (Hash, 0x0, 0x0, 0x0)
    BeginPatchingButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    KoreanAgeRatingIcon: (Hash, 0x0, 0x0, 0x0)
    StatusMessageText: (Hash, 0x0, 0x0, 0x0)
    OpenTeamPlannerButton: (Hash, 0x0, 0x0, 0x0)
    BuildVersionText: (Hash, 0x0, 0x0, 0x0)
    LoginLogoMapping: (Map, U32, Hash, 0x0)
    BeginPatchingButton: (Hash, 0x0, 0x0, 0x0)
    OpenTeamPlannerButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class AnimationResourceData():
    mAnimationFilePath: (String, 0x0, 0x0, 0x0)
    pass

class 0x9a573886(0x5a8ba29d):
    pass

class PartnerGroupPlacements():
    PartnerGroupColors: (List, 0x4, Color, 0x0)
    PlacementTexts: (List, 0x4, Hash, 0x0)
    PlacementBanners: (List, 0x4, Hash, 0x0)
    PartnerGroupBanners: (List, 0x4, Hash, 0x0)
    pass

class CherryConfigs(IGameModeConfig):
    0x31ff922d: (List2, 0x0, Embed, 0x31ff922d)
    ArenaData: (List, 0x0, Embed, CherryArenaData)
    ArenaData: (List2, 0x0, Embed, CherryArenaData)
    CombatRoundDamage: (List, 0x0, U8, 0x0)
    AugmentColors: (List, 0x0, Color, 0x0)
    AugmentColors: (List2, 0x0, Color, 0x0)
    0xa5fc6415: (List, 0x0, U32, 0x0)
    CameraBoundsAsPercentageOfMapBounds: (F32, 0x0, 0x0, 0x0)
    0xf021feb3: (U8, 0x0, 0x0, 0x0)
    pass

class 0x9a7de981(0x6ca3cfd):
    Value: (String, 0x0, 0x0, 0x0)
    pass

class ReciprocityConfig(IGameModeConfig):
    0x15470412: (F32, 0x0, 0x0, 0x0)
    0x3240c71d: (F32, 0x0, 0x0, 0x0)
    ThrottleLimit: (U8, 0x0, 0x0, 0x0)
    0x4ef1af67: (F32, 0x0, 0x0, 0x0)
    0x5502892e: (F32, 0x0, 0x0, 0x0)
    0x8e26fcb2: (F32, 0x0, 0x0, 0x0)
    0xb878b552: (F32, 0x0, 0x0, 0x0)
    0xe6f743fc: (F32, 0x0, 0x0, 0x0)
    0xf307d34d: (F32, 0x0, 0x0, 0x0)
    0xff1c05f: (F32, 0x0, 0x0, 0x0)
    pass

class DialogPickChoice():
    DisplayName: (String, 0x0, 0x0, 0x0)
    IconPath: (String, 0x0, 0x0, 0x0)
    ChoiceDescription: (String, 0x0, 0x0, 0x0)
    pass

class 0x9ab8b8e6():
    Description: (String, 0x0, 0x0, 0x0)
    Vfx: (Hash, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class TftPassRewardLoadoutData(TftPassRewardBase):
    LoadoutData: (Link, 0x0, 0x0, BaseLoadoutData)
    pass

class TftCutsceneAttachClip(TftCutsceneClip):
    AttachViaBone: (String, 0x0, 0x0, 0x0)
    BlackboardGameObjectName: (String, 0x0, 0x0, 0x0)
    BlackboardTransformName: (String, 0x0, 0x0, 0x0)
    pass

class TftStageUiData():
    StageIconPath: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    TooltipTitleTra: (String, 0x0, 0x0, 0x0)
    TooltipIconPath: (String, 0x0, 0x0, 0x0)
    TooltipDescriptionTra: (String, 0x0, 0x0, 0x0)
    pass

class TftUnitInfoCharacterRoleData():
    Button: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class CustomReductionMultiplierCalculationPart(IGameCalculationPart, ISpellCalculationPart):
    mSubPartToReduceBy: (Pointer, 0x0, 0x0, IGameCalculationPart)
    mSubPartToReduceBy: (Pointer, 0x0, 0x0, ISpellCalculationPart)
    mMaximumReductionPercent: (F32, 0x0, 0x0, 0x0)
    pass

class FontLocaleType():
    FontFilePathBold: (String, 0x0, 0x0, 0x0)
    LocaleName: (String, 0x0, 0x0, 0x0)
    Italic: (Bool, 0x0, 0x0, 0x0)
    Mipped: (Bool, 0x0, 0x0, 0x0)
    Glow: (Bool, 0x0, 0x0, 0x0)
    FontFilePathItalics: (String, 0x0, 0x0, 0x0)
    mFontFilePath: (String, 0x0, 0x0, 0x0)
    FontName: (String, 0x0, 0x0, 0x0)
    Bold: (Bool, 0x0, 0x0, 0x0)
    pass

class Area(TargetingTypeData):
    pass

class VfxLingerDefinitionData():
    UseSeparateLingerColor: (Flag, 0x0, 0x0, 0x0)
    KeyedLingerAcceleration: (Embed, 0x0, 0x0, ValueVector3)
    UseKeyedLingerDrag: (Flag, 0x0, 0x0, 0x0)
    KeyedLingerDrag: (Embed, 0x0, 0x0, ValueVector3)
    UseLingerScale: (Flag, 0x0, 0x0, 0x0)
    SeparateLingerColor: (Embed, 0x0, 0x0, ValueColor)
    UseKeyedLingerVelocity: (Flag, 0x0, 0x0, 0x0)
    LingerRotation: (Embed, 0x0, 0x0, ValueVector3)
    LingerScale: (Embed, 0x0, 0x0, ValueVector3)
    UseLingerRotation: (Flag, 0x0, 0x0, 0x0)
    UseKeyedLingerAcceleration: (Flag, 0x0, 0x0, 0x0)
    KeyedLingerVelocity: (Embed, 0x0, 0x0, ValueVector3)
    pass

class 0x9b1b08e6():
    EarnedChallengeLevel: (Hash, 0x0, 0x0, 0x0)
    EarnedChallengeDesc: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    EarnedChallengeName: (Hash, 0x0, 0x0, 0x0)
    Title: (Hash, 0x0, 0x0, 0x0)
    EarnedChallengeTokenIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class MapPathSegment():
    EndPosition: (Vec3, 0x0, 0x0, 0x0)
    pass

class SkinBorder():
    0x146a6dde: (List2, 0x0, I32, 0x0)
    CatalogEntry: (Embed, 0x0, 0x0, CatalogEntry)
    0x32c5d2fe: (List2, 0x0, Embed, SkinBorderOrder)
    LocalizedName: (String, 0x0, 0x0, 0x0)
    Priority: (U8, 0x0, 0x0, 0x0)
    Image: (String, 0x0, 0x0, 0x0)
    LocalizedDescription: (String, 0x0, 0x0, 0x0)
    pass

class UiElementEffectRotatingIconData(UiElementEffectData):
    TextureData: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mAtlas: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    pass

class SpellLevelUpInfo():
    mRequirements: (List, 0x0, Embed, SpellRankUpRequirements)
    MinLevelUpLevel: (List, 0x0, I32, 0x0)
    pass

class SkinCharacterDataProperties():
    DefaultAnimations: (List, 0x0, String, 0x0)
    SkipVoOverride: (Bool, 0x0, 0x0, 0x0)
    mOptionalBin: (Embed, 0x0, 0x0, HudOptionalBinData)
    ParticleOverride_ChampionKillDeathParticle: (String, 0x0, 0x0, 0x0)
    HudMuteEvent: (String, 0x0, 0x0, 0x0)
    IconCircleScale: (Option, 0x0, F32, 0x0)
    IconCircleScale: (Option, 0x0, String, 0x0)
    ExtraActionButtonCount: (U32, 0x0, 0x0, 0x0)
    EmoteBuffbone: (String, 0x0, 0x0, 0x0)
    EndOfGameAlias: (String, 0x0, 0x0, 0x0)
    ArmorMaterial: (String, 0x0, 0x0, 0x0)
    ChampionSkinName: (String, 0x0, 0x0, 0x0)
    VintageCutoffDate: (String, 0x0, 0x0, 0x0)
    mOptionalBins: (List, 0x0, Embed, HudOptionalBinData)
    AlternateIconsCircle: (List, 0x0, String, 0x0)
    EmblemLinks: (List, 0x0, Link, EmblemData)
    HudUnmuteEvent: (String, 0x0, 0x0, 0x0)
    SkinAnimationProperties: (Embed, 0x0, 0x0, SkinAnimationProperties)
    SkinMeshProperties: (Embed, 0x0, 0x0, SkinMeshDataProperties)
    OverrideOnScreenName: (String, 0x0, 0x0, 0x0)
    UseBetaRenderingObject: (Bool, 0x0, 0x0, 0x0)
    AttributeFlags: (U32, 0x0, 0x0, 0x0)
    SkinParent: (I32, 0x0, 0x0, 0x0)
    HealthBarData: (Embed, 0x0, 0x0, CharacterHealthBarDataRecord)
    ThemeMusic: (List, 0x0, String, 0x0)
    SkinAudioNameOverride: (String, 0x0, 0x0, 0x0)
    HealthBarData_AdditionalWorldOffset: (Option, 0x0, Vec3, 0x0)
    HealthBarData_AdditionalWorldOffset: (Vec3, 0x0, 0x0, 0x0)
    CanShareThemeMusic: (Bool, 0x0, 0x0, 0x0)
    MaterialOverridePriority: (I32, 0x0, 0x0, 0x0)
    GodrayFxBone: (String, 0x0, 0x0, 0x0)
    mResourceResolver: (Link, 0x0, 0x0, ResourceResolver)
    ExtraCharacterPreloads: (List, 0x0, String, 0x0)
    SkinUpgradeData: (Embed, 0x0, 0x0, SkinUpgradeData)
    HealthBarData_CustomUnitBarKey: (String, 0x0, 0x0, 0x0)
    VoiceOverOverride: (String, 0x0, 0x0, 0x0)
    UncensoredLoadscreens: (Map, Hash, String, 0x0)
    mAdditionalResourceResolvers: (List, 0x0, Link, ResourceResolver)
    IdleParticlesEffects: (List, 0x0, Embed, SkinCharacterDataProperties_CharacterIdleEffect)
    SkinClassification: (U32, 0x0, 0x0, 0x0)
    PersistentEffectConditions: (List, 0x0, Pointer, PersistentEffectConditionData)
    PersistentEffectConditions: (List2, 0x0, Pointer, PersistentEffectConditionData)
    IconAvatar: (String, 0x0, 0x0, 0x0)
    UncensoredIconCircles: (Map, Hash, String, 0x0)
    SkinAudioProperties: (Embed, 0x0, 0x0, SkinAudioProperties)
    MetaDataTags: (String, 0x0, 0x0, 0x0)
    HealthBarData_YOffset: (F32, 0x0, 0x0, 0x0)
    HealthBarData_YOffset: (Option, 0x0, F32, 0x0)
    Loadscreen: (Embed, 0x0, 0x0, CensoredImage)
    Loadscreen: (String, 0x0, 0x0, 0x0)
    UncensoredIconSquares: (Map, Hash, String, 0x0)
    mMarkerEvents: (Link, 0x0, 0x0, VoMarkerEvents)
    ChampionSkinId: (I32, 0x0, 0x0, 0x0)
    IconSquare: (Option, 0x0, String, 0x0)
    RarityGemOverride: (Option, 0x0, I32, 0x0)
    AlternateIconsSquare: (List, 0x0, String, 0x0)
    0xb67a2dd8: (List, 0x0, Embed, 0x9c1d99c0)
    mEmblems: (List, 0x0, Embed, SkinEmblem)
    mSpawnParticleName: (String, 0x0, 0x0, 0x0)
    LoadscreenVintage: (Embed, 0x0, 0x0, CensoredImage)
    LoadscreenVintage: (String, 0x0, 0x0, 0x0)
    0xc534e009: (Bool, 0x0, 0x0, 0x0)
    Animations: (String, 0x0, 0x0, 0x0)
    mContextualActionData: (Link, 0x0, 0x0, ContextualActionData)
    HealthBarData_Scale: (F32, 0x0, 0x0, 0x0)
    HealthBarData_Scale: (Option, 0x0, F32, 0x0)
    ContextualActionRuleConfigFile: (String, 0x0, 0x0, 0x0)
    SecondaryResourceHudDisplayData: (Pointer, 0x0, 0x0, ISecondaryResourceDisplayData)
    0xe484edc4: (Link, 0x0, 0x0, 0x48f3fe52)
    IconCircle: (Option, 0x0, String, 0x0)
    EmoteYOffset: (F32, 0x0, 0x0, 0x0)
    0xeda7817e: (Link, 0x0, 0x0, StaticMaterialDef)
    HealthBarData_XOffset: (F32, 0x0, 0x0, 0x0)
    HealthBarData_XOffset: (Option, 0x0, F32, 0x0)
    EmoteLoadout: (Hash, 0x0, 0x0, 0x0)
    ParticleOverride_DeathParticle: (String, 0x0, 0x0, 0x0)
    SkinUiProperties: (Embed, 0x0, 0x0, SkinUiProperties)
    IconMinimap: (Option, 0x0, String, 0x0)
    pass

class MissionsPanelViewController(ViewController):
    MilestoneProgressMeter: (Embed, 0x0, 0x0, UiMilestoneProgressMeter)
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    EventMissionsCompletedText: (Hash, 0x0, 0x0, 0x0)
    MissionFullManagedLayout: (Hash, 0x0, 0x0, 0x0)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    EventMissionsCompletedKey: (String, 0x0, 0x0, 0x0)
    EventEmptyGroup: (Hash, 0x0, 0x0, 0x0)
    ViewPaneDefinition: (Embed, 0x0, 0x0, ViewPaneDefinition)
    MissionButtonsLayout: (Hash, 0x0, 0x0, 0x0)
    EmptyGroup: (Hash, 0x0, 0x0, 0x0)
    WeeklyMissionTemplate: (Embed, 0x0, 0x0, UiWeeklyMissionTemplate)
    ViewPaneLink: (Hash, 0x0, 0x0, 0x0)
    MissionCategoryButtons: (List, 0x0, Embed, MissionCategoryButtonDefinition)
    ObjectiveMeterAnimEaseType: (U32, 0x0, 0x0, 0x0)
    ObjectiveMeterAnimEaseType: (U8, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    ObjectiveMeterAnimTimeSecs: (F32, 0x0, 0x0, 0x0)
    pass

class EffectArcFillElementData(EffectElementData):
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    pass

class LoadingScreenRatedTierIconData():
    RatedTierSourceIcons: (Map, String, Hash, 0x0)
    pass

class NotificationSettings():
    DefaultSound: (String, 0x0, 0x0, 0x0)
    CustomizedSounds: (Map, U8, String, 0x0)
    pass

class VfxComplexParticleDefinitionData():
    NumFrames: (I32, 0x0, 0x0, 0x0)
    EmissionMeshName: (String, 0x0, 0x0, 0x0)
    Rotation: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    bState: (U32, 0x0, 0x0, 0x0)
    UvMode: (U32, 0x0, 0x0, 0x0)
    ProjectionYRange: (F32, 0x0, 0x0, 0x0)
    Acceleration: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    Velocity: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    MeshTextureName: (String, 0x0, 0x0, 0x0)
    Color: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    QuadType: (I32, 0x0, 0x0, 0x0)
    QuadType: (U32, 0x0, 0x0, 0x0)
    BeamMode: (U32, 0x0, 0x0, 0x0)
    UvScrollRateMult: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    ProjectionFading: (F32, 0x0, 0x0, 0x0)
    StartFrame: (I32, 0x0, 0x0, 0x0)
    DirectionVelocityScale: (F32, 0x0, 0x0, 0x0)
    Scale: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    NumFramesMult: (I32, 0x0, 0x0, 0x0)
    OldMeshName: (String, 0x0, 0x0, 0x0)
    AnimationName: (String, 0x0, 0x0, 0x0)
    FrameRate: (F32, 0x0, 0x0, 0x0)
    ChildParticleSetDefinition: (Embed, 0x0, 0x0, VfxChildParticleSetDefinitionData)
    StartFrameMult: (I32, 0x0, 0x0, 0x0)
    Drag: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    Distortion: (F32, 0x0, 0x0, 0x0)
    EmissionMeshScale: (F32, 0x0, 0x0, 0x0)
    FrameRateMult: (F32, 0x0, 0x0, 0x0)
    BindWeight: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    TrailMode: (U32, 0x0, 0x0, 0x0)
    UvScrollRate: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    BeamParticleDefinition: (Embed, 0x0, 0x0, VfxBeamParticleDefinitionData)
    WorldAcceleration: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    DirectionVelocityMinScale: (F32, 0x0, 0x0, 0x0)
    MeshTextureMultName: (String, 0x0, 0x0, 0x0)
    UvParallaxScale: (F32, 0x0, 0x0, 0x0)
    SimpleMeshName: (String, 0x0, 0x0, 0x0)
    MeshName: (String, 0x0, 0x0, 0x0)
    PostRotateOrientationAxis: (Vec3, 0x0, 0x0, 0x0)
    pass

class ContextualConditionMultikillSize(IContextualCondition):
    mMultikillSize: (U8, 0x0, 0x0, 0x0)
    pass

class CallOnMissileBounce(MissileTriggeredActionSpec):
    pass

class GetFxObjectDynamicMaterialBoolDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    mKeyName: (String, 0x0, 0x0, 0x0)
    pass

class ReplayVisibilityMenuViewController(ViewController):
    KillCalloutsVisibilityKey: (String, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    ObjectiveTimersVisibilityKey: (String, 0x0, 0x0, 0x0)
    TeamFramesBlueVisibilityKey: (String, 0x0, 0x0, 0x0)
    LineHeightRef: (Hash, 0x0, 0x0, 0x0)
    TimeControleVisibilityKey: (String, 0x0, 0x0, 0x0)
    TargetFrameVisibilityKey: (String, 0x0, 0x0, 0x0)
    CheckboxTemplate: (Hash, 0x0, 0x0, 0x0)
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    TeamFramesPurpleVisibilityKey: (String, 0x0, 0x0, 0x0)
    QuestsVisibilityKey: (String, 0x0, 0x0, 0x0)
    TeamScoreVisibilityKey: (String, 0x0, 0x0, 0x0)
    Layout: (Hash, 0x0, 0x0, 0x0)
    SceneHandle: (Hash, 0x0, 0x0, 0x0)
    ScoreboardVisibilityKey: (String, 0x0, 0x0, 0x0)
    ChatVisibilityKey: (String, 0x0, 0x0, 0x0)
    LabelTemplate: (Hash, 0x0, 0x0, 0x0)
    AllVisibilityKey: (String, 0x0, 0x0, 0x0)
    MinimapVisibilityKey: (String, 0x0, 0x0, 0x0)
    pass

class TftPayoutViewController(ViewController):
    ProgressBar: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    RewardBars: (List2, 0x0, Embed, 0x209fa685)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    0x5d768e72: (Hash, 0x0, 0x0, 0x0)
    0x6373e403: (F32, 0x0, 0x0, 0x0)
    BannerDurationSecs: (F32, 0x0, 0x0, 0x0)
    0x6e6af651: (F32, 0x0, 0x0, 0x0)
    0x87eb3d0: (F32, 0x0, 0x0, 0x0)
    RewardNumber: (Hash, 0x0, 0x0, 0x0)
    RewardNumberDisplay: (Hash, 0x0, 0x0, 0x0)
    0xb2a69226: (Color, 0x0, 0x0, 0x0)
    0xc60338b8: (String, 0x0, 0x0, 0x0)
    RewardTrakey: (String, 0x0, 0x0, 0x0)
    pass

class 0x9c1d99c0():
    CombinableDamageFormat: (Link, 0x0, 0x0, FloatTextFormattingData)
    CriticalDamageFormat: (Link, 0x0, 0x0, FloatTextFormattingData)
    Spells: (List2, 0x0, Hash, 0x0)
    0x80cf3335: (Embed, 0x0, 0x0, 0x7a1a2d27)
    Spell: (Hash, 0x0, 0x0, 0x0)
    DefaultDamageFormat: (Link, 0x0, 0x0, FloatTextFormattingData)
    pass

class DamageTypeMeter():
    MeterElements: (List, 0x3, Hash, 0x0)
    pass

class ChampionSelectionViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    ChampionSlots: (List, 0x0, Embed, UiChampionSelectionSlotData)
    ChampionSlotUiData: (List, 0x0, Embed, UiChampionSelectionSlotData)
    pass

class IsCastingBoolDriver(ILogicBoolDriver):
    SpellSlot: (U32, 0x0, 0x0, 0x0)
    pass

class AbilityResourcePipsData():
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    Pips: (Embed, 0x0, 0x0, AbilityResourcePipTypeMap)
    PipSpacer: (Embed, 0x0, 0x0, AbilityResourcePipSpacerTypeMap)
    pass

class AttackSpeedParametricUpdater(IFloatParametricUpdater):
    pass

class UiElementGroupButton(UiElementGroup):
    pass

class SoundEventData(BaseEventData):
    mSkipIfPastEndFrame: (Bool, 0x0, 0x0, 0x0)
    mIsKillEvent: (Bool, 0x0, 0x0, 0x0)
    mSoundName: (String, 0x0, 0x0, 0x0)
    mIsLoop: (Bool, 0x0, 0x0, 0x0)
    ConditionClipTransitionType: (U16, 0x0, 0x0, 0x0)
    pass

class TextElementData(UiElementData, BaseElementData):
    mTextAlignmentVertical: (U8, 0x0, 0x0, 0x0)
    mEnableOuterGlow: (Bool, 0x0, 0x0, 0x0)
    mSize: (U32, 0x0, 0x0, 0x0)
    WrappingMode: (U8, 0x0, 0x0, 0x0)
    mHtmlStyleSheet: (Link, 0x0, 0x0, CssSheet)
    mFontDescription: (Link, 0x0, 0x0, GameFontDescription)
    mTextAlignment: (U8, 0x0, 0x0, 0x0)
    mMultiline: (Bool, 0x0, 0x0, 0x0)
    mTextAlignmentHorizontal: (U8, 0x0, 0x0, 0x0)
    TraKey: (String, 0x0, 0x0, 0x0)
    IconScale: (F32, 0x0, 0x0, 0x0)
    pass

class UiUnitStatusDurationBarData():
    TenacityBar: (Hash, 0x0, 0x0, 0x0)
    StatusDurationBar: (Hash, 0x0, 0x0, 0x0)
    pass

class OptionItemCheckbox(IOptionItem):
    TooltipTraKey: (String, 0x0, 0x0, 0x0)
    Template: (Hash, 0x0, 0x0, 0x0)
    Negate: (Bool, 0x0, 0x0, 0x0)
    LabelTraKey: (String, 0x0, 0x0, 0x0)
    Option: (U16, 0x0, 0x0, 0x0)
    pass

class MissileClient(Missile):
    pass

class 0x9cd4ec31():
    0xfed597b0: (F32, 0x0, 0x0, 0x0)
    pass

class VfxEmitterDefinitionData():
    FlexUvScroll: (Embed, 0x0, 0x0, FlexValueVector2)
    IsRandomStartFrameMult: (Flag, 0x0, 0x0, 0x0)
    DoesParticleLifetimeScale: (Bool, 0x0, 0x0, 0x0)
    DoesParticleLifetimeScale: (Flag, 0x0, 0x0, 0x0)
    ReflectionOpacityDirect: (F32, 0x0, 0x0, 0x0)
    ReflectionFresnel: (F32, 0x0, 0x0, 0x0)
    SubmeshesToDraw: (List, 0x0, U32, 0x0)
    ParticleUvRotateRateMult: (Embed, 0x0, 0x0, IntegratedValueFloat)
    ParticleUvRotateRateMult: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    PalleteSrcMixColor: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    PalleteSrcMixColor: (Embed, 0x0, 0x0, ValueColor)
    KeywordsRequired: (List, 0x0, String, 0x0)
    ColorRenderFlags: (U16, 0x0, 0x0, 0x0)
    ColorRenderFlags: (U8, 0x0, 0x0, 0x0)
    TexDivMult: (Vec2, 0x0, 0x0, 0x0)
    StencilReferenceId: (Hash, 0x0, 0x0, 0x0)
    ReflectionOpacityGlancing: (F32, 0x0, 0x0, 0x0)
    VoiceOverPersistentName: (String, 0x0, 0x0, 0x0)
    TimeActiveDuringPeriod: (Option, 0x0, F32, 0x0)
    UvScroll: (Vec2, 0x0, 0x0, 0x0)
    MeshRenderFlags: (U16, 0x0, 0x0, 0x0)
    MeshRenderFlags: (U8, 0x0, 0x0, 0x0)
    BirthTilingSize: (Embed, 0x0, 0x0, ValueVector3)
    BirthTilingSize: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    StencilMode: (U32, 0x0, 0x0, 0x0)
    StencilMode: (U8, 0x0, 0x0, 0x0)
    UseLingerColor: (Bool, 0x0, 0x0, 0x0)
    UseLingerColor: (Flag, 0x0, 0x0, 0x0)
    ScaleEmitOffsetByBoundObjectHeight: (F32, 0x0, 0x0, 0x0)
    BirthRotationalVelocity0: (Embed, 0x0, 0x0, ValueVector3)
    BirthRotationalVelocity0: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    NumFrames: (I32, 0x0, 0x0, 0x0)
    NumFrames: (U16, 0x0, 0x0, 0x0)
    BirthRotationalVelocity1: (Embed, 0x0, 0x0, ValueFloat)
    BirthRotationalVelocity1: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    UvScrollRate1: (Vec2, 0x0, 0x0, 0x0)
    EmissionMeshName: (String, 0x0, 0x0, 0x0)
    UvScrollRate0: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    TimeBeforeFirstEmission: (F32, 0x0, 0x0, 0x0)
    CensorPolicy: (U32, 0x0, 0x0, 0x0)
    CensorPolicy: (U8, 0x0, 0x0, 0x0)
    ParticleLinger: (F32, 0x0, 0x0, 0x0)
    ParticleLinger: (Option, 0x0, F32, 0x0)
    bState: (U32, 0x0, 0x0, 0x0)
    FlexBirthUvoffset: (Embed, 0x0, 0x0, FlexValueVector2)
    FlexBirthUvoffset: (Pointer, 0x0, 0x0, FlexValueVector2)
    ColorLookUpTypeX: (U32, 0x0, 0x0, 0x0)
    ColorLookUpTypeX: (U8, 0x0, 0x0, 0x0)
    UvMode: (U32, 0x0, 0x0, 0x0)
    UvMode: (U8, 0x0, 0x0, 0x0)
    ColorLookUpTypeY: (U32, 0x0, 0x0, 0x0)
    ColorLookUpTypeY: (U8, 0x0, 0x0, 0x0)
    FlexUvScrollMult: (Embed, 0x0, 0x0, FlexValueVector2)
    IsGroundLayer: (Bool, 0x0, 0x0, 0x0)
    IsGroundLayer: (Flag, 0x0, 0x0, 0x0)
    ProjectionYRange: (F32, 0x0, 0x0, 0x0)
    ParticleLifetime: (Embed, 0x0, 0x0, ValueFloat)
    ParticleLifetime: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    IsLocalOrientation: (Bool, 0x0, 0x0, 0x0)
    IsLocalOrientation: (Flag, 0x0, 0x0, 0x0)
    FlexScaleBirthScale: (Embed, 0x0, 0x0, FlexTypeFloat)
    FlexScaleBirthScale: (Pointer, 0x0, 0x0, FlexTypeFloat)
    TextureFlipV: (Flag, 0x0, 0x0, 0x0)
    TextureFlipU: (Flag, 0x0, 0x0, 0x0)
    SubmeshesToDrawAlways: (List, 0x0, U32, 0x0)
    TextureMult: (Pointer, 0x0, 0x0, VfxTextureMultDefinitionData)
    TextureMult: (String, 0x0, 0x0, 0x0)
    Acceleration: (Embed, 0x0, 0x0, ValueVector3)
    Acceleration: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    BirthUvScrollRateMult: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    BirthUvScrollRateMult: (Embed, 0x0, 0x0, ValueVector2)
    TexAddressModeBase: (U32, 0x0, 0x0, 0x0)
    TexAddressModeBase: (U8, 0x0, 0x0, 0x0)
    Velocity: (Embed, 0x0, 0x0, ValueVector3)
    Velocity: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    UseLingerVelocity: (Bool, 0x0, 0x0, 0x0)
    UseLingerVelocity: (Flag, 0x0, 0x0, 0x0)
    BirthUvRotateRate: (Embed, 0x0, 0x0, ValueFloat)
    BirthUvRotateRate: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    MaterialOverrideDefinitions: (List, 0x0, Embed, VfxMaterialOverrideDefinitionData)
    MaterialOverrideDefinitions: (List, 0x0, Pointer, VfxMaterialOverrideDefinitionData)
    UvRotationMult: (Embed, 0x0, 0x0, ValueFloat)
    Disabled: (Bool, 0x0, 0x0, 0x0)
    HasFixedOrbit: (Bool, 0x0, 0x0, 0x0)
    HasFixedOrbit: (Flag, 0x0, 0x0, 0x0)
    IsUniformScale: (Flag, 0x0, 0x0, 0x0)
    BirthRotationalAcceleration: (Embed, 0x0, 0x0, ValueVector3)
    BirthRotationalAcceleration: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    ParticleIsLocalOrientation: (Bool, 0x0, 0x0, 0x0)
    ParticleIsLocalOrientation: (Flag, 0x0, 0x0, 0x0)
    ScaleBirthScaleByBoundObjectRadius: (F32, 0x0, 0x0, 0x0)
    MeshTextureName: (String, 0x0, 0x0, 0x0)
    UvTransformCenterMult: (Vec2, 0x0, 0x0, 0x0)
    ParticleLingerType: (U32, 0x0, 0x0, 0x0)
    ParticleLingerType: (U8, 0x0, 0x0, 0x0)
    TextureMultFlipU: (Flag, 0x0, 0x0, 0x0)
    FresnelColor: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    FresnelColor: (Embed, 0x0, 0x0, ValueColor)
    TextureMultFlipV: (Flag, 0x0, 0x0, 0x0)
    EmitterLinger: (F32, 0x0, 0x0, 0x0)
    EmitterLinger: (Option, 0x0, F32, 0x0)
    SpawnShape: (Pointer, 0x0, 0x0, IVfxShape)
    Texture: (String, 0x0, 0x0, 0x0)
    DisableBackfaceCull: (Bool, 0x0, 0x0, 0x0)
    EmitterName: (String, 0x0, 0x0, 0x0)
    Color: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    Color: (Embed, 0x0, 0x0, ValueColor)
    ReflectionDefinition: (Pointer, 0x0, 0x0, VfxReflectionDefinitionData)
    DistortionMode: (U32, 0x0, 0x0, 0x0)
    QuadType: (U32, 0x0, 0x0, 0x0)
    IsSingleParticle: (Bool, 0x0, 0x0, 0x0)
    IsSingleParticle: (Flag, 0x0, 0x0, 0x0)
    PaletteBlendRegister: (I32, 0x0, 0x0, 0x0)
    ScaleBias: (Vec2, 0x0, 0x0, 0x0)
    ColorblindVisibility: (U8, 0x0, 0x0, 0x0)
    KeywordsIncluded: (List, 0x0, String, 0x0)
    TextureAddressModeBase: (U32, 0x0, 0x0, 0x0)
    CustomMaterial: (Pointer, 0x0, 0x0, VfxMaterialDefinitionData)
    OffsetLifeScalingSymmetryMode: (U32, 0x0, 0x0, 0x0)
    OffsetLifeScalingSymmetryMode: (U8, 0x0, 0x0, 0x0)
    FlexShapeDefinition: (Pointer, 0x0, 0x0, VfxFlexShapeDefinitionData)
    RateByVelocityFunction: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    RateByVelocityFunction: (Embed, 0x0, 0x0, ValueVector2)
    BirthOrbitalVelocity: (Embed, 0x0, 0x0, ValueVector3)
    BirthOrbitalVelocity: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    ParticleBind: (Vec2, 0x0, 0x0, 0x0)
    VoiceOverOnCreateName: (String, 0x0, 0x0, 0x0)
    WriteAlphaOnly: (Flag, 0x0, 0x0, 0x0)
    EmitterUvScrollRate: (Vec2, 0x0, 0x0, 0x0)
    Lifetime: (Option, 0x0, F32, 0x0)
    HasVariableStartTime: (Bool, 0x0, 0x0, 0x0)
    HasVariableStartTime: (Flag, 0x0, 0x0, 0x0)
    EmissionSurfaceDefinition: (Pointer, 0x0, 0x0, VfxEmissionSurfaceData)
    ReflectionFresnelColor: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    ReflectionFresnelColor: (Embed, 0x0, 0x0, ValueColor)
    EmitterPosition: (Embed, 0x0, 0x0, ValueVector3)
    BirthRotation0: (Embed, 0x0, 0x0, ValueVector3)
    BirthRotation0: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    BirthRotation1: (Embed, 0x0, 0x0, ValueFloat)
    BirthRotation1: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    BeamMode: (U32, 0x0, 0x0, 0x0)
    TexAddressModeMult: (U32, 0x0, 0x0, 0x0)
    TexAddressModeMult: (U8, 0x0, 0x0, 0x0)
    UvScrollRateMult: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    UseLingerScale: (Bool, 0x0, 0x0, 0x0)
    UseLingerScale: (Flag, 0x0, 0x0, 0x0)
    ParticleUvScrollRate: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    ParticleUvScrollRate: (Embed, 0x0, 0x0, IntegratedValueVector2)
    MiscRenderFlags: (U16, 0x0, 0x0, 0x0)
    MiscRenderFlags: (U8, 0x0, 0x0, 0x0)
    ModulationFactor: (Vec4, 0x0, 0x0, 0x0)
    ParticlesShareRandomValue: (Flag, 0x0, 0x0, 0x0)
    DepthBiasFactors: (Vec2, 0x0, 0x0, 0x0)
    OffsetLifetimeScaling: (Vec3, 0x0, 0x0, 0x0)
    LingerRotation0: (Embed, 0x0, 0x0, ValueVector3)
    TrailSmoothingMode: (U8, 0x0, 0x0, 0x0)
    ParticleUvScrollRateMult: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    ParticleUvScrollRateMult: (Embed, 0x0, 0x0, IntegratedValueVector2)
    FlexParticleLifetime: (Embed, 0x0, 0x0, FlexValueFloat)
    FlexParticleLifetime: (Pointer, 0x0, 0x0, FlexValueFloat)
    Rotation1: (Embed, 0x0, 0x0, ValueFloat)
    Rotation1: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    Rotation0: (Embed, 0x0, 0x0, IntegratedValueVector3)
    Rotation0: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    FluidDynamicsDefinition: (Pointer, 0x0, 0x0, 0xe6cd2142)
    ProjectionFading: (F32, 0x0, 0x0, 0x0)
    BirthUvoffsetMult: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    BirthUvoffsetMult: (Embed, 0x0, 0x0, ValueVector2)
    UvTransformCenter: (Vec2, 0x0, 0x0, 0x0)
    FlexBirthRotationalVelocity1: (Embed, 0x0, 0x0, FlexValueFloat)
    FlexBirthRotationalVelocity1: (Pointer, 0x0, 0x0, FlexValueFloat)
    StartFrame: (I32, 0x0, 0x0, 0x0)
    StartFrame: (U16, 0x0, 0x0, 0x0)
    RenderPhaseOverride: (U32, 0x0, 0x0, 0x0)
    RenderPhaseOverride: (U8, 0x0, 0x0, 0x0)
    FlexRate: (Embed, 0x0, 0x0, FlexValueFloat)
    FlexRate: (Pointer, 0x0, 0x0, FlexValueFloat)
    FlexScaleEmitOffset: (Embed, 0x0, 0x0, FlexTypeFloat)
    FlexScaleEmitOffset: (Pointer, 0x0, 0x0, FlexTypeFloat)
    FlexBirthRotationalVelocity0: (Embed, 0x0, 0x0, FlexValueVector3)
    FlexBirthRotationalVelocity0: (Pointer, 0x0, 0x0, FlexValueVector3)
    DoesLifetimeScale: (Bool, 0x0, 0x0, 0x0)
    DoesLifetimeScale: (Flag, 0x0, 0x0, 0x0)
    ScaleEmitOffsetByBoundObjectRadius: (F32, 0x0, 0x0, 0x0)
    UvScrollClampMult: (Flag, 0x0, 0x0, 0x0)
    DirectionVelocityScale: (F32, 0x0, 0x0, 0x0)
    Primitive: (Pointer, 0x0, 0x0, VfxPrimitiveBase)
    StencilRef: (U32, 0x0, 0x0, 0x0)
    StencilRef: (U8, 0x0, 0x0, 0x0)
    Pass: (I16, 0x0, 0x0, 0x0)
    Pass: (I32, 0x0, 0x0, 0x0)
    UseEmissionMeshNormalForBirth: (Flag, 0x0, 0x0, 0x0)
    BeamSegments: (I32, 0x0, 0x0, 0x0)
    LingerScale0: (Embed, 0x0, 0x0, ValueVector3)
    EmitRotationAngles: (List, 0x0, Embed, ValueFloat)
    EmitRotationAngles: (List, 0x0, Embed, VfxAnimatedFloatVariableData)
    TrailCutoff: (F32, 0x0, 0x0, 0x0)
    FlexInstanceScale: (Pointer, 0x0, 0x0, FlexTypeFloat)
    BirthDrag: (Embed, 0x0, 0x0, ValueVector3)
    BirthDrag: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    BirthColor: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    BirthColor: (Embed, 0x0, 0x0, ValueColor)
    NumFramesMult: (I32, 0x0, 0x0, 0x0)
    ReflectionMapTexture: (String, 0x0, 0x0, 0x0)
    TexDiv: (Vec2, 0x0, 0x0, 0x0)
    PaletteDefinition: (Pointer, 0x0, 0x0, VfxPaletteDefinitionData)
    CensorModulateValue: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    CensorModulateValue: (Vec4, 0x0, 0x0, 0x0)
    PaletteSelector: (Embed, 0x0, 0x0, ValueVector3)
    PaletteSelector: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    IsRotationEnabled: (Bool, 0x0, 0x0, 0x0)
    IsRotationEnabled: (Flag, 0x0, 0x0, 0x0)
    FlexBirthTranslation: (Embed, 0x0, 0x0, FlexValueVector3)
    FlexBirthTranslation: (Pointer, 0x0, 0x0, FlexValueVector3)
    Fresnel: (F32, 0x0, 0x0, 0x0)
    UvScrollMult: (Vec2, 0x0, 0x0, 0x0)
    SoundOnCreateName: (String, 0x0, 0x0, 0x0)
    ScaleBirthScaleByBoundObjectSize: (F32, 0x0, 0x0, 0x0)
    UvRotation: (Embed, 0x0, 0x0, ValueFloat)
    AnimationName: (String, 0x0, 0x0, 0x0)
    LingerVelocity: (Embed, 0x0, 0x0, ValueVector3)
    LockedToEmitter: (Bool, 0x0, 0x0, 0x0)
    LockedToEmitter: (Flag, 0x0, 0x0, 0x0)
    Period: (Option, 0x0, F32, 0x0)
    SoundPersistentName: (String, 0x0, 0x0, 0x0)
    FrameRate: (F32, 0x0, 0x0, 0x0)
    Shape: (Embed, 0x0, 0x0, VfxShape)
    PaletteCount: (I32, 0x0, 0x0, 0x0)
    FlexBirthVelocity: (Embed, 0x0, 0x0, FlexValueVector3)
    FlexBirthVelocity: (Pointer, 0x0, 0x0, FlexValueVector3)
    ChildParticleSetDefinition: (Embed, 0x0, 0x0, VfxChildParticleSetDefinitionData)
    ChildParticleSetDefinition: (Pointer, 0x0, 0x0, VfxChildParticleSetDefinitionData)
    BirthAcceleration: (Embed, 0x0, 0x0, ValueVector3)
    BirthAcceleration: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    StartFrameMult: (I32, 0x0, 0x0, 0x0)
    FalloffTexture: (String, 0x0, 0x0, 0x0)
    SliceTechniqueRange: (F32, 0x0, 0x0, 0x0)
    UvScrollClamp: (Bool, 0x0, 0x0, 0x0)
    UvScrollClamp: (Flag, 0x0, 0x0, 0x0)
    IsEmitterSpace: (Flag, 0x0, 0x0, 0x0)
    FieldCollectionDefinition: (Embed, 0x0, 0x0, VfxFieldCollectionDefinitionData)
    FieldCollectionDefinition: (Pointer, 0x0, 0x0, VfxFieldCollectionDefinitionData)
    Rate: (Embed, 0x0, 0x0, ValueFloat)
    Rate: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    UseLingerDrag: (Bool, 0x0, 0x0, 0x0)
    UseLingerDrag: (Flag, 0x0, 0x0, 0x0)
    TranslationOverride: (Vec3, 0x0, 0x0, 0x0)
    DoesCastShadow: (Bool, 0x0, 0x0, 0x0)
    DoesCastShadow: (Flag, 0x0, 0x0, 0x0)
    ParticleColorTexture: (String, 0x0, 0x0, 0x0)
    RotationOverride: (Vec3, 0x0, 0x0, 0x0)
    FlexBirthUvScrollRateMult: (Pointer, 0x0, 0x0, FlexValueVector2)
    Drag: (Embed, 0x0, 0x0, ValueVector3)
    Drag: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    BirthUvoffset: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    BirthUvoffset: (Embed, 0x0, 0x0, ValueVector2)
    Linger: (Pointer, 0x0, 0x0, VfxLingerDefinitionData)
    Importance: (U32, 0x0, 0x0, 0x0)
    Importance: (U8, 0x0, 0x0, 0x0)
    AlphaRef: (I32, 0x0, 0x0, 0x0)
    AlphaRef: (U8, 0x0, 0x0, 0x0)
    IsFollowingTerrain: (Bool, 0x0, 0x0, 0x0)
    IsFollowingTerrain: (Flag, 0x0, 0x0, 0x0)
    LegacySimple: (Pointer, 0x0, 0x0, VfxEmitterLegacySimple)
    Distortion: (F32, 0x0, 0x0, 0x0)
    DistortionDefinition: (Pointer, 0x0, 0x0, VfxDistortionDefinitionData)
    FixedOrbitType: (U32, 0x0, 0x0, 0x0)
    FixedOrbitType: (U8, 0x0, 0x0, 0x0)
    SortEmittersByPos: (Flag, 0x0, 0x0, 0x0)
    EmissionMeshScale: (F32, 0x0, 0x0, 0x0)
    FlexBirthUvScrollRate: (Pointer, 0x0, 0x0, FlexValueVector2)
    SoftParticleParams: (Embed, 0x0, 0x0, VfxSoftParticleDefinitionData)
    SoftParticleParams: (Pointer, 0x0, 0x0, VfxSoftParticleDefinitionData)
    ParticleUvRotateRate: (Embed, 0x0, 0x0, IntegratedValueFloat)
    ParticleUvRotateRate: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    ScaleEmitOffsetByBoundObjectSize: (F32, 0x0, 0x0, 0x0)
    KeywordsExcluded: (List, 0x0, String, 0x0)
    FrameRateMult: (F32, 0x0, 0x0, 0x0)
    AlphaErosionDefinition: (Pointer, 0x0, 0x0, VfxAlphaErosionDefinitionData)
    MaterialDrivers: (Map, String, Pointer, IVfxMaterialDriver)
    Orientation: (U32, 0x0, 0x0, 0x0)
    Orientation: (U8, 0x0, 0x0, 0x0)
    RenderFlags: (U32, 0x0, 0x0, 0x0)
    BirthFrameRate: (Embed, 0x0, 0x0, ValueFloat)
    BirthFrameRate: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    IsTexturePixelated: (Bool, 0x0, 0x0, 0x0)
    MaximumRateByVelocity: (Option, 0x0, F32, 0x0)
    BindWeight: (Embed, 0x0, 0x0, ValueFloat)
    BindWeight: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    0xcb13aff1: (F32, 0x0, 0x0, 0x0)
    UvScaleMult: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    UvScaleMult: (Embed, 0x0, 0x0, ValueVector2)
    ColorLookUpOffsets: (Vec2, 0x0, 0x0, 0x0)
    TrailMode: (U32, 0x0, 0x0, 0x0)
    ChanceToNotExist: (F32, 0x0, 0x0, 0x0)
    BirthUvScrollRate: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    BirthUvScrollRate: (Embed, 0x0, 0x0, ValueVector2)
    BeamLocalSpaceSourceOffset: (Vec3, 0x0, 0x0, 0x0)
    EmitRotationAxes: (List, 0x0, Vec3, 0x0)
    0xd1ee8634: (Flag, 0x0, 0x0, 0x0)
    Material: (Link, 0x0, 0x0, IMaterialDef)
    Material: (Link, 0x0, 0x0, StaticMaterialDef)
    Scale1: (Embed, 0x0, 0x0, ValueFloat)
    Scale1: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    Scale0: (Embed, 0x0, 0x0, ValueVector3)
    Scale0: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    BeamParticleDefinition: (Embed, 0x0, 0x0, VfxBeamParticleDefinitionData)
    HasDistortion: (Bool, 0x0, 0x0, 0x0)
    UseNavmeshMask: (Flag, 0x0, 0x0, 0x0)
    IsDirectionOriented: (Bool, 0x0, 0x0, 0x0)
    IsDirectionOriented: (Flag, 0x0, 0x0, 0x0)
    UseLingerRotation: (Bool, 0x0, 0x0, 0x0)
    UseLingerRotation: (Flag, 0x0, 0x0, 0x0)
    LingerAcceleration: (Embed, 0x0, 0x0, ValueVector3)
    Audio: (Pointer, 0x0, 0x0, VfxEmitterAudio)
    IsRandomStartFrame: (Bool, 0x0, 0x0, 0x0)
    IsRandomStartFrame: (Flag, 0x0, 0x0, 0x0)
    EmitterUvScrollRateMult: (Vec2, 0x0, 0x0, 0x0)
    FlexOffset: (Embed, 0x0, 0x0, FlexValueVector3)
    FlexOffset: (Pointer, 0x0, 0x0, FlexValueVector3)
    ScaleOverride: (Vec3, 0x0, 0x0, 0x0)
    EmitOffset: (Embed, 0x0, 0x0, ValueVector3)
    EmitOffset: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    ScaleBirthScaleByBoundObjectHeight: (F32, 0x0, 0x0, 0x0)
    SpectatorPolicy: (U32, 0x0, 0x0, 0x0)
    SpectatorPolicy: (U8, 0x0, 0x0, 0x0)
    NormalMapTexture: (String, 0x0, 0x0, 0x0)
    MeshSkeletonName: (String, 0x0, 0x0, 0x0)
    LingerColor: (Embed, 0x0, 0x0, ValueColor)
    UvScrollAlphaMult: (Flag, 0x0, 0x0, 0x0)
    WorldAcceleration: (Embed, 0x0, 0x0, IntegratedValueVector3)
    WorldAcceleration: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    DirectionVelocityMinScale: (F32, 0x0, 0x0, 0x0)
    TrailSmoothingOn: (Bool, 0x0, 0x0, 0x0)
    HasPostRotateOrientation: (Flag, 0x0, 0x0, 0x0)
    BirthUvRotateRateMult: (Embed, 0x0, 0x0, ValueFloat)
    BirthUvRotateRateMult: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    UvScale: (Embed, 0x0, 0x0, VfxAnimatedVector2fVariableData)
    UvScale: (Embed, 0x0, 0x0, ValueVector2)
    ColorLookUpScales: (Vec2, 0x0, 0x0, 0x0)
    BirthScale0: (Embed, 0x0, 0x0, ValueVector3)
    BirthScale0: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    BirthScale1: (Embed, 0x0, 0x0, ValueFloat)
    BirthScale1: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    TrailMaxAddedPerFrame: (I32, 0x0, 0x0, 0x0)
    UseLingerAcceleration: (Bool, 0x0, 0x0, 0x0)
    UseLingerAcceleration: (Flag, 0x0, 0x0, 0x0)
    mUseNavmeshMask: (Bool, 0x0, 0x0, 0x0)
    Filtering: (Pointer, 0x0, 0x0, VfxEmitterFiltering)
    MeshTextureMultName: (String, 0x0, 0x0, 0x0)
    ScaleAlongMovementVector: (F32, 0x0, 0x0, 0x0)
    UvParallaxScale: (F32, 0x0, 0x0, 0x0)
    SimpleMeshName: (String, 0x0, 0x0, 0x0)
    MeshName: (String, 0x0, 0x0, 0x0)
    ScaleUpFromOrigin: (Bool, 0x0, 0x0, 0x0)
    ScaleUpFromOrigin: (Flag, 0x0, 0x0, 0x0)
    BirthVelocity: (Embed, 0x0, 0x0, ValueVector3)
    BirthVelocity: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    PostRotateOrientationAxis: (Vec3, 0x0, 0x0, 0x0)
    ExcludedAttachmentTypes: (List, 0x0, String, 0x0)
    BlendMode: (I32, 0x0, 0x0, 0x0)
    BlendMode: (U32, 0x0, 0x0, 0x0)
    BlendMode: (U8, 0x0, 0x0, 0x0)
    LingerDrag: (Embed, 0x0, 0x0, ValueVector3)
    BeamLocalSpaceTargetOffset: (Vec3, 0x0, 0x0, 0x0)
    BirthTranslation: (Embed, 0x0, 0x0, ValueVector3)
    BirthTranslation: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    PaletteTexture: (String, 0x0, 0x0, 0x0)
    FluidPartName: (String, 0x0, 0x0, 0x0)
    pass

class 0x9d23e01f(TargetingTypeData):
    pass

class ToolSpellDesc():
    DisplayName: (String, 0x0, 0x0, 0x0)
    Desc: (String, 0x0, 0x0, 0x0)
    pass

class AddHealthCheat(Cheat):
    mAmount: (F32, 0x0, 0x0, 0x0)
    mTarget: (U32, 0x0, 0x0, 0x0)
    pass

class 0x9d62f7e(ITargetingRangeValue):
    NamedDataValue: (Hash, 0x0, 0x0, 0x0)
    Spell: (Hash, 0x0, 0x0, 0x0)
    SpellLevel: (U32, 0x0, 0x0, 0x0)
    pass

class BehaviorMapConfig():
    DefaultChampionScripts: (List2, 0x0, Hash, 0x0)
    DefaultChampionScripts: (List2, 0x0, Link, BehaviorScript)
    0x1d6ec2db: (F32, 0x0, 0x0, 0x0)
    0x1fbd2db9: (Hash, 0x0, 0x0, 0x0)
    0x226cb2a5: (U32, 0x0, 0x0, 0x0)
    0x76ecf423: (U32, 0x0, 0x0, 0x0)
    0x8eb859e: (Map, U32, Bool, 0x0)
    0x8f14f810: (U32, 0x0, 0x0, 0x0)
    0x9887bb3b: (Hash, 0x0, 0x0, 0x0)
    0x9f3cf20: (Map, U8, Embed, 0xc006cb7a)
    BehaviorScriptContainers: (List, 0x0, Embed, BehaviorScriptContainer)
    0xa503816: (Bool, 0x0, 0x0, 0x0)
    0xcf783260: (Bool, 0x0, 0x0, 0x0)
    0xfc3b5428: (Bool, 0x0, 0x0, 0x0)
    0xfd9c252a: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x9d79fb9f():
    Skins: (List2, 0x0, U32, 0x0)
    Champion: (Link, 0x0, 0x0, Champion)
    pass

class UiSliderBarDefinition():
    ObjectPath: (Hash, 0x0, 0x0, 0x0)
    SliderClickedState: (Embed, 0x0, 0x0, UiSliderBarState)
    SliderHitRegion: (Link, 0x0, 0x0, RegionElementData)
    SliderHoveredState: (Embed, 0x0, 0x0, UiSliderBarState)
    0x99774fc7: (Bool, 0x0, 0x0, 0x0)
    SoundEvents: (Pointer, 0x0, 0x0, 0x2da50c9f)
    BarHoveredState: (Embed, 0x0, 0x0, UiSliderBarState)
    DefaultState: (Embed, 0x0, 0x0, UiSliderBarState)
    Direction: (U8, 0x0, 0x0, 0x0)
    BarHitRegion: (Link, 0x0, 0x0, RegionElementData)
    pass

class ClientStateCommonSettings():
    mSecondsInBackgroundForceDisconnectOnAndroid: (U32, 0x0, 0x0, 0x0)
    mSecondsInBackgroundForceDisconnectOnIos: (U32, 0x0, 0x0, 0x0)
    mSecondsInBackgroundForceTerminateOnAndroid: (U32, 0x0, 0x0, 0x0)
    pass

class TftCutscenePositionProvider():
    pass

class ContextualConditionNeutralMinionCampName(IContextualCondition):
    mCampName: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionIsSelf(ICharacterSubcondition):
    IsSelf: (Bool, 0x0, 0x0, 0x0)
    pass

class CastOnMovementComplete(MissileBehaviorSpec):
    RollForCriticalHitResult: (Bool, 0x0, 0x0, 0x0)
    pass

class FxActionSfxBeamInstance(IFxActionInstance):
    pass

class ContextualConditionTimeSinceStealthStateChange(IContextualCondition):
    mCompareOp: (U8, 0x0, 0x0, 0x0)
    mStateToCheck: (U8, 0x0, 0x0, 0x0)
    mTimeThreshold: (F32, 0x0, 0x0, 0x0)
    pass

class FxPhase():
    Type: (U32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    DefaultDuration: (F32, 0x0, 0x0, 0x0)
    pass

class VectorTableGet(RsTableGet, ScriptTableGet, TableGet, IVectorGet):
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Var: (Hash, 0x0, 0x0, 0x0)
    Var: (String, 0x0, 0x0, 0x0)
    Default: (Option, 0x0, Vec3, 0x0)
    pass

class ScoreboardUiData():
    OverlayScene: (Hash, 0x0, 0x0, 0x0)
    Team2AllyGlow: (Hash, 0x0, 0x0, 0x0)
    MainTooltipAnchor: (Hash, 0x0, 0x0, 0x0)
    Team2SwapHoverIcon: (Hash, 0x0, 0x0, 0x0)
    Team1SwapHoverIcon: (Hash, 0x0, 0x0, 0x0)
    ScoreboardScene: (Hash, 0x0, 0x0, 0x0)
    ChaosScoreLineUiData: (Pointer, 0x0, 0x0, ScoreLineBaseUiData)
    DragOverlayScene: (Hash, 0x0, 0x0, 0x0)
    Team1AllyGlow: (Hash, 0x0, 0x0, 0x0)
    ChaosObjectiveBountiesData: (Pointer, 0x0, 0x0, SbObjectiveBounties)
    OrderObjectiveBountiesData: (Pointer, 0x0, 0x0, SbObjectiveBounties)
    Team1EnemyGlow: (Hash, 0x0, 0x0, 0x0)
    OrderScoreLineUiData: (Pointer, 0x0, 0x0, ScoreLineBaseUiData)
    ChaosTeamIdentity: (Pointer, 0x0, 0x0, UiTeamIdentityData)
    TeamScoresDefinitions: (Pointer, 0x0, 0x0, ScoreboardTeamScoresDefinitions)
    Team1SwapDragTarget: (Hash, 0x0, 0x0, 0x0)
    SummonerSocialCard: (Pointer, 0x0, 0x0, UiSummonerSocialCardData)
    Team2EnemyGlow: (Hash, 0x0, 0x0, 0x0)
    Team2SwapDragTarget: (Hash, 0x0, 0x0, 0x0)
    OrderTeamIdentity: (Pointer, 0x0, 0x0, UiTeamIdentityData)
    PlayerSlotHeightReference: (Hash, 0x0, 0x0, 0x0)
    pass

class PfxFieldOrbitalDefinitionData():
    IsLocalSpace: (Bool, 0x0, 0x0, 0x0)
    Direction: (Embed, 0x0, 0x0, PfxAnimatedVector3fVariableData)
    pass

class 0x9e1e8775(0xbc413e21):
    LocalizedTextFormat: (String, 0x0, 0x0, 0x0)
    TextFormat: (String, 0x0, 0x0, 0x0)
    TextElement: (Hash, 0x0, 0x0, 0x0)
    pass

class TftMapCharacterSkinData():
    SquareIconTexturePath: (Option, 0x0, String, 0x0)
    SquareIconTexturePath: (String, 0x0, 0x0, 0x0)
    pass

class TftArmoryViewController(ViewController):
    HoverTooltipOffsetAboveTitle: (U32, 0x0, 0x0, 0x0)
    TimerText: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    TimerFillTexture: (Hash, 0x0, 0x0, 0x0)
    ArmoryStyle: (U8, 0x0, 0x0, 0x0)
    HasTimerBar: (Bool, 0x0, 0x0, 0x0)
    ArmoryActionButtons: (Map, U8, Embed, TftArmoryActionButtonData)
    CurrentGoldText: (Hash, 0x0, 0x0, 0x0)
    FullDescriptionTraKey: (String, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    RefreshCountText: (Hash, 0x0, 0x0, 0x0)
    TimeoutDoubleClickPrevention: (F32, 0x0, 0x0, 0x0)
    MaxItemSlot: (U32, 0x0, 0x0, 0x0)
    GoldScene: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    PreArmoryVfx: (Hash, 0x0, 0x0, 0x0)
    TimeoutPreventClicksOnShow: (F32, 0x0, 0x0, 0x0)
    HideButtonScene: (Hash, 0x0, 0x0, 0x0)
    RefreshCost: (I32, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    RadiantItemTag: (String, 0x0, 0x0, 0x0)
    TimerElementGroup: (Hash, 0x0, 0x0, 0x0)
    RefreshButton: (Hash, 0x0, 0x0, 0x0)
    RecipeHintTraKey: (String, 0x0, 0x0, 0x0)
    TimeoutVfxOnToggleButton: (Hash, 0x0, 0x0, 0x0)
    TimerBarBackground: (Hash, 0x0, 0x0, 0x0)
    CurrentGoldIcon: (Hash, 0x0, 0x0, 0x0)
    UseToggleButtonOnPc: (Bool, 0x0, 0x0, 0x0)
    BadgeDisplayProperty: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideBinName: (String, 0x0, 0x0, 0x0)
    ClickShowRecipeHintTraKey: (String, 0x0, 0x0, 0x0)
    ToggleMainViewButton: (Hash, 0x0, 0x0, 0x0)
    CanSellDuringArmory: (Bool, 0x0, 0x0, 0x0)
    ShouldHideButtonsOnChoice: (Bool, 0x0, 0x0, 0x0)
    RefreshTextColor: (Color, 0x0, 0x0, 0x0)
    AllowSingleItemSelection: (Bool, 0x0, 0x0, 0x0)
    TimeoutVfxDuration: (F32, 0x0, 0x0, 0x0)
    StyleOverrides: (Map, U8, Embed, TftArmoryStyleData)
    ItemSpace: (Hash, 0x0, 0x0, 0x0)
    RefreshTextDisabledColor: (Color, 0x0, 0x0, 0x0)
    RefreshCostText: (Hash, 0x0, 0x0, 0x0)
    SellAreas: (List, 0x0, Embed, TftSellArea)
    BaseBinName: (String, 0x0, 0x0, 0x0)
    ItemSlotData: (Embed, 0x0, 0x0, TftArmorySlotData)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    ShadowItemTag: (String, 0x0, 0x0, 0x0)
    SelectAllButton: (Hash, 0x0, 0x0, 0x0)
    pass

class StrawberryRoundsViewController(0x856ba9bc):
    TimerText: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    LeftPhaseIcons: (List, 0x3, Embed, 0x43aaf187)
    RoundLabelTra: (String, 0x0, 0x0, 0x0)
    0x3aa6852c: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TimerLeftBar: (Embed, 0x0, 0x0, 0xbe081d2c)
    CurrentPhaseIcon: (Embed, 0x0, 0x0, 0x43aaf187)
    RoundLabel: (Hash, 0x0, 0x0, 0x0)
    RightPhaseIcons: (List, 0x3, Embed, 0x43aaf187)
    TimerTextDefaultColor: (Color, 0x0, 0x0, 0x0)
    0xb03d7e4b: (Color, 0x0, 0x0, 0x0)
    0xb1f34e3f: (Embed, 0x0, 0x0, 0x45f140fc)
    TimerRightBar: (Embed, 0x0, 0x0, 0xbe081d2c)
    0xcf3fe190: (Hash, 0x0, 0x0, 0x0)
    0xd24a0877: (Map, U8, String, 0x0)
    0xe527f39d: (Hash, 0x0, 0x0, 0x0)
    TooltipAnchor: (Hash, 0x0, 0x0, 0x0)
    pass

class ObjectAttacher(GameObject):
    pass

class 0x9e380c11():
    ChallengeDesc: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    0x67e8e819: (Hash, 0x0, 0x0, 0x0)
    ChallengeName: (Hash, 0x0, 0x0, 0x0)
    ChallengeTokenIcon: (Hash, 0x0, 0x0, 0x0)
    ChallengeLevel: (Hash, 0x0, 0x0, 0x0)
    pass

class UiElementI():
    pass

class 0x9e53d5cf(TargetingTypeData):
    pass

class PerLocaleTooltipAdjustments():
    TopHrYPostAdjustment: (I32, 0x0, 0x0, 0x0)
    BottomYPaddingAdjustment: (I32, 0x0, 0x0, 0x0)
    TitleYAdjustment: (I32, 0x0, 0x0, 0x0)
    TopHrYPreAdjustment: (I32, 0x0, 0x0, 0x0)
    BottomHrYPreAdjustment: (I32, 0x0, 0x0, 0x0)
    BottomHrYPostAdjustment: (I32, 0x0, 0x0, 0x0)
    pass

class TftCutsceneInputClip(TftCutsceneClip):
    DisablePingRadialMenu: (Bool, 0x0, 0x0, 0x0)
    DisableEmoteRadialMenu: (Bool, 0x0, 0x0, 0x0)
    DisableClickInput: (Bool, 0x0, 0x0, 0x0)
    BlackboardPlayers: (List2, 0x0, String, 0x0)
    DisableTftInput: (Bool, 0x0, 0x0, 0x0)
    pass

class HighlighterViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    AdditionalLevelUpLinks: (List, 0x0, Hash, 0x0)
    LevelUpLinks: (List, 0x4, Hash, 0x0)
    SummonerSpellLinks: (List, 0x2, Hash, 0x0)
    SceneLink: (Hash, 0x0, 0x0, 0x0)
    AbilityPrompts: (List, 0x4, Embed, AbilityPrompt)
    AbilityPromptAnimData: (Embed, 0x0, 0x0, UiAbilityPromptAnimData)
    Links: (List, 0xb, Hash, 0x0)
    AbilityLinks: (List, 0x4, Hash, 0x0)
    pass

class 0x9eb07cec(IEnvironmentShadingModel):
    pass

class 0x9eba3f83(0x65a1bb16):
    DurationDriver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class 0x9ec23f4d(ConditionBoolClipData):
    BuffName: (Hash, 0x0, 0x0, 0x0)
    pass

class IRsCondition():
    pass

class 0x9eeb82e6(MissileBehaviorSpec):
    ScanWidthOverride: (Option, 0x0, F32, 0x0)
    mTargeterDefinition: (Pointer, 0x0, 0x0, TargeterDefinitionSkipTerrain)
    mMaximumTerrainWallsToSkip: (Option, 0x0, U32, 0x0)
    pass

class MapPlaceableBase():
    Transform: (Mtx44, 0x0, 0x0, 0x0)
    pass

class ScriptBtSequence(IScriptBt, IScriptSequence):
    Blocks: (List2, 0x0, Pointer, IScriptBlock)
    Blocks: (List2, 0x0, Pointer, IBehaviorScriptBlock)
    pass

class NumberCalculationPart(IGameCalculationPart, ISpellCalculationPart):
    mNumber: (F32, 0x0, 0x0, 0x0)
    pass

class 0x9f30b8a6(IGameModeConfig):
    ObjectiveBountyConfig: (Pointer, 0x0, 0x0, 0xe6f0047)
    0x10bf9ca9: (F32, 0x0, 0x0, 0x0)
    0x11f10a40: (U32, 0x0, 0x0, 0x0)
    0x1eacb90a: (F32, 0x0, 0x0, 0x0)
    BaseGold: (U32, 0x0, 0x0, 0x0)
    0x561b796d: (U32, 0x0, 0x0, 0x0)
    FirstBloodBonus: (U32, 0x0, 0x0, 0x0)
    0x8c1b120: (F32, 0x0, 0x0, 0x0)
    0x907442e7: (U32, 0x0, 0x0, 0x0)
    0x937cc95a: (U32, 0x0, 0x0, 0x0)
    0xa966473c: (Pointer, 0x0, 0x0, 0xb53e2f1a)
    NegativeBountyConfig: (Pointer, 0x0, 0x0, 0x24e1cb45)
    AssistDurationOverride: (U32, 0x0, 0x0, 0x0)
    0xf3518902: (Pointer, 0x0, 0x0, 0xf01e253c)
    0xfe1b406e: (U32, 0x0, 0x0, 0x0)
    pass

class BuildingCommon(AttackableUnit):
    pass

class StoreCategoryPageData():
    mName: (String, 0x0, 0x0, 0x0)
    mEnabled: (Bool, 0x0, 0x0, 0x0)
    mOrder: (U8, 0x0, 0x0, 0x0)
    mInventoryFilters: (List, 0x0, Embed, StoreCategoryInventoryFilter)
    pass

class ISpellCalculationPartWithBuffCounter(ISpellCalculationPart):
    mBuffName: (Hash, 0x0, 0x0, 0x0)
    mIconKey: (String, 0x0, 0x0, 0x0)
    mScalingTagKey: (String, 0x0, 0x0, 0x0)
    pass

class TftCutsceneCinematicBarsClip(TftCutsceneClip):
    EnableLetterBox: (Bool, 0x0, 0x0, 0x0)
    PillarBoxRatio: (F32, 0x0, 0x0, 0x0)
    LetterBoxViewRatio: (F32, 0x0, 0x0, 0x0)
    EnablePillarBox: (Bool, 0x0, 0x0, 0x0)
    PillarBoxViewAspectRatio: (F32, 0x0, 0x0, 0x0)
    RatioType: (U32, 0x0, 0x0, 0x0)
    BlackboardAssociatedPlayers: (List2, 0x0, String, 0x0)
    LetterBoxRatio: (F32, 0x0, 0x0, 0x0)
    pass

class TftMatchupBannerViewController(ViewController):
    RoundText: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    BannerVfx: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    0x5d768e72: (Hash, 0x0, 0x0, 0x0)
    TotalDuration: (F32, 0x0, 0x0, 0x0)
    BannerDurationSecs: (F32, 0x0, 0x0, 0x0)
    0x6e9023c0: (List2, 0x0, String, 0x0)
    LeftPlayer: (Embed, 0x0, 0x0, TftMatchupBannerUiContainer)
    RightPlayer: (Embed, 0x0, 0x0, TftMatchupBannerUiContainer)
    RoundNumber: (Hash, 0x0, 0x0, 0x0)
    BannerVfxEnableTime: (F32, 0x0, 0x0, 0x0)
    pass

class UnitStatusIndicator():
    mOffset: (Vec2, 0x0, 0x0, 0x0)
    mTemplate: (Link, 0x0, 0x0, UnitStatusTemplate)
    mBarOffset: (Vec2, 0x0, 0x0, 0x0)
    pass

class IntArrayTableSet(ScriptTableSet):
    pass

class CustomTableGet(ScriptTableGet, IScriptValueGet):
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Var: (Hash, 0x0, 0x0, 0x0)
    pass

class FxActionSfxBase(IFxAction):
    EventName: (String, 0x0, 0x0, 0x0)
    AudioSource: (Embed, 0x0, 0x0, FxTarget)
    AudioSource: (Embed, 0x0, 0x0, FxObjectSelector)
    UseCharacterTags: (Bool, 0x0, 0x0, 0x0)
    ForceStopWhenDone: (Bool, 0x0, 0x0, 0x0)
    pass

class 0x9fefb5c0(IGameModeConfig):
    0xbece8da6: (String, 0x0, 0x0, 0x0)
    pass

class IsRangedParametricUpdater(IBooleanParametricUpdater):
    pass

class SurrenderData():
    mTypeData: (Map, U8, Embed, SurrenderTypeData)
    0x3afeacf3: (F32, 0x0, 0x0, 0x0)
    mTimeDelayAfterSurrenderMessage: (F32, 0x0, 0x0, 0x0)
    0x4987e889: (F32, 0x0, 0x0, 0x0)
    TimeInactiveForEarlySurrenderSecs: (F32, 0x0, 0x0, 0x0)
    mMinAfkTimeForNoVote: (F32, 0x0, 0x0, 0x0)
    0xd9d17df4: (F32, 0x0, 0x0, 0x0)
    FountainDetectionDurationSecs: (F32, 0x0, 0x0, 0x0)
    mMinTimeBetweenSurrenders: (F32, 0x0, 0x0, 0x0)
    pass

class GroupRepeat():
    Count: (I32, 0x0, 0x0, 0x0)
    Scope: (I32, 0x0, 0x0, 0x0)
    Multiplier: (F32, 0x0, 0x0, 0x0)
    pass

class 0xa05a9472(IFxAction):
    ArmLength: (F32, 0x0, 0x0, 0x0)
    Follow: (Bool, 0x0, 0x0, 0x0)
    Yaw: (F32, 0x0, 0x0, 0x0)
    ZoomEase: (U32, 0x0, 0x0, 0x0)
    ZoomEase: (U8, 0x0, 0x0, 0x0)
    Position: (Embed, 0x0, 0x0, FxTransform)
    Fov: (F32, 0x0, 0x0, 0x0)
    Pitch: (F32, 0x0, 0x0, 0x0)
    Location: (Pointer, 0x0, 0x0, IFxLocation)
    pass

class HudItemShopData():
    BuildsIntoDroplistItemHoverDefinition: (Hash, 0x0, 0x0, 0x0)
    BuildsIntoDroplistBackdropDefinition: (Hash, 0x0, 0x0, 0x0)
    InventoryPanelDefinition: (Embed, 0x0, 0x0, HudItemShopExpandingPanelDefinition)
    SearchBlockMain: (Hash, 0x0, 0x0, 0x0)
    PurchaseButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    AttackItemsFilterButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    SearchInputEditDisabledText: (Hash, 0x0, 0x0, 0x0)
    BuildTreeIconDefinition: (Hash, 0x0, 0x0, 0x0)
    ItemShopSellOverlaySellItemTextDefinition: (Hash, 0x0, 0x0, 0x0)
    CloseButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    ItemShopSellOverlayScene: (Hash, 0x0, 0x0, 0x0)
    CommonlyBuiltIconDefinition: (Hash, 0x0, 0x0, 0x0)
    PlayerDebtText: (Hash, 0x0, 0x0, 0x0)
    TabViewItemSetsScene: (Hash, 0x0, 0x0, 0x0)
    TabButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    SearchItemDescriptionDefinition: (Embed, 0x0, 0x0, HudItemShopItemDetailsDefinition)
    SearchIconDefinition: (Hash, 0x0, 0x0, 0x0)
    UndoButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    BuildsIntoSlotDefinition: (List, 0x7, Hash, 0x0)
    ItemDescriptionDefinition: (Embed, 0x0, 0x0, HudItemShopItemDetailsDefinition)
    BuildsIntoIconDefinition: (Hash, 0x0, 0x0, 0x0)
    0x46f45f7f: (Bool, 0x0, 0x0, 0x0)
    ItemSetsHeaderText: (Hash, 0x0, 0x0, 0x0)
    TileItemIconDefinition: (Hash, 0x0, 0x0, 0x0)
    ItemDetailsSceneViewPane: (Hash, 0x0, 0x0, 0x0)
    ItemShopSearchViewItemRegionDefinition: (Hash, 0x0, 0x0, 0x0)
    SellButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    RecItemCardDefinition: (Hash, 0x0, 0x0, 0x0)
    ItemSetsIconDefinition: (Hash, 0x0, 0x0, 0x0)
    BuildTreeDisplayRegionDefinition: (Hash, 0x0, 0x0, 0x0)
    BuildsIntoOverflowButton: (Hash, 0x0, 0x0, 0x0)
    QuickBuyIconDefinition: (Hash, 0x0, 0x0, 0x0)
    AllItemsIconDefinition: (Hash, 0x0, 0x0, 0x0)
    MagicalItemsFilterButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    InventoryIconDefinition: (Hash, 0x0, 0x0, 0x0)
    HorizontalBuildTreeConnector: (Hash, 0x0, 0x0, 0x0)
    SearchClearTextIcon: (Hash, 0x0, 0x0, 0x0)
    DefenseItemsFilterButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    ItemDetailsScene: (Hash, 0x0, 0x0, 0x0)
    ShowAllItemsFilterButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    PlayerGoldIcon: (Hash, 0x0, 0x0, 0x0)
    0x71d17542: (Embed, 0x0, 0x0, ViewPaneDefinition)
    StatFilterButtonDefinitions: (Hash, 0x0, 0x0, 0x0)
    AllItemGroupDefinitions: (List, 0x0, Embed, HudItemShopItemGroupDefinition)
    BuildTreeTopIconScale: (F32, 0x0, 0x0, 0x0)
    BuildsIntoTextOverflowScale: (F32, 0x0, 0x0, 0x0)
    0x816bfca7: (Bool, 0x0, 0x0, 0x0)
    ItemSetsItemRegion: (Hash, 0x0, 0x0, 0x0)
    TabViewRecItemsSceneViewPane: (Hash, 0x0, 0x0, 0x0)
    0x832e9544: (Bool, 0x0, 0x0, 0x0)
    BuildsIntoDroplistScene: (Hash, 0x0, 0x0, 0x0)
    SearchInputEdit: (Hash, 0x0, 0x0, 0x0)
    0x92f0d709: (Bool, 0x0, 0x0, 0x0)
    TabViewItemSetsSceneViewPane: (Hash, 0x0, 0x0, 0x0)
    ItemShopSellOverlaySellIconDefaultDefinition: (Hash, 0x0, 0x0, 0x0)
    RecItemSlotsDefinition: (List, 0x3, Hash, 0x0)
    Scaling: (Embed, 0x0, 0x0, 0x86baa4d)
    TabViewAllItemsScene: (Hash, 0x0, 0x0, 0x0)
    InvertGroupDisplayOrderButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    0xa8ca51f6: (List2, 0x0, Hash, 0x0)
    MarksmanItemsFilterButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    ItemSetsComboBoxDefinition: (Hash, 0x0, 0x0, 0x0)
    ItemShopSearchSceneViewPane: (Hash, 0x0, 0x0, 0x0)
    BundleItemPurchaseButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    BundleItemListRegionDefinition: (Hash, 0x0, 0x0, 0x0)
    TabViewAllItemsSceneViewPane: (Hash, 0x0, 0x0, 0x0)
    0xb3e9d346: (Embed, 0x0, 0x0, ViewPaneDefinition)
    AllItemsItemRegion: (Hash, 0x0, 0x0, 0x0)
    PageTemplateItemIconDefinition: (Hash, 0x0, 0x0, 0x0)
    ItemShopSellOverlayDragAreaDefinition: (Hash, 0x0, 0x0, 0x0)
    QuickbuyConsumablesData: (Embed, 0x0, 0x0, HudItemShopQuickBuyData)
    QuickbuyBootsData: (Embed, 0x0, 0x0, HudItemShopQuickBuyData)
    SearchViewPaneDefinition: (Embed, 0x0, 0x0, ViewPaneDefinition)
    0xcccb5e11: (Bool, 0x0, 0x0, 0x0)
    0xce14c25: (Embed, 0x0, 0x0, ViewPaneDefinition)
    PopularItemsFilterButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    SearchEnableArea: (Hash, 0x0, 0x0, 0x0)
    ItemShopSearchViewRecLabelDefinition: (Hash, 0x0, 0x0, 0x0)
    BundlePostfixTraKey: (String, 0x0, 0x0, 0x0)
    RecItemCommonlyBuiltSlotDefinition: (List, 0x9, Hash, 0x0)
    AllItemsHeaderText: (Hash, 0x0, 0x0, 0x0)
    AssassinItemsFilterButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    DefaultPotion: (List, 0x6, Hash, 0x0)
    ItemSetsHeaderRegion: (Hash, 0x0, 0x0, 0x0)
    BootsPanelDefinition: (Embed, 0x0, 0x0, HudItemShopExpandingPanelDefinition)
    PlayerGoldText: (Hash, 0x0, 0x0, 0x0)
    ConsumablesPanelDefinition: (Embed, 0x0, 0x0, HudItemShopExpandingPanelDefinition)
    UtilityItemsFilterButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    AllItemsHeaderTextDimmed: (Hash, 0x0, 0x0, 0x0)
    ItemIconTemplateScene: (Hash, 0x0, 0x0, 0x0)
    AllItemsHeaderRegion: (Hash, 0x0, 0x0, 0x0)
    ItemShopSearchViewScene: (Hash, 0x0, 0x0, 0x0)
    RecItemCardTagScale: (F32, 0x0, 0x0, 0x0)
    VerticalBuildTreeConnector: (Hash, 0x0, 0x0, 0x0)
    ItemShopSellOverlaySellIconHoverDefinition: (Hash, 0x0, 0x0, 0x0)
    TabViewRecItemsScene: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xa0b62126(MapAction):
    Duration: (F32, 0x0, 0x0, 0x0)
    TargetColor: (Color, 0x0, 0x0, 0x0)
    TargetLightingVolume: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xa0c66b29(0x64c18f7d):
    pass

class TftMapSetData():
    AugmentContainerName: (String, 0x0, 0x0, 0x0)
    ItemLists: (List, 0x0, Pointer, TftMapItemList)
    DisplayName: (String, 0x0, 0x0, 0x0)
    CharacterLists: (List, 0x0, Pointer, TftMapCharacterList)
    CoreName: (String, 0x0, 0x0, 0x0)
    TraitUnitProperties: (List2, 0x0, String, 0x0)
    0x9fd292f5: (String, 0x0, 0x0, 0x0)
    TftGameType: (U32, 0x0, 0x0, 0x0)
    ItemUnitProperties: (List2, 0x0, String, 0x0)
    AugmentContainerTexture: (String, 0x0, 0x0, 0x0)
    ObjectName: (String, 0x0, 0x0, 0x0)
    TraitLists: (List, 0x0, Pointer, TftMapTraitList)
    pass

class 0xa0d8d1a6(IScriptBlock):
    Dest: (Embed, 0x0, 0x0, IntTableSet)
    pass

class ContextualConditionNeutralMinionCampIsAlive(IContextualCondition):
    mCampIsAlive: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xa0f3252e(IFxActionInstance):
    pass

class OrInputSourceBool(IInputSourceBool):
    Sources: (List2, 0x0, Pointer, IInputSourceBool)
    pass

class ViewControllerFilter_And(ViewControllerFilterI):
    FilterList: (List2, 0x0, Pointer, ViewControllerFilterI)
    Filters: (List, 0x0, Pointer, ViewControllerFilterI)
    Filters: (List2, 0x0, Pointer, ViewControllerFilterI)
    pass

class VfxPrimitiveRay(VfxPrimitiveBase):
    pass

class ScriptPreloadSpell():
    PreloadResourceName: (String, 0x0, 0x0, 0x0)
    pass

class HudLoadingScreenWidgetCarousel(IHudLoadingScreenWidget):
    mCarouselData: (Link, 0x0, 0x0, HudLoadingScreenCarouselData)
    0x7b1f4fc8: (U8, 0x0, 0x0, 0x0)
    pass

class GameModeConstantString(GameModeConstant):
    mValue: (String, 0x0, 0x0, 0x0)
    pass

class TftTooltipList():
    Tooltips: (List2, 0x0, Link, TftTooltipData)
    pass

class 0xa19405b3(ILolSpellScriptEvent):
    pass

class ContextualConditionCharacterUnitTags(ICharacterSubcondition):
    mUnitTags: (Embed, 0x0, 0x0, ObjectTags)
    mTagMode: (U8, 0x0, 0x0, 0x0)
    pass

class MinimapBackground():
    mSize: (Vec2, 0x0, 0x0, 0x0)
    mOrigin: (Vec2, 0x0, 0x0, 0x0)
    mTextureName: (String, 0x0, 0x0, 0x0)
    pass

class DoubleSidedTipStyle(TipStyleBase):
    ReverseDirectionalTipElements: (List, 0x0, Link, ElementDataI)
    ReverseDirectionalTipElements: (List, 0x0, Link, UiElementIData)
    ReverseDirectionalTipElements: (List2, 0x0, Link, UiElementIData)
    Sliver: (Link, 0x0, 0x0, ElementDataI)
    Sliver: (Link, 0x0, 0x0, UiElementIData)
    pass

class ListenerConstraintInfo():
    pass

class ElementGroupSliderState():
    BarBackdrop: (Link, 0x0, 0x0, IconElementData)
    BarFill: (Link, 0x0, 0x0, IconElementData)
    SliderIcon: (Link, 0x0, 0x0, IconElementData)
    pass

class MaterialInstanceSwitchDef():
    On: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xa2223aee(IOptionItemFilter):
    pass

class TextInfoNubData(InfoNubData):
    BodyKey: (String, 0x0, 0x0, 0x0)
    TitleKey: (String, 0x0, 0x0, 0x0)
    pass

class ItemGrid():
    mSections: (List, 0x0, Embed, ItemGridSection)
    mLabel: (String, 0x0, 0x0, 0x0)
    pass

class 0xa24429bf():
    StartFrame: (I32, 0x0, 0x0, 0x0)
    pass

class ItemGridRow():
    mItems: (List, 0x0, Hash, 0x0)
    mItems: (List, 0xd, Hash, 0x0)
    mItems: (List, 0xd, Link, ItemData)
    pass

class SecondaryResourceDisplayFractional(ISecondaryResourceDisplayData):
    pass

class LolModesRoundData():
    Phases: (List, 0x0, Link, LolModesPhaseData)
    pass

class ItemRecommendationMatrixRow():
    mChoicesMap: (Map, String, Embed, ItemRecommendationChoices)
    pass

class CherryTeamFlyoutPanelTeamTemplate():
    Scene: (Hash, 0x0, 0x0, 0x0)
    HoverGlow: (Embed, 0x0, 0x0, 0xcc2c0827)
    FightTeamFrame: (Embed, 0x0, 0x0, CherryTeamFlyoutPanelFightTeamFrame)
    HealthTextScene: (Hash, 0x0, 0x0, 0x0)
    FightTeamBackground: (Embed, 0x0, 0x0, IconStateData)
    0x337254f3: (Embed, 0x0, 0x0, IconStateData)
    TeamButton: (Hash, 0x0, 0x0, 0x0)
    Bounds: (Hash, 0x0, 0x0, 0x0)
    0x4ea12677: (Embed, 0x0, 0x0, IconStateData)
    ChampionLayout: (Hash, 0x0, 0x0, 0x0)
    0x5388a5b: (Hash, 0x0, 0x0, 0x0)
    TeamChampionsButton: (Hash, 0x0, 0x0, 0x0)
    DefaultFillMeterColor: (Color, 0x0, 0x0, 0x0)
    Player1: (Embed, 0x0, 0x0, CherryTeamFlyoutPanelTeamTemplateChampion)
    Player2: (Embed, 0x0, 0x0, CherryTeamFlyoutPanelTeamTemplateChampion)
    LastLifeHealthTextColor: (Color, 0x0, 0x0, 0x0)
    HealthText: (Hash, 0x0, 0x0, 0x0)
    TeamIcon: (Hash, 0x0, 0x0, 0x0)
    Frames: (Embed, 0x0, 0x0, CherryTeamFlyoutPanelTeamFrame)
    ChampionTemplate: (Embed, 0x0, 0x0, CherryTeamFlyoutPanelTeamTemplateChampion)
    DefaultHealthTextColor: (Color, 0x0, 0x0, 0x0)
    FillMeter: (Hash, 0x0, 0x0, 0x0)
    0xa4577e5a: (Embed, 0x0, 0x0, 0x6a68b4f1)
    0xd4fa36ff: (Hash, 0x0, 0x0, 0x0)
    ChampionScene: (Hash, 0x0, 0x0, 0x0)
    LastLifeFillMeterColor: (Color, 0x0, 0x0, 0x0)
    pass

class BoolTableSet(RsTableSet, ScriptTableSet):
    pass

class SummonerBadgeList():
    SummonerBadges: (List, 0x0, Embed, SummonerBadgeData)
    pass

class VoiceChatViewSelfSlot():
    ConnectionButton: (Hash, 0x0, 0x0, 0x0)
    MicVolumeSliderBar: (Hash, 0x0, 0x0, 0x0)
    MicVolumeText: (Hash, 0x0, 0x0, 0x0)
    Portrait: (Hash, 0x0, 0x0, 0x0)
    Halo: (Hash, 0x0, 0x0, 0x0)
    NameText: (Hash, 0x0, 0x0, 0x0)
    MuteButton: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionCharacter(IContextualCondition):
    mChildConditions: (List, 0x0, Pointer, ICharacterSubcondition)
    mCharacterType: (U8, 0x0, 0x0, 0x0)
    pass

class MapActionAttachMapParticle(MapAction):
    Duration: (F32, 0x0, 0x0, 0x0)
    MapParticle: (String, 0x0, 0x0, 0x0)
    0x7df5733d: (Pointer, 0x0, 0x0, 0xc9440657)
    pass

class TftMapSkin(BaseLoadoutData):
    Disabled: (Bool, 0x0, 0x0, 0x0)
    BankUnitList: (Hash, 0x0, 0x0, 0x0)
    AudioBankPaths: (List, 0x0, String, 0x0)
    StandaloneLoadoutsIcon: (String, 0x0, 0x0, 0x0)
    Rarity: (U32, 0x0, 0x0, 0x0)
    GoldMineSkinId: (U32, 0x0, 0x0, 0x0)
    AwayGoldMineSkinId: (U16, 0x0, 0x0, 0x0)
    StandaloneLoadoutIcon: (String, 0x0, 0x0, 0x0)
    TrovesHighlightVfx: (Hash, 0x0, 0x0, 0x0)
    ArenaIntroCutscene: (Pointer, 0x0, 0x0, TftCutscene)
    0x8e2a4357: (Hash, 0x0, 0x0, 0x0)
    Characters: (List2, 0x0, Hash, 0x0)
    HomeGoldMineSkinId: (U16, 0x0, 0x0, 0x0)
    MapContainer: (String, 0x0, 0x0, 0x0)
    ResourceResolver: (Hash, 0x0, 0x0, 0x0)
    StandaloneLoadoutsLargeIcon: (String, 0x0, 0x0, 0x0)
    ArenaTransformCutscene: (Pointer, 0x0, 0x0, TftCutscene)
    GroupLink: (String, 0x0, 0x0, 0x0)
    RotationalShopItemData: (Embed, 0x0, 0x0, TftRotationalShopItemData)
    pass

class Mapgeo():
    Items: (Map, Hash, Pointer, MapPlaceable)
    UseEnvironmentBloom: (Bool, 0x0, 0x0, 0x0)
    LowestProjectableHeight: (F32, 0x0, 0x0, 0x0)
    SurfaceAreaToShadowMapScale: (F32, 0x0, 0x0, 0x0)
    BoundsMin: (Vec2, 0x0, 0x0, 0x0)
    BoundsMax: (Vec2, 0x0, 0x0, 0x0)
    Sun: (Embed, 0x0, 0x0, MapSunProperties)
    pass

class HudBannerData():
    PulseInterval: (F32, 0x0, 0x0, 0x0)
    TransitionTime: (F32, 0x0, 0x0, 0x0)
    PulseTime: (F32, 0x0, 0x0, 0x0)
    TransitionMinAlpha: (U8, 0x0, 0x0, 0x0)
    TransitionOffset: (Vec2, 0x0, 0x0, 0x0)
    TransitionMaxAlpha: (U8, 0x0, 0x0, 0x0)
    PulseDuration: (F32, 0x0, 0x0, 0x0)
    PulseOffset: (Vec2, 0x0, 0x0, 0x0)
    pass

class CommonUiTunables():
    mHudViewPaneInertiaTime: (F32, 0x0, 0x0, 0x0)
    mHudViewPaneInertiaEasing: (U32, 0x0, 0x0, 0x0)
    mHudViewPaneInertiaEasing: (U8, 0x0, 0x0, 0x0)
    pass

class TftDamageFxContainer():
    TargetFxKey: (Hash, 0x0, 0x0, 0x0)
    BoomFxTable: (Hash, 0x0, 0x0, 0x0)
    SourceFxKey: (Hash, 0x0, 0x0, 0x0)
    pass

class FxActionTimeDilate(IFxAction):
    Intime: (F32, 0x0, 0x0, 0x0)
    TimeDilation: (F32, 0x0, 0x0, 0x0)
    InEase: (U32, 0x0, 0x0, 0x0)
    InEase: (U8, 0x0, 0x0, 0x0)
    OutEase: (U32, 0x0, 0x0, 0x0)
    OutEase: (U8, 0x0, 0x0, 0x0)
    OutTime: (F32, 0x0, 0x0, 0x0)
    pass

class TftOptionsViewController(OptionsViewController):
    FooterScene: (Hash, 0x0, 0x0, 0x0)
    ActiveTabWithFooterScrollRegion: (Hash, 0x0, 0x0, 0x0)
    ActiveTabScrollRegion: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    BuildVersionText: (Hash, 0x0, 0x0, 0x0)
    BuildVersionTextFooter: (Hash, 0x0, 0x0, 0x0)
    0xd2dfde63: (Bool, 0x0, 0x0, 0x0)
    pass

class ElementDataBase():
    Id: (String, 0x0, 0x0, 0x0)
    PreferredOrder: (U8, 0x0, 0x0, 0x0)
    pass

class EffectElementData(UiAssetElementData, IconElementData, BaseElementData, UiElementAssetData):
    mEffectParams0: (Vec4, 0x0, 0x0, 0x0)
    mTexture1: (String, 0x0, 0x0, 0x0)
    mEffectColor0: (Color, 0x0, 0x0, 0x0)
    mEffectColor1: (Color, 0x0, 0x0, 0x0)
    mEffect: (String, 0x0, 0x0, 0x0)
    pass

class WadFileDescriptor():
    AdditionalRoots: (List, 0x0, String, 0x0)
    PackAllDataIntoWadFile: (Bool, 0x0, 0x0, 0x0)
    pass

class UiTeamFightTeamScoreData():
    ScoreUnderlay: (Hash, 0x0, 0x0, 0x0)
    ScoreText: (Hash, 0x0, 0x0, 0x0)
    pass

class TftRotationalShopItemData():
    BackgroundTexturePath: (String, 0x0, 0x0, 0x0)
    LcuBackgroundTexturePath: (String, 0x0, 0x0, 0x0)
    MobileBackgroundTexturePath: (String, 0x0, 0x0, 0x0)
    pass

class BarElementParams():
    mFillColor: (Color, 0x0, 0x0, 0x0)
    mFadeColor: (Color, 0x0, 0x0, 0x0)
    mBarColor: (Color, 0x0, 0x0, 0x0)
    pass

class TriggerOnDistanceFromCaster(MissileTriggerSpec):
    mDistance: (F32, 0x0, 0x0, 0x0)
    pass

class SplineInfo():
    mStartPositionTangent: (Vec3, 0x0, 0x0, 0x0)
    mStartPositionOffset: (Vec3, 0x0, 0x0, 0x0)
    mTargetPositionTangent: (Vec3, 0x0, 0x0, 0x0)
    pass

class AtlasData3SliceV(AtlasDataBase):
    TopBottomHeights: (Vec2, 0x0, 0x0, 0x0)
    TextureUs: (Vec2, 0x0, 0x0, 0x0)
    TextureVs: (Vec4, 0x0, 0x0, 0x0)
    pass

class RetiredStatStoneData():
    StatStoneRetiredIconMiniName: (String, 0x0, 0x0, 0x0)
    pass

class BreakBlock(IScriptBlock):
    pass

class InputEvent2Axis(InputEventBase):
    QuantizationScale: (F32, 0x0, 0x0, 0x0)
    DeadzoneRadius: (F32, 0x0, 0x0, 0x0)
    FireOnReturningToDeadZone: (Bool, 0x0, 0x0, 0x0)
    Normalize: (Bool, 0x0, 0x0, 0x0)
    SourcesY: (List, 0x0, Pointer, IInputSourceFloat)
    SourcesX: (List, 0x0, Pointer, IInputSourceFloat)
    CombineMode: (U32, 0x0, 0x0, 0x0)
    pass

class TftGameStartSequenceSimpleEvent():
    UiElement: (Hash, 0x0, 0x0, 0x0)
    StartTimeSecs: (F32, 0x0, 0x0, 0x0)
    UiObject: (Pointer, 0x0, 0x0, TftGameStartSequenceSimpleObject)
    DurationSecs: (F32, 0x0, 0x0, 0x0)
    pass

class TftCutsceneClip(TftCutsceneEntry):
    Duration: (F32, 0x0, 0x0, 0x0)
    pass

class LoadoutCompanionInfoPanel(ILoadoutInfoPanel):
    UpgradeEntitlementErrorTooltipText: (String, 0x0, 0x0, 0x0)
    JustObtainedIcon: (List, 0x3, Hash, 0x0)
    GamePassIcon: (Hash, 0x0, 0x0, 0x0)
    UnownedStarShardIcon: (List, 0x3, Hash, 0x0)
    UpgradeButtonDisabledFromEntitlementText: (String, 0x0, 0x0, 0x0)
    Tier2ButtonFeedbackVfx: (Hash, 0x0, 0x0, 0x0)
    UnownedTierButton: (List, 0x3, Hash, 0x0)
    UpgradeTierButton: (List, 0x3, Hash, 0x0)
    Tier3ButtonFeedbackVfx: (Hash, 0x0, 0x0, 0x0)
    StarShardCurrencyButton: (Hash, 0x0, 0x0, 0x0)
    RarityIcon: (List, 0x5, Hash, 0x0)
    TierButton: (List, 0x3, Hash, 0x0)
    LockIcon: (List, 0x3, Hash, 0x0)
    UpgradeErrorText: (Hash, 0x0, 0x0, 0x0)
    ItemIconText: (Hash, 0x0, 0x0, 0x0)
    UpgradeEntitlementErrorButton: (Hash, 0x0, 0x0, 0x0)
    ItemIcon: (Hash, 0x0, 0x0, 0x0)
    0xee425ddc: (Hash, 0x0, 0x0, 0x0)
    UpgradeInfoText: (Hash, 0x0, 0x0, 0x0)
    pass

class ItemRecommendationOverrideSet():
    mOverrides: (List, 0x0, Embed, ItemRecommendationOverride)
    pass

class TftMapTraitContributionData():
    TraitData: (Embed, 0x0, 0x0, TftMapTraitData)
    pass

class RegionDataBase():
    Regions: (List2, 0x0, String, 0x0)
    pass

class 0xa431a429(0x69cdddcc):
    Arc: (F32, 0x0, 0x0, 0x0)
    ArcRadius: (F32, 0x0, 0x0, 0x0)
    RotationForward: (Vec3, 0x0, 0x0, 0x0)
    RotationAxis: (Vec3, 0x0, 0x0, 0x0)
    pass

class BankUnit():
    Events: (List, 0x0, String, 0x0)
    BankPath: (List, 0x0, String, 0x0)
    VoiceOver: (Bool, 0x0, 0x0, 0x0)
    BankPath2013: (List, 0x0, String, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    Asynchrone: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xa44b28c0():
    0x42331f2a: (List, 0x2, Embed, TrackerIconSlots)
    0x7ff19d0c: (Hash, 0x0, 0x0, 0x0)
    CenterSlotIcon: (Hash, 0x0, 0x0, 0x0)
    Dragons: (Map, Hash, Embed, 0x2aa61eb4)
    0xfd894807: (Hash, 0x0, 0x0, 0x0)
    pass

class IconStateData():
    IconActiveHover: (Hash, 0x0, 0x0, 0x0)
    0x5786f895: (Hash, 0x0, 0x0, 0x0)
    IconInactiveHover: (Hash, 0x0, 0x0, 0x0)
    0xcf3d6a50: (Hash, 0x0, 0x0, 0x0)
    pass

class SettingsViewController(ViewController):
    SoundOnDeActivate: (String, 0x0, 0x0, 0x0)
    TabButton: (Hash, 0x0, 0x0, 0x0)
    SoundOnActivate: (String, 0x0, 0x0, 0x0)
    CloseButton: (Hash, 0x0, 0x0, 0x0)
    GeneralSettings: (Embed, 0x0, 0x0, GeneralSettingsGroup)
    pass

class CherryTeamFlyoutPanelTeamTemplateChampion():
    PortraitGridItem: (Hash, 0x0, 0x0, 0x0)
    PortraitFrame: (Hash, 0x0, 0x0, 0x0)
    PortraitReference: (Hash, 0x0, 0x0, 0x0)
    PortraitFrames: (Embed, 0x0, 0x0, 0xc7ca4925)
    PortraitIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class LuaPropertyDataBoolean(LuaPropertyData):
    Value: (Bool, 0x0, 0x0, 0x0)
    pass

class TftEventTimer():
    TimerText: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    0x2374a39f: (String, 0x0, 0x0, 0x0)
    0x8938c438: (String, 0x0, 0x0, 0x0)
    0xe1c84837: (Hash, 0x0, 0x0, 0x0)
    TimerIcon: (Hash, 0x0, 0x0, 0x0)
    TimerFrame: (Hash, 0x0, 0x0, 0x0)
    GreyedTimerText: (Hash, 0x0, 0x0, 0x0)
    pass

class ViewControllerFilterI():
    pass

class OptionItemFilter_ReplayApi(IOptionItemFilter):
    pass

class 0xa495afda():
    RecipientChampion: (Hash, 0x0, 0x0, 0x0)
    Spell: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxPrimitiveAttachedMesh(VfxPrimitiveMeshBase):
    UseAvatarSpecificSubmeshMask: (Bool, 0x0, 0x0, 0x0)
    pass

class HudPlayerResourceBars():
    HealthMeter: (Embed, 0x0, 0x0, HealthMeter)
    ParHitRegion: (Hash, 0x0, 0x0, 0x0)
    SarText: (Hash, 0x0, 0x0, 0x0)
    HealthAnimatedMeterSkin: (Embed, 0x0, 0x0, UiElementMeterSkin)
    ParRegenText: (Hash, 0x0, 0x0, 0x0)
    ParMeterData: (Embed, 0x0, 0x0, AbilityResourceBarData)
    HealthHitRegion: (Hash, 0x0, 0x0, 0x0)
    ArThresholdIndicator: (Pointer, 0x0, 0x0, HudAbilityResourceThresholdIndicator)
    HealthRegenText: (Hash, 0x0, 0x0, 0x0)
    ExperienceHitRegion: (Hash, 0x0, 0x0, 0x0)
    ExperienceBar: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xa4cf68bd(LevelScriptLegacyBlock):
    pass

class TooltipInstanceSpell(TooltipInstance):
    0x6386d7d8: (Bool, 0x0, 0x0, 0x0)
    EnableExtendedTooltip: (Bool, 0x0, 0x0, 0x0)
    pass

class PerkScriptData():
    mEffectAmount: (List, 0x0, F32, 0x0)
    mEffectAmount: (Map, Hash, F32, 0x0)
    mEffectAmountGameMode: (Map, Hash, Embed, PerkEffectAmountPerMode)
    mCalculations: (Map, Hash, Pointer, IGameCalculation)
    pass

class Missile(GameObject):
    pass

class LoadingScreenTips():
    TipBodyText: (Hash, 0x0, 0x0, 0x0)
    CondensedTipIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xa50ab26():
    OwnerChampion: (Hash, 0x0, 0x0, 0x0)
    Tooltip: (String, 0x0, 0x0, 0x0)
    pass

class LayoutStyleBase():
    HorizontalJustification: (U8, 0x0, 0x0, 0x0)
    VerticalJustification: (U8, 0x0, 0x0, 0x0)
    pass

class TftAugmentInfoViewController(ViewController):
    Augments: (List, 0x3, Embed, TftAugmentDisplayData)
    Scene: (Hash, 0x0, 0x0, 0x0)
    Slots: (List, 0x0, Embed, TftAugmentDisplayData)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    TitleIcon: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class ExtraJointChainData():
    StartingJointName: (Hash, 0x0, 0x0, 0x0)
    RightBias: (F32, 0x0, 0x0, 0x0)
    EndingJointName: (Hash, 0x0, 0x0, 0x0)
    pass

class MapLaneComponent(MapComponent):
    mLanes: (List, 0x0, Embed, LaneData)
    pass

class StealthData():
    RevealFlags: (Embed, 0x0, 0x0, StealthBreakFlags)
    ExitFlags: (Embed, 0x0, 0x0, StealthBreakFlags)
    CharacterFadeInstance: (Embed, 0x0, 0x0, StealthCharacterFadeInstance)
    Duration: (F32, 0x0, 0x0, 0x0)
    HasVfxPriority: (Bool, 0x0, 0x0, 0x0)
    UnitDetectionRadius: (F32, 0x0, 0x0, 0x0)
    TowerDetectionRadius: (F32, 0x0, 0x0, 0x0)
    StealthName: (String, 0x0, 0x0, 0x0)
    ScreenFade: (Link, 0x0, 0x0, StealthFadeColorEffect)
    PersistentStealthEffect: (Embed, 0x0, 0x0, StealthVfxInstance)
    DetectionEyeEffect: (Embed, 0x0, 0x0, StealthVfxInstance)
    UnitWarningOffSetRadius: (F32, 0x0, 0x0, 0x0)
    Ghosted: (Bool, 0x0, 0x0, 0x0)
    DamageShimmerSfx: (Embed, 0x0, 0x0, StealthVfxInstance)
    HideVfxFromEnemies: (Bool, 0x0, 0x0, 0x0)
    DetectedEffect: (Embed, 0x0, 0x0, StealthVfxInstance)
    ExitStealthEffect: (Embed, 0x0, 0x0, StealthVfxInstance)
    DetectionEyeWarningEffect: (Embed, 0x0, 0x0, StealthVfxInstance)
    DamageShimmerEffect: (Embed, 0x0, 0x0, StealthVfxInstance)
    RevealPriorityEffect: (Embed, 0x0, 0x0, StealthVfxInstance)
    CamoRingEffectOther: (Embed, 0x0, 0x0, StealthVfxInstance)
    EnterStealthEffect: (Embed, 0x0, 0x0, StealthVfxInstance)
    HideHealthBarFromEnemies: (Bool, 0x0, 0x0, 0x0)
    UnSelectableByEnemies: (Bool, 0x0, 0x0, 0x0)
    SelfRevealDuration: (F32, 0x0, 0x0, 0x0)
    UseStealthStatus: (Bool, 0x0, 0x0, 0x0)
    CamoRingEffect: (Embed, 0x0, 0x0, StealthVfxInstance)
    EnemyRevealDuration: (F32, 0x0, 0x0, 0x0)
    HideModelFromEnemies: (Bool, 0x0, 0x0, 0x0)
    RevealEffect: (Embed, 0x0, 0x0, StealthVfxInstance)
    Invisibility: (Bool, 0x0, 0x0, 0x0)
    pass

class GamepadButtonInputSourceBool(IInputSourceBool):
    Button: (U32, 0x0, 0x0, 0x0)
    pass

class UiElementRegionData(UiElementData):
    pass

class ChampionMasteryMap():
    MasteryData: (Map, I32, Link, MasteryData)
    pass

class LoadingScreenPlayerCardClassicSpellData():
    Frame: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class AvatarVars(ScriptTable):
    pass

class ResourceMeterSkinData():
    AdditionalMeterSkins: (Map, Hash, Embed, UiElementMeterSkin)
    DefaultMeterSkin: (Embed, 0x0, 0x0, UiElementMeterSkin)
    pass

class SummonerIconData():
    GameTexture: (String, 0x0, 0x0, 0x0)
    EsportsEventMutator: (String, 0x0, 0x0, 0x0)
    GoldEsportsSupportIcon: (Bool, 0x0, 0x0, 0x0)
    EsportsTeam: (Link, 0x0, 0x0, CollectiblesEsportsTeamData)
    IconId: (U32, 0x0, 0x0, 0x0)
    pass

class 0xa5f064ff():
    RegionPortals: (List2, 0x0, Link, 0xb3f382ff)
    0x48a30fbc: (List, 0x3, String, 0x0)
    pass

class LoadingScreenBasicViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    Version: (Embed, 0x0, 0x0, VersionString)
    Background: (Embed, 0x0, 0x0, LoadingScreenGameModeBackground)
    Tips: (Embed, 0x0, 0x0, LoadingScreenTips)
    VietnameseRatingLabel: (Embed, 0x0, 0x0, UiMetricVietnameseRatingLabel)
    ProgressMeter: (Embed, 0x0, 0x0, LoadingScreenProgressMeter)
    ObjectName: (String, 0x0, 0x0, 0x0)
    Latency: (Embed, 0x0, 0x0, LoadingScreenLatency)
    pass

class EngineFeatureToggles():
    OptimizedDecalProjection: (Bool, 0x0, 0x0, 0x0)
    LoadLuaFilesFromWad: (Bool, 0x0, 0x0, 0x0)
    OptimizedShadowBlur: (Bool, 0x0, 0x0, 0x0)
    0x26bfb812: (Bool, 0x0, 0x0, 0x0)
    0x2dfc4d62: (Bool, 0x0, 0x0, 0x0)
    CapBurstEmitters: (Bool, 0x0, 0x0, 0x0)
    UseCharacterMaterials: (Bool, 0x0, 0x0, 0x0)
    UseParticleMaterials: (Bool, 0x0, 0x0, 0x0)
    0x4ce7f384: (Bool, 0x0, 0x0, 0x0)
    UseMaterialsForCharacterPasses: (Bool, 0x0, 0x0, 0x0)
    UseMaterialsForLegacyMaps: (Bool, 0x0, 0x0, 0x0)
    DeterministicRandom: (Bool, 0x0, 0x0, 0x0)
    UseKeywordsForVfxOwner: (Bool, 0x0, 0x0, 0x0)
    0x5f9a3a3e: (Bool, 0x0, 0x0, 0x0)
    0x5fe6e49: (Bool, 0x0, 0x0, 0x0)
    VfxBrighterInFowAsDisabledFow: (Bool, 0x0, 0x0, 0x0)
    PreferNonDeterministicRandom: (Bool, 0x0, 0x0, 0x0)
    AllowCharacterMaterials: (Bool, 0x0, 0x0, 0x0)
    ScalePlaySpeedNameAnimation: (Bool, 0x0, 0x0, 0x0)
    UseNewParticleVisibilityLogic: (Bool, 0x0, 0x0, 0x0)
    AllowBloom: (Bool, 0x0, 0x0, 0x0)
    0xa0e27e9c: (Bool, 0x0, 0x0, 0x0)
    0xa40d378e: (Bool, 0x0, 0x0, 0x0)
    AnimationPool: (Bool, 0x0, 0x0, 0x0)
    UseNewX3dSkinnedMesh: (Bool, 0x0, 0x0, 0x0)
    AllowDefaultCharacterMaterialCreation: (Bool, 0x0, 0x0, 0x0)
    0xc9fddcee: (Bool, 0x0, 0x0, 0x0)
    0xcdbbc6e1: (Bool, 0x0, 0x0, 0x0)
    PathfindingV2: (Bool, 0x0, 0x0, 0x0)
    PreferBlndToGds: (Bool, 0x0, 0x0, 0x0)
    AnimationGds: (Bool, 0x0, 0x0, 0x0)
    0xf6d39e30: (Bool, 0x0, 0x0, 0x0)
    UnifiedDeathEffect: (Bool, 0x0, 0x0, 0x0)
    pass

class StoreElementData(ElementDataBase):
    InstanceData: (List2, 0x0, Embed, StoreInstanceData)
    pass

class OptionItemFilter_And(IOptionItemFilter):
    Filters: (List, 0x0, Pointer, IOptionItemFilter)
    pass

class ScriptSequence(IScriptSequence, Rscript):
    Blocks: (List, 0x0, Pointer, IScriptBlock)
    Blocks: (List2, 0x0, Pointer, IScriptBlock)
    pass

class UiButtonState():
    DisplayElements: (List, 0x0, Link, BaseElementData)
    TextElement: (Link, 0x0, 0x0, TextElementData)
    pass

class 0xa6a35b():
    pass

class OptionItemFilter_Windows(IOptionItemFilter):
    pass

class ToggleTeamCheat(Cheat):
    mTarget: (U32, 0x0, 0x0, 0x0)
    pass

class IFloatGet(IRsValueGet, IScriptValueGet):
    pass

class TftMobileLoginQueueData():
    Scene: (Hash, 0x0, 0x0, 0x0)
    BackgroundIcon: (Hash, 0x0, 0x0, 0x0)
    CurrentPositionText: (Hash, 0x0, 0x0, 0x0)
    VnLogo: (Hash, 0x0, 0x0, 0x0)
    WaitingTimeText: (Hash, 0x0, 0x0, 0x0)
    TwLogo: (Hash, 0x0, 0x0, 0x0)
    pass

class PracticeToolViewController(ViewController):
    MenuToggleScene: (Hash, 0x0, 0x0, 0x0)
    CheatIconMap: (Map, Hash, Hash, 0x0)
    SlotHeightRef: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    CheatSet: (Hash, 0x0, 0x0, 0x0)
    PageUp: (Hash, 0x0, 0x0, 0x0)
    ToggleMenuButton: (Hash, 0x0, 0x0, 0x0)
    MinimumScale: (F32, 0x0, 0x0, 0x0)
    MenuTitleScene: (Hash, 0x0, 0x0, 0x0)
    MenuScene: (Hash, 0x0, 0x0, 0x0)
    TooltipDelay: (F32, 0x0, 0x0, 0x0)
    PageDown: (Hash, 0x0, 0x0, 0x0)
    ButtonDefinition: (Embed, 0x0, 0x0, PracticeToolButtonDefinition)
    GroupDividerIndex: (U8, 0x0, 0x0, 0x0)
    GroupDividerGapSize: (F32, 0x0, 0x0, 0x0)
    MaximumScale: (F32, 0x0, 0x0, 0x0)
    pass

class OptionItemFilter_FeatureToggle(IOptionItemFilter):
    ToggleName: (String, 0x0, 0x0, 0x0)
    pass

class TftUnitInfoCustomButtonItemTooltipData():
    IsItemTooltipUnitProperty: (Hash, 0x0, 0x0, 0x0)
    ItemNameUnitProperty: (Hash, 0x0, 0x0, 0x0)
    pass

class UiElementEffectAnimationData(UiElementEffectData):
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    NumberOfFramesPerRowInAtlas: (F32, 0x0, 0x0, 0x0)
    TotalNumberOfFrames: (F32, 0x0, 0x0, 0x0)
    TextureData: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mAtlas: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFinishBehavior: (U8, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    FramesPerSecond: (F32, 0x0, 0x0, 0x0)
    pass

class LoadoutArenaSkinInfoPanel(ILoadoutInfoPanel):
    GamePassIcon: (Hash, 0x0, 0x0, 0x0)
    ItemLockIcon: (Hash, 0x0, 0x0, 0x0)
    RarityIcon: (List, 0x5, Hash, 0x0)
    ItemIconText: (Hash, 0x0, 0x0, 0x0)
    ItemIcon: (Hash, 0x0, 0x0, 0x0)
    0xee425ddc: (Hash, 0x0, 0x0, 0x0)
    pass

class BarElementTeamParams():
    mEnemyParams: (Pointer, 0x0, 0x0, BarElementParams)
    mAllyParams: (Pointer, 0x0, 0x0, BarElementParams)
    mNeutralParams: (Pointer, 0x0, 0x0, BarElementParams)
    pass

class HudReplayData():
    TeamFightData: (Embed, 0x0, 0x0, HudTeamFightData)
    MessageVisibleTime: (F32, 0x0, 0x0, 0x0)
    pass

class 0xa77231b9():
    0x1648560b: (String, 0x0, 0x0, 0x0)
    RegionsEnabled: (List2, 0x0, String, 0x0)
    Enabled: (Bool, 0x0, 0x0, 0x0)
    Target: (String, 0x0, 0x0, 0x0)
    Id: (String, 0x0, 0x0, 0x0)
    StartDate: (String, 0x0, 0x0, 0x0)
    RegionsDisabled: (List2, 0x0, String, 0x0)
    EndDate: (String, 0x0, 0x0, 0x0)
    ForegroundAssets: (Embed, 0x0, 0x0, 0xe7face9d)
    BackgroundAssets: (Embed, 0x0, 0x0, 0xe7face9d)
    TargetIsTrakey: (Bool, 0x0, 0x0, 0x0)
    TitleText: (String, 0x0, 0x0, 0x0)
    pass

class TftCutsceneCamSfxClip(TftCutsceneClip):
    StopAudioEvent: (String, 0x0, 0x0, 0x0)
    StartAudioEvent: (String, 0x0, 0x0, 0x0)
    BlackboardAssociatedPlayers: (List2, 0x0, String, 0x0)
    pass

class MapAudio(GenericMapPlaceable):
    EventName: (String, 0x0, 0x0, 0x0)
    VisibilityController: (Link, 0x0, 0x0, IMapVisibilityController)
    MaxIntervalSec: (F32, 0x0, 0x0, 0x0)
    AudioType: (U32, 0x0, 0x0, 0x0)
    StartTime: (F32, 0x0, 0x0, 0x0)
    MinIntervalSec: (F32, 0x0, 0x0, 0x0)
    pass

class GlobalAudioBanksProperties():
    AudioBankUnits: (List, 0x0, Embed, BankUnit)
    pass

class TftHintMessageViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    Background: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    MessageAnchorElements: (Map, Hash, Hash, 0x0)
    ArrowIcons: (List, 0x4, Hash, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    VfxScene: (Hash, 0x0, 0x0, 0x0)
    pass

class EffectKeyFrame():
    mTextureUvs: (Vec4, 0x0, 0x0, 0x0)
    mTime: (F32, 0x0, 0x0, 0x0)
    pass

class AbilityResourceThresholdIndicatorRange():
    RangeEnd: (F32, 0x0, 0x0, 0x0)
    RangeStart: (F32, 0x0, 0x0, 0x0)
    pass

class IdMappingEntry():
    Id: (U16, 0x0, 0x0, 0x0)
    Count: (U16, 0x0, 0x0, 0x0)
    pass

class UiElementEffectAnimatedRotatingIconData(UiElementEffectAnimationData):
    pass

class TogglePlantFastRespawnCheat(Cheat):
    pass

class EffectRotatingIconElementData(EffectElementData):
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    pass

class 0xa82b69c9(GameModeConstant):
    Item: (Link, 0x0, 0x0, TftItemData)
    pass

class BaseItemAdvice():
    mAttribute: (Hash, 0x0, 0x0, 0x0)
    pass

class MapLocator(GenericMapPlaceable):
    Scale: (Vec3, 0x0, 0x0, 0x0)
    Name: (Hash, 0x0, 0x0, 0x0)
    Position: (Vec3, 0x0, 0x0, 0x0)
    PitchYawRoll: (Vec3, 0x0, 0x0, 0x0)
    pass

class Shop(ShopCommon):
    pass

class NotScriptCondition(IScriptCondition):
    Condition: (Pointer, 0x0, 0x0, IScriptCondition)
    pass

class LevelController(BaseLevelController):
    Properties: (Map, Hash, Pointer, GameModeConstant)
    Script: (Link, 0x0, 0x0, LevelControlScript)
    Enabled: (Bool, 0x0, 0x0, 0x0)
    pass

class TftEncounterList():
    0x23c80d88: (List2, 0x0, Link, 0x42c94584)
    Encounters: (List2, 0x0, Link, TftEncounterData)
    pass

class LoadingScreenGameModeBackground():
    Background: (Hash, 0x0, 0x0, 0x0)
    pass

class PostGameLabFields():
    RatedIconData: (List, 0x0, Embed, NamedIconData)
    RatedTiersLocKeys: (Map, String, String, 0x0)
    RatedTierLocKeys: (Map, U32, String, 0x0)
    RatedLoadingIconVfx: (Hash, 0x0, 0x0, 0x0)
    RatedIcons: (Map, U32, Hash, 0x0)
    pass

class 0xa8a6ac21():
    pass

class VfxPaletteDefinitionData():
    PalleteSrcMixColor: (Embed, 0x0, 0x0, ValueColor)
    PaletteUAnimationCurve: (Embed, 0x0, 0x0, ValueFloat)
    PaletteVAnimationCurve: (Embed, 0x0, 0x0, ValueFloat)
    PaletteBlendRegister: (I32, 0x0, 0x0, 0x0)
    PaletteTextureAddressMode: (U8, 0x0, 0x0, 0x0)
    PaletteSelector: (Embed, 0x0, 0x0, ValueVector3)
    PaletteCount: (I32, 0x0, 0x0, 0x0)
    PaletteTexture: (String, 0x0, 0x0, 0x0)
    pass

class 0xa8c6f5f0():
    0x1793d323: (Hash, 0x0, 0x0, 0x0)
    0x4297f4f9: (Hash, 0x0, 0x0, 0x0)
    0x5329572e: (Hash, 0x0, 0x0, 0x0)
    0xb80015ba: (Hash, 0x0, 0x0, 0x0)
    pass

class FadeToExplicitValueBehavior(ITargeterFadeBehavior):
    mAlpha: (F32, 0x0, 0x0, 0x0)
    pass

class VfxSpawnConditions():
    mDefaultVfxData: (Embed, 0x0, 0x0, VfxDefaultSpawnConditionData)
    mConditionalVfxData: (List, 0x0, Pointer, VfxSpawnConditionData)
    pass

class ITargetingRangeValue():
    pass

class ViewControllerListFilter_And(ViewControllerListFilterI):
    Filters: (List, 0x0, Pointer, ViewControllerListFilterI)
    pass

class RemoveFromCustomTableBlock(IScriptBlock):
    Table: (Embed, 0x0, 0x0, CustomTableGet)
    Key: (Pointer, 0x0, 0x0, IScriptValueGet)
    Index: (Pointer, 0x0, 0x0, IIntGet)
    CustomTable: (Embed, 0x0, 0x0, CustomTableGet)
    pass

class UiTargetStatsMenu():
    TargetPerks: (Embed, 0x0, 0x0, UiPerksStats)
    ToggleButton: (Hash, 0x0, 0x0, 0x0)
    ParentScene: (Hash, 0x0, 0x0, 0x0)
    pass

class LoadoutSelectViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    LoadoutsButtonData: (List, 0x0, Embed, LoadoutsButtonData)
    pass

class 0xa92e29f6(ISequenceActionInstance):
    pass

class RerollTraitData():
    Badge: (Hash, 0x0, 0x0, 0x0)
    Color: (Color, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    pass

class TftCutsceneFinisherInitializer(TftCutsceneArenaLocatorInitializer):
    BlackboardFinisherSource: (String, 0x0, 0x0, 0x0)
    BlackboardFinisherTarget: (String, 0x0, 0x0, 0x0)
    pass

class VfxFieldAccelerationDefinitionData():
    Acceleration: (Embed, 0x0, 0x0, ValueVector3)
    Acceleration: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    IsLocalSpace: (Bool, 0x0, 0x0, 0x0)
    pass

class TftGameStartSequenceTurbo(TftGameStartSequence):
    GameStartTextShowDelaySecs: (F32, 0x0, 0x0, 0x0)
    GameStartText: (Hash, 0x0, 0x0, 0x0)
    GameStartTraKey: (String, 0x0, 0x0, 0x0)
    GameStartVfxStartTimeSecs: (F32, 0x0, 0x0, 0x0)
    GameStartReplacementTexture: (String, 0x0, 0x0, 0x0)
    GameStartVfxTop: (Hash, 0x0, 0x0, 0x0)
    GameStartTextShowDurationSecs: (F32, 0x0, 0x0, 0x0)
    GameStartIconBaseTexture: (String, 0x0, 0x0, 0x0)
    GameStartTextScene: (Hash, 0x0, 0x0, 0x0)
    GameStartVfxBottom: (Hash, 0x0, 0x0, 0x0)
    pass

class SelectRetreatSpellBlock(0x24f4a711):
    pass

class OptionItemSliderFloat(OptionItemSlider):
    UpdateOnDrag: (Bool, 0x0, 0x0, 0x0)
    Scale: (F32, 0x0, 0x0, 0x0)
    Option: (U16, 0x0, 0x0, 0x0)
    pass

class RemapFloatMaterialDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    mMinValue: (F32, 0x0, 0x0, 0x0)
    mMaxValue: (F32, 0x0, 0x0, 0x0)
    mDriver: (Pointer, 0x0, 0x0, IDynamicMaterialFloatDriver)
    mDriver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    mOutputMaxValue: (F32, 0x0, 0x0, 0x0)
    mOutputMinValue: (F32, 0x0, 0x0, 0x0)
    pass

class UiMilestoneMissionTemplate():
    LevelTextAvailable: (Hash, 0x0, 0x0, 0x0)
    ClaimedIcon: (Hash, 0x0, 0x0, 0x0)
    MeterAvailableIcon: (Hash, 0x0, 0x0, 0x0)
    FreeText: (Hash, 0x0, 0x0, 0x0)
    LevelTextActive: (Hash, 0x0, 0x0, 0x0)
    FreeBg: (Hash, 0x0, 0x0, 0x0)
    FreeFrameData: (Embed, 0x0, 0x0, UiMilestoneFrameData)
    PremiumFrameData: (Embed, 0x0, 0x0, UiMilestoneFrameData)
    MeterCompleteIcon: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    LevelPipCompleteDefault: (Hash, 0x0, 0x0, 0x0)
    MissionIconBackground: (Hash, 0x0, 0x0, 0x0)
    LevelPipActiveDefault: (Hash, 0x0, 0x0, 0x0)
    MeterBonusIcon: (Hash, 0x0, 0x0, 0x0)
    LevelPipBonusDefault: (Hash, 0x0, 0x0, 0x0)
    LevelTextComplete: (Hash, 0x0, 0x0, 0x0)
    LevelPipActiveHover: (Hash, 0x0, 0x0, 0x0)
    LevelPipBonusHover: (Hash, 0x0, 0x0, 0x0)
    LevelPipAvailableDefault: (Hash, 0x0, 0x0, 0x0)
    KeystoneFrameData: (Embed, 0x0, 0x0, UiMilestoneFrameData)
    EndRegion: (Hash, 0x0, 0x0, 0x0)
    MissionIcon: (Hash, 0x0, 0x0, 0x0)
    LevelPipCompleteHover: (Hash, 0x0, 0x0, 0x0)
    LevelPipAvailableHover: (Hash, 0x0, 0x0, 0x0)
    ClaimableIcon: (Hash, 0x0, 0x0, 0x0)
    HitRegion: (Hash, 0x0, 0x0, 0x0)
    ClaimableVfx: (Hash, 0x0, 0x0, 0x0)
    pass

class GameModeConstantFloatPerLevel(GameModeConstant):
    mValues: (List, 0x0, F32, 0x0)
    pass

class TftEventHubViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    0x45b34874: (Embed, 0x0, 0x0, 0x1668b3e5)
    0x5e0fc30b: (Embed, 0x0, 0x0, 0xba9f6aca)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    EventTimer: (Pointer, 0x0, 0x0, TftEventTimer)
    InfoButton: (Hash, 0x0, 0x0, 0x0)
    0xa0dd31e5: (Embed, 0x0, 0x0, 0x4e16b860)
    SceneRoot: (Hash, 0x0, 0x0, 0x0)
    CloseButton: (Hash, 0x0, 0x0, 0x0)
    0xe5388f19: (Hash, 0x0, 0x0, 0x0)
    pass

class Cast(MissileTriggeredActionSpec):
    RollForCriticalHitResult: (Bool, 0x0, 0x0, 0x0)
    pass

class GrassObject(GameObject):
    pass

class OptionTemplateCheckbox(IOptionTemplate):
    ButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    LabelElement: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xaa3a17e9(MapAction):
    CutsceneKey: (Hash, 0x0, 0x0, 0x0)
    pass

class MinimapIconRotate(MinimapIconBehavior):
    RotationPerSecondInDegrees: (F32, 0x0, 0x0, 0x0)
    pass

class EscapeBlock(IScriptBlock, IBehaviorScriptBlock):
    pass

class DamageShieldedLogic(IStatStoneLogicDriver):
    DamageSourceCanBeMinion: (Bool, 0x0, 0x0, 0x0)
    ShieldTargetCanBeTurret: (Bool, 0x0, 0x0, 0x0)
    DamageSourceCanBeChampion: (Bool, 0x0, 0x0, 0x0)
    ShieldTargetCanBeMinion: (Bool, 0x0, 0x0, 0x0)
    ShieldTargetCanBeChampion: (Bool, 0x0, 0x0, 0x0)
    ShieldTargetCanBeAlly: (Bool, 0x0, 0x0, 0x0)
    ShieldTargetCanBeSelf: (Bool, 0x0, 0x0, 0x0)
    DamageSourceCanBeTurret: (Bool, 0x0, 0x0, 0x0)
    pass

class PlayerProfileCategoryButtonDefinition():
    Button: (Hash, 0x0, 0x0, 0x0)
    Category: (U8, 0x0, 0x0, 0x0)
    pass

class DefaultHeightSolver(HeightSolverType):
    pass

class EffectGlowingRotatingIconElementData(EffectRotatingIconElementData):
    BrightnessMod: (F32, 0x0, 0x0, 0x0)
    CycleTime: (F32, 0x0, 0x0, 0x0)
    pass

class AnnouncementStyleTwoIconsFlanking(AnnouncementStyleBasic):
    OtherIcon: (Link, 0x0, 0x0, AnnouncementIcon)
    RightIcon: (Link, 0x0, 0x0, AnnouncementIcon)
    SourceIcon: (Link, 0x0, 0x0, AnnouncementIcon)
    LeftIcon: (Link, 0x0, 0x0, AnnouncementIcon)
    pass

class ToastNotificationsViewController(ViewController):
    QueueTypeToGameInviteIcon: (Map, String, Hash, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    ClickRegion: (Hash, 0x0, 0x0, 0x0)
    FriendInviteIcon: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    ToastDurationSecs: (F32, 0x0, 0x0, 0x0)
    BodyText: (Hash, 0x0, 0x0, 0x0)
    PassRewardIcon: (Hash, 0x0, 0x0, 0x0)
    EventIcon: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class SequenceTiming():
    Offset: (F32, 0x0, 0x0, 0x0)
    ScaleTiming: (Bool, 0x0, 0x0, 0x0)
    PhaseIndex: (I32, 0x0, 0x0, 0x0)
    pass

class CustomTableSet(ScriptTableSet):
    pass

class ScoreLinePortraitUiData():
    TimerText: (Hash, 0x0, 0x0, 0x0)
    0x27502925: (Hash, 0x0, 0x0, 0x0)
    FrameUnderlay: (Hash, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    PortraitIcon: (Hash, 0x0, 0x0, 0x0)
    FrameWhileDead: (Hash, 0x0, 0x0, 0x0)
    pass

class SceneData():
    mName: (String, 0x0, 0x0, 0x0)
    mHandleInputDuringPause: (Bool, 0x0, 0x0, 0x0)
    mHealthBar: (Bool, 0x0, 0x0, 0x0)
    mEnabled: (Bool, 0x0, 0x0, 0x0)
    mDynamic: (Bool, 0x0, 0x0, 0x0)
    mLayer: (U32, 0x0, 0x0, 0x0)
    SceneTransitionOut: (Pointer, 0x0, 0x0, SceneBaseTransitionData)
    SceneTransitionIn: (Pointer, 0x0, 0x0, SceneBaseTransitionData)
    mParentScene: (Link, 0x0, 0x0, SceneData)
    InheritScissoring: (Bool, 0x0, 0x0, 0x0)
    mAtlased: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xab02008c(0xa8a6ac21):
    Source: (Link, 0x0, 0x0, SequenceObjectSelector)
    DebugOverride: (String, 0x0, 0x0, 0x0)
    pass

class ShaderSamplerDef():
    AddressV: (U32, 0x0, 0x0, 0x0)
    AddressU: (U32, 0x0, 0x0, 0x0)
    FilterMin: (U32, 0x0, 0x0, 0x0)
    FilterMip: (U32, 0x0, 0x0, 0x0)
    SamplerName: (String, 0x0, 0x0, 0x0)
    FilterMag: (U32, 0x0, 0x0, 0x0)
    TextureName: (String, 0x0, 0x0, 0x0)
    AddressW: (U32, 0x0, 0x0, 0x0)
    pass

class FxActionSfxBaseInstance(IFxActionInstance):
    pass

class 0xab31041e(IGameModeConfig):
    0x2f6611e5: (U8, 0x0, 0x0, 0x0)
    0x4dccb36a: (Map, U32, U32, 0x0)
    GlobalBehaviors: (List2, 0x0, Pointer, 0x64c18f7d)
    pass

class AtlasData9Slice(AtlasDataBase):
    TopBottomHeights: (Vec2, 0x0, 0x0, 0x0)
    LeftRightWidths: (Vec2, 0x0, 0x0, 0x0)
    TextureUs: (Vec4, 0x0, 0x0, 0x0)
    TextureVs: (Vec4, 0x0, 0x0, 0x0)
    pass

class TftCustomAnnouncementViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    Style: (U8, 0x0, 0x0, 0x0)
    AnnouncementData: (Embed, 0x0, 0x0, TftCustomAnnouncementData)
    pass

class QuestDefinition():
    RecievedSoundPath: (String, 0x0, 0x0, 0x0)
    CompletedSoundPath: (String, 0x0, 0x0, 0x0)
    CategoryTitleText: (String, 0x0, 0x0, 0x0)
    MaxViewableQuests: (U32, 0x0, 0x0, 0x0)
    FailedSoundPath: (String, 0x0, 0x0, 0x0)
    pass

class 0xab597393(Cheat):
    pass

class 0xab5db4f2(0xbc413e21):
    ColorEasing: (U8, 0x0, 0x0, 0x0)
    Colors: (List2, 0x0, Pointer, 0xd1b1f16)
    pass

class LolGameStateViewController(GameStateViewController):
    DrawAreaList: (Embed, 0x0, 0x0, DrawAreaList)
    pass

class TftTraitInfoNubData(TftInfoNubData):
    Trait: (Link, 0x0, 0x0, TftTraitData)
    TitleKey: (String, 0x0, 0x0, 0x0)
    pass

class SwitchMaterialDriver(IDynamicMaterialDriver, ILogicDriver):
    mElements: (List, 0x0, Embed, SwitchMaterialDriverElement)
    mDefaultValue: (Pointer, 0x0, 0x0, IDynamicMaterialDriver)
    mDefaultValue: (Pointer, 0x0, 0x0, ILogicDriver)
    pass

class IInputSourceFloat():
    pass

class GlobalCcBehaviorData(ICcBehaviorData):
    GlobalCcBehavior: (Hash, 0x0, 0x0, 0x0)
    pass

class CustomDamageStatStoneData(StatStoneData):
    mDamageEvent: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xac27b13a():
    Groups: (List2, 0x0, Embed, HudItemShopItemGroupDefinition)
    pass

class RotateMapLightUpdater(IMapLightUpdater):
    WorldSpace: (Bool, 0x0, 0x0, 0x0)
    AxisSpeed: (Vec3, 0x0, 0x0, 0x0)
    pass

class MapAreaGroupCheck():
    AreasToCheck: (List2, 0x0, U32, 0x0)
    AreaCheckQuantifier: (U32, 0x0, 0x0, 0x0)
    pass

class 0xac83c7b():
    Id: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class 0xac9d1b24():
    pass

class TraitInfoNubData(InfoNubData):
    Trait: (Hash, 0x0, 0x0, 0x0)
    TitleKey: (String, 0x0, 0x0, 0x0)
    pass

class 0xacb2dba1():
    Region: (Hash, 0x0, 0x0, 0x0)
    0xba819369: (U8, 0x0, 0x0, 0x0)
    pass

class NeutralMinionCampCommon(GameObject):
    pass

class CrowdControlFilter(IStatStoneLogicDriver):
    ValidCcTypes: (List, 0x0, U8, 0x0)
    Root: (Bool, 0x0, 0x0, 0x0)
    Knockup: (Bool, 0x0, 0x0, 0x0)
    Slow: (Bool, 0x0, 0x0, 0x0)
    TrackDuration: (Bool, 0x0, 0x0, 0x0)
    Knockback: (Bool, 0x0, 0x0, 0x0)
    pass

class VfxAnimatedVector3fVariableData(VfxVector3fBase):
    Values: (List, 0x0, Vec3, 0x0)
    Times: (List, 0x0, F32, 0x0)
    ProbabilityTables: (List, 0x3, Pointer, VfxProbabilityTableData)
    pass

class EffectInstancedElementData(EffectElementData):
    mAdditionalOffsets: (List, 0x0, Vec2, 0x0)
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    mColor: (Color, 0x0, 0x0, 0x0)
    Offsets: (List, 0x0, Vec2, 0x0)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    pass

class MapLocatorArray():
    Locators: (List, 0x0, Embed, MapLocator)
    pass

class ProductOfSubPartsCalculationPart(IGameCalculationPart, ISpellCalculationPart):
    mPart1: (Pointer, 0x0, 0x0, IGameCalculationPart)
    mPart1: (Pointer, 0x0, 0x0, ISpellCalculationPart)
    mPart2: (Pointer, 0x0, 0x0, IGameCalculationPart)
    mPart2: (Pointer, 0x0, 0x0, ISpellCalculationPart)
    pass

class StatLargestAbilityDamageConstraintInfo(ListenerConstraintInfo):
    pass

class UnitFields():
    TwoStars: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    OneStar: (Hash, 0x0, 0x0, 0x0)
    ThreeStars: (Hash, 0x0, 0x0, 0x0)
    IconFrame: (Hash, 0x0, 0x0, 0x0)
    ItemIcons: (List, 0x0, Hash, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class ViewControllerFilter_Spectator(ViewControllerFilterI):
    pass

class HealthBarFadeData():
    FadeAcceleration: (F32, 0x0, 0x0, 0x0)
    FadeBar: (Embed, 0x0, 0x0, BarTypeMap)
    FadeHoldTime: (F32, 0x0, 0x0, 0x0)
    FadeSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class TftGameHeaderViewController(GameStateViewController, ViewController):
    TftEncounterToggleButton: (Hash, 0x0, 0x0, 0x0)
    TftGameTeamPlannerButton: (Hash, 0x0, 0x0, 0x0)
    TeamPlannerDisabledTooltipTraKey: (String, 0x0, 0x0, 0x0)
    BadgeVfx: (Hash, 0x0, 0x0, 0x0)
    TftGameHeaderScene: (Hash, 0x0, 0x0, 0x0)
    BadgeBg: (Hash, 0x0, 0x0, 0x0)
    OptionsMenuTooltipTraKey: (String, 0x0, 0x0, 0x0)
    TeamPlannerTooltipTraKey: (String, 0x0, 0x0, 0x0)
    MusicSourceButton: (Hash, 0x0, 0x0, 0x0)
    TftTraitsItemsToggleButton: (Hash, 0x0, 0x0, 0x0)
    MusicSourceInfo: (Hash, 0x0, 0x0, 0x0)
    BadgeText: (Hash, 0x0, 0x0, 0x0)
    TooltipAnchorCentering: (U8, 0x0, 0x0, 0x0)
    BatteryLevels: (List, 0xa, Hash, 0x0)
    TooltipAnchor: (Hash, 0x0, 0x0, 0x0)
    TftGameSettingsButton: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xad84e5d(0x27071fbd):
    Source: (Link, 0x0, 0x0, SequenceObjectSelector)
    pass

class TftPassRewardCurrency(TftPassRewardBase):
    CurrencyInfo: (Link, 0x0, 0x0, TftPassCurrencyInfo)
    pass

class UiMultiKillIconData():
    Region: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class MapSpotlightBase(MapProjectedTexture):
    Impact: (I32, 0x0, 0x0, 0x0)
    Impact: (U8, 0x0, 0x0, 0x0)
    Color: (Vec4, 0x0, 0x0, 0x0)
    Intensity: (F32, 0x0, 0x0, 0x0)
    0xe281ed56: (F32, 0x0, 0x0, 0x0)
    pass

class 0xae005c94(IGameModeConfig):
    ProgressionTracks: (List2, 0x0, Link, ProgressTrack)
    pass

class TftTooltipData():
    IconPath: (String, 0x0, 0x0, 0x0)
    Replication: (U8, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    TitleTra: (String, 0x0, 0x0, 0x0)
    DescriptionTra: (String, 0x0, 0x0, 0x0)
    pass

class IBoolGet(IRsValueGet, IScriptValueGet):
    pass

class CherryTeamFlyoutPanelFightTeamFrame():
    FightTeamBackground: (Embed, 0x0, 0x0, IconStateData)
    FightIcon: (Hash, 0x0, 0x0, 0x0)
    OpponentIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class InhibitorWaveBehavior(IMinionWaveBehavior):
    DefaultSpawnCount: (I32, 0x0, 0x0, 0x0)
    SpawnCountPerInhibitorDown: (List2, 0x0, I32, 0x0)
    pass

class TrueDamageGivenFilter(IStatStoneLogicDriver):
    pass

class 0xae78433f(IScriptBlock):
    pass

class TftMapCharacterList():
    ListName: (String, 0x0, 0x0, 0x0)
    Characters: (List, 0x0, Embed, TftMapCharacterData)
    Characters: (List2, 0x0, Embed, TftMapCharacterData)
    pass

class MobileCatalogData():
    PurchaseRateLimit: (I32, 0x0, 0x0, 0x0)
    Active: (Bool, 0x0, 0x0, 0x0)
    ItemInstanceId: (String, 0x0, 0x0, 0x0)
    IncrementalPurchase: (Bool, 0x0, 0x0, 0x0)
    pass

class Joint():
    mName: (String, 0x0, 0x0, 0x0)
    mNameHash: (U32, 0x0, 0x0, 0x0)
    mParentIndex: (I16, 0x0, 0x0, 0x0)
    mRadius: (F32, 0x0, 0x0, 0x0)
    mIndex: (U16, 0x0, 0x0, 0x0)
    mFlags: (U16, 0x0, 0x0, 0x0)
    pass

class 0xaeb4bf1(IScriptBlock, IBehaviorScriptBlock):
    pass

class TftCraftingDialogViewController(ModalDialogViewController):
    0x317bc379: (Hash, 0x0, 0x0, 0x0)
    ErrorTitleText: (Hash, 0x0, 0x0, 0x0)
    CraftingSequence: (Link, 0x0, 0x0, Sequence)
    ErrorBodyTra: (String, 0x0, 0x0, 0x0)
    BodyText: (Hash, 0x0, 0x0, 0x0)
    0xe6a5be46: (String, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    BackgroundTexture: (Hash, 0x0, 0x0, 0x0)
    pass

class TftUnitShopViewController(ViewController):
    BuyExpButton: (Hash, 0x0, 0x0, 0x0)
    TurboOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    StreakUi: (Embed, 0x0, 0x0, TftHudStreakUi)
    InfoNubTooltipRegion: (Hash, 0x0, 0x0, 0x0)
    RerollButtonReminderVfxHandle: (Hash, 0x0, 0x0, 0x0)
    ZoomTransitionOut: (Embed, 0x0, 0x0, HudMenuTransitionData)
    ShopClickRejectedVfx: (Hash, 0x0, 0x0, 0x0)
    RerollCostTextHandle: (Hash, 0x0, 0x0, 0x0)
    GoldTooltipTraKeys: (Map, U32, Embed, GoldTooltipTraKeys)
    0x2d835fc0: (Hash, 0x0, 0x0, 0x0)
    RerollTraitName: (String, 0x0, 0x0, 0x0)
    GoldTextHandle: (Hash, 0x0, 0x0, 0x0)
    DropRate: (Embed, 0x0, 0x0, TftHudUnitShopDropRate)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    ToggleShopButton: (Hash, 0x0, 0x0, 0x0)
    0x44358b5: (Pointer, 0x0, 0x0, TftHudUnitShopDropRate)
    InfoNubButton: (Hash, 0x0, 0x0, 0x0)
    ShopDragArea: (Hash, 0x0, 0x0, 0x0)
    RerollClickElement: (Hash, 0x0, 0x0, 0x0)
    ToggleShopButtonScene: (Hash, 0x0, 0x0, 0x0)
    ExpBar: (Embed, 0x0, 0x0, TftHudExpBar)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    RerollClickDefaultVfx: (Hash, 0x0, 0x0, 0x0)
    0x6a7a42c9: (List, 0x2, Hash, 0x0)
    MainShopSceneHandle: (Hash, 0x0, 0x0, 0x0)
    BuyExpButtonTextHandle: (Hash, 0x0, 0x0, 0x0)
    CloseShopReminderVfxHandle: (Hash, 0x0, 0x0, 0x0)
    InfoNubData: (Pointer, 0x0, 0x0, InfoNubData)
    TopLevelSceneHandle: (Hash, 0x0, 0x0, 0x0)
    InfoButton: (Hash, 0x0, 0x0, 0x0)
    ItemTemplate: (Embed, 0x0, 0x0, UnitShopItemData)
    LockButton: (Hash, 0x0, 0x0, 0x0)
    BuyExpClickElement: (Hash, 0x0, 0x0, 0x0)
    BuyExpIconData: (Embed, 0x0, 0x0, IconData)
    RerollButton: (Hash, 0x0, 0x0, 0x0)
    GoldFrame: (Hash, 0x0, 0x0, 0x0)
    BuyExpButtonScene: (Hash, 0x0, 0x0, 0x0)
    MobileDelays: (Embed, 0x0, 0x0, TftShopMobileDelays)
    RerollButtonStyles: (Map, Hash, Hash, 0x0)
    SellTextHandle: (List, 0x2, Hash, 0x0)
    0x9a02c4cf: (Hash, 0x0, 0x0, 0x0)
    RerollButtonTextHandle: (Hash, 0x0, 0x0, 0x0)
    NextShopHighlightElement: (Hash, 0x0, 0x0, 0x0)
    GainXpVfx_Top: (Hash, 0x0, 0x0, 0x0)
    LevelTextHandle: (Hash, 0x0, 0x0, 0x0)
    RerollTraitData: (Map, U8, Embed, RerollTraitData)
    ItemSlotHandles: (List, 0x5, Hash, 0x0)
    RerollTraitShouldShow: (Bool, 0x0, 0x0, 0x0)
    0xb6e30812: (List, 0x2, Hash, 0x0)
    0xbb192022: (List, 0x2, Hash, 0x0)
    RerollTraitCounterText: (Hash, 0x0, 0x0, 0x0)
    LevelUpDisplayDelaySecs: (F32, 0x0, 0x0, 0x0)
    0xc5504a34: (Bool, 0x0, 0x0, 0x0)
    DragAreaHandle: (Hash, 0x0, 0x0, 0x0)
    ExpVfx: (List, 0x3, Hash, 0x0)
    0xcfe62cb0: (List, 0x2, Hash, 0x0)
    BuyExpCostTextHandle: (Hash, 0x0, 0x0, 0x0)
    ToggleShopReminderVfxHandle: (Hash, 0x0, 0x0, 0x0)
    GoldGainVfxHandle: (Hash, 0x0, 0x0, 0x0)
    SellAreas: (List, 0x2, Embed, TftSellArea)
    TurboMobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    ModalShroudHandle: (Hash, 0x0, 0x0, 0x0)
    CurrShopHighlightElement: (Hash, 0x0, 0x0, 0x0)
    BuyExpClickDefaultVfx: (Hash, 0x0, 0x0, 0x0)
    ZoomTransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    GoldDisplaySceneHandle: (Hash, 0x0, 0x0, 0x0)
    pass

class ScoreboardGameModeConfig(IGameModeConfigClient):
    ScoreboardTeamScoreTypes: (U32, 0x0, 0x0, 0x0)
    0xc72e2257: (U32, 0x0, 0x0, 0x0)
    pass

class MapActionBuildUpMapParticle(MapAction):
    BoomMapParticleName: (String, 0x0, 0x0, 0x0)
    BoomLifeTimeSec: (F32, 0x0, 0x0, 0x0)
    BuildupMapParticleNames: (List, 0x0, String, 0x0)
    Shuffle: (Bool, 0x0, 0x0, 0x0)
    pass

class DragDirection(TargetingTypeData):
    pass

class PregameChatViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    FriendOptionsButton: (Hash, 0x0, 0x0, 0x0)
    CloseButton: (Hash, 0x0, 0x0, 0x0)
    pass

class ElementGroupSliderSoundEvents():
    OnBarClickedEvent: (String, 0x0, 0x0, 0x0)
    OnDragEndEvent: (String, 0x0, 0x0, 0x0)
    OnDragStartEvent: (String, 0x0, 0x0, 0x0)
    pass

class LoadingScreenRatedData():
    QueueTypeToSourceTierIcons: (Map, String, Link, LoadingScreenRatedTierIconData)
    RatedText: (Hash, 0x0, 0x0, 0x0)
    SourceTierIcons: (Link, 0x0, 0x0, LoadingScreenRatedTierIconData)
    RatedTierIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class AcceleratingMovement(MissileMovementSpec):
    mProjectTargetToCastRange: (Bool, 0x0, 0x0, 0x0)
    mUseGroundHeightAtTarget: (Bool, 0x0, 0x0, 0x0)
    mInferDirectionFromFacingIfNeeded: (Bool, 0x0, 0x0, 0x0)
    mInitialSpeed: (F32, 0x0, 0x0, 0x0)
    mAcceleration: (F32, 0x0, 0x0, 0x0)
    AddBonusAttackRangeToCastRange: (Bool, 0x0, 0x0, 0x0)
    mMinSpeed: (F32, 0x0, 0x0, 0x0)
    mMaxSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class NamedIconData():
    Name: (String, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class OptionsTab():
    Items: (List, 0x0, Pointer, IOptionItem)
    AddPaddingAfterLastItem: (Bool, 0x0, 0x0, 0x0)
    Filter: (Pointer, 0x0, 0x0, IOptionItemFilter)
    TabNameTraKey: (String, 0x0, 0x0, 0x0)
    ShowOn: (U8, 0x0, 0x0, 0x0)
    pass

class BezierPath(IPath):
    Segments: (List2, 0x0, Embed, BezierSegment)
    pass

class TftBannerTableEntry():
    Id: (String, 0x0, 0x0, 0x0)
    Weight: (U32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    BannerNode: (Link, 0x0, 0x0, TftBannerNode)
    pass

class RsTableSet():
    Table: (Pointer, 0x0, 0x0, RsTable)
    Var: (String, 0x0, 0x0, 0x0)
    pass

class StatLargestAttackDamageConstraintInfo(ListenerConstraintInfo):
    pass

class TftTraitTrackerTraitDataTemplate():
    MobileTapRegion: (Hash, 0x0, 0x0, 0x0)
    NameBackground: (Hash, 0x0, 0x0, 0x0)
    Count: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    AugmentedVfx: (Hash, 0x0, 0x0, 0x0)
    TotalCountBackground: (Hash, 0x0, 0x0, 0x0)
    TotalCount: (Hash, 0x0, 0x0, 0x0)
    Name: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    IconBackgrounds: (List, 0x5, Embed, TftTraitTrackerTraitIconData)
    IconBackgrounds: (List, 0x6, Embed, TftTraitTrackerTraitIconData)
    IconBackgrounds: (List, 0x7, Embed, TftTraitTrackerTraitIconData)
    pass

class BarElement():
    mTextureMode: (U32, 0x0, 0x0, 0x0)
    mMegaTickTextureUvs: (Vec4, 0x0, 0x0, 0x0)
    mOffset: (Vec2, 0x0, 0x0, 0x0)
    mTickTextureUvs: (Vec4, 0x0, 0x0, 0x0)
    mAdditionalBarTextureUvs: (List, 0x0, Vec4, 0x0)
    mAnchorToRightOfHealthBar: (Bool, 0x0, 0x0, 0x0)
    mParamsColorBlind: (Pointer, 0x0, 0x0, BarElementTeamParams)
    mParamsDefault: (Pointer, 0x0, 0x0, BarElementTeamParams)
    mBarTextureUvs: (Vec4, 0x0, 0x0, 0x0)
    mTickPixelWidth: (I32, 0x0, 0x0, 0x0)
    mFadeSpeed: (F32, 0x0, 0x0, 0x0)
    mTextureName: (String, 0x0, 0x0, 0x0)
    pass

class 0xb0617ced(0xac83c7b):
    NameTraKey: (String, 0x0, 0x0, 0x0)
    Children: (List, 0x0, Embed, 0x7c02b00b)
    pass

class HealthBarTextData():
    HealthValueText: (Hash, 0x0, 0x0, 0x0)
    IncludeMaxHealth: (Bool, 0x0, 0x0, 0x0)
    DisplayMode: (U8, 0x0, 0x0, 0x0)
    HealthRegenText: (Hash, 0x0, 0x0, 0x0)
    pass

class AnimatedBuildingCommon(BuildingClient):
    pass

class 0xb09016f6():
    EffectCalculation: (Pointer, 0x0, 0x0, IGameCalculation)
    EffectTag: (U32, 0x0, 0x0, 0x0)
    pass

class VfxTextureMultDefinitionData():
    IsRandomStartFrameMult: (Flag, 0x0, 0x0, 0x0)
    TexDivMult: (Vec2, 0x0, 0x0, 0x0)
    ParticleIntegratedUvScrollMult: (Embed, 0x0, 0x0, IntegratedValueVector2)
    TextureMult: (String, 0x0, 0x0, 0x0)
    BirthUvScrollRateMult: (Embed, 0x0, 0x0, ValueVector2)
    UvRotationMult: (Embed, 0x0, 0x0, ValueFloat)
    TextureMultFilpV: (Flag, 0x0, 0x0, 0x0)
    UvTransformCenterMult: (Vec2, 0x0, 0x0, 0x0)
    TextureMultFilpU: (Flag, 0x0, 0x0, 0x0)
    TexAddressModeMult: (U8, 0x0, 0x0, 0x0)
    BirthUvoffsetMult: (Embed, 0x0, 0x0, ValueVector2)
    UvScrollClampMult: (Flag, 0x0, 0x0, 0x0)
    FlexBirthUvScrollRateMult: (Pointer, 0x0, 0x0, FlexValueVector2)
    UvScaleMult: (Embed, 0x0, 0x0, ValueVector2)
    ParticleIntegratedUvRotateMult: (Embed, 0x0, 0x0, IntegratedValueFloat)
    EmitterUvScrollRateMult: (Vec2, 0x0, 0x0, 0x0)
    UvScrollAlphaMult: (Flag, 0x0, 0x0, 0x0)
    BirthUvRotateRateMult: (Embed, 0x0, 0x0, ValueFloat)
    pass

class SocialChatViewController(ViewController):
    UiSocialChatMessageTemplate: (Embed, 0x0, 0x0, UiSocialChatMessageTemplate)
    Scene: (Hash, 0x0, 0x0, 0x0)
    FriendIcon: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    SentMessageColor: (Color, 0x0, 0x0, 0x0)
    YesterdayTraKey: (String, 0x0, 0x0, 0x0)
    FriendName: (Hash, 0x0, 0x0, 0x0)
    InputTextFieldLink: (Hash, 0x0, 0x0, 0x0)
    TodayTraKey: (String, 0x0, 0x0, 0x0)
    FriendOptionsButton: (Hash, 0x0, 0x0, 0x0)
    SendButton: (Hash, 0x0, 0x0, 0x0)
    CloseButton: (Hash, 0x0, 0x0, 0x0)
    ReceivedMessageColor: (Color, 0x0, 0x0, 0x0)
    UiChatPaneDefinition: (Embed, 0x0, 0x0, UiChatPaneDefinition)
    pass

class TftMapTraitData():
    Description: (String, 0x0, 0x0, 0x0)
    DisplayName: (String, 0x0, 0x0, 0x0)
    DecoratedName: (String, 0x0, 0x0, 0x0)
    IconPath: (String, 0x0, 0x0, 0x0)
    ActiveIconColor: (Color, 0x0, 0x0, 0x0)
    pass

class ObjectiveVoteResultData():
    TimeLeft: (Hash, 0x0, 0x0, 0x0)
    RejectCountBg: (Hash, 0x0, 0x0, 0x0)
    VfxGroup: (Hash, 0x0, 0x0, 0x0)
    ForCountIcon: (Hash, 0x0, 0x0, 0x0)
    ForCountPlayerBg: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    BoundingRegion: (Hash, 0x0, 0x0, 0x0)
    ObjectivePortrait: (Hash, 0x0, 0x0, 0x0)
    ForIcon: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    ForCountBg: (Hash, 0x0, 0x0, 0x0)
    DividerBg: (Hash, 0x0, 0x0, 0x0)
    ObjectivePortraitVotingAligned: (Hash, 0x0, 0x0, 0x0)
    TimeLeftCampIcon: (Hash, 0x0, 0x0, 0x0)
    CountBg: (Hash, 0x0, 0x0, 0x0)
    PendingCountIcon: (Hash, 0x0, 0x0, 0x0)
    PendingIcon: (Hash, 0x0, 0x0, 0x0)
    ForCount: (Hash, 0x0, 0x0, 0x0)
    TimeLeftBg: (Hash, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    RejectCount: (Hash, 0x0, 0x0, 0x0)
    TimeExpiredCampIcon: (Hash, 0x0, 0x0, 0x0)
    RejectIcon: (Hash, 0x0, 0x0, 0x0)
    RejectCountPlayerBg: (Hash, 0x0, 0x0, 0x0)
    RejectCountIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class LoadingScreenSummonerNameData():
    OtherPlayerNameColor: (Color, 0x0, 0x0, 0x0)
    LocalPlayerNameColor: (Color, 0x0, 0x0, 0x0)
    SummonerName: (List, 0x0, Hash, 0x0)
    pass

class LolModesReplayConfig(IGameModeConfig):
    0x7eec920b: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xb0e1e45e():
    UpdaterType: (U32, 0x0, 0x0, 0x0)
    pass

class AlwaysSpawnCondition(IVfxSpawnConditions):
    mDefaultVfxData: (Embed, 0x0, 0x0, VfxDefaultSpawnConditionData)
    pass

class ContextualConditionPreviousMapRegionName(ContextualConditionMapRegionName):
    pass

class ToolEducationData():
    FirstItem: (I32, 0x0, 0x0, 0x0)
    SkillOrder: (I32, 0x0, 0x0, 0x0)
    pass

class ILevelScriptEvent(IScriptEvent):
    pass

class ColorLogicDriverLightUpdater(IMapLightUpdater):
    Driver: (Pointer, 0x0, 0x0, ILogicDriver)
    pass

class TargetHasBuffFilter(IStatStoneLogicDriver):
    ValidBuffs: (List, 0x0, U8, 0x0)
    Stun: (Bool, 0x0, 0x0, 0x0)
    pass

class PerkEffectAmountPerMode():
    mEffectAmountPerMode: (Map, Hash, F32, 0x0)
    pass

class TftCutsceneUiToggleClip(TftCutsceneClip):
    UiMobileHideShopButton: (U32, 0x0, 0x0, 0x0)
    UiHideHealthBars: (U32, 0x0, 0x0, 0x0)
    UiHideMinimap: (U32, 0x0, 0x0, 0x0)
    UiMobileHideItemPanel: (U32, 0x0, 0x0, 0x0)
    UiHideFloatingText: (U32, 0x0, 0x0, 0x0)
    UiMobileShouldClearOpenMenus: (U32, 0x0, 0x0, 0x0)
    UiMobileHideHeaderButtons: (U32, 0x0, 0x0, 0x0)
    UiHideScoreboard: (U32, 0x0, 0x0, 0x0)
    UiClearTooltips: (U32, 0x0, 0x0, 0x0)
    UiHideStage: (U32, 0x0, 0x0, 0x0)
    UiHideTraitTracker: (U32, 0x0, 0x0, 0x0)
    BlackboardAssociatedPlayers: (List2, 0x0, String, 0x0)
    UiHideShop: (U32, 0x0, 0x0, 0x0)
    pass

class VfxFlexShapeDefinitionData():
    ScaleEmitOffsetByBoundObjectHeight: (F32, 0x0, 0x0, 0x0)
    ScaleBirthScaleByBoundObjectRadius: (F32, 0x0, 0x0, 0x0)
    FlexScaleEmitOffset: (Pointer, 0x0, 0x0, FlexTypeFloat)
    ScaleEmitOffsetByBoundObjectRadius: (F32, 0x0, 0x0, 0x0)
    ScaleBirthTranslationByBoundObjectSize: (F32, 0x0, 0x0, 0x0)
    FlexBirthTranslation: (Pointer, 0x0, 0x0, FlexValueVector3)
    ScaleBirthScaleByBoundObjectSize: (F32, 0x0, 0x0, 0x0)
    ScaleEmitOffsetByBoundObjectSize: (F32, 0x0, 0x0, 0x0)
    ScaleBirthScaleByBoundObjectHeight: (F32, 0x0, 0x0, 0x0)
    pass

class NavHeaderViewController(ViewController):
    TftCoinsWidget: (Embed, 0x0, 0x0, TftCurrencyWidget)
    StarShardsWidget: (Embed, 0x0, 0x0, TftCurrencyWidget)
    StarShardsDecreaseVfx: (Hash, 0x0, 0x0, 0x0)
    StarShardsButton: (Hash, 0x0, 0x0, 0x0)
    TrovesTokenStoreListing: (Link, 0x0, 0x0, StoreListingData)
    MissionsButtonHint: (Pointer, 0x0, 0x0, TftHintUiData)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    NavigationText: (Hash, 0x0, 0x0, 0x0)
    PlayerNameTextUnranked: (Hash, 0x0, 0x0, 0x0)
    0x437a171e: (Hash, 0x0, 0x0, 0x0)
    NavHeaderScene: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    ProfileWidgetScene: (Hash, 0x0, 0x0, 0x0)
    PlayerRankText: (Hash, 0x0, 0x0, 0x0)
    0x53e676c5: (Embed, 0x0, 0x0, TftCurrencyWidget)
    StarShardsStoreDialog: (Hash, 0x0, 0x0, 0x0)
    StarShardsStoreDialog: (Link, 0x0, 0x0, StoreDialogViewController)
    PlayerIcon: (Hash, 0x0, 0x0, 0x0)
    TftCoinsIncreaseSourceVfx: (Hash, 0x0, 0x0, 0x0)
    SettingsButton: (Hash, 0x0, 0x0, 0x0)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    TrovesTokensIncreaseSourceVfx: (Hash, 0x0, 0x0, 0x0)
    0x6d205220: (Hash, 0x0, 0x0, 0x0)
    TrovesTokensButton: (Hash, 0x0, 0x0, 0x0)
    TrovesTokensIncreaseSinkVfx: (Hash, 0x0, 0x0, 0x0)
    ProfileBackground: (Hash, 0x0, 0x0, 0x0)
    LoadingSpinnerScene: (Hash, 0x0, 0x0, 0x0)
    0x781c35c3: (Hash, 0x0, 0x0, 0x0)
    StarShardsIncreaseSinkVfx: (Hash, 0x0, 0x0, 0x0)
    MissionsBadgeVfx: (Hash, 0x0, 0x0, 0x0)
    PlayerNameTextRanked: (Hash, 0x0, 0x0, 0x0)
    PlayerProfileButton: (Hash, 0x0, 0x0, 0x0)
    0x817d03a4: (Hash, 0x0, 0x0, 0x0)
    StarShardsIncreaseSourceVfx: (Hash, 0x0, 0x0, 0x0)
    TftCoinsDecreaseVfx: (Hash, 0x0, 0x0, 0x0)
    NotificationsButton: (Hash, 0x0, 0x0, 0x0)
    SocialButton: (Hash, 0x0, 0x0, 0x0)
    FiatStoreDialog: (Hash, 0x0, 0x0, 0x0)
    0x9b36efaf: (Embed, 0x0, 0x0, TftCurrencyWidget)
    SocialBadgeVfx: (Hash, 0x0, 0x0, 0x0)
    TrovesTokensWidget: (Embed, 0x0, 0x0, TftCurrencyWidget)
    0xcdbd2759: (Hash, 0x0, 0x0, 0x0)
    BackButton: (Hash, 0x0, 0x0, 0x0)
    BatteryLevels: (List, 0xa, Hash, 0x0)
    TftCoinsIncreaseSinkVfx: (Hash, 0x0, 0x0, 0x0)
    UtilityDivider: (Hash, 0x0, 0x0, 0x0)
    TftCoinsButton: (Hash, 0x0, 0x0, 0x0)
    TrovesTokensStoreDialog: (Hash, 0x0, 0x0, 0x0)
    MissionsButton: (Hash, 0x0, 0x0, 0x0)
    NotificationsBadgeVFX: (Hash, 0x0, 0x0, 0x0)
    TrovesTokensDecreaseVfx: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xb142b357():
    Techniques: (List, 0x0, Embed, 0xd5b41170)
    Name: (String, 0x0, 0x0, 0x0)
    0xd2190b18: (String, 0x0, 0x0, 0x0)
    pass

class WorldVars(ScriptTable):
    pass

class 0xb1757147(IFxAction):
    Looping: (Bool, 0x0, 0x0, 0x0)
    Particle: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    Object: (Embed, 0x0, 0x0, FxObjectSelector)
    pass

class HudScaleSettingsData():
    MaximumMinimapScale: (F32, 0x0, 0x0, 0x0)
    MinimumMinimapScale: (F32, 0x0, 0x0, 0x0)
    MaximumPracticeToolScale: (F32, 0x0, 0x0, 0x0)
    MinimumGlobalScale: (F32, 0x0, 0x0, 0x0)
    MaximumGlobalScale: (F32, 0x0, 0x0, 0x0)
    MaximumDeathRecapScale: (F32, 0x0, 0x0, 0x0)
    MinimumChatScale: (F32, 0x0, 0x0, 0x0)
    MinimumPracticeToolScale: (F32, 0x0, 0x0, 0x0)
    MinimumDeathRecapScale: (F32, 0x0, 0x0, 0x0)
    MaximumChatScale: (F32, 0x0, 0x0, 0x0)
    pass

class HeroFloatingInfoBorderTypeData():
    Highlight: (Hash, 0x0, 0x0, 0x0)
    LevelBoxOverlayAlly: (Hash, 0x0, 0x0, 0x0)
    Border: (Hash, 0x0, 0x0, 0x0)
    LevelBoxOverlaySelfColorblind: (Hash, 0x0, 0x0, 0x0)
    LevelBoxOverlaySelf: (Hash, 0x0, 0x0, 0x0)
    LevelBoxOverlayEnemy: (Hash, 0x0, 0x0, 0x0)
    AnimIn: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xb1c7f3d2(0x48eb8d47):
    EqualTo: (I32, 0x0, 0x0, 0x0)
    pass

class 0xb1c81e63():
    0x237182f6: (Bool, 0x0, 0x0, 0x0)
    Description: (String, 0x0, 0x0, 0x0)
    DelayFrames: (I32, 0x0, 0x0, 0x0)
    0x770acb64: (List, 0x0, I32, 0x0)
    Path: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    0xb119d28: (Bool, 0x0, 0x0, 0x0)
    HeroId: (I32, 0x0, 0x0, 0x0)
    Actions: (List, 0x0, Pointer, 0xbbac8ee0)
    0xbe87260f: (Bool, 0x0, 0x0, 0x0)
    0xd598ba1: (List, 0x0, I32, 0x0)
    pass

class LoadoutViewController(ViewController):
    CompanionLoadoutItemListPanelData: (Embed, 0x0, 0x0, LoadoutItemListPanelData)
    SearchbarText: (Hash, 0x0, 0x0, 0x0)
    SoundOnDeActivate: (String, 0x0, 0x0, 0x0)
    EquipButton: (Hash, 0x0, 0x0, 0x0)
    ArenaSkinLoadoutGridButtonData: (Embed, 0x0, 0x0, ArenaSkinLoadoutGridButtonData)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    StarShardsStoreDialog: (Hash, 0x0, 0x0, 0x0)
    0x6394d0ce: (Hash, 0x0, 0x0, 0x0)
    DamageSkinInfoPanel: (Embed, 0x0, 0x0, LoadoutDamageSkinInfoPanel)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    EmoteInfoPanel: (Embed, 0x0, 0x0, LoadoutEmoteInfoPanel)
    LoadoutScene: (Hash, 0x0, 0x0, 0x0)
    ArenaSkinLoadoutItemListPanelData: (Embed, 0x0, 0x0, LoadoutItemListPanelData)
    StarShardCurrencyWidget: (Embed, 0x0, 0x0, TftCurrencyWidget)
    StarShardCurrencyButton: (Hash, 0x0, 0x0, 0x0)
    SoundOnActivate: (String, 0x0, 0x0, 0x0)
    EmoteLoadoutItemListPanelData: (Embed, 0x0, 0x0, LoadoutItemListPanelData)
    CloseButton: (Hash, 0x0, 0x0, 0x0)
    GridItemButton: (Hash, 0x0, 0x0, 0x0)
    0xcee40baf: (Hash, 0x0, 0x0, 0x0)
    StarShardDecreaseVfx: (Hash, 0x0, 0x0, 0x0)
    0xd2bd41f4: (String, 0x0, 0x0, 0x0)
    CompanionInfoPanel: (Embed, 0x0, 0x0, LoadoutCompanionInfoPanel)
    UpgradeButton: (Hash, 0x0, 0x0, 0x0)
    EmoteLoadoutGridButtonData: (Embed, 0x0, 0x0, EmoteLoadoutGridButtonData)
    ArenaInfoPanel: (Embed, 0x0, 0x0, LoadoutArenaSkinInfoPanel)
    CompanionLoadoutGridButtonData: (Embed, 0x0, 0x0, CompanionLoadoutGridButtonData)
    0xf4fa4dd8: (List, 0x2, Hash, 0x0)
    DamageSkinLoadoutItemListPanelData: (Embed, 0x0, 0x0, LoadoutItemListPanelData)
    0xfaf537f0: (Hash, 0x0, 0x0, 0x0)
    DamageSkinLoadoutGridButtonData: (Embed, 0x0, 0x0, DamageSkinLoadoutGridButtonData)
    pass

class UiElementParticleSystemData(UiElementData):
    RenderAtElementLayer: (Bool, 0x0, 0x0, 0x0)
    TextureOverrides: (Map, Hash, String, 0x0)
    mRenderAtElementLayer: (Bool, 0x0, 0x0, 0x0)
    VfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    mVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    MaxPlayCount: (U32, 0x0, 0x0, 0x0)
    PlayDuringTransition: (Bool, 0x0, 0x0, 0x0)
    VfxAdjustmentScale: (F32, 0x0, 0x0, 0x0)
    mMaxPlayCount: (U32, 0x0, 0x0, 0x0)
    0xecef168c: (Bool, 0x0, 0x0, 0x0)
    pass

class HudButtonElements():
    Disabled: (Hash, 0x0, 0x0, 0x0)
    Clicked: (Hash, 0x0, 0x0, 0x0)
    Hover: (Hash, 0x0, 0x0, 0x0)
    Default: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xb1f9ca3c(ISequenceActionInstance):
    pass

class UObject(LogicDriverSource):
    pass

class 0xb2430347():
    ManagedLayout: (Hash, 0x0, 0x0, 0x0)
    BackgroundTexture: (Hash, 0x0, 0x0, 0x0)
    pass

class MapPlaceableContainer():
    Items: (Map, Hash, Pointer, MapPlaceable)
    Items: (Map, Hash, Pointer, MapPlaceableBase)
    pass

class 0xb26bd951():
    Units: (Map, Hash, Pointer, 0xb72a7d67)
    pass

class DecelToLocationMovement(AcceleratingMovement):
    pass

class OptionItemDropdown(IOptionItem):
    Items: (List, 0x0, Embed, OptionItemDropdownItem)
    TooltipTraKey: (String, 0x0, 0x0, 0x0)
    Template: (Hash, 0x0, 0x0, 0x0)
    LabelTraKey: (String, 0x0, 0x0, 0x0)
    Option: (U16, 0x0, 0x0, 0x0)
    pass

class LayoutStyleVerticalList(LayoutStyleBase):
    VerticalFillDirection: (U8, 0x0, 0x0, 0x0)
    ColumnHorizontalAlignment: (U8, 0x0, 0x0, 0x0)
    pass

class TooltipFormat():
    mOutputStrings: (Map, Hash, String, 0x0)
    mOutputStrings: (Map, String, String, 0x0)
    mListNames: (List, 0x0, String, 0x0)
    mListStyles: (Map, U32, String, 0x0)
    mListGridPrefix: (String, 0x0, 0x0, 0x0)
    mListTypeChoices: (Map, String, String, 0x0)
    mListGridSeparator: (String, 0x0, 0x0, 0x0)
    mListGridPostfix: (String, 0x0, 0x0, 0x0)
    mObjectName: (String, 0x0, 0x0, 0x0)
    mListValueSeparator: (String, 0x0, 0x0, 0x0)
    mInputLocKeysWithDefaults: (Map, Hash, String, 0x0)
    mInputLocKeysWithDefaults: (Map, String, String, 0x0)
    mUsesListValues: (Bool, 0x0, 0x0, 0x0)
    pass

class PfxFieldAttractionDefinitionData():
    Acceleration: (Embed, 0x0, 0x0, PfxAnimatedFloatVariableData)
    Position: (Embed, 0x0, 0x0, PfxAnimatedVector3fVariableData)
    Radius: (Embed, 0x0, 0x0, PfxAnimatedFloatVariableData)
    pass

class MatchHistoryPlayerTemplate():
    AugmentTitle: (String, 0x0, 0x0, 0x0)
    AugmentContainerIcon: (Hash, 0x0, 0x0, 0x0)
    AugmentContainerIconFrame: (Hash, 0x0, 0x0, 0x0)
    EmptyUnitGroup: (Hash, 0x0, 0x0, 0x0)
    TraitGrid: (Hash, 0x0, 0x0, 0x0)
    PlayerIcon: (Hash, 0x0, 0x0, 0x0)
    AugmentTooltipButton: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    PlacementText: (Hash, 0x0, 0x0, 0x0)
    AugmentIcons: (List, 0x3, Hash, 0x0)
    UnitGrid: (Hash, 0x0, 0x0, 0x0)
    MatchTypeDurationText: (Hash, 0x0, 0x0, 0x0)
    PlacementBanners: (List, 0x4, Hash, 0x0)
    MatchDateText: (Hash, 0x0, 0x0, 0x0)
    UnitCountText: (Hash, 0x0, 0x0, 0x0)
    pass

class TftEncounterSlotData():
    Description: (Hash, 0x0, 0x0, 0x0)
    Title: (Hash, 0x0, 0x0, 0x0)
    0x9a800d92: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    ActiveBackground: (Hash, 0x0, 0x0, 0x0)
    GroupLink: (Hash, 0x0, 0x0, 0x0)
    pass

class TftLobbyCustomAssets():
    0x19e7962f: (String, 0x0, 0x0, 0x0)
    0x6349b77b: (String, 0x0, 0x0, 0x0)
    CustomBackgroundTexturePath: (String, 0x0, 0x0, 0x0)
    0x90b42524: (String, 0x0, 0x0, 0x0)
    pass

class ItemDataValue():
    mName: (String, 0x0, 0x0, 0x0)
    mValue: (F32, 0x0, 0x0, 0x0)
    pass

class CharacterStealthData():
    StealthDatas: (List, 0x0, Embed, StealthData)
    pass

class BaseRigPoseModifierData():
    pass

class CursorData():
    mColorblindTextureName: (String, 0x0, 0x0, 0x0)
    mHotSpot: (Vec2, 0x0, 0x0, 0x0)
    mTargetChampionsOnlyTextureName: (String, 0x0, 0x0, 0x0)
    mColorblindTargetChampionsOnlyTextureName: (String, 0x0, 0x0, 0x0)
    mTextureName: (String, 0x0, 0x0, 0x0)
    pass

class DeathRecapShowcaseSlotMasteryData(DeathRecapShowcaseSlotData):
    Icon: (Hash, 0x0, 0x0, 0x0)
    DetailsText: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class FxActionMaterialAnimateInstance(IFxActionInstance):
    pass

class PurchaseDialogSubPurchaseHeaderElements():
    HeaderGroup: (Hash, 0x0, 0x0, 0x0)
    HeaderText: (Hash, 0x0, 0x0, 0x0)
    HeaderSpace: (Hash, 0x0, 0x0, 0x0)
    pass

class ILogicFloatDriver(ILogicDriver):
    pass

class PfxFieldAccelerationDefinitionData():
    Acceleration: (Embed, 0x0, 0x0, PfxAnimatedVector3fVariableData)
    IsLocalSpace: (Bool, 0x0, 0x0, 0x0)
    pass

class HudItemShopQuickBuyData():
    DefaultIndex: (I32, 0x0, 0x0, 0x0)
    Items: (List, 0x0, Hash, 0x0)
    NumberOfRows: (U32, 0x0, 0x0, 0x0)
    SwapData: (Embed, 0x0, 0x0, 0xd149dd3f)
    SortPopularToFront: (Bool, 0x0, 0x0, 0x0)
    ItemsPerRow: (U32, 0x0, 0x0, 0x0)
    pass

class TftCutsceneReportBone():
    BoneName: (String, 0x0, 0x0, 0x0)
    BlackboardName: (String, 0x0, 0x0, 0x0)
    pass

class HudEndOfGameData():
    mVictoryTransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mDefeatTransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    pass

class ChallengeConfigData():
    Id: (U64, 0x0, 0x0, 0x0)
    IconPath: (String, 0x0, 0x0, 0x0)
    LocalizedName: (String, 0x0, 0x0, 0x0)
    LocalizedShortDescription: (String, 0x0, 0x0, 0x0)
    LevelToIconPath: (Map, U32, String, 0x0)
    Tags: (Map, String, String, 0x0)
    LocalizedDescription: (String, 0x0, 0x0, 0x0)
    pass

class 0xb3674a86(TftGameStartSequenceSimpleObject):
    UiElement: (Hash, 0x0, 0x0, 0x0)
    pass

class MapAudioDataProperties():
    MobileMixEvent: (String, 0x0, 0x0, 0x0)
    PcMixEvent: (String, 0x0, 0x0, 0x0)
    Features: (List, 0x0, Embed, FeatureAudioDataProperties)
    Features: (List, 0x0, Link, FeatureAudioDataProperties)
    BaseData: (Link, 0x0, 0x0, MapAudioDataProperties)
    BankUnits: (List, 0x0, Embed, BankUnit)
    BankUnits: (List2, 0x0, Embed, BankUnit)
    pass

class JointSnapRigPoseModifilerData(BaseRigPoseModifierData):
    pass

class AbilityResourceTypeData():
    ThresholdIndicatorRanges: (List, 0x0, Embed, AbilityResourceThresholdIndicatorRange)
    ShowRegen: (Bool, 0x0, 0x0, 0x0)
    ShowAbilityResource: (Bool, 0x0, 0x0, 0x0)
    States: (List, 0x0, Embed, AbilityResourceStateData)
    pass

class MissileGroupSpawner():
    mChildMissileSpell: (Link, 0x0, 0x0, SpellObject)
    pass

class TooltipViewController(ViewController):
    PostScriptTitleElement: (Hash, 0x0, 0x0, 0x0)
    IconOverlayElement: (Hash, 0x0, 0x0, 0x0)
    PostScriptLeftElement: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    0x56716e4a: (String, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    HrBottom: (Hash, 0x0, 0x0, 0x0)
    MainTextElement: (Hash, 0x0, 0x0, 0x0)
    TitleRightElement: (Hash, 0x0, 0x0, 0x0)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    DefaultAdjustments: (Embed, 0x0, 0x0, PerLocaleTooltipAdjustments)
    TooltipPopupTimeout: (F32, 0x0, 0x0, 0x0)
    HrTopSubScene: (Hash, 0x0, 0x0, 0x0)
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    TooltipPopupDelayTime: (F32, 0x0, 0x0, 0x0)
    SubtitleLeftElement: (Hash, 0x0, 0x0, 0x0)
    IconElement: (Hash, 0x0, 0x0, 0x0)
    HrTop: (Hash, 0x0, 0x0, 0x0)
    PostScriptRightElement: (Hash, 0x0, 0x0, 0x0)
    HrBottomSubScene: (Hash, 0x0, 0x0, 0x0)
    SceneHandle: (Hash, 0x0, 0x0, 0x0)
    ClickAbsorbingRegionElement: (Hash, 0x0, 0x0, 0x0)
    SubtitleRightElement: (Hash, 0x0, 0x0, 0x0)
    TitleLeftElement: (Hash, 0x0, 0x0, 0x0)
    PerLocaleAdjustments: (Map, String, Embed, PerLocaleTooltipAdjustments)
    pass

class MapActionPlayAnimation(MapAction):
    ForceRestart: (Bool, 0x0, 0x0, 0x0)
    SkipIfModelInvisible: (Bool, 0x0, 0x0, 0x0)
    PropName: (String, 0x0, 0x0, 0x0)
    Looping: (Bool, 0x0, 0x0, 0x0)
    AnimationName: (String, 0x0, 0x0, 0x0)
    0xa4404f0c: (Bool, 0x0, 0x0, 0x0)
    pass

class UiMetricLaneMinionFlatDamageReductionFromMinion(UiMetricLaneMinionI):
    pass

class SummonerSpellPerkReplacementList():
    mReplacements: (List, 0x0, Pointer, SummonerSpellPerkReplacement)
    pass

class ToggleCameraHeightCheat(Cheat):
    pass

class HudKillCalloutTemplateData():
    Source: (Embed, 0x0, 0x0, HudCalloutIdentifier)
    0x1f03d8c: (Embed, 0x0, 0x0, HudCalloutIdentifier)
    EventIconAltarCapture: (Hash, 0x0, 0x0, 0x0)
    0x20e913e7: (Hash, 0x0, 0x0, 0x0)
    0x25799a22: (Hash, 0x0, 0x0, 0x0)
    Target: (Embed, 0x0, 0x0, HudCalloutIdentifier)
    0x40cfe5a8: (Hash, 0x0, 0x0, 0x0)
    SlotArea: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    GlobalSpellIcon: (Embed, 0x0, 0x0, HudCalloutIdentifier)
    0x848b3faa: (Hash, 0x0, 0x0, 0x0)
    EventIconKillNormal: (Hash, 0x0, 0x0, 0x0)
    EventIconKillBounty: (Hash, 0x0, 0x0, 0x0)
    EventIconKillShutdown: (Hash, 0x0, 0x0, 0x0)
    EventIconKillStreak: (Hash, 0x0, 0x0, 0x0)
    0xcef418bd: (Hash, 0x0, 0x0, 0x0)
    EventIconReviveAlly: (Hash, 0x0, 0x0, 0x0)
    Assisters: (List, 0x4, Embed, HudCalloutIdentifier)
    pass

class ContextualConditionCharacterHealth(ICharacterSubcondition):
    mCompareOp: (U8, 0x0, 0x0, 0x0)
    mTargetHealth: (F32, 0x0, 0x0, 0x0)
    pass

class 0xb3f382ff():
    AugmentSkin: (Link, 0x0, 0x0, SkinCharacterDataProperties)
    0x308bb787: (Hash, 0x0, 0x0, 0x0)
    Color: (Color, 0x0, 0x0, 0x0)
    LongDescriptionTra: (String, 0x0, 0x0, 0x0)
    Rarity: (U8, 0x0, 0x0, 0x0)
    Type: (U32, 0x0, 0x0, 0x0)
    RegionTra: (String, 0x0, 0x0, 0x0)
    IconPath: (String, 0x0, 0x0, 0x0)
    RegionName: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    BuffName: (String, 0x0, 0x0, 0x0)
    0x98f61e8c: (Bool, 0x0, 0x0, 0x0)
    0xafefa499: (Hash, 0x0, 0x0, 0x0)
    PortraitIconPath: (String, 0x0, 0x0, 0x0)
    ShortDescriptionTra: (String, 0x0, 0x0, 0x0)
    0xbe30f705: (Hash, 0x0, 0x0, 0x0)
    EffectAmounts: (List2, 0x0, Embed, TftEffectAmount)
    0xc397a6d5: (Hash, 0x0, 0x0, 0x0)
    0xca451de5: (List2, 0x0, Link, TftItemData)
    0xd25b1f2c: (Hash, 0x0, 0x0, 0x0)
    LocationTra: (String, 0x0, 0x0, 0x0)
    DescriptionTra: (String, 0x0, 0x0, 0x0)
    pass

class ObjectiveBountiesStatus():
    Background: (Hash, 0x0, 0x0, 0x0)
    OrderFilling: (Hash, 0x0, 0x0, 0x0)
    ChaosDecaying: (Hash, 0x0, 0x0, 0x0)
    TooltipAllyLocKey: (String, 0x0, 0x0, 0x0)
    TooltipEnemyLocKey: (String, 0x0, 0x0, 0x0)
    ChaosFilling: (Hash, 0x0, 0x0, 0x0)
    OrderDecaying: (Hash, 0x0, 0x0, 0x0)
    pass

class GameplayFeatureToggles():
    NewActorStuckPathfinding: (Bool, 0x0, 0x0, 0x0)
    VisibilityAnyToAny: (Bool, 0x0, 0x0, 0x0)
    FowCastRayAccurate: (Bool, 0x0, 0x0, 0x0)
    DisableSpellLevelMinimumProtections: (Bool, 0x0, 0x0, 0x0)
    TimerSyncForReplay: (Bool, 0x0, 0x0, 0x0)
    GridCheckFirstCell: (Bool, 0x0, 0x0, 0x0)
    IndividualItemVisibility: (Bool, 0x0, 0x0, 0x0)
    GridSkipFirstCell: (Bool, 0x0, 0x0, 0x0)
    AfkDetection2: (Bool, 0x0, 0x0, 0x0)
    LosNavGridAccurate: (Bool, 0x0, 0x0, 0x0)
    pass

class SkinFilterData():
    SkinIds: (List, 0x0, U32, 0x0)
    FilterType: (U32, 0x0, 0x0, 0x0)
    UseValidParentForChroma: (Bool, 0x0, 0x0, 0x0)
    pass

class GearData(BaseLoadoutData):
    mCharacterSubmeshesToShow: (List, 0x0, Hash, 0x0)
    mLockedToolTipTraKey: (String, 0x0, 0x0, 0x0)
    SkinMeshProperties: (Embed, 0x0, 0x0, SkinMeshDataProperties)
    mMinimapIcon: (String, 0x0, 0x0, 0x0)
    mVfxResourceResolver: (Pointer, 0x0, 0x0, ResourceResolver)
    mSelfOnlyPortraitIcon: (String, 0x0, 0x0, 0x0)
    mUiTexture: (String, 0x0, 0x0, 0x0)
    mAttachmentBone: (String, 0x0, 0x0, 0x0)
    EnableOverrideIdleParticles: (Bool, 0x0, 0x0, 0x0)
    EnableOverrideIdleEffects: (Bool, 0x0, 0x0, 0x0)
    SquarePortraitIcon: (String, 0x0, 0x0, 0x0)
    mToolTipTraKey: (String, 0x0, 0x0, 0x0)
    mPortraitIcon: (String, 0x0, 0x0, 0x0)
    mEquipAnimation: (String, 0x0, 0x0, 0x0)
    mCharacterSubmeshesToHide: (List, 0x0, Hash, 0x0)
    mAnimationGraphData: (Link, 0x0, 0x0, AnimationGraphData)
    OverrideIdleParticles: (List, 0x0, Embed, SkinCharacterDataProperties_CharacterIdleEffect)
    OverrideIdleEffects: (List, 0x0, Embed, SkinCharacterDataProperties_CharacterIdleEffect)
    AnimationGraphData: (Link, 0x0, 0x0, AnimationGraphData)
    pass

class ClientStateAudioDataProperties():
    ThemeMusic: (String, 0x0, 0x0, 0x0)
    BankPaths: (List, 0x0, String, 0x0)
    pass

class RotatingWaveBehavior(IMinionWaveBehavior):
    SpawnCountsByWave: (List2, 0x0, I32, 0x0)
    pass

class 0xb4517220():
    Complete: (Hash, 0x0, 0x0, 0x0)
    Active: (Hash, 0x0, 0x0, 0x0)
    Inactive: (Hash, 0x0, 0x0, 0x0)
    pass

class LogicDriverConditionalElementsEntry():
    Elements: (List, 0x0, Hash, 0x0)
    EnableCondition: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    pass

class IUiTextureDataProvider():
    pass

class ContextualConditionRuleCooldown(IContextualCondition):
    mRuleCooldown: (F32, 0x0, 0x0, 0x0)
    pass

class TftCutsceneArenaIntroInitializer(TftCutsceneInitializer, TftCutsceneArenaLocatorInitializer):
    LocatorBlackboardName: (String, 0x0, 0x0, 0x0)
    ArenaOwnerBlackboardName: (String, 0x0, 0x0, 0x0)
    PropNames: (List2, 0x0, Embed, TftCutsceneAddMapProp)
    IsLocatorArenaSpecific: (Bool, 0x0, 0x0, 0x0)
    CutscenePositionLocatorName: (String, 0x0, 0x0, 0x0)
    pass

class CastOnHitSpec(MissileBehaviorSpec):
    pass

class LerpMaterialDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    mTurnOffTimeSec: (F32, 0x0, 0x0, 0x0)
    mOnValue: (F32, 0x0, 0x0, 0x0)
    mTurnOnTimeSec: (F32, 0x0, 0x0, 0x0)
    mUseBrokenOldInterpolation: (Bool, 0x0, 0x0, 0x0)
    mBoolDriver: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    mBoolDriver: (Pointer, 0x0, 0x0, IDynamicMaterialBoolDriver)
    mOffValue: (F32, 0x0, 0x0, 0x0)
    pass

class SwitchIntPairData():
    Value: (I32, 0x0, 0x0, 0x0)
    ClipName: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xb4f87c91():
    0x8d18026: (Hash, 0x0, 0x0, 0x0)
    0x9b073937: (Hash, 0x0, 0x0, 0x0)
    0xa3da28b3: (Hash, 0x0, 0x0, 0x0)
    0xa927d8d6: (Hash, 0x0, 0x0, 0x0)
    Queue: (U8, 0x0, 0x0, 0x0)
    pass

class MapNavGridOverlays():
    Overlays: (List2, 0x0, Embed, MapNavGridOverlay)
    pass

class VfxChildParticleSetDefinitionData():
    BoneToSpawnAt: (List, 0x0, String, 0x0)
    ChildrenIdentifiers: (List, 0x0, Embed, VfxChildIdentifier)
    ChildEmitOnDeath: (Bool, 0x0, 0x0, 0x0)
    ParentInheritanceDefinition: (Pointer, 0x0, 0x0, VfxParentInheritanceParams)
    ChildrenName: (List, 0x0, String, 0x0)
    ChildrenProbability: (Embed, 0x0, 0x0, ValueFloat)
    ChildrenProbability: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    pass

class 0xb5215699(0xab5db4f2, 0xbc413e21):
    RadialElement: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xb53e2f1a():
    0x490b09: (U32, 0x0, 0x0, 0x0)
    0x54ccd262: (U32, 0x0, 0x0, 0x0)
    pass

class 0xb55e6cc4(0x64c18f7d):
    Duration: (F32, 0x0, 0x0, 0x0)
    TargetSkinScale: (F32, 0x0, 0x0, 0x0)
    pass

class TftCutsceneHidePlayerClip(TftCutsceneClip):
    SuppressVisibilityChanges: (Bool, 0x0, 0x0, 0x0)
    BlackboardPlayers: (List2, 0x0, String, 0x0)
    pass

class KeyFrameFloatMapClipAccessoryData(ClipAccessoryData):
    KeyFrameFloatmap: (Map, F32, F32, 0x0)
    pass

class StrawberryMapData(MapComponent):
    0x3e2cdad7: (List2, 0x0, Link, LolModesRoundsListData)
    0x7cf5e3eb: (Link, 0x0, 0x0, 0x276246d8)
    pass

class RegionBoundary(MapPlaceable):
    GroupIndex: (U32, 0x0, 0x0, 0x0)
    DrawHeight: (U32, 0x0, 0x0, 0x0)
    FillColor: (Color, 0x0, 0x0, 0x0)
    RenderInfo: (Link, 0x0, 0x0, 0x4664ae0a)
    InstanceParams: (Pointer, 0x0, 0x0, 0x76bc0857)
    RegionTag: (U32, 0x0, 0x0, 0x0)
    LineColor: (Color, 0x0, 0x0, 0x0)
    Vertices: (List2, 0x0, Vec3, 0x0)
    Priority: (F32, 0x0, 0x0, 0x0)
    ConfigOverride: (Pointer, 0x0, 0x0, RegionBoundaryConfig)
    NavGridOverlay: (Hash, 0x0, 0x0, 0x0)
    0xa9e6b95: (F32, 0x0, 0x0, 0x0)
    Margin: (F32, 0x0, 0x0, 0x0)
    NavigationGroup: (Link, 0x0, 0x0, NavigationGroup)
    pass

class SpellCalculation(ISpellCalculation):
    mFormulaParts: (List, 0x0, Pointer, ISpellCalculationPart)
    mDisplayAsPercent: (Bool, 0x0, 0x0, 0x0)
    mPrecision: (I32, 0x0, 0x0, 0x0)
    pass

class ToggleRegenCheat(Cheat):
    mToggleHp: (Bool, 0x0, 0x0, 0x0)
    mTogglePar: (Bool, 0x0, 0x0, 0x0)
    mTarget: (U32, 0x0, 0x0, 0x0)
    pass

class ToggleNetworkCheat(Cheat):
    pass

class JointSnapEventData(BaseEventData):
    Offset: (Vec3, 0x0, 0x0, 0x0)
    mJointToSnapToIdx: (U16, 0x0, 0x0, 0x0)
    mJointNameToOverride: (Hash, 0x0, 0x0, 0x0)
    mJointToOverrideIdx: (U16, 0x0, 0x0, 0x0)
    mJointNameToSnapTo: (Hash, 0x0, 0x0, 0x0)
    pass

class AtlasData3SliceH(AtlasDataBase):
    LeftRightWidths: (Vec2, 0x0, 0x0, 0x0)
    TextureUs: (Vec4, 0x0, 0x0, 0x0)
    TextureVs: (Vec2, 0x0, 0x0, 0x0)
    pass

class TftItemCodexHeaderData():
    MainItemName: (Hash, 0x0, 0x0, 0x0)
    MainItemIcon: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    MainItemBrief: (Hash, 0x0, 0x0, 0x0)
    MainItemMainText: (Hash, 0x0, 0x0, 0x0)
    pass

class IGameCalculationPartWithStats(IGameCalculationPart):
    mStat: (U8, 0x0, 0x0, 0x0)
    mStatFormula: (U8, 0x0, 0x0, 0x0)
    StatType: (U8, 0x0, 0x0, 0x0)
    OutputType: (U8, 0x0, 0x0, 0x0)
    UseNewStats: (Bool, 0x0, 0x0, 0x0)
    pass

class IGameCalculationPart():
    pass

class StrawberryHeroStatsViewController(PlayerStatsPanelViewController):
    BasicStats: (Hash, 0x0, 0x0, 0x0)
    AugmentSlots: (Embed, 0x0, 0x0, 0xfc331f53)
    Background: (Hash, 0x0, 0x0, 0x0)
    StatsUiData: (Embed, 0x0, 0x0, DisplayStatsUiData)
    pass

class CharScript(GameScript):
    pass

class 0xb62c8675(UiMetricTypeI):
    Scene: (Hash, 0x0, 0x0, 0x0)
    CrownIcons: (Embed, 0x0, 0x0, 0xa8c6f5f0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    0x462800b7: (Embed, 0x0, 0x0, 0xa8c6f5f0)
    MetersPanel: (Embed, 0x0, 0x0, 0xf43ad1ce)
    SorakaIcons: (Embed, 0x0, 0x0, 0xa8c6f5f0)
    TowerIcons: (Embed, 0x0, 0x0, 0xa8c6f5f0)
    0xb057cf4b: (U8, 0x0, 0x0, 0x0)
    DetailsPanel: (Embed, 0x0, 0x0, 0x7a19656)
    pass

class ModeSelectButtonData():
    ButtonIcons: (Embed, 0x0, 0x0, UiElementGroupButtonAdditionalElements)
    ButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    QueueId: (I64, 0x0, 0x0, 0x0)
    QueueId: (U16, 0x0, 0x0, 0x0)
    pass

class 0xb639bddc():
    HasBorder: (Bool, 0x0, 0x0, 0x0)
    NameOverride: (String, 0x0, 0x0, 0x0)
    IsKeystone: (Bool, 0x0, 0x0, 0x0)
    IsPremium: (Bool, 0x0, 0x0, 0x0)
    ImageOverride: (Hash, 0x0, 0x0, 0x0)
    Quanitity: (U32, 0x0, 0x0, 0x0)
    pass

class TftTrovesBannerActiveList():
    Banners: (List, 0x0, Link, TftTrovesBannerData)
    pass

class VfxFieldOrbitalDefinitionData():
    IsLocalSpace: (Bool, 0x0, 0x0, 0x0)
    Direction: (Embed, 0x0, 0x0, ValueVector3)
    Direction: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    pass

class LevelScriptOnLoad(ILevelScriptEvent):
    pass

class IFxAction():
    Disabled: (Bool, 0x0, 0x0, 0x0)
    Start: (Embed, 0x0, 0x0, FxTiming)
    End: (Embed, 0x0, 0x0, FxTiming)
    Timing: (Embed, 0x0, 0x0, FxTiming)
    pass

class HeroFloatingInfoIconData():
    Border: (Hash, 0x0, 0x0, 0x0)
    HighlightAnim: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionCharacterFormName(ICharacterSubcondition):
    mFormName: (String, 0x0, 0x0, 0x0)
    pass

class RsEqualCondition(IRsCondition):
    Value2: (Pointer, 0x0, 0x0, RsValueGet)
    Value1: (Pointer, 0x0, 0x0, RsValueGet)
    pass

class UiElementEffectCircleMaskCooldownData(UiElementEffectData):
    mEffectColor0: (Color, 0x0, 0x0, 0x0)
    mEffectColor1: (Color, 0x0, 0x0, 0x0)
    pass

class TftDamageSkinCeremony():
    MainCutscene: (Pointer, 0x0, 0x0, TftCutscene)
    0x918227c9: (Map, String, Pointer, TftCutscene)
    UnitCutscene: (Pointer, 0x0, 0x0, TftCutscene)
    pass

class TftPassWelcomeData():
    ConfirmButtonTraKey: (String, 0x0, 0x0, 0x0)
    SubtitleTraKey: (String, 0x0, 0x0, 0x0)
    TitleTrakey: (String, 0x0, 0x0, 0x0)
    BodyTraKey: (String, 0x0, 0x0, 0x0)
    pass

class StringHashGet(IStringHashGet):
    Value: (Hash, 0x0, 0x0, 0x0)
    pass

class Perk(BasePerk):
    mPingTextLocalizationKey: (String, 0x0, 0x0, 0x0)
    mEffectAmount: (List, 0x0, F32, 0x0)
    mDisplayNameLocalizationKey: (String, 0x0, 0x0, 0x0)
    mPerkId: (U32, 0x0, 0x0, 0x0)
    mTooltipNameLocalizationKey: (String, 0x0, 0x0, 0x0)
    mScript: (Link, 0x0, 0x0, PerkScript)
    mScript: (Pointer, 0x0, 0x0, PerkScript)
    mEnabled: (Bool, 0x0, 0x0, 0x0)
    mPerkName: (String, 0x0, 0x0, 0x0)
    mIconTextureName: (String, 0x0, 0x0, 0x0)
    mShortDescLocalizationKey: (String, 0x0, 0x0, 0x0)
    mVfxResourceResolver: (Pointer, 0x0, 0x0, ResourceResolver)
    mPerkScript: (String, 0x0, 0x0, 0x0)
    mType: (U32, 0x0, 0x0, 0x0)
    mLongDescLocalizationKey: (String, 0x0, 0x0, 0x0)
    mAffinities: (List, 0x0, Hash, 0x0)
    mMajorChangePatchVersion: (String, 0x0, 0x0, 0x0)
    mStackable: (Bool, 0x0, 0x0, 0x0)
    mDisplayStatLocalizationKey: (String, 0x0, 0x0, 0x0)
    mItemScript: (String, 0x0, 0x0, 0x0)
    mCharacters: (List, 0x0, String, 0x0)
    mDefault: (Bool, 0x0, 0x0, 0x0)
    mBuffs: (List, 0x0, Pointer, PerkBuff)
    mEndOfGameStatDescriptions: (List, 0x0, String, 0x0)
    mSummonerPerkReplacements: (Embed, 0x0, 0x0, SummonerSpellPerkReplacementList)
    pass

class 0xb6f43e50(ILogicFloatDriver):
    StartFloat: (F32, 0x0, 0x0, 0x0)
    0x5fdb41c2: (Hash, 0x0, 0x0, 0x0)
    0xba092281: (Bool, 0x0, 0x0, 0x0)
    pass

class ScissorRegionElementData(UiElementData, BaseElementData):
    mSceneToScissor: (Link, 0x0, 0x0, SceneData)
    pass

class SeasonalSinglePurchaseDialog(PurchaseDialogBase):
    SingleTitleText: (Hash, 0x0, 0x0, 0x0)
    SinglePurchaseItemIcon: (Hash, 0x0, 0x0, 0x0)
    SingleCloseButtonRegion: (Hash, 0x0, 0x0, 0x0)
    SingleScene: (Hash, 0x0, 0x0, 0x0)
    SingleBodyText: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xb72a7d67():
    CharacterRecord: (String, 0x0, 0x0, 0x0)
    0x397fe037: (Bool, 0x0, 0x0, 0x0)
    LuaScript: (String, 0x0, 0x0, 0x0)
    Skins: (Map, U32, Embed, 0xb979c2f)
    0xbd69e44b: (U32, 0x0, 0x0, 0x0)
    CharacterNameOverride: (String, 0x0, 0x0, 0x0)
    pass

class FxCategory():
    Name: (String, 0x0, 0x0, 0x0)
    Hash: (Hash, 0x0, 0x0, 0x0)
    Phases: (List, 0x0, Embed, FxPhase)
    pass

class 0xb76d3e91(TargetingTypeData):
    pass

class 0xb774f0fe(IFxAction):
    Material: (Link, 0x0, 0x0, StaticMaterialDef)
    pass

class MaterialSwitchDataCollection():
    Entries: (Map, String, Embed, IdMappingEntry)
    NextId: (U16, 0x0, 0x0, 0x0)
    Data: (Map, U16, Embed, MaterialSwitchData)
    0xea57bf12: (String, 0x0, 0x0, 0x0)
    pass

class CreateNeutralCamp(LevelScriptBlock):
    MinimapIcon: (String, 0x0, 0x0, 0x0)
    FacingLocation: (Pointer, 0x0, 0x0, IVectorGet)
    SpawnBehavior: (Pointer, 0x0, 0x0, INeutralCampSpawnBehavior)
    SpawnDurationSecs: (Pointer, 0x0, 0x0, IFloatGet)
    MinimapIconOffset: (Pointer, 0x0, 0x0, IVectorGet)
    StopSpawnTimeSecs: (Pointer, 0x0, 0x0, IFloatGet)
    RespawnDelaySecs: (Pointer, 0x0, 0x0, IFloatGet)
    0x7633e7cf: (Pointer, 0x0, 0x0, IVectorGet)
    0x7d27af7f: (Bool, 0x0, 0x0, 0x0)
    Name: (Hash, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    RevealEvent: (U16, 0x0, 0x0, 0x0)
    InitialSpawnTime: (Pointer, 0x0, 0x0, IFloatGet)
    ScoreboardTimer: (U16, 0x0, 0x0, 0x0)
    0x9ab1e29d: (Pointer, 0x0, 0x0, IBoolGet)
    CampLevel: (U16, 0x0, 0x0, 0x0)
    Team: (U32, 0x0, 0x0, 0x0)
    MaxSpawnLimit: (Pointer, 0x0, 0x0, IIntGet)
    Location: (Pointer, 0x0, 0x0, IVectorGet)
    LeashRadius: (Pointer, 0x0, 0x0, IFloatGet)
    OutCampId: (Embed, 0x0, 0x0, IntTableSet)
    pass

class AbilitiesUiData():
    CustomUiData: (Hash, 0x0, 0x0, 0x0)
    SpellRankPips: (Pointer, 0x0, 0x0, SpellRankPipsUiData)
    SpellRankText: (Pointer, 0x0, 0x0, SpellRankTextUiData)
    SpellPips: (List, 0x4, Embed, SpellPipsUiData)
    CustomAbilities: (Pointer, 0x0, 0x0, CustomAbilitiesUiData)
    RankText: (List, 0x4, Hash, 0x0)
    ChampionSpells: (List, 0x4, Embed, SpellSlotDetailedUiDefinition)
    Passive: (Embed, 0x0, 0x0, SpellSlotDetailedUiDefinition)
    SummonerSpells: (List, 0x2, Embed, SpellSlotDetailedUiDefinition)
    pass

class 0xb7b2875(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    RewardLayout: (Hash, 0x0, 0x0, 0x0)
    SceneRoot: (Hash, 0x0, 0x0, 0x0)
    CloseButton: (Hash, 0x0, 0x0, 0x0)
    0xcbfa2678: (Embed, 0x0, 0x0, 0x7638f87c)
    0xcbfa2678: (Embed, 0x0, 0x0, 0xc993142a)
    pass

class 0xb7b9b55b(0x2bde0c9c):
    0x385d61fd: (Bool, 0x0, 0x0, 0x0)
    0x6db9cb34: (String, 0x0, 0x0, 0x0)
    pass

class ISequenceLocation():
    Transform: (Mtx44, 0x0, 0x0, 0x0)
    pass

class StatFormulaData():
    StatComponents: (Map, U8, F32, 0x0)
    pass

class IsHomeguardParametricUpdater(IBooleanParametricUpdater):
    pass

class TftArmoryStyleData():
    UseBorderedIcon: (Bool, 0x0, 0x0, 0x0)
    ItemButton: (Hash, 0x0, 0x0, 0x0)
    ButtonStyle: (Embed, 0x0, 0x0, TftArmoryButtonStyleData)
    Background: (Hash, 0x0, 0x0, 0x0)
    ItemTag: (String, 0x0, 0x0, 0x0)
    Title: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualActionPlayAnimation(IContextualAction):
    mHashedAnimationName: (Hash, 0x0, 0x0, 0x0)
    mPlayAsEmote: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xb8998b83():
    mEventList: (List, 0x0, String, 0x0)
    pass

class 0xb8a49c96():
    RedSkin: (Hash, 0x0, 0x0, 0x0)
    BlueSkin: (Hash, 0x0, 0x0, 0x0)
    Meter: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionBuffCounterReachedLimitFromZero(IContextualConditionBuff):
    mCounterHighestReached: (U8, 0x0, 0x0, 0x0)
    mBuff: (Hash, 0x0, 0x0, 0x0)
    pass

class HasLossOfControlTypeBoolDriver(ILogicBoolDriver):
    LossOfControlType: (U32, 0x0, 0x0, 0x0)
    pass

class 0xb8eb241b(Rscript):
    Sequences: (Map, U32, Embed, ScriptSequence)
    pass

class HudScoreboardTransitionData():
    TransitionTime: (F32, 0x0, 0x0, 0x0)
    MinAlpha: (U8, 0x0, 0x0, 0x0)
    MaxAlpha: (U8, 0x0, 0x0, 0x0)
    pass

class TftSlotObject(AiBaseClient):
    pass

class TriggerOnDelay(MissileTriggerSpec):
    mDelay: (F32, 0x0, 0x0, 0x0)
    pass

class 0xb979c2f():
    Skin: (String, 0x0, 0x0, 0x0)
    pass

class IntTableGet(RsTableGet, ScriptTableGet, TableGet, IIntGet):
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Var: (Hash, 0x0, 0x0, 0x0)
    Var: (String, 0x0, 0x0, 0x0)
    Default: (Option, 0x0, I32, 0x0)
    pass

class UnrevealedTarget(GameObject):
    pass

class HybridMaterialDef(CustomShaderDef):
    SrcColorBlendFactor: (U8, 0x0, 0x0, 0x0)
    BlendEnable: (Bool, 0x0, 0x0, 0x0)
    DepthOffsetSlope: (F32, 0x0, 0x0, 0x0)
    StencilEnable: (Bool, 0x0, 0x0, 0x0)
    CullEnable: (Bool, 0x0, 0x0, 0x0)
    WindingToCull: (U8, 0x0, 0x0, 0x0)
    Type: (U32, 0x0, 0x0, 0x0)
    StencilPassDepthPassOp: (U8, 0x0, 0x0, 0x0)
    DstAlphaBlendFactor: (U8, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    BlendEquation: (U8, 0x0, 0x0, 0x0)
    StencilCompareFunc: (U8, 0x0, 0x0, 0x0)
    SrcAlphaBlendFactor: (U8, 0x0, 0x0, 0x0)
    DepthCompareFunc: (U8, 0x0, 0x0, 0x0)
    DataCollections: (Embed, 0x0, 0x0, MaterialDataCollections)
    StencilPassDepthFailOp: (U8, 0x0, 0x0, 0x0)
    StencilMask: (U32, 0x0, 0x0, 0x0)
    WriteMask: (U8, 0x0, 0x0, 0x0)
    DstColorBlendFactor: (U8, 0x0, 0x0, 0x0)
    StencilReferenceVal: (U32, 0x0, 0x0, 0x0)
    DepthEnable: (Bool, 0x0, 0x0, 0x0)
    StencilFailOp: (U8, 0x0, 0x0, 0x0)
    ShaderMacros: (Map, String, String, 0x0)
    Preset: (Link, 0x0, 0x0, HybridMaterialDefPreset)
    DepthOffsetBias: (F32, 0x0, 0x0, 0x0)
    pass

class 0xb9b1bd74(MapComponent):
    CutsceneEntries: (Map, Hash, Link, TftCutscene)
    pass

class TftGameStartSequence():
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    pass

class FloatingTextDamageDisplayTypeList():
    Impact: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    Ult: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    Zone: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    SelfPhysicalDamageCounter: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    Multistrike: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    SelfMagicalDamageCounter: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    MultistrikeFast: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    Mini: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    SelfTrueDamageCounter: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    Default: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    BarrackMinion: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    MultistrikeSlow: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    PlayerMinion: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    DotParentMissile: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    Dot: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    DotSlow: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    DotNoCombine: (Link, 0x0, 0x0, FloatTextDisplayOverrides)
    pass

class BaseHealthbarData():
    mTimerBar: (Pointer, 0x0, 0x0, BarElement)
    mLevelText: (Pointer, 0x0, 0x0, LabelElement)
    mChatBubble: (Pointer, 0x0, 0x0, BackdropElement)
    mHealthBarBreakpoints: (List, 0x0, Link, HealthbarBreakpoint)
    mHealthBar: (Pointer, 0x0, 0x0, BarElement)
    SecondaryAbilityResourceBar: (Pointer, 0x0, 0x0, BarElement)
    mHealthText: (Pointer, 0x0, 0x0, LabelElement)
    mUnitStatusIndicator: (Pointer, 0x0, 0x0, UnitStatusIndicator)
    mNameText: (Pointer, 0x0, 0x0, LabelElement)
    mSettingsData: (Link, 0x0, 0x0, HealthBarSettingsData)
    mLossOfControlIndicator: (Pointer, 0x0, 0x0, LossOfControlIndicator)
    mClubText: (Pointer, 0x0, 0x0, LabelElement)
    mUnitStatusText: (Pointer, 0x0, 0x0, LabelElement)
    mShieldParams: (Link, 0x0, 0x0, ShieldParams)
    mBountyIndicator: (Pointer, 0x0, 0x0, BountyIndicator)
    mParBar: (Pointer, 0x0, 0x0, BarElement)
    mDefenseModifiers: (Pointer, 0x0, 0x0, DefenseModifierIcons)
    mIconSettings: (Link, 0x0, 0x0, HealthBarIconSettings)
    PrimaryAbilityResourceBar: (Pointer, 0x0, 0x0, BarElement)
    mAggroIndicator: (Pointer, 0x0, 0x0, 0x16b1df95)
    mBackdrop: (Pointer, 0x0, 0x0, BackdropElement)
    mPercentageOffset: (Vec2, 0x0, 0x0, 0x0)
    mMidHorizontalScaling: (F32, 0x0, 0x0, 0x0)
    mHealthMaxPenaltyBar: (Pointer, 0x0, 0x0, BarElement)
    pass

class 0xb9f51fac(IScriptBlock, IBehaviorScriptBlock):
    LeftValue: (Embed, 0x0, 0x0, IntGet)
    LeftValue: (Pointer, 0x0, 0x0, IFloatGet)
    RightValue: (Embed, 0x0, 0x0, IntGet)
    RightValue: (Pointer, 0x0, 0x0, IFloatGet)
    pass

class FontResolution():
    ShadowDepthX: (I32, 0x0, 0x0, 0x0)
    ShadowDepthY: (I32, 0x0, 0x0, 0x0)
    OutlineSize: (U32, 0x0, 0x0, 0x0)
    FontSize: (U32, 0x0, 0x0, 0x0)
    ScreenHeight: (U32, 0x0, 0x0, 0x0)
    pass

class IBehaviorScriptBlock(IScriptBlock):
    pass

class PlayerReportViewController(ViewController):
    ReportNegativeAttitudeButton: (Hash, 0x0, 0x0, 0x0)
    ChampionIconLink: (Hash, 0x0, 0x0, 0x0)
    CloseRegion: (Hash, 0x0, 0x0, 0x0)
    ReportVerbalAbuseButton: (Hash, 0x0, 0x0, 0x0)
    ChampionNameLink: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    ReportCheatingButton: (Hash, 0x0, 0x0, 0x0)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    SummonerNameLink: (Hash, 0x0, 0x0, 0x0)
    BackgroundLink: (Hash, 0x0, 0x0, 0x0)
    ReportLeavingTheGameButton: (Hash, 0x0, 0x0, 0x0)
    SubmitReportButton: (Hash, 0x0, 0x0, 0x0)
    CloseRegionScene: (Hash, 0x0, 0x0, 0x0)
    MenuCloseButton: (Hash, 0x0, 0x0, 0x0)
    ReportIntentionalFeedingButton: (Hash, 0x0, 0x0, 0x0)
    DragRegion: (Hash, 0x0, 0x0, 0x0)
    ReportOffensiveNameButton: (Hash, 0x0, 0x0, 0x0)
    pass

class PerkSubStyleBonus():
    mPerk: (Link, 0x0, 0x0, Perk)
    mStyleId: (U32, 0x0, 0x0, 0x0)
    pass

class TftCutsceneProxyClip(TftCutsceneClip):
    EnableVfx: (Bool, 0x0, 0x0, 0x0)
    BlackboardGameObjectProxy: (String, 0x0, 0x0, 0x0)
    BlackboardGameObjectOriginal: (String, 0x0, 0x0, 0x0)
    pass

class VfxShapeBox(VfxShapeVolume):
    Size: (Vec3, 0x0, 0x0, 0x0)
    pass

class 0xba9f6aca():
    0x439b26dc: (String, 0x0, 0x0, 0x0)
    TroveBannerIcon: (Hash, 0x0, 0x0, 0x0)
    FailureText: (String, 0x0, 0x0, 0x0)
    0xabd0de07: (String, 0x0, 0x0, 0x0)
    FailureTexturePath: (String, 0x0, 0x0, 0x0)
    TroveNameText: (Hash, 0x0, 0x0, 0x0)
    TroveButton: (Hash, 0x0, 0x0, 0x0)
    pass

class TftCraftingCelebrationViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    0x22c15c3b: (String, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    CraftingSequence: (Link, 0x0, 0x0, Sequence)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    0x7cbd3f05: (Hash, 0x0, 0x0, 0x0)
    ContinueButton: (Hash, 0x0, 0x0, 0x0)
    0x923b6b2e: (Link, 0x0, 0x0, SequenceObjectSelector)
    pass

class UiMetricTeamBuffExists(UiMetricTypeI):
    Team2IconSlots: (List, 0x6, Hash, 0x0)
    Team1IconSlots: (List, 0x6, Hash, 0x0)
    Team2BuffIcons: (List, 0xa, Hash, 0x0)
    Team1BuffIcons: (List, 0xa, Hash, 0x0)
    pass

class Rscript():
    Path: (Hash, 0x0, 0x0, 0x0)
    ScriptName: (String, 0x0, 0x0, 0x0)
    pass

class TftHudTraitUnitSlotData():
    UnitIcon: (Hash, 0x0, 0x0, 0x0)
    BorderLevelSix: (Hash, 0x0, 0x0, 0x0)
    Border: (Hash, 0x0, 0x0, 0x0)
    Corner: (Hash, 0x0, 0x0, 0x0)
    Region: (Hash, 0x0, 0x0, 0x0)
    UnitSceneLink: (Hash, 0x0, 0x0, 0x0)
    Padding: (Hash, 0x0, 0x0, 0x0)
    BorderLevelThree: (Hash, 0x0, 0x0, 0x0)
    BorderLevelFour: (Hash, 0x0, 0x0, 0x0)
    BorderLevelTwo: (Hash, 0x0, 0x0, 0x0)
    BorderLevelFive: (Hash, 0x0, 0x0, 0x0)
    UnitShade: (Hash, 0x0, 0x0, 0x0)
    BorderLevelOne: (Hash, 0x0, 0x0, 0x0)
    UnitGroupLink: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xbaf9ac75():
    0xf128c9be: (Map, U32, Embed, 0x3b2ba6c0)
    0xfab10bb2: (String, 0x0, 0x0, 0x0)
    pass

class LevelControllerManager():
    Controllers: (List, 0x0, Link, ILevelController)
    Controllers: (List, 0x0, Link, BaseLevelController)
    pass

class 0xbafc3e15(0x67c526d3):
    ValueName: (String, 0x0, 0x0, 0x0)
    SpellLevel: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class 0xbb06bf0a():
    mEnabled: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xbb1b4a24(IGameModeConfig):
    0x2201df0d: (F32, 0x0, 0x0, 0x0)
    0x2da316cf: (I32, 0x0, 0x0, 0x0)
    0x43ea990b: (F32, 0x0, 0x0, 0x0)
    0x57cf56ee: (F32, 0x0, 0x0, 0x0)
    0x5a9d5fc: (F32, 0x0, 0x0, 0x0)
    0xa9cd4429: (F32, 0x0, 0x0, 0x0)
    0xaebc7445: (F32, 0x0, 0x0, 0x0)
    0xb3cbe7eb: (F32, 0x0, 0x0, 0x0)
    0xb73da134: (F32, 0x0, 0x0, 0x0)
    0xd55e5eb7: (F32, 0x0, 0x0, 0x0)
    0xe89de4e3: (U32, 0x0, 0x0, 0x0)
    0xfb77eb31: (F32, 0x0, 0x0, 0x0)
    pass

class UnitStatsUiData():
    BasicStats: (Map, U8, Embed, UnitStatUiData)
    NewStats: (Map, U8, Embed, UnitStatUiData)
    AdvancedStats: (Map, U8, Embed, UnitStatUiData)
    pass

class ConcatenateStringsBlock(IScriptBlock, IFunctionalScriptBlock):
    String1: (Pointer, 0x0, 0x0, IStringGet)
    String2: (Pointer, 0x0, 0x0, IStringGet)
    Result: (Embed, 0x0, 0x0, StringTableSet)
    pass

class OptionItemSecondaryHotkeys1Column(IOptionItem):
    Rows: (List, 0x0, Embed, OptionItemSecondaryHotkeys1Column_Row)
    Template: (Hash, 0x0, 0x0, 0x0)
    Header: (Embed, 0x0, 0x0, OptionItemSecondaryHotkeys1Column_Header)
    pass

class TriggerOnMovementComplete(MissileTriggerSpec):
    mDelay: (I32, 0x0, 0x0, 0x0)
    pass

class ViewControllerListFilter_Clash(ViewControllerListFilterI):
    pass

class CherryCameoList(IGameModeConfig):
    CameoList: (List, 0x0, Link, CherryCameo)
    pass

class 0xbbac8ee0():
    0x4e3b1910: (Pointer, 0x0, 0x0, 0x8bb623e8)
    RuleId: (String, 0x0, 0x0, 0x0)
    0x876b6bd0: (String, 0x0, 0x0, 0x0)
    ActionType: (U32, 0x0, 0x0, 0x0)
    pass

class BoolTableGet(RsTableGet, ScriptTableGet, TableGet, IBoolGet):
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Var: (Hash, 0x0, 0x0, 0x0)
    Var: (String, 0x0, 0x0, 0x0)
    Default: (Option, 0x0, Bool, 0x0)
    pass

class ProgressionNodeData():
    0xbd372927: (List, 0x0, Link, BaseLoadoutData)
    BuffScriptPath: (String, 0x0, 0x0, 0x0)
    pass

class UiTeamFightOffScreenDifferentiationData():
    PlayerOffscreenTimer: (F32, 0x0, 0x0, 0x0)
    PlayerOffscreenAlphaValue: (U8, 0x0, 0x0, 0x0)
    NearlyOnScreenRange: (F32, 0x0, 0x0, 0x0)
    pass

class EventControlledSelectorClipData(ClipBaseData):
    PlayAnimChangeFromBeginning: (Bool, 0x0, 0x0, 0x0)
    ChangeAnimationMidPlay: (Bool, 0x0, 0x0, 0x0)
    ChildAnimDelaySwitchTime: (F32, 0x0, 0x0, 0x0)
    DontStompTransitionClip: (Bool, 0x0, 0x0, 0x0)
    SyncFrameOnChangeAnim: (Bool, 0x0, 0x0, 0x0)
    DefaultClipName: (Hash, 0x0, 0x0, 0x0)
    SelectorPairDataList: (List, 0x0, Embed, EventControlledSelectorPairData)
    pass

class PingRadialBaseCategoryDefinition():
    CategoryText: (Hash, 0x0, 0x0, 0x0)
    PingCategory: (U8, 0x0, 0x0, 0x0)
    pass

class VfxFieldCollectionDefinitionData():
    FieldAccelerationDefinitions: (List, 0x0, Embed, VfxFieldAccelerationDefinitionData)
    FieldOrbitalDefinitions: (List, 0x0, Embed, VfxFieldOrbitalDefinitionData)
    FieldDragDefinitions: (List, 0x0, Embed, VfxFieldDragDefinitionData)
    FieldAttractionDefinitions: (List, 0x0, Embed, VfxFieldAttractionDefinitionData)
    FieldNoiseDefinitions: (List, 0x0, Embed, VfxFieldNoiseDefinitionData)
    pass

class IShaderDef():
    FeatureMask: (U32, 0x0, 0x0, 0x0)
    StaticSwitches: (List, 0x0, Embed, ShaderStaticSwitch)
    Parameters: (List, 0x0, Embed, ShaderPhysicalParameter)
    ShadingModel: (Link, 0x0, 0x0, 0x38a77cab)
    ShadingModel: (Link, 0x0, 0x0, IX3dShadingModel)
    Textures: (List, 0x0, Embed, ShaderTexture)
    AdditionalUvSetMask: (U32, 0x0, 0x0, 0x0)
    FeatureDefines: (Map, String, String, 0x0)
    pass

class RadialMenuButtonDefinitionBase():
    DefaultIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class ItemSlotHasChargesCastRequirement(ICastRequirement):
    pass

class OptionsViewController(ViewController):
    SurrenderHitRegion: (Hash, 0x0, 0x0, 0x0)
    CloseButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    MobileMenuButtonTraKeys: (List, 0x6, String, 0x0)
    TabButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    KoreaRatingsIconElement: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    Button2Definition: (Hash, 0x0, 0x0, 0x0)
    DefaultMenuButtonTraKeys: (List, 0x6, String, 0x0)
    ViewPaneDefinition: (Embed, 0x0, 0x0, ViewPaneDefinition)
    ExitHitRegion: (Hash, 0x0, 0x0, 0x0)
    Button1Definition: (Hash, 0x0, 0x0, 0x0)
    Tabs: (List, 0x0, Link, OptionsTab)
    CancelHitRegion: (Hash, 0x0, 0x0, 0x0)
    OkayHitRegion: (Hash, 0x0, 0x0, 0x0)
    ViewPaneLink: (Hash, 0x0, 0x0, 0x0)
    LastItemPadding: (Hash, 0x0, 0x0, 0x0)
    RestoreDefaultsHitRegion: (Hash, 0x0, 0x0, 0x0)
    OptionsStyle: (U8, 0x0, 0x0, 0x0)
    pass

class IOptionTemplate():
    BoundsElement: (Hash, 0x0, 0x0, 0x0)
    pass

class HomeViewSpecialOffer():
    SpecialOfferButton: (Hash, 0x0, 0x0, 0x0)
    StoreListingData: (Link, 0x0, 0x0, StoreListingData)
    0x9028d1ed: (Bool, 0x0, 0x0, 0x0)
    SpecialOfferToastScene: (Hash, 0x0, 0x0, 0x0)
    0xf3d15b7: (Hash, 0x0, 0x0, 0x0)
    pass

class StatStoneCategory():
    GameIconMini: (String, 0x0, 0x0, 0x0)
    EpicGameIcon: (String, 0x0, 0x0, 0x0)
    RareGameIconLit: (String, 0x0, 0x0, 0x0)
    GameIconLit: (String, 0x0, 0x0, 0x0)
    0x77c1219b: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    RareGameIconUnlit: (String, 0x0, 0x0, 0x0)
    0xb0ff0124: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    EpicGameIconFull: (String, 0x0, 0x0, 0x0)
    RareGameIcon: (String, 0x0, 0x0, 0x0)
    EpicGameIconUnlit: (String, 0x0, 0x0, 0x0)
    GameIconFull: (String, 0x0, 0x0, 0x0)
    RareGameIconFull: (String, 0x0, 0x0, 0x0)
    EpicGameIconLit: (String, 0x0, 0x0, 0x0)
    GameIconUnlit: (String, 0x0, 0x0, 0x0)
    CategoryColor: (Color, 0x0, 0x0, 0x0)
    pass

class 0xbc280d0a():
    pass

class GameCalculation(IGameCalculation):
    mFormulaParts: (List, 0x0, Pointer, IGameCalculationPart)
    mDisplayAsPercent: (Bool, 0x0, 0x0, 0x0)
    mPrecision: (I32, 0x0, 0x0, 0x0)
    pass

class 0xbc413e21(0x53de4f74):
    pass

class SpellRankUpRequirements():
    mRequirements: (List, 0x0, Pointer, ISpellRankUpRequirement)
    pass

class ChampionSpecificStatStoneData(StatStoneData):
    0x12a4a857: (Hash, 0x0, 0x0, 0x0)
    ParentObject: (Link, 0x0, 0x0, ChampionSpecificStatStoneData)
    mChampionEvent: (Hash, 0x0, 0x0, 0x0)
    mChampionEvent: (String, 0x0, 0x0, 0x0)
    mChampionEvent: (U32, 0x0, 0x0, 0x0)
    0x9ea543e4: (Bool, 0x0, 0x0, 0x0)
    pass

class SwitchIntClipData(ClipBaseData):
    PlayAnimChangeFromBeginning: (Bool, 0x0, 0x0, 0x0)
    SwitchIntPairDataList: (List, 0x0, Embed, SwitchIntPairData)
    ChangeAnimationMidPlay: (Bool, 0x0, 0x0, 0x0)
    ChildAnimDelaySwitchTime: (F32, 0x0, 0x0, 0x0)
    DontStompTransitionClip: (Bool, 0x0, 0x0, 0x0)
    SyncFrameOnChangeAnim: (Bool, 0x0, 0x0, 0x0)
    Driver: (Pointer, 0x0, 0x0, ILogicIntDriver)
    pass

class SetVarInTableBlock(IScriptBlock, IFunctionalScriptBlock, IBehaviorScriptBlock):
    Value: (Pointer, 0x0, 0x0, IScriptValueGet)
    Dest: (Embed, 0x0, 0x0, ScriptTableSet)
    Src: (Pointer, 0x0, 0x0, IScriptValueGet)
    pass

class TargeterDefinitionArc(TargeterDefinition):
    EndLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    IsClockwiseArc: (Bool, 0x0, 0x0, 0x0)
    ThicknessOffset: (F32, 0x0, 0x0, 0x0)
    ConstraintRange: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    ConstraintRange: (F32, 0x0, 0x0, 0x0)
    IsConstrainedToRange: (Bool, 0x0, 0x0, 0x0)
    TextureArcOverrideName: (String, 0x0, 0x0, 0x0)
    OverrideRadius: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    StartLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    pass

class HasSkinIdSpawnConditions(IVfxSpawnConditions):
    mConditions: (List, 0x0, Embed, IsSkinSpawnConditionData)
    mDefaultVfxData: (Embed, 0x0, 0x0, VfxDefaultSpawnConditionData)
    pass

class ParticleWadFileDescriptor(WadFileDescriptor):
    pass

class ReplayTeamFightViewController(TeamFightViewController):
    pass

class OptionTemplateHotkeysKey():
    EventName: (String, 0x0, 0x0, 0x0)
    EventNameTraKey: (String, 0x0, 0x0, 0x0)
    Position: (Hash, 0x0, 0x0, 0x0)
    pass

class TftCutscenePostFxClip(TftCutsceneBasePostFxClip, TftCutsceneClip):
    PostFxPriority: (U8, 0x0, 0x0, 0x0)
    BlendOutTime: (F32, 0x0, 0x0, 0x0)
    BlendInTime: (F32, 0x0, 0x0, 0x0)
    EffectKey: (String, 0x0, 0x0, 0x0)
    BlackboardEffectSource: (String, 0x0, 0x0, 0x0)
    BlackboardAssociatedPlayers: (List2, 0x0, String, 0x0)
    pass

class GameplayConfig():
    mCritBonusArmorPenPercent: (F32, 0x0, 0x0, 0x0)
    mBasicAttackCalculation: (Pointer, 0x0, 0x0, IGameCalculation)
    mLegacySummonerSpells: (List, 0x0, Hash, 0x0)
    mLethalityRatioFromAttacker: (F32, 0x0, 0x0, 0x0)
    mLethalityPercentGivenAtLevel0: (F32, 0x0, 0x0, 0x0)
    mLethalityScalesCapsAtLevel: (I32, 0x0, 0x0, 0x0)
    mMinionAutoLeeway: (F32, 0x0, 0x0, 0x0)
    mPerkRootSpellOrigination: (Hash, 0x0, 0x0, 0x0)
    mCritTotalArmorPenPercent: (F32, 0x0, 0x0, 0x0)
    mCcScoreMultipliers: (Embed, 0x0, 0x0, CcScoreMultipliers)
    mCritGlobalDamageMultiplier: (F32, 0x0, 0x0, 0x0)
    mSpellPostponeTimeoutSec: (F32, 0x0, 0x0, 0x0)
    mMinionDeathDelay: (F32, 0x0, 0x0, 0x0)
    mLethalityScalesToLevel: (I32, 0x0, 0x0, 0x0)
    mCooldownQueueThreshold: (F32, 0x0, 0x0, 0x0)
    mAutoAttackMinPreCastLockoutDeltaTimeSec: (F32, 0x0, 0x0, 0x0)
    mMinionAaHelperLimit: (F32, 0x0, 0x0, 0x0)
    mItemSellQueueTime: (F32, 0x0, 0x0, 0x0)
    mAdaptiveForceAttackDamageScale: (F32, 0x0, 0x0, 0x0)
    mItemRootSpellOrigination: (Hash, 0x0, 0x0, 0x0)
    mSummonerSpells: (List, 0x0, Hash, 0x0)
    mAdaptiveForceAbilityPowerScale: (F32, 0x0, 0x0, 0x0)
    ExtendedVisibilityDuration: (F32, 0x0, 0x0, 0x0)
    AbilityHasteMax: (F32, 0x0, 0x0, 0x0)
    mAutoAttackMinPostCastLockoutDeltaTimeSec: (F32, 0x0, 0x0, 0x0)
    mPerSlotCdrIsAdditive: (Bool, 0x0, 0x0, 0x0)
    mLethalityRatioFromTarget: (F32, 0x0, 0x0, 0x0)
    pass

class HealthBarTickStyleBase():
    pass

class TftDropRateSlot():
    TierIcon: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xbcec55fa(0x114828a9):
    OuterRadius: (F32, 0x0, 0x0, 0x0)
    InnerRadius: (F32, 0x0, 0x0, 0x0)
    pass

class SubmeshVisibilityEventData(BaseEventData):
    ApplyOnlyToAvatarMeshes: (Bool, 0x0, 0x0, 0x0)
    mShowSubmeshHash: (U32, 0x0, 0x0, 0x0)
    mShowSubmeshList: (List, 0x0, Hash, 0x0)
    mHideSubmeshHash: (U32, 0x0, 0x0, 0x0)
    mHideSubmeshList: (List, 0x0, Hash, 0x0)
    pass

class ScriptDataObjectList():
    mName: (String, 0x0, 0x0, 0x0)
    mScriptDataObjects: (List, 0x0, Link, ScriptDataObject)
    pass

class RecommendedJunglePathIcons():
    ScoreboardDisabledIcon: (Embed, 0x0, 0x0, MinimapIcon)
    ScoreboardEnabledFinalIcon: (Embed, 0x0, 0x0, MinimapIcon)
    ScoreboardEnabledIcon: (Embed, 0x0, 0x0, MinimapIcon)
    pass

class 0xbd10ca3c(IFxActionInstance):
    pass

class BaseBlendData():
    pass

class CssSheet():
    IconTexture: (String, 0x0, 0x0, 0x0)
    Styles: (Map, String, Embed, CssStyle)
    Icons: (Map, String, Embed, CssIcon)
    pass

class CustomTargeterDefinitions():
    mTargeterDefinitions: (List, 0x0, Pointer, TargeterDefinition)
    pass

class 0xbd3b9f20():
    FinalSpawnCountPerInterval: (U32, 0x0, 0x0, 0x0)
    CurveType: (U8, 0x0, 0x0, 0x0)
    0xc3628f91: (Bool, 0x0, 0x0, 0x0)
    MaxDuration: (F32, 0x0, 0x0, 0x0)
    pass

class 0xbd5ba640():
    0x749450fd: (F32, 0x0, 0x0, 0x0)
    0xfb841f25: (F32, 0x0, 0x0, 0x0)
    pass

class IsEnemyDynamicMaterialBoolDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    pass

class 0xbd659e9b(0xed4b858b):
    Key: (Pointer, 0x0, 0x0, 0xd866344b)
    Data: (Pointer, 0x0, 0x0, 0x6c7a6a03)
    pass

class MovementDirectionParametricUpdater(IFloatParametricUpdater):
    pass

class HasSpellRankSpawnConditionData(VfxSpawnConditionData):
    mSpellSlot: (U32, 0x0, 0x0, 0x0)
    mSpellLevel: (I32, 0x0, 0x0, 0x0)
    pass

class TftTrovesBannerRewardGroup(TftTrovesBannerReward):
    pass

class 0xbdbf785f(0xd866344b):
    Value: (U8, 0x0, 0x0, 0x0)
    pass

class PfxGroupDefinitionData():
    VisibilityRadius: (F32, 0x0, 0x0, 0x0)
    pass

class NavGridConfig():
    ErrorColor: (Color, 0x0, 0x0, 0x0)
    TerrainConfig: (Link, 0x0, 0x0, NavGridTerrainConfig)
    RegionGroups: (List2, 0x0, Embed, 0x2bfb084c)
    pass

class FixedDistanceIgnoringTerrain(MissileBehaviorSpec):
    ScanWidthOverride: (Option, 0x0, F32, 0x0)
    mMaximumDistance: (F32, 0x0, 0x0, 0x0)
    mMinimumGapBetweenTerrainWalls: (F32, 0x0, 0x0, 0x0)
    mTargeterDefinition: (Pointer, 0x0, 0x0, TargeterDefinitionSkipTerrain)
    mMaximumTerrainWallsToSkip: (Option, 0x0, U32, 0x0)
    pass

class MapCharacterList():
    Characters: (List, 0x0, Link, Character)
    Characters: (List2, 0x0, Link, ICharacter)
    Characters: (List2, 0x0, Link, Character)
    pass

class 0xbded2d7f():
    Map: (Map, U32, U32, 0x0)
    pass

class BrowserElementData(ElementDataBase):
    InstanceData: (List2, 0x0, Embed, BrowserInstanceData)
    pass

class 0xbe081d2c():
    TimerDefaultFill: (Hash, 0x0, 0x0, 0x0)
    0x81cbec5f: (Hash, 0x0, 0x0, 0x0)
    0x9ba9ed34: (Hash, 0x0, 0x0, 0x0)
    0xbcde5149: (Hash, 0x0, 0x0, 0x0)
    pass

class LoadScreenTipConfiguration():
    mShowTips: (Bool, 0x0, 0x0, 0x0)
    mShowInCustomGames: (Bool, 0x0, 0x0, 0x0)
    mShowPbiTipsOnLoadingScreen: (Bool, 0x0, 0x0, 0x0)
    mDurationInGame: (F32, 0x0, 0x0, 0x0)
    mShowInGame: (Bool, 0x0, 0x0, 0x0)
    mPbiTipDurationOnLoadingScreen: (F32, 0x0, 0x0, 0x0)
    pass

class EffectCooldownElementData(EffectElementData):
    mEffectColor0: (Color, 0x0, 0x0, 0x0)
    mEffectColor1: (Color, 0x0, 0x0, 0x0)
    pass

class HeroFloatingInfoBarData(FloatingInfoBarData):
    DeathAnimAlly: (Hash, 0x0, 0x0, 0x0)
    BurstHealData: (Embed, 0x0, 0x0, FloatingHealthBarBurstHealData)
    BurstHealMeterSelf: (Hash, 0x0, 0x0, 0x0)
    Divider: (Hash, 0x0, 0x0, 0x0)
    BurstData: (Embed, 0x0, 0x0, FloatingHealthBarBurstData)
    BurstHealMeterEnemy: (Hash, 0x0, 0x0, 0x0)
    ScriptedThresholdTypes: (Map, Hash, Hash, 0x0)
    BountyData: (Pointer, 0x0, 0x0, HeroFloatingInfoBountyData)
    BurstHealMeterSelfColorblind: (Hash, 0x0, 0x0, 0x0)
    DeathAnimEnemy: (Hash, 0x0, 0x0, 0x0)
    UnitStatus: (Embed, 0x0, 0x0, UiUnitStatusData)
    Borders: (Embed, 0x0, 0x0, HeroFloatingInfoBorderData)
    BurstFadeMeterSelf: (Hash, 0x0, 0x0, 0x0)
    BurstFadeMeterOther: (Hash, 0x0, 0x0, 0x0)
    Healthbar: (Embed, 0x0, 0x0, HealthBarData)
    ParBar: (Pointer, 0x0, 0x0, AbilityResourceBarData)
    ResistData: (Pointer, 0x0, 0x0, HeroFloatingInfoResistData)
    CharacterStateIndicators: (Pointer, 0x0, 0x0, HeroFloatingInfoCharacterStateIndicatorData)
    DamageFlashMeter: (Hash, 0x0, 0x0, 0x0)
    SarBar: (Pointer, 0x0, 0x0, AbilityResourceBarData)
    BurstHealMeterAlly: (Hash, 0x0, 0x0, 0x0)
    SarPips: (Pointer, 0x0, 0x0, AbilityResourcePipsData)
    Icons: (Pointer, 0x0, 0x0, HeroFloatingInfoIconsData)
    pass

class GameModeConstantStringVector(GameModeConstant):
    mValue: (List, 0x0, String, 0x0)
    pass

class FadeByMouseRangeBehavior(ITargeterFadeBehavior):
    mStartAlpha: (F32, 0x0, 0x0, 0x0)
    mRangeToEndFading: (F32, 0x0, 0x0, 0x0)
    mRangeToStartFading: (F32, 0x0, 0x0, 0x0)
    mEndAlpha: (F32, 0x0, 0x0, 0x0)
    pass

class ScriptGlobalProperties():
    IsDeathRecapSource: (Bool, 0x0, 0x0, 0x0)
    ChannelDuration: (F32, 0x0, 0x0, 0x0)
    NonDispellable: (Bool, 0x0, 0x0, 0x0)
    DisplayName: (String, 0x0, 0x0, 0x0)
    CastTime: (F32, 0x0, 0x0, 0x0)
    AutoBuffActivateEffects: (List, 0x0, String, 0x0)
    SpellDamageRatio: (F32, 0x0, 0x0, 0x0)
    SpellToggleSlot: (U32, 0x0, 0x0, 0x0)
    BuffName: (String, 0x0, 0x0, 0x0)
    DeathEventType: (U32, 0x0, 0x0, 0x0)
    OnPreDamagePriority: (I32, 0x0, 0x0, 0x0)
    BuffTextureName: (String, 0x0, 0x0, 0x0)
    PersistsThroughDeath: (Bool, 0x0, 0x0, 0x0)
    PopupMessages: (List, 0x0, String, 0x0)
    SpellFxOverrideSkins: (List, 0x0, String, 0x0)
    IsItemToggled: (Bool, 0x0, 0x0, 0x0)
    SpellVoOverrideSkins: (List, 0x0, String, 0x0)
    AutoBuffActivateAttachBoneNames: (List, 0x0, String, 0x0)
    pass

class GlobalResourceResolver(BaseResourceResolver):
    pass

class 0xbe638148(IScriptBlock, IBehaviorScriptBlock):
    Position: (Pointer, 0x0, 0x0, IVectorGet)
    pass

class KeywordViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    Shelf: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideBinName: (String, 0x0, 0x0, 0x0)
    Tab: (Hash, 0x0, 0x0, 0x0)
    BaseBinName: (String, 0x0, 0x0, 0x0)
    pass

class TargetHasUnitTagFilter(IStatStoneLogicDriver):
    UnitTags: (Embed, 0x0, 0x0, ObjectTags)
    pass

class BasePerk():
    mPingTextLocalizationKey: (String, 0x0, 0x0, 0x0)
    mDisplayNameLocalizationKey: (String, 0x0, 0x0, 0x0)
    mPerkId: (U32, 0x0, 0x0, 0x0)
    mTooltipNameLocalizationKey: (String, 0x0, 0x0, 0x0)
    mScript: (Pointer, 0x0, 0x0, PerkScript)
    mEnabled: (Bool, 0x0, 0x0, 0x0)
    mPerkName: (String, 0x0, 0x0, 0x0)
    mIconTextureName: (String, 0x0, 0x0, 0x0)
    mShortDescLocalizationKey: (String, 0x0, 0x0, 0x0)
    mVfxResourceResolver: (Pointer, 0x0, 0x0, ResourceResolver)
    mLongDescLocalizationKey: (String, 0x0, 0x0, 0x0)
    mStackable: (Bool, 0x0, 0x0, 0x0)
    mDisplayStatLocalizationKey: (String, 0x0, 0x0, 0x0)
    mCharacters: (List, 0x0, String, 0x0)
    mBuffs: (List, 0x0, Pointer, PerkBuff)
    mEndOfGameStatDescriptions: (List, 0x0, String, 0x0)
    pass

class AiTurretClient(AiTurretCommon):
    pass

class OutnumberedConstraintInfo(ListenerConstraintInfo):
    DistanceToEncompass: (F32, 0x0, 0x0, 0x0)
    pass

class BaseElementData(ElementDataI):
    mAnchorOptional: (Option, 0x0, Vec2, 0x0)
    mName: (String, 0x0, 0x0, 0x0)
    mBlockInputEvents: (Bool, 0x0, 0x0, 0x0)
    mRectSourceResolutionWidth: (U16, 0x0, 0x0, 0x0)
    mRectSourceResolutionWidth: (U32, 0x0, 0x0, 0x0)
    mAnchor: (Vec2, 0x0, 0x0, 0x0)
    mRectSourceResolutionHeight: (U16, 0x0, 0x0, 0x0)
    mRectSourceResolutionHeight: (U32, 0x0, 0x0, 0x0)
    mDraggable: (U32, 0x0, 0x0, 0x0)
    mEnabled: (Bool, 0x0, 0x0, 0x0)
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    mColor: (Color, 0x0, 0x0, 0x0)
    StickyDrag: (Bool, 0x0, 0x0, 0x0)
    mLayer: (U32, 0x0, 0x0, 0x0)
    mKeepMaxScale: (Bool, 0x0, 0x0, 0x0)
    mScene: (Link, 0x0, 0x0, Scene)
    mScene: (Link, 0x0, 0x0, SceneData)
    mScene: (String, 0x0, 0x0, 0x0)
    mHitTestPolygon: (List, 0x0, Vec2, 0x0)
    mRect: (Vec4, 0x0, 0x0, 0x0)
    mUseRectSourceResolutionAsFloor: (Bool, 0x0, 0x0, 0x0)
    mAutoRect: (Bool, 0x0, 0x0, 0x0)
    mUseAbsoluteRect: (Bool, 0x0, 0x0, 0x0)
    mFullscreen: (Bool, 0x0, 0x0, 0x0)
    mNoPixelSnappingY: (Bool, 0x0, 0x0, 0x0)
    mNoPixelSnappingX: (Bool, 0x0, 0x0, 0x0)
    mAnchors: (Pointer, 0x0, 0x0, AnchorBase)
    pass

class TftSocialPanelViewController(SocialPanelViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    BaseFriendsListScissorRegion: (Hash, 0x0, 0x0, 0x0)
    ExpandedFriendsListScissorRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class JungleRecommendationMapInformation():
    JungleLocationInformation: (List2, 0x0, Embed, JungleLocationMapInformation)
    pass

class 0xbef9baa7(0x6c7a6a03):
    Value: (Map, U8, Hash, 0x0)
    pass

class UnitShopItemData():
    Special3Vfx: (Hash, 0x0, 0x0, 0x0)
    Rarity5Vfx: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    UnitPortrait: (Hash, 0x0, 0x0, 0x0)
    BadgeVfx: (Hash, 0x0, 0x0, 0x0)
    Special5Vfx: (Hash, 0x0, 0x0, 0x0)
    Description: (Hash, 0x0, 0x0, 0x0)
    Badge: (Hash, 0x0, 0x0, 0x0)
    FramesOld: (Hash, 0x0, 0x0, 0x0)
    DefaultFrame: (Embed, 0x0, 0x0, UnitShopItemFrameData)
    HighlightThreestar: (Hash, 0x0, 0x0, 0x0)
    SoldLeftEndcap: (Hash, 0x0, 0x0, 0x0)
    SoldRightEndcap: (Hash, 0x0, 0x0, 0x0)
    GoldCostIconDisabled: (Hash, 0x0, 0x0, 0x0)
    HealthCostIconDisabled: (Hash, 0x0, 0x0, 0x0)
    Frames: (Map, U8, Embed, UnitShopItemFrameData)
    DisplayFrame: (Embed, 0x0, 0x0, UnitShopItemFrameData)
    Traits: (List, 0x0, Embed, UnitShopItemTraitData)
    Traits: (List, 0x0, Embed, UnitShopDisplayTraitData)
    HitTarget: (Hash, 0x0, 0x0, 0x0)
    Rarity6CostHealthVfx: (Hash, 0x0, 0x0, 0x0)
    UnitCostText: (Hash, 0x0, 0x0, 0x0)
    TeamPlanReminder: (Hash, 0x0, 0x0, 0x0)
    Styles: (Map, Hash, Hash, 0x0)
    Special4Vfx: (Hash, 0x0, 0x0, 0x0)
    SoldStretch: (Hash, 0x0, 0x0, 0x0)
    HighlightOnestar: (Hash, 0x0, 0x0, 0x0)
    Rarity6Vfx: (Hash, 0x0, 0x0, 0x0)
    UnitNameText: (Hash, 0x0, 0x0, 0x0)
    GoldCostIcon: (Hash, 0x0, 0x0, 0x0)
    ClickRejectedVfx: (Hash, 0x0, 0x0, 0x0)
    HealthCostIcon: (Hash, 0x0, 0x0, 0x0)
    HighlightTwostar: (Hash, 0x0, 0x0, 0x0)
    pass

class NavGridTerrainConfig():
    Tags: (List2, 0x0, Embed, 0xd82714cc)
    pass

class MapMaterialSwap():
    Swaps: (Map, String, Link, StaticMaterialDef)
    pass

class Location(TargetingTypeData):
    pass

class TftStageSceneData():
    Scene: (Hash, 0x0, 0x0, 0x0)
    TimerFillTexture: (Hash, 0x0, 0x0, 0x0)
    OvertimeBackgroundTopRight: (Hash, 0x0, 0x0, 0x0)
    BackgroundTopCenter: (Hash, 0x0, 0x0, 0x0)
    TimingOutBackgroundTopRight: (Hash, 0x0, 0x0, 0x0)
    StageRightGroup: (Hash, 0x0, 0x0, 0x0)
    StageLeftGroup: (Hash, 0x0, 0x0, 0x0)
    Timer: (Hash, 0x0, 0x0, 0x0)
    TimerBarBackground: (Hash, 0x0, 0x0, 0x0)
    StageNumber: (Hash, 0x0, 0x0, 0x0)
    BackgroundTopRight: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xbf5c4715():
    0x16ea3d9: (Embed, 0x0, 0x0, 0x1493959a)
    pass

class 0xbf6d152c(IScriptBlock, IBehaviorScriptBlock):
    pass

class InstanceDataBase():
    RegionData: (Pointer, 0x0, 0x0, RegionDataBase)
    Enabled: (Bool, 0x0, 0x0, 0x0)
    Id: (String, 0x0, 0x0, 0x0)
    BackgroundImage: (Embed, 0x0, 0x0, TextureOverride)
    StartDate: (String, 0x0, 0x0, 0x0)
    EndDate: (String, 0x0, 0x0, 0x0)
    TitleTextTra: (String, 0x0, 0x0, 0x0)
    pass

class VfxEmissionSurfaceData():
    SkeletonName: (String, 0x0, 0x0, 0x0)
    UseAvatarPose: (Bool, 0x0, 0x0, 0x0)
    AnimationName: (String, 0x0, 0x0, 0x0)
    UseSurfaceNormalForBirthPhysics: (Bool, 0x0, 0x0, 0x0)
    MaxJointWeights: (U16, 0x0, 0x0, 0x0)
    MeshScale: (F32, 0x0, 0x0, 0x0)
    MeshName: (String, 0x0, 0x0, 0x0)
    0xf8b81c77: (Pointer, 0x0, 0x0, 0x1519e8d2)
    Submeshes: (List, 0x0, Hash, 0x0)
    pass

class PlayerStatsViewController(ViewController):
    BasicStats: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    ObjectName: (String, 0x0, 0x0, 0x0)
    AdvancedStats: (Hash, 0x0, 0x0, 0x0)
    pass

class MissileSpecification():
    VerticalFacing: (Pointer, 0x0, 0x0, VerticalFacingType)
    MissileGroupSpawners: (List, 0x0, Embed, MissileGroupSpawnerSpec)
    MissileGroupSpawners: (List, 0x0, Pointer, MissileGroupSpawner)
    RenderComponent: (Pointer, 0x0, 0x0, MissileRenderSpec)
    HeightSolver: (Pointer, 0x0, 0x0, HeightSolverType)
    VisibilityComponent: (Pointer, 0x0, 0x0, MissileVisibilitySpec)
    Behaviors: (List, 0x0, Pointer, MissileBehaviorSpec)
    mMissileWidth: (F32, 0x0, 0x0, 0x0)
    0xc195fba6: (Bool, 0x0, 0x0, 0x0)
    MovementComponent: (Pointer, 0x0, 0x0, MissileMovementSpec)
    pass

class PlayerStatStonesViewController(PlayerStatsPanelViewController, ViewController):
    FrameAdvTop: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    FrameDefault: (Hash, 0x0, 0x0, 0x0)
    StatStonesStats: (Embed, 0x0, 0x0, UiStatStonesStats)
    ObjectName: (String, 0x0, 0x0, 0x0)
    FrameAdvSide: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xc006cb7a():
    0x244806e9: (U32, 0x0, 0x0, 0x0)
    MaxCount: (U32, 0x0, 0x0, 0x0)
    pass

class 0xc00f3a0f():
    0xb9dba0ce: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionMapRegionName(IContextualCondition):
    mRegionType: (U8, 0x0, 0x0, 0x0)
    mRegionName: (String, 0x0, 0x0, 0x0)
    pass

class VfxAnimatedFloat(VfxFloatBase):
    Values: (List, 0x0, F32, 0x0)
    Values: (List2, 0x0, F32, 0x0)
    Times: (List, 0x0, F32, 0x0)
    Times: (List2, 0x0, F32, 0x0)
    0x7c9bcfd5: (List, 0x0, U32, 0x0)
    Modes: (List2, 0x0, U8, 0x0)
    ProbabilityTables: (List, 0x1, Pointer, VfxProbabilityTableData)
    pass

class IGameModeConfigClient(IGameModeConfigBase):
    pass

class ItemDataAvailability():
    mForceLoad: (Bool, 0x0, 0x0, 0x0)
    mInStore: (Bool, 0x0, 0x0, 0x0)
    mHidefromAll: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xc053efcc(IBehaviorScriptBlock):
    pass

class 0xc057ee47(TftCutsceneClip):
    LightingOverride: (Vec4, 0x0, 0x0, 0x0)
    BlackboardAssociatedPlayers: (List2, 0x0, String, 0x0)
    pass

class 0xc06f5f6a():
    pass

class GameModeConstants():
    mGroups: (Map, Hash, Embed, GameModeConstantsGroup)
    pass

class UiMetricVietnameseRatingLabel(UiMetricTypeI):
    Label: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xc0bb891d():
    CompleteDefault: (Hash, 0x0, 0x0, 0x0)
    Complete: (Hash, 0x0, 0x0, 0x0)
    ActiveSelected: (Hash, 0x0, 0x0, 0x0)
    InactiveSelected: (Hash, 0x0, 0x0, 0x0)
    ActiveHover: (Hash, 0x0, 0x0, 0x0)
    ActiveDefault: (Hash, 0x0, 0x0, 0x0)
    InactiveDefault: (Hash, 0x0, 0x0, 0x0)
    CompleteHover: (Hash, 0x0, 0x0, 0x0)
    Active: (Hash, 0x0, 0x0, 0x0)
    Inactive: (Hash, 0x0, 0x0, 0x0)
    InactiveHover: (Hash, 0x0, 0x0, 0x0)
    HitRegion: (Hash, 0x0, 0x0, 0x0)
    CompleteSelected: (Hash, 0x0, 0x0, 0x0)
    pass

class MapAnimatedProp(GenericMapPlaceable):
    VisibilityController: (Link, 0x0, 0x0, IMapVisibilityController)
    PropName: (String, 0x0, 0x0, 0x0)
    EyeCandy: (Bool, 0x0, 0x0, 0x0)
    IdleAnimationName: (String, 0x0, 0x0, 0x0)
    SkinId: (U32, 0x0, 0x0, 0x0)
    PlayIdleAnimation: (Bool, 0x0, 0x0, 0x0)
    Quality: (I32, 0x0, 0x0, 0x0)
    IsClickable: (Bool, 0x0, 0x0, 0x0)
    BoxMin: (Vec3, 0x0, 0x0, 0x0)
    DefaultAnimation: (String, 0x0, 0x0, 0x0)
    BoxMax: (Vec3, 0x0, 0x0, 0x0)
    pass

class DefaultStatModPerkSet():
    mPerks: (List, 0x0, Link, Perk)
    mStyleId: (U32, 0x0, 0x0, 0x0)
    pass

class UnitStatusIcons():
    mIconData: (Link, 0x0, 0x0, UnitStatusIconData)
    mIconOffset: (Vec2, 0x0, 0x0, 0x0)
    mIconDrawSize: (Vec2, 0x0, 0x0, 0x0)
    pass

class HudReplayGameStats(GameStateViewController, ViewController):
    ChaosObjectiveBountiesData: (Pointer, 0x0, 0x0, SbObjectiveBounties)
    OrderObjectiveBountiesData: (Pointer, 0x0, 0x0, SbObjectiveBounties)
    ParentScene: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xc0fd6b7b():
    RecipeHintButton: (Hash, 0x0, 0x0, 0x0)
    0x63c87650: (Hash, 0x0, 0x0, 0x0)
    ItemFrame: (Hash, 0x0, 0x0, 0x0)
    ItemDesc: (Hash, 0x0, 0x0, 0x0)
    ItemName: (Hash, 0x0, 0x0, 0x0)
    ItemIcon: (Hash, 0x0, 0x0, 0x0)
    ElementGroup: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xc10d4fdc():
    pass

class LockRootOrientationEventData(BaseEventData):
    JointName: (Hash, 0x0, 0x0, 0x0)
    0x8c07c6b5: (I32, 0x0, 0x0, 0x0)
    BlendOutTime: (F32, 0x0, 0x0, 0x0)
    pass

class TftEmotePanelViewController(ViewController):
    MainViewScene: (Hash, 0x0, 0x0, 0x0)
    PlayDanceAnimationButton: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    PlayJokeAnimationButton: (Hash, 0x0, 0x0, 0x0)
    PlayTauntAnimationButton: (Hash, 0x0, 0x0, 0x0)
    ToplevelScene: (Hash, 0x0, 0x0, 0x0)
    SummonerEmoteIcons: (List, 0x0, Hash, 0x0)
    ToggleEmotesButton: (Hash, 0x0, 0x0, 0x0)
    PlayLaughAnimationButton: (Hash, 0x0, 0x0, 0x0)
    SummonerEmoteButtons: (List, 0x0, Hash, 0x0)
    pass

class TftTraitSetData():
    mBuffName: (String, 0x0, 0x0, 0x0)
    mEffectAmount: (Map, Hash, F32, 0x0)
    mTeamToBuff: (U8, 0x0, 0x0, 0x0)
    mActivatedBuffName: (String, 0x0, 0x0, 0x0)
    mMaxUnits: (Option, 0x0, U32, 0x0)
    mMaxUnits: (U32, 0x0, 0x0, 0x0)
    mMinUnits: (U32, 0x0, 0x0, 0x0)
    mTargetStrategy: (U8, 0x0, 0x0, 0x0)
    mTargetUnitsToBuff: (Option, 0x0, U32, 0x0)
    EffectAmounts: (List, 0x0, Embed, TftEffectAmount)
    mTraitBuff: (Link, 0x0, 0x0, SpellObject)
    mStyle: (U8, 0x0, 0x0, 0x0)
    pass

class 0xc132bfa(IScriptBlock, IBehaviorScriptBlock):
    ScriptEvent: (U32, 0x0, 0x0, 0x0)
    pass

class 0xc15041c4(0xc9440657):
    OverrideAnimation: (String, 0x0, 0x0, 0x0)
    PropName: (String, 0x0, 0x0, 0x0)
    0x7a9fe21a: (Bool, 0x0, 0x0, 0x0)
    0x7dde758d: (U8, 0x0, 0x0, 0x0)
    PropBoneName: (String, 0x0, 0x0, 0x0)
    pass

class UiElementEffectInstanced(UiElementEffect):
    pass

class TftCharacterList():
    Characters: (List2, 0x0, Link, TftCharacter)
    pass

class GameModeEventList():
    Events: (Map, String, Embed, GameModeEventDefinition)
    pass

class EvolutionDescription():
    mTitle: (String, 0x0, 0x0, 0x0)
    mFlags: (U32, 0x0, 0x0, 0x0)
    mIconNames: (List, 0x4, String, 0x0)
    mTooltips: (List, 0x4, String, 0x0)
    pass

class UiElementEffectDesaturateData(UiElementEffectData):
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    MaximumSaturation: (F32, 0x0, 0x0, 0x0)
    MinimumSaturation: (F32, 0x0, 0x0, 0x0)
    TextureData: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mAtlas: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    pass

class IIntGet(IRsValueGet, IScriptValueGet):
    pass

class KillingSpreeFilter(IStatStoneLogicDriver):
    KillingSpreeCount: (I32, 0x0, 0x0, 0x0)
    pass

class 0xc24051e7(MapAction):
    Constant: (U32, 0x0, 0x0, 0x0)
    ConstantValue: (Vec4, 0x0, 0x0, 0x0)
    LerpTime: (F32, 0x0, 0x0, 0x0)
    pass

class 0xc261f71e(ILolSpellScriptEvent):
    pass

class TftTraitTrackerViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    ResizableEnemyBackdrop: (Hash, 0x0, 0x0, 0x0)
    0x3778da6: (Bool, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    0x42746b91: (U32, 0x0, 0x0, 0x0)
    0x4aa4bfcd: (U32, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    TraitTemplate: (Embed, 0x0, 0x0, TftTraitTrackerTraitDataTemplate)
    TraitInfoCardHoverRegion: (Hash, 0x0, 0x0, 0x0)
    ResizableBackdrop: (Hash, 0x0, 0x0, 0x0)
    0x8c1d10e2: (U32, 0x0, 0x0, 0x0)
    PageButton: (Hash, 0x0, 0x0, 0x0)
    0xa39608ac: (U32, 0x0, 0x0, 0x0)
    TraitPageRegion: (Hash, 0x0, 0x0, 0x0)
    TraitHeightRef: (Hash, 0x0, 0x0, 0x0)
    TraitInfoCardRegion: (Hash, 0x0, 0x0, 0x0)
    0xd2c9ddb: (U32, 0x0, 0x0, 0x0)
    0xdeac5b13: (U32, 0x0, 0x0, 0x0)
    0xefcbc89c: (U32, 0x0, 0x0, 0x0)
    pass

class EffectAmmoElementData(EffectElementData):
    mEffectColor0: (Color, 0x0, 0x0, 0x0)
    mEffectColor1: (Color, 0x0, 0x0, 0x0)
    pass

class PracticeToolButtonDefinition():
    Portrait: (Hash, 0x0, 0x0, 0x0)
    ToggleVfx: (Hash, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxTrailDefinitionData():
    mMaxAddedPerFrame: (I32, 0x0, 0x0, 0x0)
    mBirthTilingSize: (Embed, 0x0, 0x0, ValueVector3)
    mMode: (U32, 0x0, 0x0, 0x0)
    mMode: (U8, 0x0, 0x0, 0x0)
    mSmoothingMode: (U8, 0x0, 0x0, 0x0)
    mCutoff: (F32, 0x0, 0x0, 0x0)
    pass

class OptionItemColumns(IOptionItem):
    ItemsEither: (List, 0x0, Pointer, IOptionItem)
    ItemsRight: (List, 0x0, Pointer, IOptionItem)
    ItemsLeft: (List, 0x0, Pointer, IOptionItem)
    pass

class 0xc2b1af7f(ISequenceAction):
    DisableOnEnd: (Bool, 0x0, 0x0, 0x0)
    Element: (Pointer, 0x0, 0x0, 0xe561be2e)
    EnableOnStart: (Bool, 0x0, 0x0, 0x0)
    pass

class RunSpeedRatioFloatDriver(ILogicFloatDriver):
    pass

class MapPointLightBase(MapPlaceable):
    0xe281ed56: (F32, 0x0, 0x0, 0x0)
    pass

class HudWindowPlacementData():
    Anchor: (String, 0x0, 0x0, 0x0)
    YPercent: (F32, 0x0, 0x0, 0x0)
    MinScale: (F32, 0x0, 0x0, 0x0)
    UseHeightScale: (Bool, 0x0, 0x0, 0x0)
    UseSimpleScaling: (Bool, 0x0, 0x0, 0x0)
    Name: (Hash, 0x0, 0x0, 0x0)
    XPercent: (F32, 0x0, 0x0, 0x0)
    pass

class 0xc30a6d82(IFxActionInstance):
    pass

class HudMenuTransitionData():
    TransitionTime: (F32, 0x0, 0x0, 0x0)
    EasingType: (U32, 0x0, 0x0, 0x0)
    EasingType: (U8, 0x0, 0x0, 0x0)
    MinAlpha: (U8, 0x0, 0x0, 0x0)
    MaxAlpha: (U8, 0x0, 0x0, 0x0)
    TransitionStartDelaySecs: (F32, 0x0, 0x0, 0x0)
    pass

class IStatStoneLogicDriver():
    pass

class TftMapItemList():
    Items: (List2, 0x0, Embed, TftMapItemData)
    pass

class 0xc36afd8f(0x2515101c):
    CurrencyId: (String, 0x0, 0x0, 0x0)
    NameTraKey: (String, 0x0, 0x0, 0x0)
    pass

class 0xc3737f3e():
    Button: (Hash, 0x0, 0x0, 0x0)
    0x4827dc62: (String, 0x0, 0x0, 0x0)
    0x5a6d6bfe: (Embed, 0x0, 0x0, 0x911f126a)
    BackgroundIcon: (Hash, 0x0, 0x0, 0x0)
    DefaultBackgroundTexturePath: (String, 0x0, 0x0, 0x0)
    ForegroundVfx: (Hash, 0x0, 0x0, 0x0)
    ForegroundAssets: (Embed, 0x0, 0x0, 0x131f5725)
    0xd407c07d: (Hash, 0x0, 0x0, 0x0)
    ForegroundIcon: (Hash, 0x0, 0x0, 0x0)
    BackgroundAssets: (Embed, 0x0, 0x0, 0x131f5725)
    DefaultForegroundTexturePath: (String, 0x0, 0x0, 0x0)
    BackgroundVfx: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class GetHqBlock(IScriptBlock):
    Team: (Pointer, 0x0, 0x0, IIntGet)
    pass

class 0xc38aee72(ISequenceAction):
    DisableOnEnd: (Bool, 0x0, 0x0, 0x0)
    0xd07dcd34: (Link, 0x0, 0x0, SequenceObjectSelector)
    EnableOnStart: (Bool, 0x0, 0x0, 0x0)
    pass

class TftUnitPropertyValueBool(TftUnitPropertyValue):
    Value: (Bool, 0x0, 0x0, 0x0)
    pass

class UiSceneViewPaneData(UiSceneData, SceneData):
    DragRegionElement: (Link, 0x0, 0x0, RegionElementData)
    DragRegionElement: (Link, 0x0, 0x0, UiElementRegionData)
    ScissorRegionElement: (Link, 0x0, 0x0, ScissorRegionElementData)
    ScissorRegionElement: (Link, 0x0, 0x0, UiElementScissorRegionData)
    Slider: (Link, 0x0, 0x0, UiElementGroupSliderData)
    ScrollingScene: (Link, 0x0, 0x0, UiSceneData)
    ScrollingScene: (Link, 0x0, 0x0, SceneData)
    BufferRegionElement: (Link, 0x0, 0x0, UiElementRegionData)
    ScrollDirection: (U8, 0x0, 0x0, 0x0)
    ScrollRegionElement: (Link, 0x0, 0x0, RegionElementData)
    ScrollRegionElement: (Link, 0x0, 0x0, UiElementRegionData)
    pass

class NewSpellCastFlowToggles():
    NewSpellCastFlowNormal: (Bool, 0x0, 0x0, 0x0)
    NewSpellCastFlowAutoAttack: (Bool, 0x0, 0x0, 0x0)
    NewSpellCastFlowInstant: (Bool, 0x0, 0x0, 0x0)
    pass

class MapCubemapRegion():
    Min: (Vec3, 0x0, 0x0, 0x0)
    Max: (Vec3, 0x0, 0x0, 0x0)
    pass

class Destroy(MissileTriggeredActionSpec):
    pass

class 0xc4936408(IEnabler):
    pass

class StateLogicEventData(BaseEventData):
    StateLogicEventSignalId: (Hash, 0x0, 0x0, 0x0)
    pass

class UniverseData():
    mName: (String, 0x0, 0x0, 0x0)
    mSkinSetLinks: (List, 0x0, Link, SkinLineData)
    mDisplayName: (String, 0x0, 0x0, 0x0)
    mImagePath: (String, 0x0, 0x0, 0x0)
    mUniverseId: (U32, 0x0, 0x0, 0x0)
    mDescription: (String, 0x0, 0x0, 0x0)
    pass

class FxActionVfxBeamInstance(IFxActionInstance):
    pass

class 0xc4aef724():
    pass

class AugmentDisplayTagData():
    AugmentDisplayTagSpacer: (Hash, 0x0, 0x0, 0x0)
    AugmentDisplayTagRow: (Hash, 0x0, 0x0, 0x0)
    AugmentDisplayTagFrame: (Hash, 0x0, 0x0, 0x0)
    AugmentDisplayTagText: (Hash, 0x0, 0x0, 0x0)
    pass

class HudTeamScoreMeterProperties():
    mTooltipEnemyLocKey: (String, 0x0, 0x0, 0x0)
    mTooltipAllyLocKey: (String, 0x0, 0x0, 0x0)
    mTeamScoreMeterType: (U8, 0x0, 0x0, 0x0)
    mShowScoreText: (Bool, 0x0, 0x0, 0x0)
    pass

class HudFightRecapUiData():
    mUnknownDamageIconTextureName: (String, 0x0, 0x0, 0x0)
    mItemDamageIconTextureName: (String, 0x0, 0x0, 0x0)
    mBasicAttackIconTextureName: (String, 0x0, 0x0, 0x0)
    mRuneDamageIconTextureName: (String, 0x0, 0x0, 0x0)
    pass

class 0xc53d595a(IScriptBlock, IBehaviorScriptBlock):
    pass

class HasBuffWithAttributeBoolDriver(ILogicBoolDriver):
    BuffAttribute: (U8, 0x0, 0x0, 0x0)
    pass

class OptionItemFilter_VoiceChat(IOptionItemFilter):
    NeedsPushToTalkEnabled: (Bool, 0x0, 0x0, 0x0)
    pass

class LobbySelfPortrait():
    SummonerIcon: (Hash, 0x0, 0x0, 0x0)
    ArenaSkinIcon: (Hash, 0x0, 0x0, 0x0)
    PartyLeaderIcon: (Hash, 0x0, 0x0, 0x0)
    LoadoutsButton: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    RankText: (Hash, 0x0, 0x0, 0x0)
    LittleLegendIcon: (Hash, 0x0, 0x0, 0x0)
    NameText: (Hash, 0x0, 0x0, 0x0)
    RankTextLine2: (Hash, 0x0, 0x0, 0x0)
    pass

class AddGoldCheat(Cheat):
    mTarget: (U32, 0x0, 0x0, 0x0)
    mGoldAmount: (F32, 0x0, 0x0, 0x0)
    pass

class 0xc5e16ef4(IScriptBlock):
    pass

class AllItemsSet():
    mLabel: (String, 0x0, 0x0, 0x0)
    mItemPages: (List, 0x0, Embed, AllItemsPage)
    pass

class StructureFloatingInfoBarData(UnitFloatingInfoBarData):
    DeathAnimAlly: (Hash, 0x0, 0x0, 0x0)
    BurstData: (Embed, 0x0, 0x0, FloatingHealthBarBurstData)
    DeathAnimEnemy: (Hash, 0x0, 0x0, 0x0)
    BurstFadeMeter: (Hash, 0x0, 0x0, 0x0)
    DamageFlashMeter: (Hash, 0x0, 0x0, 0x0)
    pass

class IScriptCondition():
    pass

class CharacterOverrides():
    ShowSubmeshes: (List, 0x0, Hash, 0x0)
    AnimationOverrides: (Map, String, String, 0x0)
    HideSubmeshes: (List, 0x0, Hash, 0x0)
    AttachmentOverrides: (Map, String, String, 0x0)
    pass

class CherryCombatInfoDisplayTeam():
    0x3ad87f88: (Hash, 0x0, 0x0, 0x0)
    TeamIcon: (Hash, 0x0, 0x0, 0x0)
    0x7ba0782e: (Hash, 0x0, 0x0, 0x0)
    FillMeter: (Hash, 0x0, 0x0, 0x0)
    TeamHitRegion: (Hash, 0x0, 0x0, 0x0)
    TeamTooltipAnchor: (Hash, 0x0, 0x0, 0x0)
    0xe51c9c6c: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionIsAlly(ICharacterSubcondition):
    mIsAlly: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xc66495db(IBehaviorScriptBlock):
    pass

class 0xc668ae80():
    ColorBScale: (F32, 0x0, 0x0, 0x0)
    NamePrefix: (String, 0x0, 0x0, 0x0)
    ColorA: (Vec4, 0x0, 0x0, 0x0)
    ColorB: (Vec4, 0x0, 0x0, 0x0)
    ColorAScale: (F32, 0x0, 0x0, 0x0)
    pass

class ToolInheritsData():
    Recommended: (String, 0x0, 0x0, 0x0)
    pass

class 0xc68f2b(IFxAction):
    ZoomEase: (U8, 0x0, 0x0, 0x0)
    pass

class UiMetricTeamScoreMeters(UiMetricTypeI):
    Team2MeterBlueSkin: (Embed, 0x0, 0x0, UiElementMeterSkin)
    Team2MeterBlueSkin: (Hash, 0x0, 0x0, 0x0)
    Team1MeterRedSkin: (Embed, 0x0, 0x0, UiElementMeterSkin)
    Team1MeterRedSkin: (Hash, 0x0, 0x0, 0x0)
    Team2MeterRedSkin: (Embed, 0x0, 0x0, UiElementMeterSkin)
    Team2MeterRedSkin: (Hash, 0x0, 0x0, 0x0)
    Team1MeterScoreIndex: (U32, 0x0, 0x0, 0x0)
    Team2MeterScoreIndex: (U32, 0x0, 0x0, 0x0)
    Team1MeterBlueSkin: (Embed, 0x0, 0x0, UiElementMeterSkin)
    Team1MeterBlueSkin: (Hash, 0x0, 0x0, 0x0)
    Team1Meter: (Hash, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    Team2Meter: (Hash, 0x0, 0x0, 0x0)
    pass

class UiDraggableSceneDrag(UiDraggableBasic):
    pass

class 0xc6d8a622(IBehaviorScriptBlock):
    pass

class RoleOpponentConstraintInfo(ListenerConstraintInfo):
    pass

class ChampionItemRecommendations():
    BaseCounterAdviceSets: (List, 0x0, Hash, 0x0)
    ExtraCounterAdvice: (List, 0x0, Embed, BaseItemAdvice)
    mContextListLink: (Hash, 0x0, 0x0, 0x0)
    CounterAdviceSets: (List, 0x0, Hash, 0x0)
    BaseCounterAdvice: (List, 0x0, Embed, BaseItemAdvice)
    mOverrideSetLink: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xc77834ec(ViewController):
    DefeatGroupHandle: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    0x6d28c8a1: (Hash, 0x0, 0x0, 0x0)
    LeaveButton: (Hash, 0x0, 0x0, 0x0)
    GameOverScene: (Hash, 0x0, 0x0, 0x0)
    VictoryGroupHandle: (Hash, 0x0, 0x0, 0x0)
    pass

class RegaliaPrestigeCrestList():
    PrestigeCrests: (List, 0x0, Link, RegaliaData)
    pass

class EsportsTeamData():
    LeagueName: (String, 0x0, 0x0, 0x0)
    ShortName: (String, 0x0, 0x0, 0x0)
    FullName: (String, 0x0, 0x0, 0x0)
    pass

class 0xc7ca4925():
    FrameEnemy: (Hash, 0x0, 0x0, 0x0)
    FrameAlly: (Hash, 0x0, 0x0, 0x0)
    FrameSelf: (Hash, 0x0, 0x0, 0x0)
    pass

class TipStyleBase():
    DirectionalTipElements: (List, 0x0, Link, ElementDataI)
    DirectionalTipElements: (List, 0x0, Link, UiElementIData)
    DirectionalTipElements: (List2, 0x0, Link, UiElementIData)
    pass

class LolFeatureToggles():
    PreferLegacyClocks: (Bool, 0x0, 0x0, 0x0)
    NewLoadingScreen: (Bool, 0x0, 0x0, 0x0)
    LocalGoldGivenOnLastHit: (Bool, 0x0, 0x0, 0x0)
    UseWasdControls: (Bool, 0x0, 0x0, 0x0)
    SelfMitigationLog: (Bool, 0x0, 0x0, 0x0)
    0x1243f0b: (Bool, 0x0, 0x0, 0x0)
    ChallengerRecall: (Bool, 0x0, 0x0, 0x0)
    GameModeItemLists: (Bool, 0x0, 0x0, 0x0)
    MoreAccurateBuffTimeouts: (Bool, 0x0, 0x0, 0x0)
    0x1556b55e: (Bool, 0x0, 0x0, 0x0)
    PromoController: (Bool, 0x0, 0x0, 0x0)
    0x15f45ff8: (Bool, 0x0, 0x0, 0x0)
    0x16fc1c7: (Bool, 0x0, 0x0, 0x0)
    ShopUndoRulesSpike: (Bool, 0x0, 0x0, 0x0)
    0x174cdfa1: (Bool, 0x0, 0x0, 0x0)
    AllChatRemoved: (Bool, 0x0, 0x0, 0x0)
    LoadingScreenChallenges: (Bool, 0x0, 0x0, 0x0)
    SequentialAutoAttackAnimations: (Bool, 0x0, 0x0, 0x0)
    DeathRecapRework: (Bool, 0x0, 0x0, 0x0)
    0x1c07defa: (Bool, 0x0, 0x0, 0x0)
    EnableUnitOrderHandler: (Bool, 0x0, 0x0, 0x0)
    DebugPrintCcScoreToChat: (Bool, 0x0, 0x0, 0x0)
    DeathRecapShowcaseUi: (Bool, 0x0, 0x0, 0x0)
    0x1ef4f4ea: (Bool, 0x0, 0x0, 0x0)
    0x1f64500a: (Bool, 0x0, 0x0, 0x0)
    0x1fbd20b4: (Bool, 0x0, 0x0, 0x0)
    0x20173ad0: (Bool, 0x0, 0x0, 0x0)
    SetDestroyedInFlightWhenDestroyedForTarget: (Bool, 0x0, 0x0, 0x0)
    0x234d078f: (Bool, 0x0, 0x0, 0x0)
    UseGameObjectIdsInLua: (Bool, 0x0, 0x0, 0x0)
    TftSocialModeRequestSystem: (Bool, 0x0, 0x0, 0x0)
    MinionsGainBaseMoveSpeedAtTwenty: (Bool, 0x0, 0x0, 0x0)
    0x2697ce9d: (Bool, 0x0, 0x0, 0x0)
    TftLittleLegendEvolution: (Bool, 0x0, 0x0, 0x0)
    TftZoomSkin: (Bool, 0x0, 0x0, 0x0)
    TftPcTeamPlanner: (Bool, 0x0, 0x0, 0x0)
    0x284eedf9: (Bool, 0x0, 0x0, 0x0)
    0x2929a87d: (Bool, 0x0, 0x0, 0x0)
    0x29f8cbf: (Bool, 0x0, 0x0, 0x0)
    0x2acd56a4: (Bool, 0x0, 0x0, 0x0)
    0x2afd1f6f: (Bool, 0x0, 0x0, 0x0)
    LuaVec3ErrorIsError: (Bool, 0x0, 0x0, 0x0)
    0x2b73d5d4: (Bool, 0x0, 0x0, 0x0)
    CursorDataInGds: (Bool, 0x0, 0x0, 0x0)
    0x2c5205b2: (Bool, 0x0, 0x0, 0x0)
    SpotModDragonAndSpider: (Bool, 0x0, 0x0, 0x0)
    0x2dbfa6f8: (Bool, 0x0, 0x0, 0x0)
    0x2e014f67: (Bool, 0x0, 0x0, 0x0)
    0x2e08e244: (Bool, 0x0, 0x0, 0x0)
    UseNewAttackSpeed: (Bool, 0x0, 0x0, 0x0)
    UpdateCameraBeforeParticles: (Bool, 0x0, 0x0, 0x0)
    0x2f0e955a: (Bool, 0x0, 0x0, 0x0)
    0x2f6a821a: (Bool, 0x0, 0x0, 0x0)
    SpawnEventTemporaryLocation: (Bool, 0x0, 0x0, 0x0)
    0x30ba7188: (Bool, 0x0, 0x0, 0x0)
    0x318a4b7b: (Bool, 0x0, 0x0, 0x0)
    PathControllerMessageSizeLimit: (Bool, 0x0, 0x0, 0x0)
    0x31cdd10b: (Bool, 0x0, 0x0, 0x0)
    0x326fe50b: (Bool, 0x0, 0x0, 0x0)
    DisableDisasterRecovery2Temporary: (Bool, 0x0, 0x0, 0x0)
    LuaMathExceptionRemoval: (Bool, 0x0, 0x0, 0x0)
    LogLargePacketGaps: (Bool, 0x0, 0x0, 0x0)
    AsyncLoading: (Bool, 0x0, 0x0, 0x0)
    QueuedOrdersTriggerPreIssueOrder: (Bool, 0x0, 0x0, 0x0)
    0x356f0738: (Bool, 0x0, 0x0, 0x0)
    ItemShopRework: (Bool, 0x0, 0x0, 0x0)
    SpotlightDeathVfx: (Bool, 0x0, 0x0, 0x0)
    UseNewAssistBbEvent: (Bool, 0x0, 0x0, 0x0)
    IvernPromo: (Bool, 0x0, 0x0, 0x0)
    UseAStringFormatInChat: (Bool, 0x0, 0x0, 0x0)
    TftFxSequencer: (Bool, 0x0, 0x0, 0x0)
    ConeCheckFlagOverride: (Bool, 0x0, 0x0, 0x0)
    RenderUiPingMenu: (Bool, 0x0, 0x0, 0x0)
    0x3c52809c: (Bool, 0x0, 0x0, 0x0)
    0x3db7b821: (Bool, 0x0, 0x0, 0x0)
    AutoItemPurchasingUsesNewRecData: (Bool, 0x0, 0x0, 0x0)
    0x3e3cd6e2: (Bool, 0x0, 0x0, 0x0)
    0x3ee50ba: (Bool, 0x0, 0x0, 0x0)
    PenetrationAppliesToTurrets: (Bool, 0x0, 0x0, 0x0)
    FixAttackMoveWhileSnared: (Bool, 0x0, 0x0, 0x0)
    0x408974da: (Bool, 0x0, 0x0, 0x0)
    UseSpellOriginationForSpellShields: (Bool, 0x0, 0x0, 0x0)
    0x40ad2ab: (Bool, 0x0, 0x0, 0x0)
    0x40bae5a8: (Bool, 0x0, 0x0, 0x0)
    0x423020f6: (Bool, 0x0, 0x0, 0x0)
    mOrdersInteraction: (Bool, 0x0, 0x0, 0x0)
    0x44a74e8e: (Bool, 0x0, 0x0, 0x0)
    0x45033426: (Bool, 0x0, 0x0, 0x0)
    CastLockoutTime: (Bool, 0x0, 0x0, 0x0)
    0x453f4bfc: (Bool, 0x0, 0x0, 0x0)
    0x45bb110b: (Bool, 0x0, 0x0, 0x0)
    CloseOnEndGameAfterDelay: (Bool, 0x0, 0x0, 0x0)
    0x469d1769: (Bool, 0x0, 0x0, 0x0)
    ServerSendRevealToCastTargets: (Bool, 0x0, 0x0, 0x0)
    0x47271038: (Bool, 0x0, 0x0, 0x0)
    NewSpellCastFlowTargetInRange: (Bool, 0x0, 0x0, 0x0)
    DisableAutoSnr: (Bool, 0x0, 0x0, 0x0)
    0x4a379eef: (Bool, 0x0, 0x0, 0x0)
    NewDeathSfx: (Bool, 0x0, 0x0, 0x0)
    0x4c900772: (Bool, 0x0, 0x0, 0x0)
    UseNewSkinnedObjectOnAiBase: (Bool, 0x0, 0x0, 0x0)
    DisableSubFrameThrottles: (Bool, 0x0, 0x0, 0x0)
    DetachedAnimationParticlesUseOwnerVisibility: (Bool, 0x0, 0x0, 0x0)
    UseLegacyDamageFlow: (Bool, 0x0, 0x0, 0x0)
    DirectedTrackingElement: (Bool, 0x0, 0x0, 0x0)
    DefenseModifierIcons: (Bool, 0x0, 0x0, 0x0)
    InvulnerabilityHud: (Bool, 0x0, 0x0, 0x0)
    BbScriptProfileDump: (Bool, 0x0, 0x0, 0x0)
    0x5345fdd0: (Bool, 0x0, 0x0, 0x0)
    0x53660cda: (Bool, 0x0, 0x0, 0x0)
    LoadingIndicator: (Bool, 0x0, 0x0, 0x0)
    0x573d0238: (Bool, 0x0, 0x0, 0x0)
    0x57d3f2c8: (Bool, 0x0, 0x0, 0x0)
    0x5878582d: (Bool, 0x0, 0x0, 0x0)
    0x594309f4: (Bool, 0x0, 0x0, 0x0)
    TftPcItemPanel: (Bool, 0x0, 0x0, 0x0)
    HealthScarringFeedback: (Bool, 0x0, 0x0, 0x0)
    0x5a0599c9: (Bool, 0x0, 0x0, 0x0)
    CanLoadLuaFromLooseFiles: (Bool, 0x0, 0x0, 0x0)
    0x5a90bf57: (Bool, 0x0, 0x0, 0x0)
    AntiTrollPingAfterDeath: (Bool, 0x0, 0x0, 0x0)
    0x5cf29f42: (Bool, 0x0, 0x0, 0x0)
    UsePerksInsteadOfRunesAndMasteries: (Bool, 0x0, 0x0, 0x0)
    0x5f29b66e: (Bool, 0x0, 0x0, 0x0)
    0x609a78e3: (Bool, 0x0, 0x0, 0x0)
    TftLeagueClientTeamPlanner: (Bool, 0x0, 0x0, 0x0)
    0x61ad7bce: (Bool, 0x0, 0x0, 0x0)
    TenacityRework: (Bool, 0x0, 0x0, 0x0)
    0x625c69b3: (Bool, 0x0, 0x0, 0x0)
    0x62aaa28f: (Bool, 0x0, 0x0, 0x0)
    TowerCfhRadius: (Bool, 0x0, 0x0, 0x0)
    0x632dd61f: (Bool, 0x0, 0x0, 0x0)
    DisableRenderUiChatWindows: (Bool, 0x0, 0x0, 0x0)
    0x63a2e75e: (Bool, 0x0, 0x0, 0x0)
    ReconnectScriptsWhilePaused: (Bool, 0x0, 0x0, 0x0)
    0x6568cbd2: (Bool, 0x0, 0x0, 0x0)
    0x657aebdb: (Bool, 0x0, 0x0, 0x0)
    EnableUnitStatusHealthBarNames: (Bool, 0x0, 0x0, 0x0)
    UseGdsCvars: (Bool, 0x0, 0x0, 0x0)
    0x669c3f07: (Bool, 0x0, 0x0, 0x0)
    SpotModChampions: (Bool, 0x0, 0x0, 0x0)
    CursorUiUpdate: (Bool, 0x0, 0x0, 0x0)
    0x67fc3e09: (Bool, 0x0, 0x0, 0x0)
    PingAbilityIcons: (Bool, 0x0, 0x0, 0x0)
    GearAlwaysShowSubMeshes: (Bool, 0x0, 0x0, 0x0)
    ScriptHistoryIsAStack: (Bool, 0x0, 0x0, 0x0)
    TftmEmotePanel: (Bool, 0x0, 0x0, 0x0)
    NewSpellEffectCreateBlock: (Bool, 0x0, 0x0, 0x0)
    0x6a128e16: (Bool, 0x0, 0x0, 0x0)
    0x6a3a0f60: (Bool, 0x0, 0x0, 0x0)
    0x6b52ac28: (Bool, 0x0, 0x0, 0x0)
    0x6cb0ad77: (Bool, 0x0, 0x0, 0x0)
    0x6d9b5c59: (Bool, 0x0, 0x0, 0x0)
    0x6dbee4b7: (Bool, 0x0, 0x0, 0x0)
    BuildingBlocksDontLookToPtp: (Bool, 0x0, 0x0, 0x0)
    HideEnemySpellsOnLoadingScreen: (Bool, 0x0, 0x0, 0x0)
    0x6f0ba2b0: (Bool, 0x0, 0x0, 0x0)
    TftMatchupBanner: (Bool, 0x0, 0x0, 0x0)
    EnableCustomPlayerScoreColoring: (Bool, 0x0, 0x0, 0x0)
    0x714427a1: (Bool, 0x0, 0x0, 0x0)
    0x716bb231: (Bool, 0x0, 0x0, 0x0)
    PingMuting: (Bool, 0x0, 0x0, 0x0)
    0x7291eebc: (Bool, 0x0, 0x0, 0x0)
    0x734bc96f: (Bool, 0x0, 0x0, 0x0)
    0x746bb83: (Bool, 0x0, 0x0, 0x0)
    0x75399eee: (Bool, 0x0, 0x0, 0x0)
    0x76404ab5: (Bool, 0x0, 0x0, 0x0)
    TftReplicateSlotForUnit: (Bool, 0x0, 0x0, 0x0)
    0x768400a9: (Bool, 0x0, 0x0, 0x0)
    0x76e809b: (Bool, 0x0, 0x0, 0x0)
    0x776ffa5e: (Bool, 0x0, 0x0, 0x0)
    0x77727a47: (Bool, 0x0, 0x0, 0x0)
    0x7820b7cb: (Bool, 0x0, 0x0, 0x0)
    0x791348b4: (Bool, 0x0, 0x0, 0x0)
    0x79386a30: (Bool, 0x0, 0x0, 0x0)
    0x799f5177: (Bool, 0x0, 0x0, 0x0)
    0x7ab20157: (Bool, 0x0, 0x0, 0x0)
    0x7c3a50: (Bool, 0x0, 0x0, 0x0)
    VayneCondemnBugFix: (Bool, 0x0, 0x0, 0x0)
    NewSpellCastFlowSpellCastAns: (Bool, 0x0, 0x0, 0x0)
    DisableRenderUiChatFrames: (Bool, 0x0, 0x0, 0x0)
    0x7de343b9: (Bool, 0x0, 0x0, 0x0)
    0x7e32ef30: (Bool, 0x0, 0x0, 0x0)
    0x7e349260: (Bool, 0x0, 0x0, 0x0)
    0x7e3f91dc: (Bool, 0x0, 0x0, 0x0)
    0x7f4e17b2: (Bool, 0x0, 0x0, 0x0)
    TftTraitServerQueueing: (Bool, 0x0, 0x0, 0x0)
    RegularUpdateClock: (Bool, 0x0, 0x0, 0x0)
    VideoEncoding: (Bool, 0x0, 0x0, 0x0)
    0x81a2b226: (Bool, 0x0, 0x0, 0x0)
    0x81f65bdd: (Bool, 0x0, 0x0, 0x0)
    0x82799f80: (Bool, 0x0, 0x0, 0x0)
    0x82cdcf2e: (Bool, 0x0, 0x0, 0x0)
    IgnoreReactivationForOutsideUndoFlowItems: (Bool, 0x0, 0x0, 0x0)
    HeathBarShake: (Bool, 0x0, 0x0, 0x0)
    MissileTransitionSpecs: (Bool, 0x0, 0x0, 0x0)
    0x84571e63: (Bool, 0x0, 0x0, 0x0)
    GetAcquisitionRangeUsesAttackRange: (Bool, 0x0, 0x0, 0x0)
    0x84fe7ccf: (Bool, 0x0, 0x0, 0x0)
    0x85af0cb5: (Bool, 0x0, 0x0, 0x0)
    SruRiftHerald: (Bool, 0x0, 0x0, 0x0)
    MissileStartTimeAccountsForCastTime: (Bool, 0x0, 0x0, 0x0)
    TrackObjectiveSteal: (Bool, 0x0, 0x0, 0x0)
    0x88fa2040: (Bool, 0x0, 0x0, 0x0)
    0x8907b1d1: (Bool, 0x0, 0x0, 0x0)
    0x898c0b97: (Bool, 0x0, 0x0, 0x0)
    0x89c520b4: (Bool, 0x0, 0x0, 0x0)
    SelectivelyClearActiveSpellOnTargetInRange: (Bool, 0x0, 0x0, 0x0)
    UseOverideAttackSpeedForAutoAttackTime: (Bool, 0x0, 0x0, 0x0)
    0x8bc44dc3: (Bool, 0x0, 0x0, 0x0)
    0x8c78ffd9: (Bool, 0x0, 0x0, 0x0)
    0x8cd3b1f9: (Bool, 0x0, 0x0, 0x0)
    UseAsyncChatClient: (Bool, 0x0, 0x0, 0x0)
    0x8ce38003: (Bool, 0x0, 0x0, 0x0)
    UnitsOnlyMoveForward: (Bool, 0x0, 0x0, 0x0)
    0x8d128b15: (Bool, 0x0, 0x0, 0x0)
    0x8d34e29: (Bool, 0x0, 0x0, 0x0)
    0x8dc6f20a: (Bool, 0x0, 0x0, 0x0)
    0x8ddcecfb: (Bool, 0x0, 0x0, 0x0)
    SummonerEmotesV2: (Bool, 0x0, 0x0, 0x0)
    TftTraitTrackerClarityUpdate: (Bool, 0x0, 0x0, 0x0)
    0x8f7ab49e: (Bool, 0x0, 0x0, 0x0)
    AsynchronousClientNetworking: (Bool, 0x0, 0x0, 0x0)
    MissileOwnInstanceVars: (Bool, 0x0, 0x0, 0x0)
    0x90e08cc7: (Bool, 0x0, 0x0, 0x0)
    0x92187457: (Bool, 0x0, 0x0, 0x0)
    DisableRenderUiChatOsx: (Bool, 0x0, 0x0, 0x0)
    PathfindingLevelMovementRestriction: (Bool, 0x0, 0x0, 0x0)
    ReduceClientCameraReplication: (Bool, 0x0, 0x0, 0x0)
    NewTurretLogic: (Bool, 0x0, 0x0, 0x0)
    0x9325b779: (Bool, 0x0, 0x0, 0x0)
    0x9367bdcb: (Bool, 0x0, 0x0, 0x0)
    0x937aae2c: (Bool, 0x0, 0x0, 0x0)
    InGameReportAndMuteModal: (Bool, 0x0, 0x0, 0x0)
    RetryFailedSpellLoad: (Bool, 0x0, 0x0, 0x0)
    0x940caeb7: (Bool, 0x0, 0x0, 0x0)
    0x94d35de1: (Bool, 0x0, 0x0, 0x0)
    MissileReflectionPrototype: (Bool, 0x0, 0x0, 0x0)
    PingWheelClarityExploration: (Bool, 0x0, 0x0, 0x0)
    PostponeTargetSpellOrders: (Bool, 0x0, 0x0, 0x0)
    AsynchronousNetworking: (Bool, 0x0, 0x0, 0x0)
    ShowMinimapIconBorders: (Bool, 0x0, 0x0, 0x0)
    HorizontalRulesInSpellTooltips: (Bool, 0x0, 0x0, 0x0)
    0x997ceb66: (Bool, 0x0, 0x0, 0x0)
    DisplayVisionScoreOnScoreboard: (Bool, 0x0, 0x0, 0x0)
    0x9a0588ef: (Bool, 0x0, 0x0, 0x0)
    0x9b710bf6: (Bool, 0x0, 0x0, 0x0)
    0x9bdbe0d8: (Bool, 0x0, 0x0, 0x0)
    UseCharHealthBarHeightProperty: (Bool, 0x0, 0x0, 0x0)
    CannonMinionLaneRotation: (Bool, 0x0, 0x0, 0x0)
    DontRefCountTargetableAndInvulnerable: (Bool, 0x0, 0x0, 0x0)
    FountainTickRestoresHpPenalty: (Bool, 0x0, 0x0, 0x0)
    OmnivampStat: (Bool, 0x0, 0x0, 0x0)
    RecItemsOnServer: (Bool, 0x0, 0x0, 0x0)
    0x9fa032f6: (Bool, 0x0, 0x0, 0x0)
    0x9ff95a2d: (Bool, 0x0, 0x0, 0x0)
    0xa0c45184: (Bool, 0x0, 0x0, 0x0)
    BaublesSpell: (Bool, 0x0, 0x0, 0x0)
    0xa1f9e134: (Bool, 0x0, 0x0, 0x0)
    0xa28bbddc: (Bool, 0x0, 0x0, 0x0)
    0xa37558af: (Bool, 0x0, 0x0, 0x0)
    BbNewBlockOnly: (Bool, 0x0, 0x0, 0x0)
    0xa3f47862: (Bool, 0x0, 0x0, 0x0)
    CursorScaling: (Bool, 0x0, 0x0, 0x0)
    DisableDdr: (Bool, 0x0, 0x0, 0x0)
    0xa525fa4b: (Bool, 0x0, 0x0, 0x0)
    ToggleSpellOutlineVisualOnly: (Bool, 0x0, 0x0, 0x0)
    KdaObjectivesDisplay: (Bool, 0x0, 0x0, 0x0)
    0xa66b49f5: (Bool, 0x0, 0x0, 0x0)
    DamageFlowTakeDealDamageFlip: (Bool, 0x0, 0x0, 0x0)
    UseTauntsForFirstEncounterCac: (Bool, 0x0, 0x0, 0x0)
    TftCollapsibleStageUi: (Bool, 0x0, 0x0, 0x0)
    ShowOpposingSummonerSpellsCooldown: (Bool, 0x0, 0x0, 0x0)
    MaxSlowDoesntRoot: (Bool, 0x0, 0x0, 0x0)
    0xa872224: (Bool, 0x0, 0x0, 0x0)
    UnlimitedSpellBuffs: (Bool, 0x0, 0x0, 0x0)
    0xaa0e2074: (Bool, 0x0, 0x0, 0x0)
    0xaa0fcb5: (Bool, 0x0, 0x0, 0x0)
    0xaa45fab6: (Bool, 0x0, 0x0, 0x0)
    TftMobileCameraTp: (Bool, 0x0, 0x0, 0x0)
    0xacc83ffa: (Bool, 0x0, 0x0, 0x0)
    BbGetModifiedCooldownConverted: (Bool, 0x0, 0x0, 0x0)
    MomentsUi: (Bool, 0x0, 0x0, 0x0)
    0xadfc3179: (Bool, 0x0, 0x0, 0x0)
    CallForHelpSpike: (Bool, 0x0, 0x0, 0x0)
    0xb059e275: (Bool, 0x0, 0x0, 0x0)
    MomentOfDeathStructures: (Bool, 0x0, 0x0, 0x0)
    MinionsStickToTowers: (Bool, 0x0, 0x0, 0x0)
    0xb0b637a4: (Bool, 0x0, 0x0, 0x0)
    0xb21e74b1: (Bool, 0x0, 0x0, 0x0)
    0xb25d4b37: (Bool, 0x0, 0x0, 0x0)
    0xb2d248f: (Bool, 0x0, 0x0, 0x0)
    0xb373c3ab: (Bool, 0x0, 0x0, 0x0)
    CooldownSpellQueueing: (Bool, 0x0, 0x0, 0x0)
    RunPlaybackSpeedForTransitions: (Bool, 0x0, 0x0, 0x0)
    0xb56c3d3d: (Bool, 0x0, 0x0, 0x0)
    0xb5743397: (Bool, 0x0, 0x0, 0x0)
    MinionLevelEvents: (Bool, 0x0, 0x0, 0x0)
    RuneBerserkRefactorsOn: (Bool, 0x0, 0x0, 0x0)
    TftCustomisedGameStart: (Bool, 0x0, 0x0, 0x0)
    TftUnitCombatUpdate: (Bool, 0x0, 0x0, 0x0)
    UseRiotRelationshipsForAllUnits: (Bool, 0x0, 0x0, 0x0)
    TftKeywords: (Bool, 0x0, 0x0, 0x0)
    UseRollForCriticalHit: (Bool, 0x0, 0x0, 0x0)
    0xbc0ba76a: (Bool, 0x0, 0x0, 0x0)
    UpdatedParabolicMovementMath: (Bool, 0x0, 0x0, 0x0)
    UnifiedClock: (Bool, 0x0, 0x0, 0x0)
    SpotlightHealthbar: (Bool, 0x0, 0x0, 0x0)
    ChannelingEndAutoAttackReset: (Bool, 0x0, 0x0, 0x0)
    RestoreLuaStackAfterException: (Bool, 0x0, 0x0, 0x0)
    0xbe6b5158: (Bool, 0x0, 0x0, 0x0)
    FixAccidentalAttackWhileSnared: (Bool, 0x0, 0x0, 0x0)
    FirstTimeUserExperience: (Bool, 0x0, 0x0, 0x0)
    0xc05ca3fa: (Bool, 0x0, 0x0, 0x0)
    SpotlightEogStatsLogging: (Bool, 0x0, 0x0, 0x0)
    UpdatedEmoteWheel: (Bool, 0x0, 0x0, 0x0)
    0xc25a56fb: (Bool, 0x0, 0x0, 0x0)
    RenderMiniMapToTexture: (Bool, 0x0, 0x0, 0x0)
    0xc2cad416: (Bool, 0x0, 0x0, 0x0)
    NewSpellScript: (Bool, 0x0, 0x0, 0x0)
    0xc4be5b2e: (Bool, 0x0, 0x0, 0x0)
    UseTargetingRefactor: (Bool, 0x0, 0x0, 0x0)
    0xc65a770d: (Bool, 0x0, 0x0, 0x0)
    0xc702f2f0: (Bool, 0x0, 0x0, 0x0)
    0xc779da22: (Bool, 0x0, 0x0, 0x0)
    ItemSets: (Bool, 0x0, 0x0, 0x0)
    0xc7d1098: (Bool, 0x0, 0x0, 0x0)
    0xc83a8247: (Bool, 0x0, 0x0, 0x0)
    0xc9570bbd: (Bool, 0x0, 0x0, 0x0)
    0xcad3d457: (Bool, 0x0, 0x0, 0x0)
    0xcb5747c1: (Bool, 0x0, 0x0, 0x0)
    0xcbbb0b9: (Bool, 0x0, 0x0, 0x0)
    CanCritAllies: (Bool, 0x0, 0x0, 0x0)
    0xcc5e3f8d: (Bool, 0x0, 0x0, 0x0)
    0xccaa09c4: (Bool, 0x0, 0x0, 0x0)
    0xcd2f9591: (Bool, 0x0, 0x0, 0x0)
    0xcd83b02f: (Bool, 0x0, 0x0, 0x0)
    SpellsCheckTheirAmmoRequirement: (Bool, 0x0, 0x0, 0x0)
    0xcdefc3d7: (Bool, 0x0, 0x0, 0x0)
    0xcdf0c145: (Bool, 0x0, 0x0, 0x0)
    UseAtBoundingCircles: (Bool, 0x0, 0x0, 0x0)
    0xcf600445: (Bool, 0x0, 0x0, 0x0)
    0xcf756228: (Bool, 0x0, 0x0, 0x0)
    0xcf9a337d: (Bool, 0x0, 0x0, 0x0)
    TftRegularUpdateClock: (Bool, 0x0, 0x0, 0x0)
    0xd14a06e7: (Bool, 0x0, 0x0, 0x0)
    AttackSpeedCatchup: (Bool, 0x0, 0x0, 0x0)
    OffScreenPointOfInterestSystem: (Bool, 0x0, 0x0, 0x0)
    TftPcNewInfoCard: (Bool, 0x0, 0x0, 0x0)
    0xd3488584: (Bool, 0x0, 0x0, 0x0)
    0xd41cb329: (Bool, 0x0, 0x0, 0x0)
    0xd4902062: (Bool, 0x0, 0x0, 0x0)
    0xd7a639de: (Bool, 0x0, 0x0, 0x0)
    TftFinisher: (Bool, 0x0, 0x0, 0x0)
    CcScore: (Bool, 0x0, 0x0, 0x0)
    RiftHeraldUpdate: (Bool, 0x0, 0x0, 0x0)
    StopAttackVerifiesSpell: (Bool, 0x0, 0x0, 0x0)
    0xdb71e9dd: (Bool, 0x0, 0x0, 0x0)
    0xdc49d737: (Bool, 0x0, 0x0, 0x0)
    0xdc921370: (Bool, 0x0, 0x0, 0x0)
    AbilityResetUi: (Bool, 0x0, 0x0, 0x0)
    PhysicalVampStat: (Bool, 0x0, 0x0, 0x0)
    0xdf6d671d: (Bool, 0x0, 0x0, 0x0)
    NewSpellCastFlow: (Bool, 0x0, 0x0, 0x0)
    TftUnrestrictedArenaCamera: (Bool, 0x0, 0x0, 0x0)
    0xe1a305aa: (Bool, 0x0, 0x0, 0x0)
    0xe243d4b5: (Bool, 0x0, 0x0, 0x0)
    0xe2970c5c: (Bool, 0x0, 0x0, 0x0)
    0xe32af589: (Bool, 0x0, 0x0, 0x0)
    0xe35749fa: (Bool, 0x0, 0x0, 0x0)
    0xe3c45501: (Bool, 0x0, 0x0, 0x0)
    0xe3fe9469: (Bool, 0x0, 0x0, 0x0)
    ActiveSpellFix: (Bool, 0x0, 0x0, 0x0)
    0xe5b3a75d: (Bool, 0x0, 0x0, 0x0)
    0xe759b66e: (Bool, 0x0, 0x0, 0x0)
    mNewSpellCastFlowToggles: (Embed, 0x0, 0x0, NewSpellCastFlowToggles)
    0xe7a9fb51: (Bool, 0x0, 0x0, 0x0)
    0xeaee5d02: (Bool, 0x0, 0x0, 0x0)
    LimitedTournamentPause: (Bool, 0x0, 0x0, 0x0)
    UseNewOnKillEvent: (Bool, 0x0, 0x0, 0x0)
    0xed60b862: (Bool, 0x0, 0x0, 0x0)
    NotFacingMovementWhenCasting: (Bool, 0x0, 0x0, 0x0)
    0xefe584bb: (Bool, 0x0, 0x0, 0x0)
    LiveClientDataApi: (Bool, 0x0, 0x0, 0x0)
    UseNativeJungleBrain: (Bool, 0x0, 0x0, 0x0)
    ResistVisualization: (Bool, 0x0, 0x0, 0x0)
    ItemUndo: (Bool, 0x0, 0x0, 0x0)
    BbConvertedBlockSoon: (Bool, 0x0, 0x0, 0x0)
    UseAchievements: (Bool, 0x0, 0x0, 0x0)
    0xf4caaaa8: (Bool, 0x0, 0x0, 0x0)
    0xf5b171f3: (Bool, 0x0, 0x0, 0x0)
    ClampTimeToAnimateCastTo0: (Bool, 0x0, 0x0, 0x0)
    DamageTakenPie: (Bool, 0x0, 0x0, 0x0)
    RemoveNullRepMrgTemp: (Bool, 0x0, 0x0, 0x0)
    0xf925c65b: (Bool, 0x0, 0x0, 0x0)
    0xf954c78f: (Bool, 0x0, 0x0, 0x0)
    UseNewBountyTech: (Bool, 0x0, 0x0, 0x0)
    0xf9b5e2b0: (Bool, 0x0, 0x0, 0x0)
    0xf9bf0fa9: (Bool, 0x0, 0x0, 0x0)
    0xf9d69266: (Bool, 0x0, 0x0, 0x0)
    UseNewFireBbEvents: (Bool, 0x0, 0x0, 0x0)
    0xfad8c148: (Bool, 0x0, 0x0, 0x0)
    NewTowerFortification: (Bool, 0x0, 0x0, 0x0)
    0xfb2ae6aa: (Bool, 0x0, 0x0, 0x0)
    NewSpellCastFlowLaunchAttack: (Bool, 0x0, 0x0, 0x0)
    0xfc0dc481: (Bool, 0x0, 0x0, 0x0)
    0xfcd7d881: (Bool, 0x0, 0x0, 0x0)
    UseDefaultPerksOnError: (Bool, 0x0, 0x0, 0x0)
    0xff6037fe: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xc7e628b9():
    SpellLevelOverride: (I32, 0x0, 0x0, 0x0)
    0x2ba4fd8f: (Hash, 0x0, 0x0, 0x0)
    0xa2877ddb: (Hash, 0x0, 0x0, 0x0)
    Spell: (Hash, 0x0, 0x0, 0x0)
    0xd00e123a: (Hash, 0x0, 0x0, 0x0)
    pass

class RsValueGet():
    pass

class EmoteIdIntDriver(ILogicIntDriver):
    pass

class TftHeightSolverType():
    pass

class UiElementEffectGlowConstantData(UiElementEffectData):
    FlipX: (Bool, 0x0, 0x0, 0x0)
    FlipY: (Bool, 0x0, 0x0, 0x0)
    MinimumGlowMod: (F32, 0x0, 0x0, 0x0)
    MaximumGlowMod: (F32, 0x0, 0x0, 0x0)
    Atlas: (Pointer, 0x0, 0x0, AtlasData)
    Atlas: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    TextureData: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    PerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    pass

class UiMetricBattery(UiMetricTypeI):
    BatteryLevelIcons: (List, 0xa, Hash, 0x0)
    pass

class 0xc83d315a():
    MapLightInfo: (Embed, 0x0, 0x0, MapLightingInfo)
    CubemapPath: (String, 0x0, 0x0, 0x0)
    CubemapProbeGuid: (String, 0x0, 0x0, 0x0)
    CubemapScale: (F32, 0x0, 0x0, 0x0)
    pass

class 0xc83dc592(0x66b38743):
    MutatorName: (String, 0x0, 0x0, 0x0)
    pass

class MissileTriggerSpec(MissileBehaviorSpec):
    mActions: (List, 0x0, Pointer, MissileTriggeredActionSpec)
    pass

class ContextualConditionCharacterSkinId(ICharacterSubcondition):
    mSkinIds: (List, 0x0, I32, 0x0)
    pass

class TftReturnToBoardViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    Button: (Hash, 0x0, 0x0, 0x0)
    HomeIconHandle: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    ArmoryTimeoutVfx: (Hash, 0x0, 0x0, 0x0)
    SceneHandle: (Hash, 0x0, 0x0, 0x0)
    DraftIconHandle: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xc8879e6c(0x8b33cf88):
    Value: (U32, 0x0, 0x0, 0x0)
    pass

class OneTrueMaterialDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    mDrivers: (List, 0x0, Pointer, ILogicBoolDriver)
    mDrivers: (List, 0x0, Pointer, IDynamicMaterialBoolDriver)
    pass

class HeroFloatingInfoCharacterStateIndicatorData():
    CharacterStatesMap: (Map, Hash, Embed, HeroFloatingInfoCharacterStateIndicatorList)
    pass

class QuestUiTunables():
    mSceneTransition: (Embed, 0x0, 0x0, HudMenuTransitionData)
    pass

class OptionTemplateSecondaryHotkeys1Column(IOptionTemplate):
    RowButtonColumn1: (Embed, 0x0, 0x0, OptionTemplateSecondaryHotkeys_Button)
    HeadingRowLabel1: (Embed, 0x0, 0x0, OptionTemplateSecondaryHotkeys_Label)
    HeadingRowLabel0: (Embed, 0x0, 0x0, OptionTemplateSecondaryHotkeys_Label)
    BoundsElement: (Hash, 0x0, 0x0, 0x0)
    RowLabelColumn0: (Embed, 0x0, 0x0, OptionTemplateSecondaryHotkeys_Label)
    pass

class ParametricPairData():
    mValue: (F32, 0x0, 0x0, 0x0)
    mClipId: (U32, 0x0, 0x0, 0x0)
    mClipName: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xc90736f4():
    Rows: (List2, 0x0, Embed, 0xfacd8b68)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class LeagueFlavor():
    IndividualBannerOverrides: (List, 0x0, Embed, SponsoredBanner)
    FlavorName: (String, 0x0, 0x0, 0x0)
    pass

class AiGenericClient(AiGenericCommon):
    pass

class UiPositionFullScreen(UiPositionBase):
    pass

class 0xc93653c7(0x87a6a884):
    pass

class 0xc9440657():
    pass

class IsMapPropHoveredDynamicMaterialBoolDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    pass

class HudReciprocityButton():
    Button: (Hash, 0x0, 0x0, 0x0)
    HotkeyText: (Hash, 0x0, 0x0, 0x0)
    ProgressFill: (Hash, 0x0, 0x0, 0x0)
    pass

class ObjectiveVoteCampDefinition():
    CampIndex: (U32, 0x0, 0x0, 0x0)
    PortraitIcon: (Hash, 0x0, 0x0, 0x0)
    ObjectiveName: (String, 0x0, 0x0, 0x0)
    pass

class 0xc993142a():
    RewardFrame: (Hash, 0x0, 0x0, 0x0)
    RewardBackground: (Hash, 0x0, 0x0, 0x0)
    RewardIcon: (Hash, 0x0, 0x0, 0x0)
    RewardDayText: (Hash, 0x0, 0x0, 0x0)
    Parent: (Hash, 0x0, 0x0, 0x0)
    pass

class AssistCountFilter(IStatStoneLogicDriver):
    AssistCount: (U8, 0x0, 0x0, 0x0)
    pass

class 0xc9dd46d2():
    pass

class UiElementScissorRegionData(UiElementData):
    SceneToScissor: (Link, 0x0, 0x0, UiSceneData)
    SceneToScissor: (Link, 0x0, 0x0, SceneData)
    mSceneToScissor: (Link, 0x0, 0x0, SceneData)
    pass

class RespawnPointData():
    FirstSpawnPositionOffset: (Vec3, 0x0, 0x0, 0x0)
    AlwaysRespawnWithOffset: (Bool, 0x0, 0x0, 0x0)
    Team: (U32, 0x0, 0x0, 0x0)
    pass

class TftUnitInfoTraitDisplayData():
    Highlight: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xca1b1bdd(0x2755f1f9):
    Axis: (Vec2, 0x0, 0x0, 0x0)
    GapWidth: (F32, 0x0, 0x0, 0x0)
    SideLength: (F32, 0x0, 0x0, 0x0)
    pass

class VfxSpawnConditionData():
    mPersistentVfxs: (List, 0x0, Embed, EffectCreationData)
    pass

class TftUnitFloatingInfoBarData(FloatingInfoBarData):
    Highlight: (Hash, 0x0, 0x0, 0x0)
    Border: (Hash, 0x0, 0x0, 0x0)
    Healthbar: (Embed, 0x0, 0x0, HealthBarData)
    Healthbar: (Pointer, 0x0, 0x0, HealthBarData)
    ParBar: (Embed, 0x0, 0x0, AbilityResourceBarData)
    ParBar: (Pointer, 0x0, 0x0, AbilityResourceBarData)
    AttachmentSlots: (Embed, 0x0, 0x0, TftUnitAttachmentSlotsData)
    InspectButton: (Hash, 0x0, 0x0, 0x0)
    pass

class RatioConversion():
    mResultingStatType: (U8, 0x0, 0x0, 0x0)
    mSourceToResultConversionRatio: (F32, 0x0, 0x0, 0x0)
    mSourceStatType: (U8, 0x0, 0x0, 0x0)
    mSourceStatOutput: (U8, 0x0, 0x0, 0x0)
    mResultingStatOutput: (U8, 0x0, 0x0, 0x0)
    pass

class 0xca458424(ILogicFloatDriver):
    VisibilityController: (Link, 0x0, 0x0, IMapVisibilityController)
    pass

class HudShopButton():
    ShopButton: (Hash, 0x0, 0x0, 0x0)
    TextLink: (Hash, 0x0, 0x0, 0x0)
    InactiveIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xca4d32d1():
    pass

class 0xca7e5285(ILolSpellScriptEvent):
    pass

class OverrideAutoAttackCastTimeData():
    mOverrideAutoattackCastTimeCalculation: (Pointer, 0x0, 0x0, IGameCalculation)
    pass

class UiElementAssetData(UiElementData):
    pass

class AiMinionClient(AiMinionCommon):
    pass

class 0xcaace5db(ViewController):
    pass

class IContextualCondition():
    pass

class NudgeIntoBrush(TargetingTypeData):
    NudgeDistance: (F32, 0x0, 0x0, 0x0)
    pass

class FixedTimeSplineMovement(GenericSplineMovementSpec):
    mTravelTime: (F32, 0x0, 0x0, 0x0)
    pass

class ContextualConditionCharacterInRangeForSyncedAnimation(ICharacterSubcondition):
    pass

class OptionTemplateBorder(IOptionTemplate):
    Border: (Hash, 0x0, 0x0, 0x0)
    pass

class LoginRootScene(RootScene):
    pass

class TargetingRangeValue(ITargetingRangeValue):
    Range: (F32, 0x0, 0x0, 0x0)
    pass

class 0xcb3604f0(IScriptCondition):
    Emote: (U8, 0x0, 0x0, 0x0)
    pass

class DefaultVisibilitySpec(MissileVisibilitySpec):
    pass

class 0xcb3cb339(0x6a6e3b03):
    0x33f49d23: (F32, 0x0, 0x0, 0x0)
    0x49a9c7a8: (F32, 0x0, 0x0, 0x0)
    0xb610e02e: (List, 0x0, U8, 0x0)
    pass

class UiMetricFps(UiMetricTypeI):
    FpsText: (Hash, 0x0, 0x0, 0x0)
    pass

class VertexAnimationRigPoseModifierData(BaseRigPoseModifierData):
    mFrequency: (F32, 0x0, 0x0, 0x0)
    mMaxVelocityContribution: (F32, 0x0, 0x0, 0x0)
    mMaxAmplitude: (F32, 0x0, 0x0, 0x0)
    mMass: (F32, 0x0, 0x0, 0x0)
    mDamping: (F32, 0x0, 0x0, 0x0)
    mStiffness: (F32, 0x0, 0x0, 0x0)
    mMaxSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class TftCutsceneObjVfxClip(TftCutsceneVfxClip):
    HideWhenNotViewed: (Bool, 0x0, 0x0, 0x0)
    0x1d6290fe: (String, 0x0, 0x0, 0x0)
    0x2558e68b: (Bool, 0x0, 0x0, 0x0)
    BlackboardTargetObject: (String, 0x0, 0x0, 0x0)
    0xce35e628: (String, 0x0, 0x0, 0x0)
    TargetBone: (String, 0x0, 0x0, 0x0)
    pass

class IOptionItemFilter():
    pass

class ScriptBtRandomWeightedSelector(IScriptBt, IScriptSequence):
    Blocks: (List2, 0x0, Pointer, IScriptBlock)
    Blocks: (List2, 0x0, Pointer, IBehaviorScriptBlock)
    Percentages: (List2, 0x0, Pointer, IIntGet)
    pass

class TftChangeDamageSkinCheat(Cheat):
    pass

class MapAction():
    StartTime: (F32, 0x0, 0x0, 0x0)
    pass

class UnitStatusTemplate():
    mBarElement: (Embed, 0x0, 0x0, BarElement)
    InterruptibleImmobilize: (String, 0x0, 0x0, 0x0)
    Charmed: (String, 0x0, 0x0, 0x0)
    Grounded: (String, 0x0, 0x0, 0x0)
    InterruptibleDisable: (String, 0x0, 0x0, 0x0)
    Disarmed: (String, 0x0, 0x0, 0x0)
    Resurrecting: (String, 0x0, 0x0, 0x0)
    Stunned: (String, 0x0, 0x0, 0x0)
    Unstoppable: (String, 0x0, 0x0, 0x0)
    Taunted: (String, 0x0, 0x0, 0x0)
    UnSlowable: (String, 0x0, 0x0, 0x0)
    Suppressed: (String, 0x0, 0x0, 0x0)
    Rooted: (String, 0x0, 0x0, 0x0)
    Blinded: (String, 0x0, 0x0, 0x0)
    Nearsighted: (String, 0x0, 0x0, 0x0)
    Drowsy: (String, 0x0, 0x0, 0x0)
    Silenced: (String, 0x0, 0x0, 0x0)
    Polymorphed: (String, 0x0, 0x0, 0x0)
    InterruptibleDamage: (String, 0x0, 0x0, 0x0)
    mIcons: (Embed, 0x0, 0x0, UnitStatusIcons)
    Airborne: (String, 0x0, 0x0, 0x0)
    Fleeing: (String, 0x0, 0x0, 0x0)
    Asleep: (String, 0x0, 0x0, 0x0)
    pass

class LoadingScreenPlayerCardBaseData():
    MainScene: (Hash, 0x0, 0x0, 0x0)
    StateScenes: (List, 0x0, Hash, 0x0)
    HitRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class HudLoadingScreenWidgetPing(IHudLoadingScreenWidget):
    mPingThresholdGreen: (U32, 0x0, 0x0, 0x0)
    mPingThresholdOrange: (U32, 0x0, 0x0, 0x0)
    mPingThresholdYellow: (U32, 0x0, 0x0, 0x0)
    mPingThresholdRed: (U32, 0x0, 0x0, 0x0)
    mDebugPing: (U32, 0x0, 0x0, 0x0)
    pass

class DestroyCustomTableBlock(IScriptBlock):
    TableName: (Embed, 0x0, 0x0, CustomTableSet)
    CustomTable: (Embed, 0x0, 0x0, CustomTableSet)
    pass

class TftCurrencyWidget():
    TooltipOffsetY: (F32, 0x0, 0x0, 0x0)
    TooltipOffsetX: (F32, 0x0, 0x0, 0x0)
    0x3b061cb9: (Bool, 0x0, 0x0, 0x0)
    TooltipTitleTra: (String, 0x0, 0x0, 0x0)
    TooltipDescriptionTra: (String, 0x0, 0x0, 0x0)
    CurrencyButton: (Hash, 0x0, 0x0, 0x0)
    TooltipButton: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xcc2c0827():
    BaseHoverGlow: (Hash, 0x0, 0x0, 0x0)
    0xd3467f57: (Hash, 0x0, 0x0, 0x0)
    pass

class BlendData():
    mBlendTime: (F32, 0x0, 0x0, 0x0)
    mToAnimId: (U32, 0x0, 0x0, 0x0)
    mBlendFlags: (U32, 0x0, 0x0, 0x0)
    mFromAnimId: (U32, 0x0, 0x0, 0x0)
    pass

class 0xcc35f742(0xf9e5b8b9):
    Denominator: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class TftDragDropGroupProperty():
    DropHoverAnimName: (String, 0x0, 0x0, 0x0)
    DropThreshold: (F32, 0x0, 0x0, 0x0)
    DropHoverEndAnimName: (String, 0x0, 0x0, 0x0)
    0x7f78e1a0: (Bool, 0x0, 0x0, 0x0)
    AnimationThreshold: (F32, 0x0, 0x0, 0x0)
    HoverStartVfxName: (String, 0x0, 0x0, 0x0)
    DragGroup: (U32, 0x0, 0x0, 0x0)
    pass

class TftUnitInfoItemDisplayData():
    Button: (Hash, 0x0, 0x0, 0x0)
    ItemsOnlyIcon: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class MapLightingInfo():
    PbrSunAdditionalScale: (F32, 0x0, 0x0, 0x0)
    FogColor: (Vec4, 0x0, 0x0, 0x0)
    FogEmissiveRemap: (F32, 0x0, 0x0, 0x0)
    FogLowQualityModeEmissiveRemap: (F32, 0x0, 0x0, 0x0)
    SunIntensityScale: (F32, 0x0, 0x0, 0x0)
    FogAlternateColor: (Vec4, 0x0, 0x0, 0x0)
    GroundColor: (Vec4, 0x0, 0x0, 0x0)
    SunColor: (Vec4, 0x0, 0x0, 0x0)
    FogStartAndEnd: (Vec2, 0x0, 0x0, 0x0)
    FogEnabled: (Bool, 0x0, 0x0, 0x0)
    LightMapColorScale: (F32, 0x0, 0x0, 0x0)
    OverrideSunSpecDirection: (Option, 0x0, Vec3, 0x0)
    SkyLightColor: (Vec4, 0x0, 0x0, 0x0)
    SkyLightScale: (F32, 0x0, 0x0, 0x0)
    ScaleSunShadowIntensity: (F32, 0x0, 0x0, 0x0)
    0xc6d048fc: (F32, 0x0, 0x0, 0x0)
    ShadowBias: (F32, 0x0, 0x0, 0x0)
    SunRadiusForShadows: (F32, 0x0, 0x0, 0x0)
    SunDirection: (Vec3, 0x0, 0x0, 0x0)
    HorizonColor: (Vec4, 0x0, 0x0, 0x0)
    pass

class ContextualConditionCharacterHasCac(ICharacterSubcondition):
    mCacs: (List, 0x0, Hash, 0x0)
    pass

class RefundDialogViewController(ModalDialogViewController):
    RefundTitleText: (Hash, 0x0, 0x0, 0x0)
    RefundButton: (Hash, 0x0, 0x0, 0x0)
    RefundBodyText: (Hash, 0x0, 0x0, 0x0)
    pass

class HasReceivedAnimEmoteEventBoolDriver(ILogicBoolDriver):
    pass

class KeyFrameFloatClipReaderDriver(ILogicFloatDriver):
    DefaultFloat: (F32, 0x0, 0x0, 0x0)
    ClipAccessoryToRead: (Hash, 0x0, 0x0, 0x0)
    StartFloat: (F32, 0x0, 0x0, 0x0)
    PersistentFloatChanges: (Bool, 0x0, 0x0, 0x0)
    0xba092281: (Bool, 0x0, 0x0, 0x0)
    pass

class SpringPhysicsRigPoseModifierData(BaseRigPoseModifierData):
    SpringStiffness: (F32, 0x0, 0x0, 0x0)
    Invert: (Bool, 0x0, 0x0, 0x0)
    DoRotation: (Bool, 0x0, 0x0, 0x0)
    DoTranslation: (Bool, 0x0, 0x0, 0x0)
    MaxAngle: (F32, 0x0, 0x0, 0x0)
    Name: (Hash, 0x0, 0x0, 0x0)
    Joint: (Hash, 0x0, 0x0, 0x0)
    Damping: (F32, 0x0, 0x0, 0x0)
    DefaultOn: (Bool, 0x0, 0x0, 0x0)
    Mass: (F32, 0x0, 0x0, 0x0)
    MaxDistance: (F32, 0x0, 0x0, 0x0)
    pass

class TftMapModeData():
    ActiveSets: (List, 0x0, Pointer, TftMapSetData)
    DefaultSet: (Pointer, 0x0, 0x0, TftMapSetData)
    pass

class 0xccb78d30(IFxActionInstance):
    pass

class 0xccb921b(0x9a573886):
    DelayTimeDriver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class SocialPanelFriendsListItemData():
    SelectedHighlightTexture: (Hash, 0x0, 0x0, 0x0)
    ClickRegion: (Hash, 0x0, 0x0, 0x0)
    UnreadMessagesBadgeVfx: (Hash, 0x0, 0x0, 0x0)
    PlayerIcon: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    ActiveInviteButton: (Hash, 0x0, 0x0, 0x0)
    StatusText: (Hash, 0x0, 0x0, 0x0)
    NameText: (Hash, 0x0, 0x0, 0x0)
    StatusIcons: (Embed, 0x0, 0x0, SocialStatusIcons)
    pass

class UiMetricMultiDragonKillsSrX(UiMetricTypeI):
    SourceIcons: (List, 0x0, Hash, 0x0)
    SoulSlot: (Pointer, 0x0, 0x0, MultiDragonSoulSlotUiData)
    Team2IconSlots: (List, 0x0, Hash, 0x0)
    Team1IconSlots: (List, 0x0, Hash, 0x0)
    DragonNames: (List, 0x0, String, 0x0)
    TeamSlotDisabledIcon: (Hash, 0x0, 0x0, 0x0)
    DragonTypeIcons: (Map, Hash, Embed, MultiDragonTypeSourceUiData)
    pass

class LevelScriptOnReset(ILevelScriptEvent):
    pass

class TftUnitPropertyValue():
    pass

class InsertIntoCustomTableBlock(IScriptBlock):
    Value: (Pointer, 0x0, 0x0, IScriptValueGet)
    OutIndex: (Embed, 0x0, 0x0, IntTableSet)
    Index: (Pointer, 0x0, 0x0, IIntGet)
    DestIndex: (Pointer, 0x0, 0x0, IIntGet)
    DestTable: (Embed, 0x0, 0x0, CustomTableGet)
    CustomTable: (Embed, 0x0, 0x0, CustomTableGet)
    pass

class DragonUiTunables():
    mDragonBaseNames: (List, 0x0, String, 0x0)
    mSlots: (U8, 0x0, 0x0, 0x0)
    pass

class ContextualConditionItemPriceMinimum(IContextualCondition):
    mItemPriceMinimum: (U32, 0x0, 0x0, 0x0)
    pass

class PlayerFrameViewController(ViewController):
    ResourceBars: (Embed, 0x0, 0x0, HudPlayerResourceBars)
    Scene: (Hash, 0x0, 0x0, 0x0)
    StatusMessage: (Hash, 0x0, 0x0, 0x0)
    PlayerBuffsScene: (Hash, 0x0, 0x0, 0x0)
    DrawAreaList: (Embed, 0x0, 0x0, DrawAreaList)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    CenterTooltipRegion: (Hash, 0x0, 0x0, 0x0)
    MessageDisplayTime: (F32, 0x0, 0x0, 0x0)
    LevelUpDisplay: (Embed, 0x0, 0x0, UiLevelUp)
    NegativeBuffs: (Embed, 0x0, 0x0, BuffDisplayList)
    0x53e4225c: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    Loadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    LevelUpLinks: (List, 0x0, Hash, 0x0)
    PortraitUiData: (Embed, 0x0, 0x0, PlayerPortraitUiData)
    StatPages: (List, 0x0, Embed, StatPageEntry)
    RootScene: (Hash, 0x0, 0x0, 0x0)
    0xae44d689: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    AbilitiesUiData: (Embed, 0x0, 0x0, AbilitiesUiData)
    SummonerSpellSpecialist: (Embed, 0x0, 0x0, UiPerkSummonerSpecialistToggles)
    PositiveBuffs: (Embed, 0x0, 0x0, BuffDisplayList)
    LevelUpUiData: (Embed, 0x0, 0x0, LevelUpUiData)
    SpellCastMessage: (Hash, 0x0, 0x0, 0x0)
    HudCenterFrameGlowData: (Embed, 0x0, 0x0, HudCenterFrameGlowData)
    pass

class StatBySubPartCalculationPart(IGameCalculationPartWithStats, ISpellCalculationPartWithStats, ISpellCalculationPart):
    mSubpart: (Pointer, 0x0, 0x0, IGameCalculationPart)
    mSubpart: (Pointer, 0x0, 0x0, ISpellCalculationPart)
    mStat: (U8, 0x0, 0x0, 0x0)
    mStatFormula: (U8, 0x0, 0x0, 0x0)
    pass

class 0xcd164709(BaseLoadoutData):
    Augments: (List2, 0x0, Hash, 0x0)
    Enabled: (Bool, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class MapSkin():
    mMapSkinServerConstants: (Link, 0x0, 0x0, GameModeConstants)
    MapNavigationMesh: (Link, 0x0, 0x0, MapNavigationMesh)
    mMapObjectsMob: (String, 0x0, 0x0, 0x0)
    mLevelScripts: (List, 0x0, String, 0x0)
    mMinimapBackgroundConfig: (Embed, 0x0, 0x0, MinimapBackgroundConfig)
    mResourceResolver: (Link, 0x0, 0x0, ResourceResolver)
    mNavigationMesh: (String, 0x0, 0x0, 0x0)
    MaterialSwap: (Pointer, 0x0, 0x0, MapMaterialSwap)
    WorldParticles: (Link, 0x0, 0x0, MapWorldParticles)
    GammaParameters: (Pointer, 0x0, 0x0, GammaParameters)
    Name: (String, 0x0, 0x0, 0x0)
    mResourceResolvers: (List, 0x0, Link, ResourceResolver)
    mObjectSkinFallbacks: (Map, Hash, I32, 0x0)
    mMapContainerLink: (String, 0x0, 0x0, 0x0)
    mWorldParticlesIni: (String, 0x0, 0x0, 0x0)
    mWorldGeoLink: (String, 0x0, 0x0, 0x0)
    mWorldGeometry: (String, 0x0, 0x0, 0x0)
    mSkyboxCubemapTexture: (String, 0x0, 0x0, 0x0)
    mColorizationPostEffect: (Pointer, 0x0, 0x0, MapSkinColorizationPostEffect)
    mGrassTintTexture: (String, 0x0, 0x0, 0x0)
    mAlternateAssets: (Embed, 0x0, 0x0, MapAlternateAssets)
    mMapObjectsCfg: (String, 0x0, 0x0, 0x0)
    mWorldParticlesDat: (String, 0x0, 0x0, 0x0)
    pass

class ChangeMissileSpeedOnDelay(MissileBehaviorSpec):
    mDelay: (F32, 0x0, 0x0, 0x0)
    mSpeedValue: (F32, 0x0, 0x0, 0x0)
    mSpeedChangeType: (U32, 0x0, 0x0, 0x0)
    pass

class DamageSourceSettings():
    TemplateDefinition: (List, 0x0, Embed, DamageSourceTemplate)
    DamageTagDefinition: (List, 0x0, String, 0x0)
    pass

class OptionItemFilter_GameStyle(IOptionItemFilter):
    ShowInTftReplay: (Bool, 0x0, 0x0, 0x0)
    ShowInLolGame: (Bool, 0x0, 0x0, 0x0)
    ShowInTftGame: (Bool, 0x0, 0x0, 0x0)
    ShowInLolReplay: (Bool, 0x0, 0x0, 0x0)
    ShowInTftPregame: (Bool, 0x0, 0x0, 0x0)
    pass

class UiDraggableElementGroupDrag(UiDraggableBasic):
    pass

class LevelScriptController(ILevelController):
    Properties: (Map, Hash, Pointer, GameModeConstant)
    Script: (Link, 0x0, 0x0, LevelControlScript)
    Enabled: (Bool, 0x0, 0x0, 0x0)
    pass

class FxActionSfxMissile(FxActionSfxBase):
    Target: (Pointer, 0x0, 0x0, IFxLocation)
    SplineInfo: (Pointer, 0x0, 0x0, ISplineInfo)
    Location: (Pointer, 0x0, 0x0, IFxLocation)
    pass

class TftCutsceneSetPositionAction(TftCutsceneAction):
    GameObjectBlackboardName: (String, 0x0, 0x0, 0x0)
    PositionBlackboardName: (String, 0x0, 0x0, 0x0)
    pass

class UiStoreItemTileData():
    BalanceHeader: (Hash, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    Vfx: (Hash, 0x0, 0x0, 0x0)
    PriceText: (Hash, 0x0, 0x0, 0x0)
    BalanceValue: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class TftTeamPlannerMemberTraitData():
    Background: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class ChampionAugmentTagList(IGameModeConfig):
    ChampionTags: (List, 0x0, Embed, ChampionAugmentTags)
    pass

class ScriptPreloadParticle():
    PreloadResourceName: (String, 0x0, 0x0, 0x0)
    pass

class ISpellCalculationPartWithStats(ISpellCalculationPart):
    mStat: (U8, 0x0, 0x0, 0x0)
    mStatFormula: (U8, 0x0, 0x0, 0x0)
    pass

class ContextualConditionLastBoughtItem(IContextualCondition):
    mItem: (Hash, 0x0, 0x0, 0x0)
    mItemId: (I32, 0x0, 0x0, 0x0)
    pass

class DrawablePositionLocator():
    OrientationType: (U32, 0x0, 0x0, 0x0)
    BasePosition: (U32, 0x0, 0x0, 0x0)
    AngleOffsetRadian: (F32, 0x0, 0x0, 0x0)
    DistanceOffset: (F32, 0x0, 0x0, 0x0)
    pass

class MapAreaEventConstraintInfo(ListenerConstraintInfo):
    ExclusionChecks: (Embed, 0x0, 0x0, ChallengeMapAreaGroupCheck)
    SpecificEventType: (U32, 0x0, 0x0, 0x0)
    InclusionChecks: (Embed, 0x0, 0x0, ChallengeMapAreaGroupCheck)
    pass

class CursorDataCaptureCooldownContext():
    mData: (List, 0x7, Embed, CursorData)
    pass

class ElementGroupButtonState():
    DisplayElements: (List, 0x0, Link, ElementDataI)
    TextElement: (Link, 0x0, 0x0, TextElementData)
    pass

class ConformToPathRigPoseModifierData(BaseRigPoseModifierData):
    mFrequency: (F32, 0x0, 0x0, 0x0)
    mVelMultiplier: (F32, 0x0, 0x0, 0x0)
    mEndingJoint: (I32, 0x0, 0x0, 0x0)
    mDefaultMaskName: (Hash, 0x0, 0x0, 0x0)
    mStartingJoint: (I32, 0x0, 0x0, 0x0)
    BlendDistance: (F32, 0x0, 0x0, 0x0)
    TurnOnDistance: (F32, 0x0, 0x0, 0x0)
    mMaxBoneAngle: (F32, 0x0, 0x0, 0x0)
    mEndingJointName: (Hash, 0x0, 0x0, 0x0)
    TurnOnAngle: (F32, 0x0, 0x0, 0x0)
    OnlyActivateInTurns: (Bool, 0x0, 0x0, 0x0)
    DebugVisualization: (Bool, 0x0, 0x0, 0x0)
    ActivationAngle: (F32, 0x0, 0x0, 0x0)
    mStartingJointName: (Hash, 0x0, 0x0, 0x0)
    0xee8cc7a: (Bool, 0x0, 0x0, 0x0)
    ActivationDistance: (F32, 0x0, 0x0, 0x0)
    ExtraJointChains: (List, 0x0, Embed, ExtraJointChainData)
    mDampingValue: (F32, 0x0, 0x0, 0x0)
    pass

class UiTeamFightTeamData():
    TeamMember: (Embed, 0x0, 0x0, UiTeamFightTeamMemberData)
    TeamScore: (Pointer, 0x0, 0x0, UiTeamFightTeamScoreData)
    TeamMemberSlots: (List, 0x5, Hash, 0x0)
    TeamHealthMeter: (Pointer, 0x0, 0x0, UiTeamFightTeamHealthMeterData)
    pass

class RsCase():
    Sequence: (Embed, 0x0, 0x0, Sequence)
    Condition: (Pointer, 0x0, 0x0, IRsCondition)
    pass

class AbilityResourceSlotInfo():
    arBaseFactorRegen: (F32, 0x0, 0x0, 0x0)
    arType: (U8, 0x0, 0x0, 0x0)
    arOverrideSpacerName: (String, 0x0, 0x0, 0x0)
    arBase: (F32, 0x0, 0x0, 0x0)
    arPreventRegenWhileAtZero: (Bool, 0x0, 0x0, 0x0)
    arBaseStaticRegen: (F32, 0x0, 0x0, 0x0)
    HideEmptyPips: (Bool, 0x0, 0x0, 0x0)
    arIsShownOnlyOnLocalPlayer: (Bool, 0x0, 0x0, 0x0)
    arOverrideLargePipName: (String, 0x0, 0x0, 0x0)
    arOverrideEmptyPipName: (String, 0x0, 0x0, 0x0)
    arMaxSegments: (I32, 0x0, 0x0, 0x0)
    arContributesToHealthValues: (Bool, 0x0, 0x0, 0x0)
    arHasRegenText: (Bool, 0x0, 0x0, 0x0)
    arOverrideSmallPipName: (String, 0x0, 0x0, 0x0)
    arIncrements: (F32, 0x0, 0x0, 0x0)
    StartAtZeroOnSpawn: (Bool, 0x0, 0x0, 0x0)
    arDisplayAsPips: (Bool, 0x0, 0x0, 0x0)
    arNegativeSpacer: (Bool, 0x0, 0x0, 0x0)
    arRegenPerLevel: (F32, 0x0, 0x0, 0x0)
    arPerLevel: (F32, 0x0, 0x0, 0x0)
    arOverrideMediumPipName: (String, 0x0, 0x0, 0x0)
    arAllowMaxValueToBeOverridden: (Bool, 0x0, 0x0, 0x0)
    arIsShown: (Bool, 0x0, 0x0, 0x0)
    pass

class SkinnedMeshDataMaterialController():
    pass

class SwitchCase(0x38a7f9b3):
    Sequence: (Embed, 0x0, 0x0, Sequence)
    Sequence: (Embed, 0x0, 0x0, ScriptSequence)
    IsDisabled: (Bool, 0x0, 0x0, 0x0)
    Condition: (Pointer, 0x0, 0x0, IRsCondition)
    Condition: (Pointer, 0x0, 0x0, IScriptCondition)
    pass

class TftUnitPropertyValueInteger(TftUnitPropertyValue):
    Value: (I32, 0x0, 0x0, 0x0)
    pass

class LuaObjectOverrides():
    Tables: (Map, String, Link, LuaTableData)
    pass

class 0xce8f4190():
    Settings: (Embed, 0x0, 0x0, 0x502b0c72)
    pass

class DoDamage(IBlock):
    mAmount: (F32, 0x0, 0x0, 0x0)
    mAmountVar: (String, 0x0, 0x0, 0x0)
    mTargetHeroName: (String, 0x0, 0x0, 0x0)
    pass

class MapActionCyclePropAnimation(MapAction):
    PropName: (String, 0x0, 0x0, 0x0)
    Shuffle: (Bool, 0x0, 0x0, 0x0)
    AnimationList: (List, 0x0, Embed, MapActionAnimationData)
    pass

class OptionTemplateSecondaryHotkeys_Label():
    BackgroundElement: (Hash, 0x0, 0x0, 0x0)
    TextElement: (Hash, 0x0, 0x0, 0x0)
    pass

class RegaliaBorder(RegaliaData):
    pass

class StealthVfx():
    UseOwnerFacing: (Bool, 0x0, 0x0, 0x0)
    FowVisibilityRadius: (F32, 0x0, 0x0, 0x0)
    BoneName: (String, 0x0, 0x0, 0x0)
    EffectName: (String, 0x0, 0x0, 0x0)
    SpecificTeamOnly: (U8, 0x0, 0x0, 0x0)
    TimeoutInFow: (F32, 0x0, 0x0, 0x0)
    UseTargetObject: (Bool, 0x0, 0x0, 0x0)
    EffectNameForOtherTeam: (String, 0x0, 0x0, 0x0)
    Scale: (F32, 0x0, 0x0, 0x0)
    AttachToCamera: (Bool, 0x0, 0x0, 0x0)
    UseKeywordObject: (Bool, 0x0, 0x0, 0x0)
    UseAttachmentForMeshOnly: (Bool, 0x0, 0x0, 0x0)
    PersistentThroughReconnect: (Bool, 0x0, 0x0, 0x0)
    SendIfOnScreenOrDiscard: (Bool, 0x0, 0x0, 0x0)
    OnlySendToOwner: (Bool, 0x0, 0x0, 0x0)
    HidefromSpectator: (Bool, 0x0, 0x0, 0x0)
    FowTeam: (U8, 0x0, 0x0, 0x0)
    pass

class MapActionToggleMapParticle(MapAction):
    MapParticleName: (List, 0x0, String, 0x0)
    MapParticleName: (String, 0x0, 0x0, 0x0)
    Shown: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xcee2aac6(IBehaviorScriptBlock):
    pass

class BoolDefaultTableGet(IBoolGet):
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Table: (Pointer, 0x0, 0x0, RsTable)
    Var: (String, 0x0, 0x0, 0x0)
    Default: (Bool, 0x0, 0x0, 0x0)
    pass

class TftCutsceneMissileClip(TftCutsceneClip):
    0x15909afd: (F32, 0x0, 0x0, 0x0)
    SourceObject: (String, 0x0, 0x0, 0x0)
    Source: (Pointer, 0x0, 0x0, TftCutscenePositionProvider)
    0x1f0b4b9f: (String, 0x0, 0x0, 0x0)
    Target: (Pointer, 0x0, 0x0, TftCutscenePositionProvider)
    HitEffectKey: (String, 0x0, 0x0, 0x0)
    0x491746de: (String, 0x0, 0x0, 0x0)
    MissileRadius: (F32, 0x0, 0x0, 0x0)
    0x5e6afcf4: (String, 0x0, 0x0, 0x0)
    HeightSolver: (Pointer, 0x0, 0x0, TftHeightSolverType)
    0x789f4661: (Bool, 0x0, 0x0, 0x0)
    0x7d4eb6e7: (String, 0x0, 0x0, 0x0)
    DamagePercent: (F32, 0x0, 0x0, 0x0)
    EffectKey: (String, 0x0, 0x0, 0x0)
    0xa0d7eb85: (String, 0x0, 0x0, 0x0)
    0xa32d933a: (Bool, 0x0, 0x0, 0x0)
    0xc547d3c0: (Bool, 0x0, 0x0, 0x0)
    TargetObject: (String, 0x0, 0x0, 0x0)
    pass

class ObjectiveIconDefinition():
    ObjectiveNameTraKey: (String, 0x0, 0x0, 0x0)
    TimerIcon: (Hash, 0x0, 0x0, 0x0)
    PortraitIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualActionData(IResource):
    mObjectPath: (String, 0x0, 0x0, 0x0)
    mCooldown: (F32, 0x0, 0x0, 0x0)
    mSituations: (Map, Hash, Embed, ContextualSituation)
    mHealthPercentThreshold: (F32, 0x0, 0x0, 0x0)
    pass

class 0xcf4a55da(MapComponent):
    Overlays: (Link, 0x0, 0x0, MapNavGridOverlays)
    pass

class LookAtSpellTargetDistanceParametricUpdater(IFloatParametricUpdater):
    pass

class MapLightUpdaterType():
    Updaters: (List2, 0x0, Pointer, IMapLightUpdater)
    pass

class SourceHasBuffFilter(IStatStoneLogicDriver):
    Invisibility: (Bool, 0x0, 0x0, 0x0)
    pass

class ItemScript(GameScript, Rscript):
    Functions: (Map, Hash, Embed, ScriptFunction)
    Sequences: (Map, Hash, Embed, ScriptSequence)
    pass

class FxActionSfxMissileInstance(IFxActionInstance):
    pass

class BuffDisplayData():
    StacksText: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    IconBorderPositive: (Hash, 0x0, 0x0, 0x0)
    IconBorderNegative: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    CooldownFx: (Hash, 0x0, 0x0, 0x0)
    HitRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class MapFrustum(MapPlaceable):
    OrthoHeight: (F32, 0x0, 0x0, 0x0)
    Near: (F32, 0x0, 0x0, 0x0)
    Aspect: (F32, 0x0, 0x0, 0x0)
    Fov: (F32, 0x0, 0x0, 0x0)
    Far: (F32, 0x0, 0x0, 0x0)
    Orthographic: (Bool, 0x0, 0x0, 0x0)
    pass

class GetMapPropBoolDynamicMaterialBoolDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    mKeyName: (String, 0x0, 0x0, 0x0)
    pass

class ToolAiPresence():
    Intro: (Bool, 0x0, 0x0, 0x0)
    Medium: (Bool, 0x0, 0x0, 0x0)
    Easy: (Bool, 0x0, 0x0, 0x0)
    Hard: (Bool, 0x0, 0x0, 0x0)
    pass

class BarTypeMap():
    AdditionalBarTypes: (Map, Hash, Hash, 0x0)
    DrainDirection: (U32, 0x0, 0x0, 0x0)
    DefaultBar: (Hash, 0x0, 0x0, 0x0)
    MinDisplayPercentOverride: (F32, 0x0, 0x0, 0x0)
    pass

class FloatGraphMaterialDriver(IDynamicMaterialDriver, ILogicDriver, ILogicFloatDriver):
    Graph: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    Driver: (Pointer, 0x0, 0x0, IDynamicMaterialFloatDriver)
    Driver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class CensoredImage():
    UncensoredImages: (Map, Hash, String, 0x0)
    Image: (String, 0x0, 0x0, 0x0)
    pass

class MapUniquePointLight(MapStaticPointLightBase):
    Impact: (I32, 0x0, 0x0, 0x0)
    Impact: (U8, 0x0, 0x0, 0x0)
    IntensityScale: (F32, 0x0, 0x0, 0x0)
    LightColor: (Vec4, 0x0, 0x0, 0x0)
    CastStaticShadows: (Bool, 0x0, 0x0, 0x0)
    Radius: (F32, 0x0, 0x0, 0x0)
    pass

class MinimapViewController(ViewController):
    VoiceChatButtonGlowFxTimeoutSecs: (F32, 0x0, 0x0, 0x0)
    PingButton: (Hash, 0x0, 0x0, 0x0)
    MinimapContent: (Hash, 0x0, 0x0, 0x0)
    0x2df6e474: (Bool, 0x0, 0x0, 0x0)
    MinimapTooltipAnchor: (Hash, 0x0, 0x0, 0x0)
    DrawAreaList: (Embed, 0x0, 0x0, DrawAreaList)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    FirstTimeUxOffscreenButtonGroup: (Hash, 0x0, 0x0, 0x0)
    MinimumScale: (F32, 0x0, 0x0, 0x0)
    JunglePath: (Pointer, 0x0, 0x0, JunglePath)
    OptionsMenuButton: (Hash, 0x0, 0x0, 0x0)
    FirstTimeUxOffScreenPoiTimeout: (F32, 0x0, 0x0, 0x0)
    FirstTimeUxCloseButtonGroup: (Hash, 0x0, 0x0, 0x0)
    0x947c803c: (Pointer, 0x0, 0x0, 0x947c803c)
    VoiceChatButton: (Hash, 0x0, 0x0, 0x0)
    FtuxScene: (Hash, 0x0, 0x0, 0x0)
    JunglePathButton: (Hash, 0x0, 0x0, 0x0)
    ObjectiveBountiesStatus: (Pointer, 0x0, 0x0, ObjectiveBountiesStatus)
    CameraLockButton: (Hash, 0x0, 0x0, 0x0)
    VoiceChatButtonGlowFx: (Hash, 0x0, 0x0, 0x0)
    0xc0492f95: (Hash, 0x0, 0x0, 0x0)
    MinimapVoiceChatAnchor: (Hash, 0x0, 0x0, 0x0)
    ObjectName: (String, 0x0, 0x0, 0x0)
    MaximumScale: (F32, 0x0, 0x0, 0x0)
    FlippedOverride: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    pass

class 0xd082b191(IFxAction):
    ZoomOutTime: (F32, 0x0, 0x0, 0x0)
    ArmLength: (F32, 0x0, 0x0, 0x0)
    ZoomOutEase: (U32, 0x0, 0x0, 0x0)
    ZoomOutEase: (U8, 0x0, 0x0, 0x0)
    Yaw: (F32, 0x0, 0x0, 0x0)
    ZoomInEase: (U32, 0x0, 0x0, 0x0)
    ZoomInEase: (U8, 0x0, 0x0, 0x0)
    Position: (Embed, 0x0, 0x0, FxTransform)
    ZoomInTime: (F32, 0x0, 0x0, 0x0)
    Fov: (F32, 0x0, 0x0, 0x0)
    Pitch: (F32, 0x0, 0x0, 0x0)
    pass

class TftCutsceneArenaLocatorInitializer(TftCutsceneInitializer):
    LocatorBlackboardName: (String, 0x0, 0x0, 0x0)
    ArenaLocatorBlackboardName: (String, 0x0, 0x0, 0x0)
    ArenaPositionLocatorName: (String, 0x0, 0x0, 0x0)
    IsLocatorArenaSpecific: (Bool, 0x0, 0x0, 0x0)
    CutscenePositionLocatorName: (String, 0x0, 0x0, 0x0)
    pass

class DeathRecapDamageOverview():
    RadialTotalDamageValueText: (Hash, 0x0, 0x0, 0x0)
    FightLengthValueText: (Hash, 0x0, 0x0, 0x0)
    LossOfControlValueText: (Hash, 0x0, 0x0, 0x0)
    DamageByTypeValueText: (Hash, 0x0, 0x0, 0x0)
    LegendMagicDamageValueText: (Hash, 0x0, 0x0, 0x0)
    LegendMagicDamageIcon: (Hash, 0x0, 0x0, 0x0)
    TotalDamageRadialChart: (Embed, 0x0, 0x0, DamageTypeRadialChart)
    LegendTrueDamageValueText: (Hash, 0x0, 0x0, 0x0)
    LegendTrueDamageIcon: (Hash, 0x0, 0x0, 0x0)
    LegendPhysicalDamageIcon: (Hash, 0x0, 0x0, 0x0)
    LegendPhysicalDamageValueText: (Hash, 0x0, 0x0, 0x0)
    pass

class EffectElement():
    mKeyFrames: (List, 0x0, Embed, EffectKeyFrame)
    mTextureName: (String, 0x0, 0x0, 0x0)
    pass

class EsportsBannerConfiguration():
    LeagueName: (String, 0x0, 0x0, 0x0)
    LeagueFlavors: (List, 0x0, Embed, LeagueFlavor)
    IndividualBannerOverrides: (List, 0x0, Embed, SponsoredBanner)
    Name: (String, 0x0, 0x0, 0x0)
    Priority: (U32, 0x0, 0x0, 0x0)
    AssociatedTeams: (List, 0x0, String, 0x0)
    Configuration: (List, 0x0, Embed, SponsoredBanner)
    EsportsTeam: (Hash, 0x0, 0x0, 0x0)
    IsAnEvent: (Bool, 0x0, 0x0, 0x0)
    TexturePath: (File, 0x0, 0x0, 0x0)
    TexturePath: (String, 0x0, 0x0, 0x0)
    EventMutator: (Link, 0x0, 0x0, GameMutatorExpansions)
    AssociatedVersions: (List, 0x0, String, 0x0)
    pass

class TftUnitInfoCustomButtonPlainTextTooltipData():
    MainTextTra: (String, 0x0, 0x0, 0x0)
    TitleTra: (String, 0x0, 0x0, 0x0)
    pass

class MapSpotlight(MapSpotlightBase):
    CastStaticShadows: (Bool, 0x0, 0x0, 0x0)
    pass

class RsNotCondition(IRsCondition):
    Condition: (Pointer, 0x0, 0x0, IRsCondition)
    pass

class SlopeAngleParametricUpdater(IFloatParametricUpdater):
    pass

class UiTextureProviderMeshData(IUiTextureDataProvider):
    SkinMeshProperties: (Embed, 0x0, 0x0, SkinMeshDataProperties)
    ModelTransformation: (Mtx44, 0x0, 0x0, 0x0)
    AnimationGraphData: (Link, 0x0, 0x0, AnimationGraphData)
    pass

class IStringHashGet():
    pass

class 0xd149dd3f():
    ToSlotId: (I32, 0x0, 0x0, 0x0)
    FromSlotId: (I32, 0x0, 0x0, 0x0)
    pass

class SelectorMovementEntry():
    Weight: (F32, 0x0, 0x0, 0x0)
    MovementSpec: (Pointer, 0x0, 0x0, MissileMovementSpec)
    pass

class TftItemData():
    mName: (String, 0x0, 0x0, 0x0)
    mBuffName: (String, 0x0, 0x0, 0x0)
    mEffectAmount: (Map, Hash, F32, 0x0)
    mVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    0x41b0f90b: (Link, 0x0, 0x0, StaticMaterialDef)
    Value: (Map, U8, I32, 0x0)
    mColor: (Option, 0x0, Color, 0x0)
    IncompatibleTraits: (List, 0x0, Link, TftTraitData)
    ShopData: (Link, 0x0, 0x0, TftShopData)
    mCodexDisplayIndex: (I32, 0x0, 0x0, 0x0)
    mDescriptionNameTra: (String, 0x0, 0x0, 0x0)
    BonusTrait: (Link, 0x0, 0x0, TftTraitData)
    mComposition: (List, 0x0, Link, TftItemData)
    mIconPath: (String, 0x0, 0x0, 0x0)
    AssociatedTraits: (List, 0x0, Link, TftTraitData)
    mRandomAnimationStrengthRange: (Vec2, 0x0, 0x0, 0x0)
    mIsUnique: (Bool, 0x0, 0x0, 0x0)
    DialogPickChoice: (Pointer, 0x0, 0x0, DialogPickChoice)
    VfxResourceResolver: (Link, 0x0, 0x0, ResourceResolver)
    mAlternativeCompositions: (List, 0x0, Embed, TftItemComposition)
    ItemTags: (List, 0x0, Hash, 0x0)
    IsAugment: (Bool, 0x0, 0x0, 0x0)
    EffectAmounts: (List, 0x0, Embed, TftEffectAmount)
    0xc24a5adb: (Bool, 0x0, 0x0, 0x0)
    mDisplayNameTra: (String, 0x0, 0x0, 0x0)
    mId: (I32, 0x0, 0x0, 0x0)
    mId: (U32, 0x0, 0x0, 0x0)
    IconMaterial: (Link, 0x0, 0x0, StaticMaterialDef)
    mArmoryIconOverridePath: (String, 0x0, 0x0, 0x0)
    ItemBuffTarget: (U8, 0x0, 0x0, 0x0)
    MutuallyExclusiveItems: (List, 0x0, Link, TftItemData)
    AssociatedCharacterName: (String, 0x0, 0x0, 0x0)
    Keywords: (List2, 0x0, Hash, 0x0)
    pass

class IntegratedValueFloat(ValueFloat):
    pass

class SceneBaseTransitionData():
    TransitionTime: (F32, 0x0, 0x0, 0x0)
    EndAlpha: (U8, 0x0, 0x0, 0x0)
    EasingType: (U32, 0x0, 0x0, 0x0)
    EasingType: (U8, 0x0, 0x0, 0x0)
    StartAlpha: (U8, 0x0, 0x0, 0x0)
    TransitionStartDelaySecs: (F32, 0x0, 0x0, 0x0)
    pass

class 0xd19d72ee():
    DescriptionText: (Hash, 0x0, 0x0, 0x0)
    ProgressText: (Hash, 0x0, 0x0, 0x0)
    RewardText: (Hash, 0x0, 0x0, 0x0)
    RewardIcon: (Hash, 0x0, 0x0, 0x0)
    ProgressCompleteIcon: (Hash, 0x0, 0x0, 0x0)
    0xedc62dad: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xd1ae9686():
    pass

class 0xd1b1f16():
    Color: (Pointer, 0x0, 0x0, ILogicDriver)
    ColorValues: (List2, 0x0, Color, 0x0)
    StartingValue: (F32, 0x0, 0x0, 0x0)
    SpellLevel: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class MaterialDef(IMaterialDef):
    DefaultTechnique: (String, 0x0, 0x0, 0x0)
    Type: (U32, 0x0, 0x0, 0x0)
    Techniques: (List, 0x0, Embed, TechniqueDef)
    Name: (String, 0x0, 0x0, 0x0)
    SamplerValues: (List, 0x0, Embed, ShaderSamplerDef)
    ParamValues: (List, 0x0, Embed, ShaderParamDef)
    ShaderMacros: (Map, String, String, 0x0)
    pass

class TftAnnouncementData():
    mDelay: (F32, 0x0, 0x0, 0x0)
    mDuration: (F32, 0x0, 0x0, 0x0)
    AnimatedIcon: (Hash, 0x0, 0x0, 0x0)
    mIconPath: (String, 0x0, 0x0, 0x0)
    mTitleTra: (String, 0x0, 0x0, 0x0)
    pass

class UiElementEffectCustomMaterialData(UiElementEffectData):
    mMaterial: (Link, 0x0, 0x0, StaticMaterialDef)
    pass

class Barracks(BuildingClient):
    pass

class AiUnitConfigLink():
    Group: (Link, 0x0, 0x0, AiUnitGroup)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class TftGameStartLabFields():
    GameStartTraKey: (String, 0x0, 0x0, 0x0)
    GameStartReplacementTexture: (String, 0x0, 0x0, 0x0)
    pass

class HudItemShopExpandingPanelDefinition():
    ExpandedRegion: (Hash, 0x0, 0x0, 0x0)
    Slots: (List, 0x0, Hash, 0x0)
    QuickBuyData: (Embed, 0x0, 0x0, HudItemShopQuickBuyData)
    HoverVfx: (Hash, 0x0, 0x0, 0x0)
    PinButton: (Hash, 0x0, 0x0, 0x0)
    SceneData: (Hash, 0x0, 0x0, 0x0)
    TutorialVfx: (Hash, 0x0, 0x0, 0x0)
    Opened: (Hash, 0x0, 0x0, 0x0)
    Closed: (Hash, 0x0, 0x0, 0x0)
    pass

class LooseUiTextureData3SliceV(LooseUiTextureDataBase, LooseUiTextureData):
    TopBottomHeights: (Vec2, 0x0, 0x0, 0x0)
    EdgeSizes: (Vec2, 0x0, 0x0, 0x0)
    EdgeSizesTopBottom: (Vec2, 0x0, 0x0, 0x0)
    pass

class AbilityResourcePipSpacerTypeMap():
    AdditionalPipSpacerTypes: (Map, Hash, Hash, 0x0)
    DefaultPipSpacer: (Hash, 0x0, 0x0, 0x0)
    pass

class EffectFillPercentageElementData(EffectElementData):
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    pass

class DisplayStatUiData():
    StatNameTra: (String, 0x0, 0x0, 0x0)
    IsDetailedStat: (Bool, 0x0, 0x0, 0x0)
    StatType: (U8, 0x0, 0x0, 0x0)
    NewStatType: (U8, 0x0, 0x0, 0x0)
    TexturePath: (String, 0x0, 0x0, 0x0)
    pass

class HudReplaySliderData():
    mIconDataPriorityList: (List, 0x0, Embed, HudReplaySliderIconData)
    mIconDataMap: (Map, Hash, Embed, HudReplaySliderIconData)
    mTooltipEventWindow: (F32, 0x0, 0x0, 0x0)
    pass

class LevelPropAiCommon(AiBaseClient):
    pass

class EquippedGearParametricUpdater(IFloatParametricUpdater):
    pass

class Defaultvisibility(MissileVisibilitySpec):
    pass

class ClipAccessoryData():
    Name: (Hash, 0x0, 0x0, 0x0)
    pass

class HudItemShopItemDetailsDefinition():
    GoldIconDefinition: (Hash, 0x0, 0x0, 0x0)
    ItemIconDefinition: (Hash, 0x0, 0x0, 0x0)
    ClickData: (Hash, 0x0, 0x0, 0x0)
    TitleTextDefinition: (Hash, 0x0, 0x0, 0x0)
    BodyDefinition: (Hash, 0x0, 0x0, 0x0)
    CostTextDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class TftCutsceneColorFxClip(TftCutsceneBasePostFxClip):
    Color: (Color, 0x0, 0x0, 0x0)
    pass

class ChampionBaseItemAdvice():
    mBaseItemAdvices: (List, 0x0, Embed, BaseItemAdvice)
    pass

class HasBuffOfTypeBoolDriver(ILogicBoolDriver):
    BuffType: (U8, 0x0, 0x0, 0x0)
    pass

class AbilityResourceDynamicMaterialFloatDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    Slot: (U8, 0x0, 0x0, 0x0)
    pass

class MultipleEventsWithinTimeConstraintInfo(ListenerConstraintInfo):
    NumberToPassChallenge: (U32, 0x0, 0x0, 0x0)
    DurationTotrack: (F32, 0x0, 0x0, 0x0)
    pass

class HudElementalSectionUiData():
    StormColoration: (Color, 0x0, 0x0, 0x0)
    FireColoration: (Color, 0x0, 0x0, 0x0)
    FirstSelectionAnimationDelay: (F32, 0x0, 0x0, 0x0)
    FairyColoration: (Color, 0x0, 0x0, 0x0)
    DarkColoration: (Color, 0x0, 0x0, 0x0)
    GlowingRingCycleTime: (F32, 0x0, 0x0, 0x0)
    IceColoration: (Color, 0x0, 0x0, 0x0)
    MeterFilledButtonFadeInDelay: (F32, 0x0, 0x0, 0x0)
    MagmaColoration: (Color, 0x0, 0x0, 0x0)
    EarthColoration: (Color, 0x0, 0x0, 0x0)
    LightColoration: (Color, 0x0, 0x0, 0x0)
    WaterColoration: (Color, 0x0, 0x0, 0x0)
    AirColoration: (Color, 0x0, 0x0, 0x0)
    SecondSelectionAnimationDelay: (F32, 0x0, 0x0, 0x0)
    pass

class LobbyLeaderControls():
    PlayerIcon: (Hash, 0x0, 0x0, 0x0)
    KickButton: (Hash, 0x0, 0x0, 0x0)
    SceneHandle: (Hash, 0x0, 0x0, 0x0)
    PromoteButton: (Hash, 0x0, 0x0, 0x0)
    PlayerName: (Hash, 0x0, 0x0, 0x0)
    pass

class ScriptBtInverter(IScriptBt, IScriptSequence):
    Blocks: (List2, 0x0, Pointer, IScriptBlock)
    Blocks: (List2, 0x0, Pointer, IBehaviorScriptBlock)
    pass

class MapTerrainPaint(MapGraphicsFeature, MapComponent):
    TerrainPaintTexturePath: (String, 0x0, 0x0, 0x0)
    pass

class HudGameModeScoreData():
    mEncounterUi: (Pointer, 0x0, 0x0, EncounterUiTunables)
    mGroupName: (String, 0x0, 0x0, 0x0)
    mTeamScoreMeterTypes: (List, 0x2, U8, 0x0)
    mTeamFightUi: (Pointer, 0x0, 0x0, TeamFightUiTunables)
    mTeamFightUi: (Pointer, 0x0, 0x0, HudTeamFightData)
    mIndividualScoreElementTypes: (List, 0x0, U8, 0x0)
    mOptionalBins: (List, 0x0, Embed, HudOptionalBinData)
    mTeamScoreTextType: (U8, 0x0, 0x0, 0x0)
    ScoreboardTeamScoreTypes: (U32, 0x0, 0x0, 0x0)
    mTeamScoreMeterMaxRoundsPerTeam: (U32, 0x0, 0x0, 0x0)
    mTeamScoreElementTypes: (List, 0x0, U8, 0x0)
    mCountdownTimer: (Bool, 0x0, 0x0, 0x0)
    mTeamScoreMeterUi: (Pointer, 0x0, 0x0, TeamScoreMeterUiTunables)
    mTeamScoreMeterType: (U8, 0x0, 0x0, 0x0)
    mDragonUi: (Pointer, 0x0, 0x0, DragonUiTunables)
    mQuestUi: (Pointer, 0x0, 0x0, QuestUiTunables)
    mTeamGameScorePingMessage: (String, 0x0, 0x0, 0x0)
    0xc72e2257: (U32, 0x0, 0x0, 0x0)
    mUseEncounterUi: (Bool, 0x0, 0x0, 0x0)
    EnableObjectiveBounties: (Bool, 0x0, 0x0, 0x0)
    mEventCount: (U8, 0x0, 0x0, 0x0)
    mModeKeyName: (String, 0x0, 0x0, 0x0)
    mAllowDynamicVisibility: (Bool, 0x0, 0x0, 0x0)
    pass

class StatStoneMilestoneCalloutViewController(ViewController):
    MilestoneContentScene: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    MilestonePersonalBestScene: (Hash, 0x0, 0x0, 0x0)
    MilestonePersonalBestEffect: (Hash, 0x0, 0x0, 0x0)
    MilestoneSelfIntroTime: (F32, 0x0, 0x0, 0x0)
    MilestoneStoneIcon: (Hash, 0x0, 0x0, 0x0)
    MilestoneDisplayTime: (F32, 0x0, 0x0, 0x0)
    MilestoneTransitionOutEasingType: (U8, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MilestoneTransitionInEasingType: (U8, 0x0, 0x0, 0x0)
    MilestoneTextPosition: (Hash, 0x0, 0x0, 0x0)
    EnemyFrame: (Hash, 0x0, 0x0, 0x0)
    MilestoneTransitionOutMinAlpha: (U8, 0x0, 0x0, 0x0)
    AllyFrame: (Hash, 0x0, 0x0, 0x0)
    0x4ea59d14: (Bool, 0x0, 0x0, 0x0)
    UiSoundForPersonalBest: (String, 0x0, 0x0, 0x0)
    UniqueEffectElements: (Embed, 0x0, 0x0, StatStoneMilestoneVfxDefinition)
    MilestoneTransitionInMinAlpha: (U8, 0x0, 0x0, 0x0)
    MilestoneBgFrameOther: (Hash, 0x0, 0x0, 0x0)
    MilestoneName: (Hash, 0x0, 0x0, 0x0)
    MilestoneTransitionInTime: (F32, 0x0, 0x0, 0x0)
    MilestoneOtherIntroTime: (F32, 0x0, 0x0, 0x0)
    CommonEffectElements: (Embed, 0x0, 0x0, StatStoneMilestoneVfxDefinition)
    MilestoneOwnerIcon: (Hash, 0x0, 0x0, 0x0)
    ChampIconMinAlpha: (U8, 0x0, 0x0, 0x0)
    SelfFrame: (Hash, 0x0, 0x0, 0x0)
    MilestoneTransitionOutTime: (F32, 0x0, 0x0, 0x0)
    MilestoneFgUncolored: (Hash, 0x0, 0x0, 0x0)
    UiSound: (String, 0x0, 0x0, 0x0)
    MilestoneBgFrameSelf: (Hash, 0x0, 0x0, 0x0)
    UiSoundForPersonalBestForLocalPlayer: (String, 0x0, 0x0, 0x0)
    MilestoneFgEffectTinted: (Hash, 0x0, 0x0, 0x0)
    MilestoneTransitionInMaxAlpha: (U8, 0x0, 0x0, 0x0)
    ChampIconNativeOffset: (F32, 0x0, 0x0, 0x0)
    PersonalBestIntroTime: (F32, 0x0, 0x0, 0x0)
    MilestoneBgEffectTinted: (Hash, 0x0, 0x0, 0x0)
    MaxNumberOfMilestonesToShowPerStonePerGame: (U32, 0x0, 0x0, 0x0)
    MilestoneDisplayTimeForLocalPlayer: (F32, 0x0, 0x0, 0x0)
    MilestoneOwnerScene: (Hash, 0x0, 0x0, 0x0)
    MilestoneCount: (Hash, 0x0, 0x0, 0x0)
    UiSoundForLocalPlayer: (String, 0x0, 0x0, 0x0)
    pass

class TftAnimClipModifier():
    pass

class IScriptPreload():
    pass

class IconElementGradientExtension(IconElementDataExtension):
    mStartColor: (Vec4, 0x0, 0x0, 0x0)
    mCustomGradientParams: (Vec4, 0x0, 0x0, 0x0)
    mAlphaTexture: (String, 0x0, 0x0, 0x0)
    DitherStrength: (F32, 0x0, 0x0, 0x0)
    mEndColor: (Vec4, 0x0, 0x0, 0x0)
    mGradientDirection: (U32, 0x0, 0x0, 0x0)
    0xda784e92: (Bool, 0x0, 0x0, 0x0)
    pass

class TftTrovesViewControllerV2(ViewController):
    FailureSubtitleTraKey: (String, 0x0, 0x0, 0x0)
    TftBannerIconData: (Embed, 0x0, 0x0, TftBannerIconData)
    Scene: (Hash, 0x0, 0x0, 0x0)
    CraftButton: (Hash, 0x0, 0x0, 0x0)
    BannerList: (Hash, 0x0, 0x0, 0x0)
    SubtitleText: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    0x40810d53: (Link, 0x0, 0x0, ModalDialogViewController)
    NoActiveBannersIcon: (Hash, 0x0, 0x0, 0x0)
    Roll10TextDisable: (Hash, 0x0, 0x0, 0x0)
    MilestoneRewardsTemplate: (Embed, 0x0, 0x0, 0x93e412e0)
    FailureIcon: (Hash, 0x0, 0x0, 0x0)
    MoreInfoButton: (Hash, 0x0, 0x0, 0x0)
    Roll10Text: (Hash, 0x0, 0x0, 0x0)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    ActiveBannerParent: (Hash, 0x0, 0x0, 0x0)
    CraftTextDisable: (Hash, 0x0, 0x0, 0x0)
    FailureTitleTraKey: (String, 0x0, 0x0, 0x0)
    Roll1Button: (Hash, 0x0, 0x0, 0x0)
    CraftText: (Hash, 0x0, 0x0, 0x0)
    BannerTimer: (Pointer, 0x0, 0x0, TftEventTimer)
    RedeemTrakey: (String, 0x0, 0x0, 0x0)
    MilestoneTooltipIcon: (Hash, 0x0, 0x0, 0x0)
    0xa4419c92: (Map, String, String, 0x0)
    FailureText: (Hash, 0x0, 0x0, 0x0)
    MilestoneTooltipButton: (Hash, 0x0, 0x0, 0x0)
    CraftTextClicked: (Hash, 0x0, 0x0, 0x0)
    Roll10Button: (Hash, 0x0, 0x0, 0x0)
    CraftSubtitle: (Hash, 0x0, 0x0, 0x0)
    Roll1TextDisable: (Hash, 0x0, 0x0, 0x0)
    NoContentSubtitleTraKey: (String, 0x0, 0x0, 0x0)
    NoContentTitleTraKey: (String, 0x0, 0x0, 0x0)
    Roll1TextClicked: (Hash, 0x0, 0x0, 0x0)
    Roll1Text: (Hash, 0x0, 0x0, 0x0)
    Roll10TextClicked: (Hash, 0x0, 0x0, 0x0)
    BannerBackground: (Hash, 0x0, 0x0, 0x0)
    0xe00d8f17: (String, 0x0, 0x0, 0x0)
    0xeceb0f26: (String, 0x0, 0x0, 0x0)
    OwnedTrakey: (String, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    0xfbff5912: (String, 0x0, 0x0, 0x0)
    pass

class SpellPassiveData():
    mDisplayFlags: (U8, 0x0, 0x0, 0x0)
    mRemoveWhenOnCooldown: (Bool, 0x0, 0x0, 0x0)
    RemoveOnPopCharacterData: (Bool, 0x0, 0x0, 0x0)
    mBuff: (Link, 0x0, 0x0, SpellObject)
    mWhenToAddSpell: (U32, 0x0, 0x0, 0x0)
    mRemoveWithSpell: (Bool, 0x0, 0x0, 0x0)
    RemoveOnPushCharacterData: (Bool, 0x0, 0x0, 0x0)
    pass

class ReturnToCaster(MissileTriggeredActionSpec):
    mPreserveSpeed: (Bool, 0x0, 0x0, 0x0)
    mOverrideSpec: (Pointer, 0x0, 0x0, MissileMovementSpec)
    pass

class BannerFrameData():
    NameTranslationKey: (String, 0x0, 0x0, 0x0)
    VfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    Skin: (String, 0x0, 0x0, 0x0)
    Texture: (String, 0x0, 0x0, 0x0)
    SkinMeshProperties: (Embed, 0x0, 0x0, SkinMeshDataProperties)
    BannerFrameId: (U32, 0x0, 0x0, 0x0)
    Skeleton: (String, 0x0, 0x0, 0x0)
    InventoryIcon: (String, 0x0, 0x0, 0x0)
    AnimationGraphData: (Link, 0x0, 0x0, AnimationGraphData)
    pass

class SpellLockDeltaTimeData():
    mSpellLockDeltaTimeCalculation: (Pointer, 0x0, 0x0, IGameCalculation)
    pass

class FloatTableSet(RsTableSet, ScriptTableSet):
    pass

class TftBannerReward(TftBannerNode):
    Quantity: (U32, 0x0, 0x0, 0x0)
    Rarity: (U32, 0x0, 0x0, 0x0)
    RewardTexturePath: (String, 0x0, 0x0, 0x0)
    pass

class IsOwnerAliveConditionData(VfxSpawnConditionData):
    pass

class 0xd55b5c23(IContextualCondition):
    DamageResultType: (U32, 0x0, 0x0, 0x0)
    pass

class StringTableSet(RsTableSet, ScriptTableSet):
    pass

class LevelScriptLegacyBlock(LevelScriptBlock):
    pass

class UiMetricUnitCreepScore(UiMetricUnitTypeI, UiMetricUnitTypeSimpleI):
    ShowDisguise: (Bool, 0x0, 0x0, 0x0)
    CsIcon: (Hash, 0x0, 0x0, 0x0)
    CsText: (Hash, 0x0, 0x0, 0x0)
    pass

class BannerConfiguration():
    LeagueName: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    Configuration: (List, 0x0, Embed, SponsoredBanner)
    EsportsTeam: (Hash, 0x0, 0x0, 0x0)
    pass

class NotMaterialDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    mDriver: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    mDriver: (Pointer, 0x0, 0x0, IDynamicMaterialBoolDriver)
    pass

class 0xd5b41170():
    Passes: (List, 0x0, Embed, 0x95a54f7f)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class 0xd5c5318a():
    ValueDriver: (Pointer, 0x0, 0x0, 0x6ca3cfd)
    Key: (String, 0x0, 0x0, 0x0)
    pass

class DamageTypeRadialChart():
    ArcFillElements: (List, 0x3, Hash, 0x0)
    pass

class UnitShopItemTraitData():
    TraitNub: (Hash, 0x0, 0x0, 0x0)
    Highlight: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    NameText: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class FxActionSfx(IFxAction):
    EventName: (String, 0x0, 0x0, 0x0)
    AudioSource: (Embed, 0x0, 0x0, FxTarget)
    AudioSource: (Embed, 0x0, 0x0, FxObjectSelector)
    Position: (Embed, 0x0, 0x0, FxTransform)
    UseCharacterTags: (Bool, 0x0, 0x0, 0x0)
    Location: (Pointer, 0x0, 0x0, IFxLocation)
    ForceStopWhenDone: (Bool, 0x0, 0x0, 0x0)
    pass

class EmoteLoadoutGridButtonData(LoadoutGridButtonData):
    pass

class MaxAllSkillsCheat(Cheat):
    mOnlyOnePointEach: (Bool, 0x0, 0x0, 0x0)
    mTarget: (U32, 0x0, 0x0, 0x0)
    pass

class BoolValueGet(DirectValueGet):
    Value: (Bool, 0x0, 0x0, 0x0)
    pass

class ElementGroupButtonData(ElementGroupData):
    DefaultStateElements: (Embed, 0x0, 0x0, ElementGroupButtonState)
    SelectedStateElements: (Embed, 0x0, 0x0, ElementGroupButtonState)
    InactiveTooltipTraKey: (String, 0x0, 0x0, 0x0)
    SelectedClickedStateElements: (Embed, 0x0, 0x0, ElementGroupButtonState)
    HitRegionElement: (Link, 0x0, 0x0, RegionElementData)
    InactiveStateElements: (Embed, 0x0, 0x0, ElementGroupButtonState)
    ClickReleaseParticleElement: (Link, 0x0, 0x0, ParticleSystemElementData)
    ActiveTooltipTraKey: (String, 0x0, 0x0, 0x0)
    SoundEvents: (Pointer, 0x0, 0x0, ElementSoundEvents)
    ClickedStateElements: (Embed, 0x0, 0x0, ElementGroupButtonState)
    SelectedHoverStateElements: (Embed, 0x0, 0x0, ElementGroupButtonState)
    HoverStateElements: (Embed, 0x0, 0x0, ElementGroupButtonState)
    IsActive: (Bool, 0x0, 0x0, 0x0)
    IsEnabled: (Bool, 0x0, 0x0, 0x0)
    IsSelected: (Bool, 0x0, 0x0, 0x0)
    pass

class UiMetricTeamKills(UiMetricTypeI):
    TeamKillsIcon: (Hash, 0x0, 0x0, 0x0)
    Team1KillText: (Hash, 0x0, 0x0, 0x0)
    Team2KillText: (Hash, 0x0, 0x0, 0x0)
    pass

class LaunchAreaData():
    DivergenceTolerance: (F32, 0x0, 0x0, 0x0)
    TargetDistance: (F32, 0x0, 0x0, 0x0)
    IndicatorTextureName: (String, 0x0, 0x0, 0x0)
    InnerRadius: (F32, 0x0, 0x0, 0x0)
    Radius: (F32, 0x0, 0x0, 0x0)
    IndicatorRadius: (F32, 0x0, 0x0, 0x0)
    InnerAreaTargetDistance: (F32, 0x0, 0x0, 0x0)
    pass

class AreaAim(TargetingTypeData):
    pass

class SequencePhaseOverride():
    Duration: (F32, 0x0, 0x0, 0x0)
    OverrideDuration: (Bool, 0x0, 0x0, 0x0)
    OverrideType: (Bool, 0x0, 0x0, 0x0)
    Type: (U32, 0x0, 0x0, 0x0)
    pass

class SpellSlotSimpleUiDefinition(SpellSlotBasicUiDefinition):
    OverlayHandle: (Hash, 0x0, 0x0, 0x0)
    SpellGuessLockoutIcon: (Hash, 0x0, 0x0, 0x0)
    CooldownFx: (Hash, 0x0, 0x0, 0x0)
    pass

class MatchHistoryMapItemData():
    ItemId: (U32, 0x0, 0x0, 0x0)
    IconPath: (String, 0x0, 0x0, 0x0)
    NameId: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class EsportsBannerOptions():
    SubMeshName: (String, 0x0, 0x0, 0x0)
    DefaultTexturePath: (File, 0x0, 0x0, 0x0)
    DefaultTexturePath: (String, 0x0, 0x0, 0x0)
    IsSpectatorOnly: (Bool, 0x0, 0x0, 0x0)
    RequiredTeamMatches: (U32, 0x0, 0x0, 0x0)
    DefaultBlankMaterial: (Link, 0x0, 0x0, IMaterialDef)
    pass

class 0xd65c937c():
    CompleteDefault: (String, 0x0, 0x0, 0x0)
    TrackerGroup: (Hash, 0x0, 0x0, 0x0)
    ActiveSelected: (String, 0x0, 0x0, 0x0)
    InactiveSelected: (String, 0x0, 0x0, 0x0)
    TrackerIcon: (Hash, 0x0, 0x0, 0x0)
    ActiveHover: (String, 0x0, 0x0, 0x0)
    ActiveDefault: (String, 0x0, 0x0, 0x0)
    InactiveDefault: (String, 0x0, 0x0, 0x0)
    CompleteHover: (String, 0x0, 0x0, 0x0)
    TrackerLayout: (Hash, 0x0, 0x0, 0x0)
    InactiveHover: (String, 0x0, 0x0, 0x0)
    HitRegion: (Hash, 0x0, 0x0, 0x0)
    CompleteSelected: (String, 0x0, 0x0, 0x0)
    pass

class AiUnitConfigSkinLink():
    Skin: (String, 0x0, 0x0, 0x0)
    pass

class HudPingData():
    DistanceToNotTrollPingCorpses: (F32, 0x0, 0x0, 0x0)
    TimeToNotTrollPingCorpses: (F32, 0x0, 0x0, 0x0)
    pass

class 0xd68073ec(ISequenceActionInstance):
    pass

class AnnouncementMap():
    Announcements: (Map, String, Link, AnnouncementDefinition)
    SpectatorOffsetRegion: (Hash, 0x0, 0x0, 0x0)
    AssetBinName: (String, 0x0, 0x0, 0x0)
    DeathRecapOffsetRegion: (Hash, 0x0, 0x0, 0x0)
    ParentList: (Link, 0x0, 0x0, AnnouncementMap)
    pass

class TftItemCombineTooltipData():
    FourstarBadge: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    ItemIconTwo: (Hash, 0x0, 0x0, 0x0)
    ChampionIcon: (Hash, 0x0, 0x0, 0x0)
    TwostarBadge: (Hash, 0x0, 0x0, 0x0)
    ThreestarBadge: (Hash, 0x0, 0x0, 0x0)
    ComponentIcons: (Hash, 0x0, 0x0, 0x0)
    ChampionName: (Hash, 0x0, 0x0, 0x0)
    OnestarBadge: (Hash, 0x0, 0x0, 0x0)
    ItemIconOne: (Hash, 0x0, 0x0, 0x0)
    pass

class HeroFloatingInfoResistData():
    MagicResistThreshold: (F32, 0x0, 0x0, 0x0)
    0x7870d4f: (Hash, 0x0, 0x0, 0x0)
    ArmorThreshold: (F32, 0x0, 0x0, 0x0)
    0xcd61161d: (Hash, 0x0, 0x0, 0x0)
    0xdbfad963: (Hash, 0x0, 0x0, 0x0)
    pass

class TftMapTraitList():
    Traits: (List, 0x0, Pointer, TftMapTraitData)
    pass

class EmoteAlternativeRadialViewController(RadialMenuViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    pass

class TftBattlepassViewController(ViewController):
    MilestoneProgressMeter: (Embed, 0x0, 0x0, UiMilestoneProgressMeter)
    MilestonesViewPane: (Hash, 0x0, 0x0, 0x0)
    SelectedMilestoneHighlight: (Hash, 0x0, 0x0, 0x0)
    BackgroundImage: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    SelectedRewardBanner: (Embed, 0x0, 0x0, TftBattlepassSelectedRewardBannerUiData)
    WelcomeDialogViewController: (Link, 0x0, 0x0, ModalDialogViewController)
    ThemeDataMap: (Map, String, Embed, 0x5cb6b755)
    SelectedRewardBannerScene: (Hash, 0x0, 0x0, 0x0)
    MilestoneTimelineEnd: (Embed, 0x0, 0x0, UiMilestoneTimelineEnd)
    RewardBannerTransitionOut: (Embed, 0x0, 0x0, HudMenuTransitionData)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    LootTableButton: (Hash, 0x0, 0x0, 0x0)
    ModalDialogViewController: (Link, 0x0, 0x0, ModalDialogViewController)
    ViewPaneDefinition: (Embed, 0x0, 0x0, ViewPaneDefinition)
    SelectedReward: (Embed, 0x0, 0x0, TftBattlepassSelectedRewardUiData)
    PassTitle: (Hash, 0x0, 0x0, 0x0)
    UiMilestoneMissionTemplate: (Embed, 0x0, 0x0, UiMilestoneMissionTemplate)
    UpgradePassButton: (Hash, 0x0, 0x0, 0x0)
    RewardBannerDurationSecs: (F32, 0x0, 0x0, 0x0)
    BattlepassScene: (Hash, 0x0, 0x0, 0x0)
    DefaultThemeData: (Embed, 0x0, 0x0, 0x5cb6b755)
    0xf3399e0e: (Hash, 0x0, 0x0, 0x0)
    PassSubtitle: (Hash, 0x0, 0x0, 0x0)
    pass

class TftDamageSkinDescriptor():
    EffectType: (U32, 0x0, 0x0, 0x0)
    EffectKey: (String, 0x0, 0x0, 0x0)
    AttachedToBone: (U32, 0x0, 0x0, 0x0)
    TriggeredBy: (U32, 0x0, 0x0, 0x0)
    EffectDelay: (F32, 0x0, 0x0, 0x0)
    pass

class UiElementTextData(UiElementData):
    mTextAlignmentVertical: (U8, 0x0, 0x0, 0x0)
    FontDescription: (Link, 0x0, 0x0, GameFontDescription)
    WrappingMode: (U8, 0x0, 0x0, 0x0)
    0x6e4f45c5: (Bool, 0x0, 0x0, 0x0)
    mHtmlStyleSheet: (Link, 0x0, 0x0, CssSheet)
    mFontDescription: (Link, 0x0, 0x0, GameFontDescription)
    mTextAlignmentHorizontal: (U8, 0x0, 0x0, 0x0)
    TraKey: (String, 0x0, 0x0, 0x0)
    TextAlignmentHorizontal: (U8, 0x0, 0x0, 0x0)
    TextAlignmentVertical: (U8, 0x0, 0x0, 0x0)
    HtmlStyleSheet: (Link, 0x0, 0x0, CssSheet)
    IconScale: (F32, 0x0, 0x0, 0x0)
    pass

class StealthCharacterFadeInstance():
    Fade: (Link, 0x0, 0x0, StealthCharacterFade)
    pass

class OptionItemGroup(IOptionItem):
    Items: (List, 0x0, Pointer, IOptionItem)
    Template: (Hash, 0x0, 0x0, 0x0)
    LabelTraKey: (String, 0x0, 0x0, 0x0)
    ExpandedByDefault: (Bool, 0x0, 0x0, 0x0)
    pass

class FaceTargetEventData(BaseEventData):
    BlendOutTime: (F32, 0x0, 0x0, 0x0)
    FaceTarget: (U8, 0x0, 0x0, 0x0)
    BlendInTime: (F32, 0x0, 0x0, 0x0)
    YRotationDegrees: (F32, 0x0, 0x0, 0x0)
    pass

class LayoutStyleGrid(LayoutStyleBase):
    VerticalFillDirection: (U8, 0x0, 0x0, 0x0)
    RowHorizontalAlignment: (U8, 0x0, 0x0, 0x0)
    RowVerticalAlignment: (U8, 0x0, 0x0, 0x0)
    HorizontalFillDirection: (U8, 0x0, 0x0, 0x0)
    pass

class JunglePathRecommendation():
    ChaosJunglePath: (List, 0x0, Pointer, JungleAction)
    OrderJunglePath: (List, 0x0, Pointer, JungleAction)
    pass

class 0xd813df3b(TargetingTypeData):
    pass

class CallFunctionBlock(IScriptBlock, IFunctionalScriptBlock):
    Function: (Link, 0x0, 0x0, ScriptFunction)
    pass

class UiMilestoneFrameData():
    LockedHoverIcon: (Hash, 0x0, 0x0, 0x0)
    AvailableDefaultIcon: (Hash, 0x0, 0x0, 0x0)
    CompleteDefaultIcon: (Hash, 0x0, 0x0, 0x0)
    ClaimableHoverIcon: (Hash, 0x0, 0x0, 0x0)
    AvailableHoverIcon: (Hash, 0x0, 0x0, 0x0)
    CompleteHoverIcon: (Hash, 0x0, 0x0, 0x0)
    LockedDefaultIcon: (Hash, 0x0, 0x0, 0x0)
    ClaimableDefaultIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xd82714cc():
    Color: (Color, 0x0, 0x0, 0x0)
    Name: (Hash, 0x0, 0x0, 0x0)
    Flags: (U16, 0x0, 0x0, 0x0)
    pass

class UiSceneViewPane(UiScene):
    pass

class UiMetricTeamGold(UiMetricTypeI):
    Team2GoldText: (Hash, 0x0, 0x0, 0x0)
    Team1GoldIcon: (Hash, 0x0, 0x0, 0x0)
    Team1GoldText: (Hash, 0x0, 0x0, 0x0)
    Team2GoldIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class CelebrationLabFields():
    RatedTierVfx: (Map, U32, Hash, 0x0)
    RatedTierTraKeys: (Map, U32, String, 0x0)
    RatedTiersTraKeys: (Map, String, String, 0x0)
    pass

class HealthDynamicMaterialFloatDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    pass

class 0xd8662a22(ILolSpellScriptEvent):
    pass

class 0xd866344b():
    pass

class 0xd86db9b6(0xb72a7d67):
    DestroyedSkin: (String, 0x0, 0x0, 0x0)
    DestroyedCharacter: (String, 0x0, 0x0, 0x0)
    pass

class ObjectiveVotetTallyData():
    ForCountIcon: (Hash, 0x0, 0x0, 0x0)
    CountBg: (Hash, 0x0, 0x0, 0x0)
    PendingCountIcon: (Hash, 0x0, 0x0, 0x0)
    ForCount: (Hash, 0x0, 0x0, 0x0)
    VfxPlayerReject: (Hash, 0x0, 0x0, 0x0)
    RejectCount: (Hash, 0x0, 0x0, 0x0)
    RejectCountIcon: (Hash, 0x0, 0x0, 0x0)
    VfxPlayerFor: (Hash, 0x0, 0x0, 0x0)
    pass

class CountAttacksCheat(Cheat):
    pass

class OptionItemFilter_Map(IOptionItemFilter):
    Map: (Hash, 0x0, 0x0, 0x0)
    pass

class ViewControllerList():
    ViewControllers: (List, 0x0, String, 0x0)
    ViewControllers: (List2, 0x0, String, 0x0)
    Filter: (Pointer, 0x0, 0x0, ViewControllerListFilterI)
    Filter: (Pointer, 0x0, 0x0, ViewControllerFilterI)
    pass

class UiElementMeterSkin():
    TipElements: (List, 0x0, Hash, 0x0)
    TipElements: (List2, 0x0, Hash, 0x0)
    ReverseDirectionalTipElements: (List, 0x0, Hash, 0x0)
    ReverseDirectionalTipElements: (List2, 0x0, Hash, 0x0)
    0x4b68f340: (List2, 0x0, Hash, 0x0)
    BarElementList: (List2, 0x0, Hash, 0x0)
    Sliver: (Hash, 0x0, 0x0, 0x0)
    BarElements: (List, 0x0, Hash, 0x0)
    BarElements: (List2, 0x0, Hash, 0x0)
    TipElementList: (List2, 0x0, Hash, 0x0)
    pass

class ChangeMissileSpeed(MissileTriggeredActionSpec):
    mSpeedValue: (F32, 0x0, 0x0, 0x0)
    mSpeedChangeType: (U32, 0x0, 0x0, 0x0)
    pass

class TftUxTunables():
    TftPartnerGroupColors: (List, 0x4, Color, 0x0)
    TftFutureSightIconColor: (Color, 0x0, 0x0, 0x0)
    TftMatchmakingIconColor: (Color, 0x0, 0x0, 0x0)
    pass

class 0xd97f9bd3(TftCutsceneMissileClip):
    SplineInfo: (Pointer, 0x0, 0x0, ISplineInfo)
    pass

class MatchmakingQueue():
    RankedType: (U8, 0x0, 0x0, 0x0)
    IllustrationIconPath: (String, 0x0, 0x0, 0x0)
    Description: (String, 0x0, 0x0, 0x0)
    SmallIconPath: (String, 0x0, 0x0, 0x0)
    MaxPartySize: (U8, 0x0, 0x0, 0x0)
    ShortName: (String, 0x0, 0x0, 0x0)
    TftDisplayName: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    0x911a6a86: (Bool, 0x0, 0x0, 0x0)
    MapId: (U8, 0x0, 0x0, 0x0)
    DetailedDescription: (String, 0x0, 0x0, 0x0)
    Product: (String, 0x0, 0x0, 0x0)
    QueueId: (I64, 0x0, 0x0, 0x0)
    Mode: (String, 0x0, 0x0, 0x0)
    QueueType: (String, 0x0, 0x0, 0x0)
    pass

class FixedTimeMovementSpec(MissileMovementSpec):
    mProjectTargetToCastRange: (Bool, 0x0, 0x0, 0x0)
    mUseGroundHeightAtTarget: (Bool, 0x0, 0x0, 0x0)
    mInferDirectionFromFacingIfNeeded: (Bool, 0x0, 0x0, 0x0)
    mTargetHeightAugment: (F32, 0x0, 0x0, 0x0)
    mTravelTime: (F32, 0x0, 0x0, 0x0)
    pass

class VfxMaterialOverrideDefinitionData():
    FixedAlphaScrolling: (Bool, 0x0, 0x0, 0x0)
    TransitionTexture: (String, 0x0, 0x0, 0x0)
    UScrolling: (F32, 0x0, 0x0, 0x0)
    SubMeshName: (Option, 0x0, String, 0x0)
    SubMeshName: (String, 0x0, 0x0, 0x0)
    RenderingMode: (I32, 0x0, 0x0, 0x0)
    OverrideBlendMode: (U32, 0x0, 0x0, 0x0)
    TransitionSample: (F32, 0x0, 0x0, 0x0)
    Priority: (I32, 0x0, 0x0, 0x0)
    Flags: (U32, 0x0, 0x0, 0x0)
    BaseTexture: (String, 0x0, 0x0, 0x0)
    UvScrolling: (Vec2, 0x0, 0x0, 0x0)
    TransitionSource: (U32, 0x0, 0x0, 0x0)
    Material: (Link, 0x0, 0x0, MaterialDef)
    Material: (Link, 0x0, 0x0, IMaterialDef)
    GlossTexture: (String, 0x0, 0x0, 0x0)
    VScrolling: (F32, 0x0, 0x0, 0x0)
    pass

class ClearAlreadyHitTrackingOnMovementCompleteSpec(MissileBehaviorSpec):
    pass

class CastOnHit(MissileBehaviorSpec):
    RollForCriticalHitResult: (Bool, 0x0, 0x0, 0x0)
    pass

class ResetGoldCheat(Cheat):
    mTarget: (U32, 0x0, 0x0, 0x0)
    pass

class LoadingScreenPlayerCardsViewController(ViewController):
    CardTemplate: (Pointer, 0x0, 0x0, LoadingScreenPlayerCardBaseData)
    SpacerData: (Pointer, 0x0, 0x0, 0xacb2dba1)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    LowerCardRegion: (Hash, 0x0, 0x0, 0x0)
    UpperCardRegion: (Hash, 0x0, 0x0, 0x0)
    IsTeamBased: (Bool, 0x0, 0x0, 0x0)
    pass

class ScoreLineBaseUiData():
    Scene: (Hash, 0x0, 0x0, 0x0)
    Portrait: (Embed, 0x0, 0x0, ScoreLinePortraitUiData)
    Portrait: (Embed, 0x0, 0x0, UiPlayerPortraitData)
    FowSlotHighlight: (Hash, 0x0, 0x0, 0x0)
    DragBarSlot: (Hash, 0x0, 0x0, 0x0)
    PortraitRegion: (Hash, 0x0, 0x0, 0x0)
    DeadSlotHighlight: (Hash, 0x0, 0x0, 0x0)
    IndividualScoreDefinitions: (Map, U8, Embed, IndividualScoreUiData)
    Metrics: (Map, U8, Pointer, UiMetricUnitTypeI)
    MusicButton: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xda3ab4c4(IFxAction):
    Magnitude: (F32, 0x0, 0x0, 0x0)
    ShakesPerSecond: (F32, 0x0, 0x0, 0x0)
    FalloffRate: (F32, 0x0, 0x0, 0x0)
    Direction: (Vec3, 0x0, 0x0, 0x0)
    pass

class 0xda3c6dc6():
    mSceneTransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mSceneTransitionOut: (Embed, 0x0, 0x0, HudMenuTransitionData)
    pass

class TargetTeamFilter(IStatStoneLogicDriver):
    Self: (Bool, 0x0, 0x0, 0x0)
    Enemy: (Bool, 0x0, 0x0, 0x0)
    Ally: (Bool, 0x0, 0x0, 0x0)
    pass

class IDynamicMaterialBoolDriver(IDynamicMaterialFloatDriver):
    pass

class TftSinusoidalHeightSolver(TftHeightSolverType):
    Amplitude: (F32, 0x0, 0x0, 0x0)
    NumberOfPeriods: (F32, 0x0, 0x0, 0x0)
    PhaseShift: (F32, 0x0, 0x0, 0x0)
    VerticalOffset: (F32, 0x0, 0x0, 0x0)
    pass

class 0xda790a65(ISequenceAction):
    0xd07dcd34: (Link, 0x0, 0x0, SequenceObjectSelector)
    pass

class Blnd2GdsMapping():
    mBlnd2GdsMap: (Map, String, Embed, 0xbded2d7f)
    pass

class HudLoadingScreenWidgetPlayers(IHudLoadingScreenWidget):
    mCardConfig: (Embed, 0x0, 0x0, PlayerCardWidgetConfig)
    pass

class OverrideResourceResolver(IResourceResolver):
    SourceResolver: (Link, 0x0, 0x0, IResourceResolver)
    ResourceMap: (Map, Hash, Link, IResource)
    pass

class GdsMapObject(GenericMapPlaceable):
    Type: (U8, 0x0, 0x0, 0x0)
    VisibilityController: (Link, 0x0, 0x0, IMapVisibilityController)
    EyeCandy: (Bool, 0x0, 0x0, 0x0)
    IgnoreCollisionOnPlacement: (Bool, 0x0, 0x0, 0x0)
    MapObjectSkinId: (U32, 0x0, 0x0, 0x0)
    BoxMin: (Vec3, 0x0, 0x0, 0x0)
    BoxMax: (Vec3, 0x0, 0x0, 0x0)
    ExtraInfo: (List, 0x0, Pointer, GdsMapObjectExtraInfo)
    pass

class LootItemLineElements():
    LootLineItemGroup: (Hash, 0x0, 0x0, 0x0)
    LootLineArrowIcon: (Hash, 0x0, 0x0, 0x0)
    LootLineItemDropRateText: (Hash, 0x0, 0x0, 0x0)
    LootLineItemButton: (Hash, 0x0, 0x0, 0x0)
    LootLineItemSpacing: (Hash, 0x0, 0x0, 0x0)
    LootLineItemNameText: (Hash, 0x0, 0x0, 0x0)
    pass

class TftHudMobileDownscaleData():
    mDownscale: (F32, 0x0, 0x0, 0x0)
    0xd4d2ea52: (F32, 0x0, 0x0, 0x0)
    pass

class 0xdae7f670(IScriptBt):
    Blocks: (List2, 0x0, Pointer, IBehaviorScriptBlock)
    pass

class ItemSelectionViewController(ItemSelectionBaseViewController, ViewController):
    ItemSlots: (List, 0x0, Embed, UiItemSelectionSlotData)
    Scene: (Hash, 0x0, 0x0, 0x0)
    Loadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    pass

class TftMapCharacterRecordData():
    Tier: (U8, 0x0, 0x0, 0x0)
    ShopData: (List, 0x0, Embed, TftMapShopData)
    LinkedTraits: (List, 0x0, Embed, TftMapTraitContributionData)
    pass

class UiPositionBase():
    pass

class DeathRecapShowcase():
    Scene: (Hash, 0x0, 0x0, 0x0)
    FrameScene: (Hash, 0x0, 0x0, 0x0)
    MasterySlot: (Embed, 0x0, 0x0, DeathRecapShowcaseSlotMasteryData)
    TextSummonerName: (Hash, 0x0, 0x0, 0x0)
    PortraitTimer: (Hash, 0x0, 0x0, 0x0)
    PortraitScene: (Hash, 0x0, 0x0, 0x0)
    StatStoneSlot: (Embed, 0x0, 0x0, DeathRecapShowcaseSlotStatStoneData)
    PortraitIconKill: (Hash, 0x0, 0x0, 0x0)
    KdaSlot: (Embed, 0x0, 0x0, DeathRecapShowcaseSlotKdaData)
    Pips: (Embed, 0x0, 0x0, DeathRecapShowcasePips)
    PortraitIconAssist: (Hash, 0x0, 0x0, 0x0)
    ShowUiTextHandle: (Hash, 0x0, 0x0, 0x0)
    DragRegion: (Hash, 0x0, 0x0, 0x0)
    TooltipAnchor: (Hash, 0x0, 0x0, 0x0)
    DetailsScene: (Hash, 0x0, 0x0, 0x0)
    PortraitIconSummoner: (Hash, 0x0, 0x0, 0x0)
    SlotsLayout: (Hash, 0x0, 0x0, 0x0)
    pass

class TargetingPriorityList():
    mAffectsStatusFlags: (U32, 0x0, 0x0, 0x0)
    mSpellFlags: (U32, 0x0, 0x0, 0x0)
    Radius: (F32, 0x0, 0x0, 0x0)
    mAffectsTypeFlags: (U32, 0x0, 0x0, 0x0)
    TargetingParametersList: (List2, 0x0, Pointer, TargetingParameters)
    pass

class IconElementDataExtension():
    pass

class IVectorGet(IRsValueGet, IScriptValueGet):
    pass

class 0xdb7c04f8():
    InkFillTime: (F32, 0x0, 0x0, 0x0)
    Acceleration: (Vec2, 0x0, 0x0, 0x0)
    MovementProjectionY: (Vec3, 0x0, 0x0, 0x0)
    MovementProjectionX: (Vec3, 0x0, 0x0, 0x0)
    MoveKick: (F32, 0x0, 0x0, 0x0)
    MoveDensity: (F32, 0x0, 0x0, 0x0)
    JetKinetics: (List, 0x3, Vec3, 0x0)
    Viscosity: (F32, 0x0, 0x0, 0x0)
    InitialDensityMapAsset: (String, 0x0, 0x0, 0x0)
    RenderGridSize: (I32, 0x0, 0x0, 0x0)
    Dissipation: (F32, 0x0, 0x0, 0x0)
    JetChaos: (List, 0x3, Vec3, 0x0)
    Diffusion: (F32, 0x0, 0x0, 0x0)
    Buoyancy: (F32, 0x0, 0x0, 0x0)
    InkFillRate: (F32, 0x0, 0x0, 0x0)
    pass

class IntDefaultTableGet(IIntGet):
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Table: (Pointer, 0x0, 0x0, RsTable)
    Var: (String, 0x0, 0x0, 0x0)
    Default: (I32, 0x0, 0x0, 0x0)
    pass

class OptionItemSliderVolume(OptionItemSliderFloat):
    MuteButtonTemplate: (Hash, 0x0, 0x0, 0x0)
    MuteOption: (U16, 0x0, 0x0, 0x0)
    pass

class TftUnitPropertyValueIntegerSet(TftUnitPropertyValue):
    Value: (List2, 0x0, I32, 0x0)
    pass

class 0xdb9a90ba(0xe561be2e):
    Source: (Link, 0x0, 0x0, SequenceObjectSelector)
    DebugOverride: (Hash, 0x0, 0x0, 0x0)
    pass

class UiTeamFightTeamMemberData():
    Scene: (Hash, 0x0, 0x0, 0x0)
    MultikillIcon: (Pointer, 0x0, 0x0, UiMultiKillIconData)
    Frame: (Embed, 0x0, 0x0, UiTeamMemberData)
    pass

class FxActionVfxStatic(FxActionVfxBase):
    pass

class HasBuffComparisonData():
    mCompareOp: (U8, 0x0, 0x0, 0x0)
    mBuffs: (List, 0x0, Embed, HasBuffData)
    pass

class StringGet(IStringGet, IScriptValueGet):
    Value: (String, 0x0, 0x0, 0x0)
    pass

class FxTiming():
    Offset: (F32, 0x0, 0x0, 0x0)
    ScaleTiming: (Bool, 0x0, 0x0, 0x0)
    PhaseIndex: (I32, 0x0, 0x0, 0x0)
    Duration: (F32, 0x0, 0x0, 0x0)
    Anchor: (U32, 0x0, 0x0, 0x0)
    Type: (U32, 0x0, 0x0, 0x0)
    pass

class TftTrovesCelebrationStandardSegmentData():
    InterItemTimingOffset: (F32, 0x0, 0x0, 0x0)
    EntryRevealSfx: (String, 0x0, 0x0, 0x0)
    InterItemTimingOffsetEpic: (F32, 0x0, 0x0, 0x0)
    EntrySfxOffset: (F32, 0x0, 0x0, 0x0)
    Sequence: (Link, 0x0, 0x0, Sequence)
    EntryEchoSfx: (String, 0x0, 0x0, 0x0)
    FirstItemTimingOffsetLegendary: (F32, 0x0, 0x0, 0x0)
    FirstItemTimingOffsetRare: (F32, 0x0, 0x0, 0x0)
    StandardRewardTemplateRareEpic: (Hash, 0x0, 0x0, 0x0)
    StandardContentBackground: (Hash, 0x0, 0x0, 0x0)
    FirstItemTimingOffsetEpic: (F32, 0x0, 0x0, 0x0)
    InterItemTimingOffsetRare: (F32, 0x0, 0x0, 0x0)
    InterItemTimingOffsetLegendary: (F32, 0x0, 0x0, 0x0)
    FirstItemTimingOffset: (F32, 0x0, 0x0, 0x0)
    BackgroundTimingOffset: (F32, 0x0, 0x0, 0x0)
    StandardRewardTemplateLegendary: (Hash, 0x0, 0x0, 0x0)
    0xfdfabc7d: (F32, 0x0, 0x0, 0x0)
    pass

class NeutralTimerSourceIconData():
    mTooltipName: (String, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    CampName: (Hash, 0x0, 0x0, 0x0)
    mIconName: (String, 0x0, 0x0, 0x0)
    TooltipName: (String, 0x0, 0x0, 0x0)
    pass

class 0xdbede580(ModalDialogViewController):
    0xed13979f: (Embed, 0x0, 0x0, UiHyperlink)
    pass

class ScriptCheat(Cheat):
    UseTargetAsSource: (Bool, 0x0, 0x0, 0x0)
    mTarget: (U32, 0x0, 0x0, 0x0)
    mScriptCallback: (Hash, 0x0, 0x0, 0x0)
    pass

class NavigationGroup():
    0x5f001719: (Bool, 0x0, 0x0, 0x0)
    Hash: (Hash, 0x0, 0x0, 0x0)
    pass

class HomeguardSkinUpgrade(ISkinUpgradeObject):
    pass

class ResourceMeterGroupData(ResourceMeterBaseData):
    MeterSkins: (Pointer, 0x0, 0x0, ResourceMeterSkinData)
    Meter: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xdc24bc6f():
    0x439b26dc: (String, 0x0, 0x0, 0x0)
    TroveBannerIcon: (Hash, 0x0, 0x0, 0x0)
    FailureText: (String, 0x0, 0x0, 0x0)
    0xabd0de07: (String, 0x0, 0x0, 0x0)
    FailureTexturePath: (String, 0x0, 0x0, 0x0)
    TroveButton: (Hash, 0x0, 0x0, 0x0)
    pass

class MaterialSamplerDataCollection():
    Entries: (Map, String, Embed, IdMappingEntry)
    NextId: (U16, 0x0, 0x0, 0x0)
    Data: (Map, U16, Embed, MaterialSamplerData)
    pass

class 0xdc53945d(ViewController):
    0x1ea15738: (List, 0x4, Hash, 0x0)
    0x1ea15738: (List, 0x5, Hash, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    RetryButton: (Hash, 0x0, 0x0, 0x0)
    CloseButton: (Hash, 0x0, 0x0, 0x0)
    pass

class AbilityObject():
    mName: (String, 0x0, 0x0, 0x0)
    mRootSpell: (Link, 0x0, 0x0, SpellObject)
    mLifetimeManuallyManaged: (Bool, 0x0, 0x0, 0x0)
    mType: (U8, 0x0, 0x0, 0x0)
    mChildSpells: (List, 0x0, Link, SpellObject)
    AbilityTraits: (U32, 0x0, 0x0, 0x0)
    pass

class InvalidClipData(ClipBaseData):
    pass

class IsRangedCastRequirement(ICastRequirement):
    pass

class LookAtSpellTargetHeightOffsetParametricUpdater(IFloatParametricUpdater):
    pass

class MissileAttachedTargetingDefinition():
    mBaseTextureName: (String, 0x0, 0x0, 0x0)
    mLineTextureName: (String, 0x0, 0x0, 0x0)
    mLineTextureWidth: (F32, 0x0, 0x0, 0x0)
    mEndPositionType: (U8, 0x0, 0x0, 0x0)
    mEndPositionLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    mLineEndTextureHeight: (F32, 0x0, 0x0, 0x0)
    mLineEndTextureName: (String, 0x0, 0x0, 0x0)
    mWidth: (F32, 0x0, 0x0, 0x0)
    mLineEndTextureWidth: (F32, 0x0, 0x0, 0x0)
    pass

class MapLightingV2(MapGraphicsFeature):
    BounceLightFalloffDistance: (F32, 0x0, 0x0, 0x0)
    MinimumEnvironmentColorContribution: (F32, 0x0, 0x0, 0x0)
    pass

class HudReplaySliderIconData():
    BlueTeamElementSelectedColor: (Color, 0x0, 0x0, 0x0)
    mElementSpacer: (F32, 0x0, 0x0, 0x0)
    mTooltipIconNames: (List, 0x0, String, 0x0)
    mElementAlphaDefault: (F32, 0x0, 0x0, 0x0)
    mElementName: (String, 0x0, 0x0, 0x0)
    mElementAlphaSelected: (F32, 0x0, 0x0, 0x0)
    mElementAlphaUnselected: (F32, 0x0, 0x0, 0x0)
    mType: (Hash, 0x0, 0x0, 0x0)
    RedeTeamElementUnselectedColor: (Color, 0x0, 0x0, 0x0)
    RedTeamElementSelectedColor: (Color, 0x0, 0x0, 0x0)
    ElementT1: (Hash, 0x0, 0x0, 0x0)
    mTooltipStyle: (U8, 0x0, 0x0, 0x0)
    BlueTeamElementUnselectedColor: (Color, 0x0, 0x0, 0x0)
    ElementT0: (Hash, 0x0, 0x0, 0x0)
    ElementTextT0: (Hash, 0x0, 0x0, 0x0)
    ElementTextT1: (Hash, 0x0, 0x0, 0x0)
    pass

class FontResolutionData():
    AutoScale: (Bool, 0x0, 0x0, 0x0)
    LocaleResolutions: (List, 0x0, Embed, FontLocaleResolutions)
    pass

class TftMobileLoginButtonData():
    Button: (Hash, 0x0, 0x0, 0x0)
    LoginStrategy: (U32, 0x0, 0x0, 0x0)
    pass

class IsOwnerHeroConditionData(VfxSpawnConditionData):
    pass

class EffectCircleMaskDesaturateElementData(EffectDesaturateElementData):
    pass

class UiMetricUnitBounty(UiMetricUnitTypeSimpleI):
    pass

class Cone(TargetingTypeData):
    pass

class LolSpellPreloadData():
    ModulePreloads: (List, 0x0, Pointer, ScriptPreloadModule)
    SpellPreloads: (List, 0x0, Pointer, ScriptPreloadSpell)
    ParticlePreloads: (List, 0x0, Pointer, ScriptPreloadParticle)
    CharacterPreloads: (List, 0x0, Pointer, ScriptPreloadCharacter)
    pass

class Obj_GeneralParticleEmitter(GameObject):
    pass

class FxActionVfxBase(IFxAction):
    ScalePlaybackSpeedReferenceDuration: (F32, 0x0, 0x0, 0x0)
    UseLocalRotation: (Bool, 0x0, 0x0, 0x0)
    Scale: (F32, 0x0, 0x0, 0x0)
    Particle: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    Position: (Embed, 0x0, 0x0, FxTransform)
    Location: (Pointer, 0x0, 0x0, IFxLocation)
    pass

class PatchingRootScene(RootScene):
    pass

class VfxPrimitiveBeamBase(VfxPrimitiveBase):
    mBeam: (Embed, 0x0, 0x0, VfxBeamDefinitionData)
    pass

class DecelToLocationMovementSpec(MissileMovementSpec):
    mProjectTargetToCastRange: (Bool, 0x0, 0x0, 0x0)
    mUseGroundHeightAtTarget: (Bool, 0x0, 0x0, 0x0)
    mInferDirectionFromFacingIfNeeded: (Bool, 0x0, 0x0, 0x0)
    mInitialSpeed: (F32, 0x0, 0x0, 0x0)
    mAcceleration: (F32, 0x0, 0x0, 0x0)
    mTargetHeightAugment: (F32, 0x0, 0x0, 0x0)
    mMinSpeed: (F32, 0x0, 0x0, 0x0)
    mMaxSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class 0xdd661aab():
    TriggerSpells: (List2, 0x0, Hash, 0x0)
    0x8f7842e4: (List2, 0x0, Pointer, 0x55f6bf86)
    OverrideParams: (Pointer, 0x0, 0x0, 0xc7e628b9)
    Condition: (Pointer, 0x0, 0x0, 0xfd51006c)
    pass

class NextBuffVars(ScriptTable):
    pass

class ParticleSystemElementData(UiElementData, BaseElementData):
    TextureOverrides: (Map, Hash, String, 0x0)
    mRenderAtElementLayer: (Bool, 0x0, 0x0, 0x0)
    mVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    PlayDuringTransition: (Bool, 0x0, 0x0, 0x0)
    VfxAdjustmentScale: (F32, 0x0, 0x0, 0x0)
    mUseUserScale: (Bool, 0x0, 0x0, 0x0)
    mMaxPlayCount: (U32, 0x0, 0x0, 0x0)
    pass

class 0xdd8ea5ae():
    TopBarIcon: (Hash, 0x0, 0x0, 0x0)
    0x550cba72: (Hash, 0x0, 0x0, 0x0)
    0x720b91e8: (Hash, 0x0, 0x0, 0x0)
    MissionCompleteText: (Hash, 0x0, 0x0, 0x0)
    0x88131f9a: (Embed, 0x0, 0x0, 0x4fbb3f5d)
    TimeRemainingText: (Hash, 0x0, 0x0, 0x0)
    0xe2f95b32: (Hash, 0x0, 0x0, 0x0)
    pass

class SpellRankIntDriver(ILogicIntDriver):
    SpellSlot: (U32, 0x0, 0x0, 0x0)
    pass

class PerkSlot():
    mPerks: (List, 0x0, Link, Perk)
    mType: (U32, 0x0, 0x0, 0x0)
    mSlotLabelKey: (String, 0x0, 0x0, 0x0)
    pass

class TroveInstanceData(InstanceDataBase):
    BannerData: (Hash, 0x0, 0x0, 0x0)
    0xbaca3b7b: (Bool, 0x0, 0x0, 0x0)
    ForegroundVfx: (Embed, 0x0, 0x0, TextureOverride)
    0xd407c07d: (Embed, 0x0, 0x0, TextureOverride)
    BackgroundVfx: (Embed, 0x0, 0x0, TextureOverride)
    pass

class ChallengeCompletionLevel():
    mThreshold: (I64, 0x0, 0x0, 0x0)
    mDescriptionTraKey: (String, 0x0, 0x0, 0x0)
    mNameTraKey: (String, 0x0, 0x0, 0x0)
    pass

class ScriptBtSelector(IScriptBt, IScriptSequence):
    Blocks: (List2, 0x0, Pointer, IScriptBlock)
    Blocks: (List2, 0x0, Pointer, IBehaviorScriptBlock)
    pass

class PostGameViewController(ViewController):
    CurrentExpText: (Hash, 0x0, 0x0, 0x0)
    ModeText: (Hash, 0x0, 0x0, 0x0)
    GainedRatingText: (Hash, 0x0, 0x0, 0x0)
    RankIconData: (List, 0x0, Embed, NamedIconData)
    Scene: (Hash, 0x0, 0x0, 0x0)
    GainedExpText: (Hash, 0x0, 0x0, 0x0)
    RankIcons: (Map, U32, Hash, 0x0)
    RatedIconData: (List, 0x0, Embed, NamedIconData)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    PlayerTemplate: (Embed, 0x0, 0x0, PostGamePlayerTemplate)
    PlayAgainButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    PlacementTextRight: (Hash, 0x0, 0x0, 0x0)
    QuitButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    DemotionProtectionText: (Hash, 0x0, 0x0, 0x0)
    PlayAgainButton: (Hash, 0x0, 0x0, 0x0)
    Labs: (Map, U32, Embed, PostGameLabFields)
    PlayerFields: (Embed, 0x0, 0x0, PlayerFields)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    0x71309e56: (I32, 0x0, 0x0, 0x0)
    CurrentPlayerHighlight: (Hash, 0x0, 0x0, 0x0)
    WinStreakVfx: (Hash, 0x0, 0x0, 0x0)
    PlayerSlots: (List, 0x8, Hash, 0x0)
    LostExpText: (Hash, 0x0, 0x0, 0x0)
    LostRatingText: (Hash, 0x0, 0x0, 0x0)
    RatedTierText: (Hash, 0x0, 0x0, 0x0)
    RatedIconVfx: (Hash, 0x0, 0x0, 0x0)
    PartnerGroupPlacements: (Pointer, 0x0, 0x0, PartnerGroupPlacements)
    UnitTemplate: (Embed, 0x0, 0x0, PostGameUnitTemplate)
    RankText: (Hash, 0x0, 0x0, 0x0)
    QuitButton: (Hash, 0x0, 0x0, 0x0)
    ProvisionalTextRight: (Hash, 0x0, 0x0, 0x0)
    UnitFields: (Embed, 0x0, 0x0, UnitFields)
    RatedTierLocKeys: (Map, String, String, 0x0)
    PlayerPlacementBanners: (List, 0x8, Hash, 0x0)
    RatedIconLoadingVfx: (Hash, 0x0, 0x0, 0x0)
    PlacementBanners: (List, 0x4, Hash, 0x0)
    CurrentRatingText: (Hash, 0x0, 0x0, 0x0)
    WinstreakText: (Hash, 0x0, 0x0, 0x0)
    BackgroundTexture: (Hash, 0x0, 0x0, 0x0)
    SceneDivider: (Hash, 0x0, 0x0, 0x0)
    pass

class MapContainer():
    Components: (List, 0x0, Pointer, MapComponent)
    Items: (Map, Hash, Pointer, MapPlaceable)
    Chunks: (Map, Hash, Link, MapPlaceableContainer)
    BoundsMin: (Vec2, 0x0, 0x0, 0x0)
    BoundsMax: (Vec2, 0x0, 0x0, 0x0)
    MapPath: (String, 0x0, 0x0, 0x0)
    ConvertStreamsToHalfFloat: (Bool, 0x0, 0x0, 0x0)
    LowestWalkableHeight: (F32, 0x0, 0x0, 0x0)
    MeshCombineRadius: (F32, 0x0, 0x0, 0x0)
    pass

class ICharacterSubcondition():
    pass

class TftAttachmentSlotStyleData():
    mName: (String, 0x0, 0x0, 0x0)
    mOverlayIconPath: (String, 0x0, 0x0, 0x0)
    mSubtextTra: (String, 0x0, 0x0, 0x0)
    pass

class IsInGrassDynamicMaterialBoolDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    pass

class SkinBorderOrder():
    Layer: (U8, 0x0, 0x0, 0x0)
    SkinId: (I32, 0x0, 0x0, 0x0)
    Priority: (U8, 0x0, 0x0, 0x0)
    pass

class TftTrovesCelebrationViewController(ViewController):
    0x104fe04e: (Link, 0x0, 0x0, SequenceObjectSelector)
    0x183c04eb: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    DefaultStandardItemRarityTexturePath: (String, 0x0, 0x0, 0x0)
    StandardItemStarLevelTexturePaths: (List, 0x3, String, 0x0)
    0x2726ce1f: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    0x27edf69a: (List2, 0x0, Link, SequenceObjectSelector)
    0x2e05d5a9: (Link, 0x0, 0x0, SequenceObjectSelector)
    DefaultStandardItemThumbnailTexturePath: (String, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    0x58134905: (Link, 0x0, 0x0, SequenceObjectSelector)
    0x629d7fe5: (Link, 0x0, 0x0, SequenceObjectSelector)
    DefaultTheme: (Link, 0x0, 0x0, TftTrovesCelebrationThemeData)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    SingleStandardItemLegendaryVfx: (Hash, 0x0, 0x0, 0x0)
    SingleStandardItemVfx: (Hash, 0x0, 0x0, 0x0)
    StandardItemRarityTexturePaths: (Map, U32, String, 0x0)
    0x7e6bb126: (Link, 0x0, 0x0, SequenceObjectSelector)
    StandardContentLayout: (Hash, 0x0, 0x0, 0x0)
    0x880040f3: (Link, 0x0, 0x0, SequenceObjectSelector)
    VignetteTitle: (Hash, 0x0, 0x0, 0x0)
    0x8a6d374d: (Link, 0x0, 0x0, SequenceObjectSelector)
    0x8bbe1dcd: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    ContinueButton: (Hash, 0x0, 0x0, 0x0)
    0x96de2eba: (Link, 0x0, 0x0, SequenceObjectSelector)
    StandardItemTemplate: (Embed, 0x0, 0x0, MultiPullStandardItemData)
    0xa3021f81: (Link, 0x0, 0x0, SequenceObjectSelector)
    0xa7b45c64: (Link, 0x0, 0x0, SequenceObjectSelector)
    0xaad46f66: (Hash, 0x0, 0x0, 0x0)
    0xabdd4859: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    CommonScene: (Hash, 0x0, 0x0, 0x0)
    DefaultStandardItemStarLevelTexturePath: (String, 0x0, 0x0, 0x0)
    0xc1d80535: (Link, 0x0, 0x0, SequenceObjectSelector)
    0xd7ce36cb: (Link, 0x0, 0x0, SequenceObjectSelector)
    ParentScene: (Hash, 0x0, 0x0, 0x0)
    0xeed1cb06: (Link, 0x0, 0x0, SequenceObjectSelector)
    UseSequencer: (Bool, 0x0, 0x0, 0x0)
    SingleStandardItemText: (Hash, 0x0, 0x0, 0x0)
    0xf9ae2168: (Link, 0x0, 0x0, SequenceObjectSelector)
    VignetteTitleTraKey: (String, 0x0, 0x0, 0x0)
    pass

class TftPassRewardEntitlement(TftPassRewardBase):
    ItemId: (String, 0x0, 0x0, 0x0)
    Type: (String, 0x0, 0x0, 0x0)
    TypeId: (String, 0x0, 0x0, 0x0)
    ItemTypeId: (String, 0x0, 0x0, 0x0)
    pass

class StaticMaterialShaderParamDef():
    Value: (Vec4, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class LuaPropertyDataGlobalRef(LuaPropertyData):
    Globalslink: (Link, 0x0, 0x0, LuaPropertyDataGlobals)
    LookupKey: (Hash, 0x0, 0x0, 0x0)
    Coefficient: (F32, 0x0, 0x0, 0x0)
    pass

class ContextualConditionTeammateDeathsNearby(IContextualCondition, ICharacterSubcondition):
    mTeammateDeaths: (U32, 0x0, 0x0, 0x0)
    pass

class AnnouncementStyleBasic():
    TextField: (Hash, 0x0, 0x0, 0x0)
    DurationWithoutSound: (F32, 0x0, 0x0, 0x0)
    OnShowTransitionData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    FadeInData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    MinAnnouncementDuration: (F32, 0x0, 0x0, 0x0)
    OnHideTransitionData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    FadeOutData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    pass

class 0xde69c8a4():
    mEventToTrack: (U32, 0x0, 0x0, 0x0)
    pass

class MinimapIconTextureData():
    mBase: (String, 0x0, 0x0, 0x0)
    mColorblind: (Option, 0x0, String, 0x0)
    pass

class TftUnitInfoViewController(ViewController):
    0x16a05d07: (List2, 0x0, Hash, 0x0)
    ItemCodexUpperRightAnchor: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    UnitPortrait: (Hash, 0x0, 0x0, 0x0)
    PositioningIcon: (Hash, 0x0, 0x0, 0x0)
    Region: (Hash, 0x0, 0x0, 0x0)
    ChampInspectVfx: (Hash, 0x0, 0x0, 0x0)
    ChampInspectVfx: (String, 0x0, 0x0, 0x0)
    ParBarData: (Embed, 0x0, 0x0, AbilityResourceBarData)
    Items: (List, 0x3, Embed, TftUnitInfoItemDisplayData)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    0x40c4c900: (List, 0x3, Hash, 0x0)
    UnitName: (Hash, 0x0, 0x0, 0x0)
    StatTooltipUpperRightAnchor: (Hash, 0x0, 0x0, 0x0)
    SellUnitButtonTextTra: (String, 0x0, 0x0, 0x0)
    RangeButton: (Hash, 0x0, 0x0, 0x0)
    0x517ee83f: (List2, 0x0, Embed, 0x629f5938)
    HealthBarData: (Embed, 0x0, 0x0, HealthBarData)
    RangeTextTra: (String, 0x0, 0x0, 0x0)
    AbilityTooltipUpperRightAnchor: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    AbilityIcon: (Hash, 0x0, 0x0, 0x0)
    SellUnitButtonGoldText: (Hash, 0x0, 0x0, 0x0)
    TraitInfoCardHoverRegion: (Hash, 0x0, 0x0, 0x0)
    RangeHexVfx: (Hash, 0x0, 0x0, 0x0)
    ItemsOnlyRegion: (Hash, 0x0, 0x0, 0x0)
    PositioningButton: (Hash, 0x0, 0x0, 0x0)
    ItemHighlights: (List, 0x3, Hash, 0x0)
    PositioningText: (Hash, 0x0, 0x0, 0x0)
    Traits: (List, 0x3, Embed, TftUnitInfoTraitDisplayData)
    SellUnitButtonText: (Hash, 0x0, 0x0, 0x0)
    RangeText: (Hash, 0x0, 0x0, 0x0)
    ItemButtonHighlights: (List, 0x3, Hash, 0x0)
    SellUnitButton: (Hash, 0x0, 0x0, 0x0)
    PositioningHexVfx: (Hash, 0x0, 0x0, 0x0)
    GoldIcon: (Hash, 0x0, 0x0, 0x0)
    ChosenBadge: (Hash, 0x0, 0x0, 0x0)
    StarLevelOverlays: (List, 0x4, Hash, 0x0)
    TooltipRegion: (Hash, 0x0, 0x0, 0x0)
    CharacterRoleData: (Embed, 0x0, 0x0, TftUnitInfoCharacterRoleData)
    CharacterRoleData: (List, 0x1, Embed, TftUnitInfoCharacterRoleData)
    CharacterRoleData: (List, 0x2, Embed, TftUnitInfoCharacterRoleData)
    CustomButtonData: (Embed, 0x0, 0x0, TftUnitInfoCustomButtonData)
    PositioningData: (Map, U8, Embed, TftCharacterPositioningData)
    AbilityName: (Hash, 0x0, 0x0, 0x0)
    TraitInfoCardRegion: (Hash, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    ItemTooltipUpperRightAnchor: (Hash, 0x0, 0x0, 0x0)
    AbilityButton: (Hash, 0x0, 0x0, 0x0)
    RarityUnderlays: (List, 0x6, Hash, 0x0)
    RarityUnderlays: (List, 0x8, Hash, 0x0)
    RarityUnderlays: (List, 0x9, Hash, 0x0)
    ItemsOnlyScene: (Hash, 0x0, 0x0, 0x0)
    0xeeea5fa1: (Hash, 0x0, 0x0, 0x0)
    GoldText: (Hash, 0x0, 0x0, 0x0)
    StatsUiData: (Embed, 0x0, 0x0, UnitStatsUiData)
    pass

class 0xde86026a(SelectSpellBlock):
    pass

class UiElementEffectCircleMaskDesaturateData(UiElementEffectDesaturateData):
    pass

class 0xdec5122e():
    Comp: (Embed, 0x0, 0x0, 0xc90736f4)
    pass

class ViewControllerFilter_Or(ViewControllerFilterI):
    FilterList: (List2, 0x0, Pointer, ViewControllerFilterI)
    Filters: (List, 0x0, Pointer, ViewControllerFilterI)
    Filters: (List2, 0x0, Pointer, ViewControllerFilterI)
    pass

class HeroFloatingInfoResistBorderData():
    ArmorThresholds: (List, 0x3, F32, 0x0)
    ArmorBorders: (List, 0x3, Embed, HeroFloatingInfoBorderTypeData)
    MagicResistBorders: (List, 0x3, Embed, HeroFloatingInfoBorderTypeData)
    MagicResistThresholds: (List, 0x3, F32, 0x0)
    ComboBorders: (List, 0x3, Embed, HeroFloatingInfoBorderTypeData)
    pass

class ContextualConditionCharacterName(ICharacterSubcondition):
    mNames: (List, 0x0, String, 0x0)
    mCharacters: (List, 0x0, Hash, 0x0)
    pass

class DamageTypeMeterData():
    MeterElements: (List, 0x3, Hash, 0x0)
    pass

class UiTeamFightTeamHealthMeterData():
    OnscreenHealthFill: (Hash, 0x0, 0x0, 0x0)
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    TotalHealthFill: (Hash, 0x0, 0x0, 0x0)
    pass

class AnchorDouble(AnchorBase):
    AnchorLeft: (Vec2, 0x0, 0x0, 0x0)
    AnchorRight: (Vec2, 0x0, 0x0, 0x0)
    pass

class UiElementGroupSliderState():
    BarBackdrop: (Link, 0x0, 0x0, UiElementIconData)
    BarBackdrop: (Link, 0x0, 0x0, IconElementData)
    BarFill: (Link, 0x0, 0x0, UiElementIconData)
    BarFill: (Link, 0x0, 0x0, IconElementData)
    SliderIcon: (Link, 0x0, 0x0, UiElementIconData)
    SliderIcon: (Link, 0x0, 0x0, IconElementData)
    pass

class IsSpecifiedUnitCastRequirement(ICastRequirement):
    mUnit: (Hash, 0x0, 0x0, 0x0)
    pass

class LoadingScreenSettings():
    MaxSize: (F32, 0x0, 0x0, 0x0)
    SpeedDegrees: (F32, 0x0, 0x0, 0x0)
    TexV: (F32, 0x0, 0x0, 0x0)
    TexU: (F32, 0x0, 0x0, 0x0)
    TexSize: (F32, 0x0, 0x0, 0x0)
    Margin: (F32, 0x0, 0x0, 0x0)
    pass

class 0xdf694fb2():
    0x9d6e31fd: (Hash, 0x0, 0x0, 0x0)
    0xc742ceb4: (Hash, 0x0, 0x0, 0x0)
    BottomHrMomentumPost: (List2, 0x0, Hash, 0x0)
    pass

class ToggleInvulnerableCheat(Cheat):
    mTarget: (U32, 0x0, 0x0, 0x0)
    pass

class Direction(TargetingTypeData):
    pass

class SequenceLocationObject(ISequenceLocation):
    Object: (Embed, 0x0, 0x0, SequenceObjectSelector)
    Object: (Link, 0x0, 0x0, SequenceObjectSelector)
    pass

class LoadingScreenChallengeTokenData():
    ChallengeTokenGroup: (Hash, 0x0, 0x0, 0x0)
    ChallengeTokenCapstoneIcon: (Hash, 0x0, 0x0, 0x0)
    ChallengeTokenHitRegion: (Hash, 0x0, 0x0, 0x0)
    ChallengeTokenIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class MapThemeMusic(MapComponent):
    ThemeMusicTransitionEvent: (String, 0x0, 0x0, 0x0)
    EnterBoardEvent: (String, 0x0, 0x0, 0x0)
    LocalThemeMusic: (String, 0x0, 0x0, 0x0)
    ExitBoardEvent: (String, 0x0, 0x0, 0x0)
    pass

class ReplayTeamFramesViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    ChaosTeamData: (Embed, 0x0, 0x0, UiReplayTeamFramesData)
    OrderTeamData: (Embed, 0x0, 0x0, UiReplayTeamFramesData)
    pass

class Map(WadFileDescriptor):
    SharedCharacterLists: (List2, 0x0, Link, MapCharacterListContainer)
    AudioBankUnits: (List, 0x0, Embed, BankUnit)
    MapSkins: (List2, 0x0, Link, MapSkin)
    0x30eafcaa: (U8, 0x0, 0x0, 0x0)
    0x31af8e97: (Map, Hash, Link, 0xb26bd951)
    AdditionalRoots: (List, 0x0, String, 0x0)
    InitialVisibilityMask: (U8, 0x0, 0x0, 0x0)
    NavigationGridOverlays: (Embed, 0x0, 0x0, MapNavigationGridOverlays)
    RequiredLocations: (Map, Hash, Link, MapPlaceableContainer)
    CharacterLists: (List, 0x0, Link, MapCharacterList)
    CharacterLists: (List2, 0x0, Link, MapCharacterList)
    FogOfWarProperties: (Link, 0x0, 0x0, FogOfWarProperties)
    AiUnits: (Map, Hash, Link, AiUnitGroup)
    VisibilityFlagDefines: (Embed, 0x0, 0x0, MapVisibilityFlagDefinitions)
    Locations: (List, 0x0, Embed, MapPlaceableLinkGroup)
    MapStringId: (String, 0x0, 0x0, 0x0)
    0xd31ac6ce: (Embed, 0x0, 0x0, MapVisibilityFlagDefinitions)
    BasedOnMap: (Link, 0x0, 0x0, Map)
    GameModeCharacterLists: (List, 0x0, Embed, GameModeCharacterList)
    pass

class HudHealthBarBurstData():
    BurstTriggerPercent: (F32, 0x0, 0x0, 0x0)
    FadeAcceleration: (F32, 0x0, 0x0, 0x0)
    FlashTriggerPercent: (F32, 0x0, 0x0, 0x0)
    FadeHoldTime: (F32, 0x0, 0x0, 0x0)
    FlashDuration: (F32, 0x0, 0x0, 0x0)
    ShakeTriggerPercent: (F32, 0x0, 0x0, 0x0)
    BurstTimeWindow: (F32, 0x0, 0x0, 0x0)
    ShakeDuration: (F32, 0x0, 0x0, 0x0)
    MinPercentDamageToResetHold: (F32, 0x0, 0x0, 0x0)
    ShakeFrequency: (F32, 0x0, 0x0, 0x0)
    ShakeBox: (Vec2, 0x0, 0x0, 0x0)
    ShakeReferenceResolution: (Vec2, 0x0, 0x0, 0x0)
    MaximumHoldTime: (F32, 0x0, 0x0, 0x0)
    FadeSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class CameraConfig():
    mDragMomentumDecay: (F32, 0x0, 0x0, 0x0)
    HighHeight: (F32, 0x0, 0x0, 0x0)
    mElasticLockAcceleration: (F32, 0x0, 0x0, 0x0)
    GetPocClampBufferTrapezoid: (Embed, 0x0, 0x0, CameraTrapezoid)
    0x4ffc6f01: (F32, 0x0, 0x0, 0x0)
    mDragScale: (F32, 0x0, 0x0, 0x0)
    mSemiLockTrapezoid: (Embed, 0x0, 0x0, CameraTrapezoid)
    mElasticClampTrapezoid: (Embed, 0x0, 0x0, CameraTrapezoid)
    mTopdownZoom: (F32, 0x0, 0x0, 0x0)
    mDragMomentumRecencyWeight: (F32, 0x0, 0x0, 0x0)
    GetPocLockAcceleration: (F32, 0x0, 0x0, 0x0)
    mLockedCameraEasingDistance: (F32, 0x0, 0x0, 0x0)
    GetPocClampTrapezoid: (Embed, 0x0, 0x0, CameraTrapezoid)
    mZoomMinSpeed: (F32, 0x0, 0x0, 0x0)
    mPositionSemiLockMaxZDown: (F32, 0x0, 0x0, 0x0)
    mPositionSemiLockMaxZUp: (F32, 0x0, 0x0, 0x0)
    mPositionSemiLockMaxXBottom: (F32, 0x0, 0x0, 0x0)
    mPositionSemiLockMaxXTop: (F32, 0x0, 0x0, 0x0)
    mTransitionDurationIntoCinematicMode: (F32, 0x0, 0x0, 0x0)
    mZoomEaseTime: (F32, 0x0, 0x0, 0x0)
    mDecelerationTimeMouse: (F32, 0x0, 0x0, 0x0)
    mAccelerationTimeMouse: (F32, 0x0, 0x0, 0x0)
    mDecelerationTimeKeyboard: (F32, 0x0, 0x0, 0x0)
    mZoomMaxDistance: (F32, 0x0, 0x0, 0x0)
    mElasticDeadZoneTrapezoid: (Embed, 0x0, 0x0, CameraTrapezoid)
    MediumHeight: (F32, 0x0, 0x0, 0x0)
    mAccelerationTimeKeyboard: (F32, 0x0, 0x0, 0x0)
    mZoomMinDistance: (F32, 0x0, 0x0, 0x0)
    pass

class TftTeamPlannerMemberDisplayTrait():
    Styles: (Map, U32, Embed, TftTeamPlannerMemberTraitData)
    pass

class TftTraitContributionData():
    TraitData: (Link, 0x0, 0x0, TftTraitData)
    mShowInTraitTooltip: (Bool, 0x0, 0x0, 0x0)
    ShowTraitNub: (Bool, 0x0, 0x0, 0x0)
    Amount: (I32, 0x0, 0x0, 0x0)
    pass

class StateAnimTransitionData():
    TransitionDelaySwitchTime: (F32, 0x0, 0x0, 0x0)
    PlayAnimChangeFromBeginning: (Bool, 0x0, 0x0, 0x0)
    PauseOnEnd: (Bool, 0x0, 0x0, 0x0)
    CanTransitionMidPlay: (Bool, 0x0, 0x0, 0x0)
    DontStompTransitionClip: (Bool, 0x0, 0x0, 0x0)
    SyncFrameOnChangeAnim: (Bool, 0x0, 0x0, 0x0)
    Blend: (Bool, 0x0, 0x0, 0x0)
    TargetClipName: (Hash, 0x0, 0x0, 0x0)
    Condition: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    pass

class 0xe067bdf9(IScriptBlock, IBehaviorScriptBlock):
    pass

class MessageBoxDialog(ModalDialogViewController):
    HeaderTitleText: (Hash, 0x0, 0x0, 0x0)
    CancelButtonAdditionalIcons: (Embed, 0x0, 0x0, UiElementGroupButtonAdditionalElements)
    PlaceholderText: (Hash, 0x0, 0x0, 0x0)
    SoftKeyboardTransitionData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    InputScene: (Hash, 0x0, 0x0, 0x0)
    MainBodyText: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    ConfirmButtonIcons: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    InputText: (Hash, 0x0, 0x0, 0x0)
    HeaderBodyText: (Hash, 0x0, 0x0, 0x0)
    mSoftKeyboardTransitionData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    ConfirmButtonAdditionalIcons: (Embed, 0x0, 0x0, UiElementGroupButtonAdditionalElements)
    ButtonScene: (Hash, 0x0, 0x0, 0x0)
    InputErrorText: (Hash, 0x0, 0x0, 0x0)
    CancelButtonIcons: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xe07edfa4(IMapVisibilityController):
    DefaultVisible: (Bool, 0x0, 0x0, 0x0)
    Name: (Hash, 0x0, 0x0, 0x0)
    pass

class TakeCamp(JungleAction):
    Camp: (U8, 0x0, 0x0, 0x0)
    pass

class StateTransitionData():
    TransitionDelaySwitchTime: (F32, 0x0, 0x0, 0x0)
    PlayAnimChangeFromBeginning: (Bool, 0x0, 0x0, 0x0)
    Conditions: (List, 0x0, Embed, 0xb0e1e45e)
    Conditions: (List, 0x0, Pointer, 0xb0e1e45e)
    CanTransitionMidPlay: (Bool, 0x0, 0x0, 0x0)
    DontStompTransitionClip: (Bool, 0x0, 0x0, 0x0)
    SyncFrameOnChangeAnim: (Bool, 0x0, 0x0, 0x0)
    TargetClipName: (Hash, 0x0, 0x0, 0x0)
    pass

class BarExtensionTipStyle(TipStyleBase):
    pass

class HudTipTrackerMessageTemplate():
    ClickRegion: (Hash, 0x0, 0x0, 0x0)
    IconHover: (Hash, 0x0, 0x0, 0x0)
    SlotArea: (Hash, 0x0, 0x0, 0x0)
    TipBodyText: (Hash, 0x0, 0x0, 0x0)
    TipTitleText: (Hash, 0x0, 0x0, 0x0)
    BackgroundDefault: (Hash, 0x0, 0x0, 0x0)
    IconDefault: (Hash, 0x0, 0x0, 0x0)
    BackgroundHover: (Hash, 0x0, 0x0, 0x0)
    pass

class ColorGraphMaterialDriver(IDynamicMaterialDriver, ILogicDriver):
    Driver: (Pointer, 0x0, 0x0, IDynamicMaterialFloatDriver)
    Driver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    Colors: (Embed, 0x0, 0x0, VfxAnimatedColorVariableData)
    pass

class UiPropertyLoadable(PropertyLoadable):
    pass

class PauseDialogViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    Text: (Hash, 0x0, 0x0, 0x0)
    Meter: (Hash, 0x0, 0x0, 0x0)
    pass

class TftCharacterRoleCardHeaderData():
    Description: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    Title: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class AllItemsPage():
    mCategoryName: (String, 0x0, 0x0, 0x0)
    mPageName: (String, 0x0, 0x0, 0x0)
    mItemGrId: (Embed, 0x0, 0x0, ItemGrid)
    pass

class ParametricMovementType_AngleFromTarget(ParametricMovementType):
    pass

class MapNavGridOverlay():
    Name: (Hash, 0x0, 0x0, 0x0)
    NavGridFileName: (String, 0x0, 0x0, 0x0)
    RegionsFilename: (String, 0x0, 0x0, 0x0)
    pass

class UiChampionSelectionSlotData():
    Portrait: (Hash, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    ExButton: (Hash, 0x0, 0x0, 0x0)
    pass

class TftBaseTraitSetData():
    TargetUnitsToBuff: (Option, 0x0, U32, 0x0)
    ActivatedBuffName: (String, 0x0, 0x0, 0x0)
    TargetStrategy: (U8, 0x0, 0x0, 0x0)
    TeamToBuff: (U8, 0x0, 0x0, 0x0)
    0x86b5abcb: (List2, 0x0, Embed, 0x76621fa6)
    BuffName: (String, 0x0, 0x0, 0x0)
    EffectAmounts: (List, 0x0, Embed, TftEffectAmount)
    pass

class 0xe1555e0a():
    AugmentGroup: (List2, 0x0, Link, BasicSkinAugment)
    pass

class HudTeamFightData():
    mStyleFlags: (U32, 0x0, 0x0, 0x0)
    mSceneTransition: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mOffscreenDifferentiation: (Pointer, 0x0, 0x0, HudTeamFightOffScreenDifferentiationData)
    pass

class TftSoulFighterTournamentBracketsViewController(ViewController):
    0x17baadb7: (Hash, 0x0, 0x0, 0x0)
    Duration: (F32, 0x0, 0x0, 0x0)
    StageConfigs: (List, 0x0, Embed, 0x1181085f)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    0x5d768e72: (Hash, 0x0, 0x0, 0x0)
    Title: (Hash, 0x0, 0x0, 0x0)
    0xa9affd87: (Hash, 0x0, 0x0, 0x0)
    pass

class MapActionToggleMapThemeMusic(MapAction):
    pass

class 0xe1c21adb(ModalDialogViewController):
    0x2bea4c1a: (String, 0x0, 0x0, 0x0)
    0x389ed80b: (String, 0x0, 0x0, 0x0)
    0x4d69a446: (Hash, 0x0, 0x0, 0x0)
    0x6c8d3317: (String, 0x0, 0x0, 0x0)
    0xa621a3c: (Hash, 0x0, 0x0, 0x0)
    0xb121269e: (String, 0x0, 0x0, 0x0)
    BodyText: (Hash, 0x0, 0x0, 0x0)
    0xd578ba42: (String, 0x0, 0x0, 0x0)
    0xed13979f: (Embed, 0x0, 0x0, UiHyperlink)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    0xfba456c3: (String, 0x0, 0x0, 0x0)
    pass

class HealthbarStyleTemplate():
    ColorblindPalette: (Link, 0x0, 0x0, BaseHealthbarData)
    InvulnColorblindPalette: (Link, 0x0, 0x0, BaseHealthbarData)
    DefaultPalette: (Link, 0x0, 0x0, BaseHealthbarData)
    InvulnDefaultPalette: (Link, 0x0, 0x0, BaseHealthbarData)
    pass

class BinFileContainer(PropertyLoadable):
    pass

class CherryAugmentSelectionViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    AugmentSelectionGrid: (Hash, 0x0, 0x0, 0x0)
    0x56592fa3: (U32, 0x0, 0x0, 0x0)
    TimeoutPreventClicksOnShow: (F32, 0x0, 0x0, 0x0)
    0x6da1a863: (Embed, 0x0, 0x0, 0xfb1989a3)
    RerollButtonData: (Embed, 0x0, 0x0, RerollButtonData)
    MaxAugmentSlots: (U32, 0x0, 0x0, 0x0)
    0xce64b8ab: (Embed, 0x0, 0x0, 0xfb1989a3)
    AugmentSlotData: (Embed, 0x0, 0x0, AugmentSlotData)
    0xf8d5ccda: (Embed, 0x0, 0x0, 0xfb1989a3)
    pass

class MaterialTextureData():
    AddressV: (U8, 0x0, 0x0, 0x0)
    AddressU: (U8, 0x0, 0x0, 0x0)
    FilterMin: (U8, 0x0, 0x0, 0x0)
    FilterMip: (U8, 0x0, 0x0, 0x0)
    DefaultTexturePath: (String, 0x0, 0x0, 0x0)
    FilterMag: (U8, 0x0, 0x0, 0x0)
    AddressW: (U8, 0x0, 0x0, 0x0)
    pass

class RichBackgroundViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    Background: (Embed, 0x0, 0x0, RichBackgroundGameModeBackground)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    pass

class TftStageViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    CollapseButton: (Hash, 0x0, 0x0, 0x0)
    TimerFillTexture: (Hash, 0x0, 0x0, 0x0)
    OvertimeBackgroundTopRight: (Hash, 0x0, 0x0, 0x0)
    BackgroundTopCenter: (Hash, 0x0, 0x0, 0x0)
    TimingOutBackgroundTopRight: (Hash, 0x0, 0x0, 0x0)
    StageRightGroup: (Hash, 0x0, 0x0, 0x0)
    CollapseIcon: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    StageLeftGroup: (Hash, 0x0, 0x0, 0x0)
    CollapsedStageScene: (Embed, 0x0, 0x0, TftStageSceneData)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    Timer: (Hash, 0x0, 0x0, 0x0)
    TimerBarBackground: (Hash, 0x0, 0x0, 0x0)
    ExpandIcon: (Hash, 0x0, 0x0, 0x0)
    GameModeIcon: (Hash, 0x0, 0x0, 0x0)
    PhaseIcons: (List, 0x5, Hash, 0x0)
    StageNumber: (Hash, 0x0, 0x0, 0x0)
    ExpandButton: (Hash, 0x0, 0x0, 0x0)
    PlanningPhaseTimeOutSecs: (F32, 0x0, 0x0, 0x0)
    BackgroundTopRight: (Hash, 0x0, 0x0, 0x0)
    ExpandedStageScene: (Embed, 0x0, 0x0, TftStageSceneData)
    RoundTemplate: (Embed, 0x0, 0x0, TftStageRoundDataTemplate)
    StageIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xe20ffd3f(IFxAction):
    Size: (I32, 0x0, 0x0, 0x0)
    Target: (Embed, 0x0, 0x0, FxObjectSelector)
    Color: (Color, 0x0, 0x0, 0x0)
    pass

class ChildMapVisibilityController(IMapVisibilityController):
    Parents: (List2, 0x0, Link, IMapVisibilityController)
    ParentMode: (U32, 0x0, 0x0, 0x0)
    pass

class StaticMaterialSwitchDef():
    On: (Bool, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class TargeterDefinitionAoe(TargeterDefinition):
    TextureOrientation: (U32, 0x0, 0x0, 0x0)
    MaxRangeSizeScalar: (Embed, 0x0, 0x0, TargeterDefinitionAoeScalar)
    TextureRadiusOverrideName: (String, 0x0, 0x0, 0x0)
    ConstraintRange: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    ConstraintRange: (F32, 0x0, 0x0, 0x0)
    IsConstrainedToRange: (Bool, 0x0, 0x0, 0x0)
    DynamicGameCalcSizeScalar: (Pointer, 0x0, 0x0, IGameCalculation)
    ConstraintPosLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    OverrideRadius: (Embed, 0x0, 0x0, FloatPerSpellLevel)
    CenterLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    pass

class IGameModeConfig(IGameModeConfigBase):
    pass

class LoadingScreenLatencyThreshold():
    Threshold: (U32, 0x0, 0x0, 0x0)
    TextColor: (Color, 0x0, 0x0, 0x0)
    Image: (Hash, 0x0, 0x0, 0x0)
    pass

class AiHeroClient(AiHero):
    pass

class UiComboBoxSoundEvents():
    OnSelectionEvent: (String, 0x0, 0x0, 0x0)
    pass

class ItemRecommendationNode():
    mItem: (Hash, 0x0, 0x0, 0x0)
    mAltRecommendations: (List, 0x0, Embed, ItemRecommendationNode)
    mRecommendations: (List, 0x0, Embed, ItemRecommendationNode)
    pass

class VfxPrimitiveBase():
    pass

class TftTrovesCelebrationHighlightSegmentData():
    Sequence: (Link, 0x0, 0x0, Sequence)
    HighlightEndVfx: (Hash, 0x0, 0x0, 0x0)
    0x65bf457: (String, 0x0, 0x0, 0x0)
    HighlightsSequence: (Link, 0x0, 0x0, Sequence)
    NoHighlightsSequence: (Link, 0x0, 0x0, Sequence)
    HighlightEndTimingOffset: (F32, 0x0, 0x0, 0x0)
    0xb6160f23: (F32, 0x0, 0x0, 0x0)
    HighlightContentTimingOffset: (F32, 0x0, 0x0, 0x0)
    0xfb0b5e13: (String, 0x0, 0x0, 0x0)
    ChaseContentVfx: (Hash, 0x0, 0x0, 0x0)
    pass

class ItemPurchaseModifier():
    mDeltaBuffCurrencyCostPercent: (F32, 0x0, 0x0, 0x0)
    mMaximumDeltasToStack: (I32, 0x0, 0x0, 0x0)
    mItemPurchaseModifierId: (Hash, 0x0, 0x0, 0x0)
    mDeltaRequiredLevel: (I32, 0x0, 0x0, 0x0)
    mModifiedIfBuildsFromItem: (Link, 0x0, 0x0, ItemData)
    mModifiedGroup: (Link, 0x0, 0x0, ItemGroup)
    mAddedBuildFrom: (List, 0x0, Link, ItemData)
    mIgnoreMaxGroupOwnable: (Bool, 0x0, 0x0, 0x0)
    mRemovedBuildFrom: (List, 0x0, Link, ItemData)
    mModifiedItem: (Link, 0x0, 0x0, ItemData)
    mReplaceInsteadOfAddingBuildFrom: (Bool, 0x0, 0x0, 0x0)
    mModifierIsInheritedByOwnedParentItems: (Bool, 0x0, 0x0, 0x0)
    mDeltaGoldCost: (F32, 0x0, 0x0, 0x0)
    mMinimumModifierInstancesToBeActive: (I32, 0x0, 0x0, 0x0)
    mDeltaGoldCostPercent: (F32, 0x0, 0x0, 0x0)
    mDeltaMaxStacks: (I32, 0x0, 0x0, 0x0)
    mShowAsModifiedInUi: (Bool, 0x0, 0x0, 0x0)
    mMaximumModifierInstancesToBeActive: (I32, 0x0, 0x0, 0x0)
    mDeltaBuffCurrencyCost: (I32, 0x0, 0x0, 0x0)
    pass

class CollectiblesEsportsTeamData():
    LeagueName: (String, 0x0, 0x0, 0x0)
    TeamId: (U32, 0x0, 0x0, 0x0)
    ShortName: (String, 0x0, 0x0, 0x0)
    FullName: (String, 0x0, 0x0, 0x0)
    pass

class 0xe2ff8b22():
    GeneralCondition: (Pointer, 0x0, 0x0, 0x487b1677)
    0x6c8f6dcf: (List2, 0x0, Pointer, 0x304e703f)
    CompleteRewardList: (List2, 0x0, Pointer, 0x304e703f)
    0x7829e090: (List2, 0x0, Pointer, 0x304e703f)
    QuestName: (String, 0x0, 0x0, 0x0)
    IsEnabled: (Bool, 0x0, 0x0, 0x0)
    pass

class GameFontDescription():
    ResolutionData: (Link, 0x0, 0x0, FontResolutionData)
    OutlineColor: (Color, 0x0, 0x0, 0x0)
    GlowColor: (Color, 0x0, 0x0, 0x0)
    ColorblindGlowColor: (Option, 0x0, Color, 0x0)
    SelectionBoxColor: (Color, 0x0, 0x0, 0x0)
    Color: (Color, 0x0, 0x0, 0x0)
    ShadowColor: (Color, 0x0, 0x0, 0x0)
    ColorblindData: (Embed, 0x0, 0x0, FontColors)
    TypeData: (Link, 0x0, 0x0, FontType)
    ColorblindOutlineColor: (Option, 0x0, Color, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    FillTextureName: (String, 0x0, 0x0, 0x0)
    ColorblindShadowColor: (Option, 0x0, Color, 0x0)
    ColorData: (Embed, 0x0, 0x0, FontColors)
    ColorblindSelectionBoxColor: (Option, 0x0, Color, 0x0)
    HasColorblindData: (Bool, 0x0, 0x0, 0x0)
    ColorblindColor: (Option, 0x0, Color, 0x0)
    pass

class IVfxSpawnConditions():
    pass

class DestroyOnExitMap(MissileBehaviorSpec):
    pass

class UiElementParticleSystem(UiElement):
    pass

class LooseUiTextureData9Slice(LooseUiTextureDataBase, LooseUiTextureData):
    TopBottomHeights: (Vec2, 0x0, 0x0, 0x0)
    LeftRightWidths: (Vec2, 0x0, 0x0, 0x0)
    EdgeSizesLeftRight: (Vec2, 0x0, 0x0, 0x0)
    EdgeSizesTopBottom: (Vec2, 0x0, 0x0, 0x0)
    pass

class HudReplayEventTooltip():
    TimeTextHandle: (Hash, 0x0, 0x0, 0x0)
    ReplayEventLineBaseIcons: (Embed, 0x0, 0x0, HudReplayEventLineBaseIcons)
    EventBackdrop: (Hash, 0x0, 0x0, 0x0)
    TimeBackdropHandle: (Hash, 0x0, 0x0, 0x0)
    SceneHandle: (Hash, 0x0, 0x0, 0x0)
    pass

class LevelScriptBlock(IScriptBlock):
    pass

class MinimapPingTypeContainer():
    PingEffectList: (List, 0x0, Embed, MinimapPingEffectAndTextureData)
    pass

class Obj_SpawnPoint(BuildingClient):
    pass

class RegaliaRankedCrestEntry():
    Base: (Link, 0x0, 0x0, RegaliaData)
    SeasonSplitToCrestMap: (Map, I32, Link, RegaliaData)
    DivisionToCrestMap: (Map, I32, Link, RegaliaData)
    pass

class SwitchScriptBlock(IScriptBlock):
    Cases: (List, 0x0, Embed, SwitchCase)
    Cases: (List2, 0x0, Embed, SwitchCase)
    pass

class ContextualConditionItemVoGroup(IContextualCondition):
    mItemVoGroupHash: (Hash, 0x0, 0x0, 0x0)
    pass

class PathingAngleParametricUpdater(IFloatParametricUpdater):
    pass

class GameComponentData():
    pass

class VfxPrimitiveProjectionBase(VfxPrimitiveBase):
    mProjection: (Embed, 0x0, 0x0, VfxProjectionDefinitionData)
    pass

class TftShopContentData():
    TierBags: (List2, 0x0, Embed, 0x5f5925f1)
    pass

class HasBuffData():
    mBuffName: (String, 0x0, 0x0, 0x0)
    mFromAnyone: (Bool, 0x0, 0x0, 0x0)
    mFromOwner: (Bool, 0x0, 0x0, 0x0)
    mFromAttacker: (Bool, 0x0, 0x0, 0x0)
    pass

class TftCutsceneCamLerpClip(TftCutsceneClip):
    OverrideFov: (Bool, 0x0, 0x0, 0x0)
    AssociatedPlayer: (String, 0x0, 0x0, 0x0)
    BlackboardCameraBone: (String, 0x0, 0x0, 0x0)
    ViewType: (U32, 0x0, 0x0, 0x0)
    EasingType: (U8, 0x0, 0x0, 0x0)
    NearClipPlane: (F32, 0x0, 0x0, 0x0)
    BlackboardFovBone: (String, 0x0, 0x0, 0x0)
    FarClipPlane: (F32, 0x0, 0x0, 0x0)
    pass

class AbilityResourceStateColorOptions():
    Color: (Color, 0x0, 0x0, 0x0)
    FadeColor: (Color, 0x0, 0x0, 0x0)
    pass

class ISpellCalculationPart():
    pass

class UiElementEffectCooldownRadialData(UiElementEffectData):
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    mIsFill: (Bool, 0x0, 0x0, 0x0)
    TextureData: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mAtlas: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xe4f33df2(0x2515101c):
    NameTraKey: (String, 0x0, 0x0, 0x0)
    LoadoutsItem: (Link, 0x0, 0x0, BaseLoadoutData)
    pass

class ItemShopViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MinimumShopScale: (F32, 0x0, 0x0, 0x0)
    ResizeDragRegion: (Hash, 0x0, 0x0, 0x0)
    MaximumShopScale: (F32, 0x0, 0x0, 0x0)
    SceneHandle: (Hash, 0x0, 0x0, 0x0)
    DragRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class ClearTargetAndKeepMoving(MissileTriggeredActionSpec):
    mOverrideHeightAugment: (Option, 0x0, F32, 0x0)
    mOverrideRange: (Option, 0x0, F32, 0x0)
    LetServerDriveTargetPosition: (Bool, 0x0, 0x0, 0x0)
    mOverrideMovement: (Pointer, 0x0, 0x0, MissileMovementSpec)
    pass

class TftShopData():
    SquareSplashPath: (String, 0x0, 0x0, 0x0)
    mName: (String, 0x0, 0x0, 0x0)
    mRarity: (U8, 0x0, 0x0, 0x0)
    mMobileSmallIconPath: (String, 0x0, 0x0, 0x0)
    PcSplashPath: (String, 0x0, 0x0, 0x0)
    mMobileIconPath: (String, 0x0, 0x0, 0x0)
    mPortraitIconPath: (String, 0x0, 0x0, 0x0)
    mDisplayName: (String, 0x0, 0x0, 0x0)
    TeamPlannerSplashPath: (String, 0x0, 0x0, 0x0)
    mIcon: (String, 0x0, 0x0, 0x0)
    mAbilityNameTra: (String, 0x0, 0x0, 0x0)
    mIconPath: (String, 0x0, 0x0, 0x0)
    SellOverwriteTra: (String, 0x0, 0x0, 0x0)
    SellMobileOverwriteTra: (String, 0x0, 0x0, 0x0)
    BaseCurrency: (U8, 0x0, 0x0, 0x0)
    mDescriptionTra: (String, 0x0, 0x0, 0x0)
    mDisplayNameTra: (String, 0x0, 0x0, 0x0)
    TeamPlannerPortraitPath: (String, 0x0, 0x0, 0x0)
    AbilityIconPath: (String, 0x0, 0x0, 0x0)
    BaseCost: (I32, 0x0, 0x0, 0x0)
    mDescription: (String, 0x0, 0x0, 0x0)
    pass

class ItemDataBuild():
    ItemLinks: (List, 0x0, Link, ItemData)
    pass

class ChatChannelSelectionComboBoxDefinition():
    ComboBoxHeaderText: (Hash, 0x0, 0x0, 0x0)
    AllChatChannelTra: (String, 0x0, 0x0, 0x0)
    OptionReferenceRegion: (Hash, 0x0, 0x0, 0x0)
    ChatChannelOptionListHover: (Hash, 0x0, 0x0, 0x0)
    TeamChatChannelTra: (String, 0x0, 0x0, 0x0)
    ComboBoxHeaderButton: (Hash, 0x0, 0x0, 0x0)
    OptionReferenceText: (Hash, 0x0, 0x0, 0x0)
    ChatChannelOptionListBackdrop: (Hash, 0x0, 0x0, 0x0)
    PartyChatChannelTra: (String, 0x0, 0x0, 0x0)
    pass

class MapAlternateAsset():
    AudioBankUnits: (List2, 0x0, Embed, BankUnit)
    mNavmeshFxMaskName: (String, 0x0, 0x0, 0x0)
    mFowOverlayTextureName: (String, 0x0, 0x0, 0x0)
    mParticleResourceResolver: (Link, 0x0, 0x0, ResourceResolver)
    mVisibilityFlagName: (Hash, 0x0, 0x0, 0x0)
    mGrassTintTextureName: (String, 0x0, 0x0, 0x0)
    pass

class TftEncounterPanelViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    EncounterPanelScene: (Hash, 0x0, 0x0, 0x0)
    EncounterSlotTemplate: (Embed, 0x0, 0x0, TftEncounterSlotData)
    EncounterToggleButton: (Hash, 0x0, 0x0, 0x0)
    MobileOverride: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    EncounterVerticalList: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xe561be2e():
    pass

class PerkStyle():
    mPingTextLocalizationKey: (String, 0x0, 0x0, 0x0)
    mDisplayNameLocalizationKey: (String, 0x0, 0x0, 0x0)
    mTooltipNameLocalizationKey: (String, 0x0, 0x0, 0x0)
    mScript: (Link, 0x0, 0x0, PerkScript)
    mScript: (Pointer, 0x0, 0x0, PerkScript)
    mEnabled: (Bool, 0x0, 0x0, 0x0)
    mDefaultPerksWhenSplashed: (List, 0x0, Link, Perk)
    mPerkStyleScript: (String, 0x0, 0x0, 0x0)
    mIconTextureName: (String, 0x0, 0x0, 0x0)
    mSubStyleBonus: (List, 0x0, Embed, PerkSubStyleBonus)
    mPerkStyleName: (String, 0x0, 0x0, 0x0)
    mScriptAsSubStyle: (Pointer, 0x0, 0x0, PerkScript)
    mDefaultPageLocalizationKey: (String, 0x0, 0x0, 0x0)
    mAllowedSubStyles: (List, 0x0, U32, 0x0)
    mSlots: (List, 0x0, Embed, PerkSlot)
    mPerkStyleId: (U32, 0x0, 0x0, 0x0)
    mSlotlinks: (List, 0x0, Link, PerkSlot)
    mIsAdvancedStyle: (Bool, 0x0, 0x0, 0x0)
    mDefaultSplash: (Pointer, 0x0, 0x0, DefaultSplashedPerkStyle)
    mStyleVfxResourceResolver: (Pointer, 0x0, 0x0, ResourceResolver)
    mLcuAssetFileMap: (Map, String, String, 0x0)
    mBuffs: (List, 0x0, Pointer, PerkBuff)
    mDefaultStatModsPerSubStyle: (List, 0x0, Embed, DefaultStatModPerkSet)
    pass

class ToolSoundData():
    Move: (List, 0x0, String, 0x0)
    Attack: (List, 0x0, String, 0x0)
    Click: (List, 0x0, String, 0x0)
    Ready: (String, 0x0, 0x0, 0x0)
    Death: (String, 0x0, 0x0, 0x0)
    Special: (List, 0x0, String, 0x0)
    pass

class TftCutsceneAddMapProp():
    MapPropName: (String, 0x0, 0x0, 0x0)
    BlackboardName: (String, 0x0, 0x0, 0x0)
    pass

class BasicSpellSlotIntDriver(ILogicIntDriver):
    pass

class EnvironmentBakedLightingShadingModel(IEnvironmentShadingModel):
    pass

class SpringPhysicsEventData(BaseEventData):
    SpringToAffect: (Hash, 0x0, 0x0, 0x0)
    BlendOutTime: (F32, 0x0, 0x0, 0x0)
    BlendInTime: (F32, 0x0, 0x0, 0x0)
    pass

class HudKillCalloutData():
    TransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    MessageDuration: (F32, 0x0, 0x0, 0x0)
    pass

class 0xe5d6d75(IBehaviorScriptBlock):
    pass

class LuaPropertyDataGlobals():
    PropertyDataMap: (Map, Hash, Pointer, LuaPropertyData)
    pass

class StringArrayTableSet(ScriptTableSet):
    pass

class 0xe60a86d3(TableValue):
    mValue: (I32, 0x0, 0x0, 0x0)
    SlotType: (U32, 0x0, 0x0, 0x0)
    Value: (I32, 0x0, 0x0, 0x0)
    mType: (U32, 0x0, 0x0, 0x0)
    mBook: (U32, 0x0, 0x0, 0x0)
    Book: (U32, 0x0, 0x0, 0x0)
    pass

class 0xe6144e6d(0x64c18f7d):
    pass

class 0xe6147387(BaseRigPoseModifierData):
    OrientationType: (U8, 0x0, 0x0, 0x0)
    OrientationSource: (Pointer, 0x0, 0x0, ILogicVector3Driver)
    Joints: (List2, 0x0, Hash, 0x0)
    pass

class ILevelBehavior():
    pass

class 0xe622d482(ILogicFloatDriver):
    pass

class ISkinAugmentInstance():
    pass

class UiMetricTypeSimpleI(UiMetricTypeI):
    Text: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionSituationHasRecentlyRun(IContextualCondition):
    mSituationNameHash: (Hash, 0x0, 0x0, 0x0)
    mTime: (F32, 0x0, 0x0, 0x0)
    pass

class TftTeamPlannerTierData():
    TierCostText: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    TierChampionListLayout: (Hash, 0x0, 0x0, 0x0)
    TierCostIcon: (Hash, 0x0, 0x0, 0x0)
    TierTitle: (Hash, 0x0, 0x0, 0x0)
    pass

class TftCutsceneAcceleratingMissileClip(TftCutsceneMissileClip):
    Acceleration: (F32, 0x0, 0x0, 0x0)
    InitialSpeed: (F32, 0x0, 0x0, 0x0)
    MaxSpeed: (F32, 0x0, 0x0, 0x0)
    MinSpeed: (F32, 0x0, 0x0, 0x0)
    pass

class AttackEvents(MissileTriggeredActionSpec):
    TriggerOnlyOnce: (Bool, 0x0, 0x0, 0x0)
    TriggerOncePerParent: (Bool, 0x0, 0x0, 0x0)
    RollForCriticalHitResult: (Bool, 0x0, 0x0, 0x0)
    TriggerOncePerEnemyOfParent: (Bool, 0x0, 0x0, 0x0)
    TriggerPreAttack: (Bool, 0x0, 0x0, 0x0)
    TriggerLaunchAttack: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xe6cd2142():
    InkFillTime: (F32, 0x0, 0x0, 0x0)
    Acceleration: (Vec2, 0x0, 0x0, 0x0)
    MovementProjectionY: (Vec3, 0x0, 0x0, 0x0)
    MovementProjectionX: (Vec3, 0x0, 0x0, 0x0)
    MoveKick: (F32, 0x0, 0x0, 0x0)
    MoveDensity: (F32, 0x0, 0x0, 0x0)
    JetKinetics: (List, 0x3, Vec3, 0x0)
    Viscosity: (F32, 0x0, 0x0, 0x0)
    InitialDensityMapAsset: (String, 0x0, 0x0, 0x0)
    RenderGridSize: (I32, 0x0, 0x0, 0x0)
    Dissipation: (F32, 0x0, 0x0, 0x0)
    JetChaos: (List, 0x3, Vec3, 0x0)
    Diffusion: (F32, 0x0, 0x0, 0x0)
    Buoyancy: (F32, 0x0, 0x0, 0x0)
    InkFillRate: (F32, 0x0, 0x0, 0x0)
    FluidPartName: (String, 0x0, 0x0, 0x0)
    pass

class LuaPropertyDataEntry():
    Key: (String, 0x0, 0x0, 0x0)
    Property: (Pointer, 0x0, 0x0, LuaPropertyData)
    pass

class 0xe6f0047():
    DragonGoldValue: (U32, 0x0, 0x0, 0x0)
    0x296018d6: (U32, 0x0, 0x0, 0x0)
    DragonSoulGoldValue: (U32, 0x0, 0x0, 0x0)
    BaronGoldValue: (U32, 0x0, 0x0, 0x0)
    0x490b09: (U32, 0x0, 0x0, 0x0)
    TurretGoldValue: (U32, 0x0, 0x0, 0x0)
    0xbbdccf4e: (U32, 0x0, 0x0, 0x0)
    0xc649ac3c: (U32, 0x0, 0x0, 0x0)
    RiftHeraldGoldValue: (U32, 0x0, 0x0, 0x0)
    pass

class AiUnitConfig(AiUnitConfigBase):
    pass

class LolModesTeamConfig(IGameModeConfig):
    ByeTeamDisplayData: (Pointer, 0x0, 0x0, LolModesTeamDisplayData)
    0x363278ea: (U8, 0x0, 0x0, 0x0)
    TeamDisplayData: (List, 0x0, Embed, LolModesTeamDisplayData)
    TeamDisplayData: (List2, 0x0, Embed, LolModesTeamDisplayData)
    MaxTeams: (U8, 0x0, 0x0, 0x0)
    StartingHealth: (I32, 0x0, 0x0, 0x0)
    pass

class TftCutsceneProxy(GameObject):
    pass

class GlowCenteredOverlayTipStyle(TipStyleBase):
    pass

class MapNavigationGridOverlays():
    Overlays: (Map, String, Link, MapNavigationGridOverlay)
    pass

class VfxFieldDragDefinitionData():
    Position: (Embed, 0x0, 0x0, ValueVector3)
    Position: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    Radius: (Embed, 0x0, 0x0, ValueFloat)
    Radius: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    Strength: (Embed, 0x0, 0x0, ValueFloat)
    Strength: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    pass

class PingSecondaryRadialViewController(PingRadialBaseViewController):
    pass

class FixedNeutralCampSpawnBehavior(INeutralCampSpawnBehavior):
    0x29bec30a: (Hash, 0x0, 0x0, 0x0)
    AiGroupName: (Hash, 0x0, 0x0, 0x0)
    Units: (List2, 0x0, Embed, NeutralMinionSpawnConfig)
    pass

class 0xe75aad84():
    0x10a065ec: (List2, 0x0, U8, 0x0)
    MaxSpawnCount: (U32, 0x0, 0x0, 0x0)
    SpawnCountPerInterval: (U32, 0x0, 0x0, 0x0)
    0x299c176c: (Bool, 0x0, 0x0, 0x0)
    WaveShape: (Pointer, 0x0, 0x0, 0x114828a9)
    WaveShape: (Pointer, 0x0, 0x0, 0x2755f1f9)
    SpawnLocation: (Pointer, 0x0, 0x0, 0x7546469c)
    SpawnLocation: (Pointer, 0x0, 0x0, 0x87a6a884)
    SpawnIntervalSecs: (F32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    Characters: (List2, 0x0, Embed, 0x4f4c4ffc)
    Behaviors: (List2, 0x0, Pointer, 0x64c18f7d)
    0xa8705448: (Pointer, 0x0, 0x0, 0x968ce2ad)
    TeamToSpawn: (U32, 0x0, 0x0, 0x0)
    0xaebfc2af: (Bool, 0x0, 0x0, 0x0)
    CanDespawn: (Bool, 0x0, 0x0, 0x0)
    SpawnCountOvertime: (Pointer, 0x0, 0x0, 0xbd3b9f20)
    0xb97e4d7e: (Bool, 0x0, 0x0, 0x0)
    0xdc6c6389: (Bool, 0x0, 0x0, 0x0)
    ClusterSize: (U32, 0x0, 0x0, 0x0)
    ConditionalBehaviors: (List2, 0x0, Embed, 0xeff830de)
    pass

class BuffEffect():
    pass

class MaterialInstanceDef(IResource, IMaterialDef):
    Params: (List, 0x0, Embed, MaterialInstanceParamDef)
    Params: (Map, U16, Embed, MaterialInstanceParamDef)
    DynamicTextures: (Map, U16, Embed, MaterialInstanceDynamicTexture)
    DynamicSwitch: (Embed, 0x0, 0x0, MaterialInstanceDynamicSwitch)
    DynamicSwitch: (Pointer, 0x0, 0x0, IDynamicMaterialBoolDriver)
    DynamicParams: (Map, U16, Embed, MaterialInstanceDynamicParam)
    DynamicParams: (Map, U16, Pointer, IDynamicMaterialDriver)
    Name: (String, 0x0, 0x0, 0x0)
    BaseMaterial: (Link, 0x0, 0x0, HybridMaterialDef)
    ChildTechniques: (List, 0x0, Embed, 0xf7084b4a)
    Textures: (Map, U16, Embed, MaterialInstanceTextureDef)
    DynamicSwitchId: (U16, 0x0, 0x0, 0x0)
    Switches: (Map, U16, Embed, MaterialInstanceSwitchDef)
    ShaderMacros: (Map, String, String, 0x0)
    pass

class 0xe78a27ae(0x2b00c366):
    ItemId: (String, 0x0, 0x0, 0x0)
    0x2484d6c3: (Bool, 0x0, 0x0, 0x0)
    Emote: (Link, 0x0, 0x0, SummonerEmote)
    ItemTypeId: (String, 0x0, 0x0, 0x0)
    pass

class Challenge(BaseLoadoutData):
    mCompletionLevels: (List, 0x0, Embed, ChallengeCompletionLevel)
    pass

class EndOfGameViewController(ViewController):
    DefeatGroupHandle: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    VanguardScene: (Hash, 0x0, 0x0, 0x0)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    VanguardBgScene: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    ContinueButton: (Hash, 0x0, 0x0, 0x0)
    VictoryGroupHandle: (Hash, 0x0, 0x0, 0x0)
    TencentOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    VanguardContinueButton: (Hash, 0x0, 0x0, 0x0)
    pass

class UnitStatusPriorityList():
    mPrioritizedIconHandleNames: (List, 0x0, Hash, 0x0)
    mMinimumDisplayTime: (F32, 0x0, 0x0, 0x0)
    mPrioritizedUnitStatusData: (List, 0x0, Embed, UnitStatusData)
    TextureName: (String, 0x0, 0x0, 0x0)
    pass

class LaneData():
    mNavigationPoints: (List, 0x0, String, 0x0)
    mContainedRegions: (List, 0x0, String, 0x0)
    pass

class DamageSourceTemplate():
    DamageTags: (List, 0x0, String, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    DamageProperties: (U32, 0x0, 0x0, 0x0)
    pass

class 0xe7d2c6f3(ITftBehaviorScriptEvent):
    pass

class LabelElement():
    mOffset: (Vec2, 0x0, 0x0, 0x0)
    mFontDescription: (Link, 0x0, 0x0, GameFontDescription)
    pass

class LuaPropertyDataIntArray(LuaPropertyData):
    Values: (List, 0x0, I32, 0x0)
    pass

class VerticalFacingType():
    pass

class 0xe7face9d():
    StaticTexturePath: (String, 0x0, 0x0, 0x0)
    VfxTexturePath: (String, 0x0, 0x0, 0x0)
    pass

class HudColorData():
    mSelectedIndicatorColor: (Color, 0x0, 0x0, 0x0)
    mEnemyChatColor: (Color, 0x0, 0x0, 0x0)
    mClubTagNeutralChatColor: (Color, 0x0, 0x0, 0x0)
    mClubTagChaosChatColor: (Color, 0x0, 0x0, 0x0)
    mOrderColor: (Color, 0x0, 0x0, 0x0)
    QuestTrackerOngoingColor: (Color, 0x0, 0x0, 0x0)
    0x2558b51: (Color, 0x0, 0x0, 0x0)
    mNeutralChatColor: (Color, 0x0, 0x0, 0x0)
    mEnemyColor: (Color, 0x0, 0x0, 0x0)
    QuestTrackerSuccessColor: (Color, 0x0, 0x0, 0x0)
    mPingChatColor: (Color, 0x0, 0x0, 0x0)
    TftThreeStarColor: (Color, 0x0, 0x0, 0x0)
    ChatComboBoxOptionHighlightedColor: (Color, 0x0, 0x0, 0x0)
    mSummonerNameDeadColor: (Color, 0x0, 0x0, 0x0)
    mOrderChatColor: (Color, 0x0, 0x0, 0x0)
    mTeamChatColor: (Color, 0x0, 0x0, 0x0)
    TftActiveButtonTextColor: (Color, 0x0, 0x0, 0x0)
    mDeathRecapPhysicalDamageColor: (Color, 0x0, 0x0, 0x0)
    mSpellHotKeyEnabledColor: (Color, 0x0, 0x0, 0x0)
    AbilityResourceThresholdRangeLowColor: (Color, 0x0, 0x0, 0x0)
    mJunglePlantColor: (Color, 0x0, 0x0, 0x0)
    mInputChatColor: (Color, 0x0, 0x0, 0x0)
    0x3fdee6e4: (List, 0x4, Color, 0x0)
    KillCalloutBountyColor: (Color, 0x0, 0x0, 0x0)
    mSpellHotKeyDisabledColor: (Color, 0x0, 0x0, 0x0)
    0x425297af: (Color, 0x0, 0x0, 0x0)
    VoteEmptyColor: (Color, 0x0, 0x0, 0x0)
    ChatComboBoxOptionDefaultColor: (Color, 0x0, 0x0, 0x0)
    mSelfColor: (Color, 0x0, 0x0, 0x0)
    mLevelUpColor: (Color, 0x0, 0x0, 0x0)
    VoteYesColor: (Color, 0x0, 0x0, 0x0)
    mVoiceChatHaloTextureColor: (Color, 0x0, 0x0, 0x0)
    TftFriendlyColor: (Color, 0x0, 0x0, 0x0)
    mEvolutionColor: (Color, 0x0, 0x0, 0x0)
    mDeathFriendlyTeamColor: (Color, 0x0, 0x0, 0x0)
    mItemCalloutBodyColor: (Color, 0x0, 0x0, 0x0)
    mSummonerSpellUpgradeColor: (Color, 0x0, 0x0, 0x0)
    mPlatformChatColor: (Color, 0x0, 0x0, 0x0)
    TftInactiveButtonTextColor: (Color, 0x0, 0x0, 0x0)
    mItemHotKeyDisabledColor: (Color, 0x0, 0x0, 0x0)
    0x6b1a20e0: (Color, 0x0, 0x0, 0x0)
    0x6cfe6e40: (Color, 0x0, 0x0, 0x0)
    mVoiceChatHoverTextColor: (Color, 0x0, 0x0, 0x0)
    mChaosChatColor: (Color, 0x0, 0x0, 0x0)
    mSummonerNameDefaultColor: (Color, 0x0, 0x0, 0x0)
    mItemCalloutItemColor: (Color, 0x0, 0x0, 0x0)
    TftShopDropRateTextColors: (List, 0x5, Color, 0x0)
    TftActiveTextColor: (Color, 0x0, 0x0, 0x0)
    mStatBoostedColor: (Color, 0x0, 0x0, 0x0)
    mClubTagEnemyChatColor: (Color, 0x0, 0x0, 0x0)
    mDeathChaosColor: (Color, 0x0, 0x0, 0x0)
    mAllChatColor: (Color, 0x0, 0x0, 0x0)
    mHighlightedIndicatorColor: (Color, 0x0, 0x0, 0x0)
    mMarkedIndicatorColor: (Color, 0x0, 0x0, 0x0)
    mClubTagOrderChatColor: (Color, 0x0, 0x0, 0x0)
    mTimestampChatColor: (Color, 0x0, 0x0, 0x0)
    mWhisperColor: (Color, 0x0, 0x0, 0x0)
    VoteNocolor: (Color, 0x0, 0x0, 0x0)
    mShadowChatColor: (Color, 0x0, 0x0, 0x0)
    mFeedbackChatColor: (Color, 0x0, 0x0, 0x0)
    TftPenalizedStatColor: (Color, 0x0, 0x0, 0x0)
    AbilityResourceThresholdRangeHighColor: (Color, 0x0, 0x0, 0x0)
    mEnemyLaneMinionBarColor: (Color, 0x0, 0x0, 0x0)
    mNetworkChatColor: (Color, 0x0, 0x0, 0x0)
    QuestTrackerFailureColor: (Color, 0x0, 0x0, 0x0)
    AbilityResourceThresholdRangeMediumColor: (Color, 0x0, 0x0, 0x0)
    0xce60fb10: (Color, 0x0, 0x0, 0x0)
    0xd4a472e0: (Color, 0x0, 0x0, 0x0)
    mFriendlyColor: (Color, 0x0, 0x0, 0x0)
    mDeathRecapTrueDamageColor: (Color, 0x0, 0x0, 0x0)
    mFriendlyChatColor: (Color, 0x0, 0x0, 0x0)
    mClubTagFriendlyChatColor: (Color, 0x0, 0x0, 0x0)
    mDeathRecapMagicDamageColor: (Color, 0x0, 0x0, 0x0)
    mVoiceChatDefaultTextColor: (Color, 0x0, 0x0, 0x0)
    mSummonerNameSelfColor: (Color, 0x0, 0x0, 0x0)
    mPartyChatColor: (Color, 0x0, 0x0, 0x0)
    TftChosenColor: (Color, 0x0, 0x0, 0x0)
    mDeathOrderColor: (Color, 0x0, 0x0, 0x0)
    mNeutralColor: (Color, 0x0, 0x0, 0x0)
    mGoldChatColor: (Color, 0x0, 0x0, 0x0)
    mItemHotKeyEnabledColor: (Color, 0x0, 0x0, 0x0)
    mChaosColor: (Color, 0x0, 0x0, 0x0)
    mDeathEnemyTeamColor: (Color, 0x0, 0x0, 0x0)
    TftInactiveTextColor: (Color, 0x0, 0x0, 0x0)
    mStatNormalColor: (Color, 0x0, 0x0, 0x0)
    mFriendlyLaneMinionBarColor: (Color, 0x0, 0x0, 0x0)
    pass

class LoadingScreenSummonerTitleData():
    LocalPlayerTitleColor: (Color, 0x0, 0x0, 0x0)
    SummonerTitle: (List, 0x0, Hash, 0x0)
    OtherPlayerTitleColor: (Color, 0x0, 0x0, 0x0)
    pass

class SkinnedPbrShadingModel(ISkinnedShadingModel):
    pass

class GetMapPropFloatDynamicMaterialFloatDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    mKeyName: (String, 0x0, 0x0, 0x0)
    pass

class ItemRecommendationOverrideContext():
    mModeNameStringId: (Hash, 0x0, 0x0, 0x0)
    mPosition: (Hash, 0x0, 0x0, 0x0)
    mMapId: (U32, 0x0, 0x0, 0x0)
    pass

class StealthVfxInstance():
    Effect: (Link, 0x0, 0x0, StealthVfx)
    pass

class LobbyLabFields():
    PopupViewController: (Link, 0x0, 0x0, ModalDialogViewController)
    pass

class RunLevelFunctionBlock(IRunFunctionBlock):
    Function: (Embed, 0x0, 0x0, LevelScriptFunctionLink)
    pass

class BerserkTargetingPriorityList():
    BerserkTargetingParametersPriorityList: (List, 0x0, Embed, BerserkTargetingParameters)
    pass

class SkinLineData():
    mName: (String, 0x0, 0x0, 0x0)
    mSkinLineId: (U32, 0x0, 0x0, 0x0)
    mDisplayName: (String, 0x0, 0x0, 0x0)
    pass

class ParTypeConfig():
    Wind: (Embed, 0x0, 0x0, ParTypeData)
    Heat: (Embed, 0x0, 0x0, ParTypeData)
    Energy: (Embed, 0x0, 0x0, ParTypeData)
    Shield: (Embed, 0x0, 0x0, ParTypeData)
    0x49e12631: (Embed, 0x0, 0x0, ParTypeData)
    Rage: (Embed, 0x0, 0x0, ParTypeData)
    Ferocity: (Embed, 0x0, 0x0, ParTypeData)
    None: (Embed, 0x0, 0x0, ParTypeData)
    Other: (Embed, 0x0, 0x0, ParTypeData)
    Bloodwell: (Embed, 0x0, 0x0, ParTypeData)
    0xd70134be: (Embed, 0x0, 0x0, ParTypeData)
    Mana: (Embed, 0x0, 0x0, ParTypeData)
    0xfa8e0bdd: (Embed, 0x0, 0x0, ParTypeData)
    pass

class HqCommon(AnimatedBuilding):
    pass

class 0xe8c34b52(IGameModeConfig):
    EliminatedColor: (Color, 0x0, 0x0, 0x0)
    AugmentColors: (Map, U8, Color, 0x0)
    0xf021feb3: (U8, 0x0, 0x0, 0x0)
    pass

class ObjectiveBannerViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    AnimData: (Embed, 0x0, 0x0, HudBannerData)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    Text: (Hash, 0x0, 0x0, 0x0)
    ObjectName: (String, 0x0, 0x0, 0x0)
    pass

class TftPassRewardLootItem(TftPassRewardBase):
    LootItem: (Link, 0x0, 0x0, LootItem)
    pass

class ViewControllerFilter_Not(ViewControllerFilterI):
    Filter: (Pointer, 0x0, 0x0, ViewControllerFilterI)
    pass

class ManagerSettings():
    MaximumMinimapScale: (F32, 0x0, 0x0, 0x0)
    MinimumMinimapScale: (F32, 0x0, 0x0, 0x0)
    MinimumGlobalScale: (F32, 0x0, 0x0, 0x0)
    MaximumGlobalScale: (F32, 0x0, 0x0, 0x0)
    pass

class 0xe90af953():
    Buff: (Hash, 0x0, 0x0, 0x0)
    0xbe161d6e: (U8, 0x0, 0x0, 0x0)
    pass

class IResourceResolver():
    pass

class 0xe92f8b6c(ViewController):
    0x147429f5: (String, 0x0, 0x0, 0x0)
    0x1b7ff930: (Embed, 0x0, 0x0, 0x12b12bdf)
    0x23ff90f5: (String, 0x0, 0x0, 0x0)
    CardTemplate: (Pointer, 0x0, 0x0, LoadingScreenPlayerCardBaseData)
    PlayerSlotSplashUv: (Vec4, 0x0, 0x0, 0x0)
    SpacerData: (Pointer, 0x0, 0x0, 0xacb2dba1)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    0x42324784: (Embed, 0x0, 0x0, 0x7dc4f3ec)
    0x52a578b9: (Embed, 0x0, 0x0, 0x12b12bdf)
    0x5d9323c0: (Hash, 0x0, 0x0, 0x0)
    0x68773c45: (Hash, 0x0, 0x0, 0x0)
    LowerCardRegion: (Hash, 0x0, 0x0, 0x0)
    UpperCardRegion: (Hash, 0x0, 0x0, 0x0)
    0xa052ddda: (Hash, 0x0, 0x0, 0x0)
    0xadf9c6d7: (Embed, 0x0, 0x0, 0x7dc4f3ec)
    0xc2e4a761: (String, 0x0, 0x0, 0x0)
    SubTeamsLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    0xebeabff1: (Hash, 0x0, 0x0, 0x0)
    0xfff63be6: (String, 0x0, 0x0, 0x0)
    pass

class ClipBaseData():
    mName: (Hash, 0x0, 0x0, 0x0)
    mAnimationInterruptionGroupNames: (List, 0x0, Hash, 0x0)
    mFlags: (U32, 0x0, 0x0, 0x0)
    Accessorylist: (List, 0x0, Pointer, ClipAccessoryData)
    mId: (U32, 0x0, 0x0, 0x0)
    pass

class VfxPrimitivePlanarProjection(VfxPrimitiveProjectionBase):
    pass

class 0xe9a3c91d(GameCalculation):
    mRangedMultiplier: (Pointer, 0x0, 0x0, IGameCalculationPart)
    pass

class FontLocaleResolutions():
    LocaleName: (String, 0x0, 0x0, 0x0)
    Resolutions: (List, 0x0, Embed, FontResolution)
    pass

class CurveTheDifferenceHeightSolver(HeightSolverType):
    mInitialTargetHeightOffset: (F32, 0x0, 0x0, 0x0)
    pass

class HudOptionalBinData():
    mName: (String, 0x0, 0x0, 0x0)
    mPriority: (U32, 0x0, 0x0, 0x0)
    pass

class NeutralTimerViewController(ViewController):
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    NeutralTimers: (List, 0x0, Embed, NeutralTimers)
    HasEsportsUi: (Bool, 0x0, 0x0, 0x0)
    ObjectName: (String, 0x0, 0x0, 0x0)
    EsportsLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    pass

class MaterialParameterDataCollection():
    Entries: (Map, String, Embed, IdMappingEntry)
    NextId: (U16, 0x0, 0x0, 0x0)
    Data: (Map, U16, Embed, MaterialParameterData)
    0xea57bf12: (String, 0x0, 0x0, 0x0)
    pass

class GameCalculationConditional(IGameCalculation):
    mDefaultGameCalculation: (Hash, 0x0, 0x0, 0x0)
    mConditionalGameCalculation: (Hash, 0x0, 0x0, 0x0)
    mConditionalCalculationRequirements: (Pointer, 0x0, 0x0, ICastRequirement)
    pass

class ScoreLineCherryUiData(ScoreLineBaseUiData):
    UnitLevel: (Embed, 0x0, 0x0, UnitLevelUiData)
    OpenMuteModalButton: (Hash, 0x0, 0x0, 0x0)
    ItemSlots: (Embed, 0x0, 0x0, DetailedItemSlots)
    ItemSlots: (Embed, 0x0, 0x0, SimpleItemSlots)
    Scene: (Hash, 0x0, 0x0, 0x0)
    Portrait: (Embed, 0x0, 0x0, CherryUiPlayerPortraitData)
    ChatMuteButton: (Hash, 0x0, 0x0, 0x0)
    AugmentSlots: (Embed, 0x0, 0x0, 0xfc331f53)
    OpenReportModalButton: (Hash, 0x0, 0x0, 0x0)
    DragBarSlot: (Hash, 0x0, 0x0, 0x0)
    PortraitRegion: (Hash, 0x0, 0x0, 0x0)
    SpellSlots: (Embed, 0x0, 0x0, ScoreLineSpellSlots)
    SelfSlotHighlight: (Hash, 0x0, 0x0, 0x0)
    ChampionName: (Embed, 0x0, 0x0, ChampionNameUiData)
    0x9f82652b: (Hash, 0x0, 0x0, 0x0)
    MuteAllButton: (Hash, 0x0, 0x0, 0x0)
    SocialTooltipAnchor: (Hash, 0x0, 0x0, 0x0)
    EmoteMuteButton: (Hash, 0x0, 0x0, 0x0)
    MuteModalAnchor: (Hash, 0x0, 0x0, 0x0)
    SummonerName: (Embed, 0x0, 0x0, SummonerNameUiData)
    UltCooldownGem: (Embed, 0x0, 0x0, CooldownGemUiData)
    Metrics: (Map, U8, Pointer, UiMetricUnitTypeI)
    MuteSelfButton: (Hash, 0x0, 0x0, 0x0)
    MusicButton: (Hash, 0x0, 0x0, 0x0)
    PingMuteButton: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xe9ed7e9e(0x2755f1f9):
    Radius: (F32, 0x0, 0x0, 0x0)
    pass

class UiElementEffectCooldownData(UiElementEffectData):
    mEffectColor0: (Color, 0x0, 0x0, 0x0)
    mEffectColor1: (Color, 0x0, 0x0, 0x0)
    pass

class SiblingStatCoefficientBySubPart(IGameCalculationPart):
    SourceStatFormula: (U8, 0x0, 0x0, 0x0)
    SourceStat: (U8, 0x0, 0x0, 0x0)
    SubPart: (Pointer, 0x0, 0x0, IGameCalculationPart)
    pass

class 0xea148f98(IFxActionInstance):
    pass

class PercentageOfBuffNameElapsed(IGameCalculationPart):
    ScalingTagKey: (String, 0x0, 0x0, 0x0)
    BuffName: (Hash, 0x0, 0x0, 0x0)
    IconKey: (String, 0x0, 0x0, 0x0)
    Coefficient: (F32, 0x0, 0x0, 0x0)
    pass

class OptionItemSecondaryHotkeys2Column_Header():
    Column2LabelTraKey: (String, 0x0, 0x0, 0x0)
    Column0LabelTraKey: (String, 0x0, 0x0, 0x0)
    Column1LabelTraKey: (String, 0x0, 0x0, 0x0)
    pass

class LoadoutFeatureData(BinFileContainer):
    mLoadoutCategory: (String, 0x0, 0x0, 0x0)
    LoadingScreenOnly: (Bool, 0x0, 0x0, 0x0)
    mAudioBanks: (List, 0x0, Embed, BankUnit)
    mScript: (Link, 0x0, 0x0, LoadoutScript)
    mBinaryFile: (Option, 0x0, String, 0x0)
    mBinaryFile: (String, 0x0, 0x0, 0x0)
    mLoadoutProperties: (List, 0x0, String, 0x0)
    mGdsObjectPathTemplates: (Map, String, String, 0x0)
    mTutorialTftCompanion: (Hash, 0x0, 0x0, 0x0)
    mDefaultTftCompanion: (Hash, 0x0, 0x0, 0x0)
    mMutator: (Option, 0x0, String, 0x0)
    mMutator: (String, 0x0, 0x0, 0x0)
    mFeature: (U32, 0x0, 0x0, 0x0)
    mLoadFromContentIds: (Bool, 0x0, 0x0, 0x0)
    pass

class FxActionTimeDilateInstance(IFxActionInstance):
    pass

class CherrySpectateMatchDialogViewController(ViewController):
    ButtonDefaultText: (Hash, 0x0, 0x0, 0x0)
    MatchTemplate: (Embed, 0x0, 0x0, 0x77fb37dd)
    0x14810744: (String, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    SpectateButtonHandle: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MatchGrid: (Hash, 0x0, 0x0, 0x0)
    ButtonHoverText: (Hash, 0x0, 0x0, 0x0)
    DialogText: (Embed, 0x0, 0x0, CherrySpectateMatchDialogText)
    TeamOneIcon: (Hash, 0x0, 0x0, 0x0)
    TeamTwoIcon: (Hash, 0x0, 0x0, 0x0)
    0x9e7b5cd7: (String, 0x0, 0x0, 0x0)
    ButtonText: (Hash, 0x0, 0x0, 0x0)
    TitleOngoingTra: (String, 0x0, 0x0, 0x0)
    0xd9e1766a: (String, 0x0, 0x0, 0x0)
    ButtonPressedText: (Hash, 0x0, 0x0, 0x0)
    SpectateTitleText: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class Champion(WadFileDescriptor):
    CatalogEntry: (Embed, 0x0, 0x0, CatalogEntry)
    JunglePathRecommendations: (Embed, 0x0, 0x0, JunglePathRecommendations)
    SpellRankUpRecommendations: (Embed, 0x0, 0x0, RecSpellRecommendations)
    RecSpellRankUpInfolist: (Hash, 0x0, 0x0, 0x0)
    AdditionalRoots: (List, 0x0, String, 0x0)
    mChampionItemRecommendations: (Embed, 0x0, 0x0, ChampionItemRecommendations)
    StatStoneSets: (List, 0x0, Hash, 0x0)
    StatStoneSets: (List, 0x0, Link, StatStoneSet)
    Name: (String, 0x0, 0x0, 0x0)
    DefaultItemShopFilter: (U32, 0x0, 0x0, 0x0)
    CharacterSelectionUiPlaceholderIconPath: (String, 0x0, 0x0, 0x0)
    FixedLoadScreenPosition: (I8, 0x0, 0x0, 0x0)
    AdditionalCharacters: (List, 0x0, Link, Character)
    pass

class SelfAoe(TargetingTypeData):
    pass

class ContextualConditionSpellIsReady(IContextualConditionSpell, IContextualCondition):
    mSpellIsReady: (Bool, 0x0, 0x0, 0x0)
    pass

class CherryTeamFlyoutPanelTeamFrame():
    EliminatedState: (Embed, 0x0, 0x0, IconStateData)
    Critical: (Hash, 0x0, 0x0, 0x0)
    CriticalState: (Embed, 0x0, 0x0, IconStateData)
    Default: (Hash, 0x0, 0x0, 0x0)
    Eliminated: (Hash, 0x0, 0x0, 0x0)
    DefaultState: (Embed, 0x0, 0x0, IconStateData)
    pass

class CreateCustomTableBlock(IScriptBlock):
    Dest: (Embed, 0x0, 0x0, CustomTableSet)
    CustomTable: (Embed, 0x0, 0x0, CustomTableSet)
    pass

class SpellCalculationConditional(ISpellCalculation):
    mDefaultSpellCalculation: (Hash, 0x0, 0x0, 0x0)
    mConditionalCalculationRequirements: (Pointer, 0x0, 0x0, ICastRequirement)
    mConditionalSpellCalculation: (Hash, 0x0, 0x0, 0x0)
    pass

class NotificationListItemData():
    LootItemCountBackground: (Hash, 0x0, 0x0, 0x0)
    ClickRegion: (Hash, 0x0, 0x0, 0x0)
    ActiveGameInviteIcon: (Hash, 0x0, 0x0, 0x0)
    ActiveGameGradient: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    LootItemCountText: (Hash, 0x0, 0x0, 0x0)
    InactiveGameInviteIcon: (Hash, 0x0, 0x0, 0x0)
    AlertIcon: (Hash, 0x0, 0x0, 0x0)
    LootIcon: (Hash, 0x0, 0x0, 0x0)
    UnreadIcon: (Hash, 0x0, 0x0, 0x0)
    BodyText: (Hash, 0x0, 0x0, 0x0)
    PassRewardIcon: (Hash, 0x0, 0x0, 0x0)
    TimestampText: (Hash, 0x0, 0x0, 0x0)
    AddFriendIcon: (Hash, 0x0, 0x0, 0x0)
    GenericIcon: (Hash, 0x0, 0x0, 0x0)
    WarningIcon: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xeacb459e(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    HealthBarData: (Embed, 0x0, 0x0, HealthBarData)
    0xe97a2996: (Hash, 0x0, 0x0, 0x0)
    StatusData: (Embed, 0x0, 0x0, UiUnitStatusData)
    pass

class AiUnitConfigBase():
    CharacterRecord: (String, 0x0, 0x0, 0x0)
    Skin: (String, 0x0, 0x0, 0x0)
    AiScript: (Link, 0x0, 0x0, Rscript)
    Skins: (Map, U32, Embed, AiUnitConfigSkinLink)
    pass

class StatStoneMasteryEffects():
    MasteryToBackgroundEffect: (Map, U32, Link, VfxSystemDefinitionData)
    pass

class HudFeedbackDamageData():
    mOverTimeForFlashSeconds: (F32, 0x0, 0x0, 0x0)
    mStunTexture: (String, 0x0, 0x0, 0x0)
    mMaxPercentageForMostReadHealth: (F32, 0x0, 0x0, 0x0)
    mLowHealthFlashOpacityStrength: (F32, 0x0, 0x0, 0x0)
    mHitTexture: (String, 0x0, 0x0, 0x0)
    mLowHealthFlashDuration: (F32, 0x0, 0x0, 0x0)
    mStartFlashAlpha: (F32, 0x0, 0x0, 0x0)
    mPercentageDamageForFlash: (F32, 0x0, 0x0, 0x0)
    mLowHealthFlashThresholdPercentage: (F32, 0x0, 0x0, 0x0)
    mFlashDuration: (F32, 0x0, 0x0, 0x0)
    pass

class 0xeaef4fc9(0xca4d32d1):
    Value: (U32, 0x0, 0x0, 0x0)
    pass

class BackdropElementParams():
    mBackdropColor: (Color, 0x0, 0x0, 0x0)
    mHighlightColor: (Color, 0x0, 0x0, 0x0)
    pass

class UiComboBoxDefinition():
    ObjectPath: (Hash, 0x0, 0x0, 0x0)
    ListOptionTextElementData: (Hash, 0x0, 0x0, 0x0)
    ListOptionTextElementData: (Link, 0x0, 0x0, TextElementData)
    ListOptionHitAreaElementData: (Hash, 0x0, 0x0, 0x0)
    ListOptionHitAreaElementData: (Link, 0x0, 0x0, RegionElementData)
    DropdownHoverElementData: (Hash, 0x0, 0x0, 0x0)
    DropdownHoverElementData: (Link, 0x0, 0x0, IconElementData)
    DropdownBackdropElementData: (Hash, 0x0, 0x0, 0x0)
    DropdownBackdropElementData: (Link, 0x0, 0x0, IconElementData)
    SoundEvents: (Pointer, 0x0, 0x0, UiComboBoxSoundEvents)
    SelectedHighlightElementData: (Hash, 0x0, 0x0, 0x0)
    SelectedHighlightElementData: (Link, 0x0, 0x0, IconElementData)
    DropdownDisplayTraKey: (String, 0x0, 0x0, 0x0)
    ButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    ListDisplayDirection: (U8, 0x0, 0x0, 0x0)
    pass

class 0xeaf8e31e(SkinnedMeshDataMaterialController):
    pass

class DetailedItemSlots():
    Item6: (Embed, 0x0, 0x0, ItemSlotDetailedUiData)
    Item4: (Embed, 0x0, 0x0, ItemSlotDetailedUiData)
    Item5: (Embed, 0x0, 0x0, ItemSlotDetailedUiData)
    Item2: (Embed, 0x0, 0x0, ItemSlotDetailedUiData)
    Item3: (Embed, 0x0, 0x0, ItemSlotDetailedUiData)
    Item0: (Embed, 0x0, 0x0, ItemSlotDetailedUiData)
    Item1: (Embed, 0x0, 0x0, ItemSlotDetailedUiData)
    pass

class ISequenceAction():
    Disabled: (Bool, 0x0, 0x0, 0x0)
    Start: (Embed, 0x0, 0x0, SequenceTiming)
    End: (Embed, 0x0, 0x0, SequenceTiming)
    pass

class PurchaseDialog(ModalDialogViewController):
    MultiTitleText: (Hash, 0x0, 0x0, 0x0)
    SingleTitleText: (Hash, 0x0, 0x0, 0x0)
    MultiBackgroundRegion: (Hash, 0x0, 0x0, 0x0)
    SinglePurchaseItemIcon: (Hash, 0x0, 0x0, 0x0)
    SingleCloseButtonRegion: (Hash, 0x0, 0x0, 0x0)
    SubPurchaseRegion: (Hash, 0x0, 0x0, 0x0)
    SingleScene: (Hash, 0x0, 0x0, 0x0)
    MultiPurchaseManagedLayout: (Hash, 0x0, 0x0, 0x0)
    PurchaseButton: (Hash, 0x0, 0x0, 0x0)
    MoreInfoButton: (Hash, 0x0, 0x0, 0x0)
    SubPurchaseElements: (Embed, 0x0, 0x0, PurchaseDialogSubPurchaseElements)
    StoreDialog: (Hash, 0x0, 0x0, 0x0)
    StoreDialog: (Link, 0x0, 0x0, StoreDialogViewController)
    MultiBodyText: (Hash, 0x0, 0x0, 0x0)
    0x76d6191: (Embed, 0x0, 0x0, ViewPaneDefinition)
    HeaderElements: (Embed, 0x0, 0x0, PurchaseDialogSubPurchaseHeaderElements)
    ResizableBackdrop: (Hash, 0x0, 0x0, 0x0)
    MultiSubPurchaseSectionLabel: (Hash, 0x0, 0x0, 0x0)
    MultiPurchaseItemIcon: (Hash, 0x0, 0x0, 0x0)
    0xa567ed12: (Embed, 0x0, 0x0, ViewPaneDefinition)
    MultiScene: (Hash, 0x0, 0x0, 0x0)
    SingleBodyText: (Hash, 0x0, 0x0, 0x0)
    MultiCloseButtonRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class ActiveItemTelemetryData():
    ActiveItemTelemetryEventOptions: (List, 0x0, String, 0x0)
    pass

class SummonerNameCreateViewController(ViewController):
    ErrorText: (Hash, 0x0, 0x0, 0x0)
    SubmitButton: (Hash, 0x0, 0x0, 0x0)
    SoftKeyboardTransitionData: (Embed, 0x0, 0x0, HudMenuTransitionData)
    InputScene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    LoadingText: (Hash, 0x0, 0x0, 0x0)
    InputText: (Hash, 0x0, 0x0, 0x0)
    SubmitButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xeb7bcb69(ISequenceAction):
    ParticleEffects: (Map, U8, Hash, 0x0)
    0x5af11142: (Link, 0x0, 0x0, SequenceObjectSelector)
    pass

class HoverTips():
    mHovertipList: (List, 0x0, String, 0x0)
    pass

class UpdaterData():
    mOutputType: (U32, 0x0, 0x0, 0x0)
    mInputType: (U32, 0x0, 0x0, 0x0)
    mValueProcessorDataList: (List, 0x0, Pointer, ValueProcessorData)
    Input: (Pointer, 0x0, 0x0, IBaseParametricUpdater)
    pass

class IScriptBtEvent(IScriptEvent):
    pass

class PostGamePlayerTemplate():
    SummonerIcon: (Hash, 0x0, 0x0, 0x0)
    AugmentTitle: (String, 0x0, 0x0, 0x0)
    AugmentContainerIcon: (Hash, 0x0, 0x0, 0x0)
    0x244a6cca: (U8, 0x0, 0x0, 0x0)
    AugmentContainerIconFrame: (Hash, 0x0, 0x0, 0x0)
    NameTag: (Hash, 0x0, 0x0, 0x0)
    PaginationButtonNext: (Hash, 0x0, 0x0, 0x0)
    PlaybookButton: (Hash, 0x0, 0x0, 0x0)
    AugmentTooltipButton: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    PlacementText: (Hash, 0x0, 0x0, 0x0)
    UnitSlots: (List, 0x0, Hash, 0x0)
    UnitSlots: (List, 0x8, Hash, 0x0)
    PlaybookIconFrame: (Hash, 0x0, 0x0, 0x0)
    PaginationButtonBack: (Hash, 0x0, 0x0, 0x0)
    SummonerIconFrame: (Hash, 0x0, 0x0, 0x0)
    AugmentIcons: (List, 0x3, Hash, 0x0)
    HiddenUnitCountText: (Hash, 0x0, 0x0, 0x0)
    PlaybookIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class TftAnnouncementsViewController(ViewController):
    CenterIconLink: (Hash, 0x0, 0x0, 0x0)
    CenterTitleLink: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    SceneTransitionOut: (Embed, 0x0, 0x0, HudMenuTransitionData)
    SceneTransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    MobileOverrideBinName: (String, 0x0, 0x0, 0x0)
    SceneLink: (Hash, 0x0, 0x0, 0x0)
    AnimatedIconLink: (Hash, 0x0, 0x0, 0x0)
    BaseBinName: (String, 0x0, 0x0, 0x0)
    pass

class ContextualConditionBuffCounterChanged(IContextualConditionBuff):
    0x395e4a90: (Bool, 0x0, 0x0, 0x0)
    Buff: (Hash, 0x0, 0x0, 0x0)
    ExcludeIncrements: (Bool, 0x0, 0x0, 0x0)
    0xfa24eccf: (Bool, 0x0, 0x0, 0x0)
    pass

class CustomAbilitiesUiData():
    ExtraAbilities: (Map, String, Embed, SpellSlotDetailedUiDefinition)
    ExtraAbilities: (Map, U32, Embed, SpellSlotDetailedUiDefinition)
    pass

class TftGravityHeightSolver(TftHeightSolverType):
    Gravity: (F32, 0x0, 0x0, 0x0)
    pass

class LogicDriverBoolParametricUpdater(IBooleanParametricUpdater):
    Driver: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    pass

class IPath(MapPlaceable):
    pass

class LossOfControlTemplate():
    mBarElement: (Embed, 0x0, 0x0, BarElement)
    mBackdropElement: (Embed, 0x0, 0x0, BackdropElement)
    mIcons: (Embed, 0x0, 0x0, LossOfControlIcons)
    pass

class IFloatParametricUpdater(IBaseParametricUpdater):
    pass

class CharacterToolData():
    LevelDodge: (F32, 0x0, 0x0, 0x0)
    AlternateForms: (List, 0x0, Embed, ToolAlternateForm)
    BaseSpellEffectiveness: (F32, 0x0, 0x0, 0x0)
    Description: (String, 0x0, 0x0, 0x0)
    ChampionId: (I32, 0x0, 0x0, 0x0)
    RecItems: (List, 0x0, String, 0x0)
    PlatformEnabled: (Bool, 0x0, 0x0, 0x0)
    MapAiPresence: (Map, U32, Embed, ToolAiPresence)
    LevelSpellEffectiveness: (F32, 0x0, 0x0, 0x0)
    AttackSpeed: (F32, 0x0, 0x0, 0x0)
    BotEnabledMm: (Bool, 0x0, 0x0, 0x0)
    Tips3: (String, 0x0, 0x0, 0x0)
    MagicRank: (I32, 0x0, 0x0, 0x0)
    PostAttackMoveDelay: (F32, 0x0, 0x0, 0x0)
    BaseAttackSpeedBonus: (F32, 0x0, 0x0, 0x0)
    SearchTagsSecondary: (String, 0x0, 0x0, 0x0)
    Education: (Embed, 0x0, 0x0, ToolEducationData)
    DefenseRank: (I32, 0x0, 0x0, 0x0)
    PassiveData: (List, 0x0, Embed, ToolPassiveData)
    Roles: (String, 0x0, 0x0, 0x0)
    Inherits: (Embed, 0x0, 0x0, ToolInheritsData)
    ChasingAttackRangePercent: (F32, 0x0, 0x0, 0x0)
    ParFadeColor: (String, 0x0, 0x0, 0x0)
    BotEnabled: (Bool, 0x0, 0x0, 0x0)
    WeaponMaterialCrit: (String, 0x0, 0x0, 0x0)
    CastShadows: (Bool, 0x0, 0x0, 0x0)
    DifficultyRank: (I32, 0x0, 0x0, 0x0)
    Lore2: (String, 0x0, 0x0, 0x0)
    Classification: (String, 0x0, 0x0, 0x0)
    AbilitySlotCc: (List, 0x0, I32, 0x0)
    PassLev1Desc: (List, 0x0, String, 0x0)
    Sound: (Embed, 0x0, 0x0, ToolSoundData)
    SkipDrawToonInking: (Bool, 0x0, 0x0, 0x0)
    TutorialRecItems: (List, 0x0, String, 0x0)
    SoulGivenOnDeath: (F32, 0x0, 0x0, 0x0)
    AttackRank: (I32, 0x0, 0x0, 0x0)
    SpellData: (List, 0x0, Embed, ToolSpellDesc)
    SearchTags: (String, 0x0, 0x0, 0x0)
    BotDefaultSpell2: (String, 0x0, 0x0, 0x0)
    BotDefaultSpell1: (String, 0x0, 0x0, 0x0)
    pass

class TftTeamPlannerViewController(ViewController):
    EmptyActiveTraitTemplate: (Hash, 0x0, 0x0, 0x0)
    MemberGrid: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    0x23d62977: (Hash, 0x0, 0x0, 0x0)
    ActiveTraitButtonTemplate: (Hash, 0x0, 0x0, 0x0)
    ActiveTraitSelectionOutline: (Hash, 0x0, 0x0, 0x0)
    ActiveTraitHighlightOutline: (Hash, 0x0, 0x0, 0x0)
    TraitLevelIconTemplates: (List, 0x0, Hash, 0x0)
    0x33f55ad2: (String, 0x0, 0x0, 0x0)
    TeamMemberData: (Embed, 0x0, 0x0, TftTeamPlannerMemberData)
    ActiveTraitGrid: (Hash, 0x0, 0x0, 0x0)
    DismissSound: (String, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    AddToTeamFailureSound: (String, 0x0, 0x0, 0x0)
    ActiveTraitDataByStyle: (Map, U32, Embed, TftTeamPlannerActiveTraitData)
    ChampionsPerRow: (U8, 0x0, 0x0, 0x0)
    0x4eb96eb2: (Hash, 0x0, 0x0, 0x0)
    ChampionHoverEffectGlowMod: (F32, 0x0, 0x0, 0x0)
    CloseButtonTemplate: (Hash, 0x0, 0x0, 0x0)
    PaginateTraitButtonTemplate: (Hash, 0x0, 0x0, 0x0)
    ActiveTraitBackground: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    ActiveTraitsBg: (Hash, 0x0, 0x0, 0x0)
    TabletOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    SnapshotButton: (Hash, 0x0, 0x0, 0x0)
    0x68b73b7b: (String, 0x0, 0x0, 0x0)
    TierData: (Embed, 0x0, 0x0, TftTeamPlannerTierData)
    TeamFullErrorDisplayTimeSecs: (F32, 0x0, 0x0, 0x0)
    TraitsPerRow: (U8, 0x0, 0x0, 0x0)
    0x7fccbc1f: (String, 0x0, 0x0, 0x0)
    TeamFullScene: (Hash, 0x0, 0x0, 0x0)
    PaginateTraitsButton: (Hash, 0x0, 0x0, 0x0)
    ViewPaneDefinition: (Embed, 0x0, 0x0, ViewPaneDefinition)
    ChampionListingData: (Embed, 0x0, 0x0, TftTeamPlannerChampionListingData)
    SnapshotTraKey: (String, 0x0, 0x0, 0x0)
    ClearAllTrakey: (String, 0x0, 0x0, 0x0)
    0xa579b2bc: (Hash, 0x0, 0x0, 0x0)
    0xa88951d0: (Hash, 0x0, 0x0, 0x0)
    ActiveTraitButton: (Hash, 0x0, 0x0, 0x0)
    TierGroupsLayout: (Hash, 0x0, 0x0, 0x0)
    ActiveTraitData: (Embed, 0x0, 0x0, TftTeamPlannerActiveTraitData)
    ActiveTraitLevelIcon: (Hash, 0x0, 0x0, 0x0)
    ActiveTraitIcon: (Hash, 0x0, 0x0, 0x0)
    ChampionButtonTemplate: (Hash, 0x0, 0x0, 0x0)
    CloseButton: (Hash, 0x0, 0x0, 0x0)
    ActiveTraitGroup: (Hash, 0x0, 0x0, 0x0)
    OpenMenuSoundPc: (String, 0x0, 0x0, 0x0)
    ClearButton: (Hash, 0x0, 0x0, 0x0)
    ClearButtonTemplate: (Hash, 0x0, 0x0, 0x0)
    0xcc043494: (Hash, 0x0, 0x0, 0x0)
    0xdcc2ec0a: (String, 0x0, 0x0, 0x0)
    ChampionsViewPane: (Hash, 0x0, 0x0, 0x0)
    0xe588b2b2: (String, 0x0, 0x0, 0x0)
    0xeb092076: (Hash, 0x0, 0x0, 0x0)
    HintText: (Hash, 0x0, 0x0, 0x0)
    0xf9d5a86b: (Hash, 0x0, 0x0, 0x0)
    pass

class DamageUnitCheat(Cheat):
    mDamageAmount: (U32, 0x0, 0x0, 0x0)
    mTarget: (U32, 0x0, 0x0, 0x0)
    mPercentageOfAttack: (F32, 0x0, 0x0, 0x0)
    mDamageType: (U32, 0x0, 0x0, 0x0)
    mHitResult: (U32, 0x0, 0x0, 0x0)
    pass

class 0xec468463(SelectSpellBlock):
    pass

class 0xec733fe2(0xe07edfa4):
    0x8bff8cdf: (U8, 0x0, 0x0, 0x0)
    pass

class ContextualConditionNeutralCampId(IContextualCondition):
    mCampId: (U8, 0x0, 0x0, 0x0)
    pass

class TftFinisherCutscene(TftCutscene):
    GameplayDuration: (F32, 0x0, 0x0, 0x0)
    ScriptName: (String, 0x0, 0x0, 0x0)
    pass

class UiChatPaneDefinition():
    MaxMessages: (U32, 0x0, 0x0, 0x0)
    ViewPaneDefinition: (Embed, 0x0, 0x0, ViewPaneDefinition)
    MessageList: (Hash, 0x0, 0x0, 0x0)
    ViewPane: (Hash, 0x0, 0x0, 0x0)
    pass

class LooseUiTextureData(LooseUiTextureDataBase, IUiEffectTextureDataProvider, IUiTextureDataProvider):
    TextureName: (String, 0x0, 0x0, 0x0)
    pass

class MultiDragonSoulSlotUiData():
    SoulSourceEmptyIcon: (Hash, 0x0, 0x0, 0x0)
    SoulIconSlot: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xeca2da9a():
    Inputs: (List2, 0x0, Pointer, ScriptTableSet)
    Outputs: (List2, 0x0, Pointer, IScriptValueGet)
    pass

class HasNNearbyVisibleUnitsRequirement(ICastRequirement):
    mUnitsRequirements: (List, 0x0, Pointer, ICastRequirement)
    mDistanceType: (U32, 0x0, 0x0, 0x0)
    mRange: (F32, 0x0, 0x0, 0x0)
    mAffectsStatusFlags: (U32, 0x0, 0x0, 0x0)
    mUnitsRequired: (U32, 0x0, 0x0, 0x0)
    mAffectsTypeFlags: (U32, 0x0, 0x0, 0x0)
    pass

class ContextualConditionAmountHealed(IContextualCondition):
    AmountHealed: (F32, 0x0, 0x0, 0x0)
    CompareOp: (U8, 0x0, 0x0, 0x0)
    pass

class VeritcalFacingMatchVelocity(VerticalFacingType):
    pass

class 0xece8d41b():
    DescriptionText: (Hash, 0x0, 0x0, 0x0)
    ProgressText: (Hash, 0x0, 0x0, 0x0)
    SecondRewardGroup: (Hash, 0x0, 0x0, 0x0)
    FirstRewardGroup: (Hash, 0x0, 0x0, 0x0)
    RewardText: (Hash, 0x0, 0x0, 0x0)
    RewardIcon: (Hash, 0x0, 0x0, 0x0)
    RewardRegion: (Hash, 0x0, 0x0, 0x0)
    SecondRewardIcon: (Hash, 0x0, 0x0, 0x0)
    SecondRewardFrame: (Hash, 0x0, 0x0, 0x0)
    RewardLayout: (Hash, 0x0, 0x0, 0x0)
    FirstRewardIcon: (Hash, 0x0, 0x0, 0x0)
    FirstRewardFrame: (Hash, 0x0, 0x0, 0x0)
    ProgressCompleteIcon: (Hash, 0x0, 0x0, 0x0)
    0xedc62dad: (Hash, 0x0, 0x0, 0x0)
    TitleText: (Hash, 0x0, 0x0, 0x0)
    pass

class IMaterialDef():
    pass

class OffscreenPlayerPipSource(IPictureInPictureSource):
    pass

class EnvironmentUnlitShadingModel(IEnvironmentShadingModel):
    pass

class 0xed070692(IScriptBlock):
    SelectedTerrain: (Embed, 0x0, 0x0, IntTableSet)
    pass

class 0xed124985(IScriptBlock):
    OverrideBehavior: (Pointer, 0x0, 0x0, IMinionWaveBehavior)
    MinionType: (U8, 0x0, 0x0, 0x0)
    pass

class StatStoneData(BaseLoadoutData):
    MilestoneData: (Embed, 0x0, 0x0, MilestoneData)
    IsRetired: (Bool, 0x0, 0x0, 0x0)
    IsDuration: (Bool, 0x0, 0x0, 0x0)
    MilestoneForFullLitImage: (U32, 0x0, 0x0, 0x0)
    TrackingType: (U8, 0x0, 0x0, 0x0)
    Milestones: (List, 0x0, U64, 0x0)
    EpicStatStone: (Bool, 0x0, 0x0, 0x0)
    NameTraKey: (String, 0x0, 0x0, 0x0)
    mStatLogic: (Pointer, 0x0, 0x0, IStatStoneLogicDriver)
    StoneName: (String, 0x0, 0x0, 0x0)
    TriggeredFromScript: (Bool, 0x0, 0x0, 0x0)
    EventsToTrack: (List, 0x0, Embed, StatStoneEventToTrack)
    DataCollectionOnly: (Bool, 0x0, 0x0, 0x0)
    Category: (Link, 0x0, 0x0, StatStoneCategory)
    DarkLaunch: (Bool, 0x0, 0x0, 0x0)
    mChatEntry: (String, 0x0, 0x0, 0x0)
    mEventToTrack: (U32, 0x0, 0x0, 0x0)
    MilestoneForHalfLitImage: (U32, 0x0, 0x0, 0x0)
    StatFilters: (List, 0x0, Pointer, IStatStoneLogicDriver)
    pass

class 0xed4b858b():
    pass

class ViewController():
    PathHashToSelf: (File, 0x0, 0x0, 0x0)
    ThemeMusicState: (String, 0x0, 0x0, 0x0)
    mBackViewControllerLink: (Link, 0x0, 0x0, ViewController)
    ThemeMusicStateGroup: (String, 0x0, 0x0, 0x0)
    pass

class 0xed76e0cf(ISequenceAction):
    SoundEvent: (String, 0x0, 0x0, 0x0)
    pass

class CherryCameo():
    Enabled: (Bool, 0x0, 0x0, 0x0)
    0x3942d706: (String, 0x0, 0x0, 0x0)
    SkinId: (U32, 0x0, 0x0, 0x0)
    ChampionName: (String, 0x0, 0x0, 0x0)
    0xbe8164b4: (String, 0x0, 0x0, 0x0)
    ChampionNameHash: (Hash, 0x0, 0x0, 0x0)
    0xf426fde9: (String, 0x0, 0x0, 0x0)
    pass

class FunctionDefinition():
    InputParameters: (List, 0x0, Hash, 0x0)
    InputParameters: (List, 0x0, String, 0x0)
    Sequence: (Embed, 0x0, 0x0, ScriptSequence)
    OutputParameters: (List, 0x0, Hash, 0x0)
    OutputParameters: (List, 0x0, String, 0x0)
    FunctionDef: (Embed, 0x0, 0x0, 0xeca2da9a)
    pass

class MultiKillLogic(IStatStoneLogicDriver):
    pass

class ConfigFloat():
    Enabler: (Link, 0x0, 0x0, IEnabler)
    Value: (F32, 0x0, 0x0, 0x0)
    pass

class NotificationsViewPanelController(ViewController):
    ClearAllButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class FloatTableGet(RsTableGet, ScriptTableGet, TableGet, IFloatGet):
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Var: (Hash, 0x0, 0x0, 0x0)
    Var: (String, 0x0, 0x0, 0x0)
    Default: (Option, 0x0, F32, 0x0)
    pass

class CssIcon():
    XY: (Vec2, 0x0, 0x0, 0x0)
    Wh: (Vec2, 0x0, 0x0, 0x0)
    YAdjustment: (F32, 0x0, 0x0, 0x0)
    pass

class EsportsData():
    SummonerIconToTeamLookup: (Map, U32, Link, EsportsTeamData)
    Leagues: (List, 0x0, String, 0x0)
    pass

class FunctionModule(GameScript):
    pass

class TargetTypeFilter(IStatStoneLogicDriver):
    MinionsAreValid: (Bool, 0x0, 0x0, 0x0)
    ChampionsAreValid: (Bool, 0x0, 0x0, 0x0)
    TurretsAreValid: (Bool, 0x0, 0x0, 0x0)
    pass

class CursorConfig():
    mHoverNotUseableCursor: (Embed, 0x0, 0x0, CursorDataCaptureCooldownContext)
    mTeamContextCursors: (List, 0x3, Embed, CursorDataTeamContext)
    mSingleContextCursors: (List, 0xa, Embed, CursorData)
    pass

class TargeterDefinitionSkipTerrain(TargeterDefinition):
    mBaseTextureName: (String, 0x0, 0x0, 0x0)
    mTargetTextureName: (String, 0x0, 0x0, 0x0)
    mTerrainTextureName: (String, 0x0, 0x0, 0x0)
    mEndLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    mFallbackDirection: (U32, 0x0, 0x0, 0x0)
    mTargetTextureRadius: (F32, 0x0, 0x0, 0x0)
    mStartLocator: (Embed, 0x0, 0x0, DrawablePositionLocator)
    pass

class 0xee28fb8d():
    DetailedStatName: (Hash, 0x0, 0x0, 0x0)
    DetailedStatTra: (String, 0x0, 0x0, 0x0)
    DetailedHoverRegion: (Hash, 0x0, 0x0, 0x0)
    DetailedGroup: (Hash, 0x0, 0x0, 0x0)
    0xab77f602: (Hash, 0x0, 0x0, 0x0)
    DetailedStatAmount: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xee39916f(IVfxShape):
    EmitOffset: (Vec3, 0x0, 0x0, 0x0)
    pass

class VfxSimpleEmitterDefinitionData():
    DoesParticleLifetimeScale: (Bool, 0x0, 0x0, 0x0)
    KeywordsRequired: (List, 0x0, String, 0x0)
    VoiceOverPersistentName: (String, 0x0, 0x0, 0x0)
    TimeActiveDuringPeriod: (Option, 0x0, F32, 0x0)
    BirthRotationalVelocity: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    ScaleEmitOffsetByBoundObjectHeight: (F32, 0x0, 0x0, 0x0)
    NumFrames: (I32, 0x0, 0x0, 0x0)
    Rotation: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    TimeBeforeFirstEmission: (F32, 0x0, 0x0, 0x0)
    ParticleLinger: (F32, 0x0, 0x0, 0x0)
    ColorLookUpTypeX: (U32, 0x0, 0x0, 0x0)
    UvMode: (U32, 0x0, 0x0, 0x0)
    ColorLookUpTypeY: (U32, 0x0, 0x0, 0x0)
    IsGroundLayer: (Bool, 0x0, 0x0, 0x0)
    ProjectionYRange: (F32, 0x0, 0x0, 0x0)
    ParticleLifetime: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    IsLocalOrientation: (Bool, 0x0, 0x0, 0x0)
    FlexScaleBirthScale: (Embed, 0x0, 0x0, FlexTypeFloat)
    MaterialOverrideDefinitions: (List, 0x0, Pointer, VfxMaterialOverrideDefinitionData)
    HasFixedOrbit: (Bool, 0x0, 0x0, 0x0)
    ParticleIsLocalOrientation: (Bool, 0x0, 0x0, 0x0)
    ScaleBirthScaleByBoundObjectRadius: (F32, 0x0, 0x0, 0x0)
    EmitterLinger: (F32, 0x0, 0x0, 0x0)
    Texture: (String, 0x0, 0x0, 0x0)
    EmitterName: (String, 0x0, 0x0, 0x0)
    DistortionMode: (U32, 0x0, 0x0, 0x0)
    QuadType: (U32, 0x0, 0x0, 0x0)
    IsSingleParticle: (Bool, 0x0, 0x0, 0x0)
    ScaleBias: (Vec2, 0x0, 0x0, 0x0)
    KeywordsIncluded: (List, 0x0, String, 0x0)
    TextureAddressModeBase: (U32, 0x0, 0x0, 0x0)
    BirthScale: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    ParticleBind: (Vec2, 0x0, 0x0, 0x0)
    VoiceOverOnCreateName: (String, 0x0, 0x0, 0x0)
    Lifetime: (Option, 0x0, F32, 0x0)
    ModulationFactor: (Vec4, 0x0, 0x0, 0x0)
    FlexParticleLifetime: (Embed, 0x0, 0x0, FlexValueFloat)
    FluidDynamicsDefinition: (Pointer, 0x0, 0x0, 0xe6cd2142)
    ProjectionFading: (F32, 0x0, 0x0, 0x0)
    StartFrame: (I32, 0x0, 0x0, 0x0)
    FlexRate: (Embed, 0x0, 0x0, FlexValueFloat)
    FlexScaleEmitOffset: (Embed, 0x0, 0x0, FlexTypeFloat)
    DoesLifetimeScale: (Bool, 0x0, 0x0, 0x0)
    ScaleEmitOffsetByBoundObjectRadius: (F32, 0x0, 0x0, 0x0)
    Pass: (I32, 0x0, 0x0, 0x0)
    EmitRotationAngles: (List, 0x0, Embed, VfxAnimatedFloatVariableData)
    Scale: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    TexDiv: (Vec2, 0x0, 0x0, 0x0)
    FlexBirthTranslation: (Embed, 0x0, 0x0, FlexValueVector3)
    SoundOnCreateName: (String, 0x0, 0x0, 0x0)
    ScaleBirthScaleByBoundObjectSize: (F32, 0x0, 0x0, 0x0)
    AnimationName: (String, 0x0, 0x0, 0x0)
    LockedToEmitter: (Bool, 0x0, 0x0, 0x0)
    Period: (Option, 0x0, F32, 0x0)
    SoundPersistentName: (String, 0x0, 0x0, 0x0)
    FrameRate: (F32, 0x0, 0x0, 0x0)
    BirthRotation: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    FlexBirthVelocity: (Embed, 0x0, 0x0, FlexValueVector3)
    FalloffTexture: (String, 0x0, 0x0, 0x0)
    SliceTechniqueRange: (F32, 0x0, 0x0, 0x0)
    UvScrollClamp: (Bool, 0x0, 0x0, 0x0)
    MeshDisableBackfaceCull: (Bool, 0x0, 0x0, 0x0)
    FieldCollectionDefinition: (Embed, 0x0, 0x0, VfxFieldCollectionDefinitionData)
    Rate: (Embed, 0x0, 0x0, VfxAnimatedFloatVariableData)
    DoesCastShadow: (Bool, 0x0, 0x0, 0x0)
    ParticleColorTexture: (String, 0x0, 0x0, 0x0)
    Importance: (U32, 0x0, 0x0, 0x0)
    AlphaRef: (I32, 0x0, 0x0, 0x0)
    IsFollowingTerrain: (Bool, 0x0, 0x0, 0x0)
    Distortion: (F32, 0x0, 0x0, 0x0)
    FixedOrbitType: (U32, 0x0, 0x0, 0x0)
    SoftParticleParams: (Embed, 0x0, 0x0, VfxSoftParticleDefinitionData)
    ScaleEmitOffsetByBoundObjectSize: (F32, 0x0, 0x0, 0x0)
    KeywordsExcluded: (List, 0x0, String, 0x0)
    Orientation: (U32, 0x0, 0x0, 0x0)
    RenderFlags: (U32, 0x0, 0x0, 0x0)
    IsTexturePixelated: (Bool, 0x0, 0x0, 0x0)
    ColorLookUpOffsets: (Vec2, 0x0, 0x0, 0x0)
    UvScrollRate: (Vec2, 0x0, 0x0, 0x0)
    EmitRotationAxes: (List, 0x0, Vec3, 0x0)
    IsDirectionOriented: (Bool, 0x0, 0x0, 0x0)
    IsRandomStartFrame: (Bool, 0x0, 0x0, 0x0)
    FlexOffset: (Embed, 0x0, 0x0, FlexValueVector3)
    EmitOffset: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    ScaleBirthScaleByBoundObjectHeight: (F32, 0x0, 0x0, 0x0)
    NormalMapTexture: (String, 0x0, 0x0, 0x0)
    MeshSkeletonName: (String, 0x0, 0x0, 0x0)
    ColorLookUpScales: (Vec2, 0x0, 0x0, 0x0)
    ScaleAlongMovementVector: (F32, 0x0, 0x0, 0x0)
    SimpleMeshName: (String, 0x0, 0x0, 0x0)
    MeshName: (String, 0x0, 0x0, 0x0)
    ScaleUpFromOrigin: (Bool, 0x0, 0x0, 0x0)
    BirthVelocity: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    ExcludedAttachmentTypes: (List, 0x0, String, 0x0)
    BlendMode: (I32, 0x0, 0x0, 0x0)
    RotationIsEnabled: (Bool, 0x0, 0x0, 0x0)
    BirthTranslation: (Embed, 0x0, 0x0, VfxAnimatedVector3fVariableData)
    FlexBirthRotationalVelocity: (Embed, 0x0, 0x0, FlexValueFloat)
    FluidPartName: (String, 0x0, 0x0, 0x0)
    pass

class FacingParametricUpdater(IFloatParametricUpdater):
    pass

class UvScaleBiasFromAnimationDynamicMaterialDriver(IDynamicMaterialDriver, ILogicDriver):
    mSubMeshName: (String, 0x0, 0x0, 0x0)
    mUvAnimIndex: (U32, 0x0, 0x0, 0x0)
    pass

class OptionItemFilter_Mutator(IOptionItemFilter):
    Mutator: (String, 0x0, 0x0, 0x0)
    pass

class EffectGlowElementData(EffectElementData):
    BaseScale: (F32, 0x0, 0x0, 0x0)
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    0x56a13f9a: (F32, 0x0, 0x0, 0x0)
    MinimumAlpha: (F32, 0x0, 0x0, 0x0)
    0x9240004a: (F32, 0x0, 0x0, 0x0)
    0xadbdad5b: (F32, 0x0, 0x0, 0x0)
    CycleBasedScaleAddition: (F32, 0x0, 0x0, 0x0)
    CycleTime: (F32, 0x0, 0x0, 0x0)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    0xf64230: (F32, 0x0, 0x0, 0x0)
    pass

class AugmentSlotData():
    AugmentIconBackground: (Hash, 0x0, 0x0, 0x0)
    AugmentGroup: (Hash, 0x0, 0x0, 0x0)
    AugmentPickedVfx: (Hash, 0x0, 0x0, 0x0)
    0x4ddb7d67: (Hash, 0x0, 0x0, 0x0)
    AugmentDescription: (Hash, 0x0, 0x0, 0x0)
    AugmentRefreshVfx: (Hash, 0x0, 0x0, 0x0)
    AugmentNotPickedVfx: (Hash, 0x0, 0x0, 0x0)
    AugmentIcon: (Hash, 0x0, 0x0, 0x0)
    AugmentIdleVfx: (Hash, 0x0, 0x0, 0x0)
    AugmentName: (Hash, 0x0, 0x0, 0x0)
    AugmentIconMedium: (Hash, 0x0, 0x0, 0x0)
    AugmentHoverVfx: (Hash, 0x0, 0x0, 0x0)
    AugmentDisplayTagData: (Embed, 0x0, 0x0, AugmentDisplayTagData)
    AugmentIconLarge: (Hash, 0x0, 0x0, 0x0)
    AugmentRefreshOverlayVfx: (Hash, 0x0, 0x0, 0x0)
    AugmentButton: (Hash, 0x0, 0x0, 0x0)
    pass

class TimedWaveBehaviorInfo():
    StartTimeSecs: (I32, 0x0, 0x0, 0x0)
    Behavior: (Pointer, 0x0, 0x0, IMinionWaveBehavior)
    pass

class ContextualConditionItemCanBePurchased(IContextualCondition):
    mItemCanBePurchased: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xeea0bf1(ISkinAugmentModifier):
    0x629c2476: (String, 0x0, 0x0, 0x0)
    0x7679ee15: (String, 0x0, 0x0, 0x0)
    0xa3ab316a: (String, 0x0, 0x0, 0x0)
    0xc29fd86f: (String, 0x0, 0x0, 0x0)
    pass

class TargetCatFrameVisibilityKey(IScriptBlock, IBehaviorScriptBlock):
    Sequence: (Embed, 0x0, 0x0, ScriptBtRandomWeightedSelector)
    Percentages: (List2, 0x0, Pointer, IIntGet)
    pass

class AttackCausedDamageConstraintInfo(ListenerConstraintInfo):
    DamageThresholdRequired: (F32, 0x0, 0x0, 0x0)
    pass

class TftPlayerPlacementDynamicMaterialFloatDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    UseOpponentPlacement: (Bool, 0x0, 0x0, 0x0)
    pass

class TextureAndColorData():
    ColorblindTextureFile: (Option, 0x0, String, 0x0)
    ColorblindTextureFile: (String, 0x0, 0x0, 0x0)
    Color: (Color, 0x0, 0x0, 0x0)
    TextureFile: (String, 0x0, 0x0, 0x0)
    ColorblindColor: (Option, 0x0, Color, 0x0)
    pass

class MapDynamicLighting(MapGraphicsFeature):
    0x2451a0b: (Bool, 0x0, 0x0, 0x0)
    0xb41ddb79: (Bool, 0x0, 0x0, 0x0)
    0xed17c5c8: (Bool, 0x0, 0x0, 0x0)
    pass

class TftCompanionBucket():
    Companions: (List, 0x0, Hash, 0x0)
    pass

class AiSpellData():
    mSpeed: (F32, 0x0, 0x0, 0x0)
    mSendAiEvent: (Bool, 0x0, 0x0, 0x0)
    mRadius: (F32, 0x0, 0x0, 0x0)
    mRange: (F32, 0x0, 0x0, 0x0)
    mBlockLevel: (U8, 0x0, 0x0, 0x0)
    mEndOnly: (Bool, 0x0, 0x0, 0x0)
    mLifetime: (F32, 0x0, 0x0, 0x0)
    pass

class TftCutsceneTftCamClip(TftCutsceneClip):
    AssociatedPlayers: (List2, 0x0, String, 0x0)
    OverrideFov: (Bool, 0x0, 0x0, 0x0)
    0x24271739: (Bool, 0x0, 0x0, 0x0)
    BlackboardCameraBone: (String, 0x0, 0x0, 0x0)
    0x4e6a18f2: (Bool, 0x0, 0x0, 0x0)
    NearClipPlane: (F32, 0x0, 0x0, 0x0)
    0x7a57b83: (String, 0x0, 0x0, 0x0)
    BlackboardFovBone: (String, 0x0, 0x0, 0x0)
    FarClipPlane: (F32, 0x0, 0x0, 0x0)
    0xfb8cc774: (F32, 0x0, 0x0, 0x0)
    pass

class HudItemShopItemIconDefinition():
    LockedHoverIcon: (Hash, 0x0, 0x0, 0x0)
    LockedHoverIcon: (Link, 0x0, 0x0, BaseElementData)
    OffsetRegion: (Hash, 0x0, 0x0, 0x0)
    OffsetRegion: (Link, 0x0, 0x0, BaseElementData)
    CostTextSelected: (Hash, 0x0, 0x0, 0x0)
    CostTextSelected: (Link, 0x0, 0x0, BaseElementData)
    PopularIcon: (Hash, 0x0, 0x0, 0x0)
    PopularIcon: (Link, 0x0, 0x0, BaseElementData)
    CooldownEffectData: (Embed, 0x0, 0x0, CooldownEffectUiData)
    OrnnFrame: (Hash, 0x0, 0x0, 0x0)
    OrnnFrame: (Link, 0x0, 0x0, BaseElementData)
    RecentlyChangedIcon: (Hash, 0x0, 0x0, 0x0)
    RecentlyChangedIcon: (Link, 0x0, 0x0, BaseElementData)
    MythicPurchaseableVfx: (Hash, 0x0, 0x0, 0x0)
    MythicPurchaseableVfx: (Link, 0x0, 0x0, BaseElementData)
    PurchaseableVfx: (Hash, 0x0, 0x0, 0x0)
    PurchaseableVfx: (Link, 0x0, 0x0, BaseElementData)
    MythicFrameIcon: (Hash, 0x0, 0x0, 0x0)
    MythicFrameIcon: (Link, 0x0, 0x0, BaseElementData)
    SelectedIcon: (Hash, 0x0, 0x0, 0x0)
    SelectedIcon: (Link, 0x0, 0x0, BaseElementData)
    PurchasedOverlay: (Hash, 0x0, 0x0, 0x0)
    PurchasedOverlay: (Link, 0x0, 0x0, BaseElementData)
    FrameIcon: (Hash, 0x0, 0x0, 0x0)
    FrameIcon: (Link, 0x0, 0x0, BaseElementData)
    MythicPurchasedVfx: (Hash, 0x0, 0x0, 0x0)
    MythicPurchasedVfx: (Link, 0x0, 0x0, BaseElementData)
    HoverFrameIcon: (Hash, 0x0, 0x0, 0x0)
    HoverFrameIcon: (Link, 0x0, 0x0, BaseElementData)
    LockedIcon: (Hash, 0x0, 0x0, 0x0)
    LockedIcon: (Link, 0x0, 0x0, BaseElementData)
    CostTextUnpurchaseable: (Hash, 0x0, 0x0, 0x0)
    CostTextUnpurchaseable: (Link, 0x0, 0x0, BaseElementData)
    NameText: (Hash, 0x0, 0x0, 0x0)
    NameText: (Link, 0x0, 0x0, BaseElementData)
    HoverIcon: (Hash, 0x0, 0x0, 0x0)
    HoverIcon: (Link, 0x0, 0x0, BaseElementData)
    ItemIcon: (Hash, 0x0, 0x0, 0x0)
    ItemIcon: (Link, 0x0, 0x0, BaseElementData)
    SelectedVfx: (Hash, 0x0, 0x0, 0x0)
    SelectedVfx: (Link, 0x0, 0x0, BaseElementData)
    UnpurchaseableOverlay: (Hash, 0x0, 0x0, 0x0)
    UnpurchaseableOverlay: (Link, 0x0, 0x0, BaseElementData)
    CostText: (Hash, 0x0, 0x0, 0x0)
    CostText: (Link, 0x0, 0x0, BaseElementData)
    HitRegion: (Hash, 0x0, 0x0, 0x0)
    HitRegion: (Link, 0x0, 0x0, BaseElementData)
    pass

class UiPerkSummonerSpecialistToggles():
    Scene: (Hash, 0x0, 0x0, 0x0)
    ToggleButtons: (List, 0x2, Hash, 0x0)
    SelectorMenu: (Embed, 0x0, 0x0, UiPerkSummonerSpecialistSelector)
    pass

class UiMetricUnitKda(UiMetricUnitTypeI, UiMetricUnitTypeSimpleI):
    ShowDisguise: (Bool, 0x0, 0x0, 0x0)
    KdaText: (Hash, 0x0, 0x0, 0x0)
    KdaIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class TouchOverlayViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TouchFeedbackElement: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xef339ef9(0xf9e5b8b9):
    Multiplier: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class DynamicMaterialStaticSwitch():
    Enabled: (Bool, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    Driver: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    Driver: (Pointer, 0x0, 0x0, IDynamicMaterialBoolDriver)
    pass

class ResourceResolver(BaseResourceResolver):
    pass

class CursorDataTeamContext():
    mData: (List, 0x3, Embed, CursorData)
    pass

class ObjectiveVoteData():
    ForIcon: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    PendingIcon: (Hash, 0x0, 0x0, 0x0)
    PlayerRejectIcon: (Hash, 0x0, 0x0, 0x0)
    RejectIcon: (Hash, 0x0, 0x0, 0x0)
    PlayerForIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class NeutralTimerElements():
    TimerText: (Hash, 0x0, 0x0, 0x0)
    VoteForButton: (Hash, 0x0, 0x0, 0x0)
    VoteStartTimeBeforeSpawn: (F32, 0x0, 0x0, 0x0)
    DeadIcon: (Hash, 0x0, 0x0, 0x0)
    AliveIcon: (Hash, 0x0, 0x0, 0x0)
    Backdrop: (Hash, 0x0, 0x0, 0x0)
    VoteReject: (Hash, 0x0, 0x0, 0x0)
    pass

class PropertyLoadable():
    FilepathHash: (File, 0x0, 0x0, 0x0)
    pass

class 0xefe2309(IVectorGet, IScriptValueGet):
    MapPlaceable: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xeff830de():
    Behaviors: (List2, 0x0, Pointer, 0x64c18f7d)
    Condition: (Pointer, 0x0, 0x0, 0x26d26471)
    pass

class DestroyChildrenOnMovementCompleteSpec(MissileBehaviorSpec):
    mDelay: (I32, 0x0, 0x0, 0x0)
    pass

class LooseUiTextureData3SliceH(LooseUiTextureDataBase, LooseUiTextureData):
    LeftRightWidths: (Vec2, 0x0, 0x0, 0x0)
    EdgeSizes: (Vec2, 0x0, 0x0, 0x0)
    EdgeSizesLeftRight: (Vec2, 0x0, 0x0, 0x0)
    pass

class 0xf008d4c9(0xd97f9bd3):
    TimeToTarget: (F32, 0x0, 0x0, 0x0)
    pass

class SinusoidalHeightSolver(HeightSolverType):
    mVerticalOffset: (F32, 0x0, 0x0, 0x0)
    mAmplitude: (F32, 0x0, 0x0, 0x0)
    mNumberOfPeriods: (F32, 0x0, 0x0, 0x0)
    PhaseShift: (F32, 0x0, 0x0, 0x0)
    pass

class 0xf00f3333(0x288b8edc):
    pass

class 0xf01e253c():
    0x18c1cf54: (U32, 0x0, 0x0, 0x0)
    0x20e00ac7: (List2, 0x0, Hash, 0x0)
    0x490b09: (U32, 0x0, 0x0, 0x0)
    JungleItems: (List2, 0x0, Hash, 0x0)
    JunglePlayerBuffs: (List2, 0x0, Hash, 0x0)
    0x77936f56: (List2, 0x0, Hash, 0x0)
    GainedReplay: (List2, 0x0, Hash, 0x0)
    0x92ac2c5f: (F32, 0x0, 0x0, 0x0)
    0xa5084a86: (F32, 0x0, 0x0, 0x0)
    JunglePlayerWeight: (F32, 0x0, 0x0, 0x0)
    0xca245131: (List2, 0x0, Hash, 0x0)
    pass

class 0xf02f881():
    ChallengePlayerLevel: (Hash, 0x0, 0x0, 0x0)
    ChallengePlayerLevelIcon: (Hash, 0x0, 0x0, 0x0)
    PlayerName: (Hash, 0x0, 0x0, 0x0)
    0xee313940: (Hash, 0x0, 0x0, 0x0)
    pass

class TftSellArea():
    DefaultSceneHandle: (Hash, 0x0, 0x0, 0x0)
    HoverSceneHandle: (Hash, 0x0, 0x0, 0x0)
    HitTargetHandle: (Hash, 0x0, 0x0, 0x0)
    SellTextHandle: (Hash, 0x0, 0x0, 0x0)
    SceneHandle: (Hash, 0x0, 0x0, 0x0)
    pass

class StringTableGet(RsTableGet, ScriptTableGet, IStringGet, TableGet, IStringHashGet):
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Var: (Hash, 0x0, 0x0, 0x0)
    Var: (String, 0x0, 0x0, 0x0)
    Default: (Option, 0x0, String, 0x0)
    pass

class UiElementRegion(UiElement):
    pass

class TftPassRepeatInfo():
    Count: (I32, 0x0, 0x0, 0x0)
    RepeatLevels: (List2, 0x0, Embed, TftPassLevel)
    Multiplier: (F32, 0x0, 0x0, 0x0)
    pass

class ChallengeMapAreaGroupCheck():
    AreasToCheck: (List, 0x0, U32, 0x0)
    AreaCheckQuantifier: (U32, 0x0, 0x0, 0x0)
    pass

class ExperienceModData():
    mPlayerMinionSplitXp: (List, 0x0, F32, 0x0)
    pass

class LogicDriverViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    ViewEntries: (List, 0x0, Embed, LogicDriverViewEntry)
    Loadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TransitionOnState: (Hash, 0x0, 0x0, 0x0)
    EnableCondition: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    TransitionOffState: (Hash, 0x0, 0x0, 0x0)
    pass

class TftUnitAttachmentLargeSlotData():
    Text: (Hash, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class BarracksDampenerCommon(AnimatedBuilding):
    pass

class TrophyPedestalData(BaseLoadoutData):
    mTierTraKey: (String, 0x0, 0x0, 0x0)
    mName: (String, 0x0, 0x0, 0x0)
    SkinMeshProperties: (Embed, 0x0, 0x0, SkinMeshDataProperties)
    mSkinMeshProperties: (Embed, 0x0, 0x0, SkinMeshDataProperties)
    mPedestalId: (U32, 0x0, 0x0, 0x0)
    mAnimationGraphData: (Link, 0x0, 0x0, AnimationGraphData)
    mJointName: (String, 0x0, 0x0, 0x0)
    mImage: (String, 0x0, 0x0, 0x0)
    AnimationGraphData: (Link, 0x0, 0x0, AnimationGraphData)
    pass

class GameModeEventDefinition():
    EventCardDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxPrimitiveCameraSegmentBeam(VfxPrimitiveBeamBase):
    pass

class EffectMaskElementData(EffectElementData):
    0x74d50d7a: (String, 0x0, 0x0, 0x0)
    MaskTexture: (String, 0x0, 0x0, 0x0)
    pass

class LolModesPhaseData():
    0x44bdfcf8: (String, 0x0, 0x0, 0x0)
    Type: (U8, 0x0, 0x0, 0x0)
    DisplayNameTra: (String, 0x0, 0x0, 0x0)
    0x7011dd78: (String, 0x0, 0x0, 0x0)
    Subphases: (List, 0x0, Embed, LolModesSubphaseData)
    0xbafc35cb: (String, 0x0, 0x0, 0x0)
    pass

class EnterFowVisibilitySpec(MissileVisibilitySpec):
    mMissileClientWaitForTargetUpdateBeforeMissileShow: (Bool, 0x0, 0x0, 0x0)
    mMissileClientExitFowPrediction: (Bool, 0x0, 0x0, 0x0)
    pass

class RelicDropScenario():
    0x44178a50: (List, 0x0, Link, RelicList)
    0x47178f09: (List, 0x0, Link, RelicList)
    mDropNumber: (U32, 0x0, 0x0, 0x0)
    mDropType: (String, 0x0, 0x0, 0x0)
    0xabdeade2: (U32, 0x0, 0x0, 0x0)
    0xb12acf0d: (Bool, 0x0, 0x0, 0x0)
    0xddd65460: (Option, 0x0, F32, 0x0)
    pass

class SpawnAiTurret(LevelScriptBlock):
    0x29bec30a: (Hash, 0x0, 0x0, 0x0)
    AiUnitName: (String, 0x0, 0x0, 0x0)
    Lane: (U16, 0x0, 0x0, 0x0)
    AiGroupName: (Hash, 0x0, 0x0, 0x0)
    Position: (U16, 0x0, 0x0, 0x0)
    0x96cbc77d: (Hash, 0x0, 0x0, 0x0)
    Team: (U32, 0x0, 0x0, 0x0)
    MapObjectName: (String, 0x0, 0x0, 0x0)
    pass

class BotsSpellData():
    0x38382c53: (List2, 0x0, Embed, 0x150d1b92)
    DamageTag: (U32, 0x0, 0x0, 0x0)
    0x61c10808: (U32, 0x0, 0x0, 0x0)
    0x6d548702: (Pointer, 0x0, 0x0, IGameCalculation)
    0xec17e271: (List2, 0x0, Embed, 0xb09016f6)
    pass

class SpawnOnCreate(MissileGroupSpawner):
    pass

class InstanceVarsTable(ScriptTable):
    pass

class VotePanelViewController(ViewController):
    YesButton: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    NoButton: (Hash, 0x0, 0x0, 0x0)
    TimerBar: (Hash, 0x0, 0x0, 0x0)
    StatusText: (Hash, 0x0, 0x0, 0x0)
    VoteIcon: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xf1cf8988(0x8b33cf88):
    Source: (Link, 0x0, 0x0, SequenceObjectSelector)
    DebugOverride: (U32, 0x0, 0x0, 0x0)
    pass

class 0xf1fd1323():
    0x53d20c62: (Hash, 0x0, 0x0, 0x0)
    0xa8dd5e13: (Hash, 0x0, 0x0, 0x0)
    0xb63628: (Hash, 0x0, 0x0, 0x0)
    0xd98c2482: (Embed, 0x0, 0x0, 0x51db35d3)
    pass

class InputControlSet():
    Events: (List2, 0x0, Link, InputEventBase)
    MutuallyExlusiveSets: (List2, 0x0, Link, InputControlSet)
    Name: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xf252334a(0x2755f1f9):
    OuterRadius: (F32, 0x0, 0x0, 0x0)
    InnerRadius: (F32, 0x0, 0x0, 0x0)
    pass

class TftDropRateTable():
    0x4f7d4b97: (I8, 0x0, 0x0, 0x0)
    mDropRatesByLevel: (List, 0x0, Embed, TftDropRates)
    pass

class LuaTableData():
    Properties: (List, 0x0, Embed, LuaPropertyDataEntry)
    pass

class SubmeshVisibilityBoolDriver(ILogicBoolDriver):
    Visible: (Bool, 0x0, 0x0, 0x0)
    AnySubmesh: (Bool, 0x0, 0x0, 0x0)
    Submeshes: (List, 0x0, Hash, 0x0)
    pass

class ScoreLineSpellSlots():
    SummonerSpell1: (Embed, 0x0, 0x0, SpellSlotSimpleUiDefinition)
    SummonerSpell2: (Embed, 0x0, 0x0, SpellSlotSimpleUiDefinition)
    pass

class MouseOverEffectData():
    mInteractionSizes: (List, 0x4, I32, 0x0)
    mAvatarBlurPassCount: (U32, 0x0, 0x0, 0x0)
    mInteractionTimes: (List, 0x4, F32, 0x0)
    mEnemyColor: (Color, 0x0, 0x0, 0x0)
    mAllyColor: (Color, 0x0, 0x0, 0x0)
    mSelfColor: (Color, 0x0, 0x0, 0x0)
    mSelectedBlurPassCount: (U32, 0x0, 0x0, 0x0)
    mKillerColorFactor: (F32, 0x0, 0x0, 0x0)
    mSelectedColorFactor: (F32, 0x0, 0x0, 0x0)
    mAvatarSize: (I32, 0x0, 0x0, 0x0)
    mSelectedSize: (I32, 0x0, 0x0, 0x0)
    mMouseOverColorFactor: (F32, 0x0, 0x0, 0x0)
    mAvatarColor: (Color, 0x0, 0x0, 0x0)
    mMouseOverBlurPassCount: (U32, 0x0, 0x0, 0x0)
    mMouseOverSize: (I32, 0x0, 0x0, 0x0)
    mKillerBlurPassCount: (U32, 0x0, 0x0, 0x0)
    mKillerSize: (I32, 0x0, 0x0, 0x0)
    mAvatarColorFactor: (F32, 0x0, 0x0, 0x0)
    mNeutralColor: (Color, 0x0, 0x0, 0x0)
    pass

class StoreCategoryButtonDefinition():
    Button: (Hash, 0x0, 0x0, 0x0)
    Category: (U32, 0x0, 0x0, 0x0)
    NewPip: (Embed, 0x0, 0x0, 0x6241da2)
    ButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class MapActionSetVisibilityFlag(MapAction):
    TransitionTime: (F32, 0x0, 0x0, 0x0)
    OperationType: (U8, 0x0, 0x0, 0x0)
    VisibilityFlags: (U8, 0x0, 0x0, 0x0)
    pass

class TftDropRates():
    mDropRatesByTier: (List, 0x5, F32, 0x0)
    0xbcf1e6a6: (List2, 0x0, F32, 0x0)
    pass

class ParametricClipData(BlendableClipData, ClipBaseData):
    Updater: (Pointer, 0x0, 0x0, IBaseParametricUpdater)
    mUpdaterType: (U32, 0x0, 0x0, 0x0)
    mMaskData: (Link, 0x0, 0x0, MaskData)
    mParametricPairDataList: (List, 0x0, Embed, ParametricPairData)
    mMaskDataName: (Hash, 0x0, 0x0, 0x0)
    mTrackData: (Link, 0x0, 0x0, TrackData)
    mTrackDataName: (Hash, 0x0, 0x0, 0x0)
    pass

class FeatureAudioDataProperties():
    Bank: (List, 0x0, String, 0x0)
    BankAssetPath: (List, 0x0, String, 0x0)
    Music: (Embed, 0x0, 0x0, MusicAudioDataProperties)
    Feature: (Hash, 0x0, 0x0, 0x0)
    BankUnits: (List, 0x0, Embed, BankUnit)
    BankUnits: (List2, 0x0, Embed, BankUnit)
    pass

class 0xf2bc55fb():
    Color: (Color, 0x0, 0x0, 0x0)
    Elements: (List, 0x0, Hash, 0x0)
    pass

class 0xf2c8525d(0x114828a9):
    Axis: (Vec2, 0x0, 0x0, 0x0)
    GapWidth: (F32, 0x0, 0x0, 0x0)
    SideLength: (F32, 0x0, 0x0, 0x0)
    pass

class MissionBuffData():
    FireDrake: (Embed, 0x0, 0x0, TeamBuffData)
    AirDrake: (Embed, 0x0, 0x0, TeamBuffData)
    EarthDrake: (Embed, 0x0, 0x0, TeamBuffData)
    ElderDrake: (Embed, 0x0, 0x0, TeamBuffData)
    WaterDrake: (Embed, 0x0, 0x0, TeamBuffData)
    GameModeCustom9: (Embed, 0x0, 0x0, TeamBuffData)
    GameModeCustom8: (Embed, 0x0, 0x0, TeamBuffData)
    GameModeCustom3: (Embed, 0x0, 0x0, TeamBuffData)
    GameModeCustom2: (Embed, 0x0, 0x0, TeamBuffData)
    GameModeCustom1: (Embed, 0x0, 0x0, TeamBuffData)
    GameModeCustom7: (Embed, 0x0, 0x0, TeamBuffData)
    GameModeCustom6: (Embed, 0x0, 0x0, TeamBuffData)
    GameModeCustom5: (Embed, 0x0, 0x0, TeamBuffData)
    GameModeCustom4: (Embed, 0x0, 0x0, TeamBuffData)
    GameModeCustom10: (Embed, 0x0, 0x0, TeamBuffData)
    Dragon: (Embed, 0x0, 0x0, TeamBuffData)
    pass

class UiSliderBarState():
    BarBackdrop: (Link, 0x0, 0x0, IconElementData)
    BarFill: (Link, 0x0, 0x0, IconElementData)
    SliderIcon: (Link, 0x0, 0x0, IconElementData)
    pass

class 0xf2dd2d14():
    0x10074827: (String, 0x0, 0x0, 0x0)
    TitleVictoryTra: (String, 0x0, 0x0, 0x0)
    0x3fca802: (String, 0x0, 0x0, 0x0)
    TitleDefeatTra: (String, 0x0, 0x0, 0x0)
    0x4c453e79: (String, 0x0, 0x0, 0x0)
    TitleNextTra: (String, 0x0, 0x0, 0x0)
    0x8e3d338b: (String, 0x0, 0x0, 0x0)
    0x9128c36f: (String, 0x0, 0x0, 0x0)
    TitleFutureTra: (String, 0x0, 0x0, 0x0)
    ByeLabels: (Embed, 0x0, 0x0, 0xf3c319e2)
    0xd0133f4a: (String, 0x0, 0x0, 0x0)
    0xe130f1de: (String, 0x0, 0x0, 0x0)
    pass

class MultiDragonTypeSourceUiData():
    TeamSlotSourceIcon: (Hash, 0x0, 0x0, 0x0)
    SoulActiveSourceIcon: (Hash, 0x0, 0x0, 0x0)
    SoulRewardBuffName: (String, 0x0, 0x0, 0x0)
    TeamRewardBuffName: (String, 0x0, 0x0, 0x0)
    SoulKnownSourceIcon: (Hash, 0x0, 0x0, 0x0)
    SoulPreviewBuffName: (String, 0x0, 0x0, 0x0)
    pass

class LoadingScreenPlayerCardSwitcherData():
    TabData: (List, 0x0, Embed, LoadingScreenPlayerCardTabData)
    PlayerCardSwitcherLayout: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xf307d6c9(0x114828a9):
    SpawnDirection: (Vec2, 0x0, 0x0, 0x0)
    SpawnerCharacter: (Pointer, 0x0, 0x0, 0x4f4c4ffc)
    0xfd6b703e: (F32, 0x0, 0x0, 0x0)
    pass

class LevelUpUiData():
    PlayerBuffsScene: (Hash, 0x0, 0x0, 0x0)
    Spells: (List, 0x4, Embed, SpellLevelUpUiData)
    FxInScene: (Hash, 0x0, 0x0, 0x0)
    Title: (Hash, 0x0, 0x0, 0x0)
    pass

class FixedShaderDef(IShaderDef):
    VertexShader: (String, 0x0, 0x0, 0x0)
    PixelShader: (String, 0x0, 0x0, 0x0)
    pass

class CompanionLoadoutGridButtonData(LoadoutGridButtonData):
    FavoriteIcon: (Hash, 0x0, 0x0, 0x0)
    RarityIcon: (List, 0x0, Hash, 0x0)
    pass

class SkinSummonerEmoteLoadout():
    mEmotes: (List, 0xa, Link, SummonerEmote)
    mEmotes: (List, 0xe, Link, SummonerEmote)
    pass

class TftTeamPlannerChampionListingData():
    ChampionIcon: (Hash, 0x0, 0x0, 0x0)
    ChampionTierFrames: (List, 0x0, Hash, 0x0)
    TierChampionPortraitGroup: (Hash, 0x0, 0x0, 0x0)
    ChampionButtonTemplate: (Hash, 0x0, 0x0, 0x0)
    pass

class SummonerSpellPerkReplacement():
    mSummonerSpellRequired: (Hash, 0x0, 0x0, 0x0)
    mReplaceCurrentPerkWith: (Hash, 0x0, 0x0, 0x0)
    pass

class ChampSelectCharacterRecord():
    Id: (I32, 0x0, 0x0, 0x0)
    0x51f324f4: (Bool, 0x0, 0x0, 0x0)
    Key: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    PortraitPath: (String, 0x0, 0x0, 0x0)
    pass

class OptionItemBorder(IOptionItem):
    Items: (List, 0x0, Pointer, IOptionItem)
    Template: (Hash, 0x0, 0x0, 0x0)
    Item: (Pointer, 0x0, 0x0, IOptionItem)
    pass

class TimeMaterialDriver(IDynamicMaterialFloatDriver, ILogicFloatDriver):
    LoopDuration: (Option, 0x0, F32, 0x0)
    LoopTimeAsFraction: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xf37151c(TftCutsceneClip):
    BlackboardPosition: (String, 0x0, 0x0, 0x0)
    0x40d522bc: (String, 0x0, 0x0, 0x0)
    BlackboardOrientation: (String, 0x0, 0x0, 0x0)
    pass

class EffectCircleMaskCooldownElementData(EffectElementData):
    mEffectColor0: (Color, 0x0, 0x0, 0x0)
    mEffectColor1: (Color, 0x0, 0x0, 0x0)
    pass

class TftAnimClipOverrideModifier(TftAnimClipModifier):
    Animation: (String, 0x0, 0x0, 0x0)
    pass

class GlobalStatsUiData():
    FormulaPartStyleBonusPercent: (String, 0x0, 0x0, 0x0)
    FormulaPartRangeStylePercent: (String, 0x0, 0x0, 0x0)
    mNumberStyleTotalAndCoefficientPercent: (String, 0x0, 0x0, 0x0)
    FormulaPartStyle: (String, 0x0, 0x0, 0x0)
    FormulaPartRangeStyleBonus: (String, 0x0, 0x0, 0x0)
    mStatUiData: (Map, U8, Embed, StatUiData)
    mCharLevelScalingTagKey: (String, 0x0, 0x0, 0x0)
    mNumberStyleBonus: (String, 0x0, 0x0, 0x0)
    FormulaPartRangeStyleBonusPercent: (String, 0x0, 0x0, 0x0)
    mNumberStylePercent: (String, 0x0, 0x0, 0x0)
    CharLevelIconKey: (String, 0x0, 0x0, 0x0)
    mNumberStyleBonusPercent: (String, 0x0, 0x0, 0x0)
    StaticTooltipCalculationExpansion: (U8, 0x0, 0x0, 0x0)
    FormulaPartStyleBonus: (String, 0x0, 0x0, 0x0)
    BonusOutputIconModifier: (String, 0x0, 0x0, 0x0)
    mExpandedTooltipCalculationExpansion: (U8, 0x0, 0x0, 0x0)
    NumberStyleTotalAndFormula: (String, 0x0, 0x0, 0x0)
    mNumberStyleTotalAndCoefficient: (String, 0x0, 0x0, 0x0)
    FormulaPartRangeStyle: (String, 0x0, 0x0, 0x0)
    BaseOutputIconModifier: (String, 0x0, 0x0, 0x0)
    mNumberStyle: (String, 0x0, 0x0, 0x0)
    FormulaPartStylePercent: (String, 0x0, 0x0, 0x0)
    NumberStyleTotalAndScalingIcons: (String, 0x0, 0x0, 0x0)
    mManaScalingTagKey: (String, 0x0, 0x0, 0x0)
    mManaIconKey: (String, 0x0, 0x0, 0x0)
    NewStatUiData: (Map, U8, Embed, StatUiData)
    mTooltipCalculationExpansion: (U8, 0x0, 0x0, 0x0)
    pass

class IMapLightUpdater():
    pass

class LossOfControlIconData():
    0x13fcfacc: (String, 0x0, 0x0, 0x0)
    0x323596c9: (String, 0x0, 0x0, 0x0)
    AttackLossIcon: (String, 0x0, 0x0, 0x0)
    MovementTauntIcon: (String, 0x0, 0x0, 0x0)
    MovementSlowIcon: (String, 0x0, 0x0, 0x0)
    0x7d5eb39b: (String, 0x0, 0x0, 0x0)
    0x80939423: (String, 0x0, 0x0, 0x0)
    SuppressionIcon: (String, 0x0, 0x0, 0x0)
    0x919e3a94: (String, 0x0, 0x0, 0x0)
    0x9791c2c0: (String, 0x0, 0x0, 0x0)
    AbilityLossIcon: (String, 0x0, 0x0, 0x0)
    0x9c21de96: (String, 0x0, 0x0, 0x0)
    0x9cff312b: (String, 0x0, 0x0, 0x0)
    MovementLossIcon: (String, 0x0, 0x0, 0x0)
    0xa0caac29: (String, 0x0, 0x0, 0x0)
    KnockBackIcon: (String, 0x0, 0x0, 0x0)
    KnockUpIcon: (String, 0x0, 0x0, 0x0)
    FullLossIcon: (String, 0x0, 0x0, 0x0)
    AttackBlindIcon: (String, 0x0, 0x0, 0x0)
    0xde943bb9: (String, 0x0, 0x0, 0x0)
    MovementCharmIcon: (String, 0x0, 0x0, 0x0)
    MovementFearIcon: (String, 0x0, 0x0, 0x0)
    0xf2cb2755: (String, 0x0, 0x0, 0x0)
    0xffcf267d: (String, 0x0, 0x0, 0x0)
    pass

class 0xf3c319e2():
    0x3f8acbfd: (String, 0x0, 0x0, 0x0)
    0x3fca802: (String, 0x0, 0x0, 0x0)
    0x6c52029a: (String, 0x0, 0x0, 0x0)
    TitleTra: (String, 0x0, 0x0, 0x0)
    0xbb21a9ed: (String, 0x0, 0x0, 0x0)
    pass

class 0xf3cbe7b2(IGameCalculationPart):
    mSpellCalculationKey: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xf3cf86a3():
    Scene: (Hash, 0x0, 0x0, 0x0)
    Description: (Hash, 0x0, 0x0, 0x0)
    Button: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    Title: (Hash, 0x0, 0x0, 0x0)
    ButtonText: (Hash, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class ItemRecommendationPath():
    mAltRecommendations: (List, 0x0, Embed, ItemRecommendationNode)
    mRecommendations: (List, 0x0, Embed, ItemRecommendationNode)
    pass

class HasTypeAndStatusFlags(ICastRequirement):
    mAffectsStatusFlags: (U32, 0x0, 0x0, 0x0)
    mAffectsTypeFlags: (U32, 0x0, 0x0, 0x0)
    pass

class TftShopDropRates():
    mDropRatesByTier: (List, 0x5, F32, 0x0)
    pass

class 0xf43ad1ce():
    IconShadowT1: (Hash, 0x0, 0x0, 0x0)
    IconShadowT2: (Hash, 0x0, 0x0, 0x0)
    Team1Meter: (Embed, 0x0, 0x0, 0xb8a49c96)
    Frame: (Hash, 0x0, 0x0, 0x0)
    Team2Meter: (Embed, 0x0, 0x0, 0xb8a49c96)
    pass

class ElementGroupData(ElementDataI):
    Elements: (List, 0x0, Link, ElementDataI)
    Elements: (List2, 0x0, Link, ElementDataI)
    pass

class ItemDataModifiable():
    mInStore: (Bool, 0x0, 0x0, 0x0)
    pass

class LoadoutEmoteInfoPanel(ILoadoutInfoPanel):
    SaveButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelSwButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelSButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelUpperButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelRightButton: (Hash, 0x0, 0x0, 0x0)
    EmoteVictoryButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelLeftButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelLowerButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelNeButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelWButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelCButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelNwButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelLeftButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelSwButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelSButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelCenterButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelCButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelUpperButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelRightButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteStartButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelNeButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelCenterButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelSeButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelEButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelNButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelNwButton: (Hash, 0x0, 0x0, 0x0)
    EmoteVictoryButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelWButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelLowerButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelNButton: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelEButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteStartButton_Icon: (Hash, 0x0, 0x0, 0x0)
    EmoteWheelSeButton_Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class GameModeConstantTraKey(GameModeConstant):
    mValue: (String, 0x0, 0x0, 0x0)
    pass

class UseableData():
    UseHeroSpellName: (String, 0x0, 0x0, 0x0)
    UseSpellName: (String, 0x0, 0x0, 0x0)
    UseCooldownSpellSlot: (I32, 0x0, 0x0, 0x0)
    Flags: (U32, 0x0, 0x0, 0x0)
    pass

class 0xf4737fbd(0xc06f5f6a):
    Value: (Hash, 0x0, 0x0, 0x0)
    pass

class Obj_InfoPoint(GameObject):
    pass

class ProgressionNode(BaseLoadoutData):
    0xda181aa2: (Map, I32, Embed, ProgressionNodeData)
    pass

class UiElementScissorRegion(UiElement):
    pass

class BaseLevelController():
    pass

class ItemShopGameModeData():
    mAllItemsSet: (Link, 0x0, 0x0, AllItemsSet)
    0x176889a9: (List, 0x0, Embed, 0x8b38bb8d)
    mEnableChatRecommendations: (Bool, 0x0, 0x0, 0x0)
    BootsQuickBuyData: (Embed, 0x0, 0x0, HudItemShopQuickBuyData)
    PurchasedItemExclusionItems: (List, 0x0, Hash, 0x0)
    RecFallbackModeName: (Hash, 0x0, 0x0, 0x0)
    ConsumablesQuickBuyData: (Embed, 0x0, 0x0, HudItemShopQuickBuyData)
    RecRoleSwaps: (Map, Hash, Hash, 0x0)
    RecItemsSwaps: (Map, U32, U32, 0x0)
    mItemRecommendationContexts: (List, 0x0, Embed, ItemRecommendationContext)
    RecFallbackMapId: (U32, 0x0, 0x0, 0x0)
    RecOverrideSmiteStartingItems: (List, 0x0, Hash, 0x0)
    CompletedItems: (List2, 0x0, Hash, 0x0)
    AllItemGroupDefinitionsOverride: (Pointer, 0x0, 0x0, 0xac27b13a)
    pass

class TftRoundData():
    mName: (String, 0x0, 0x0, 0x0)
    mDurationPlanningDeparture: (F32, 0x0, 0x0, 0x0)
    mRoundActiveIconPath: (String, 0x0, 0x0, 0x0)
    mDurationPlanningArrival: (F32, 0x0, 0x0, 0x0)
    mDraft: (Embed, 0x0, 0x0, TftPhaseData)
    mDurationCombatDeparture: (F32, 0x0, 0x0, 0x0)
    mDurationCombat: (F32, 0x0, 0x0, 0x0)
    0x4b01b075: (Bool, 0x0, 0x0, 0x0)
    mDraftArrival: (Embed, 0x0, 0x0, TftPhaseData)
    mRoundResultDrawIconPath: (String, 0x0, 0x0, 0x0)
    mDurationDraft: (F32, 0x0, 0x0, 0x0)
    mDurationDraftDeparture: (F32, 0x0, 0x0, 0x0)
    0x5a4ea04e: (Bool, 0x0, 0x0, 0x0)
    mDurationPlanning: (F32, 0x0, 0x0, 0x0)
    mDraftDeparture: (Embed, 0x0, 0x0, TftPhaseData)
    mDurationDraftArrival: (F32, 0x0, 0x0, 0x0)
    mStateTooltipsTra: (Map, U32, String, 0x0)
    mDurationCombatArrival: (F32, 0x0, 0x0, 0x0)
    mPlanningDeparture: (Embed, 0x0, 0x0, TftPhaseData)
    mScriptData: (Map, String, Pointer, GameModeConstant)
    CombatArtCleanup: (Embed, 0x0, 0x0, TftPhaseData)
    mPlanningArrival: (Embed, 0x0, 0x0, TftPhaseData)
    mIconPath: (String, 0x0, 0x0, 0x0)
    mCombatArrival: (Embed, 0x0, 0x0, TftPhaseData)
    mPlanning: (Embed, 0x0, 0x0, TftPhaseData)
    mDescriptionTra: (String, 0x0, 0x0, 0x0)
    mDisplayNameTra: (String, 0x0, 0x0, 0x0)
    mRoundResultLossIconPath: (String, 0x0, 0x0, 0x0)
    mRoundResultWinIconPath: (String, 0x0, 0x0, 0x0)
    mRoundUpcomingIconPath: (String, 0x0, 0x0, 0x0)
    0xecd6dad4: (Bool, 0x0, 0x0, 0x0)
    mDefaultTooltipTra: (String, 0x0, 0x0, 0x0)
    mCombatDeparture: (Embed, 0x0, 0x0, TftPhaseData)
    mRoundResultNoneIconPath: (String, 0x0, 0x0, 0x0)
    mCombat: (Embed, 0x0, 0x0, TftPhaseData)
    pass

class MapPropCommon(GameObject):
    pass

class Float4LiteralMaterialDriver(IDynamicMaterialDriver, ILogicDriver):
    Value: (Vec4, 0x0, 0x0, 0x0)
    pass

class StopAnimationEventData(BaseEventData):
    mStopAnimationName: (Hash, 0x0, 0x0, 0x0)
    pass

class VfxEmitterFiltering():
    KeywordsRequired: (List, 0x0, String, 0x0)
    CensorPolicy: (U8, 0x0, 0x0, 0x0)
    KeywordsIncluded: (List, 0x0, String, 0x0)
    KeywordsExcluded: (List, 0x0, String, 0x0)
    SpectatorPolicy: (U8, 0x0, 0x0, 0x0)
    pass

class 0xf4e577e(IGameModeConfig):
    ChampionComponents: (List2, 0x0, Pointer, 0x51f54b8e)
    pass

class ContextualConditionItemPurchased(IContextualCondition):
    mItemPurchased: (Bool, 0x0, 0x0, 0x0)
    pass

class GeneralSettingsGroup():
    RestorePurchaseButton: (Hash, 0x0, 0x0, 0x0)
    PromoteAccountButton: (Hash, 0x0, 0x0, 0x0)
    SignOutButton: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xf5022dc7():
    BaseModel: (String, 0x0, 0x0, 0x0)
    QualitySetting: (Link, 0x0, 0x0, QualitySetting)
    VersionThreshold: (U32, 0x0, 0x0, 0x0)
    pass

class UiElementEffect(UiElementAsset):
    pass

class OptionItemVoiceInputDeviceDropdown(OptionItemDropdown):
    pass

class SimpleItemSlots():
    Item6: (Embed, 0x0, 0x0, ItemSlotSimpleUiData)
    Item4: (Embed, 0x0, 0x0, ItemSlotSimpleUiData)
    Item5: (Embed, 0x0, 0x0, ItemSlotSimpleUiData)
    Item2: (Embed, 0x0, 0x0, ItemSlotSimpleUiData)
    Item3: (Embed, 0x0, 0x0, ItemSlotSimpleUiData)
    Item0: (Embed, 0x0, 0x0, ItemSlotSimpleUiData)
    Item1: (Embed, 0x0, 0x0, ItemSlotSimpleUiData)
    pass

class MasteryBadgeConfig():
    mBadges: (List, 0x0, Embed, MasteryBadgeData)
    mBadges: (Map, Hash, Embed, MasteryBadgeData)
    pass

class SpellSlotPassiveUiDefinition(SpellSlotBasicUiDefinition):
    OverlayDisabled: (Hash, 0x0, 0x0, 0x0)
    BorderEnabled: (Hash, 0x0, 0x0, 0x0)
    BorderDisabled: (Hash, 0x0, 0x0, 0x0)
    CooldownUiData: (Embed, 0x0, 0x0, CooldownEffectUiData)
    pass

class TerminatePath(JungleAction):
    pass

class FxActionMove(IFxAction):
    OvershootDistance: (F32, 0x0, 0x0, 0x0)
    EasingType: (U32, 0x0, 0x0, 0x0)
    EasingType: (U8, 0x0, 0x0, 0x0)
    FaceVelocity: (Bool, 0x0, 0x0, 0x0)
    Destination: (Embed, 0x0, 0x0, FxTransform)
    0xd935fe42: (Bool, 0x0, 0x0, 0x0)
    TargetObject: (Embed, 0x0, 0x0, FxTarget)
    pass

class 0xf5821f8b(ILogicBoolDriver):
    pass

class RichBackgroundGameModeBackground():
    Background: (Hash, 0x0, 0x0, 0x0)
    BackgroundElementMap: (Map, String, Hash, 0x0)
    BackgroundElementMap: (Map, String, String, 0x0)
    BackgroundElementMap: (Map, U32, String, 0x0)
    pass

class GameMutatorExpansions():
    mExpandedMutator: (String, 0x0, 0x0, 0x0)
    mMutators: (List, 0x0, String, 0x0)
    mMutators: (List2, 0x0, String, 0x0)
    pass

class ObjectiveVotePanelViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    CollapseButton: (Hash, 0x0, 0x0, 0x0)
    ForButton: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    ObjectivePortrait: (Hash, 0x0, 0x0, 0x0)
    ObjectiveText: (Hash, 0x0, 0x0, 0x0)
    RejectButton: (Hash, 0x0, 0x0, 0x0)
    SpawningText: (Hash, 0x0, 0x0, 0x0)
    VoteResultTemplate: (Embed, 0x0, 0x0, ObjectiveVoteResultData)
    VoteAutoCloseDelay: (F32, 0x0, 0x0, 0x0)
    AutoActivateTimeBeforeSpawn: (F32, 0x0, 0x0, 0x0)
    PortraitLayout: (Hash, 0x0, 0x0, 0x0)
    VotesLayout: (Hash, 0x0, 0x0, 0x0)
    NumVoters: (U32, 0x0, 0x0, 0x0)
    ObjectiveCampInfo: (List, 0x0, Embed, ObjectiveVoteCampDefinition)
    VoteTemplate: (Embed, 0x0, 0x0, ObjectiveVoteData)
    pass

class HudStatStoneMilestoneData():
    MilestoneIntroTime: (F32, 0x0, 0x0, 0x0)
    MilestoneSelfIntroTime: (F32, 0x0, 0x0, 0x0)
    MilestoneTransitionOut: (Embed, 0x0, 0x0, HudMenuTransitionData)
    0x39fecf93: (F32, 0x0, 0x0, 0x0)
    0x3d69612a: (F32, 0x0, 0x0, 0x0)
    MilestoneDisplayTime: (F32, 0x0, 0x0, 0x0)
    0x4ea59d14: (Bool, 0x0, 0x0, 0x0)
    UiSoundForPersonalBest: (String, 0x0, 0x0, 0x0)
    MilestoneOtherIntroTime: (F32, 0x0, 0x0, 0x0)
    0x86f904d1: (F32, 0x0, 0x0, 0x0)
    0x8ca5c29b: (F32, 0x0, 0x0, 0x0)
    MasteryToBackgroundLookup: (Map, U32, Link, VfxSystemDefinitionData)
    0xa6d1b459: (Embed, 0x0, 0x0, HudMenuTransitionData)
    UiSound: (String, 0x0, 0x0, 0x0)
    MilestoneTransitionIn: (Embed, 0x0, 0x0, HudMenuTransitionData)
    UiSoundForPersonalBestForLocalPlayer: (String, 0x0, 0x0, 0x0)
    PersonalBestIntroTime: (F32, 0x0, 0x0, 0x0)
    MaxNumberOfMilestonesToShowPerStonePerGame: (U32, 0x0, 0x0, 0x0)
    MilestoneDisplayTimeForLocalPlayer: (F32, 0x0, 0x0, 0x0)
    UiSoundForLocalPlayer: (String, 0x0, 0x0, 0x0)
    pass

class HudLoadingScreenWidgetTutorial(IHudLoadingScreenWidget):
    pass

class TftTrovesBannerData():
    PullCost: (U32, 0x0, 0x0, 0x0)
    BannerTexturePath: (String, 0x0, 0x0, 0x0)
    PityThreshold: (U32, 0x0, 0x0, 0x0)
    MaxTotalRolls: (U32, 0x0, 0x0, 0x0)
    PlatformTexturePath: (String, 0x0, 0x0, 0x0)
    Id: (String, 0x0, 0x0, 0x0)
    ChaseTable: (Link, 0x0, 0x0, TftTrovesBannerTable)
    ActivationDateTime: (String, 0x0, 0x0, 0x0)
    DeactivationDateTime: (String, 0x0, 0x0, 0x0)
    BannerCurrencyId: (String, 0x0, 0x0, 0x0)
    ThumbnailTexturePath: (String, 0x0, 0x0, 0x0)
    NameTraKey: (String, 0x0, 0x0, 0x0)
    BannerCurrency: (Link, 0x0, 0x0, TftCurrency)
    TotalRollsCounterId: (String, 0x0, 0x0, 0x0)
    BackgroundTexturePath: (String, 0x0, 0x0, 0x0)
    CelebrationTheme: (Link, 0x0, 0x0, TftTrovesCelebrationThemeData)
    PityCounterId: (String, 0x0, 0x0, 0x0)
    RootTable: (Link, 0x0, 0x0, TftTrovesBannerTable)
    DescriptionTraKey: (String, 0x0, 0x0, 0x0)
    MythicTokenOfferId: (String, 0x0, 0x0, 0x0)
    0xe147c198: (String, 0x0, 0x0, 0x0)
    0xfbca1d6b: (Bool, 0x0, 0x0, 0x0)
    pass

class TrophyCupData():
    mName: (String, 0x0, 0x0, 0x0)
    mSkinMeshProperties: (Embed, 0x0, 0x0, SkinMeshDataProperties)
    mAnimationGraphData: (Link, 0x0, 0x0, AnimationGraphData)
    mCupId: (U32, 0x0, 0x0, 0x0)
    mJointName: (String, 0x0, 0x0, 0x0)
    mImage: (String, 0x0, 0x0, 0x0)
    pass

class AnimationGraphData():
    mCascadeBlendValue: (F32, 0x0, 0x0, 0x0)
    mBlendDataList: (List, 0x0, Embed, BlendData)
    mBlendDataTable: (Map, U64, Pointer, BaseBlendData)
    mTrackDataMap: (Map, Hash, Embed, TrackData)
    AnimStateGraphEntryClips: (List, 0x0, Hash, 0x0)
    mClipDataMap: (Map, Hash, Pointer, ClipBaseData)
    mClipDataList: (List, 0x0, Pointer, ClipBaseData)
    mTrackDataList: (List, 0x0, Embed, TrackData)
    mMaskDataList: (List, 0x0, Embed, MaskData)
    mSyncGroupDataMap: (Map, Hash, Embed, SyncGroupData)
    mTransitionClipDataList: (List, 0x0, Embed, TransitionClipData)
    mUseCascadeBlend: (Bool, 0x0, 0x0, 0x0)
    mSyncGroupDataList: (List, 0x0, Embed, SyncGroupData)
    AnimStateGraphEntryClip: (Hash, 0x0, 0x0, 0x0)
    mMaskDataMap: (Map, Hash, Embed, MaskData)
    pass

class AdditionalMapContainersConfig(IGameModeConfig):
    MapContainers: (List, 0x0, String, 0x0)
    pass

class MinionUpgradeConfig():
    LocalGoldGivenOnLastHit: (F32, 0x0, 0x0, 0x0)
    HpUpgradeLate: (F32, 0x0, 0x0, 0x0)
    HpUpgradeGrowth: (F32, 0x0, 0x0, 0x0)
    DamageUpgradeLate: (F32, 0x0, 0x0, 0x0)
    DamageUpgrade: (F32, 0x0, 0x0, 0x0)
    DamageMax: (F32, 0x0, 0x0, 0x0)
    HpUpgrade: (F32, 0x0, 0x0, 0x0)
    DamageInhibitor: (F32, 0x0, 0x0, 0x0)
    HpInhibitor: (F32, 0x0, 0x0, 0x0)
    ArmorUpgradeGrowth: (F32, 0x0, 0x0, 0x0)
    ArmorUpgrade: (F32, 0x0, 0x0, 0x0)
    MagicResistanceUpgrade: (F32, 0x0, 0x0, 0x0)
    HpUpgradeGrowthLate: (F32, 0x0, 0x0, 0x0)
    LocalGoldGiven: (F32, 0x0, 0x0, 0x0)
    HpMaxBonus: (F32, 0x0, 0x0, 0x0)
    ArmorMax: (F32, 0x0, 0x0, 0x0)
    pass

class VfxAssetRemap():
    Type: (U32, 0x0, 0x0, 0x0)
    OldAsset: (Hash, 0x0, 0x0, 0x0)
    NewAsset: (String, 0x0, 0x0, 0x0)
    pass

class BezierSegment():
    ControlPoint1: (Vec3, 0x0, 0x0, 0x0)
    ControlPoint2: (Vec3, 0x0, 0x0, 0x0)
    Endpoint: (Vec3, 0x0, 0x0, 0x0)
    pass

class TftStageRoundDataTemplate():
    ActiveIcon: (Hash, 0x0, 0x0, 0x0)
    Group: (Hash, 0x0, 0x0, 0x0)
    RoundStateIcon: (Hash, 0x0, 0x0, 0x0)
    HitRegion: (Hash, 0x0, 0x0, 0x0)
    pass

class UnitShopDisplayTraitData():
    Styles: (Map, U32, Embed, UnitShopItemTraitData)
    pass

class OptionTemplateSecondaryHotkeys2Column(IOptionTemplate):
    RowButtonColumn1: (Embed, 0x0, 0x0, OptionTemplateSecondaryHotkeys_Button)
    RowButtonColumn2: (Embed, 0x0, 0x0, OptionTemplateSecondaryHotkeys_Button)
    HeadingRowLabel2: (Embed, 0x0, 0x0, OptionTemplateSecondaryHotkeys_Label)
    HeadingRowLabel1: (Embed, 0x0, 0x0, OptionTemplateSecondaryHotkeys_Label)
    HeadingRowLabel0: (Embed, 0x0, 0x0, OptionTemplateSecondaryHotkeys_Label)
    BoundsElement: (Hash, 0x0, 0x0, 0x0)
    RowLabelColumn0: (Embed, 0x0, 0x0, OptionTemplateSecondaryHotkeys_Label)
    pass

class RandomChanceScriptCondition(IScriptCondition):
    Chance: (Pointer, 0x0, 0x0, IFloatGet)
    PercentageChance: (Pointer, 0x0, 0x0, IFloatGet)
    pass

class ScoreLineSrUiData(ScoreLineBaseUiData):
    UnitLevel: (Embed, 0x0, 0x0, UnitLevelUiData)
    OpenMuteModalButton: (Hash, 0x0, 0x0, 0x0)
    ItemSlots: (Embed, 0x0, 0x0, SimpleItemSlots)
    ChatMuteButton: (Hash, 0x0, 0x0, 0x0)
    OpenReportModalButton: (Hash, 0x0, 0x0, 0x0)
    SpellSlots: (Embed, 0x0, 0x0, ScoreLineSpellSlots)
    SelfSlotHighlight: (Hash, 0x0, 0x0, 0x0)
    0x9f82652b: (Hash, 0x0, 0x0, 0x0)
    MuteAllButton: (Hash, 0x0, 0x0, 0x0)
    SocialTooltipAnchor: (Hash, 0x0, 0x0, 0x0)
    EmoteMuteButton: (Hash, 0x0, 0x0, 0x0)
    MuteModalAnchor: (Hash, 0x0, 0x0, 0x0)
    Keystone: (Embed, 0x0, 0x0, ChampionPerkKeystoneUiData)
    SummonerName: (Embed, 0x0, 0x0, SummonerNameUiData)
    UltCooldownGem: (Embed, 0x0, 0x0, CooldownGemUiData)
    MuteSelfButton: (Hash, 0x0, 0x0, 0x0)
    PingMuteButton: (Hash, 0x0, 0x0, 0x0)
    pass

class BackdropElement():
    mOffset: (Vec2, 0x0, 0x0, 0x0)
    mBorderOffset: (Vec2, 0x0, 0x0, 0x0)
    mParamsColorBlind: (Pointer, 0x0, 0x0, BackdropElementTeamParams)
    mParamsDefault: (Pointer, 0x0, 0x0, BackdropElementTeamParams)
    mHighlightRightTextureUvs: (Vec4, 0x0, 0x0, 0x0)
    mHighlightMidTextureUvs: (Vec4, 0x0, 0x0, 0x0)
    mBorderLeftTextureUvs: (Vec4, 0x0, 0x0, 0x0)
    mHighlightOffset: (Vec2, 0x0, 0x0, 0x0)
    mBorderRightTextureUvs: (Vec4, 0x0, 0x0, 0x0)
    mHighlightLeftTextureUvs: (Vec4, 0x0, 0x0, 0x0)
    mTextureName: (String, 0x0, 0x0, 0x0)
    mBorderMidTextureUvs: (Vec4, 0x0, 0x0, 0x0)
    pass

class ScriptTableSet():
    Table: (Pointer, 0x0, 0x0, ScriptTable)
    Var: (Hash, 0x0, 0x0, 0x0)
    Var: (String, 0x0, 0x0, 0x0)
    pass

class UiDraggableProxyElementDrag(UiDraggableBasic):
    ProxyElement: (Link, 0x0, 0x0, UiElementIData)
    pass

class 0xf6da700f(0xb0e1e45e):
    Updater: (Pointer, 0x0, 0x0, IBooleanParametricUpdater)
    Comparator: (U8, 0x0, 0x0, 0x0)
    pass

class LookAtGoldRedirectTargetAngleParametricUpdater(IFloatParametricUpdater):
    pass

class IScriptValueGet():
    pass

class 0xf6f4bb5f():
    Color: (Color, 0x0, 0x0, 0x0)
    Name: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xf6fd1c96(EffectElementData):
    mMaterial: (Link, 0x0, 0x0, StaticMaterialDef)
    pass

class MapActionFaceCamera(MapAction):
    Duration: (F32, 0x0, 0x0, 0x0)
    PropNames: (List2, 0x0, String, 0x0)
    pass

class 0xf7084b4a():
    Name: (String, 0x0, 0x0, 0x0)
    ShaderMacros: (Map, String, String, 0x0)
    pass

class SkinUiProperties():
    ViewController: (Hash, 0x0, 0x0, 0x0)
    pass

class LoadScreenTipSet():
    mName: (Hash, 0x0, 0x0, 0x0)
    mTips: (List, 0x0, Link, LoadScreenTip)
    pass

class UiElementEffectFillPercentageData(UiElementEffectData):
    mPerPixelUvsX: (Bool, 0x0, 0x0, 0x0)
    TextureData: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mAtlas: (Pointer, 0x0, 0x0, AtlasData)
    mAtlas: (Pointer, 0x0, 0x0, IUiEffectTextureDataProvider)
    mFlipY: (Bool, 0x0, 0x0, 0x0)
    mFlipX: (Bool, 0x0, 0x0, 0x0)
    pass

class StatStoneEventToTrack():
    EventToTrack: (U32, 0x0, 0x0, 0x0)
    StatFilters: (List, 0x0, Pointer, IStatStoneLogicDriver)
    pass

class FixedTimeMovement(MissileMovementSpec):
    mProjectTargetToCastRange: (Bool, 0x0, 0x0, 0x0)
    mUseGroundHeightAtTarget: (Bool, 0x0, 0x0, 0x0)
    mInferDirectionFromFacingIfNeeded: (Bool, 0x0, 0x0, 0x0)
    AddBonusAttackRangeToCastRange: (Bool, 0x0, 0x0, 0x0)
    mTravelTime: (F32, 0x0, 0x0, 0x0)
    pass

class TftStageData():
    mName: (String, 0x0, 0x0, 0x0)
    mRounds: (List, 0x0, Link, TftRoundData)
    pass

class VfxProjectionDefinitionData():
    mFading: (F32, 0x0, 0x0, 0x0)
    mYRange: (F32, 0x0, 0x0, 0x0)
    ColorModulate: (Embed, 0x0, 0x0, ValueColor)
    pass

class HudChatData():
    DefaultWordWrapMargin: (U8, 0x0, 0x0, 0x0)
    mChatMessageDefault: (U8, 0x0, 0x0, 0x0)
    mChatMessageExtended: (U8, 0x0, 0x0, 0x0)
    HideAfterSeconds: (F32, 0x0, 0x0, 0x0)
    pass

class LogicDriverVisibilityController(IMapVisibilityController):
    0x35b17559: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    VisibilityDriver: (Pointer, 0x0, 0x0, ILogicBoolDriver)
    TransitionTimeDriver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class TftCutsceneAction(TftCutsceneEntry):
    pass

class ILineIndicatorType():
    pass

class TftTrovesBannerNode():
    Id: (String, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    pass

class IInputSourceBool():
    pass

class HasAllSubRequirementsCastRequirement(ICastRequirement):
    mSubRequirements: (List, 0x0, Pointer, ICastRequirement)
    pass

class BufferedInputChain():
    InputStrideTimeInSecs: (F32, 0x0, 0x0, 0x0)
    Inputs: (List, 0x0, I32, 0x0)
    Inputs: (List, 0x0, U32, 0x0)
    Priority: (U8, 0x0, 0x0, 0x0)
    0x97d20804: (Bool, 0x0, 0x0, 0x0)
    pass

class TftStageRoundData():
    Stages: (List2, 0x0, Embed, TftStageData)
    pass

class AiBaseClient(AiBaseCommon):
    pass

class SkinCharacterMetaDataProperties():
    UseAudioProperties: (Bool, 0x0, 0x0, 0x0)
    UseWadBinaries: (Bool, 0x0, 0x0, 0x0)
    TagToEnableSpawnSkinOffset: (String, 0x0, 0x0, 0x0)
    EsportLeagueTable: (List, 0x0, Embed, EsportLeagueEntry)
    IsRelativeColorCharacter: (Bool, 0x0, 0x0, 0x0)
    EsportCharacter: (Bool, 0x0, 0x0, 0x0)
    EsportTeamTable: (List, 0x0, Embed, EsportTeamEntry)
    UseAnimationProperties: (Bool, 0x0, 0x0, 0x0)
    Dummy: (String, 0x0, 0x0, 0x0)
    SkinBasedRelativeColorScheme: (Bool, 0x0, 0x0, 0x0)
    UseGdsBinaries: (Bool, 0x0, 0x0, 0x0)
    SpawningSkinOffsets: (List, 0x0, Embed, SkinCharacterMetaDataProperties_SpawningSkinOffset)
    EsportTeamMatchingTable: (List, 0x0, String, 0x0)
    SpawnSkinOffset: (I32, 0x0, 0x0, 0x0)
    RelativeColorSwapTable: (List, 0x0, I32, 0x0)
    pass

class OptionItemFilter_Osx(IOptionItemFilter):
    pass

class ItemRecommendationOverrideStartingItemBundle():
    Items: (List, 0x0, Hash, 0x0)
    pass

class SummonerBadgeManagerSettings():
    mGlobalCooldown: (F32, 0x0, 0x0, 0x0)
    mAllyFacingDetectionRange: (F32, 0x0, 0x0, 0x0)
    mDefaultBadgeIds: (List, 0x4, U32, 0x0)
    mDefaultBadgeIds: (List, 0x7, U32, 0x0)
    mEnemyFacingDetectionRange: (F32, 0x0, 0x0, 0x0)
    mNoEmoteWheelTexture: (String, 0x0, 0x0, 0x0)
    pass

class PlaybookItemListPanelData():
    ButtonArea: (Hash, 0x0, 0x0, 0x0)
    ViewPanelScene: (Hash, 0x0, 0x0, 0x0)
    pass

class 0xf8739c73():
    OtherChallengeName: (Hash, 0x0, 0x0, 0x0)
    Background: (Hash, 0x0, 0x0, 0x0)
    OtherChallengeDesc: (Hash, 0x0, 0x0, 0x0)
    LocalPlayer: (Embed, 0x0, 0x0, 0xf02f881)
    OtherPlayer: (Embed, 0x0, 0x0, 0xf02f881)
    pass

class DisabledRegionData(RegionDataBase):
    pass

class CastOnDistanceFromCaster(MissileBehaviorSpec):
    mDistance: (F32, 0x0, 0x0, 0x0)
    pass

class 0xf8c18a6e():
    NameTraKey: (String, 0x0, 0x0, 0x0)
    pass

class TftBotSkillData():
    SkillAxes: (Map, U8, Embed, 0x6de4753e)
    pass

class FxActionVfx(IFxAction):
    UseRotation: (Bool, 0x0, 0x0, 0x0)
    TargetPosition: (Embed, 0x0, 0x0, FxTransform)
    FollowPath: (Bool, 0x0, 0x0, 0x0)
    ScalePlaybackSpeedReferenceDuration: (F32, 0x0, 0x0, 0x0)
    Follow: (Bool, 0x0, 0x0, 0x0)
    Scale: (F32, 0x0, 0x0, 0x0)
    Particle: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    Position: (Embed, 0x0, 0x0, FxTransform)
    SplineInfo: (Pointer, 0x0, 0x0, ISplineInfo)
    PathTargetPosition: (Embed, 0x0, 0x0, FxTransform)
    IsBeam: (Bool, 0x0, 0x0, 0x0)
    pass

class 0xf9162ab6(TargetingTypeData):
    pass

class DisplacementParametricUpdater(IFloatParametricUpdater):
    pass

class 0xf9324178():
    mUnit: (U32, 0x0, 0x0, 0x0)
    Unit: (U32, 0x0, 0x0, 0x0)
    pass

class TeamScoreMeterUiTunables():
    mTeamScoreMeterTypes: (List, 0x2, U8, 0x0)
    mTeamScoreMeterMaxRoundsPerTeam: (U32, 0x0, 0x0, 0x0)
    mSceneTransition: (Embed, 0x0, 0x0, HudMenuTransitionData)
    mCountdownTimer: (Bool, 0x0, 0x0, 0x0)
    mTeamScoreMeterProperties: (List, 0x2, Embed, HudTeamScoreMeterProperties)
    mEventCount: (U8, 0x0, 0x0, 0x0)
    mAllowDynamicVisibility: (Bool, 0x0, 0x0, 0x0)
    pass

class TftCutsceneObjSfxClip(TftCutsceneClip):
    0x3cff8270: (Bool, 0x0, 0x0, 0x0)
    StopAudioEvent: (String, 0x0, 0x0, 0x0)
    0x78afa616: (String, 0x0, 0x0, 0x0)
    StartAudioEvent: (String, 0x0, 0x0, 0x0)
    0xbdee689d: (Bool, 0x0, 0x0, 0x0)
    pass

class FxActionScaleInstance(IFxActionInstance):
    pass

class VfxMaterialOverrideDefinition():
    TransitionTexture: (String, 0x0, 0x0, 0x0)
    UScrolling: (F32, 0x0, 0x0, 0x0)
    SubMeshName: (String, 0x0, 0x0, 0x0)
    RenderingMode: (I32, 0x0, 0x0, 0x0)
    TransitionSample: (F32, 0x0, 0x0, 0x0)
    Priority: (I32, 0x0, 0x0, 0x0)
    Flags: (U32, 0x0, 0x0, 0x0)
    BaseTexture: (String, 0x0, 0x0, 0x0)
    TransitionSource: (U32, 0x0, 0x0, 0x0)
    GlossTexture: (String, 0x0, 0x0, 0x0)
    VScrolling: (F32, 0x0, 0x0, 0x0)
    pass

class UiScene():
    pass

class SetInvulnerableBlock(IScriptBlock):
    Value: (Pointer, 0x0, 0x0, IBoolGet)
    pass

class SocialPanelViewController(ViewController):
    EmptyStateGroup: (Hash, 0x0, 0x0, 0x0)
    AddFriendButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    InviteButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    AddFriendButton: (Hash, 0x0, 0x0, 0x0)
    ViewPaneDefinition: (Embed, 0x0, 0x0, ViewPaneDefinition)
    FriendsListSceneViewPane: (Hash, 0x0, 0x0, 0x0)
    SlotOneRegion: (Hash, 0x0, 0x0, 0x0)
    SlotZeroRegion: (Hash, 0x0, 0x0, 0x0)
    FriendButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    FriendsListItem: (Embed, 0x0, 0x0, SocialPanelFriendsListItemData)
    InviteButton: (Hash, 0x0, 0x0, 0x0)
    pass

class IsAttackingBoolDriver(ILogicBoolDriver):
    pass

class SelectSpellBlock(IScriptBlock, IBehaviorScriptBlock):
    pass

class 0xf9e5b8b9(ILogicFloatDriver):
    Value: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    pass

class 0xfa040e57(0xbc280d0a):
    Source: (Link, 0x0, 0x0, SequenceObjectSelector)
    DefaultValue: (String, 0x0, 0x0, 0x0)
    DebugOverride: (String, 0x0, 0x0, 0x0)
    pass

class SelectorMovement(MissileMovementSpec):
    MovementOptions: (List, 0x0, Embed, SelectorMovementEntry)
    pass

class UiPlayerPortraitData():
    0x16d8ddbe: (Hash, 0x0, 0x0, 0x0)
    0x27502925: (Hash, 0x0, 0x0, 0x0)
    SingleClickToPing: (Bool, 0x0, 0x0, 0x0)
    FrameUnderlay: (Hash, 0x0, 0x0, 0x0)
    RespawnTimerText: (Hash, 0x0, 0x0, 0x0)
    Frame: (Hash, 0x0, 0x0, 0x0)
    PortraitIconShape: (U8, 0x0, 0x0, 0x0)
    PortraitIcon: (Hash, 0x0, 0x0, 0x0)
    FrameWhileDead: (Hash, 0x0, 0x0, 0x0)
    pass

class WardSkinDisabler():
    DisableAllSkins: (Bool, 0x0, 0x0, 0x0)
    DisabledIds: (List, 0x0, U32, 0x0)
    pass

class UiElementGroupFramed(UiElementGroup):
    pass

class NeutralTimerState():
    0x56841fae: (List2, 0x0, Hash, 0x0)
    0xbe0caaff: (List2, 0x0, Hash, 0x0)
    pass

class PersistentVfxData():
    FollowGroundTilt: (Bool, 0x0, 0x0, 0x0)
    BoneName: (String, 0x0, 0x0, 0x0)
    PlaySpeedModifier: (F32, 0x0, 0x0, 0x0)
    SpecificTeam: (U32, 0x0, 0x0, 0x0)
    EffectKeyForOtherTeam: (Hash, 0x0, 0x0, 0x0)
    Scale: (F32, 0x0, 0x0, 0x0)
    BindFlexToOwnerPar: (Bool, 0x0, 0x0, 0x0)
    UseDifferentKeyForOtherTeam: (Bool, 0x0, 0x0, 0x0)
    FaceTarget: (Bool, 0x0, 0x0, 0x0)
    AttachToCamera: (Bool, 0x0, 0x0, 0x0)
    EffectKey: (Hash, 0x0, 0x0, 0x0)
    TargetPosIsOwner: (Bool, 0x0, 0x0, 0x0)
    ShowToSpecificTeam: (Bool, 0x0, 0x0, 0x0)
    ShowToOwnerOnly: (Bool, 0x0, 0x0, 0x0)
    TargetBoneName: (String, 0x0, 0x0, 0x0)
    OrientTowardsTarget: (Bool, 0x0, 0x0, 0x0)
    pass

class ClearBit(IScriptBlock):
    BitIndex: (Pointer, 0x0, 0x0, IIntGet)
    BitField: (Embed, 0x0, 0x0, IntTableSet)
    pass

class IsDeadDynamicMaterialBoolDriver(ILogicBoolDriver, IDynamicMaterialBoolDriver):
    pass

class HudLoadingScreenData():
    mLoadingSpinnerRows: (U8, 0x0, 0x0, 0x0)
    mLoadingSpinnerSpeed: (F32, 0x0, 0x0, 0x0)
    mLoadingSpinnerFrames: (U8, 0x0, 0x0, 0x0)
    0x9d17e9e3: (Bool, 0x0, 0x0, 0x0)
    mProgressBarData: (Embed, 0x0, 0x0, HudLoadingScreenProgressBarData)
    pass

class 0xfacd8b68():
    ChampionNames: (List2, 0x0, String, 0x0)
    BoardPosition: (Embed, 0x0, 0x0, TftBoardPosition)
    pass

class 0xface6a25(BuffEffect):
    pass

class LongestLossOfControlTypeIntDriver(ILogicIntDriver):
    pass

class IPictureInPictureSource():
    pass

class IContextualConditionBuff(IContextualCondition):
    pass

class ItemAdviceReason():
    mReason: (String, 0x0, 0x0, 0x0)
    pass

class DestroyOnMovementComplete(MissileBehaviorSpec):
    RenderParticlesAfterDestroy: (Bool, 0x0, 0x0, 0x0)
    mDelay: (I32, 0x0, 0x0, 0x0)
    pass

class 0xfb16e4be(0xfd51006c):
    OrderTypes: (List2, 0x0, U8, 0x0)
    pass

class 0xfb1989a3():
    PickedVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    0x34296273: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    IdleVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    RefreshVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    NotPickedVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    RefreshOverlayVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    IconBackgroundPath: (String, 0x0, 0x0, 0x0)
    HoverVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    pass

class Turret(AnimatedBuilding):
    pass

class TooltipInstanceList():
    Elements: (List, 0x0, Embed, TooltipInstanceListElement)
    LevelCount: (U32, 0x0, 0x0, 0x0)
    pass

class RemapVec4MaterialDriver(ILogicDriver):
    OutputMinValue: (Vec4, 0x0, 0x0, 0x0)
    MaxValue: (Vec4, 0x0, 0x0, 0x0)
    OutputMaxValue: (Vec4, 0x0, 0x0, 0x0)
    Driver: (Pointer, 0x0, 0x0, ILogicDriver)
    MinValue: (Vec4, 0x0, 0x0, 0x0)
    pass

class ReplayControlsViewController(ViewController):
    TooltipHandle: (Hash, 0x0, 0x0, 0x0)
    SpeedUp: (Embed, 0x0, 0x0, ReplayControlsButton)
    BackdropLite: (Hash, 0x0, 0x0, 0x0)
    RecordingCompleteToPathMessage: (String, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    Record: (Embed, 0x0, 0x0, ReplayControlsButton)
    SkipBack: (Embed, 0x0, 0x0, ReplayControlsButton)
    ReplaySlider: (Embed, 0x0, 0x0, HudReplaySlider)
    PlaybackSpeedTextHandle: (Hash, 0x0, 0x0, 0x0)
    MessageTextHandle: (Hash, 0x0, 0x0, 0x0)
    RecordingErrorMessage: (String, 0x0, 0x0, 0x0)
    BackdropFull: (Hash, 0x0, 0x0, 0x0)
    SpeedDown: (Embed, 0x0, 0x0, ReplayControlsButton)
    RecordingActiveMessage: (String, 0x0, 0x0, 0x0)
    Play: (Embed, 0x0, 0x0, ReplayControlsButton)
    MessageDisplayDurationSecs: (F32, 0x0, 0x0, 0x0)
    SceneHandle: (Hash, 0x0, 0x0, 0x0)
    pass

class ISequenceActionInstance():
    pass

class HeroStatData():
    MultipleRoundCombinationRule: (U32, 0x0, 0x0, 0x0)
    StatType: (String, 0x0, 0x0, 0x0)
    StatType: (U32, 0x0, 0x0, 0x0)
    StatName: (String, 0x0, 0x0, 0x0)
    SumMultipleRoundsAtEog: (Bool, 0x0, 0x0, 0x0)
    MultipleRoundCombinationRuleAtEog: (U32, 0x0, 0x0, 0x0)
    ModeInclusions: (U32, 0x0, 0x0, 0x0)
    pass

class 0xfbad517f(TargetingTypeData):
    pass

class CherryRoundsViewController(0x856ba9bc, ViewController):
    TimerText: (Hash, 0x0, 0x0, 0x0)
    Scene: (Hash, 0x0, 0x0, 0x0)
    TimerFillTexture: (Hash, 0x0, 0x0, 0x0)
    LeftPhaseIcons: (List, 0x3, Embed, 0x9784901f)
    LeftPhaseIcons: (List, 0x3, Hash, 0x0)
    RoundLabelTra: (String, 0x0, 0x0, 0x0)
    0x3aa6852c: (Hash, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    TimerLeftBar: (Embed, 0x0, 0x0, 0x5b5e6994)
    CurrentPhaseIcon: (Embed, 0x0, 0x0, 0x9784901f)
    CurrentPhaseIcon: (Hash, 0x0, 0x0, 0x0)
    RoundLabel: (Hash, 0x0, 0x0, 0x0)
    0x580dfb9d: (F32, 0x0, 0x0, 0x0)
    Timer: (Hash, 0x0, 0x0, 0x0)
    PhaseLabel: (Hash, 0x0, 0x0, 0x0)
    RightPhaseIcons: (List, 0x3, Embed, 0x9784901f)
    RightPhaseIcons: (List, 0x3, Hash, 0x0)
    TimerTextDefaultColor: (Color, 0x0, 0x0, 0x0)
    StageNumber: (Hash, 0x0, 0x0, 0x0)
    0xa2e2709c: (String, 0x0, 0x0, 0x0)
    0xb03d7e4b: (Color, 0x0, 0x0, 0x0)
    0xb1f34e3f: (Embed, 0x0, 0x0, 0xf2dd2d14)
    TimerRightBar: (Embed, 0x0, 0x0, 0x5b5e6994)
    TimerFillLeftTexture: (Hash, 0x0, 0x0, 0x0)
    0xcf3fe190: (Hash, 0x0, 0x0, 0x0)
    0xd24a0877: (Map, U8, String, 0x0)
    TimerFillRightTexture: (Hash, 0x0, 0x0, 0x0)
    0xda3e6b10: (String, 0x0, 0x0, 0x0)
    0xe527f39d: (Hash, 0x0, 0x0, 0x0)
    TooltipAnchor: (Hash, 0x0, 0x0, 0x0)
    PlaceholderCombatText: (Hash, 0x0, 0x0, 0x0)
    pass

class HasSkillPointRequirement(ISpellRankUpRequirement):
    pass

class HudTeamFightOffScreenDifferentiationData():
    mPlayerOffscreenAlphaValue: (F32, 0x0, 0x0, 0x0)
    mPlayerOffscreenAlphaValue: (U8, 0x0, 0x0, 0x0)
    mNearlyOnScreenRange: (F32, 0x0, 0x0, 0x0)
    mPlayerOffscreenTimer: (F32, 0x0, 0x0, 0x0)
    pass

class SpecialOfferController():
    StoreListingData: (Link, 0x0, 0x0, StoreListingData)
    pass

class RenderStyleData():
    mUnitFilterParamsExterior: (Embed, 0x0, 0x0, ToonInkingFilterParams)
    mUnitFilterParamsInterior: (Embed, 0x0, 0x0, ToonInkingFilterParams)
    mUnitStyleUntextured: (Bool, 0x0, 0x0, 0x0)
    mWorldStyleUntextured: (Bool, 0x0, 0x0, 0x0)
    mUnitStyleUseInking: (Bool, 0x0, 0x0, 0x0)
    pass

class MutatorEnabler(IEnabler):
    Mutator: (String, 0x0, 0x0, 0x0)
    pass

class ContextualSituation():
    mRules: (List, 0x0, Embed, ContextualRule)
    mChooseRandomValidRule: (Bool, 0x0, 0x0, 0x0)
    mCoolDownTime: (F32, 0x0, 0x0, 0x0)
    pass

class UiElementGroupButtonSoundEvents():
    RollOutEvent: (String, 0x0, 0x0, 0x0)
    MouseDownOnInactive: (String, 0x0, 0x0, 0x0)
    MouseDownSelected: (String, 0x0, 0x0, 0x0)
    MouseUpEvent: (String, 0x0, 0x0, 0x0)
    RolloverEvent: (String, 0x0, 0x0, 0x0)
    MouseUpSelected: (String, 0x0, 0x0, 0x0)
    MouseUpOnInactive: (String, 0x0, 0x0, 0x0)
    MouseDownEvent: (String, 0x0, 0x0, 0x0)
    pass

class 0xfc331f53():
    AugmentLayout: (Hash, 0x0, 0x0, 0x0)
    AugmentSlotData: (Embed, 0x0, 0x0, AugmentSlot)
    pass

class EsportsBannerMaterialController(SkinnedMeshDataMaterialController):
    pass

class LolModesTeamDisplayData():
    0x179db98: (String, 0x0, 0x0, 0x0)
    0x1cb3b8e6: (String, 0x0, 0x0, 0x0)
    0x1ef5b158: (String, 0x0, 0x0, 0x0)
    0x20e0b520: (String, 0x0, 0x0, 0x0)
    TeamMatchupIconPath: (String, 0x0, 0x0, 0x0)
    0x33f929a8: (String, 0x0, 0x0, 0x0)
    LoadingScreenData: (Pointer, 0x0, 0x0, 0x79ca73e7)
    TeamIconPath: (String, 0x0, 0x0, 0x0)
    0x581ad352: (String, 0x0, 0x0, 0x0)
    0x59fbc855: (String, 0x0, 0x0, 0x0)
    TeamEliminatedIconPath: (String, 0x0, 0x0, 0x0)
    0x7dbd6ef1: (String, 0x0, 0x0, 0x0)
    0x9290be1: (String, 0x0, 0x0, 0x0)
    0x95fd5384: (String, 0x0, 0x0, 0x0)
    0x95fde6c5: (String, 0x0, 0x0, 0x0)
    0xabb1919f: (String, 0x0, 0x0, 0x0)
    0xb94c1f8e: (String, 0x0, 0x0, 0x0)
    TeamDisplayNameTra: (String, 0x0, 0x0, 0x0)
    0xbfdc3540: (String, 0x0, 0x0, 0x0)
    0xc73349d0: (String, 0x0, 0x0, 0x0)
    0xf4186080: (String, 0x0, 0x0, 0x0)
    pass

class VfxPrimitiveMeshBase(VfxPrimitiveBase):
    0x6aec9e7a: (Bool, 0x0, 0x0, 0x0)
    AlignYawToCamera: (Bool, 0x0, 0x0, 0x0)
    AlignPitchToCamera: (Bool, 0x0, 0x0, 0x0)
    mMesh: (Embed, 0x0, 0x0, VfxMeshDefinitionData)
    mAlignYawToCamera: (Bool, 0x0, 0x0, 0x0)
    mAlignPitchToCamera: (Bool, 0x0, 0x0, 0x0)
    pass

class FxActionMoveResetInstance(IFxActionInstance):
    pass

class CharacterPreloadData():
    mCharacter: (Hash, 0x0, 0x0, 0x0)
    mSkinId: (U32, 0x0, 0x0, 0x0)
    pass

class RoleOpponentEquivalentChallengeConstraintInfo(ListenerConstraintInfo):
    pass

class 0xfc6af367():
    PickedVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    0x34296273: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    0x3c66a261: (String, 0x0, 0x0, 0x0)
    0x56fabff4: (String, 0x0, 0x0, 0x0)
    IdleVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    RefreshVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    NotPickedVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    0x8371223f: (String, 0x0, 0x0, 0x0)
    RefreshOverlayVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    0x941f723a: (String, 0x0, 0x0, 0x0)
    0xb95f539d: (String, 0x0, 0x0, 0x0)
    0xd908f898: (String, 0x0, 0x0, 0x0)
    HoverVfxSystem: (Link, 0x0, 0x0, VfxSystemDefinitionData)
    pass

class WardData(BaseLoadoutData):
    WardSkinId: (U32, 0x0, 0x0, 0x0)
    pass

class Relic(BasePerk):
    0xdc503ca6: (Bool, 0x0, 0x0, 0x0)
    pass

class MaterialInstanceSamplerDef():
    UncensoredTextures: (Map, Hash, String, 0x0)
    TextureName: (String, 0x0, 0x0, 0x0)
    pass

class SequencePhase():
    Type: (U32, 0x0, 0x0, 0x0)
    Name: (String, 0x0, 0x0, 0x0)
    DefaultDuration: (F32, 0x0, 0x0, 0x0)
    pass

class DamageSkinLoadoutGridButtonData(LoadoutGridButtonData):
    FavoriteIcon: (Hash, 0x0, 0x0, 0x0)
    RarityIcon: (List, 0x0, Hash, 0x0)
    pass

class IFunctionGet(IScriptValueGet):
    pass

class HudHealthBarBurstHealData():
    HealFadeDuration: (F32, 0x0, 0x0, 0x0)
    HealTimeWindow: (F32, 0x0, 0x0, 0x0)
    HealTriggerPercent: (F32, 0x0, 0x0, 0x0)
    pass

class 0xfd51006c(ILogicBoolDriver):
    DelayOrder: (Bool, 0x0, 0x0, 0x0)
    pass

class PfxAnimatedVector3fVariableData():
    Values: (List, 0x0, Vec3, 0x0)
    Times: (List, 0x0, F32, 0x0)
    ProbabilityTables: (List, 0x3, Pointer, PfxProbabilityTableData)
    pass

class OptionTemplateMuteButton(IOptionTemplate):
    ButtonDefinition: (Hash, 0x0, 0x0, 0x0)
    pass

class SetTableValueBlock(IBlock, IScriptBlock):
    Value: (Pointer, 0x0, 0x0, IRsValueGet)
    Value: (Pointer, 0x0, 0x0, IScriptValueGet)
    Dest: (Embed, 0x0, 0x0, ScriptTableSet)
    Destination: (Embed, 0x0, 0x0, RsTableSet)
    Destination: (Embed, 0x0, 0x0, ScriptTableSet)
    pass

class HasReceivedAnimationEventBoolDriver(ILogicBoolDriver):
    EventName: (Hash, 0x0, 0x0, 0x0)
    pass

class PingRadialBaseViewController(RadialMenuViewController):
    CategoryTextOnHoverOnly: (Bool, 0x0, 0x0, 0x0)
    EnableCenterActivateDefaultPing: (Bool, 0x0, 0x0, 0x0)
    PingCategories: (List, 0x0, Embed, PingRadialBaseCategoryDefinition)
    ObjectName: (String, 0x0, 0x0, 0x0)
    CenterOverrides: (List, 0x0, Embed, PingRadialBaseDefaultCommandDefinition)
    0xf2df8264: (Map, U8, String, 0x0)
    pass

class TftArenaOwnerStreakParametricUpdater(IFloatParametricUpdater):
    pass

class IFxActionInstance():
    pass

class HudCenterFrameGlowData():
    0xcdeba821: (F32, 0x0, 0x0, 0x0)
    EaseType: (U8, 0x0, 0x0, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class TftScoreboardDelays():
    CombatStateSlideInTimeSecs: (F32, 0x0, 0x0, 0x0)
    WinStreakLevel1LoopStartDelaySecs: (F32, 0x0, 0x0, 0x0)
    WinStreakLevel2LoopStartDelaySecs: (F32, 0x0, 0x0, 0x0)
    pass

class TftArmoryItemTraitData():
    Name: (Hash, 0x0, 0x0, 0x0)
    Backgrounds: (Map, U32, Hash, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    pass

class MatchHistoryUnitTemplate():
    Group: (Hash, 0x0, 0x0, 0x0)
    OneStar: (Hash, 0x0, 0x0, 0x0)
    TwoStar: (Hash, 0x0, 0x0, 0x0)
    ThreeStar: (Hash, 0x0, 0x0, 0x0)
    IconFrame: (Hash, 0x0, 0x0, 0x0)
    ItemIcons: (List, 0x3, Hash, 0x0)
    Icon: (Hash, 0x0, 0x0, 0x0)
    TooltipButton: (Hash, 0x0, 0x0, 0x0)
    pass

class TftTrovesBannerCurrencyReward(TftTrovesBannerReward):
    CurrencyId: (String, 0x0, 0x0, 0x0)
    NameTraKey: (String, 0x0, 0x0, 0x0)
    pass

class LuaPropertyDataInteger(LuaPropertyData):
    Value: (I32, 0x0, 0x0, 0x0)
    pass

class VfxPrimitiveCameraUnitQuad(VfxPrimitiveBase):
    pass

class StrawberryAugmentSelectionViewController(ViewController):
    0x23de7775: (String, 0x0, 0x0, 0x0)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MainScene: (Hash, 0x0, 0x0, 0x0)
    AugmentSelectionGrid: (Hash, 0x0, 0x0, 0x0)
    0x56592fa3: (U32, 0x0, 0x0, 0x0)
    0x583ec19b: (String, 0x0, 0x0, 0x0)
    TimeoutPreventClicksOnShow: (F32, 0x0, 0x0, 0x0)
    0x6da1a863: (Embed, 0x0, 0x0, 0xfc6af367)
    0x760d1e6a: (String, 0x0, 0x0, 0x0)
    0x8371223f: (String, 0x0, 0x0, 0x0)
    0xa040493d: (String, 0x0, 0x0, 0x0)
    MaxAugmentSlots: (U32, 0x0, 0x0, 0x0)
    0xce64b8ab: (Embed, 0x0, 0x0, 0xfc6af367)
    0xd93a5b65: (Embed, 0x0, 0x0, 0xfc6af367)
    0xdcf99336: (String, 0x0, 0x0, 0x0)
    AugmentSlotData: (Embed, 0x0, 0x0, StrawberryAugmentSlotData)
    0xf8d5ccda: (Embed, 0x0, 0x0, 0xfc6af367)
    pass

class ContextualConditionNumberOfCharactersNearTargetPos(IContextualCondition, ICharacterSubcondition):
    mCompareOp: (U8, 0x0, 0x0, 0x0)
    mNumberOfCharacters: (U32, 0x0, 0x0, 0x0)
    mNumberOfAllies: (U32, 0x0, 0x0, 0x0)
    mTeamCompareOp: (U8, 0x0, 0x0, 0x0)
    pass

class 0xfde8af7f(IFxAction):
    Object: (Embed, 0x0, 0x0, FxObjectSelector)
    AttachToLocation: (Pointer, 0x0, 0x0, IFxLocation)
    AttachOrientation: (Bool, 0x0, 0x0, 0x0)
    pass

class VfxAnimatedFloatVariableData(VfxFloatBase):
    Values: (List, 0x0, F32, 0x0)
    Times: (List, 0x0, F32, 0x0)
    ProbabilityTables: (List, 0x1, Pointer, VfxProbabilityTableData)
    pass

class PoiFadeData():
    FullVisTimeSecs: (F32, 0x0, 0x0, 0x0)
    MinAlphaTimeSecs: (F32, 0x0, 0x0, 0x0)
    FadeDownTimeSecs: (F32, 0x0, 0x0, 0x0)
    FadeupTimeSecs: (F32, 0x0, 0x0, 0x0)
    pass

class RelicLoadoutData(BaseLoadoutData):
    mRelics: (List, 0x0, Hash, 0x0)
    pass

class 0xfe31ac4d(0xc06f5f6a):
    Source: (Link, 0x0, 0x0, SequenceObjectSelector)
    DebugOverride: (Hash, 0x0, 0x0, 0x0)
    pass

class ContextualConditionNearbyChampionCount(IContextualCondition):
    mCompareOp: (U8, 0x0, 0x0, 0x0)
    mCount: (U32, 0x0, 0x0, 0x0)
    mTeamCompareOp: (U8, 0x0, 0x0, 0x0)
    pass

class ItemRecommendationContext():
    mStartingItems: (List, 0x0, Hash, 0x0)
    mMapStringId: (Hash, 0x0, 0x0, 0x0)
    mModeNameStringId: (Hash, 0x0, 0x0, 0x0)
    mPosition: (Hash, 0x0, 0x0, 0x0)
    mItemPath: (Embed, 0x0, 0x0, ItemRecommendationPath)
    mPopularItems: (List, 0x0, Hash, 0x0)
    mStartingItemMatrix: (Embed, 0x0, 0x0, ItemRecommendationMatrix)
    mMapId: (U32, 0x0, 0x0, 0x0)
    mChampionId: (I32, 0x0, 0x0, 0x0)
    mChampionId: (U32, 0x0, 0x0, 0x0)
    mCompletedItemMatrix: (Embed, 0x0, 0x0, ItemRecommendationMatrix)
    mIsDefaultPosition: (Bool, 0x0, 0x0, 0x0)
    mStartingItemBundles: (List, 0x0, Embed, ItemRecommendationItemList)
    UpgradeChoices: (Map, U32, Embed, ItemRecommendationItemList)
    mItemMatrix: (Embed, 0x0, 0x0, ItemRecommendationMatrix)
    pass

class NeutralMinionCamp(NeutralMinionCampCommon):
    pass

class 0xfe897399():
    Name: (String, 0x0, 0x0, 0x0)
    RunOnce: (Bool, 0x0, 0x0, 0x0)
    pass

class MapActionTftCameraShake(MapAction):
    Duration: (F32, 0x0, 0x0, 0x0)
    Magnitude: (F32, 0x0, 0x0, 0x0)
    0x728fa513: (Bool, 0x0, 0x0, 0x0)
    ShakesPerSecond: (F32, 0x0, 0x0, 0x0)
    FalloffRate: (F32, 0x0, 0x0, 0x0)
    Direction: (Vec3, 0x0, 0x0, 0x0)
    pass

class 0xfeacedf2(0x30aa7360):
    ValueDriver: (Pointer, 0x0, 0x0, ILogicFloatDriver)
    0x7a721423: (List2, 0x0, Pointer, 0x9a573886)
    0x94eea539: (List2, 0x0, Pointer, 0xbc413e21)
    pass

class TftCharacterRoleCardViewController(ViewController):
    Scene: (Hash, 0x0, 0x0, 0x0)
    ItemData: (Embed, 0x0, 0x0, TftCharacterRoleCardItem)
    BaseLoadable: (Link, 0x0, 0x0, UiPropertyLoadable)
    MobileOverrideLoadable: (Link, 0x0, 0x0, UiPropertyOverrideLoadable)
    HeaderData: (Embed, 0x0, 0x0, TftCharacterRoleCardHeader)
    HeaderData: (Embed, 0x0, 0x0, TftCharacterRoleCardHeaderData)
    ItemRows: (List, 0x0, Embed, TftCharacterRoleCardItemRowData)
    Grid: (Hash, 0x0, 0x0, 0x0)
    Layout: (Hash, 0x0, 0x0, 0x0)
    pass

class FxActionSfxBeam(FxActionSfxBase):
    MidpointEvent: (Embed, 0x0, 0x0, FxSfxBeamEvent)
    Target: (Pointer, 0x0, 0x0, IFxLocation)
    EndpointEvent: (Embed, 0x0, 0x0, FxSfxBeamEvent)
    Location: (Pointer, 0x0, 0x0, IFxLocation)
    pass

class TriggerFromScript(MissileTriggerSpec):
    mDelay: (F32, 0x0, 0x0, 0x0)
    mTriggerName: (Hash, 0x0, 0x0, 0x0)
    mTriggerName: (String, 0x0, 0x0, 0x0)
    pass

class ItemScriptEvent(IScriptEvent):
    pass

class FloatTextDisplayOverrides():
    DisableHorizontalReverse: (Option, 0x0, Bool, 0x0)
    CombinableTextShowCrit: (Option, 0x0, Bool, 0x0)
    RandomOffsetMaxY: (Option, 0x0, F32, 0x0)
    RandomOffsetMaxX: (Option, 0x0, F32, 0x0)
    IgnoreCombineRules: (Option, 0x0, Bool, 0x0)
    MinYVelocity: (Option, 0x0, F32, 0x0)
    RelativeOffsetMin: (Option, 0x0, F32, 0x0)
    CombinableCounterDisplay: (Option, 0x0, Bool, 0x0)
    CombinableCounterCategory: (Option, 0x0, I32, 0x0)
    MinScale: (Option, 0x0, F32, 0x0)
    RelativeOffsetMax: (Option, 0x0, F32, 0x0)
    GrowthYScalar: (Option, 0x0, F32, 0x0)
    OverwritePreviousNumber: (Option, 0x0, Bool, 0x0)
    MaxInstances: (Option, 0x0, I32, 0x0)
    ExtendTimeOnNewDamage: (Option, 0x0, F32, 0x0)
    MinXVelocity: (Option, 0x0, F32, 0x0)
    Scale: (Option, 0x0, F32, 0x0)
    HangTime: (Option, 0x0, F32, 0x0)
    Priority: (Option, 0x0, I32, 0x0)
    MaxXVelocity: (Option, 0x0, F32, 0x0)
    MaxLifeTime: (Option, 0x0, F32, 0x0)
    ShrinkTime: (Option, 0x0, F32, 0x0)
    MaxScale: (Option, 0x0, F32, 0x0)
    ContinualForceY: (Option, 0x0, F32, 0x0)
    ShrinkScale: (Option, 0x0, F32, 0x0)
    ContinualForceX: (Option, 0x0, F32, 0x0)
    StartOffsetX: (Option, 0x0, F32, 0x0)
    StartOffsetY: (Option, 0x0, F32, 0x0)
    MomentumFromHit: (Option, 0x0, Bool, 0x0)
    IsAnimated: (Option, 0x0, Bool, 0x0)
    MaxYVelocity: (Option, 0x0, F32, 0x0)
    AlternateRightLeft: (Option, 0x0, Bool, 0x0)
    DecayDelay: (Option, 0x0, F32, 0x0)
    RandomOffsetMinY: (Option, 0x0, F32, 0x0)
    RandomOffsetMinX: (Option, 0x0, F32, 0x0)
    Decay: (Option, 0x0, F32, 0x0)
    DisableVerticalReverse: (Option, 0x0, Bool, 0x0)
    GrowthXScalar: (Option, 0x0, F32, 0x0)
    FollowSource: (Option, 0x0, Bool, 0x0)
    ColorOffsetB: (Option, 0x0, I32, 0x0)
    ColorOffsetG: (Option, 0x0, I32, 0x0)
    IgnoreQueue: (Option, 0x0, Bool, 0x0)
    ColorOffsetR: (Option, 0x0, I32, 0x0)
    pass

class UnitLevelUiData():
    LevelText: (Hash, 0x0, 0x0, 0x0)
    pass

class HudInputBoxData():
    SelectedLineSizePx: (F32, 0x0, 0x0, 0x0)
    MarkedOffsetY: (F32, 0x0, 0x0, 0x0)
    MarkedLineSizePx: (F32, 0x0, 0x0, 0x0)
    SelectedOffsetY: (F32, 0x0, 0x0, 0x0)
    CaretBlinkTime: (F32, 0x0, 0x0, 0x0)
    InputTextLengthMax: (U8, 0x0, 0x0, 0x0)
    0xbeabf2d8: (F32, 0x0, 0x0, 0x0)
    CaretAlphaMax: (F32, 0x0, 0x0, 0x0)
    pass

class StaticMaterialDef(IResource, IMaterialDef):
    DefaultTechnique: (String, 0x0, 0x0, 0x0)
    Type: (U32, 0x0, 0x0, 0x0)
    SharedTextureSets: (List, 0x0, Embed, StaticMaterialSharedTextureDef)
    Techniques: (List, 0x0, Embed, StaticMaterialTechniqueDef)
    DynamicMaterial: (Pointer, 0x0, 0x0, DynamicMaterialDef)
    Name: (String, 0x0, 0x0, 0x0)
    ChildTechniques: (List, 0x0, Embed, StaticMaterialChildTechniqueDef)
    SamplerValues: (List, 0x0, Embed, StaticMaterialShaderSamplerDef)
    SamplerValues: (List2, 0x0, Embed, StaticMaterialShaderSamplerDef)
    ParamValues: (List, 0x0, Embed, StaticMaterialShaderParamDef)
    ParamValues: (List2, 0x0, Embed, StaticMaterialShaderParamDef)
    Switches: (List, 0x0, Embed, StaticMaterialSwitchDef)
    Switches: (List2, 0x0, Embed, StaticMaterialSwitchDef)
    ShaderMacros: (Map, String, String, 0x0)
    pass

class CustomChampionKillStatStoneData(StatStoneData):
    mKillEvent: (Hash, 0x0, 0x0, 0x0)
    pass

class BarracksLevelController(ILevelController, BaseLevelController):
    TriggerEventsOnInitialSpawn: (List2, 0x0, U32, 0x0)
    BarracksConfig: (Embed, 0x0, 0x0, BarracksConfig)
    LinkedBarracks: (List2, 0x0, Embed, BarracksLink)
    pass

class 0xffcac16f():
    BehaviorsData: (Map, String, Embed, 0x709bc2e4)
    pass

class HudAbilityPromptData():
    PulseInterval: (F32, 0x0, 0x0, 0x0)
    PulseTime: (F32, 0x0, 0x0, 0x0)
    PulseEndColor: (Color, 0x0, 0x0, 0x0)
    PulseStartColor: (Color, 0x0, 0x0, 0x0)
    PulseOffset: (Vec2, 0x0, 0x0, 0x0)
    pass

class AbilityResourcePipTypeMap():
    DefaultMediumPip: (Hash, 0x0, 0x0, 0x0)
    DefaultSmallPip: (Hash, 0x0, 0x0, 0x0)
    AdditionalPipTypes: (Map, Hash, Hash, 0x0)
    DefaultLargePip: (Hash, 0x0, 0x0, 0x0)
    DefaultEmptyPip: (Hash, 0x0, 0x0, 0x0)
    pass

class RsAndCondition(IRsCondition):
    Conditions: (List, 0x0, Pointer, IRsCondition)
    pass

