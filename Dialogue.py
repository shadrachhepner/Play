from PlayerStatement import PlayerStatement
from DialogueNode import DialogueNode


class Dialogue:
    """ 
    Dialogue is an entire interaction between a player and NPC 
    This is an extra comment that I am adding to play with git
    """
    def __init__(self, first_node : DialogueNode = DialogueNode()): 
        self.first_node = first_node 

    def have_conversation(self):
        self.first_node.have()
