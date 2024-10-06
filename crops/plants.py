from code_enums import VeryLowDroughtRisk, LowDroughtRisk, MediumDroughtRisk, HighDroughtRisk, VeryHighDroughtRisk

very_low_drought_risk = {
    VeryLowDroughtRisk.CACTUS,
    VeryLowDroughtRisk.CASSAVA,
    VeryLowDroughtRisk.SWEET_POTATO,
    VeryLowDroughtRisk.WATERCRESS,
    VeryLowDroughtRisk.CABBAGE,
    VeryLowDroughtRisk.LETTUCE
}

low_drought_risk = {
    LowDroughtRisk.MILLET,
    LowDroughtRisk.SORGHUM,
    LowDroughtRisk.PEANUT,
    LowDroughtRisk.CHICKPEA,
    LowDroughtRisk.PIGEON_PEA,
    LowDroughtRisk.QUINOA,
    LowDroughtRisk.TEFF,
    LowDroughtRisk.FENNEL,
    LowDroughtRisk.KALE
}

medium_drought_risk = {
    MediumDroughtRisk.TOMATO,
    MediumDroughtRisk.CORN,
    MediumDroughtRisk.CUCUMBER,
    MediumDroughtRisk.SPINACH,
    MediumDroughtRisk.ZUCCHINI,
    MediumDroughtRisk.PUMPKIN,
    MediumDroughtRisk.BARLEY,
    MediumDroughtRisk.OATS,
    MediumDroughtRisk.LENTILS,
    MediumDroughtRisk.EGGPLANT
}

high_drought_risk = {
    HighDroughtRisk.WHEAT,
    HighDroughtRisk.RICE,
    HighDroughtRisk.POTATO,
    HighDroughtRisk.SUGARCANE,
    HighDroughtRisk.BROCCOLI,
    HighDroughtRisk.ONION,
    HighDroughtRisk.RED_ONION,
    HighDroughtRisk.BELL_PEPPER,
    HighDroughtRisk.CARROT,
    HighDroughtRisk.RADISH
}

very_high_drought_risk = {
    VeryHighDroughtRisk.BANANA,
    VeryHighDroughtRisk.PAPAYA,
    VeryHighDroughtRisk.COCOA,
    VeryHighDroughtRisk.GRAPE,
    VeryHighDroughtRisk.ORANGE,
    VeryHighDroughtRisk.COTTON,
    VeryHighDroughtRisk.SWEET_CORN,
    VeryHighDroughtRisk.POPCORN,
    VeryHighDroughtRisk.SOYBEAN
}

all_plants = very_low_drought_risk | \
             low_drought_risk | \
             medium_drought_risk | \
             high_drought_risk | \
             very_high_drought_risk
