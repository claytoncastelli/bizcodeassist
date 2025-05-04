from text_processing.summarizer.summarizer_factory import get_summarizer
from text_processing.summarizer.summarizer_type import SummarizerType

def smart_summarize(text: str):
    word_count = len(text.split())
    if word_count < 50:
        return text

    if word_count <= 400:
        summarizer_type = SummarizerType.PEGASUS
    elif word_count <= 1024:
        summarizer_type = SummarizerType.BART
    else:
        summarizer_type = SummarizerType.FALCON

    summarizer = get_summarizer(summarizer_type)
    return summarizer.summarize(text)
