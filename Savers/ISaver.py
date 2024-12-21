from abc import abstractmethod
from abc import ABC

class ISaver(ABC):
    @abstractmethod
    def create_screenshot(self) -> None:
        return