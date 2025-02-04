from typing import List, Tuple


class Path:
    def __init__(self) -> None:
        self.steps = []

    def append_step(self, step: Tuple[int, int]) -> None:
        self.steps.append(step)

    def inverse_path(self) -> List[Tuple[int, int]]:
        return self.steps[::-1]
