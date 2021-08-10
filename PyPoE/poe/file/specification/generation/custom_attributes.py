
class CustomizedField:
    def __init__(self,
                 enum: str = None,
                 file_path: bool = False,
                 description: str = None):
        self.enum = enum
        self.file_path = file_path
        self.description = description


custom_attributes = {
    'AbyssObjects.dat': {
        'MetadataFile': CustomizedField(
            file_path=True,
        ),
    },
    'ActiveSkills.dat': {
        'SkillTotemId': CustomizedField(
            description='This links to SkillTotems.dat, but the number mayexceed the number of entries; in that case it is player skill.',
        ),
        'Input_StatKeys': CustomizedField(
            description='Stats that will modify this skill specifically',
        ),
        'Output_StatKeys': CustomizedField(
            description='Stat an input stat will be transformed into',
        ),
        'MinionActiveSkillTypes': CustomizedField(
            description='ActiveSkillTypes of skills of minions summoned by this skill',
        ),
    },
    'Archetypes.dat': {
        'UIImageFile': CustomizedField(
            file_path=True,
        ),
        'BackgroundImageFile': CustomizedField(
            file_path=True,
        ),
        'ArchetypeImage': CustomizedField(
            file_path=True,
        ),
    },
    'Ascendancy.dat': {
        'CoordinateRect': CustomizedField(
            description='Coordinates in "x1, y1, x2, y2" format',
        ),
    },
    'AtlasExiles.dat': {
        'Art': CustomizedField(
            file_path=True,
        ),
    },
    'AwardDisplay.dat': {
        'BackgroundImage': CustomizedField(
            file_path=True,
        ),
        'ForegroundImage': CustomizedField(
            file_path=True,
        ),
    },
    'BaseItemTypes.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
        'InheritsFrom': CustomizedField(
            file_path=True,
        ),
        'ModDomainsKey': CustomizedField(
            enum='MOD_DOMAIN',
        ),
        'VendorRecipe_AchievementItemsKeys': CustomizedField(
            description='Achievement check when selling this item to vendors',
        ),
        'Inflection': CustomizedField(
            description='the inflection identifier used for i18n in related fields',
        ),
        'FragmentBaseItemTypesKey': CustomizedField(
            description='the item which represents this item in the fragment stash tab',
        ),
        'Equip_AchievementItemsKey': CustomizedField(
            description='Achievement check when equipping this item',
        ),
    },
    'BestiaryCapturableMonsters.dat': {
        'IconSmall': CustomizedField(
            file_path=True,
        ),
        'Icon': CustomizedField(
            file_path=True,
        ),
    },
    'BestiaryFamilies.dat': {
        'Icon': CustomizedField(
            file_path=True,
        ),
        'IconSmall': CustomizedField(
            file_path=True,
        ),
        'Illustration': CustomizedField(
            file_path=True,
        ),
        'PageArt': CustomizedField(
            file_path=True,
        ),
        'FlavourText': CustomizedField(
            file_path=True,
        ),
    },
    'BestiaryGenus.dat': {
        'Icon': CustomizedField(
            file_path=True,
        ),
    },
    'BestiaryGroups.dat': {
        'Icon': CustomizedField(
            file_path=True,
        ),
        'IconSmall': CustomizedField(
            file_path=True,
        ),
    },
    'BestiaryRecipeComponent.dat': {
        'RarityKey': CustomizedField(
            enum='RARITY',
        ),
    },
    'BetrayalJobs.dat': {
        'Art': CustomizedField(
            file_path=True,
        ),
    },
    'BetrayalRanks.dat': {
        'RankImage': CustomizedField(
            file_path=True,
        ),
    },
    'BetrayalTargets.dat': {
        'Art': CustomizedField(
            file_path=True,
        ),
    },
    'BetrayalUpgrades.dat': {
        'ArtFile': CustomizedField(
            file_path=True,
        ),
        'BetrayalUpgradeSlotsKey': CustomizedField(
            enum='BETRAYAL_UPGRADE_SLOTS',
        ),
    },
    'BlightEncounterTypes.dat': {
        'Icon': CustomizedField(
            file_path=True,
        ),
    },
    'BlightRewardTypes.dat': {
        'Icon': CustomizedField(
            file_path=True,
        ),
    },
    'BlightTowers.dat': {
        'Icon': CustomizedField(
            file_path=True,
        ),
    },
    'Bloodlines.dat': {
        'SpawnWeight_Values': CustomizedField(
            description='0 disables',
        ),
    },
    'BuffDefinitions.dat': {
        'Maximum_StatsKey': CustomizedField(
            description='Stat that holds the maximum number for this buff',
        ),
        'Current_StatsKey': CustomizedField(
            description='Stat that holds the current number for this buff',
        ),
    },
    'BuffVisuals.dat': {
        'ExtraArt': CustomizedField(
            file_path=True,
        ),
    },
    'CharacterAudioEvents.dat': {
        'Goddess_CharacterTextAudioKeys': CustomizedField(
            description='For the Goddess Bound/Scorned/Unleashed unique',
        ),
        'JackTheAxe_CharacterTextAudioKeys': CustomizedField(
            description='For Jack the Axe unique',
        ),
    },
    'Characters.dat': {
        'WeaponSpeed': CustomizedField(
            description='Attack Speed in milliseconds',
        ),
    },
    'ChestClusters.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
    },
    'Chests.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
        'Corrupt_AchievementItemsKey': CustomizedField(
            description='Achievement item granted on corruption',
        ),
        'CurrencyUse_AchievementItemsKey': CustomizedField(
            description='Achievement item checked on currency use',
        ),
        'Encounter_AchievementItemsKeys': CustomizedField(
            description='Achievement items granted on encounter',
        ),
        'InheritsFrom': CustomizedField(
            file_path=True,
        ),
    },
    'ComponentAttributeRequirements.dat': {
        'BaseItemTypesKey': CustomizedField(
            file_path=True,
        ),
    },
    'ComponentCharges.dat': {
        'BaseItemTypesKey': CustomizedField(
            file_path=True,
        ),
    },
    'CurrencyItems.dat': {
        'FullStack_BaseItemTypesKey': CustomizedField(
            description='Full stack transforms into this item',
        ),
    },
    'DelveBiomes.dat': {
        'UIImage': CustomizedField(
            file_path=True,
        ),
        'Art2D': CustomizedField(
            file_path=True,
        ),
    },
    'DelveFeatures.dat': {
        'Image': CustomizedField(
            file_path=True,
        ),
    },
    'DelveUpgrades.dat': {
        'DelveUpgradeTypeKey': CustomizedField(
            enum='DELVE_UPGRADE_TYPE',
        ),
    },
    'DivinationCardArt.dat': {
        'VirtualFile': CustomizedField(
            file_path=True,
        ),
    },
    'EffectivenessCostConstants.dat': {
        'Multiplier': CustomizedField(
            description='Rounded',
        ),
    },
    'ElderMapBossOverride.dat': {
        'TerrainMetadata': CustomizedField(
            file_path=True,
        ),
    },
    'ExecuteGEAL.dat': {
        'MetadataIDs': CustomizedField(
            file_path=True,
        ),
    },
    'Flasks.dat': {
        'RecoveryTime': CustomizedField(
            description='in 1/10 s',
        ),
    },
    'FragmentStashTabLayout.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
    },
    'GrantedEffects.dat': {
        'AllowedActiveSkillTypes': CustomizedField(
            description='This support gem only supports active skills with at least one of these types',
        ),
        'AddedActiveSkillTypes': CustomizedField(
            description='This support gem adds these types to supported active skills',
        ),
        'ExcludedActiveSkillTypes': CustomizedField(
            description='This support gem does not support active skills with one of these types',
        ),
        'SupportsGemsOnly': CustomizedField(
            description='This support gem only supports active skills that come from gem items',
        ),
    },
    'GrantedEffectsPerLevel.dat': {
        'DamageEffectiveness': CustomizedField(
            description='Damage effectiveness based on 0 = 100%',
        ),
        'CooldownBypassType': CustomizedField(
            description='Charge type to expend to bypass cooldown (Endurance, Frenzy, Power, none)',
        ),
        'StatsKeys2': CustomizedField(
            description='Used with a value of one',
        ),
        'DamageMultiplier': CustomizedField(
            description='Damage multiplier in 1/10000 for attack skills',
        ),
        'StatInterpolationTypesKeys': CustomizedField(
            enum='STAT_INTERPOLATION_TYPES',
        ),
        'VaalSoulGainPreventionTime': CustomizedField(
            description='Time in milliseconds',
        ),
    },
    'HarvestCraftOptions.dat': {
        'PlainText': CustomizedField(
            description='Text without any tags for formatting',
        ),
    },
    'HarvestCraftTiers.dat': {
        'FrameImage': CustomizedField(
            file_path=True,
        ),
        'FrameHighlight': CustomizedField(
            file_path=True,
        ),
    },
    'HarvestObjects.dat': {
        'ObjectType': CustomizedField(
            enum='HARVEST_OBJECT_TYPES',
        ),
    },
    'HarvestStorageLayout.dat': {
        'Button': CustomizedField(
            file_path=True,
        ),
        'ButtonHighlight': CustomizedField(
            file_path=True,
        ),
    },
    'HeistChestRewardTypes.dat': {
        'Art': CustomizedField(
            file_path=True,
        ),
    },
    'HeistJobs.dat': {
        'RequiredSkillIcon': CustomizedField(
            file_path=True,
        ),
        'SkillIcon': CustomizedField(
            file_path=True,
        ),
    },
    'HeistLockType.dat': {
        'SkillIcon': CustomizedField(
            file_path=True,
        ),
    },
    'HeistNPCs.dat': {
        'PortraitFile': CustomizedField(
            file_path=True,
        ),
        'SilhouetteFile': CustomizedField(
            file_path=True,
        ),
        'ActiveNPCIcon': CustomizedField(
            file_path=True,
        ),
    },
    'HeistRevealingNPCs.dat': {
        'PortraitFile': CustomizedField(
            file_path=True,
        ),
    },
    'HideoutDoodads.dat': {
        'InheritsFrom': CustomizedField(
            file_path=True,
        ),
    },
    'Hideouts.dat': {
        'HideoutImage': CustomizedField(
            file_path=True,
        ),
    },
    'ImpactSoundData.dat': {
        'Sound': CustomizedField(
            description='Located in Audio/SoundEffects. Format has SG removed and $(#) replaced with the number',
        ),
    },
    'IncursionChestRewards.dat': {
        'Unknown0': CustomizedField(
            file_path=True,
        ),
    },
    'IncursionRooms.dat': {
        'UIIcon': CustomizedField(
            file_path=True,
        ),
    },
    'ItemVisualIdentity.dat': {
        'SoundEffectsKey': CustomizedField(
            description='Inventory sound effect',
        ),
    },
    'KillstreakThresholds.dat': {
        'MonsterVarietiesKey': CustomizedField(
            description='Monster that plays the effect, i.e. the "nova" etc.',
        ),
    },
    'LabyrinthIzaroChests.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
    },
    'LabyrinthRewardTypes.dat': {
        'ObjectPath': CustomizedField(
            file_path=True,
        ),
    },
    'LeagueInfo.dat': {
        'PanelImage': CustomizedField(
            file_path=True,
        ),
        'HeaderImage': CustomizedField(
            file_path=True,
        ),
        'Screenshots': CustomizedField(
            file_path=True,
        ),
        'ItemImages': CustomizedField(
            file_path=True,
        ),
        'HoverImages': CustomizedField(
            file_path=True,
        ),
        'BackgroundImage': CustomizedField(
            file_path=True,
        ),
    },
    'MapDevices.dat': {
        'InheritsFrom': CustomizedField(
            file_path=True,
        ),
    },
    'MapFragmentMods.dat': {
        'MapFragmentFamilies': CustomizedField(
            enum='MAP_FRAGMENT_FAMILIES',
        ),
    },
    'MapPins.dat': {
        'PositionX': CustomizedField(
            description='X starts at left side of image, can be negative',
        ),
        'PositionY': CustomizedField(
            description='Y starts at top side of image, can be negative',
        ),
    },
    'MetamorphosisMetaSkillTypes.dat': {
        'UnavailableArt': CustomizedField(
            file_path=True,
        ),
        'AvailableArt': CustomizedField(
            file_path=True,
        ),
    },
    'MetamorphosisRewardTypes.dat': {
        'Art': CustomizedField(
            file_path=True,
        ),
    },
    'MetamorphosisStashTabLayout.dat': {
        'ButtonImage': CustomizedField(
            file_path=True,
        ),
    },
    'MicrotransactionRarityDisplay.dat': {
        'ImageFile': CustomizedField(
            file_path=True,
        ),
    },
    'MiscObjects.dat': {
        'EffectVirtualPath': CustomizedField(
            file_path=True,
        ),
    },
    'MissionTimerTypes.dat': {
        'Image': CustomizedField(
            file_path=True,
        ),
        'BackgroundImage': CustomizedField(
            file_path=True,
        ),
    },
    'Mods.dat': {
        'Domain': CustomizedField(
            enum='MOD_DOMAIN',
        ),
        'GenerationType': CustomizedField(
            enum='MOD_GENERATION_TYPE',
        ),
    },
    'MonsterSpawnerGroups.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
    },
    'MonsterVarieties.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
        'BaseMonsterTypeIndex': CustomizedField(
            file_path=True,
        ),
        'ModelSizeMultiplier': CustomizedField(
            description='in percent',
        ),
        'ExperienceMultiplier': CustomizedField(
            description='in percent',
        ),
        'DamageMultiplier': CustomizedField(
            description='in percent',
        ),
        'LifeMultiplier': CustomizedField(
            description='in percent',
        ),
        'AttackSpeed': CustomizedField(
            description='in ms',
        ),
    },
    'MTXSetBonus.dat': {
        'ArtFile': CustomizedField(
            file_path=True,
        ),
    },
    'NPCDialogueStyles.dat': {
        'HeaderBaseFile': CustomizedField(
            file_path=True,
        ),
        'ButtomFile': CustomizedField(
            file_path=True,
        ),
        'BannerFiles': CustomizedField(
            file_path=True,
        ),
        'HeaderFiles': CustomizedField(
            file_path=True,
        ),
    },
    'NPCs.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
        'Metadata': CustomizedField(
            file_path=True,
        ),
        'PortraitFile': CustomizedField(
            file_path=True,
        ),
    },
    'PackFormation.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
    },
    'PantheonPanelLayout.dat': {
        'CoverImage': CustomizedField(
            file_path=True,
        ),
        'SelectionImage': CustomizedField(
            file_path=True,
        ),
    },
    'PassiveSkills.dat': {
        'PassiveSkillGraphId': CustomizedField(
            description='Id used by PassiveSkillGraph.psg',
        ),
    },
    'PassiveTreeExpansionJewels.dat': {
        'Art': CustomizedField(
            file_path=True,
        ),
    },
    'Pet.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
    },
    'Projectiles.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
        'InheritsFrom': CustomizedField(
            file_path=True,
        ),
    },
    'RecipeUnlockObjects.dat': {
        'InheritsFrom': CustomizedField(
            file_path=True,
        ),
    },
    'Scarabs.dat': {
        'ScarabType': CustomizedField(
            enum='SCARAB_TYPES',
        ),
    },
    'ShopPaymentPackage.dat': {
        'BackgroundImage': CustomizedField(
            file_path=True,
        ),
        'PhysicalItemPoints': CustomizedField(
            description='Number of points the user gets back if they opt-out of physical items',
        ),
        'ShopPackagePlatformKeys': CustomizedField(
            enum='SHOP_PACKAGE_PLATFORM',
        ),
    },
    'ShrineBuffs.dat': {
        'BuffStatValues': CustomizedField(
            description='For use for the related stat in the buff.',
        ),
    },
    'Shrines.dat': {
        'SummonMonster_MonsterVarietiesKey': CustomizedField(
            description='The aoe ground effects for example',
        ),
        'SummonPlayer_MonsterVarietiesKey': CustomizedField(
            description='The aoe ground effects for example',
        ),
    },
    'SigilDisplay.dat': {
        'Inactive_ArtFile': CustomizedField(
            file_path=True,
        ),
        'Active_ArtFile': CustomizedField(
            file_path=True,
        ),
        'Frame_ArtFile': CustomizedField(
            file_path=True,
        ),
    },
    'StrDexIntMissionExtraRequirement.dat': {
        'TimeLimit': CustomizedField(
            description='in milliseconds',
        ),
        'TimeLimitBonusFromObjective': CustomizedField(
            description='in milliseconds',
        ),
    },
    'SupporterPackSets.dat': {
        'ShopPackagePlatformKey': CustomizedField(
            enum='SHOP_PACKAGE_PLATFORM',
        ),
    },
    'SynthesisAreas.dat': {
        'ArtFile': CustomizedField(
            file_path=True,
        ),
    },
    'SynthesisRewardTypes.dat': {
        'ArtFile': CustomizedField(
            file_path=True,
        ),
    },
    'UniqueChests.dat': {
        'AppearanceChestsKey': CustomizedField(
            description='Uses this chest for it"s visuals',
        ),
    },
    'UniqueStashTypes.dat': {
        'Image': CustomizedField(
            file_path=True,
        ),
    },
    'WeaponTypes.dat': {
        'Speed': CustomizedField(
            description='1000 / speed -> attacks per second',
        ),
    },
    'Words.dat': {
        'WordlistsKey': CustomizedField(
            enum='WORDLISTS',
        ),
        'Inflection': CustomizedField(
            description='the inflection identifier used for i18n in related fields',
        ),
    },
    'WorldAreas.dat': {
        'Strongbox_RarityWeight': CustomizedField(
            description='Normal/Magic/Rare/Unique spawn distribution',
        ),
        'FirstEntry_NPCsKey': CustomizedField(
            file_path=True,
        ),
    },
    'WorldPopupIconTypes.dat': {
        'Unknown0': CustomizedField(
            file_path=True,
        ),
        'Unknown1': CustomizedField(
            file_path=True,
        ),
        'Unknown2': CustomizedField(
            file_path=True,
        ),
    },
}
