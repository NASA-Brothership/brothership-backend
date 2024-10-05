from enum import Enum

class VeryHighSusceptibility(Enum):
    CORN = "Corn"
    BEAN = "Bean"
    RICE = "Rice"
    WHEAT = "Wheat"
    TOMATO = "Tomato"
    POTATO = "Potato"
    COCOA = "Cocoa"
    CUCUMBER = "Cucumber"
    SWEET_CORN = "Sweet corn"
    POPCORN = "Popcorn"

class HighSusceptibility(Enum):
    SOYBEAN = "Soybean"
    COTTON = "Cotton"
    SUGAR_CANE = "Sugar cane"
    COFFEE = "Coffee"
    ORANGE = "Orange"
    BELL_PEPPER = "Bell pepper"
    EGGPLANT = "Eggplant"
    LETTUCE = "Lettuce"
    SPINACH = "Spinach"
    ZUCCHINI = "Zucchini"

class MediumSusceptibility(Enum):
    BARLEY = "Barley"
    PEANUT = "Peanut"
    GRAPE = "Grape"
    PEA = "Pea"
    BROCCOLI = "Broccoli"
    ONION = "Onion"
    KALE = "Kale"
    RED_ONION = "Red onion"
    FENNEL = "Fennel"

class LowSusceptibility(Enum):
    SORGHUM = "Sorghum"
    MILLET = "Millet"
    SUNFLOWER = "Sunflower"
    RYE = "Rye"
    SWEET_POTATO = "Sweet potato"
    CARROT = "Carrot"
    RADISH = "Radish"

class VeryLowSusceptibility(Enum):
    CASSAVA = "Cassava"
    CACTACEAE = "Cactaceae"

class PlantingPeriod(Enum):
    BEFORE = "Before planting period"
    DURING = "During planting period"
    AFTER = "After planting period"