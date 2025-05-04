from enum import Enum

class SummarizerType(str, Enum):
    PEGASUS = "pegasus"
    BART = "bart"
    FALCON = "falcon"
    AUTO = "auto"
