Family Name: SOLUTIONS First Name: Student ID:

## Final Exam

# Digital Design and Computer Architecture (252-0028-00L)

 ETH Zürich, Spring 2023

### Prof. Onur Mutlu

Problem 1 (45 Points): Boolean Logic Circuits

Problem 2 (45 Points): Finite State Machines

Problem 3 (45 Points): ISA vs. Microarchitecture

Problem 4 (60 Points): Verilog

Problem 5 (45 Points): Memory Potpourri

Problem 6 (50 Points): Performance Evaluation

Problem 7 (70 Points): Pipelining

Problem 8 (80 Points): Vector Processing

Problem 9 (60 Points): VLIW

Problem 10 (50 Points): Caches

Problem 11 (BONUS: 50 Points): Systolic Arrays

Problem 12 (BONUS: 50 Points): Prefetching

Total (650 (550+100 bonus) Points):

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

Initials: Digital Design and Computer Architecture August 21st, 2023

This page intentionally left blank

Final Exam Page 1 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

## 1 Boolean Logic Circuits [[45 points]]

During your job interview, you are asked to design a combinational circuit with a four-bit input,
{A, B, C, D} (A is the most signicant bit and D is the least signicant bit), and two 1-bit outputs,
_Fib and G3. The value of each output is determined as follows:_


The output Fib is 1 only when the input 4-bit number is a Fibonacci number. You can calculate
Fibonacci numbers as follows, f (0) = 0, f (1) = 1, and f (n) = f (n − 1) + f (n − 2) for n ≥ 2.


The output G3 is 1 only when the input 4-bit number is greater than 3.


Otherwise, the corresponding output is zero.

Please answer the following three questions.

(a) [10 points] Fill in the missing entries in the truth table below for the combinational circuit you are
designing and express the output Fib in the sum of products representation.

Inputs Outputs

_A_ _B_ _C_ _D_ _Fib_ _G3_

0 0 0 0 1 0

0 0 0 1 1 0

0 0 1 0 1 0

0 0 1 1 1 0

0 1 0 0 0 1

0 1 0 1 1 1

0 1 1 0 0 1

0 1 1 1 0 1

1 0 0 0 1 1

1 0 0 1 0 1

1 0 1 0 0 1

1 0 1 1 0 1

1 1 0 0 0 1

1 1 0 1 1 1

1 1 1 0 0 1

1 1 1 1 0 1

_Fib = (A · B · C · D) + (A · B · C · D) + (A · B · C · D) + (A · B · C · D) + (A · B · C · D) +_
(A _B_ _C_ _D) + (A_ _B_ _C_ _D)_
_·_ _·_ _·_ _·_ _·_ _·_

Final Exam Page 2 of 27

|Inputs|Col2|Col3|Col4|Outputs|Col6|
|---|---|---|---|---|---|
|A|B|C|D|Fib|G3|
|0|0|0|0|1|0|
|0|0|0|1|1|0|
|0|0|1|0|1|0|
|0|0|1|1|1|0|
|0|1|0|0|0|1|
|0|1|0|1|1|1|
|0|1|1|0|0|1|
|0|1|1|1|0|1|
|1|0|0|0|1|1|
|1|0|0|1|0|1|
|1|0|1|0|0|1|
|1|0|1|1|0|1|
|1|1|0|0|0|1|
|1|1|0|1|1|1|
|1|1|1|0|0|1|
|1|1|1|1|0|1|


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

(b) [15 points] Simplify the Fib expression using Boolean minimization rules. Show your work stepby-step.

_Fib = (A · B · C · D) + (A · B · C · D) + (A · B · C · D) + (A · B · C · D) + (A · B · C · D) +_
(A _B_ _C_ _D) + (A_ _B_ _C_ _D)_
_·_ _·_ _·_ _·_ _·_ _·_

_Fib = ((A·B)·((C_ _·D)+(C_ _·D)+(C_ _·D)+(C_ _·D)))+(A·B·C_ _·D)+(A·B·C_ _·D)+(A·B·C_ _·D)_

_Fib = ((A · B) · (1)) + (A · B · C · D) + (A · B · C · D) + (A · B · C · D)_

_Fib = (A · B) + (A · B · C · D) + (A · B · C · D) + (A · B · C · D)_

_Fib = (A · B) + (C · ((A · B · D) + (A · B · D) + (A · B · D)))_

_Fib = (A · B) + (C · ((B · D) + (A · B · D)))_

_Fib = (A · B) + (B · C · D) + (A · B · C · D)_

_Fib = (A · B) + (A · B · C · D) + (B · C · D)_

_Fib = (A · B) + (B · C · D) + (B · C · D)_

(c) [20 points] Find the simplest representation of the G3 output by using only 2-input NAND gates.
Show your work step-by-step.

_G3 = (A · A) · (B · B)_
Explanation:

_G3 = (A·B_ _·C ·D)+(A·B_ _·C ·D)+(A·B_ _·C ·D)+(A·B_ _·C ·D)+(A·B_ _·C ·D)+(A·B_ _·C ·_
_D)+(A_ _B_ _C_ _D)+(A_ _B_ _C_ _D)+(A_ _B_ _C_ _D)+(A_ _B_ _C_ _D)+(A_ _B_ _C_ _D)+(A_ _B_ _C_ _D)_

_·_ _·_ _·_ _·_ _·_ _·_ _·_ _·_ _·_ _·_ _·_ _·_ _·_ _·_ _·_ _·_ _·_ _·_

_G3 = (A · B · ((C · D) + (C · D) + (C · D) + (C · D))) + (A · B · ((C · D) + (C · D) + (C ·_
_D) + (C_ _D))) + (A_ _B_ ((C _D) + (C_ _D) + (C_ _D) + (C_ _D)))_
_·_ _·_ _·_ _·_ _·_ _·_ _·_

_G3 = (A · B · (1)) + (A · B · (1)) + (A · B · (1))_

_G3 = (A · B) + (A · B) + (A · B)_

_G3 = A + B_

_G3 = A + B_

_G3 = A · B_

_G3 = (A · A) · (B · B)_

Final Exam Page 3 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

## 2 Finite State Machines [[45 points]]

### 2.1 Simplifying an FSM [[20 points]]

You are given the nite state machine of a one input / one output digital circuit design. Answer the
following questions for the given state diagram.


0/1


1/0


1/0 1/0

Reset

C D

0/1

Is it possible to simplify this state diagram and reduce the number of states? If so, simplify it to the
minimum number of states. Explain each step of your simplication. Draw the simplied state diagram.
If not, explain why it is not possible to simplify the state diagram.

Yes, it is possible. Below is the state transition table of the given state machine:

Current State Input Next State Output

A 0 A 1
A 1 B 0

B 0 A 1
B 1 B 0

C 0 D 1
C 1 A 0

D 0 A 1
D 1 B 0

We can see that the states A, B, and D are identical. For all of these states,


an input of 0 leads to the next state A and the output 1

an input of 1 leads to the next state B and the output 0
Therefore, we can merge states A, B, and D. Let's use the name X:

