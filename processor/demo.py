import numpy
from typing import List
from typing import Tuple

Events = List[Tuple[str, float, float]]


class StreamAnalyser:
    """potentially stateful analysers that run from the start to the end of the stream"""
    def analyse(self, timestamp: float, current_value: float) -> bool|float|int:
        pass


class StreamMetric(StreamAnalyser):
    def analyse(self, timestamp: float, current_value: float) -> float|int:
        pass


class StreamEvent(StreamAnalyser):
    def analyse(self, timestamp: float, current_value: float) -> bool:
        pass


class Average(StreamMetric):
    """example of operation over window.
    different algorithms might want to retain the same data over a window; this could be inefficient
    in terms of maintaining multiple buffers.
    """
    def __init__(self, window_length: int=10):
        pass

    def analyse(self, timestamp: float, current_value: float) -> float:
        raise NotImplementedError()


class RunLength(StreamMetric):
    """returns the current count of identical values
    """
    def __init__(self):
        self.previous = None
        self.count = 0

    def analyse(self, timestamp: float, current_value: float) -> int:
        if self.previous == current_value:
            self.count += 1
        else:
            self.count = 0
        self.previous = current_value
        return self.count


class GreaterThanEdge(StreamEvent):
    """returns an event when the new value transitions from being less than (or equal), to greater than
    the configured value
    """
    def __init__(self, value: float=0.5):
        self.previous = None
        self.value: float = value

    def analyse(self, timestamp: float, current_value: float) -> bool:
        outcome = False
        if self.previous is not None:
            if (current_value > self.value) and (self.previous <= self.value):
                outcome = True
        self.previous = current_value
        return outcome


def run():
    data = [0] * 1000 + [1] * 1000 + [0] * 1000

    max_window_ms = 500
    processor_length = max_window_ms * 2
    channel_processor = numpy.ndarray((1, processor_length))
    current_insertion_index = 0

    gt = GreaterThanEdge(value=0.7)
    raw_rle = RunLength()


__name__ == "__main__" and run()
