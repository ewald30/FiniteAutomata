from FiniteAutomata import *

def printMenu():
    print("\n\n================================")
    print("              Menu              ")
    print("================================\n")
    print("1.      Print initial state.")
    print("2.      Print states.")
    print("3.      Print final states.")
    print("4.      Print alphabet.")
    print("5.      Print transitions.")
    print("6.      Check sequence.")
    print("7.      Check deterministic.")
    print("q.      Quit.\n")
    print("================================\n\n")

def run():
    while True:
        printMenu()
        cmd = input(": ")
        if cmd == '1':
            fa.printInitialState()
        elif cmd == '2':
            fa.printStates()
        elif cmd == '3':
            fa.printFinalStates()
        elif cmd == '4':
            fa.printAlphabet()
        elif cmd == '5':
            fa.printTranstions()
        elif cmd == '6':
            seq = input("Enter sequence: ")
            fa.printValidity(seq)
        elif cmd == '7':
            fa.printIsDeterministic()
        elif cmd == 'q':
            return

fa = FiniteAutomata()
fa.parseFile("FA.in")
run()