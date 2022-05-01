"""Main module."""


class FSNode:

    def __init__(self, name: str) -> None:
        self.name = name
        self.children = set()

    def get_name(self) -> str:
        self.name
