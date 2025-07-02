# from text_processing.summarizer.pegasus_summarizer import PegasusSummarizer
# from text_processing.summarizer.bart_summarizer import BartSummarizer
# from text_processing.summarizer.falcon_summarizer import FalconSummarizer
from text_processing.summarizer.summarizer_type import SummarizerType
# from text_processing.summarizer.t5_summarizer import T5Summarizer
from text_processing.summarizer.summarizer import SummarizerBase

# English models
from text_processing.summarizer.english_models.bart_samsum_summarizer import BartSamsumDialogue
from text_processing.summarizer.english_models.bart_summarizer import BartLargeCNN
from text_processing.summarizer.english_models.pegasus_cnn_summarizer import PegasusCNN
from text_processing.summarizer.english_models.pegasus_xsum_summarizer import PegasusXSUM
from text_processing.summarizer.english_models.t5_base_summarizer import T5BaseEnglish


# Multilingual models
from text_processing.summarizer.multilingual_models.mt5base_summarizer import MT5BaseSummarizer
from text_processing.summarizer.multilingual_models.mt5xlsum_summarizer import XLSumSummarizer
from text_processing.summarizer.multilingual_models.t5base_cnn_summarizer import PierreguillouSummarizer


class SumarizerFactory:
    @staticmethod
    def create_sumarizer(summarizer_type: SummarizerType) -> SummarizerBase:
        match summarizer_type:
            case "philschmid/bart-large-cnn-samsum":
                return BartSamsumDialogue()
            case "facebook/bart-large-cnn":
                return BartLargeCNN()
            case "google/pegasus-cnn_dailymail":
                return PegasusCNN()
            case "google/pegasus-xsum":
                return PegasusXSUM()
            case "t5-base":
                return T5BaseEnglish()
            case "google/mt5-base":
                return MT5BaseSummarizer()
            case "csebuetnlp/mT5_multilingual_XLSum":
                return XLSumSummarizer()
            case "pierreguillou/t5-base-pt-summarizer-cnn-multilingual":
                return PierreguillouSummarizer()
            case _:
                raise ValueError(f"Unsupported summarizer type: {summarizer_type}")

# def get_summarizer(summarizer_type: SummarizerType, word_count: int):
#     print("[get_summarizer] - word_count = ", word_count)
#
#     # BART_SAMSUM =
#     # BART_CNN = ""
#     # PEGASUS_CNN = ""
#     # PEGASUS_XSUM = ""
#     # T5_BASE = ""
#     #
#     # MT5_BASE = ""
#     # MT5_XLSUM = ""
#     # T5_PT_CNN = ""
#
#     match summarizer_type:
#         case "philschmid/bart-large-cnn-samsum":
#             return BartSamsumDialogue()
#
#         case "facebook/bart-large-cnn":
#             return BartLargeCNN()
#
#         case "google/pegasus-cnn_dailymail":
#             return PegasusCNN()
#
#         case "google/pegasus-xsum":
#             return PegasusXSUM()
#
#         case "t5-base":
#             return T5BaseEnglish()
#         case "google/mt5-base":
#             return MT5BaseSummarizer()
#         case "csebuetnlp/mT5_multilingual_XLSum":
#             return XLSumSummarizer()
#         case "pierreguillou/t5-base-pt-summarizer-cnn-multilingual":
#             return PierreguillouSummarizer()
#         case _:
#             raise ValueError(f"Unsupported summarizer type: {summarizer_type}")
#
#
#
#
#
#     if summarizer_type == SummarizerType.PEGASUS:
#         return PegasusSummarizer()
#     elif summarizer_type == SummarizerType.BART:
#         return BartSummarizer()
#     elif summarizer_type == SummarizerType.FALCON:
#         return FalconSummarizer()
#     elif summarizer_type == SummarizerType.AUTO:
#         # Example logic – adjust as needed
#         if word_count < 150:
#             return BartSummarizer()
#         elif word_count < 500:
#             return PegasusSummarizer()
#         else:
#             #return FalconSummarizer()
#             return T5Summarizer()
#     else:
#         raise ValueError(f"Unsupported summarizer type: {summarizer_type}")