Current State Input Next State Output

X 0 X 1
X 1 X 0

C 0 X 1
C 1 X 0

We can further simplify this state machine as both states C and X are identical in terms of
their next state and output. As a result, this state machine has only one state and the output
is always the inverse of the input.

1/0
0/1

S

Final Exam Page 4 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

### 2.2 Designing an FSM [[25 points]]

Design a Moore nite state machine (FSM), where each output is solely determined by the current state
of the machine and not directly inuenced by the inputs. The state machine should have one input and
one output. This FSM's goal is to detect a stable transition in the input signal from repeated logic-0 to
repeated logic-1. The output should be logic-1 only when the input sequence of "0-0-1-1" is observed.
The output should be zero in all other cases.

When the circuit is reset, your state machine should assume that the input signal has been high (logic-1)
for a long time. Draw the state diagram and explain why it works. Your state machine should use as
few states as possible and each state should have a precise denition and output.

We need to keep track of the bit values in the last four bits. This requires 16 states. However,
many of these states behave the same. We can reduce the number of states down to ve.


Since this is a Moore machine, the output should be independent from the input. Therefore, there should be a state for the posedge where the output is "1". All other states
will have the output of "0". The FSM goes to the posedge state only when the last four
bits are 0-0-1-1. We call this state S0011.


The FSM should reach to the posedge state from another state where the last three input
bits are 0-0-1. We call this state SX001.


The FSM should reach to the 0-0-1 state from a state where the last two input bits are
0-0. Note that it does not matter what the input bits are, earlier than the last two zeros.
We call this state SXX01.


The FSM should not stay in state S0011 for more than one clock cycle as when the new
input comes, the last four bits will not be 0-0-1-1 anymore. If the input is 1, the next
state should be SXXX1: the last bit is zero but it is not a posedge and the earlier bits
are not important. If the input is 0, the next state should be SXX10: the last two bits
are 1-0 and the earlier bits are not important.


Intuitively, if the state is SXXX1, the FSM should remain at this state if the input is 1
and go to SXX10 if the input is 0.


If the state is SXX10, the FSM should not remain at this state regardless of the input.
If the input is 0, the next state is SXX00. If the input is 1, the next state is SXXX1.
Therefore, it is possible to design this state machine with ve states. The state diagram is
shown below.

### 1 0 0 0

SXXX1 SXX10 SXX00

### 1

0 0 0

### reset

 0 1 1 0

S0011 SX001

1 0

### 1

Final Exam Page 5 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

## 3 ISA vs. Microarchitecture [[45 points]]

Circle whether each of the following is an aspect of the ISA or the microarchitecture.

Note: we will subtract 2 points for each incorrect answer and award 0 points for each unanswered
question.

1. [3 points] Width of the immediate value in an ADD instruction.

1. ISA 2. Microarchitecture

2. [3 points] The algorithm used by the ALU to perform multiplication.

1. ISA 2. Microarchitecture

3. [3 points] Number of bits required for indexing the source register of a store instruction.

1. ISA 2. Microarchitecture

4. [3 points] Number of entries in the L3 cache.

1. ISA 2. Microarchitecture

5. [3 points] The data cache organization (e.g., direct-mapped, set-associative).

1. ISA 2. Microarchitecture

6. [3 points] Support for conveying prefetching hints to the hardware via the compiler.

1. ISA 2. Microarchitecture

7. [3 points] Available data types (e.g., integer) for arithmetic and logic operations.

1. ISA 2. Microarchitecture

8. [3 points] Cache coherence protocol in multi-core processors.

1. ISA 2. Microarchitecture

9. [3 points] Width of the data bus between the processor and main memory.

1. ISA 2. Microarchitecture

10. [3 points] The memory controller's memory request scheduling algorithm.

1. ISA 2. Microarchitecture

11. [3 points] Instruction encoding for control ow and branch instructions.

1. ISA 2. Microarchitecture

12. [3 points] The design of the register renaming logic.

1. ISA 2. Microarchitecture

13. [3 points] Number of instructions decoded per cycle in a superscalar processor.

1. ISA 2. Microarchitecture

14. [3 points] L2 cache miss latency.

1. ISA 2. Microarchitecture

15. [3 points] Width of the program counter.

1. ISA 2. Microarchitecture

Final Exam Page 6 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

## 4 Verilog [[60 points]]

### 4.1 What Does This Code Do? [[30 points]]

Analyze the following Verilog module and answer the question.

1 **module module_x (input wire clk, input wire rst,**

2 **input wire [7:0] in, output wire [7:0] out);**

3

4 **reg [7:0] var1, var2, var3, var4;**

5

6 **assign out = (var4 == in) ? var3 : var4;**

7

8 **always @(posedge clk) begin**

9 **if (rst) begin**

10 var1 <= 8’b0; var2 <= 8’b1;

11 var3 <= 8’b0; var4 <= 8’b0;

12 **end else begin**

13 var1 <= var2; var2 <= var1 + var2;

14 var3 <= var1 + var2;

15 var4 <= var4 + 8’b1;

16 **end**

17 **end**

18 **endmodule**

Assume that the input in always has the following value:
in = 8’h09

What unsigned decimal values does the out signal get in the following waveform diagram? Fill in the
gray boxes with an out value for each clk cycle. Briey explain your answer.

_posedge 0 posedge 1 …_

0 1 2 3 4 5 6 7 8 55

## …

**_fill in all 10 empty boxes_**

Brief explanation (to help us award you partial credit):

Explanation.
The module outputs the in[th] number in the Fibonacci sequence after in clock cycles. Until
then, it outputs the number of clock cycles that have passed since reset.
For the given value of in (8'h09), the values for out are from leftmost yellow box to the
rightmost yellow box:
0, 1, 2, 3, 4, 5, 6, 7, 8, 55

Final Exam Page 7 of 27


0 1 2 3 4 5 6 7 8 55


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

### 4.2 Is ChatGPT not Right? [[30 points]]

You gave ChatGPT the following prompt to help with your lab report: A Verilog module that simulates
a character's movement on a 2D-plane. The module takes four inputs for four directions (direction
inputs) the character can move to. The module outputs x and y coordinates. The character stays in the
same coordinate if none of the direction inputs are set. Initial coordinates (set on reset) are 0, 0. Stride
determines how many units the character moves in one step.

1 **module movement (**

2 **input clk,** **input rst,**

3 **input up,** **input down,**

4 **input left,** **input right,**

5 1 stride,

6 **output [7:0] x_coord,**

7 **output [7:0] y_coord**

8 );

9 2 x_internal, y_internal; // 8-bit signals

10 **wire [2:0] move_amount =** 3 ; // if stride is not zero, move by stride amount, else move by 1

11 **always @(posedge clk) begin**

12 **if (rst) begin**

13 x_internal <= 0; y_internal <= 0;

14 **end else begin**

15 **if (up) y_internal <= y_internal + move_amount;**

16 **else if (down) y_internal <= y_internal - move_amount;**

