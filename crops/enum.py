from enum import Enum

class MuitoAltaSusceptibilidade(Enum):
    MILHO = "Milho"
    FEIJAO = "Feijão"
    ARROZ = "Arroz"
    TRIGO = "Trigo"
    TOMATE = "Tomate"
    BATATA = "Batata"
    CACAU = "Cacau"
    PEPINO = "Pepino"
    MILHO_DOCE = "Milho-doce"
    MILHO_PIPOCA = "Milho pipoca"

class AltaSusceptibilidade(Enum):
    SOJA = "Soja"
    ALGODAO = "Algodão"
    CANA_DE_ACUCAR = "Cana-de-açúcar"
    CAFE = "Café"
    LARANJA = "Laranja"
    PIMENTAO = "Pimentão"
    BERINJELA = "Berinjela"
    ALFACE = "Alface"
    ESPINAFRE = "Espinafre"
    ABOBRINHA = "Abobrinha"

class MediaSusceptibilidade(Enum):
    CEVADA = "Cevada"
    AMENDOIM = "Amendoim"
    UVA = "Uva"
    ERVILHA = "Ervilha"
    BROCOLIS = "Brócolis"
    CEBOLA = "Cebola"
    COUVE = "Couve"
    CEBOLA_ROXA = "Cebola roxa"
    ERVA_DOCE = "Erva-doce"

class BaixaSusceptibilidade(Enum):
    SORGO = "Sorgo"
    MILHETO = "Milheto"
    GIRASSOL = "Girassol"
    CENTEIO = "Centeio"
    BATATA_DOCE = "Batata doce"
    CENOURA = "Cenoura"
    RABANETE = "Rabanete"

class MuitoBaixaSusceptibilidade(Enum):
    MANDIOCA = "Mandioca"
    CACTACEAS = "Cactáceas"


class PlantingPeriod(Enum):
    BEFORE = "Before planting period"
    DURING = "During planting period"
    AFTER = "After planting period"
