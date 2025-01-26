from abc import ABC, abstractmethod

class Component_tree(ABC):

    @abstractmethod
    def calculate_result(self) -> None: pass

    @abstractmethod
    def add_feature_branch(self, c_tree: Component_tree) -> None: pass

    @abstractmethod
    def remove_feature_branch(self, c_tree: Component_tree) -> None: pass

    @abstractmethod
    def get_feature_branches(self) -> None: pass