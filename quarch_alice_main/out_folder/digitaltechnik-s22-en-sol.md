Family Name: SOLUTIONS First Name: Student ID:

###### Final Exam

#### Digital Design and Computer Architecture (252-0028-00L)

 ETH Zürich, Spring 2022

###### Prof. Onur Mutlu

Problem 1 (40 Points): Boolean Logic Circuits

Problem 2 (50 Points): Finite State Machines

Problem 3 (30 Points): ISA vs. Microarchitecture

Problem 4 (60 Points): Verilog

Problem 5 (30 Points): Memory Potpourri

Problem 6 (70 Points): Performance Evaluation

Problem 7 (70 Points): Pipelining

Problem 8 (60 Points): Tomasulo's Algorithm

Problem 9 (45 Points): GPUs and SIMD

Problem 10 (70 Points): Branch Prediction

Problem 11 (BONUS: 50 Points): Prefetching

Problem 12 (BONUS: 70 Points): Caches

Total (645 (525+120 bonus) Points):

Examination Rules:

1. Written exam, 180 minutes in total.

2. No books, no calculators, no computers or communication devices. 3 double-sided (or 6 onesided) A4 sheets of handwritten notes are allowed.

3. Write all your answers on this document; space is reserved for your answers after each question.

4. You are provided with scratchpad sheets. Do not answer questions on them. We will not collect them.

5. Clearly indicate your nal answer for each problem. Answers will only be evaluated if they are readable.

6. Put your Student ID card visible on the desk during the exam.

7. If you feel disturbed, immediately call an assistant.

8. Write with a black or blue pen (no pencil, no green, red or any other color).

9. Show all your work. For some questions, you may get partial credit even if the end result is wrong due
to a calculation mistake. If you make assumptions, state your assumptions clearly and precisely.

10. Please write your initials at the top of every page.

Tips:

_• Be cognizant of time. Do not spend too much time on one question._

_• Be concise. You may be penalized for verbosity._

_• Show work when needed. You will receive partial credit at the instructors' discretion._

_• Write legibly. Show your nal answer._


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

This page intentionally left blank

Final Exam Page 1 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 1 Boolean Logic Circuits [[40 points]]

During your job interview, you are asked to design a combinational circuit with a four-bit input,
{A, B, C, D} (A is the most signicant bit and D is the least signicant bit), and two 1-bit outputs,
_Factorial and Div4. The value of each output is determined as follows:_


The output Factorial is 1 only when the input 4-bit number is a product of ALL positive integers
that are less than or equal to the input number.


The output Div4 is 1 only when the input 4-bit number is divisible by 4.


Otherwise, the corresponding outputs are zero.

Please answer the following four questions.

(a) [10 points] Fill in the missing entries in the truth table below for the combinational circuit you are
designing.

Inputs Outputs

_A_ _B_ _C_ _D_ _Factorial_ _Div4_

0 0 0 0 1 1

0 0 0 1 1 0

0 0 1 0 1 0

0 0 1 1 0 0

0 1 0 0 0 1

0 1 0 1 0 0

0 1 1 0 0 0

0 1 1 1 0 0

1 0 0 0 0 1

1 0 0 1 0 0

1 0 1 0 0 0

1 0 1 1 0 0

1 1 0 0 0 1

1 1 0 1 0 0

1 1 1 0 0 0

1 1 1 1 0 0

Final Exam Page 2 of 28

|Inputs|Col2|Col3|Col4|Outputs|Col6|
|---|---|---|---|---|---|
|A|B|C|D|Factorial|Div4|
|0|0|0|0|1|1|
|0|0|0|1|1|0|
|0|0|1|0|1|0|
|0|0|1|1|0|0|
|0|1|0|0|0|1|
|0|1|0|1|0|0|
|0|1|1|0|0|0|
|0|1|1|1|0|0|
|1|0|0|0|0|1|
|1|0|0|1|0|0|
|1|0|1|0|0|0|
|1|0|1|1|0|0|
|1|1|0|0|0|1|
|1|1|0|1|0|0|
|1|1|1|0|0|0|
|1|1|1|1|0|0|


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

(b) [10 points] Express the output Div4 as the simplest sum of products representation. Show your
work step-by-step.

_Div4 = (C.D)_

Explanation:

_Div4 = (A · B · C · D) + (A · B · C · D) + (A · B · C · D) + (A · B · C · D)_
_Div4 = (A · C · D)(B + B) + (A · B · C · D) + (A · B · C · D)_
_Div4 = (A · C · D) + (A · B · C · D) + (A · B · C · D)_
_Div4 = (C · D)(A · B + A) + (A · B · C · D)_
_Div4 = (C · D · B) + (C · D · A) + (A · B · C · D)_
_Div4 = (C · D · A) + (C · D)(A · B + B)_
_Div4 = (C · D)(A + A) + (C · D · B)_
_Div4 = (C · D) + (C · D · B)_
_Div4 = (C · D)_

(c) [20 points] Find the simplest representation of the Factorial output by using only NOR gates.
Show your work step-by-step.

_Factorial = B + A + C + C + D + D_
Explanation:

_Factorial = (A + B + C + D) · (A + B + C + D) · (A + B + C + D)_

_Factorial = (A · (A + B + C + D) + B · (A + B + C + D) + C · (A + B + C + D) + D ·_
(A + B + C + D)) (A + B + C + D)
_·_

_Factorial = (A + AB + AC + AD + AB + B + BC + BD + AC + CB + C + CD +_
_AD + BD + CD + DD)_ (A + B + C + D)
_·_

_Factorial = (A + B + C) · (A + B + C + D)_

_Factorial = (A + AB + AC + AD) + (AB + B + BC + BD) + (AC + BC + CD)_

_Factorial = B + A + CD_

_Factorial = B + A + CD_

_Factorial = B + A + C + D_

_Factorial = B + A + C + C + D + D_

Final Exam Page 3 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 2 Finite State Machines [[50 points]]

The Polybahn from Central to Polyterasse has broken down! To x it you need to design a nite state
machine that controls the Polybahn's two doors A and B.

The Polybahn should operate as follows:


Initially the Polybahn is empty and idle, and passengers can enter through door A.


The Polybahn is full when it carries 2 passengers.


When it is full and idle, the Polybahn goes into transit to the other station with both doors closed.


