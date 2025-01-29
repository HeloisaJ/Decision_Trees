from tree_structure.component_tree import Component_tree
from exception.exception import Decision_tree_exception

class Leaf(Component_tree):

    def __init__(self):
        pass

    def predict(self):
        # Define a form of better represent the result
        pass

    def add_feature_branch(self, c_tree: Component_tree):
        raise Decision_tree_exception("Invalid Operation, can not add a branch to a leaf")

    def remove_feature_branch(self, c_tree: Component_tree):
        raise Decision_tree_exception("Invalid Operation, it does not exist a branch in a leaf")

    def get_feature_branches(self):
        return dict()