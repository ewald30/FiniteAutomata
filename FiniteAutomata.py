class FiniteAutomata:
    def __init__(self):
        self._alphabet = []
        self._transitions = {}
        self._states = []
        self._finalStates = []
        self._initialState = None
        self._isDeterministic = True

    def parseFile(self, fileName):
        file = open(fileName, "r")
        lines = file.readlines()

        for line in lines:
            if line[:2] == 'S=':                                    # this line contains all the states
                self._states = line[2:].split(',')
                self._states[-1] = self._states[-1].replace('\n','')        # to remove \n from the last element

            elif line[:2] == 'I=':                                    # contains the initial state
                self._initialState = line[2:].replace('\n','')          # remove the \n

            elif line[:2] == 'A=':                                    # contains the alphabet
                self._alphabet = line[2:].split(',')
                self._alphabet[-1] = self._alphabet[-1].replace('\n', '')

            elif line[:2] == 'F=':
                self._finalStates = line[2:].split(',')
                self._finalStates[-1] = self._finalStates[-1].replace('\n', '')

            else:
                transition = line.split(',')
                transition[-1] = transition[-1].replace('\n', '')
                if self._isDeterministic:
                    for key, value in self._transitions.items():
                        if key[0] == transition[0] and value == transition[2]:
                            self._isDeterministic = False
                            break
                    key = (transition[0], transition[1])
                    self._transitions[key] = transition[2]
                print(self._transitions)

    def printStates(self):
        print("Q = ",self._states)

    def printAlphabet(self):
        print("Sigma = ",self._alphabet)

    def printInitialState(self):
        print("Q0 = ", self._initialState)

    def printFinalStates(self):
        print("F = ", self._finalStates)

    def printIsDeterministic(self):
        if self._isDeterministic:
            print("The finite automata is deterministic")
        else:
            print("The finite automata is not deterministic")

    def printTranstions(self):
        for key, value in self._transitions.items():

            print("Delta (" + str(key[0]) + ", " + str(key[1]) + ") = " + value)

    def _checkValidity(self, sequence):
        if sequence == 'E' and self._initialState in self._finalStates:
            return True

        index = 0
        current = self._initialState
        while index < len(sequence):
            key = (current, sequence[index])
            if key in self._transitions.keys():
                current = self._transitions.get(key)
                index += 1
            else:
                return False
        return True

    def printValidity(self, sequence):
        if not self._isDeterministic:
            print("Finite automata is non-deterministic")
            return

        if self._checkValidity(sequence):
            print("Sequence is accepted")
        else:
            print("Sequence is not accepted")