After reaching the station, the Polybahn will unload all passengers through door B, while door A
is still closed.


After the last passenger has exited the Polybahn, door B closes and the Polybahn becomes idle.


Should (1) a passenger fall out of the Polybahn during transit, or (2) the Polybahn become overfull
(≥ 3 passengers) at any point, it stops in emergency mode, where it opens all doors and remains
(unless reset to the initial idle state).

The FSM receives two input bits, with the following meaning:

Input Meaning

00 no change

01 exactly one passenger left

10 exactly one passenger entered

11 the Polybahn arrived in a station

The FSM produces two output bits: The rst bit, A, holds door A open when it is 1. The second bit,
B, holds door B open when it is 1.

(a) [25 points] Complete the Moore-type FSM below by (1) drawing the transition edges between the
states (including reset), (2) specifying the edges' respective input bits, and (3) specifying the output
bits of each state. Any input for which no outgoing edge is specied is assumed as a self loop. The
6 given states are sucient, do not draw additional states.
Note: Passengers sometimes slip in or out through incorrect doors, or even through closed doors.
Your FSM must correctly handle such cases.

Final Exam Page 4 of 28

|Input|Meaning|
|---|---|
|00|no change|
|01|exactly one passenger left|
|10|exactly one passenger entered|
|11|the Polybahn arrived in a station|


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

(b) [25 points] You need to design a second FSM that controls only the bell. The bell should ring (i.e.,
the output bit is 1) whenever the Moore-type FSM you designed for part (a) opens or closes a
door, and is constantly ringing in the case of an emergency.

Complete the Mealy-type FSM below by (1) drawing the transition edges between the states (including reset), and (2) specifying the edges' respective input and output bits. Label edges in the
following format: [input0][input1]/[bell], e.g., 10/0 = passenger entered, bell o. Any input for
which no outgoing edge is specied is assumed as a self loop with output 0.

Final Exam Page 5 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 3 ISA vs. Microarchitecture [[30 points]]

Circle whether each of the following is an aspect of the ISA or the microarchitecture.

Note: we will subtract 1 point for each incorrect answer and award 0 points for unanswered questions.

1. [2 points] Two-level global branch prediction.

1. ISA 2. Microarchitecture

2. [2 points] Location of the bits that identify the destination register in an ADD instruction.

1. ISA 2. Microarchitecture

3. [2 points] Number of instructions fetched per cycle.

1. ISA 2. Microarchitecture

4. [2 points] Ratio of the number of oating-point to integer general-purpose registers.

1. ISA 2. Microarchitecture

5. [2 points] Number of integer arithmetic and logic units (ALUs).

1. ISA 2. Microarchitecture

6. [2 points] Instruction issue width of the processor core's pipeline.

1. ISA 2. Microarchitecture

7. [2 points] SIMD support.

1. ISA 2. Microarchitecture

8. [2 points] L3 cache replacement policy.

1. ISA 2. Microarchitecture

9. [2 points] Width of the data bus to memory.

1. ISA 2. Microarchitecture

10. [2 points] The size of the addressable memory by programs.

1. ISA 2. Microarchitecture

11. [2 points] Number of cycles it takes to execute an ADD instruction.

1. ISA 2. Microarchitecture

12. [2 points] Ability to choose a specic cache replacement policy using operating system code.

1. ISA 2. Microarchitecture

13. [2 points] Number of read/write ports in the physical register le.

1. ISA 2. Microarchitecture

14. [2 points] Function of each bit in a programmable prefetcher's conguration register.

1. ISA 2. Microarchitecture

15. [2 points] Number of L3 cache banks.

1. ISA 2. Microarchitecture

Final Exam Page 6 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 4 Verilog [[60 points]]

 4.1 What Does This Code Do? [[30 points]]

Analyze the following Verilog module and answer the question.

1 **module mystery_module (clk, en, in1, in2, out);**

2

3 **input clk, en;**

4 **input[63:0] in1;**

5 **input[7:0] in2;**

6 **output reg[10:0] out = 0;**

7

8 **reg[2:0] var1 = 0;**

9

10 **always @(posedge clk) begin**

11 out <= out;

12 **if (en & (var1 == 0)) begin**

13 var1 <= var1 + 1’b1;

14

15 **if (in2[var1])**

16 out <= 11’d0 + in1[var1*8 +: 8];

17 **else**

18 out <= 11’d0 - in1[var1*8 +: 8];

19 **end**

20

21 **if (var1 != 0) begin**

22 var1 <= var1 + 1’b1;

23

24 **if (in2[var1])**

25 out <= out + in1[var1*8 +: 8];

26 **else**

27 out <= out - in1[var1*8 +: 8];

28 **end**

29 **end**

30

31 **endmodule**


Assume that the inputs in1 and in2 always have the following values:
in1 = 64’h0807060504030201
in2 = 8’b10111011

What unsigned decimal values does the out signal get in the following waveform diagram? Fill in the
gray boxes with an out value for each clk cycle. Briey explain your answer.

_posedge 0_ _posedge 1 …_

**0** **0** **1** **3** **0** **4** **9** **15** **8** **16** **16**

###### …

**_fill in all 11 gray boxes_**

|0 0 1 3 0 4 9 15 8 16 16|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||3|0|4|9|15|8|16|16|
|0|||||||||
||||||||||


Final Exam Page 7 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

Brief explanation (to help us award you partial credit):

Explanation. Once en becomes 1, the mystery_module begins processing the inputs in1
and in2.
The output signal out is initially 0 (line 6).
var1 is used to index both in1 and in2. in1 is indexed in 8-bit data chunks and every bit
in in2 is indexed separalety. var1 is initially 0 and indexes both inputs starting from their
least-signicant bits.
When var1 is 0, the mystery_module adds (if in2[0] = 1) or subtracts (if in2[0] =
0) the least signicant 8 bits of in1 (i.e., in1[7:0]) to/from the 11-bit out register. In
consecutive cycles, var1 gets incremented by 1 and the module adds or subtracts the other
8-bit data chunks in in1 to/from out.

