class Decision_tree_exception(Exception):

    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return f"Exception: {self.message}"