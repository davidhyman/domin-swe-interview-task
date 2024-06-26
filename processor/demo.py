import numpy
from typing import List
from typing import Tuple

Events = List[Tuple[str, float, float]]


class Analyser:
    def analyse(self, arr: numpy.ndarray) -> Events:
        pass


class WindowRepeatAnalyser:
    """example of operation over window. some algorithms don't require a full window
    such as this specific run-length counter, or averaging; a different group of Analysers could be implemented
    in such cases for greater performance (as they wouldn't repeatedly loop already-processed data)
    """
    def __init__(self, event_when_sequential: int):
        self.event_when_sequential = event_when_sequential

    def analyse(self, arr: numpy.ndarray) -> Events:
        avg_value = numpy.average(arr)



def run():
    data = [0] * 1000 + [1] * 1000 + [0] * 1000

    max_window_ms = 500
    processor_length = max_window_ms * 2
    channel_processor = numpy.ndarray((1, processor_length))
    current_insertion_index = 0

    analysers = {
        "detector_1": WindowAvgAnalyser(event_when_greater_than=0.5),
    }



__name__ == "__main__" and run()
