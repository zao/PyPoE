
class CustomizedField:
    def __init__(self,
                 enum: str = None,
                 description: str = None):
        self.enum = enum
        self.description = description


custom_attributes = {
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
    'Ascendancy.dat': {
        'CoordinateRect': CustomizedField(
            description='Coordinates in "x1, y1, x2, y2" format',
        ),
    },
    'BaseItemTypes.dat': {
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
    'BestiaryRecipeComponent.dat': {
        'RarityKey': CustomizedField(
            enum='RARITY',
        ),
    },
    'BetrayalUpgrades.dat': {
        'BetrayalUpgradeSlotsKey': CustomizedField(
            enum='BETRAYAL_UPGRADE_SLOTS',
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
    'Chests.dat': {
        'Corrupt_AchievementItemsKey': CustomizedField(
            description='Achievement item granted on corruption',
        ),
        'CurrencyUse_AchievementItemsKey': CustomizedField(
            description='Achievement item checked on currency use',
        ),
        'Encounter_AchievementItemsKeys': CustomizedField(
            description='Achievement items granted on encounter',
        ),
    },
    'CurrencyItems.dat': {
        'FullStack_BaseItemTypesKey': CustomizedField(
            description='Full stack transforms into this item',
        ),
    },
    'DelveUpgrades.dat': {
        'DelveUpgradeTypeKey': CustomizedField(
            enum='DELVE_UPGRADE_TYPE',
        ),
    },
    'EffectivenessCostConstants.dat': {
        'Multiplier': CustomizedField(
            description='Rounded',
        ),
    },
    'Flasks.dat': {
        'RecoveryTime': CustomizedField(
            description='in 1/10 s',
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
    'HarvestObjects.dat': {
        'ObjectType': CustomizedField(
            enum='HARVEST_OBJECT_TYPES',
        ),
    },
    'ImpactSoundData.dat': {
        'Sound': CustomizedField(
            description='Located in Audio/SoundEffects. Format has SG removed and $(#) replaced with the number',
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
    'Mods.dat': {
        'Domain': CustomizedField(
            enum='MOD_DOMAIN',
        ),
        'GenerationType': CustomizedField(
            enum='MOD_GENERATION_TYPE',
        ),
    },
    'MonsterVarieties.dat': {
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
    'PassiveSkills.dat': {
        'PassiveSkillGraphId': CustomizedField(
            description='Id used by PassiveSkillGraph.psg',
        ),
    },
    'Scarabs.dat': {
        'ScarabType': CustomizedField(
            enum='SCARAB_TYPES',
        ),
    },
    'ShopPaymentPackage.dat': {
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
    'UniqueChests.dat': {
        'AppearanceChestsKey': CustomizedField(
            description='Uses this chest for it"s visuals',
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
    },
}
