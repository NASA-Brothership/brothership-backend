import crops.plants as plants
from crops.code_enums import (
    DroughtRisk, DroughtRiskValues, Recomendation, PlantingPeriod
)

# Function to get drought risk category for a crop
def get_drought_risk(crop: str) -> DroughtRiskValues:
    # Check for crop in each drought risk category
    print(crop)
    if crop in plants.very_low_drought_risk:
        return DroughtRiskValues.VERY_LOW
    elif crop in plants.low_drought_risk:
        return DroughtRiskValues.LOW
    elif crop in plants.medium_drought_risk:
        return DroughtRiskValues.MEDIUM
    elif crop in plants.high_drought_risk:
        return DroughtRiskValues.HIGH
    elif crop in plants.very_high_drought_risk:
        return DroughtRiskValues.VERY_HIGH

def get_mean_risk(sc, su, sb, spt):
    return 0.3*sc + 0.5*su + 0.25*sb + 0.20*spt

def get_recomendation(mean_risk, is_irrigated, planting_period, existing_crops):
    if existing_crops == "yes":
        if mean_risk <= 0.2:
            return Recomendation.VERY_LOW_RISK_WITH_CULTURE.value
        elif mean_risk > 0.2 and mean_risk <= 0.4:
            return Recomendation.LOW_RISK_WITH_CULTURE.value
        elif mean_risk > 0.4 and mean_risk <= 0.6:
            if is_irrigated == "yes":
                return Recomendation.MEDIUM_RISK_WITH_CULTURE_WITH_IRRIGATION.value
            else:
                return Recomendation.MEDIUM_RISK_WITH_CULTURE_WITH_IRRIGATION.value
        elif mean_risk > 0.6 and mean_risk <= 0.8:
            if is_irrigated == "yes":
                return Recomendation.HIGH_RISK_WITH_CULTURE_WITH_IRRIGATION.value
            else:
                return Recomendation.HIGH_RISK_WITH_CULTURE_WITHOUT_IRRIGATION.value
        elif mean_risk > 0.8:
            if is_irrigated == "yes":
                return Recomendation.VERY_HIGH_RISK_WITH_CULTURE_WITH_IRRIGATION.value
            else:
                return Recomendation.VERY_HIGH_RISK_WITH_CULTURE_WITHOUT_IRRIGATION.value
    else:
        if is_irrigated == "yes" and planting_period in (PlantingPeriod.BEFORE.value, PlantingPeriod.AFTER.value):
            if mean_risk <= 0.4:
                return Recomendation.LOW_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD.value
            if mean_risk > 0.4 and mean_risk <= 0.6:
                return Recomendation.MEDIUM_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD.value
            if mean_risk > 0.6:
                return Recomendation.HIGH_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD.value
        elif is_irrigated == "yes" and planting_period  == PlantingPeriod.DURING.value:
            if mean_risk <= 0.6:
                return Recomendation.LOW_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_DURING_PLANTING_PERIOD.value
            if mean_risk > 0.6:
                return Recomendation.HIGH_RISK_WITHOUT_CULTURE_WITH_IRRIGATION_DURING_PLANTING_PERIOD.value
        if is_irrigated == "no" and planting_period in (PlantingPeriod.BEFORE.value, PlantingPeriod.AFTER.value):
            if mean_risk <= 0.4:
                return Recomendation.LOW_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD.value
            if mean_risk > 0.4 and mean_risk <= 0.6:
                return Recomendation.MEDIUM_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD.value
            if mean_risk > 0.6:
                return Recomendation.HIGH_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD.value
        elif is_irrigated == "no" and planting_period  == PlantingPeriod.DURING.value:
            if mean_risk <= 0.4:
                return Recomendation.LOW_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_DURING_PLANTING_PERIOD.value
            if mean_risk > 0.4:
                return Recomendation.HIGH_RISK_WITHOUT_CULTURE_WITHOUT_IRRIGATION_DURING_PLANTING_PERIOD.value