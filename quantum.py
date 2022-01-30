import math
import qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
#from azure.quantum.qiskit import AzureQuantumProvider

#this is to reveal the statevector to the user for each qubit

def statevec_reveal(score):
  backend = Aer.get_backend('statevector_simulator')
  sv1 = execute(cirk1, backend).result().get_statevector(cirk1)
  for i,v in enumerate(sv1):
   if abs(v**2) > 0:
     print(f"Chances of ending in position {i} are {abs(v**2)}")

#this describes our ckt
n = 2
cirk1 = QuantumCircuit(n, n)


# all the gate functions are here
# =hadmad() needs to be defiend here
def hadmad(gatenum, score):
    bitno = input("Enter qubit no this gate will be applied on:")
    cirk1.h(bitno)
    gatenum = gatenum + 1
    score = score + had


# contnot()
def contnot(gatenum, score):
    control_bit = input("Enter control bit")
    target_bit = input("Enter target bit")
    cirk1.cx(control_bit, target_bit)
    gatenum = gatenum + 1
    score = score + cnott
    # paulx here


def paulx(gatenum, score):
    bitno = input("Enter qubit no this gate will be applied on:")
    cirk1.x(bitno)
    gatenum = gatenum + 1
    score = score + X

    # pauly here


def pauly(gatenum, score):
    bitno = input("Enter the qubit no to apply the y gate onto")
    cirk1.y(bitno)
    gatenum = gatenum + 1
    score = score + Y

    # paulz


def paulz(gatenum, score):
    bitno = input("Enter the qubit no to apply the z gate onto")
    cirk1.z(bitno)
    gatenum = gatenum + 1
    score = score + Z


# rotz
def rotz(gatenum, score):
    angle = math.radians(input("Enter the angle"))
    mathangle = math.radians(angle)
    bitno = input("Enter the qubit no to applt the rz gate onto")
    cirk1.rz(mathangle, bitno)


# to end the game we'll ask the user to measure the state of the virus
# so here we need a measurement module

def measurements():
    sim = Aer.get_backend('aer_simulator')
    result = sim.run(cirk1).result()
    counts = result.get_counts()

    return (counts)

#here we'll be initializing a few stuff

user_state=1
points_init=500
#defining point values of each operation based on their weight:
had=-10
cnott=-10
X=-20
Y=-20
Z=-20
state_reveal=-10

#here we need to assign a random statevector to the virus:

def init_virus():
    firststate= cirk1.initialize(qiskit.quantum_info.random_statevector(2).data,0)
    secondstate=cirk1.initalize(qiskit.quantum_info.random_statevector(2).data,1)

def menu_display():
  act=input("Menu:\n1.State vector reveal=sv\n2.Hadamard Gate=h\n3.X gate=x\n4.Y gate=x\n5.Z gate=x\n6.")  #create a menu here add in names of other gates in the format ive written here
  return(act)


# GAME MAIN:
# game UI:
# create a main function : it will call the functions we've defined before
# the main function needs to have a while loop , the game will run while scores>=0

score = 500
gatenum = 0
print("Welcome to S.O.S:")
print("The virus is running amock.....")
print('Whilst you\'re masked and double masked, you need to make sure the virus doesnt reach your cell')
print('You\'re required to keep the probablity of the |11> state within 5+/-2%')
init1 = input('Hit \'y\' if you\'re ready for this do or die adventure....')
while init1 == 'y' or init1 == 'Y':
    while score > 0 or gatenum < 11 or while act1 == 'y':
        act2 = menu_display()


        # write a switch case to implement gates and call functions

        def gates_fin(act2):
            switch
            {
                'sv': statevec_reveal(score),
                'h': hadam(gatenum, score),
                'cnot': contnot(gatenum, score),
                'x': paulx(gatenum, score),
                'y' = pauly(gatenum, score),
                      'z' = paulz(gatenum, score),
                            'rx' = rotz(gatenum, score),
            } return switch.get(act2, 'Invalid input')


        act1 = input('Would you like to use  the menu again?(y/n)')
        # to win, one needs to have a have <25% counts of state 11
        act3 = input('Want to measure(y/n)??')
        if act3 == 'y':
            d1 = measurements()
            print("Game over....")
            l1 = list(int(d1.keys()))
            l2 = list(d2.values())
            for i in l1:
                if i == 11:
                    s = l1.index(i)
                    if (l2[s] / 1024) < 0.25:
                        print('Time for CHICKEN DINNER.....!')
                    else:
                        print("RIP. Get well soon!")

