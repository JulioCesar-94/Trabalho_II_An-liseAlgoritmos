"""Implemente as três filas de prioridade sem usar heapq."""

from __future__ import annotations


class BinaryHeap:
    def __init__(self):
        raise NotImplementedError

    def push(self, vertex: int, priority: float):
        raise NotImplementedError

    def decrease_key(self, handle, new_priority: float) -> None:
        raise NotImplementedError

    def pop_min(self) -> tuple[int, float]:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


class BinomialHeap:
    def __init__(self):
        raise NotImplementedError

    def push(self, vertex: int, priority: float):
        raise NotImplementedError

    def decrease_key(self, handle, new_priority: float) -> None:
        raise NotImplementedError

    def pop_min(self) -> tuple[int, float]:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


class FibonacciHeap:
    def __init__(self):
        raise NotImplementedError

    def push(self, vertex: int, priority: float):
        raise NotImplementedError

    def decrease_key(self, handle, new_priority: float) -> None:
        raise NotImplementedError

    def pop_min(self) -> tuple[int, float]:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

