
class CustomizedField:
    def __init__(self,
                 enum: str = None,
                 file_path: bool = False,
                 file_ext: str = None,
                 description: str = None):
        self.enum = enum
        self.file_path = file_path
        self.file_ext = file_ext
        self.description = description


custom_attributes = {
    'AbyssObjects.dat': {
        'MetadataFile': CustomizedField(
            file_path=True,
        ),
    },
    'AchievementSetRewards.dat': {
        'NotificationIcon': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
    },
    'ActiveSkills.dat': {
        'Icon_DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
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
        'AIFile': CustomizedField(
            file_path=True,
            file_ext='.ai',
        ),
    },
    'AdditionalLifeScaling.dat': {
        'DatFile': CustomizedField(
            file_path=True,
            file_ext='.dat',
        ),
    },
    'AdvancedSkillsTutorial.dat': {
        'International_BK2File': CustomizedField(
            file_path=True,
            file_ext='.bk2',
        ),
        'China_BK2File': CustomizedField(
            file_path=True,
            file_ext='.bk2',
        ),
    },
    'AlternatePassiveSkills.dat': {
        'DDSIcon': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
    },
    'ArchetypeRewards.dat': {
        'BK2File': CustomizedField(
            file_path=True,
            file_ext='.BK2',
        ),
    },
    'Archetypes.dat': {
        'UIImageFile': CustomizedField(
            file_path=True,
        ),
        'TutorialVideo_BKFile': CustomizedField(
            file_path=True,
            file_ext='.bk',
        ),
        'BackgroundImageFile': CustomizedField(
            file_path=True,
        ),
        'ArchetypeImage': CustomizedField(
            file_path=True,
        ),
    },
    'AreaInfluenceDoodads.dat': {
        'AOFiles': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
    },
    'Ascendancy.dat': {
        'CoordinateRect': CustomizedField(
            description='Coordinates in "x1, y1, x2, y2" format',
        ),
        'OGGFile': CustomizedField(
            file_path=True,
            file_ext='.ogg',
        ),
    },
    'AtlasExiles.dat': {
        'Art': CustomizedField(
            file_path=True,
        ),
    },
    'AtlasNode.dat': {
        'DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
    },
    'AwardDisplay.dat': {
        'BackgroundImage': CustomizedField(
            file_path=True,
        ),
        'ForegroundImage': CustomizedField(
            file_path=True,
        ),
        'OGGFile': CustomizedField(
            file_ext='.ogg',
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
    'BestiaryEncounters.dat': {
        'MonsterSpawnerId': CustomizedField(
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
        'Safehouse_ARMFile': CustomizedField(
            file_path=True,
            file_ext='.arm',
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
    'BloodTypes.dat': {
        'PETFile1': CustomizedField(
            file_path=True,
            file_ext='.pet',
        ),
        'PETFile2': CustomizedField(
            file_path=True,
            file_ext='.pet',
        ),
        'PETFile3': CustomizedField(
            file_path=True,
            file_ext='.pet',
        ),
        'PETFile4': CustomizedField(
            file_path=True,
            file_ext='.pet',
        ),
        'PETFile5': CustomizedField(
            file_path=True,
            file_ext='.pet',
        ),
        'PETFile6': CustomizedField(
            file_path=True,
            file_ext='.pet',
        ),
        'PETFile7': CustomizedField(
            file_path=True,
            file_ext='.pet',
        ),
        'PETFile8': CustomizedField(
            file_path=True,
            file_ext='.pet',
        ),
        'PETFile9': CustomizedField(
            file_path=True,
            file_ext='.pet',
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
        'BuffDDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
        'EPKFiles1': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'EPKFiles2': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'EPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'ExtraArt': CustomizedField(
            file_path=True,
        ),
        'EPKFiles': CustomizedField(
            file_path=True,
            file_ext='.epk',
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
    'CharacterTextAudio.dat': {
        'SoundFile': CustomizedField(
            file_path=True,
            file_ext='.ogg',
        ),
    },
    'Characters.dat': {
        'AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'ACTFile': CustomizedField(
            file_path=True,
            file_ext='.act',
        ),
        'WeaponSpeed': CustomizedField(
            description='Attack Speed in milliseconds',
        ),
        'IntroSoundFile': CustomizedField(
            file_path=True,
            file_ext='.ogg',
        ),
    },
    'ChestClusters.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
    },
    'ChestEffects.dat': {
        'Normal_EPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'Normal_Closed_AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'Normal_Open_AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'Magic_EPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'Unique_EPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'Rare_EPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'Magic_Closed_AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'Unique_Closed_AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'Rare_Closed_AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'Magic_Open_AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'Unique_Open_AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'Rare_Open_AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
    },
    'Chests.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
        'AOFiles': CustomizedField(
            file_path=True,
            file_ext='.ao',
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
    'DamageParticleEffects.dat': {
        'PETFile': CustomizedField(
            file_path=True,
            file_ext='.pet',
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
    'DelveRooms.dat': {
        'ARMFile': CustomizedField(
            file_path=True,
            file_ext='.arm',
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
    'DropEffects.dat': {
        'AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
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
    'EnvironmentTransitions.dat': {
        'OTFiles': CustomizedField(
            file_path=True,
            file_ext='.ot',
        ),
    },
    'Environments.dat': {
        'Base_ENVFile': CustomizedField(
            file_path=True,
            file_ext='.env',
        ),
        'Corrupted_ENVFile': CustomizedField(
            file_path=True,
            file_ext='.env',
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
    'Footprints.dat': {
        'Active_AOFiles': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'Idle_AOFiles': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
    },
    'FragmentStashTabLayout.dat': {
        'Id': CustomizedField(
            file_path=True,
        ),
    },
    'GeometryChannel.dat': {
        'EPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
    },
    'Grandmasters.dat': {
        'GMFile': CustomizedField(
            file_path=True,
            file_ext='.gm',
        ),
        'AISFile': CustomizedField(
            file_path=True,
            file_ext='.ais',
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
    'GroundEffects.dat': {
        'AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
    },
    'HarvestCraftOptionIcons.dat': {
        'DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
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
        'AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'ObjectType': CustomizedField(
            enum='HARVEST_OBJECT_TYPES',
        ),
    },
    'HarvestSeedTypes.dat': {
        'AOFiles': CustomizedField(
            file_path=True,
            file_ext='.ao',
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
    'HeistAreas.dat': {
        'DGRFile': CustomizedField(
            file_path=True,
            file_ext='.dgr',
        ),
        'Blueprint_DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
    },
    'HeistChestRewardTypes.dat': {
        'Art': CustomizedField(
            file_path=True,
        ),
    },
    'HeistDoodadNPCs.dat': {
        'AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
    },
    'HeistIntroAreas.dat': {
        'DGRFile': CustomizedField(
            file_path=True,
            file_ext='.dgr',
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
        'AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
    },
    'HeistRevealingNPCs.dat': {
        'PortraitFile': CustomizedField(
            file_path=True,
        ),
    },
    'HeistRooms.dat': {
        'ARMFile': CustomizedField(
            file_path=True,
            file_ext='.arm',
        ),
    },
    'HideoutDoodads.dat': {
        'Variation_AOFiles': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'InheritsFrom': CustomizedField(
            file_path=True,
        ),
    },
    'Hideouts.dat': {
        'HideoutFile': CustomizedField(
            file_path=True,
            file_ext='.hideout',
        ),
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
        'PresentARMFile': CustomizedField(
            file_path=True,
            file_ext='.arm',
        ),
        'PastARMFile': CustomizedField(
            file_path=True,
            file_ext='.arm',
        ),
        'TSIFile': CustomizedField(
            file_path=True,
            file_ext='.tsi',
        ),
        'UIIcon': CustomizedField(
            file_path=True,
        ),
    },
    'ItemVisualEffect.dat': {
        'DaggerEPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'BowEPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'OneHandedMaceEPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'OneHandedSwordEPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'TwoHandedSwordEPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'TwoHandedStaffEPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'TwoHandedMaceEPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'OneHandedAxeEPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'TwoHandedAxeEPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'ClawEPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'PETFile': CustomizedField(
            file_path=True,
            file_ext='.pet',
        ),
    },
    'ItemVisualIdentity.dat': {
        'DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
        'AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'SoundEffectsKey': CustomizedField(
            description='Inventory sound effect',
        ),
        'AOFile2': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'MarauderSMFiles': CustomizedField(
            file_path=True,
            file_ext='.sm',
        ),
        'RangerSMFiles': CustomizedField(
            file_path=True,
            file_ext='.sm',
        ),
        'WitchSMFiles': CustomizedField(
            file_path=True,
            file_ext='.sm',
        ),
        'DuelistDexSMFiles': CustomizedField(
            file_path=True,
            file_ext='.sm',
        ),
        'TemplarSMFiles': CustomizedField(
            file_path=True,
            file_ext='.sm',
        ),
        'ShadowSMFiles': CustomizedField(
            file_path=True,
            file_ext='.sm',
        ),
        'ScionSMFiles': CustomizedField(
            file_path=True,
            file_ext='.sm',
        ),
        'SMFiles': CustomizedField(
            file_path=True,
            file_ext='.sm',
        ),
        'EPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
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
    'LabyrinthSecretEffects.dat': {
        'OTFile': CustomizedField(
            file_path=True,
            file_ext='.ot',
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
    'MapSeries.dat': {
        'BaseIcon_DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
        'Infected_DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
        'Shaper_DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
        'Elder_DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
        'Drawn_DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
    },
    'Melee.dat': {
        'SurgeEffect_EPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
    },
    'MeleeTrails.dat': {
        'EPKFile1': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'EPKFile2': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'AOFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
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
    'MicrotransactionCombineFormula.dat': {
        'BK2File': CustomizedField(
            file_path=True,
            file_ext='.bk2',
        ),
    },
    'MicrotransactionFireworksVariations.dat': {
        'AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
    },
    'MicrotransactionPeriodicCharacterEffectVariations.dat': {
        'AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
    },
    'MicrotransactionPortalVariations.dat': {
        'AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'MapAOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
    },
    'MicrotransactionRarityDisplay.dat': {
        'ImageFile': CustomizedField(
            file_path=True,
        ),
    },
    'MicrotransactionSocialFrameVariations.dat': {
        'BK2File': CustomizedField(
            file_path=True,
            file_ext='.bk2',
        ),
    },
    'MiscAnimated.dat': {
        'AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
    },
    'MiscEffectPacks.dat': {
        'EPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
        ),
        'PlayerOnly_EPKFile': CustomizedField(
            file_path=True,
            file_ext='.epk',
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
    'MissionTransitionTiles.dat': {
        'TDTFile': CustomizedField(
            file_path=True,
            file_ext='.tdt',
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
    'MonsterArmours.dat': {
        'ArtString_SMFile': CustomizedField(
            file_ext='.sm',
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
        'ACTFiles': CustomizedField(
            file_path=True,
            file_ext='.act',
        ),
        'AOFiles': CustomizedField(
            file_path=True,
            file_ext='.ao',
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
        'AISFile': CustomizedField(
            file_path=True,
            file_ext='.ais',
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
        'SinkAnimation_AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
    },
    'MTXSetBonus.dat': {
        'ArtFile': CustomizedField(
            file_path=True,
        ),
    },
    'Music.dat': {
        'SoundFile': CustomizedField(
            file_path=True,
            file_ext='.ogg',
        ),
        'BankFile': CustomizedField(
            file_ext='.bank',
        ),
    },
    'MysteryBoxes.dat': {
        'BK2File': CustomizedField(
            file_path=True,
            file_ext='.bk2',
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
    'NPCTextAudio.dat': {
        'Mono_AudioFile': CustomizedField(
            file_path=True,
            file_ext='.ogg',
        ),
        'Stereo_AudioFile': CustomizedField(
            file_path=True,
            file_ext='.ogg',
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
        'Icon_DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
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
        'AOFiles': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'InheritsFrom': CustomizedField(
            file_path=True,
        ),
        'Stuck_AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
        'Bounce_AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
    },
    'Prophecies.dat': {
        'OGGFile': CustomizedField(
            file_path=True,
            file_ext='.ogg',
        ),
    },
    'Quest.dat': {
        'Icon_DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
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
    'ShopCategory.dat': {
        'ClientJPGFile': CustomizedField(
            file_path=True,
            file_ext='.jpg',
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
    'ShrineSounds.dat': {
        'StereoSoundFile': CustomizedField(
            file_path=True,
            file_ext='.ogg',
        ),
        'MonoSoundFile': CustomizedField(
            file_path=True,
            file_ext='.ogg',
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
        'DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
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
    'SkillMorphDisplay.dat': {
        'DDSFiles': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
    },
    'SoundEffects.dat': {
        'SoundFile': CustomizedField(
            file_path=True,
            file_ext='.ogg',
        ),
        'SoundFile_2D': CustomizedField(
            file_path=True,
            file_ext='.ogg',
        ),
    },
    'SpecialRooms.dat': {
        'ARMFile': CustomizedField(
            file_path=True,
            file_ext='arm',
        ),
    },
    'SpecialTiles.dat': {
        'TDTFile': CustomizedField(
            file_path=True,
            file_ext='tdt',
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
    'Topologies.dat': {
        'DGRFile': CustomizedField(
            file_path=True,
            file_ext='.dgr',
        ),
    },
    'Tutorial.dat': {
        'UIFile': CustomizedField(
            file_path=True,
            file_ext='.ui',
        ),
    },
    'UITalkText.dat': {
        'OGGFile': CustomizedField(
            file_path=True,
            file_ext='.ogg',
        ),
    },
    'UniqueChests.dat': {
        'AOFile': CustomizedField(
            file_path=True,
            file_ext='.ao',
        ),
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
        'LoadingScreen_DDSFile': CustomizedField(
            file_path=True,
            file_ext='.dds',
        ),
        'Strongbox_RarityWeight': CustomizedField(
            description='Normal/Magic/Rare/Unique spawn distribution',
        ),
        'TSIFile': CustomizedField(
            file_path=True,
            file_ext='.tsi',
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
