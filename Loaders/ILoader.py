from abc import abstractmethod
from abc import ABC

class ILoader(ABC):
    @abstractmethod
    def to_string(self) -> str:
        return ""