For the given values of in1 and in2, out gets the following values:
cycle 0: out = 0 (en = 0 so out remains 0)
cycle 1: out = 0 (en = 1 but out will be updated for the next cycle (after posedge 2))
cycle 2: out = 0 + 1 = 1
cycle 3: out = 1 + 2 = 3
cycle 4: out = 3 - 3 = 0
cycle 5: out = 0 + 4 = 4
cycle 6: out = 4 + 5 = 9
cycle 7: out = 9 + 6 = 15
cycle 8: out = 15 - 7 = 8
cycle 9: out = 8 + 8 = 16
cycle 10: out = 16 (all inputs have been processed. var1 becomes 0 and out remains as is
for future cycles unless en becomes 1)

Final Exam Page 8 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 4.2 Complete the Verilog code [[30 points]]

For each numbered blank 1 - 5 in the following Verilog code, mark the choice below (i.e., one of
options A, B, C, D) that makes the Verilog module operate as described in the comments. The resulting
code must have correct syntax.

1 **module my_module (input clk, input rst,**

2 **input[1:0] data,** 1 result);

3

4 2 state = 2’b00; // defining a 2-bit signal with an initial value of 0

5

6 **always @(posedge clk) begin**

7 **case (state)**

8 2’b00:

9 state <= state + 3 ; // set the next ’state’ to 2’b11

10 2’b01:

11 state <= 2’b00;

12 2’b10: begin

13 state <= 2’b11;

14

15 **if ( 4 data)** // set the next ’state’ to 2’b01 if

16 state <= 2’b01; // all bits of ’data’ are 1

17 **end**

18 2’b11:

19 state <= 2’b10;

20 **endcase**

21

22 **end**

23

24 **assign result =** 5 state; // assign 1’b1 to ’result’ if ’state’ has any bit set to 1

25 // otherwise assign 1’b0

26 **endmodule**

Provide your choice for each blank 1 - 5 below. Circle only one of A, B, C, D for each blank.

1 : A. output B. output reg C. output reg[0:0] D. input reg

2 : A. reg[1:0] B. reg C. wire D. wire[1:0]

3 : A. 1'b3 B. 3'b2 C. 2'd11 D. 3

4 : A. || B. & C. ! D. 1

5 : A. | B. & C. && D. ˆ

Final Exam Page 9 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

Explanation.

1 : result must be specied as a single bit 'output' signal because it gets assigned either
1'b0 or 1'b1 via an 'assign' operator. It cannot be specied as a 'output reg' because the
'assign' operator can be used only with 'wire' signals. Note: 'output' is the same as 'output
wire'.

2 : state is a two-bit signal (as we can tell from lines 8, 10, 12) and must be a 'reg' because
it gets assigned a value in an 'always' block.

3 : In order to transition to state = 3 from state = 0, we need to add 3. Note that A.
1'b3 is not a valid syntax as 3 is not a binary number. Not in the choices, but 1'd3 would also
be incorrect since 3 cannot be encoded with a single bit. C. 2'd11 has a similar problem as
decimal 11 cannot be encoded with 2 bits.

4 : In the given choices, only the AND-reduction (&) operator provides the expected functionality of resulting in 1 when all bits of data are 1.

5 : In the given choices, only the OR-reduction (|) operator provides the expected functionality of resulting in 1 when state contains at least one 1.

Final Exam Page 10 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 5 Memory Potpourri [[30 points]]

Read the following statements about memory organization & technology. Circle True if the statement
is true and False otherwise. Note: we will subtract 1 point for each incorrect answer and award 0
points for unanswered questions.

1. [[2 points] ]A main memory access typically consumes less energy than a register le access.

1. True 2. False

2. [2 points] Building a larger memory array by increasing the length of the array's wordlines and
bitlines increases the cost ($) but does not increase the access time of the array.

1. True 2. False

3. [2 points] Activating a DRAM cell temporarily destroys the value stored in the DRAM cell.

1. True 2. False

4. [2 points] DRAM cost ($) per bit is much higher than that of SRAM.

1. True 2. False

5. [2 points] The memory hierarchy of a typical computer system comprises dierent memory technologies.

1. True 2. False

6. [2 points] Recently accessed data should be kept at the bottom-level in the memory hierarchy (e.g.,
main memory or disk) and not at the top-level (e.g., caches) in the hierarchy.

1. True 2. False

7. [2 points] A program with no branches has high temporal locality in its instruction memory references.

1. True 2. False

8. [2 points] A cache that has a block size equal to word size of memory access instructions cannot
exploit spatial locality.

1. True 2. False

9. [2 points] Memory banking enables concurrent access to the memory structure.

1. True 2. False

10. [2 points] In DRAM, accesses to dierent rows in one bank can be serviced faster compared to
accesses to the same row in one bank.

1. True 2. False

11. [2 points] PCM is non-volatile, which means PCM retains stored data even when it is powered o.

1. True 2. False

12. [2 points] If a hypothetical system is not constrained by chip area, memory cost ($), and energy
consumption, DRAM would be the best memory technology to use in that system.

1. True 2. False

13. [2 points] The entire page table is typically stored in physical memory.

1. True 2. False

14. [2 points] Virtual-to-physical address translation is on the critical path of a memory access.

1. True 2. False

15. [2 points] Virtual memory makes programmer's and microarchitect's tasks easier.

Final Exam Page 11 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

1. True 2. False

Final Exam Page 12 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 6 Performance Evaluation [[70 points]]

Some fellow students are working on a project called AwesomeMEM, where their goal is to optimize the
memory hierarchy (caches and DRAM) to enhance the performance of a multi-core system.

They evaluate two system congurations. First, the Baseline conguration constitutes a system with
two processors, a last-level cache (LLC), and DRAM as main memory. Second, the AwesomeMEM
conguration builds on top of the Baseline conguration by employing optimizations to the memory
hierarchy.

The students evaluate the performance benets of AwesomeMEM in simulation as follows:

1. First, they collect performance metrics of four single-threaded applications (App1, App2, App3,
_App4) running in isolation in the Baseline conguration._

2. Second, they create two-application mixes to perform a multi-program simulation, where two applications run concurrently in the Baseline conguration, each in a dedicated processor. They
evaluate two application mixes: Mix1 (consisting of App1 and App2); and Mix2 (consisting of
_App3 and App4)._

3. Third, they use the same two-application mixes as in the second step to perform a multi-program
simulation, where two applications run concurrently in the AwesomeMEM conguration, each in
a dedicated processor.

Table 1 summarizes the performance metrics the students collected for each step.

