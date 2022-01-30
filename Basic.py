#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import numpy
import qiskit
#from qiskit import QuantumCircuit, Aer, execute
#from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from azure.quantum.qiskit import AzureQuantumProvider

provider = AzureQuantumProvider (
    resource_id = "/subscriptions/b1d7f7f8-743f-458e-b3a0-3e09734d716d/resourceGroups/aq-hackathons/providers/Microsoft.Quantum/Workspaces/aq-hackathon-01",
    location = "eastus"
)
# In[1]:


#this describes our ckt
n = 2
cirk1 = QuantumCircuit(n, n)
cirk1.initialize(qiskit.quantum_info.random_statevector(2).data,0)
cirk1.initialize(qiskit.quantum_info.random_statevector(2).data,1)

#backend = Aer.get_backend('statevector_simulator')
backend = provider.get_backend("ionq.simulator")
sv1 = execute(cirk1, backend).result().get_statevector(cirk1)
states=['00','01','10','11']

sv1=numpy.array(sv1)
sv2=numpy.around(abs(sv1)**2,3)
for i in range(len(sv1)) :
    if abs(sv1[i]**2) > 0:
        print("Chances of ending in position " +states[i]+ " are " +str(sv2[i]))


cirk1.draw('mpl')            


# In[ ]:



#all the gate functions are here


# =hadmad() needs to be defiend here
def hadmad(gatenum, score,cirk1):
    bitno=input("Enter qubit no this gate will be applied on(0/1):")
    cirk1.h(int(bitno))
    gatenum=gatenum+1
    score=score+had
  
 #contnot()
def contnot(gatenum,score,cirk1):
    control_bit=input("Enter control bit(0/1)")
    target_bit=input("Enter target bit")
    cirk1.cx(int(control_bit),int(target_bit))
    gatenum=gatenum+1
    score=score+cnott

  #paulx here
def paulx(gatenum,score,cirk1):
    bitno=input("Enter qubit no this gate will be applied on(0/1):")
    cirk1.x(int(bitno))
    gatenum=gatenum+1
    score=score+X
  

  #pauly here
def pauly(gatenum,score,cirk1):
    bitno=input("Enter the qubit no to apply the y gate onto(0/1)")
    cirk1.y(int(bitno))
    gatenum=gatenum+1
    score=score+Y

  #paulz 
def paulz(gatenum,score):
    bitno=input("Enter the qubit no to apply the z gate onto(0/1)")
    cirk1.z(int(bitno))
    gatenum=gatenum+1
    score=score+Z

# rotz
def rotz(gatenum,score):
    bitno=input("Enter the qubit no to apply the R_z gate onto(0/1)")
    angle= math.radians(input("Enter the angle"))
    mathangle= math.radians(angle)
    #bitno=input("Enter the qubit no to applt the rz gate onto")
    cirk1.rz(angle,int(bitno))

    
#this is to reveal the statevector to the user for each qubit
    
def statevec_reveal(score,cirk1):
     #print("instatevic")
    backend = Aer.get_backend('statevector_simulator')
    sv1 = execute(cirk1, backend).result().get_statevector(cirk1)
    states=['00','01','10','11']

    sv1=numpy.array(sv1)
    sv2=numpy.around(abs(sv1)**2,3)
    for i in range(len(sv1)) :
        if abs(sv1[i]**2) > 0:
            print("Chances of ending in position " +states[i]+ " are " +str(sv2[i]))

    
    
    #for i,v in enumerate(sv1):
     #   if abs(v**2) > 0:
      #      print(f"Chances of ending in position {i} are {abs(v**2)}")

  


# In[ ]:


#to end the game we'll ask the user to measure the state of the virus
#so here we need a measurement module

def measurements():

    sim =   provider.get_backend("ionq.simulator")
    result = sim.run(cirk1).result()
    counts = result.get_counts()
  
    return(counts)


# In[57]:


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



# In[69]:


#Display menu
def menu_display():
    act=input("Menu:\n1.State vector reveal=sv\n2.Hadamard Gate=h\n3.X gate=x\n4.Y gate=x\n5.Z gate=x\n6.")  #create a menu here add in names of other gates in the format ive written here
    return(act)
#Functional menu
#write a switch case to implement gates and call functions
def gates_fin(act2):
            if act2=='sv':
               statevec_reveal(score,cirk1)
            if act2=='h':  
                hadmad(gatenum,score,cirk1)
            if act2=='cnot'    :
                
                contnot(gatenum,score,cirk1)
            if act2=='x'           :
                paulx(gatenum,score,cirk1)
            if act2=='y'        :
                
                pauly(gatenum,score,cirk1)
            if act2=='z':
                
                   paulz(gatenum,score,cirk1)
            if act2=='rz'            :
                
                  rotz(gatenum,score,cirk1)
            else: 
                 return('Invalid input')


# In[ ]:



#GAME MAIN:
#game UI:
#create a main function : it will call the functions we've defined before
#the main function needs to have a while loop , the game will run while scores>=0

score=500
gatenum=0
print("Welcome to S.O.S:")
print("The virus is running amock.....")
print('Whilst you\'re masked and double masked, you need to make sure the virus doesnt reach your cell')
print('You\'re required to keep the probablity of the |11> state within 5+/-2%')
init1=input('Hit \'y\' if you\'re ready for this do or die adventure....')
act1='y'
act3='y'

while init1=='y' and act3=='y':

    while score>0 and gatenum<11 and act1=='y':
        act2=menu_display()
        gates_fin(act2)
        act1=input('Would you like to use  the menu again?(y/n)')


# to win, one needs to have a have <25% counts of state 11
    act3=input('Want to measure(y/n)??') 
    if act3=='y':
        d1=measurements()
        print("Game over....")
        l1=list(d1.keys())
        l2=list(d1.values())
        print(l1)
        for i in l1:
            if i=='n11':
                s=l1.index(i)
                if (l2[s]/1024)<0.25:
                    print('Time for CHICKEN DINNER.....!')
                else :
                    print("RIP. Get well soon!")  

      


# In[ ]:




