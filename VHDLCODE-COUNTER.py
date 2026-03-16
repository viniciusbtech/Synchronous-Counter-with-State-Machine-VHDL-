from enum import Enum

class State(Enum):
    s0 = 0
    s1 = 1
    s2 = 2
    s3 = 3
    s4 = 4
    s5 = 5
    s6 = 6
    s7 = 7

state = State.s0
reset = False

while True:

    if reset:
        state = State.s0

    if state == State.s0:
        q = "0001"
        state = State.s1

    elif state == State.s1:
        q = "0111"
        state = State.s2

    elif state == State.s2:
        q = "0101"
        state = State.s3

    elif state == State.s3:
        q = "0011"
        state = State.s4

    elif state == State.s4:
        q = "0011"
        state = State.s5

    elif state == State.s5:
        q = "0000"
        state = State.s6

    elif state == State.s6:
        q = "0101"
        state = State.s7

    elif state == State.s7:
        q = "0101"
        state = State.s0

    print("Saída q =", q)

    input("Pressione Enter para simular o clock...")