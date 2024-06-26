import itertools
from pathlib import Path

import numpy
from typing import List, Generator, Iterable
from typing import Tuple

Events = List[Tuple[str, float, float]]

OUTFILE = Path("./events.csv")


def gen_run_length(data: Iterable[float|int]) -> Generator[int, None, None]:
    """returns the current count of identical values"""
    previous = None
    count: int = 0

    for value in data:
        if previous == value:
            count += 1
        else:
            count = 0
        previous = value
        yield count


def gen_rising_edge(data: Iterable[float|int], threshold: float) -> Generator[bool, None, None]:
    """returns an event when the new value transitions from being less than (or equal), to greater than
    the configured threshold
    """
    previous = None

    for value in data:
        outcome = False
        if previous is not None:
            if (value > threshold) and (previous <= threshold):
                outcome = True
        previous = value
        yield outcome


def output_event(name: str, timestamp: float, event: bool) -> None:
    if not event:
        return
    with OUTFILE.open("a") as fh:
        fh.write(f"{timestamp},{name}\n")


def run():
    data = [0] * 1000 + [1] * 1000 + [0] * 1000

    # working with generators allows us to compose processing pipelines in a functional style

    # we split our source data before handing it to individual processing pipelines
    # so that they can increment at their own pace
    # the pipelines themselves could be multiprocessed, in the case that the processing is more costly
    # than the data transfer
    raw_data, input_gt, input_gen_rising_edge = itertools.tee(data, 3)

    # since we can't reuse generators, we'd have to do something a bit fancier if we wanted
    # to store intermediate results, such as "analyse_runlength"
    analyse_rising_edge = gen_rising_edge(input_gt, threshold=0.7)
    analyse_runlength = gen_run_length(input_gen_rising_edge)
    analyse_rising_edge_of_runlength = gen_rising_edge(analyse_runlength, 9)

    counter = 0
    for value in raw_data:
        counter += 1

        event = next(analyse_rising_edge_of_runlength)
        output_event("ten_identical_values", counter, event)

        event = next(analyse_rising_edge)
        output_event("more_than_0.7", counter, event)


__name__ == "__main__" and run()
