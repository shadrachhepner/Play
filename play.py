import Dialogue as D
import PlayerStatement as PS
import DialogueNode as DN

END_NODE_ARRAY = [PS.PlayerStatement(text="[End conversation]", ends_convo=True)]

node_1 = DN.DialogueNode()
node_2 = DN.DialogueNode()

node_array = []
node_array.append(PS.PlayerStatement(text="Well hey!", next_node=node_2, ends_convo=False))
node_array.append(PS.PlayerStatement(text="Go fuck yourself", ends_convo=True))

node_1.set_prompt_text("Hello stranger.")
node_1.set_link_array(node_array)

node_2.set_prompt_text("It's quite nice to meet you.")
node_2.set_link_array(END_NODE_ARRAY)

my_convo = D.Dialogue(first_node = node_1)
my_convo.have_conversation()
