from PlayerStatement import PlayerStatement
from DialogueNode import DialogueNode


class Dialogue:
    """ Dialogue is an entire interaction between a player and NPC """
    def __init__(self, first_node : DialogueNode = DialogueNode()): 
        self.first_node = first_node 

    def have_conversation(self):
        self.first_node.have()
