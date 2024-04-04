class Tape(object):
    
    blank_symbol = " "
    
    def __init__(self,
                 tape_string = ""):
        self.__tape = dict((enumerate(tape_string)))
        
    def __str__(self):
        s = ""
        min_used_index = min(self.__tape.keys()) 
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.__tape[i]
        return s    
   
    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char 

        
class TuringMachine(object):
    
    def __init__(self, 
                 tape = "", 
                 initial_state = "",
                 final_states = None,
                 transition_function = None,
                 head_position = 0):
        self.__tape = Tape(tape)
        self.__head_position = head_position
        self.__current_state = initial_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)
        
    def get_tape(self): 
        return str(self.__tape)
    
    def step(self):
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == "R":
                self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            self.__current_state = y[0]
        #print(self.get_tape(), self.__head_position, self.__current_state)

    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False
        
accepting_states = ["final"]
transition_function = {("init", "."): ("init", ".", "R"),
                       ("init", "+"): ("skip", "+", "R"),
                       ("skip", "."): ("add_one", "+", "L"),
                       ("add_one", "+"): ("init", ".", "R"),
                       ("skip", " "): ("del_last", " ", "L"),
                       ("del_last", "+"): ("final", "", "N"),
                       }
final_states = {"final"}

t = TuringMachine("...+... ", 
                  initial_state = "init",
                  final_states = final_states,
                  transition_function=transition_function)

print("Input on Tape:\n" + t.get_tape())

while not t.final():
    t.step()

print("Result of the Turing machine calculation:")    
print(t.get_tape())

accepting_states = ["final"]
transition_function = {("0", "0"): ("0", "0", "R"),
                       ("0", "1"): ("0", "1", "R"),
                       ("0", " "): ("1", " ", "R"),
                       
                       ("1", "0"): ("1", "0", "R"),
                       ("1", "1"): ("1", "1", "R"),
                       ("1", " "): ("2", " ", "L"),
                       
                       ("2", "0"): ("2", "1", "L"),
                       ("2", "1"): ("3", "0", "L"),
                       ("2", " "): ("5", " ", "R"),
                       
                       ("3", "0"): ("3", "0", "L"),
                       ("3", "1"): ("3", "1", "L"),
                       ("3", " "): ("4", " ", "L"),
                       
                       ("4", "0"): ("0", "1", "R"),
                       ("4", "1"): ("4", "0", "L"),
                       ("4", " "): ("0", "1", "R"),
                       
                       ("5", "1"): ("5", "", "R"),
                       ("5", " "): ("final", " ", "N"),
                       }
final_states = {"final"}

t = TuringMachine("   10 11    ", 
                  initial_state = "0",
                  final_states = final_states,
                  transition_function=transition_function,
                  head_position=3)

print("Input on Tape:\n" + t.get_tape())

while not t.final():
    t.step()

print("Result of the Turing machine calculation:")    
print(t.get_tape())

accepting_states = ["final"]
transition_function = {("0", " "): ("0", " ", "R"),
                       ("0", "."): ("1", " ", "R"),
                       ("1", " "): ("2", " ", "R"),
                       ("1", "."): ("1", ".", "R"),
                       ("2", " "): ("3", " ", "L"),
                       ("2", "."): ("2", ".", "R"),
                       ("3", " "): ("final", ".", "N"),
                       ("3", "."): ("4", " ", "L"),
                       ("4", " "): ("final", " ", "N"),
                       ("4", "."): ("5", ".", "L"),
                       ("5", " "): ("6", " ", "L"),
                       ("5", "."): ("5", ".", "L"),
                       ("6", " "): ("final", ".", "N"),
                       ("6", "."): ("7", ".", "L"),
                       ("7", " "): ("0", " ", "R"),
                       ("7", "."): ("7", ".", "L"),
                       }
final_states = {"final"}

t = TuringMachine("   ...... ...   ", 
                  initial_state = "0",
                  final_states = final_states,
                  transition_function=transition_function)

print("Input on Tape:\n" + t.get_tape())

while not t.final():
    t.step()

