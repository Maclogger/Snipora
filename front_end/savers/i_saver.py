from abc import abstractmethod
from abc import ABC

class ISaver(ABC):
    @abstractmethod
    def save(self, screenshot_path: str) -> bool:
        return False