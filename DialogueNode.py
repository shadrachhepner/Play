import PlayerStatement 


def get_user_selection(options):
    selection = 0
    while((selection<=0) or (selection > len(options))):
        is_err = False
        try:
            selection = int(input("Select an option: "))
        except ValueError:
            is_err = True
        if selection <= 0 or selection > len(options):
            is_err = True
        if is_err:
            print("Please select a number between 1 and " + str(len(options)))
            selection = 0
    return selection


class DialogueNode: 
    def __init__(self, prompt_text="Hi there.",
            player_statement_array = [],
            next_dlg_array = []):
        self.prompt_text = prompt_text
        self.player_statement_array = player_statement_array
        self.next_dlg_array = next_dlg_array
    
     
    def have(self):
        print(self.prompt_text)
        for i in self.player_statement_array:
            print(str(self.player_statement_array.index(i)+1)+") "
                    + i.get_text())
        selection = get_user_selection(self.player_statement_array)
        self.player_statement_array[selection-1].go()
    
    def set_link_array(self, player_statement_array):
        self.player_statement_array = player_statement_array

    def set_prompt_text(self, text):
        self.prompt_text = text
        
