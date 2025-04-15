# TranslatorFactory
from text_processing.translator.fairseq_translator import FairseqTranslator
from text_processing.translator.google_translator import GoogleTranslator
from text_processing.translator.marian_mt_translator import MarianMTTranslator
from text_processing.translator.mt_translate import MTranslator
from text_processing.translator.translator import BaseTranslator
from text_processing.translator.translator_type import TranslatorType


class TranslatorFactory:
    @staticmethod
    def create_translator(typeTranslator: TranslatorType) -> BaseTranslator:
        if typeTranslator == TranslatorType.MARIANMT:
            return MarianMTTranslator()
        elif typeTranslator == TranslatorType.GOOGLETRANS:
            return GoogleTranslator()
        elif typeTranslator == TranslatorType.MTRANSLATE:
            return MTranslator()
        elif typeTranslator == TranslatorType.FAIRSEQ:
            return FairseqTranslator()
        else:
            raise ValueError("Invalid Translator Type")