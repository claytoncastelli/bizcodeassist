# Enum TranslatorType
from enum import Enum

class TranslatorType(Enum):
    MARIANMT = "marianmt"
    GOOGLETRANS = "googletrans"
    MTRANSLATE = "mtranslate"
    FAIRSEQ = "fairseq"