17 **else if (left) x_internal <= x_internal - move_amount;**

18 x_internal <= x_internal + move_amount;

19 **end**

20 **end**

21 4 x_coord = x_internal; // output coordinate

22 4 y_coord = y_internal; // output coordinate

23 **endmodule**

Provide your choice for each blank 1, 2, and 4 below. Circle only one of A, B, C, D. Provide a

one-line expression for 3 (Hint: Use the ternary operator (?) to implement a MUX).

1 : A. output B. output reg C. input wire [2:0] D. input reg

2 : A. wire [7:0] B. [7:0] wire C. wire [8:0] D. reg [7:0]

3 : stride != 3’b0 ? stride : 3’b1;

4 : A. B. assign C. == D. let

Final Exam Page 8 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

Explanation.

1 : Signal stride is used as an input to the module, so it should be declared as an input.
Among options that describe input signals (C and D), input reg is not valid Verilog syntax.

2 : The correct way to describe signals that we can assign values to in an always block is
reg [7:0].

3 : We describe a mux using the ternary operator as such: stride != 3’b0 ? stride
: 3’b1;. If stride is zero, the left-hand side of the ternary operator (i.e., stride) is the
output of the mux and otherwise the right-hand side (i.e., 3’b1) is the output of the mux.

4 : The correct syntax for assigning a value to a signal is assign x_coord =
x_internal;. Other options are not valid Verilog syntax.

Did ChatGPT inject any errors in this code? Write down line number(s) and a short explanation (to
help us award you partial credit).

Explanation. Line 18 introduces a logical error, causing x_internal to always be incremented by move_amount regardless of the direction of movement.

Final Exam Page 9 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

## 5 Memory Potpourri [[45 points]]

Read the following statements about memory organization & technology. Circle True if the statement
is true and False otherwise. Note: we will subtract 2 points for each incorrect answer and award 0
points for each unanswered question.

1. [[3 points] ]A main memory access typically has larger latency than a register le access.
1. True 2. False

2. [3 points] SRAM is commonly used as main memory in modern computers.
1. True 2. False

3. [3 points] A DRAM cell requires larger power to store data compared to an SRAM cell.
1. True 2. False

4. [3 points] Reads are faster than writes in DRAM.

1. True 2. False

5. [3 points] Reads are faster than writes in phase change memory.
1. True 2. False

6. [3 points] A bitline in a DRAM array connects all DRAM cells in a DRAM row to the row decoder
circuitry.
1. True 2. False

7. [3 points] Using virtual memory reduces the memory access latency.
1. True 2. False

8. [3 points] Phase Change Memory (PCM) is non-volatile.
1. True 2. False

9. [3 points] If a hypothetical system is not constrained by chip area, memory cost ($), and energy
consumption, PCM would be the best memory technology to use in that system.
1. True 2. False

10. [3 points] A program with a streaming memory access pattern leads to very high temporal locality
in the last level data cache.
1. True 2. False

11. [3 points] In DRAM, accesses to dierent rows in one bank can be serviced faster compared to
accesses to dierent rows in dierent banks.
1. True 2. False

12. [3 points] TLB is a specialized instruction cache that caches instructions based on branch prediction
results.
1. True 2. False

13. [3 points] Virtual memory simplies software design.
1. True 2. False

14. [3 points] A page fault happens when the TLB does not contain the entry needed by an instruction.

1. True 2. False

15. [3 points] A fully-associative L1 TLB that only stores 4KB virtual-to-physical mappings and has
1024 entries can cover up to 4MB of memory.

1. True 2. False

Final Exam Page 10 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

## 6 Performance Evaluation [[50 points]]

A multi-cycle processor P 1 executes load instructions in 6 cycles, store instructions in 6 cycles, arithmetic instructions in 2 cycles, and branch instructions in 2 cycles. Consider an application A where
40% of all instructions are load instructions, 20% of all instructions are store instructions, 30% of all
instructions are arithmetic instructions, and 10% of all instructions are branch instructions.

(a) [5 points] What is the CPI (cycles per instruction) of application A when executing on processor
_P_ 1? Show your work.

_CPI = 0.4_ 6 + 0.2 6 + 0.3 2 + 0.1 2
_×_ _×_ _×_ _×_
_CPI = 4.4_

(b) [5 points] A new design of the processor doubles the clock frequency of P 1. However, the latencies of
all instructions increase by 4 cycles. We call this new processor P 2. The compiler used to generate
instructions for P 2 is the same as for P 1. Thus, it produces the same number of instructions
for program A. What is the CPI of application A when executing on processor P 2? Show your
work.

_CPI = 0.4_ 10 + 0.2 10 + 0.3 6 + 0.1 6
_×_ _×_ _×_ _×_
_CPI = 8.4_

(c) [20 points] Which processor is faster (P 1 or P 2)? By how much (i.e., what is the speedup)? Show
your work.

_P_ 2 is 1.05× faster than P 1.

Explanation.
_Execution_Time_P_ 1 = instructions × CPIP 1 × clock_time

_clockExecution_time_ =Timeclock_Pfrequency2 =1_ _instructions × CPIP 2 ×_ _[clock][_]2_ _[time]_

_

Assuming that _Execution_Time_P_ 2 _<_ _Execution_Time_P_ 1 =⇒
_Execution_ _T ime_ _P 1_
_ _
_Execution_ _T ime_ _P 2_ _[>][ 1][. Thus:]_
_ _

= _instructions×CP IP 1×clock_time_
_⇒_ _instructions×CP IP 2×_ _[clock][_]2_ _[time]_

= 4.4×clock_time
_⇒_ 8.4× _[clock][_]2_ _[time]_

=⇒ 44..42
= 1.05
_⇒_

Final Exam Page 11 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

(d) [20 points] You want to improve the original P 1 design by including one new optimization without

changing the clock frequency. You can choose only one of the following options:

(1) ALU: An optimized ALU, which halves the latency of both arithmetic and branch instructions.

(2) LSU: An asymmetric load-store unit, which halves the latency of load operations but doubles
the latency of store operations.

Which optimization do you add to P 1 for application A? Show your work and justify your choice.

The ALU optimization.

Explanation.
Application A executes 40% load, 20% store, 30% arithmetic, and 10% branch instructions.
By Amdahl's Law, we have:

_SpeedupALU =_ (1−0.3−0.11)+ [0][.][3+0]2 _[.][1]_ = 1.25

_SpeedupLSU =_ (1−0.4−0.2)+1 [0]2[.][4] [+0][.][2][×][2][ = 1][.][0]

The ALU optimization provides 1.25× speedup, while the LSU provides no speedup at all.

Alternative Solution.
With the ALU, the new CPI of processor P 1 will be:
_CPIALU = 0.4 × 6 + 0.2 × 6 + 0.3 ×_ [2]2 [+ 0][.][1][ ×][ 2]2

_CPIALU = 4.0_

With the LSU, the new CPI of processor P 1 will be:
_CPILSU = 0.4 ×_ [6]2 [+ 0][.][2][ ×][ (6][ ×][ 2) + 0][.][3][ ×][ 2 + 0][.][1][ ×][ 2]

