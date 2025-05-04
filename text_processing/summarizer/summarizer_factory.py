from text_processing.summarizer.pegasus_summarizer import PegasusSummarizer
from text_processing.summarizer.bart_summarizer import BartSummarizer
from text_processing.summarizer.falcon_summarizer import FalconSummarizer
from text_processing.summarizer.summarizer_type import SummarizerType
from text_processing.summarizer.t5_summarizer import T5Summarizer


def get_summarizer(summarizer_type: SummarizerType, word_count: int):
    print("[get_summarizer] - word_count = ", word_count)

    if summarizer_type == SummarizerType.PEGASUS:
        return PegasusSummarizer()
    elif summarizer_type == SummarizerType.BART:
        return BartSummarizer()
    elif summarizer_type == SummarizerType.FALCON:
        return FalconSummarizer()
    elif summarizer_type == SummarizerType.AUTO:
        # Example logic – adjust as needed
        if word_count < 150:
            return BartSummarizer()
        elif word_count < 500:
            return PegasusSummarizer()
        else:
            #return FalconSummarizer()
            return T5Summarizer()
    else:
        raise ValueError(f"Unsupported summarizer type: {summarizer_type}")

