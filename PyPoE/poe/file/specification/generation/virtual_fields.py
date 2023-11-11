from collections import defaultdict

from PyPoE.poe.constants import VERSION
from PyPoE.poe.file.specification.fields import VirtualField

virtual_fields_mappings = {
    VERSION.STABLE: defaultdict(
        list[VirtualField],
        {
            "BlightCraftingItems": [
                VirtualField(
                    name="BaseItemTypesKey",
                    fields=("Oil",),
                    alias=True,
                ),
            ],
            "BuffDefinitions": [
                VirtualField(
                    name="Binary_StatsKeys",
                    fields=("BinaryStats",),
                    alias=True,
                ),
            ],
            "CraftingBenchOptions": [
                VirtualField(
                    name="Cost",
                    fields=("Cost_BaseItemTypes", "Cost_Values"),
                    zip=True,
                ),
                VirtualField(
                    name="AddModOrEnchantment",
                    fields=("AddMod", "AddEnchantment"),
                ),
            ],
            "DelveUpgrades": [
                VirtualField(
                    name="Stats",
                    fields=("StatsKeys", "StatValues"),
                    zip=True,
                ),
            ],
            "GrantedEffectsPerLevel": [
                VirtualField(
                    name="StatValues",
                    fields=(
                        "Stat1Value",
                        "Stat2Value",
                        "Stat3Value",
                        "Stat4Value",
                        "Stat5Value",
                        "Stat6Value",
                        "Stat7Value",
                        "Stat8Value",
                        "Stat9Value",
                    ),
                ),
                VirtualField(
                    name="StatFloats",
                    fields=(
                        "Stat1Float",
                        "Stat2Float",
                        "Stat3Float",
                        "Stat4Float",
                        "Stat5Float",
                        "Stat6Float",
                        "Stat7Float",
                        "Stat8Float",
                    ),
                ),
                VirtualField(
                    name="Stats",
                    fields=("StatsKeys", "StatValues"),
                    zip=True,
                ),
                VirtualField(
                    name="Costs",
                    fields=("CostTypesKeys", "CostAmounts"),
                    zip=True,
                ),
            ],
            "HarvestCraftOptions": [
                VirtualField(
                    name="HarvestCraftTiersKey",
                    fields=("Tier",),
                    alias=True,
                ),
                VirtualField(
                    name="LifeforceCostType",
                    fields=("LifeforceType",),
                    alias=True,
                ),
                VirtualField(
                    name="SacredBlossomCost",
                    fields=("SacredCost",),
                    alias=True,
                ),
            ],
            "HeistAreas": [
                VirtualField(
                    name="ClientStringsKey",
                    fields=("Reward",),
                    alias=True,
                ),
            ],
            "IndexableSkillGems": [
                VirtualField(
                    name="Name",
                    fields=("Name1",),
                    alias=True,
                ),
            ],
            "MapPurchaseCosts": [
                VirtualField(
                    name="NormalPurchase",
                    fields=("NormalPurchase_BaseItemTypesKeys", "NormalPurchase_Costs"),
                    zip=True,
                ),
                VirtualField(
                    name="MagicPurchase",
                    fields=("MagicPurchase_BaseItemTypesKeys", "MagicPurchase_Costs"),
                    zip=True,
                ),
                VirtualField(
                    name="RarePurchase",
                    fields=("RarePurchase_BaseItemTypesKeys", "RarePurchase_Costs"),
                    zip=True,
                ),
                VirtualField(
                    name="UniquePurchase",
                    fields=("UniquePurchase_BaseItemTypesKeys", "UniquePurchase_Costs"),
                    zip=True,
                ),
            ],
            "MapSeriesTiers": [
                VirtualField(
                    name="AncestralTier",
                    fields=("AncestorTier",),
                    alias=True,
                ),
            ],
            "Mods": [
                VirtualField(
                    name="SpawnWeight",
                    fields=("SpawnWeight_TagsKeys", "SpawnWeight_Values"),
                    zip=True,
                ),
                VirtualField(
                    name="Stat1",
                    fields=("StatsKey1", "Stat1Min", "Stat1Max"),
                ),
                VirtualField(
                    name="Stat2",
                    fields=("StatsKey2", "Stat2Min", "Stat2Max"),
                ),
                VirtualField(
                    name="Stat3",
                    fields=("StatsKey3", "Stat3Min", "Stat3Max"),
                ),
                VirtualField(
                    name="Stat4",
                    fields=("StatsKey4", "Stat4Min", "Stat4Max"),
                ),
                VirtualField(
                    name="Stat5",
                    fields=("StatsKey5", "Stat5Min", "Stat5Max"),
                ),
                VirtualField(
                    name="Stat6",
                    fields=("StatsKey6", "Stat6Min", "Stat6Max"),
                ),
                VirtualField(
                    name="StatsKeys",
                    fields=(
                        "StatsKey1",
                        "StatsKey2",
                        "StatsKey3",
                        "StatsKey4",
                        "StatsKey5",
                        "StatsKey6",
                    ),
                ),
                VirtualField(
                    name="Stats",
                    fields=("Stat1", "Stat2", "Stat3", "Stat4", "Stat5", "Stat6"),
                ),
                VirtualField(
                    name="GenerationWeight",
                    fields=("GenerationWeight_TagsKeys", "GenerationWeight_Values"),
                    zip=True,
                ),
            ],
            "MonsterMapBossDifficulty": [
                VirtualField(
                    name="Stat1",
                    fields=("StatsKey1", "Stat1Value"),
                ),
                VirtualField(
                    name="Stat2",
                    fields=("StatsKey2", "Stat2Value"),
                ),
                VirtualField(
                    name="Stat3",
                    fields=("StatsKey3", "Stat3Value"),
                ),
                VirtualField(
                    name="Stat4",
                    fields=("StatsKey4", "Stat4Value"),
                ),
                VirtualField(
                    name="Stat5",
                    fields=("StatsKey5", "Stat5Value"),
                ),
                VirtualField(
                    name="Stats",
                    fields=("Stat1", "Stat2", "Stat3", "Stat4", "Stat5"),
                ),
            ],
            "MonsterMapDifficulty": [
                VirtualField(
                    name="Stat1",
                    fields=("StatsKey1", "Stat1Value"),
                ),
                VirtualField(
                    name="Stat2",
                    fields=("StatsKey2", "Stat2Value"),
                ),
                VirtualField(
                    name="Stat3",
                    fields=("StatsKey3", "Stat3Value"),
                ),
                VirtualField(
                    name="Stat4",
                    fields=("StatsKey4", "Stat4Value"),
                ),
                VirtualField(
                    name="Stats",
                    fields=("Stat1", "Stat2", "Stat3", "Stat4"),
                ),
            ],
            "PantheonSouls": [
                VirtualField(
                    name="BaseItemTypesKey",
                    fields=("CapturedVessel",),
                    alias=True,
                ),
                VirtualField(
                    name="MonsterVarietiesKey",
                    fields=("CapturedMonster",),
                    alias=True,
                ),
                VirtualField(
                    name="PantheonPanelLayoutKey",
                    fields=("PanelLayout",),
                    alias=True,
                ),
                VirtualField(
                    name="BossDescription",
                    fields=("CapturedMonsterDescription",),
                    alias=True,
                ),
            ],
            "PassiveSkills": [
                VirtualField(
                    name="StatValues",
                    fields=("Stat1Value", "Stat2Value", "Stat3Value", "Stat4Value", "Stat5Value"),
                ),
                VirtualField(
                    name="StatsZip",
                    fields=("Stats", "StatValues"),
                    zip=True,
                ),
                VirtualField(
                    name="ReminderTextKeys",
                    fields=("ReminderStrings",),
                    alias=True,
                ),
            ],
            "PassiveSkillMasteryEffects": [
                VirtualField(
                    name="StatValues",
                    fields=("Stat1Value", "Stat2Value", "Stat3Value"),
                ),
                VirtualField(
                    name="StatsZip",
                    fields=("Stats", "StatValues"),
                    zip=True,
                ),
            ],
            "PassiveSkillOverrides": [
                VirtualField(
                    name="PassiveSkillOverrideTypesKey",
                    fields=("Type",),
                    alias=True,
                ),
            ],
            "PassiveSkillTattoos": [
                VirtualField(
                    name="BaseItemTypesKey",
                    fields=("Tattoo",),
                    alias=True,
                ),
                VirtualField(
                    name="PassiveSkillOverrideTypesKey",
                    fields=("OverrideType",),
                    alias=True,
                ),
            ],
            "WorldAreas": [
                VirtualField(
                    name="AreaType_TagsKeys",
                    fields=("AreaTypeTags",),
                    alias=True,
                ),
                VirtualField(
                    name="VaalArea_WorldAreasKeys",
                    fields=("VaalArea",),
                    alias=True,
                ),
            ],
            "SkillGems": [
                VirtualField(
                    name="ExperienceProgression",
                    fields=("ItemExperienceType",),
                    alias=True,
                ),
            ],
        },
    )
}