_CPILSU = 4.4_

Since CPIALU _< CPILSU_, integrating the ALU will improve the overall cyclesper-instruction.

Final Exam Page 12 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

## 7 Pipelining [[70 points]]

Code Listing 1 contains a piece of assembly code. Table 1 presents the execution timeline of this code.

1 MOVI R1, X _# R1 <- X_

2 MOVI R2, Y _# R2 <- Y_

3 L1:

4 MUL R4, R1, R1 _# R4 <- R1 × R1_

5 MUL R1, R1, R2 _# R1 <- R1 × R2_

6 ADD R4, R5, R6 _# R4 <- R5 + R6_

7 ADD R5, R2, R4 _# R5 <- R2 + R4_

8 SUBI R3, R1, 2048 _# R3 <- R1 - 2048, set condition flags_

9 JNZ L1 _# Jump to L1 if zero flag is NOT set_

10 MUL R1, R1, R2 _# R1 <- R1 × R2_

Code Listing 1: Assembly Program

Cycles

Instructions 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

1 MOVI R1, X F D E1 E2 E3 M W

2 MOVI R2, Y F D E1 E2 E3 M W

3 MUL R4, R1, R1 F D   - E1 E2 E3 M W

4 MUL R1, R1, R2 F   - D E1 E2 E3 M W

5 ADD R4, R5, R6 F D E1 E2 E3 M W

6 ADD R5, R2, R4 F D   -   - E1 E2 E3 M W

7 SUBI R3, R1, 2048 F   -   - D E1 E2 E3 M W

8 JNZ L1 F D   -   - E1 ...

9 ... ...

Table 1: Execution timeline (F:Fetch, D:Decode, E:Execute, M:Memory, W:WriteBack)

Use this information to reverse engineer the architecture of this microprocessor to answer the following
questions. Answer the questions as precisely as possible. If the provided information is not sucient to
answer a question, answer Unknown and explain your reasoning clearly.

(a) [15 points] List the data forwarding paths between pipeline stages.

The result of E3 stage is forwarded to E1 stage (e.g., R1's value at clock cycle 6 and R4's
value at clock cycle 11). The result of M stage is forwarded to E1 stage (e.g., R1's value
at clock cycle 7.)
The result of E3 stage is forwarded to the condition registers (e.g., SUBI and JNZ at
clock cycle 15).
There is no other information for any other data forwarding. Therefore, other data
forwardings are unknown.

Final Exam Page 13 of 27

|Col1|Col2|Code Listing 1: Assembly Program|
|---|---|---|
||Instructions|Cycles 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16|
|1|MOVI R1, X|F D E1 E2 E3 M W|
|2|MOVI R2, Y|F D E1 E2 E3 M W|
|3|MUL R4, R1, R1|F D - E1 E2 E3 M W|
|4|MUL R1, R1, R2|F - D E1 E2 E3 M W|
|5|ADD R4, R5, R6|F D E1 E2 E3 M W|
|6|ADD R5, R2, R4|F D - - E1 E2 E3 M W|
|7|SUBI R3, R1, 2048|F - - D E1 E2 E3 M W|
|8|JNZ L1|F D - - E1 ...|
|9|...|...|


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

(b) [10 points] Does this machine use hardware interlocking or software interlocking? Explain.

Hardware interlocking. It detects data dependencies and stalls the pipeline accordingly
without needing any software-induced NOPs.

For the rest of this question, assume the following:

_• X = 4, Y = 2 in Code Listing 1._

_• Branch predictor always predicts correctly._

_• The machine uses hardware interlocking._

At a given clock cycle T,

_• the value stored in R1 is 1024._

_• the processor fetches the dynamic instruction N which is MUL R4, R1, R1_

(c) [15 points] Calculate the value of T (the clock cycle of the given snapshot). Show your work.

T = 82.

Explanation.
The instruction MUL R4, R1, R1 is fetched for the rst time at the clock cycle 3. After
the rst iteration of the loop, the instruction is fetched for the second time at the clock
cycle 12.

The instruction JNZ L1 stalls at the Decode stage and delays MUL R4, R1, R1. Due
to this delay, there are 10 cycles in between the Nth and (N+1)th times the instruction
is fetched, after the rst iteration of the loop.

If R1 = 1024, this instruction is fetched and executed 8 times so far.

Since in cycle T the rst instruction in the loop (MUL R4, R1, R1) is being fetched,
no cycles of the 9th iteration have executed so far.

Then, T = 12 + 7 × 10 = 82

Final Exam Page 14 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

(d) [15 points] Calculate the value of N (the total number of dynamic instructions fetched by the clock
cycle T ). Show your work.

N = 51.

Explanation.
Loop iterates for 8 times before the processor reaches to clock cycle T .

There are two instructions before the loop starts.

Then, N = 2 + 8 × 6 + 1 = 51 (assuming that the instruction indices start from 1).

(e) [15 points] Calculate the total execution time of the assembly code in Code Listing 1 until the
completion in terms of the number of clock cycles. Show your work.

100 cycles.

Explanation.
Until the end of the second iteration, the loop takes 19 cycles as shown above.
The steady-state throughput of an iteration after the rst iteration is 6 instructions in
10 cycles.

Loop will iterate until R1 becomes 2048, which means 9 iterations in total.

There is only one instruction after the loop, which takes 1 cycle to complete.

Then, T = 19 + 8 × 10 + 1 = 100

Final Exam Page 15 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

## 8 Vector Processing [[80 points]]

Assume a vector processor that implements the following ISA:

Opcode Operands Latency (cycles) Description

SET _Vst, #n_ 1 _Vst ←_ n (Vst = Vector Stride Register)

SET _Vln, #n_ 1 _Vln ←_ n (Vln = Vector Length Register)

LDM _Vi_ 1 _VMSK ←_ _LSB(Vi) (VMSK = Vector Mask Register)_

VLD _Vi, #A_ 50 row hit, 100 row miss, pipelined _Vi ←_ _Mem[Address]_

VST _Vi, #A_ 50 row hit, 100 row miss, pipelined _Mem[Address] ←_ _Vi_

VMUL _Vi, Vj, Vk_ 10, pipelined _Vi ←_ _Vj ∗_ _Vk_

VADD _Vi, Vj, Vk_ 5, pipelined _Vi_ _Vj + Vk_
_←_

VSHFR _Vi, Vj_ 10, pipelined _Vi_ _Vj >> 1_
_←_

VNOT _Vi_ 4, pipelined _Vi ←_ _BitwiseNOT_ (Vi)

VCMPZ _Vi, Vj_ 4, pipelined if(Vj == 0) Vi ← 0xFFFF; else Vi ← 0x0000

Assume the following:


The processor has an in-order pipeline and issues one instruction per cycle.


There are 8 vector registers (V0,V1,V2,V3,V4,V5,V6,V7), and the size of a vector element is 4 bytes.


_Vst and Vln are 10-bit registers._


