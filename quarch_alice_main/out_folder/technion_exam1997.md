## VLSI Architecture Design Course Final Exam Spring 1997

##### Student name:_____________________Student number_______________
 date:________________
 This exam contains three questions.  You must answer all questions. The exam duration is 2:00 hours. Please fill the answers ON THE EXAM forms. Additional support to your findings you should add in your exercise-book. 
 Good luck!

1


-----

#### Question 1 (30%):

Given is an in order, single pipeline CPU, with Internal combined (Instruction/Data) L1 cache,
which is physically tagged. The CPU internal operating frequency is 1GHz with its average Cycle
Per Instruction is 2.0 (with perfect Branch prediction, perfect cache (L1)) .
The CPU’s external bus frequency is 100Mhz.

# L2/Memory
 CPU

### Internal freq. 100Mhz 1000Mhz

##### Figure 1

Branches occur on the average every 5 instructions, and the branch prediction accuracy is 90%,
and the BTB hit rate is 100%. Average branch misprediction penalty is 20 internal cycles. The
internal combined L1 cache hit rate (per access) is 95%. The access latency (for cache line) to L2
is 4 cycles (at a rate of 100Mhz), and the L2 hit rate is 100%. The machine’s average instruction
and data access is 1 access/instruction. TLB hit rate is 99% and its miss penalty is 15 cycles (at
100mhz).

Compute the average statistical CPI of this CPU:

A. What is the CPI degradation due to wrong Branch prediction?
Answer A:__________________ Cycle/Instruction

B.  What is the CPI degradation due to internal cache misses?
Answer B:__________________ Cycle/Instruction

C.  What is the CPI degradation due TLB misses?
Answer C:__________________ Cycle/Instruction

D.  What is the average statistical CPI of this CPU?
Answer D:__________________ Cycle/Instruction

2

|L2/Memory CPU Internal freq. 100Mhz 1000Mhz|Col2|
|---|---|
|CPU Internal freq. 1000Mhz||
||100Mhz|


-----

#### Question 2 (35%):

A CPU with >4 general purpose execution units, and on die Instruction and data caches is given.
The CPU micro-architecture supports Out Of Order execution, and its internal to external
frequency ratio is >20.
Following (Figure 2) is the CPU with Instruction Per Cycle (IPC) vs Time curve.

You should identify and explain what are the reasons (what) for the curve changes (see figure 2
points A=”saturation”, B=”the drop”, C=”end of drop”, and D=”the ramp up”) .
Answer below, for each point, what are the causes (1=why), the interval delay (2=interval), and
the potential performance improvement (3=solutions).

IPC

A
B

D 1 C D 2

time

##### Figure 2

 A. 1. ____________________________________________ A. 2. Interval from A to D1:____________________________ A. 3. ____________________________________________     ____________________________________________
 B. 1. ____________________________________________ B. 2. Interval from B to A:____________________________ B. 3. ____________________________________________     ____________________________________________
 C. 1. ____________________________________________ C. 2. Interval from C to B:____________________________ C. 3. ____________________________________________     ____________________________________________
 D. 1. ____________________________________________ D. 2. Interval from D2 to C:____________________________ D. 3. ____________________________________________      ____________________________________________
 E. What is the cause of the Interval from one B to the next B?    ____________________________________________    ____________________________________________

3


-----

#### Question 3 (35%):

This question will confront the issue of a partially decoded instruction cache in a variable
instruction length machine.
##### Figure 3 depicts machine A with a 5 stage pipe, and 4 cycle latency to the L2 cache (i.e.,
Instruction L1 cache miss and L2 cache hit causes a 4 cycle penalty. Machine B has a shorter
pipe, one pipe stage was reduced relative to machine A. The instruction length decode stage was
removed, and the instruction length information is kept in the L1 instruction cache. On machine B,
the length decode stage is between the instruction L1 cache and L2 cache, thus increasing the
instruction L1 miss penalty to 5 cycles.

A) Propose a structure for the instruction L1 cache of machine B, with minimal area impact.

Answer A:_________________________________________________________

__________________________________________________________________

__________________________________________________________________

__________________________________________________________________

#####   Machine A  Machine B
 L2 Cache   L2 Cache

###### latency 4 L1 I-cache
instruction length decode

######   latency 5

Stage 1: instruction fetch L1 I-cache

Stage 2: instruction length decode Stage 1: instruction fetch

Stage 3: Stage 2:

Stage 4: Stage 3:

Stage 5: Stage 4:

##### Figure 3 - Machine A has a length decode pipe stage, machine B has a partially decoded cache.

4

|Machine B|Col2|
|---|---|
|L2 Cache||
|instruction length decode||
|latency 5|L1 I-cache|
|Stage 1: instruction fetch||
|||
|Stage 2:||
|||
|Stage 3:||
|||
|Stage 4:||


-----

The following code section demonstrates a problem with machine B’s pipeline for variable length
Instruction Set Architectures (ISA). Assume value of R1 is 1 before this code begins. Assume a
16 byte instruction cache line size.

Address Instruction Comments
1F7h Loop: ADD R1, R1, #1 Increment R1 by 1
1F9h AND R1, R1, #00000001 Mask R1 with the value 1
1FEh JZ R1, Even If R1=0 jump to label Even
200h ADD R3, R3, #1 Increment R3 by 1
202h JMP Odd Jump to label Odd
204h Even: SUB R2, R2, #1 Decrement R2 by 1
206h Odd: JNZ R2, Loop If R2!=0 jump to label Loop

##### Figure 4

B) Describe the problem of a length decoded instruction cache for variable length ISAs, as
reflected by the above loop?

Answer B:_________________________________________________________

__________________________________________________________________

__________________________________________________________________

__________________________________________________________________

C) How many fetch requests are required in order to fetch all the instructions in the code above?
Note the address of each instruction, and the address 200h begins on a new cache line.

Answer C:_________________________________________________________

__________________________________________________________________

__________________________________________________________________

__________________________________________________________________

5


-----

Machine C (Figure 5) has a Trace cache instead of a partially decoded cache. The trace cache
lines can contain up to 3 instructions per line. A trace has only one entry point - the beginning of
the trace. Every backward taken branch ends the current trace (i.e. the instruction after a
backward taken branch begins a new trace).

##### Machine C
   L2 Cache

instruction length decode

Trace build

###### Trace
 Cache Stage 1: instruction fetch

Stage 2:

Stage 3:

##### Figure 5 - Machine C has a Trace Cache

D) How would the code above (Figure 4) be mapped into the Trace Cache assuming the loop
runs 10 times? Write the instructions into the TC lines below. Note the lines in which a new
trace begins. Use as many lines that you need.

### Instruction1 Instruction2 Instruction3
 Line1
 Line2
 Line3
 Line4
 Line5

6

|Col1|Instruction1|Instruction2|Instruction3|
|---|---|---|---|
|Line1||||
|Line2||||
|Line3||||
|Line4||||
|Line5||||


-----

