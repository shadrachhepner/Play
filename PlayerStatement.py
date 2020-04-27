import DialogueNode

class PlayerStatement:
    """
    PlayerStatement incorporates one dialogue option of the player
    """
    def __init__(self, text="", 
            next_node=DialogueNode.DialogueNode(),
            ends_convo = False):
        self.text = text
        self.next_node = next_node
        self.ends_convo = ends_convo

    def get_text(self):
        return self.text
    
    def go(self):
        print(self.get_text())
        if not self.ends_convo:
            self.next_node.have()

