# Finite Automata file format:
    - States are on the line which start with "S="
    - Initial state is on the line which starts with "I="
    - Alphabet is on the line which starts with "A="
    - Final states are on the line which start with "F="
    - Transitions are specified as triplets with a comma in between
    - The letter E is reserved for Epsilon

    EBNF:
        digit ::= "0" | "1" | "2" | ... | "9"
        letter ::= "A" | "B" | "C" | ... | "a" | "b" | ... | "z" 
        alphabetItem ::= letter | digit
        initialState ::= letter {letter}
        state ::= letter {letter}
        states ::= {state ","} state
        finalStates ::= "F="states
        alphabet ::= {alphabetItem ","} alphabetItem
        transition ::= state "," alphabetItem "," state
        transitions ::= {transition "\n"}
        
        
    
    