print("Result of the Turing machine calculation:")   
print(t.get_tape()) 

accepting_states = ["final"]

transition_function = {
    ("0", "."): ("0", ".", "R"),
    ("0", " "): ("1", " ", "R"),
    
    ("1", "."): ("1", ".", "R"),
    ("1", " "): ("2", " ", "L"),
    
    ("2", "."): ("2", ".", "L"),
    ("2", " "): ("3", " ", "R"),
    
    ("3", "X"): ("3", "X", "R"),
    ("3", "."): ("4", "X", "L"),
    ("3", " "): ("12", " ", "L"),
    
    ("4", "X"): ("4", "X", "L"),
    ("4", " "): ("5", " ", "L"),
    
    ("5", "Y"): ("5", "Y", "L"),
    ("5", "."): ("6", "Y", "R"),
    ("5", " "): ("11", " ", "R"),
    
    ("6", "Y"): ("6", "Y", "R"),
    ("6", " "): ("7", " ", "R"),
    
    ("7", "."): ("7", ".", "R"),
    ("7", "X"): ("7", "X", "R"),
    ("7", " "): ("8", " ", "R"),
    
    ("8", "."): ("8", ".", "R"),
    ("8", " "): ("9", ".", "L"),
    
    ("9", "."): ("9", ".", "L"),
    ("9", " "): ("10", " ", "L"),
    
    ("10", "."): ("10", ".", "L"),
    ("10", "X"): ("10", "X", "L"),
    ("10", " "): ("5", " ", "L"),
    
    ("11", "Y"): ("11", ".", "R"),
    ("11", " "): ("3", " ", "R"),
    
    ("12", "X"): ("12", " ", "L"),
    ("12", " "): ("12", " ", "L"),
    ("12", "."): ("13", " ", "L"),
    
    ("13", "."): ("13", " ", "L"),
    ("13", " "): ("14", " ", "R"),
    
    ("14", " "): ("14", " ", "R"),
    ("14", "."): ("15", ".", "R"),
    
    ("15", "."): ("15", ".", "R"),
    ("15", " "): ("final", " ", "N"),
}


final_states = {"final"}


t = TuringMachine(" .... ...  ", 
                  initial_state = "0",
                  final_states = final_states,
                  transition_function=transition_function,
                  head_position=1)

print("Input on Tape:\n" + t.get_tape())

while not t.final():
    t.step()

print("Result of the Turing machine calculation:")   
print(t.get_tape())

accepting_states = ["final"]

transition_function = {
    ("0", "."): ("1", " ", "L"),
    ("0", " "): ("0", " ", "R"),
    ("0", "|"): ("final", " ", "N"),
    ("0", "0"): ("0", "0", "R"),
    ("0", "1"): ("0", "1", "R"),
    ("0", "2"): ("0", "2", "R"),
    ("0", "3"): ("0", "3", "R"),
    ("0", "4"): ("0", "4", "R"),
    ("0", "5"): ("0", "5", "R"),
    ("0", "6"): ("0", "6", "R"),
    ("0", "7"): ("0", "7", "R"),
    ("0", "8"): ("0", "8", "R"),
    ("0", "9"): ("0", "9", "R"),
    
    ("1", " "): ("1", " ", "L"),
    ("1", "0"): ("0", "1", "R"),
    ("1", "1"): ("0", "2", "R"),
    ("1", "2"): ("0", "3", "R"),
    ("1", "3"): ("0", "4", "R"),
    ("1", "4"): ("0", "5", "R"),
    ("1", "5"): ("0", "6", "R"),
    ("1", "6"): ("0", "7", "R"),
    ("1", "7"): ("0", "8", "R"),
    ("1", "8"): ("0", "9", "R"),
    ("1", "9"): ("1", "0", "L"),
}

final_states = {"final"}


t = TuringMachine(" 000 ...............|  ", 
                  initial_state = "0",
                  final_states = final_states,
                  transition_function=transition_function,
                  head_position=5)

print("Input on Tape:\n" + t.get_tape())

while not t.final():
    t.step()

print("Result of the Turing machine calculation:")   
print(t.get_tape())