The processor does not support chaining between vector functional units.


LDM moves the least-signicant bit (LSB) of each vector element in a vector register Vi into the
corresponding position in VMSK. This instruction is executed in one single cycle.


The main memory is composed of N banks, and each bank has a row buer of size 64 bits.


All rows in main memory are initially closed (i.e., all banks are precharged).


The memory is byte addressable, and the address space is represented using 32 bits.


Vector elements are stored in memory in a 4-byte-aligned manner. The rst element of a vector
always starts at the beginning of a memory row.


Vector elements stored in consecutive memory addresses are interleaved between the memory banks.
E.g., if a vector element at address A maps to bank B, a vector element at A + 4 maps to bank
(B + 1)%N, where % is the modulo operator and N is the number of banks. N is not necessarily
a power of two.


The latency of accessing memory is 100 cycles when the memory request misses in the row buer,
and 50 cycles when the memory request hits in the row buer.


Each memory bank has a single read and a single write port so that a load and a store operation
can be performed simultaneously.


There is one functional unit for executing VLD instructions and a separate functional unit for
executing VST instructions. This means the load and store operations for dierent vectors cannot
be overlapped.


The operations on a vector do not aect the vector elements corresponding to the locations in the
Vector Mask Register (VMSK) that are set to 0.

Final Exam Page 16 of 27

|Opcode|Operands|Latency (cycles)|Description|
|---|---|---|---|
|SET|V , #n st|1|V st ← n (V st = Vector Stride Register)|
|SET|V , #n ln|1|V ln ← n (V ln = Vector Length Register)|
|LDM|V i|1|V ←LSB(V i) (V = Vector Mask Register) MSK MSK|
|VLD|V , #A i|50 row hit, 100 row miss, pipelined|V Mem[Address] i ←|
|VST|V , #A i|50 row hit, 100 row miss, pipelined|Mem[Address] V ← i|
|VMUL|V , V , V i j k|10, pipelined|V V V i ← j ∗ k|
|VADD|V , V , V i j k|5, pipelined|V ←V + V i j k|
|VSHFR|V , V i j|10, pipelined|V ←V >> 1 i j|
|VNOT|V i|4, pipelined|V BitwiseNOT(V ) i ← i|
|VCMPZ|V , V i j|4, pipelined|if(V j == 0) V i ← 0xFFFF; else V i ← 0x0000|


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

(a) [20 points] What should the minimum number of banks (N ) be to avoid stalls while executing a
VLD or VST instruction? Calculate the minimum number of banks for every stride from 1 to 10.
Explain.

101 banks for even strides, 100 banks for odd strides
Explanation.
To calculate the minimum value, we have to assume the worst case, which is when all
memory accesses are row buer misses (latency = 100). To avoid stalls, we need to
ensure that consecutive vector elements access 100 dierent banks.

We illustrate the solution for even strides (2 and 4) and odd strides (1 and 3).

101 banks are enough to avoid stalls with even numbers. For example, with a vector
stride of 2, consecutive elements of a vector will map to banks 0, 2, 4 ... 96, 98, 100, 1, 3
... 97, 99. With a vector stride of 4, consecutive elements of a vector will map to banks
0, 4, 8 ... 96, 100, 3, 7 ... 95, 99, 2, etc.

100 banks are enough to avoid stalls with odd numbers. For example, with a vector
stride of 1, consecutive elements of a vector will map to banks 0, 1, 2, 3 ... 98, 99. With
a vector of stride 3, consecutive elements of a vector will map to banks 0, 3, 6 ... 96, 99,
2, 5 ... 95, 98

So, the minimum number of banks is 100 for odd strides, and 101 for even strides.

Final Exam Page 17 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

(b) [30 points] Translate the following loop into assembly code that can be executed in the least possible

number of cycles in the previously described vector machine:

for i= 0 to 45:
if(a[i] == 0):
c[i] = b[i]
else:
c[i] = a[i] * b[i] + a[i]/2

Assume:

_• The same machine as in part (a)._

_• In the for loop, 45 is inclusive, i.e., [0, 45]_

_• The size of the elements of vectors a, b, and c is 4 bytes_

_• Vectors a, b, and c do not share parts of the same DRAM row_

SET Vst, 1 # Load Vector Stride Register
SET Vln, 46 # Load Vector Length Register
VLD V1, a # Read from array a
VLD V2, b # Read from array b
VCMPZ V3, V1 # Compare V1 to 0
LDM V3 # Load Vector Mask Register
VST c, V2 # Write to array c
VNOT V3 # BitwiseNOT
LDM V3 # Load Vector Mask Register
VSHFR V4, V1 # Shift to divide
VMUL V5, V1, V2 # Multiply
VADD V6, V5, V4 # Add
VST c, V6 # Write to array c

Final Exam Page 18 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

(c) [30 points] What is the number of cycles the previous code takes to execute in the vector processor
described in this question? Assume:

_• Vectors a and b are in dierent rows_

_• A machine that has a memory with 8 banks._

_• The rest of the machine is the same as in part (a)._

1822 cycles
Explanation.

The memory accesses look like:
bank0 --MISS-|--HIT--|--MISS--|--HIT--|--MISS--|--HIT--|
bank1 --MISS--|--HIT--|--MISS--|--HIT--|--MISS--|--HIT--|
bank2 --MISS--|--HIT--|--MISS--|--HIT--|--MISS--|--HIT--|
bank3 --MISS--|--HIT--|--MISS--|--HIT--|--MISS--|--HIT--|
bank4 --MISS--|--HIT--|--MISS--|--HIT--|--MISS--|--HIT--|
bank5 --MISS--|--HIT--|--MISS--|--HIT--|--MISS--|--HIT--|
bank6 --MISS--|--HIT--|--MISS--|--HIT--|--MISS--|
bank7 --MISS--|--HIT--|--MISS--|--HIT--|--MISS--|

Therefore, the latency of the load corresponds to the latency of the bank with the larger
latency. In this case, bank 5 (300+150+5 = 455 cycles). The latency of a store is also
455 cycles.

The general picture is:

SET: |-S-|
SET: |-S-|
VLD: |-----VLD-----|
VLD: |-----VLD-----|
VCMPZ: |VCMPZ|
LDM: |L|
VST: |-----VST-----|
VNOT: |VNOT|
LDM: |L|
VSHFR: |VSHFR|
VMUL: |VMUL|
VADD: |VADD|
VST: |-----VST-----|

S = 1
VLD_cycles = VST_cycles = 455
VMUL_cycles = 10 + 45 = 55
VCMPZ_cycles = 4 + 45 = 49
VNOT_cycles = 4 + 45 = 49
L = 1
VSHFR = 10 + 45 = 55
VADD = 5 + 45 = 50

Considering how the latency of some instructions is hidden by the other instructions,
the total cycles can be calculated as:
_total_cycles = S + S + V LD_cycles + V LD_cycles + V ST_ _cycles + V ST _cycles =
1822 cycles

Final Exam Page 19 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

## 9 VLIW [[60 points]]

