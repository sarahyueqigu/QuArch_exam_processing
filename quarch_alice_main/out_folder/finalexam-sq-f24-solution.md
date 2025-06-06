# ECE544 Fault-Tolerant Computing & Reliability Engineering
 Solution to Final Exam Sample Questions (Fall 2024)

1. Consider the reliability block diagram (RBD) shown in the following figure and answer the following questions
(HW#6 Problem 1 and HW#7 Problem 1):

a). Convert the RBD to an equivalent fault tree
b). Find all the minimal path sets.
c). Find all the minimal cut sets.
d). Generate the binary decision diagram (BDD) model of the system using the ordering of E<D<C<B<A.
e). Assume the failure probability for each component is 0.1. Find the system reliability at time t=10 hours.
f). Assume each component has the same constant failure rate of 0.1/hour. Find the system reliability at time
t=10 hours using the BDD method.

B

A

C E

D

**Please refer to solution to HW#6 Problem 1 and HW#7 Problem 1.**

2. A plant has two identical process streams A and B. Each process stream has a transfer pump and a rotary filter, as
shown in the figure. Both process streams have to be functioning to secure full production. It is assumed that
the pumps and the filters are functioning independent of each other. The reliability of a pump has been estimated
to be 0.992 while the reliability of a filter is 96.8%.

a). Determine the reliability with respect to full production for the system
b). Assume the total cost of a pump is $15 per day. The total cost of a filter is estimated to $60 per day. The
company gets a penalty of $10,000 per day when the system is not able to give full production. What is
the total cost for the system per day (on the average)?

**Solution:**


-----

3. **(HW#7 Problem 2, HW#8 Problem 1) Consider the following system fault tree model. Assume the failure**
probability for each component is:

Component A B C D E

Failure probability 0.2 0.2 0.1 0.3 0.3

AND

OR OR

_A_ AND _D_ _E_

_B_ _C_

a). Find the system reliability at time t=1000 hours.
b). Rank the importance of the four components using the Birnbaum’s measure
c). Find the importance value of component B using the diagnostic importance factor (DIF)

**Please refer to solution to HW#7 Problem 2 and HW#8 Problem 1.**

4. Construct the dynamic fault tree model for the following computer system. Processors A1 and A2 share the cold
spare A; 4 out of the 5 memory units are needed; if MIU fails, memory is not accessible; at least one bus is
required. The system requires at least 2 of the three processors, at least 4 of the memory units, at least one of the
redundant buses, and the operator, console and software to be operating correctly.

Redundant BusRedundant Bus

|Component|A|B|C|D|E|
|---|---|---|---|---|---|
|Failure probability|0.2|0.2|0.1|0.3|0.3|

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|RReedduunnddaann|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|AA11||||||||||||
|||||||||||||
|||||||||||||

|MM22|MM33|
|---|---|


-----

**Solution:**

**Similar Question in Lecture #14, Slides 12-15**

5. For the fault tree model below, assume components A and B have the failure rate of λA and λB, respectively.
Component C has the failure rate of λC after being activated.
a) find the state transition diagram of the Markov chain (HW#8 Problem#2(a))
b) find the state equations of the asymptotic solution
c) find the system unreliability in the steady-state
d) find the state equations for the time-dependent solution
e) find the Laplace transform of time-dependent state probabilities P*(s)

System failure

CSP

A B C

**Solution:**


-----

b) find the state equations of the asymptotic solution

Or using

## c) find the system unreliability in the steady-state by solving the equations in b)

d) find the state equations for the time-dependent solution

e) find the Laplace transform of time-dependent state probabilities P*(s)


-----

6. **(Lecture#15 Hands-on Problem on Slide 40) Consider a parallel system of two independent and identical**
components with failure rate λ. When one of the components fails, it is repaired. The repair time is assumed to be
exponentially distributed with repair rate μ. When both components have failed, the system is considered to have
failed and no recovery is possible. Let the number of functioning components denote the state of the system. The
state space is thus {0,1,2}. Assume the system to be in state 2 at time t=0.

a). Draw the state transition diagram for the system Markov chain.
b). Find the state equations for the time-dependent solution.
c). Find the state equations for the asymptotic solution.
d). Find the steady-state probabilities: P0, P1, P2
e). Find the Laplace transform of time-dependent state probabilities: P0*(s), P1*(s), P2* (s)

**Please refer to solution to Lecture#15 Hands-on Problem on Slide 40.**


-----