Table 1: Performance metrics the students collected.

Execution Application Executed Executed LLC Branch DRAM Bank

Conguration Application

Mode Mix Instructions Cycles Miss Rate (%) Misprediction Rate (%) Conict Rate (%)

_App1_ 100,000 40,000 26% 1% 42%

Single- N/A Baseline _App2_ 100,000 800,000 99% 1% 94%
threaded _App3_ 100,000 500,000 52% 1% 89%

_App4_ 100,000 20,000 10% 1% 14%

Baseline _App1_ 100,000 200,000 99% 1% 97%

_Mix1_ AwesomeMEM _AppApp21_ 100,00080,000 900,000100,000 65% 1% 55%

Multi- _App2_ 80,000 400,000
programmed Baseline _App3_ 100,000 600,000 60% 1% 90%

_Mix2_ AwesomeMEM _AppApp43_ 100,00080,000 400,00020,000 50% 1% 45%

_App4_ 100,000 20,000

Answer the following questions based on the performance metrics the students collected.

(a) [20 points] What is the Instructions Per Cycle (IPC) of each of the four applications when the
application is executed in isolation in the Baseline conguration? Show your work.

_App1:_

_IPC =_ [#][instructions]#cycles = [100]40,[,]000[000] [=][ 2][.][5]

_App2:_

_IPC =_ [#][instructions]#cycles = 800[100],[,]000[000] [=][ 0][.][125]

_App3:_

_IPC =_ [#][instructions]#cycles = 500[100],[,]000[000] [=][ 0][.][2]

_App4:_

_IPC =_ [#][instructions]#cycles = [100]20,[,]000[000] [=][ 5]

Final Exam Page 13 of 28

|Execution Mode|Application Mix|Con guration|Application|Executed Instructions|Executed Cycles|LLC Miss Rate (%)|Branch Misprediction Rate (%)|DRAM Bank Con ict Rate (%)|
|---|---|---|---|---|---|---|---|---|
|Single- threaded|N/A|Baseline|App1|100,000|40,000|26%|1%|42%|
||||App2|100,000|800,000|99%|1%|94%|
||||App3|100,000|500,000|52%|1%|89%|
||||App4|100,000|20,000|10%|1%|14%|
|Multi- programmed|Mix1|Baseline|App1|100,000|200,000|99%|1%|97%|
||||App2|100,000|900,000||||
|||AwesomeMEM|App1|80,000|100,000|65%|1%|55%|
||||App2|80,000|400,000||||
||Mix2|Baseline|App3|100,000|600,000|60%|1%|90%|
||||App4|100,000|20,000||||
|||AwesomeMEM|App3|80,000|400,000|50%|1%|45%|
||||App4|100,000|20,000||||


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

To measure the system throughput of a multi-core system, the students use the weighted speedup
metric, which sums the Instructions Per Cycle (IPC) slowdown experienced by each application
compared to when it is run alone (IPCi[alone]) for the same number of instructions as it executed in
the multi-programmed application mix (IPCi[shared]):


System Throughput = Weighted Speedup = [�]i


_IP Ci[shared]_

_IP Ci[alone]_


(b) [20 points] What is the IPCi[shared], i ∈{App1, App2, App3, App4}, of each of the four applications
when they are executed concurrently in accordance with their multi-programmed application mix
in the Baseline and AwesomeMEM congurations? Show your work.

_App1:_

Baseline: For the Baseline: IPCApp[shared]1 = [#][instructions]#cycles = 200[100],[,]000[000] [=][ 0][.][5]

AwesomeMEM: For AwesomeMEM : IPCApp[shared]1 = [#][instructions]#cycles = 10080,,000000 [=][ 0][.][8]

_App2:_

Baseline: For the Baseline: IPCApp[shared]2 = [#][instructions]#cycles = 900[100],[,]000[000] [=][ 0][.][11]

AwesomeMEM: For AwesomeMEM : IPCApp[shared]2 = [#][instructions]#cycles = 40080,,000000 [=][ 0][.][2]

_App3:_

Baseline: For the Baseline: IPCApp[shared]3 = [#][instructions]#cycles = 600[100],[,]000[000] [=][ 0][.][16]

AwesomeMEM: For AwesomeMEM : IPCApp[shared]3 = [#][instructions]#cycles = 40080,,000000 [=][ 0][.][2]

_App4:_

Baseline: For the Baseline: IPCApp[shared]4 = [#][instructions]#cycles = [100]20,[,]000[000] [=][ 5]

AwesomeMEM: For AwesomeMEM : IPCApp[shared]4 = [#][instructions]#cycles = [100]20,[,]000[000] [=][ 5]

(c) [10 points] What is the weighted speedup of each of the two application mixes when it is executed
in the Baseline conguration? Show your work.

_Mix1:_

Weighted Speedup = _IP Ci[shared]_ = _IP CApp[shared]1_ + _IP CApp[shared]2_

[�]i _IP Ci[alone]_ _IP CApp[alone]1_ _IP CApp[alone]2_

Weighted Speedup = 2[0].[.]5[5] [+][ 0]0.[.]125[11] [=][ 1][.][08]

Final Exam Page 14 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

_Mix2:_

Weighted Speedup = _IP Ci[shared]_ = _IP CApp[shared]3_ + _IP CApp[shared]4_

[�]i _IP Ci[alone]_ _IP CApp[alone]3_ _IP CApp[alone]4_

Weighted Speedup = [0]0[.].[16]2 [+][ 5]5 [=][ 1][.][8]

(d) [10 points] What is the weighted speedup of each of the two application mixes when it is executed
in the AwesomeMEM conguration? Show your work.

_Mix1:_

Weighted Speedup = _IP Ci[shared]_ = _IP CApp[shared]1_ + _IP CApp[shared]2_

[�]i _IP Ci[alone]_ _IP CApp[alone]1_ _IP CApp[alone]2_

Weighted Speedup = 2[0].[.]5[8] [+] 00.125.2 [=][ 1][.][92]

_Mix2:_

Weighted Speedup = _IP Ci[shared]_ = _IP CApp[shared]3_ + _IP CApp[shared]4_

[�]i _IP Ci[alone]_ _IP CApp[alone]3_ _IP CApp[alone]4_

Weighted Speedup = 0[0].[.]2[2] [+][ 5]5 [=][ 2]

The students do not want to reveal the primary technique behind AwesomeMEM. When asked, they
provided the following list of architectural techniques and told you that some of them could be the reason
behind AwesomeMEM 's system throughput improvement:

(i) AwesomeMEM increases the LLC capacity by 2× that of the Baseline.

(ii) AwesomeMEM randomizes main memory requests to reduce DRAM bank conicts.

(iii) AwesomeMEM employs a perfect branch predictor that always predicts a branch's direction correctly.

(iv) AwesomeMEM employs an ecient hardware prefetcher.

(e) [10 points] Which of the above explanations cannot possible be a reason for AwesomeMEM 's
higher performance over the Baseline? Explain your reasoning based on the data in Table 1.

Option (iii) cannot possible be a reason for AwesomeMEM 's performance improvement
compared to the Baseline.

Explanation:
(iii) is not possible since the branch misprediction rate n the AwesomeMEM conguration is the same for Mix1 and Mix2 compared to the Baseline conguration.

(i) is possible since LLC miss rate in the AwesomeMEM conguration drops for Mix1
and Mix2 compared to the Baseline conguration.

(ii) is possible since bank conicts in the AwesomeMEM conguration drops for Mix1
and Mix2 compared to the Baseline conguration.

(iv) is possible since LLC miss rate in the AwesomeMEM conguration drops for Mix1
and Mix2 compared to the Baseline conguration.

Final Exam Page 15 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 7 Pipelining [[70 points]]

The following piece of code runs on an in-order pipelined processor as shown in the table (F: Fetch, D:
Decode, E: Execute, M: Memory, W: Write back). Instructions are in the form Instruction Destination,Source1,Source2/Immediate. For example, ADD A, B, C means A ← B + C.

Cycles 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

1 MUL R5, R6, R7 F D1 D2 E1 E2 E3 M W

2 ADDI R4, R6, 5 F - D1 E1 - - M W

3 MUL R4, R7, R8 F D1 D2 E1 E2 E3 M W

4 ADD R5, R5, R6 F - D1 E1 - - M W

5 ADD R6, R7, R5 F D1 - - - E1 M W

6 ADD R7, R1, R4 F - - - D1 D2 E1 M W

Use this information to reverse engineer the microarchitecture of this processor to answer the following
questions. Answer the questions as precisely as possible with the provided information. If the provided
information is not sucient to answer a question, answer Unknown and explain your reasoning clearly.

(a) [10 points] What is the ALU's latency for an addition and for a multiplication, respectively?

Addition: 1 cycle for an addition (E1).

Multiplication: 3 cycles for a multiplication (E1, E2, E3).

(b) [10 points] Does this processor implement data forwarding? If so, between which pipeline stages?
Explain your reasoning.

The processor implements data forwarding from W to E1.

(c) [10 points] The number of cycles in the decode stage dynamically varies between instructions.
Explain why this might be the case. Hint: Register values are read from the register le in the
decode stage.

All listed instructions require two operands for the ALU, which require up to two cycles
to read from the register le. If one of the inputs is an immediate (e.g., instruction 2) or
is forwarded from an earlier instruction, the register le has to be queried for only one
input. Then, a shorter decode stage is sucient.

Final Exam Page 16 of 28

|Col1|Cycles|1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16|
|---|---|---|
|1 2 3 4 5 6|MUL R5, R6, R7 ADDI R4, R6, 5 MUL R4, R7, R8 ADD R5, R5, R6 ADD R6, R7, R5 ADD R7, R1, R4|F D1 D2 E1 E2 E3 M W F - D1 E1 - - M W F D1 D2 E1 E2 E3 M W F - D1 E1 - - M W F D1 - - - E1 M W F - - - D1 D2 E1 M W|


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

(d) [10 points] What is the minimum number of register le read ports and write ports that this
processor implements? Explain.

The register le has one read port and one write port.

Acording to the timeline in cycles 2 and 3, the decode stage operates in two cycles for
an instruction that has two register operands. Also, acording to cycle 4, the decode
stage takes one cycle for an instruction with one register operand. We conclude that the
decode stage needs one cycle to decode and read each register operand which means the
register le has one read port.

The register le has at least one dedicated write port since acording to cycle 12, the
decode stage and the write back stage are both using the register le, and we are sure
that both have been serviced by the register le within that cycle since the next cycle is
not a stall for any of them.

(e) [15 points] Can we reduce the execution time of this code by enabling more read or write ports
in the register le? Explain. If yes, what is the speedup compared to the baseline microprocessor
assuming the changes do not impact clock frequency? Show your work.

Yes. Adding a new read port to the register le will enable the register le to service
the decode unit in one cycle for any instruction with one or two register operands. The
speedup is 16/13. Here is the new timeline:

Cycles 1 2 3 4 5 6 7 8 9 10 11 12 13

1 MUL R5, R6, R7 F D E1 E2 E3 M W

2 ADDI R4, R6, 5 F D E1       -       - M W

3 MUL R4, R7, R8 F D E1 E2 E3 M W

4 ADD R5, R5, R6 F D       - E1       - M W

5 ADD R6, R7, R5 F       - D       -       - E1 M W

6 ADD R7, R1, R4 F       -       - D E1 M W

(f) [15 points] Is it possible to run this code faster by adding more data forwarding paths to the
original pipeline? If it is, explain how and calculate the speedup with respect to the original
pipeline assuming the changes do not impact clock frequency. Otherwise, explain why it is not
possible.

Yes, it is possible. Adding a forwarding path from M to E1 can improve the performance.
The speedup is 16/15. Here is a new timeline:

Cycles 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

1 MUL R5, R6, R7 F D1 D2 E1 E2 E3 M W

2 ADDI R4, R6, 5 F       - D1 E1       -       - M W

3 MUL R4, R7, R8 F D1 D2 E1 E2 E3 M W

4 ADD R5, R5, R6 F       - D1 E1       -       - M W

5 ADD R6, R7, R5 F D1       -       - E1 M W

6 ADD R7, R1, R4 F       -       - D1 D2 E1 M W

Final Exam Page 17 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 8 Tomasulo's Algorithm [[60 points]]

Consider an in-order fetch, out-of-order dispatch, and in-order retirement execution engine that employs
Tomasulo's algorithm. This engine has the following characteristics:


The engine has four main pipeline stages: Fetch (F), Decode (D), Execute (E), and Write-back
(W).


The engine can fetch one instruction per cycle, decode one instruction per cycle, and write back
the result of one instruction per cycle.


The engine has two execution units: 1) an adder to execute ADD instructions and 2) a multiplier
to execute MUL instructions.


The execution units are fully pipelined. The adder has two stages (E1-E2), and the multiplier has
four stages (E1-E2-E3-E4). Execution of each stage takes one cycle.


The adder has a two-entry reservation station, and the multiplier has a three-entry reservation
station.


An instruction always allocates the rst available entry of the reservation station (in top-to-bottom
order) of the corresponding execution unit.


Full data forwarding is available, i.e., during the last cycle of the E stage, the tags and data are
broadcast to the reservation station and the Register Alias Table (RAT). For example, an ADD
instruction updates the reservation station entries of the dependent instructions in the E2 stage.
So, the updated value can be read from the reservation station entry in the next cycle. Therefore,
a dependent instruction can potentially begin its execution in the next cycle (after E2).


The multiplier and adder have separate output data buses, which allow both the adder and the
multiplier to update the reservation station and the RAT in the same cycle.

 ID V Tag Value V Tag Value
An instruction continues to occupy a reservation station slot until it nishes the Write-back (W)

E 1 – 7 1 – 35

stage. The reservation station entry is deallocated after the Write-back (W) stage.


###### 8.1 Problem Denition


Z 1 – 82 0 – H

|ID|V|Tag|Value|V|Tag|Value|
|---|---|---|---|---|---|---|
|tio E ter|n s 1 th|lot u – e Wr|ntil it 7 ite-ba|n 1 ck (|ishe – W)|s the 35 stage|
|T|1|–|14|1|–|35|
|H|1|–|35|1|–|35|
|Z|1|–|82|0|–|H|


The processor is to fetch and execute ve instructions. Assume the reservation stations (RS) are all
initially empty, and the initial state of the register alias table (RAT) is given below in Figure (a).
Instructions are fetched, decoded, and executed as discussed in class. At some point during the execution×
of the ve instructions, a snapshot of the state of the RS and the RAT is taken. Figures (b) and (c)
show the state of the RS and the RAT at the snapshot time. A dash () indicates that a value has been
cleared. A question mark (?) indicates that a value is unknown to you.

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||ID|V|Tag||Value|V|Tag||Value|||
||||D|0|T||–|0|H||–|||
|I|D||V|T|ag||Value||V||Tag||Value|
|||||||||||||||
|- Z||K- 1|K-|0|-D||– -|0|- Z||– -|||
|||||?||||1||?||||
|||||||||||||||
||||ID|V|Tag||Value|V|Tag||Value|||
||||E|1|–||+ 7|1|–||35|||
|||||||||||||||
||||T|1|–||14|1|–||35|||
|I|D||V H|T 1|ag –||Value 35|1|V –||Tag 35||Value|
||X Y T|1 Z0 1|1||?||50||1||?|||
||||Z0|1|– X||8?2|0|– 1||?H|||
|||||?||||1||?||||

|Reg|Valid|Tag|Value|
|---|---|---|---|
|R0|1||256|
|R1|1||28|
|R2|1||1|
|R3|1||3|
|R4|1||30|
|R5|1||5|
|R6|1||23|
|R7|1||20|
|R8|1||61|
|R9|1||4|

|Reg|Valid|Tag|Value|
|---|---|---|---|
|R0|1|?|256|
|R1|1|?|28|
|R2|1|?|1|
|R3|1|?|50|
|R4|1|?|30|
|R5|0|X|?|
|R6|1|?|23|
|R7|0|Y|?|
|R8|0|Z|?|
|R9|0|T|?|


(a) Initial state of the RAT


(b) State of the RAT at the snapshot time


## ×

(c) State of the RS at the snapshot time

ID V Tag Value V Tag Value

D 0 T – 0 H –

K 0 D – 0 Z –

|ID|V|Tag V|alue|V|Tag|Value|
|---|---|---|---|---|---|---|
|D|0|T|–|0|H|–|
|K|0|D|–|0|Z|–|


## +

Final Exam Page 18 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 8.2 Questions

8.2.1 Dataow Graph [[40 points]]

Based on the information provided above, identify the instructions and provide the dataow graph
below for the instructions that have been fetched. Please appropriately connect the nodes using edges
and specify the direction of each edge. Label each edge with the destination architectural register and
the corresponding Tag.

##### R1 R2 R4 R6 R7

### + +

##### Z/R8 A/R3

### x x

##### T/R9 X/R5

### x

##### Y/R7

8.2.2 Program Instructions [[20 points]]

Fill in the blanks below with the ve-instruction sequence in program order. There can be more than
one correct ordering. Please provide only one correct ordering. When referring to registers, please use
their architectural names (R0 through R9). Place the register with the smaller architectural name on
the left source register box.
For example, ADD R8 ⇐ R1, R5.

ADD R3 _⇐_ R7, R4

MUL R5 _⇐_ R3, R2

MUL R7 _⇐_ R5, R7

ADD R8 _⇐_ R1, R2

MUL R9 _⇐_ R6, R3

Final Exam Page 19 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 9 GPUs and SIMD [[45 points]]

We dene the SIMD utilization of a program that runs on a GPU as the fraction of SIMD lanes that are
kept busy with active threads during the run of a program. As we saw in lecture and practice exercises,
the SIMD utilization of a program is computed across the complete run of the program.

The following code segment is run on a GPU. A warp in the GPU consists of 32 threads, and there are
32 SIMD lanes in the GPU. Each thread executes a single iteration of the shown loop. Assume that
the data values of the arrays A, B and C are already in vector registers so there are no loads and stores
in this program. Both B and C are arrays of integers and each integer in these arrays has an absolute
value of less than 10 (i.e., |B[i]| < 10 and |C[i]| < 10, for all i).

for (i = 0; i < 1024; i++) {
A[i] = B[i] * C[i]; // instruction 1
if (/* Condition */) { // instruction 2
// instruction 3
// instruction 4
.
.
.
// instruction k + 2
}
C[i] = C[i] - 1; // instruction k + 3
}

Please answer the following four questions.

(a) [5 points] How many warps does it take to execute this program? Show your work.

32 Warps.

Explanation:
Warps = (Number of threads) / (Number of threads per warp) Number of threads =
2[10] (i.e., one thread per loop iteration) Number of threads per warp = 32 = 2[5] (given)
Warps = 2[10]/2[5] = 2[5]

(b) [20 points] Assume that the condition for the if statement is (i % 16 == 0). What is the
number of instructions (k) in the body of the conditional block given a SIMD utilization of 32[11] [?]

Assume that there are no control ow instructions in the body of the if statement. Show your
work.

7 Instructions.

Explanation:
Two of the 32 threads go inside of the conditional block. This pattern is homogeneous
through all warps.

2×32(3+×k(3+)+30k)×3 = [11]32 _[→]_ _[k][ = 7][ instructions.]_

Final Exam Page 20 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

(c) [20 points] Assume that the condition for the if statement is (i % 16 == 0 && i < 512).
What is the number of instructions (k) in the body of the conditional block given a SIMD utilization
of [5]8 [? Assume that there are][ no][ control ow instructions in the body of the][ if][ statement. Show]

your work.

4 Instructions.

Explanation:
Two of the 32 threads only within the rst 16 warps go inside of the conditional
block. In the rest of the warps no thread goes inside of the conditional block.

16(3216(32×(3))+16(2×(3+k))+16(32×(k+3)+30×3)×3) = [5]8 _[→]_ _[k][ = 4][ instructions.]_

Final Exam Page 21 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 10 Branch Prediction [[70 points]]

A processor implements an in-order pipeline with multiple stages. Each stage completes in a single
cycle. The pipeline stalls after fetching a conditional branch instruction and resumes execution once the
condition of the branch is evaluated. There is no other case in which the pipeline stalls.

###### 10.1 Part I: Microbenchmarking [[30 points]]

You create a microbenchmark as follows to reverse-engineer the pipeline characteristics:

LOOP1:
SUB R1, R1, #1 // R1 = R1 - 1
BGT R1, LOOP1 // Branch to LOOP1 if R1 > 0

LOOP2:
B LOOP2 // Branch to LOOP2
// Repeats until program is killed

The microbenchmark takes one input value R1 and runs until it is killed (e.g., via an external interrupt).

You carefully run the microbenchmark using dierent input values (R1) as summarized in Table 2. You
terminate the microbenchmark using an external interrupt such that each run is guaranteed to execute
exactly 50 dynamic instructions (i.e., the instructions actually executed by the processor, in contrast to
static instructions, which is the number of instructions the microbenchmark has).

Initial R1 Value Number of Cycles Taken

2 71

4 83

8 107

16 155

Table 2: Microbenchmark results.

Using this information, you need to determine the following two system characteristics. Clearly show all
work to receive full points!

1. How many stages are in the pipeline?

2. For how many cycles does a conditional branch instruction cause a stall?

1. 10 pipeline stages
2. 6 cycles
Explanation: We have a system of equations in the variables:


_C is the total number of cycles taken_

_P is the total number of pipeline stages_

_I is the total number of dynamic instructions executed_

_B is the number of conditional branch instructions executed_

_D is the number of cycles stalled for each conditional branch_
The total number of cycles can be expressed as C = P + I − 1 + B ∗ _D._
We know that I = 50, and Table 2 gives us B and C, which we can use to solve the following
system of equations:


71 = P + 50 1 + 2 _D_
_−_ _∗_

83 = P + 50 1 + 4 _D_
_−_ _∗_
Solving this system, we obtain P = 10, D = 6

Final Exam Page 22 of 28

|Initial R1 Value|Number of Cycles Taken|
|---|---|
|2|71|
|4|83|
|8|107|
|16|155|


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 10.2 Part II: Performance Enhancement [[40 points]]

To improve performance, the designers add a mystery branch prediction mechanism to the processor.
All we know about this mystery branch predictior is that it does not stall the piepline at all if the
prediction is correct. They keep the rest of the design exactly the same as before. You re-run the same
microbenchmark with R1 = 4 for the same number of total dynamic instructions with the new design,
and you nd that the microbenchmark executes in 77 cycles.

Based on this given information, determine which of the following branch prediction mechanisms could
be the mystery branch predictor implemented in the new version of the processor. For each branch
prediction mechanism below, you should circle the conguration parameters that makes it match the
performance of the mystery branch predictor.

(a) [10 points] Static Branch Predictor

Could this be the mystery branch predictor: YES NO

If YES, for which conguration below is the answer YES?

(I) Static Prediction Direction

Always taken Always not taken

Explain:

YES, if the static prediction direction is always not taken.
Explanation: The execution time corresponds to 3 mispredictions and 1 correct prediction. The correct prediction occurs when the branch condition evaluates to FALSE and
execution falls through to the following instruction (i.e., NOT TAKEN).

(b) [10 points] Last Time Branch Predictor

Could this be the mystery branch predictor?

YES NO

If YES, for which conguration is the answer YES ? Pick an option for each conguration parameter.

(I) Initial Prediction Direction

Taken Not taken

(II) Local for each branch instruction (PC-based) or global (shared among all branches) history?

Local Global

Explain:

NO.
Explanation: The last-time predictor will make a correct prediction at least three times,
which means that it cannot be the mystery predictor.

Final Exam Page 23 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

(c) [10 points] Backward taken, Forward not taken (BTFN)

Could this be the mystery branch predictor?

YES NO

Explain:

NO.

Explanation: The BTFN predictor makes exactly one misprediction, which is the opposite of what the mystery predictor achieves.

(d) [10 points] Forward taken, Backward not taken (FTBN)

Could this be the mystery branch predictor?

YES NO

Explain:

YES.

Explanation: The FTBN predictor makes exactly one correct prediction, which is what
we observe from the microbenchmark.

Final Exam Page 24 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 11 BONUS: Data Prefetching [[50 points]]

You and your colleague are tasked with designing the prefetcher of a machine your company is designing.
The machine has a single processor attached to a main memory (DRAM) system.

You need to examine dierent prefetcher designs and analyze the trade-os involved. For all parts of
this question, you need to compute the coverage or overhead of the prefetcher in its steady state.

You run an application that has the following memory access pattern (note that these are cache block
addresses). Assume this memory access pattern repeats for a long time.

_A, A + 1, A + 9, A + 10, A + 18, A + 19, A + 27, A + 28, A + 36, A + 37, ..._

(a) [10 points] You rst design a stride prefetcher PrefX that observes the last three cache block
requests. If there is a constant stride S between the last three requests, PrefX issues a prefetch
to the next cache block using the stride S. In absence of a constant stride, PrefX refrains from
prefetching. What is the coverage of PrefX for the application? Show your work. Please recall,
prefetcher coverage is dened as:

_Total number of prefetch requests used by the program_

_Total number of main memory requests without the prefetcher_

0%

Explanation: Since the stride in the address pattern is changing between +1 and +8,
the stride prefetcher PrefX cannot learn any constant stride to issue prefetch requests.

(b) [10 points] You then design a next-N-block prefetcher PrefY . For every memory access to cacheline
address A, the PrefY prefetches addresses A + 1, A + 2, ..., A + N . What is the coverage of PrefY
if you set N = 2?

50%

Explanation: PrefY will prefetch A + 1 by seeing A, A + 9 by seeing A + 8, and so on.
Hence every alternate memory requests will be sucessfully prefetched.

Final Exam Page 25 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

(c) [10 points] A prefetcher also incurs bandwidth overhead to the system. We dene a prefetcher's
bandwidth overhead to the the system as:

_Total number of main memory requests with the prefetcher_

_Total number of main memory requests without the prefetcher_

Please note that, if multiple prefetch requests are generated for one memory address, only one
request goes to the DRAM.

What is the bandwidth overhead of PrefY when N = 2? Show your work.

3/2

Explanation:
For PrefY :


_A will prefetch addresses A + 1, A + 2_

_A + 1 will prefetch addresses A + 2, A + 3_
So, for every 2 unique cache block requests without the prefetcher, there are 3 unique
cache block requests with the prefetcher PrefY . Hence the bandwidth overhead is 2[3] [.]

(d) [10 points] What is the minimum value of N required to achieve a 100% prefetch coverage for
_PrefY ? Show your work. Remember that you should consider the prefetcher's coverage in its_
steady state.

8

Explanation: At N = 8, A + 1 can prefetch for A + 9, thus acheiving 100% coverage.

(e) [10 points] What is the bandwidth overhead of PrefY at the value of N you nd for part (d)?
Show your work.

9/2

Explanation:
For PrefY at N = 8:


_A will prefetch addresses A + 1, A + 2, A + 3, A + 4, A + 5, A + 6, A + 7, A + 8_

_A + 1 will prefetch addresses A + 2, A + 3, A + 4, A + 5, A + 6, A + 7, A + 8, A + 9_
So, for every 2 unique cache block requests without the prefetcher, there are 9 unique
cache block requests with the prefetcher PrefY . Hence the bandwidth overhead is 2[9] [.]

Final Exam Page 26 of 28


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

###### 12 BONUS: Cache Reverse Engineering [[70 points]]

You are trying to reverse-engineer the cache associativity in a newly-released system. You already know
that the cache has a FIFO replacement policy and 8 blocks with a block size of 4 B. Starting with an
empty cache, an application accesses ve byte addresses in the following order

2 _→_ 9 _→_ 16 _→_ 25 _→_ 33

Assume you can access three addresses after the above sequence and observe the cache hit rate across
these three accesses.

1. [30 points] Which three addresses should you access in order to identify the set-associativity of the
cache (1-, 2-, 4- or 8-way)? There may be multiple solutions; please give the lowest possible
addresses that can enable the identication of the set-associativity . Please explain every
step in detail to get full points.

0 → 8 → 16
Explanation. There are four possible set/way congurations, shown below. Each conguration shows the cache state after the ve initial accesses. Rows and columns represent
sets and ways, respectively, and the byte address accessed is shown for each occupied set:

(a) (8 sets, 1 way)

33

            
9

            
16

            
25

            
(b) (4 sets, 2 ways)

33 16

            -            
9 25

            -            
(c) (2 sets, 4 ways)

33 9 16 25

_−_ _−_ _−_ _−_

(d) (1 set, 8 ways)

2 9 16 25 33
_−_ _−_ _−_

At this point, all four cache associativities have 100% miss rate since they started cold.
In order to dierentiate the four cases with just three more accesses, we need to induce
dierent hit/miss counts in each of the four types of cache associativities. The only
way this is possible is if one cache type experiences three hits, another experiences three
misses, the third one has one hit and two misses, and the last one has two hits and one
miss.
Only two solutions exist to produce this case. In the two solutions, any address in each
of the address ranges below can be accessed to reverse-engineer the cache associativity.


(0-3)→(16-19)→(32-35)

(0-3)→(8-11)→(16-19)

Choosing the lowest possible addresses, the correct solution is 0 → 8 → 16

Final Exam Page 27 of 28

|33|16|
|---|---|
|-|-|
|9|25|
|-|-|

|33|9|16|25|
|---|---|---|---|
|−|−|−|−|

|2|9|16|25|33|−|−|−|
|---|---|---|---|---|---|---|---|


-----

Initials: Digital Design and Computer Architecture August 11th, 2022

2. [20 points] What is the associativity of the cache if the cache hit rate observed over the 3 extra
addresses accessed in Part (1) were:

Hit rate Associativity

0

1/3

2/3

1

Based on the solution to Part (1), these are the cache associativities corresponding to
dierent hit rates.

Hit rate Associativity

0 4-way, 2 sets

1/3 2-way, 4 sets

2/3 1-way, 8 sets

1 8-way, 1 set

3. [20 points] When you accessed the three addresses you determined in Part (1), you observed a
100% hit rate across these three accesses. Now, your friend asks you to access four more addresses
in the following order:

32 _→_ 0 _→_ 8 _→_ 28

Which of the above four addresses would result in a cache miss?

28.
The cache associativity which provides 100% cache hit for the three extra accesses in
Part (1) is 8-way and 1 set. The three addresses 32, 0 and 8 are already available in
the cache before the four new accesses requested by your friend. 28 will result in a miss
and will be added to the cache.

Final Exam Page 28 of 28

|Hit rate|Associativity|
|---|---|
|0||
|1/3||
|2/3||
|1||

|Hit rate|Associativity|
|---|---|
|0|4-way, 2 sets|
|1/3|2-way, 4 sets|
|2/3|1-way, 8 sets|
|1|8-way, 1 set|


-----