You are the human compiler for a VLIW processor whose specications are as follows:


There are a total of 7 functional units: 3 load units, 1 store unit, 1 addition unit, 1 multiplication
unit, and 1 branch unit.


The VLIW processor can only execute assembly operations listed in Table 1. The table shows the
instructions that each functional unit can execute and each instructon's semantics. Note that the
load_inc/store_inc instructions automatically increment the address source register rsrc2 by
1, after data is loaded/stored.


All assembly operations have a 1-cycle latency (including load, load_inc, store, and store_inc).


This machine has 32 registers (r0, r1, ..., r31).


The registers are read at the rising edge and written at the falling edge of the clock.


The memory is word-addressable (1 word = 4 bytes).


The VLIW processor operates at 1 GHz.

Functional

Operation (in assembly notation) Semantics

Unit Type

load rdst, [rsrc1, rsrc2, #offset] rdst := MEM[rsrc1 + rsrc2 + #oset]

load rdst := MEM[rsrc1 + rsrc2 + #oset]

load_inc rdst, [rsrc1, rsrc2, #offset]

rsrc2 := rsrc2 + 1

store [rsrc1, rsrc2, #offset], rsrc3 MEM[rsrc1 + rsrc2 + #oset] := rsrc3

store MEM[rsrc1 + rsrc2 + #oset] := rsrc3

store_inc [rsrc1, rsrc2, #offset], rsrc3

rsrc2 := rsrc2 + 1

addition add rdst, rsrc1, rsrc2 rdst := rsrc1 + rsrc2

multiplication mult rdst, rsrc1, rsrc2 rdst := rsrc1 × rsrc2

branch bne rsrc1, #offset, TARGET branch to TARGET if rsrc1 is not equal to #oset

(any of the above) NOP Functional unit is idle for one cycle

Table 1: Assembly operations of the target VLIW processor. #offset indicates an immediate value.

Figure 1 shows the C code and its equivalent assembly code for the application that we will execute in
this VLIW processor. Assume that N is an even positive integer throughout this question.

In the assembly code, registers r29, r30, and r31 hold the base addresses of the C-code arrays A, B,
and C, respectively. Register r0 is initialized with 0 and register r1 is initialized with 1.

C code Assembly code

|Functional Unit Type|Operation (in assembly notation)|Semantics|
|---|---|---|
|load|load r, [r, r, #offset] dst src1 src2|rdst := MEM[rsrc1 + rsrc2 + #oset]|
||load_inc r, [r, r, #offset] dst src1 src2|rdst := MEM[rsrc1 + rsrc2 + #oset] rsrc2 := rsrc2 + 1|
|store|store [r, r, #offset], r src1 src2 src3|MEM[rsrc1 + rsrc2 + #oset] := rsrc3|
||store_inc [r, r, #offset], r src1 src2 src3|MEM[rsrc1 + rsrc2 + #oset] := rsrc3 rsrc2 := rsrc2 + 1|
|addition|add r, r, r dst src1 src2|rdst := rsrc1 + rsrc2|
|multiplication|mult r, r, r dst src1 src2|rdst := rsrc1 × rsrc2|
|branch|bne r, #offset, TARGET src1|branch to TARGET if rsrc1 is not equal to #oset|
|(any of the above)|NOP|Functional unit is idle for one cycle|


// An i n t e g e r i s 4 bytes long
int A[N+1];
int B[N+1];
int C[N+1];
. . . // code to i n i t i a l i z e A and B
for ( int i = 1; i <= N; i++)
C[ i ] = C[ i =1] * A[ i ] + B[ i ] ;


LOOP:
( v1 ) load_inc r2, [ r31, r0, #0] // r2 := [ r31 + r0 + #0]; r0 := r0 + 1
( v2 ) load r3, [ r29, r1, #0] // r3 := [ r29 + r1 + #0]
( v3 ) load r4, [ r30, r1, #0] // r4 := [ r30 + r1 + #0]
( v4 ) mult r5, r2, r3 // r5 := r2 * r3
( v5 ) add r6, r5, r4 // r6 := r5 + r4
( v6 ) store_inc [ r31, r1, #0], r6 // [ r31 + r1 + #0] := r6 ; r1 := r1 + 1
( v7 ) bne r1, #N, LOOP // branch to LOOP i f r1 not equal to #N


Figure 1: C and assembly codes. (v1) .. (v7) are instruction labels.

Final Exam Page 20 of 27


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

(a) [30 points] Your goal in this question is to statically schedule the instructions in Figure 1 to the
VLIW processor specied above. Table 2 (on the next page) represents the occupancy of each
functional unit during the execution of the assembly code in Figure 1.

For the assembly code given in Figure 1, ll in Table 2 with the appropriate VLIW instructions.

In your solution, minimize the number of VLIW instructions, and ensure that each instruction is scheduled to execute as soon as possible. Table 2 should only contain assembly operations
supported by the VLIW processor, as described in Table 1.

Functional Unit

VLIW
Instruction Load Load Load Store Mult Add Branch

1 LOOP: load_inc r2, [r31, r0, #0] load r3, [r29, r1, #0] load r4, [r30, r1, #0] NOP NOP NOP NOP

2 NOP NOP NOP NOP mult r5, r2, r3 NOP NOP

3 NOP NOP NOP NOP NOP add r6, r5, r4 NOP

4 NOP NOP NOP store_inc [r31, r1, #0], r6 NOP NOP NOP

5 NOP NOP NOP NOP NOP NOP bne r1, #N, LOOP

6

7

8

9

10

11

12

13

14

15

Table 2

(b) [15 points] What is the ratio between the number of useful operations and the number of VLIW

instructions in your code? A useful operation refers to any assembly operation that is not a NOP.

7
5 [useful operations per VLIW instruction.]

Explanation.
There are a total of 7 assembly operations (excluding NOPs) composing 5 VLIW instructions.

(c) [15 points] What is the execution time (in cycles) of the VLIW processor when executing the
sequence of instructions in Table 2, as a function of the loop counter N ? Show your work.

_Execution time = 5 × N_ .

Explanation.
A single iteration of the loop takes 5 clock cycles to execute. Since the loop repeats N
times, the total execution time is equal to 5 × N .

Final Exam Page 21 of 27

|Col1|Functional Unit|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|VLIW Instruction|Load|Load|Load|Store|Mult|Add|Branch|
|1 LOOP:|load_inc r2, [r31, r0, #0]|load r3, [r29, r1, #0]|load r4, [r30, r1, #0]|NOP|NOP|NOP|NOP|
|2|NOP|NOP|NOP|NOP|mult r5, r2, r3|NOP|NOP|
|3|NOP|NOP|NOP|NOP|NOP|add r6, r5, r4|NOP|
|4|NOP|NOP|NOP|store_inc [r31, r1, #0], r6|NOP|NOP|NOP|
|5|NOP|NOP|NOP|NOP|NOP|NOP|bne r1, #N, LOOP|
|6||||||||
|7||||||||
|8||||||||
|9||||||||
|10||||||||
|11||||||||
|12||||||||
|13||||||||
|14||||||||
|15||||||||


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

## 10 Cache [[50 points]]

Consider a processor using a 4-block LRU-based L1 data cache with a block size of 1 byte. Starting
with an empty cache, an application accesses three cache blocks with the following addresses in the order
given below:

0 → 2 → 4

A malicious programmer tries to reverse-engineer the number of sets and ways in the L1 data cache by
issuing only two more accesses and observing the cache hit rate across these two accesses. Assume that
the programmer can insert the malicious accesses only after the above three accesses of the application.

(a) [20 points] What are the addresses of the next two cache blocks that should be accessed to successfully reverse-engineer the number of sets and ways in the cache? There may be multiple solutions;
please give the lowest possible addresses that can enable the identication of the number of sets and ways. Please explain every step in detail to get full points.

0 → 2

Explanation. There are two possible answers:



[0 → 2]



[0 → 4]

There are three possible set/way congurations, shown below labeled by their respective
sets/ways. Each conguration shows a drawing of the cache state after the three initial
accesses. Rows and columns represent sets and ways, respectively, and the LRU address
is shown for each occupied set:

(a) (4 sets, 1 way)

4

            
2

            
(b) (2 sets, 2 ways)

4 2

            -            
(c) (1 set, 4 ways)

0 2 4        
At this point, all three congurations have a 100% miss rate since they started cold. In
order to dierentiate between the three congurations with just two more accesses, we
need to induce dierent hit/miss counts in each of them. The only way this is possible
is if one conguration experiences two hits, another two misses, and the last one hit and
one miss.
Only two solutions exist to produce this case:



[0 → 2]

(a) 0 miss, 2 hit = 50% miss rate

(b) 0 miss, 2 miss = 100% miss rate

(c) 0 hit, 2 hit = 0% miss rate



[0 → 4]

(a) 0 miss, 4 miss = 100% miss rate

(b) 0 miss, 4 hit = 50% miss rate

(c) 0 hit, 4 hit = 0% miss rate

Choosing the lowest possible addresses, the correct solution is 0 → 2

Final Exam Page 22 of 27

|4|2|
|---|---|
|-|-|

|0|2|4|-|
|---|---|---|---|


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

(b) [15 points] What is the number of sets and ways if the cache hit rate observed over the two extra
addresses accessed in Part (1) were:

L1 hit rate # sets # ways

100%

50%

0%

Explain your reasoning:

Based on the solution to Part (1), these are the number of sets and ways corresponding
to dierent hit rates.

L1 hit rate # sets # ways

100% 1 4

Solution:

50% 4 1

0% 2 2

(c) [15 points] Is it possible to reverse-engineer the number of sets and ways of the cache using two
accesses (after the application's rst three accesses) if the Most Recently Used (MRU) block is
replaced rst? Explain your reasoning.

No. There is no solution for just two more accesses because with an MRU policy, no
permutation of two more accesses is able to assign a unique L1 hit rate to each of the
three cache congurations.

Final Exam Page 23 of 27

|L1 hit rate|# sets|# ways|
|---|---|---|
|100%|||
|50%|||
|0%|||

|L1 hit rate|# sets|# ways|
|---|---|---|
|100%|1|4|
|50%|4|1|
|0%|2|2|


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

## 11 BONUS: Systolic Arrays [[50 points]]

You are given a systolic array of 2 × 2 Processing Elements (PEs), interconnected as shown in Figure 2.
The inputs of the systolic array are labeled as H0, H1 and V0, V1. Figure 3 shows the PE logic, which
performs a multiply-accumulate (MAC) operation and saves the result to an internal register (reg).
Figure 3 also shows how each PE propagates its inputs. We make the following assumptions:


The latency of each MAC operation is one cycle, i.e., if the inputs to a PE are available in cycle c,
the updated register value will be available in cycle c + 1.


The propagation of the values from i0 to o0, and from i1 to o1, takes one cycle.


The initial values of all internal registers is zero.

Figure 2: PE array Figure 3: Processing Element (PE)

Your goal is to use the systolic array shown in Figure 2 to perform the multiplication C = A × B, where
_A, B, and C are 2 × 2 matrices. Recall that the multiplication of two K × K matrices is dened as_
follows:

_K−1_
�

_Cij =_ _Aik_ _Bkj_

_×_
_k=0_

As an example, for K = 2, the calculation for C00 is as follows:

_C00 = A00_ _B00 + A01_ _B10_
_×_ _×_

Compute the multiplication in the minimum possible number of cycles. Fill the following table with:

1. Each input element (from matrices A2×2 and B2×2) in the correct cycle and input port of the
systolic array (H0, H1 and V0, V1).

2. Each output element (for matrix C2×2) in the cycle and PE that generates each output.

(a) [25 points] Fill in the blanks only with relevant information. Input cells left blank are interpreted
as 0.

cycle H0 H1 V0 V1 PE00 PE01 PE10 PE11

0 _A00_ _B00_

1 _A01 A10 B10 B01_

2 _A11_ _B11_ _C00_

3 _C01_ _C10_

4 _C11_

5
6
7

Final Exam Page 24 of 27

|cycle|H0|H1|V0|V1|PE 00|PE 01|PE 10|PE 11|
|---|---|---|---|---|---|---|---|---|
|0|A 00||B 00||||||
|1|A 01|A 10|B 10|B 01|||||
|2||A 11||B 11|C 00||||
|3||||||C 01|C 10||
|4||||||||C 11|
|5|||||||||
|6|||||||||
|7|||||||||


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

(b) [25 points] Suppose that the same systolic array from Figure 2 is used to compute the multiplication
of two 4 × 4 matrices. How many cycles does it take to perform the multiplication? Assume that
the register in a PE resets to 0 immediately after an output is generated, i.e., PEs can start
accumulating for the next output element in the next cycle without waiting for an extra cycle to
reset the register to 0. Show your work.

19 cycles.

Each PE needs to calculate four elements to calculate the 4 × 4 = 16 output elements.

For the rst element calculated by each PE, the timeline looks similar to (a), but requires
two additional cycles for the four MAC operations instead of two per element, i.e., seven
cycles in total until PE11 produces its output.

The remaining three elements calculated by each PE require four cycles each if pipelined
with the previously calculated element.

Thus, the total number of cycles is 7 + 3 × 4 = 19.

cycle H0 H1 V0 V1 PE00 PE01 PE10 PE11

0 _A00_ _B00_

1 _A01 A10 B10 B01_

2 _A02 A11 B20 B11_

3 _A03 A12 B30 B21_

4 _A00 A13 B02 B31_ _C00_

5 _A01 A10 B12 B03_ _C01_ _C10_

6 _A02 A11 B22 B13_ _C11_

7 _A03 A12 B32 B23_

8 _A20 A13 B00 B33_ _C02_

9 _A21 A30 B10 B01_ _C03_ _C12_

10 _A22 A31 B20 B11_ _C13_

11 _A23 A32 B30 B21_

12 _A20 A33 B02 B31_ _C20_

13 _A21 A30 B12 B03_ _C21_ _C30_

14 _A22 A31 B22 B13_ _C31_

15 _A23 A32 B32 B23_

16 _A33_ _B33_ _C22_

17 _C23_ _C32_

18 _C33_

Final Exam Page 25 of 27

|cycle|H0|H1|V0|V1|PE 00|PE 01|PE 10|PE 11|
|---|---|---|---|---|---|---|---|---|
|0|A 00||B 00||||||
|1|A 01|A 10|B 10|B 01|||||
|2|A 02|A 11|B 20|B 11|||||
|3|A 03|A 12|B 30|B 21|||||
|4|A 00|A 13|B 02|B 31|C 00||||
|5|A 01|A 10|B 12|B 03||C 01|C 10||
|6|A 02|A 11|B 22|B 13||||C 11|
|7|A 03|A 12|B 32|B 23|||||
|8|A 20|A 13|B 00|B 33|C 02||||
|9|A 21|A 30|B 10|B 01||C 03|C 12||
|10|A 22|A 31|B 20|B 11||||C 13|
|11|A 23|A 32|B 30|B 21|||||
|12|A 20|A 33|B 02|B 31|C 20||||
|13|A 21|A 30|B 12|B 03||C 21|C 30||
|14|A 22|A 31|B 22|B 13||||C 31|
|15|A 23|A 32|B 32|B 23|||||
|16||A 33||B 33|C 22||||
|17||||||C 23|C 32||
|18||||||||C 33|


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

## 12 BONUS: Prefetching [[50 points]]

An ETH student writes two programs (A and B) and runs them on two dierent toy machines (M1 and
M2) to determine the type of the prefetcher used in each of these machines. She observes programs A
and B to generate the following memory access patterns (note that these are cacheblock addresses, not
byte addresses).

Program A: 27 memory accesses

a, a + 1, a + 2, a + 3, a + 4, a + 8, a + 16, a + 32, a + 64,
a, a + 1, a + 2, a + 3, a + 4, a + 8, a + 16, a + 32, a + 64,
a, a + 1, a + 2, a + 3, a + 4, a + 8, a + 16, a + 32, a + 64

Program B: 501 memory accesses

b, b + 2, b + 4, ...., b + 998, b + 1000

The student measures the coverage (i.e., the fraction of program's memory accesses correctly predicted by
the prefetcher) and accuracy (i.e., the fraction of sent prefetch requests that are used by the program) of
the prefetching mechanism in each of the machines. The following table shows her measurement results:

Machine M1 Machine M2

Coverage Accuracy Coverage Accuracy

Program A 6/27 6/27 1/3 9/26

Program B 499/501 499/501 499/501 499/500

The student knows the following information about the machines:


There are three possible choices for the prefetching mechanism:

1. Stride prefetcher

2. 1st-next-block prefetcher with degree 1: Prefetches cacheline A +1 after seeing access to block

_A_

3. 4th-next-block prefetcher with degree 1: Prefetches cacheline A+4 after seeing access to block

_A_


Each prefetcher has large enough resources to detect and store access patterns.


Each prefetcher starts with an empty table.


Each prefetcher sends only one prefetch request for each program access.


Each memory access is separated long enough in time so that all prefetch requests sent can complete
before the next access occurs.


No prefetcher employs any condence mechanism (e.g., the stride prefetcher will send a prefetch

request to address A+4 by only seeing two consecutive memory accesses to addresses A and A+2).

Determine what type of prefetching mechanism is used by M1 and M2. Show your work. Answers
without explanation will not be rewarded.

Machine M1: 4th-next-line prefetcher

Machine M2: Stride prefetcher

Final Exam Page 26 of 27

|Col1|Machine M1 Coverage Accuracy|Machine M2 Coverage Accuracy|
|---|---|---|
|Program A Program B|6/27 6/27 499/501 499/501|1/3 9/26 499/501 499/500|


-----

Initials: Digital Design and Computer Architecture August 21st, 2023

Space for explanation:

M1: 4th-next-line prefetcher
M2: Stride prefetcher

Explanation

We calculate the accuracy and coverage for all three types of prefetchers, and then we can answer what
prefetcher each machine is using. Underlined and red-marked cacheline addresses are correctly and incorrectly
prefetched, respectively.

Each prefetcher works in the following way while running Application A:

Stride: Coverage: 1/3, Accuracy: 9/26
a, a + 1, a + 2, a + 3, a + 4, a + 8, a + 16, a + 32, a + 64, (incorrect: a + 5, a + 12, a + 24, a + 48, a + 96)
a, a + 1, a + 2, a + 3, a + 4, a + 8, a + 16, a + 32, a + 64, (incorrect: a - 64, a + 5, a + 12, a + 24, a + 48,
a + 96)
a, a + 1, a + 2, a + 3, a + 4, a + 8, a + 16, a + 32, a + 64 (incorrect: a - 64, a + 5, a + 12, a + 24, a + 48,
a + 96)

1st-next-line: Coverage: 4/9, Accuracy: 4/9
a, a + 1, a + 2, a + 3, a + 4, a + 8, a + 16, a + 32, a + 64, (incorrect: a + 5, a + 9, a + 17, a + 33, a + 65)
a, a + 1, a + 2, a + 3, a + 4, a + 8, a + 16, a + 32, a + 64, (incorrect: a + 5, a + 9, a + 17, a + 33, a + 65)
a, a + 1, a + 2, a + 3, a + 4, a + 8, a + 16, a + 32, a + 64, (incorrect: a + 5, a + 9, a + 17, a + 33, a + 65)

4th-next-line: Coverage: 6/27, Accuracy: 6/27
a, a + 1, a + 2, a + 3, a + 4, a + 8, a + 16, a + 32, a + 64, (incorrect: a + 5, a + 6, a + 7, a + 12, a + 20,
a + 36, a + 68)
a, a + 1, a + 2, a + 3, a + 4, a + 8, a + 16, a + 32, a + 64, (incorrect: a + 5, a + 6, a + 7, a + 12, a + 20,
a + 36, a + 68)
a, a + 1, a + 2, a + 3, a + 4, a + 8, a + 16, a + 32, a + 64 (incorrect: a + 5, a + 6, a + 7, a + 12, a + 20, a
+ 36, a + 68)

The three prefetechers work in the following way while running Application B:

Stride: Coverage: 499/501, Accuracy: 499/500
b, b + 2, b + 4, b + 6, b + 8, b + 10, ..., b + 998, b + 1000 (incorrect: b + 1002)

1st-next-line: Coverage: 0, Accuracy: 0
b, b + 2, b + 4, b + 6, b + 8, b + 10, ..., b + 998, b + 1000 (incorrect: b + 1, b + 3, ..., b + 999, b + 1001)

4th-next-line: Coverage: 499/501, Accuracy: 499/501
b, b + 2, b + 4, b + 6, b + 8, b + 10, ..., b + 998, b + 1000 (incorrect: b +1002, b + 1004)

Final Exam Page 27 of 27


-----

