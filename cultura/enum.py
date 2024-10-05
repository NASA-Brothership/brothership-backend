from enum import Enum

class AltaSusceptibilidade(Enum):
    MILHO = "Milho"
    FEIJAO = "Feijão"
    ARROZ = "Arroz"
    TRIGO = "Trigo"
    TOMATE = "Tomate"
    BATATA = "Batata"
    CACAU = "Cacau"
    LARANJA = "Laranja"

class MediaSusceptibilidade(Enum):
    SOJA = "Soja"
    ALGODAO = "Algodão"
    CANA_DE_ACUCAR = "Cana-de-açúcar"
    CAFE = "Café"
    CEVADA = "Cevada"
    AMENDOIM = "Amendoim"
    UVA = "Uva"

class BaixaSusceptibilidade(Enum):
    SORGO = "Sorgo"
    MILHETO = "Milheto"
    GIRASSOL = "Girassol"
    CENTEIO = "Centeio"
    MANDIOCA = "Mandioca"
    BATATA_DOCE = "Batata doce"
