from enum import Enum

# Define Enums for drought risk categories
class DroughtRisk(Enum):
    VERY_LOW = 'Very Low'
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    VERY_HIGH = 'Very High'

class DroughtRiskValues(Enum):
    VERY_LOW = 0
    LOW = 0.25
    MEDIUM = 0.5
    HIGH = 0.75
    VERY_HIGH = 1


class VeryLowDroughtRisk(Enum):
    CACTUS = 'Cactus'
    CASSAVA = 'Cassava'
    SWEET_POTATO = 'Sweet Potato'
    WATERCRESS = 'Watercress'
    CABBAGE = 'Cabbage'
    LETTUCE = 'Lettuce'


class LowDroughtRisk(Enum):
    MILLET = 'Millet'
    SORGHUM = 'Sorghum'
    PEANUT = 'Peanut'
    CHICKPEA = 'Chickpea'
    PIGEON_PEA = 'Pigeon Pea'
    QUINOA = 'Quinoa'
    TEFF = 'Teff'
    FENNEL = 'Fennel'
    KALE = 'Kale'


class MediumDroughtRisk(Enum):
    TOMATO = 'Tomato'
    CORN = 'Corn'
    CUCUMBER = 'Cucumber'
    SPINACH = 'Spinach'
    ZUCCHINI = 'Zucchini'
    PUMPKIN = 'Pumpkin'
    BARLEY = 'Barley'
    OATS = 'Oats'
    LENTILS = 'Lentils'
    EGGPLANT = 'Eggplant'


class HighDroughtRisk(Enum):
    WHEAT = 'Wheat'
    RICE = 'Rice'
    POTATO = 'Potato'
    SUGARCANE = 'Sugarcane'
    BROCCOLI = 'Broccoli'
    ONION = 'Onion'
    RED_ONION = 'Red Onion'
    BELL_PEPPER = 'Bell Pepper'
    CARROT = 'Carrot'
    RADISH = 'Radish'


class VeryHighDroughtRisk(Enum):
    BANANA = 'Banana'
    PAPAYA = 'Papaya'
    COCOA = 'Cocoa'
    GRAPE = 'Grape'
    ORANGE = 'Orange'
    COTTON = 'Cotton'
    SWEET_CORN = 'Sweet Corn'
    POPCORN = 'Popcorn'
    SOYBEAN = 'Soybean'


class PlantingPeriod(Enum):
    BEFORE = "BEFORE"
    DURING = "DURING"
    AFTER = "AFTER"

class Recomendation(Enum):
    VERY_LOW_RISK_WITH_CULTURE = 'VERY_LOW_RISK_WITH_CULTURE'
    LOW_RISK_WITH_CULTURE = 'LOW_RISK_WITH_CULTURE'
    MEDIUM_RISK_WITH_CULTURE_WITH_IRRIGATION = 'MEDIUM_RISK_WITH_CULTURE_WITH_IRRIGATION'
    MEDIUM_RISK_WITH_CULTURE_WITHOUT_IRRIGATION = 'MEDIUM_RISK_WITH_CULTURE_WITHOUT_IRRIGATION'
    HIGH_RISK_WITH_CULTURE_WITH_IRRIGATION = 'HIGH_RISK_WITH_CULTURE_WITH_IRRIGATION'
    HIGH_RISK_WITH_CULTURE_WITHOUT_IRRIGATION = 'HIGH_RISK_WITH_CULTURE_WITHOUT_IRRIGATION'
    VERY_HIGH_RISK_WITH_CULTURE_WITH_IRRIGATION = 'VERY_HIGH_RISK_WITH_CULTURE_WITH_IRRIGATION'
    VERY_HIGH_RISK_WITH_CULTURE_WITHOUT_IRRIGATION = 'VERY_HIGH_RISK_WITH_CULTURE_WITHOUT_IRRIGATION'

    LOW_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD = 'LOW_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD'
    MEDIUM_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD = 'MEDIUM_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD'
    HIGH_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD = 'HIGH_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD'
    
    LOW_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_DURING_PLANTING_PERIOD = 'LOW_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_DURING_PLANTING_PERIOD'
    HIGH_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_DURING_PLANTING_PERIOD = 'HIGH_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_DURING_PLANTING_PERIOD'

    LOW_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD = 'LOW_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD'
    MEDIUM_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD = 'MEDIUM_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD'
    HIGH_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD = 'HIGH_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD'
    LOW_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_DURING_PLANTING_PERIOD = 'LOW_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_DURING_PLANTING_PERIOD'
    HIGH_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_DURING_PLANTING_PERIOD = 'HIGH_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_DURING_PLANTING_PERIOD'
    