from abc import ABC, abstractmethod


# BaseClass
class SummarizerBase(ABC):

    # @abstractmethod
    # def __init__(self, max_length:int=50, min_length:int=10, do_sample:bool=False):
    #     self.max_length = max_length
    #     self.min_length = min_length
    #     self.do_sample = do_sample


    @abstractmethod
    def summarize(self, text: str) -> str:
        pass
