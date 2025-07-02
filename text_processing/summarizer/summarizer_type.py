from enum import Enum

class SummarizerType(str, Enum):

    BART_SAMSUM = "philschmid/bart-large-cnn-samsum"
    BART_CNN = "facebook/bart-large-cnn"
    PEGASUS_CNN = "google/pegasus-cnn_dailymail"
    PEGASUS_XSUM = "google/pegasus-xsum"
    T5_BASE = "t5-base"

    MT5_BASE = "google/mt5-base"
    MT5_XLSUM = "csebuetnlp/mT5_multilingual_XLSum"
    T5_PT_CNN = "pierreguillou/t5-base-pt-summarizer-cnn-multilingual"
