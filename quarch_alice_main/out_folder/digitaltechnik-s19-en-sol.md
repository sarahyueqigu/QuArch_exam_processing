Family Name: SOLUTIONS First Name: Student ID:

### Final Exam

# Design of Digital Circuits (252-0028-00L)

 ETH Zürich, Spring 2019

#### Prof. Onur Mutlu

Problem 1 (12 Points): Boolean Algebra

Problem 2 (20 Points): Verilog

Problem 3 (30 Points): Finite State Machines (FSM)

Problem 4 (20 Points): ISA vs. Microarchitecture

Problem 5 (20 Points): Performance Evaluation

Problem 6 (40 Points): Pipeline (Reverse Engineering)

Problem 7 (36 Points): Tomasulo’s Algorithm

Problem 8 (30 Points): Systolic Arrays

Problem 9 (35 Points): GPUs and SIMD

Problem 10 (40 Points): Reverse Engineering Caches

Problem 11 (30 Points): Dataflow

Problem 12 (BONUS: 30 Points): Branch Prediction

Total (343 (313 + 30 bonus) Points):

**Examination Rules:**

1. Written exam, 180 minutes in total.

2. No books, no calculators, no computers or communication devices. 3 double-sided A4 sheets of
handwritten notes are allowed.

3. Write all your answers on this document; space is reserved for your answers after each question.

4. You are provided with scratchpad sheets. Do not answer questions on them. We will not collect them.

5. Clearly indicate your final answer for each problem. Answers will only be evaluated if they are readable.

6. Put your Student ID card visible on the desk during the exam.

7. If you feel disturbed, immediately call an assistant.

8. Write with a black or blue pen (no pencil, no green or red color).

9. Show all your work. For some questions, you may get partial credit even if the end result is wrong due
to a calculation mistake. If you make assumptions, state your assumptions clearly and precisely.

10. Please write your initials at the top of every page.

**Tips:**

_• Be cognizant of time. Do not spend too much time on one question._

_• Be concise. You may be penalized for verbosity._

_• Show work when needed. You will receive partial credit at the instructors’ discretion._

_• Write legibly. Show your final answer._


-----

Initials: Design of Digital Circuits August 23rd, 2019

_This page intentionally left blank_

Final Exam Page 1 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

### 1 Boolean Algebra [12 points]

(a) [6 points] Find the simplest sum-of-products representation of the following Boolean equation. Show
your work step-by-step.

_F = (A + B + C).(A + B + C).C + A_

_F = B.C + A_

**Explanation:**
_F = (A.A + A.B + A.C + B.A + B.B + B.C + C.A + C.B + C.C).C + A_
_F = (0 + B.(A + A) + A.C + B + B.(C + C) + C.A + 0).C + A_
_F = (B + A.C + B + B + C.A).C + A_
_F = (B.C + A.C.C + B.C + C.A.C) + A_
_F = (B.C + 0 + C.A) + A_
_F = B.C + A.(C + 1)_
_F = B.C + A_

(b) [6 points] Convert the following Boolean equation so that it contains only NAND operations. Show
your work step-by-step.

_F = A + (B.C + A.C)_

_F = (A.(B.C.A.C.A.C))_

**Explanation:**

_F = ((A + (B.C + A.C))_
_F = (A.(B.C + A.C))_

_F = (A.(B.C + A.C))_

_F = (A.(B.C.A.C))_

_F = (A.(B.C.A.C.A.C))_

Final Exam Page 2 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

### 2 Verilog [[20 points]]

Please answer the following three questions about Verilog.

(a) [5 points] Does the following code result in a single D Flip-Flop with a synchronous active-low reset?
Please explain your answer.

1 **module mem (input clk, input reset, input [1:0] d, output reg [1:0] q);**

2 **always @ (posedge clk or negedge reset)**

3 **begin**

4 **if (!reset) q <= 0;**

5 **else q <= d;**

6 **end**

7 **endmodule**

No.
The code implements two D Flip-Flops, not one. Each D Flip-Flop works with an
_asynchronous active-low reset signal._

**Explanation:**

      - D and Q signals are two-bit-wide. Therefore, this code implements two D flip-flops.

      - The reset input is included in the sensitivity list, therefore it is not synchronous.

      - The code resets the output if the reset signal is low. Thus, the reset signal is activelow.

(b) [5 points] Does the following code result in a sequential circuit or a combinational circuit? Please
explain your answer.

1 **module Mask (input [1:0] data_in, input mask, output reg [1:0] data_out);**

2 **always @ (*)**

3 **begin**

4 data_out[1] = data_in[1];

5 **if (mask)**

6 data_out[0] = 0;

7 **end**

8 **endmodule**

Sequential circuit.

**Explanation:**
This code results in a sequential circuit, as all the left-hand side signals are not assigned in
every possible condition. For example, data_out[0] is not assigned when mask signal
equals to zero.

Final Exam Page 3 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

(c) [10 points] Is the following code syntactically correct? If not, please explain the mistake(s) and how
to fix it/them.

1 **module fulladd(input a, b, c, output reg s, c_out);**

2 **assign s = a^b;**

3 **assign c_out = (a & b) | (b & c) & (c & a);**

4 **endmodule**

5

6 **module top ( input wire [5:0] instr, input wire op, output z);**

7

8 **reg[1:0] r1, r2;**

9 **wire [3:0] w1, w2;**

10

11 fulladd FA1 (.a(instr[0]), .b(instr[1]), .c(instr[2]),

12 .c_out(r1[1]), .z(r1[0]));

13 fulladd FA2 (.a(instr[3]), .b(instr[4]), .c(instr[5]),

14 .z(r2[0]), .c_out(r2[1]));

15

16 **assign z = r1 | op;**

17 **assign w1 = r1 + 1;**

18 **assign w2 = r2 << 1;**

19 **assign op = r1 ^ r2;**

20

21 **endmodule**

The code is not syntactically correct.

**Explanation:**

_• ‘r1’ and ‘r2’ have to be declared as wires._

_• ‘op’ signal is connected to multiple drivers. It gets assigned from the input port and in_
line 19.

_• The module ‘fulladd’ does not have ports named ‘z’. Those need to be changed to ‘s’._

_• The output signals ‘s’ and ‘c_out’ have to be declared as wires but not as regs, since_
they are driven by assign statements.

Final Exam Page 4 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

### 3 Finite State Machines (FSM) [[30 points]]

You are given two one-bit input signals (TA and TB) and one one-bit output signal (O) for the following
modular equation: 2N (TA)+N (TB) ≡ 2 (mod 4). In this modular equation, N (TA) and N (TB) represent
the total number of times the inputs TA and TB are high (i.e., logic 1) at each positive clock edge,
respectively. The one-bit output signal, O, is set to 1 when the modular equation is satisfied (i.e.,
2N (TA) + N (TB) ≡ 2 (mod 4)), and 0 otherwise. An example that sets O = 1 at the end of the fourth
cycle would be:

   - (1[st] cycle) TA = 0 (N (TA) = 0), TB = 0 (N (TB) = 0), 2N (TA) + N (TB) ≡ 0 (mod 4) ⇒ _O = 0_

  - (2[nd] cycle) TA = 1 (N (TA) = 1), TB = 1 (N (TB) = 1), 2N (TA) + N (TB) ≡ 3 (mod 4) ⇒ _O = 0_

  - (3[rd] cycle) TA = 1 (N (TA) = 2), TB = 0 (N (TB) = 1), 2N (TA) + N (TB) ≡ 1 (mod 4) ⇒ _O = 0_

   - (4[th] cycle) TA = 0 (N (TA) = 2), TB = 1 (N (TB) = 2), 2N (TA) + N (TB) ≡ 2 (mod 4) ⇒ _O = 1_

(a) [10 points] You are given a partial Moore machine state transition diagram that corresponds to
the modular equation described above. However, the input labels of most of the transitions are
still missing in this diagram. Please label the transitions with the correct inputs so that the FSM
correctly implements the above specification.
```
         0(mod4) 1(mod4)
        O:0 O:0
         3(mod4) 2(mod4)
        O:0 O:1

```
Final Exam Page 5 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

(b) [10 points] Describe the FSM with Boolean equations assuming that the states are encoded with
**one-hot encoding. Assign state encodings while using the minimum possible number of bits to**
represent the states. Please indicate the values you assign to each state.

State assignments: 0 (mod 4): 0001, 1 (mod 4): 0010, 2 (mod 4): 0100, 3 (mod 4): 1000
CS denotes current states, and NS denotes next states.
_NS[0] = CS[0] TA TB + CS[1] TA TB + CS[2] TA TB + CS[3] TA TB_
_NS[1] = CS[1] TA TB + CS[2] TA TB + CS[3] TA TB + CS[0] TA TB_
_NS[2] = CS[2] TA TB + CS[3] TA TB + CS[0] TA TB + CS[1] TA TB_
_NS[3] = CS[3] TA TB + CS[0] TA TB + CS[1] TA TB + CS[2] TA TB_
_O[0] = CS[2]_

(c) [10 points] Describe the FSM with Boolean equations assuming that the states are encoded with
**binary encoding (i.e., fully encoding). Assign state encodings while using the minimum possible**
number of bits to represent the states. Please indicate the values you assign to each state.

State assignments: 0 (mod 4): 00, 1 (mod 4): 01, 2 (mod 4): 10, 3 (mod 4): 11
CS denotes current states, and NS denotes next states.
_NS[0] = CS[0] TB + CS[0] TB_
_NS[1] = CS[0] (CS[1] XOR TA XOR TB) + CS[0] (TA XOR CS[1])_
_O[0] = CS[1] CS[0]_

Final Exam Page 6 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

### 4 ISA vs. Microarchitecture [[20 points]]

A new CPU has two comprehensive user manuals available for purchase as shown in Table 1.

**Manual Title** **Cost** **Description**

the_isa.pdf CHF 1 million describes the ISA in detail

the_microarchitecture.pdf CHF 10 million describes the microarchitecture in detail

Table 1: Manual Costs

Unfortunately, the manuals are extremely expensive, and you can only afford one of the two. If both
manuals might be useful, you would prefer the cheaper one.

For each of the following questions that you would like to answer, decide which manual is more likely to
help. Note: we will subtract 1 point for each incorrect answer. For an unanswered question, you will
_get +0 points._

1. [2 points] The latency of a branch predictor misprediction.

1. the_isa.pdf 2. the_microarchitecture.pdf

2. [2 points] The size of a physical memory page.

1. the_isa.pdf 2. the_microarchitecture.pdf

3. [2 points] The memory-mapped locations of exception vectors.

1. the_isa.pdf 2. the_microarchitecture.pdf

4. [2 points] The function of each bit in a programmable branch-predictor configuration register.

1. the_isa.pdf 2. the_microarchitecture.pdf

5. [2 points] The bit-width of the interface between the CPU and the L1 cache.

1. the_isa.pdf 2. the_microarchitecture.pdf

6. [2 points] The number of pipeline stages in the CPU.

1. the_isa.pdf 2. the_microarchitecture.pdf

7. [[2 points] ]The order in which loads and stores are executed by a multi-core CPU.

1. the_isa.pdf 2. the_microarchitecture.pdf

8. [2 points] The memory addressing modes available for arithmetic operations.

1. the_isa.pdf 2. the_microarchitecture.pdf

9. [2 points] The program counter width.

1. the_isa.pdf 2. the_microarchitecture.pdf

10. [2 points] The number of cache sets at each level of the cache hierarchy.

1. the_isa.pdf 2. the_microarchitecture.pdf

Final Exam Page 7 of 24

|Manual Title|Cost|Description|
|---|---|---|
|the_isa.pdf|CHF 1 million|describes the ISA in detail|
|the_microarchitecture.pdf|CHF 10 million|describes the microarchitecture in detail|


-----

Initials: Design of Digital Circuits August 23rd, 2019

### 5 Performance Evaluation [[20 points]]

You are the leading engineer of a new processor. Both the design of the processor and the compiler for it
are already done. Now, you need to decide if you will send the processor to manufacturing at its current
stage or if you will delay the production to introduce last-minute improvements to the design. To make
the decision, you meet with your team to brainstorm about how to improve the design. Together, after
profiling the target applications for the processor, you come up with two options:

  - Keep the current project. For version A of the processor, the clock frequency is 600 MHz, and
the following measurements are obtained:

**Instruction Class** **CPI** **Frequency of Occurrence**

A 2 40%

B 3 25%

C 3 25%

D 7 10%

  - Include optimizations to the design. For version B of the processor, the clock frequency is
700 MHz. The ISA for processor B includes three new types of instructions. Those three new
types of instructions increase the total number of executed instructions for processor B by 50%, in
comparison to processor A. The following measurements are obtained:

**Instruction Class** **CPI** **Frequency of Occurrence**

A 2 15%

B 2 15%

C 4 10%

D 6 10%

E 1 10%

F 2 20%

G 2 20%

(a) [7 points] What is the CPI of each version? Show your work.

_CPIA:_

3

_CPIB:_

2.5

_CPIA = 2 × 0.4 + 3 × 0.25 + 3 × 0.25 + 7 × 0.1 = 3_
_CPIB = 2 × 0.15 + 2 × 0.15 + 4 × 0.1 + 6 × 0.1 + 1 × 0.1 + 2 × 0.2 + 2 × 0.2 = 2.5_

(b) [6 points] What are the MIPS (Million Instructions Per Second) of each version? Show your work.

Final Exam Page 8 of 24

|Instruction Class|CPI|Frequency of Occurrence|
|---|---|---|

|A|2|40%|
|---|---|---|

|B|3|25%|
|---|---|---|

|C|3|25%|
|---|---|---|

|D|7|10%|
|---|---|---|

|Instruction Class|CPI|Frequency of Occurrence|
|---|---|---|

|A|2|15%|
|---|---|---|

|B|2|15%|
|---|---|---|

|C|4|10%|
|---|---|---|

|D|6|10%|
|---|---|---|

|E|1|10%|
|---|---|---|

|F|2|20%|
|---|---|---|

|G|2|20%|
|---|---|---|


-----

Initials: Design of Digital Circuits August 23rd, 2019

_MIPSA:_

200

_MIPSB:_

280

_MIPSA =_ 6003∗MHz10[6] = 200

_MIPSB =_ 7002.5MHz∗10[6][ = 280]

(c) [7 points] Considering your team is aiming to release to the market the processor that gives better
performance when executing the target application, which processor version will you choose as the
final design? Show your work.

Processor A.

**Explanation:**
We calculate the execution time for each processor, Time = Ninstr. _× CPI ×_ _clockfrequency1_

Since the compiler for processor B generates 50% more instructions than the compiler for
processor A, the total execution time for processor B is larger than the total execution
time for processor A.

_TimeA = Ninstr. × 3 ×_ 600∗110[6]

_TimeB = 1.5Ninstr. × 2.5 ×_ 700∗110[6]

Final Exam Page 9 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

### 6 Pipeline (Reverse Engineering) [[40 points]]

The following piece of code runs on a pipelined microprocessor as shown in the table (F: Fetch, D:
Decode, E: Execute, M: Memory, W: Write back). Instructions are in the form “Instruction Destination,
Source1, Source2.” For example, “ADD A, B, C” means A ← B + C.

Cycles 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

0 MUL R5, R6, R7 F D E1 E2 E3 E4 M W

1 ADD R4, R6, R7 F D E1 E2 E3 - M W

2 ADD R5, R5, R6 F D - - E1 E2 E3 M W

3 MUL R4, R7, R7 F - - D E1 E2 E3 E4 M W

4 ADD R6, R7, R5 F D - E1 E2 E3 M W

5 ADD R3, R0, R6 F - D - - E1 E2 E3 M

6 ADD R7, R1, R4 F - - D E1 E2 E3

Use this information to reverse engineer the architecture of this microprocessor to answer the following
questions. Answer the questions as precise as possible with the provided information. If the provided
information is not sufficient to answer a question, answer “Unknown” and explain your reasoning clearly.

(a) [5 points] How many cycles does it take for an adder and for a multiplier to calculate a result?

3 cycles for adder (E1, E2, E3) and 4 cycles for multiplier (E1, E2, E3, E4).

(b) [[5 points] ]What is the minimum number of register file read/write ports that this architecture implements? Explain.

The register file has two read ports and one write port.

(c) [5 points] Can we reduce the execution time of this code by enabling more read/write ports in the
register file? Explain.

It is not possible to reduce stall cycles of the given code by enabling more register file
ports.

(d) [5 points] Does this architecture implement any data forwarding? If so, how is data forwarding done
between pipeline stages? Explain.

There is data forwarding from the M stage to E1, as we observe that the instruction 2
starts using R5 at the clk cycle 7, which is one clk cycle after the instruction 0 finishes
calculating its result in the execution unit.
Similarly, as another proof of this data forwarding, we observe that the instruction 4
starts using R5 at the clk cycle 10, which is one clk cycle after the instruction 2 finishes
calculating its result in the execution unit.

Any other data forwarding is unknown with the given information.

Final Exam Page 10 of 24

|Col1|Cycles|1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18|
|---|---|---|
|0 1 2 3 4 5 6|MUL R5, R6, R7 ADD R4, R6, R7 ADD R5, R5, R6 MUL R4, R7, R7 ADD R6, R7, R5 ADD R3, R0, R6 ADD R7, R1, R4|F D E1 E2 E3 E4 M W F D E1 E2 E3 - M W F D - - E1 E2 E3 M W F - - D E1 E2 E3 E4 M W F D - E1 E2 E3 M W F - D - - E1 E2 E3 M W F - - D E1 E2 E3 M W|


-----

Initials: Design of Digital Circuits August 23rd, 2019

(e) [5 points] Is it possible to run this code faster by adding more data forwarding paths? If it is, how?
Explain.

Not possible.

All instructions that stall due to data dependency are already using the best possible data
forwarding. There is no stall cycles that can be eliminated by enabling another form of
data forwarding.

(f) [5 points] Is there internal forwarding in the register file? If there is not, how would the execution
time of the same program change by enabling internal forwarding in the register file? Explain.

There already is internal forwarding in the register file, as instruction 6 can finish the
decode stage by fetching the value of R4 from the register file in the same cycle that R4 is
written (cycle 13).

Final Exam Page 11 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

(g) [10 points] Optimize the assembly code in order to reduce the number of stall cycles. You are allowed
to reorder, add, or remove ADD and MUL instructions. You are expected to achieve the minimum
possible execution time. Make sure that the register values that the optimized code generates at
the end of its execution are identical to the register values that the original code generates at the
end of its execution. Justify each individual change you make. Show the execution timeline of each
instruction and what stage it is in the table below. (Notice that the table below consists of two parts:
_the first ten cycles at the top, and the next ten cycles at the bottom.)_

      - Instruction 1 is useless due to write-after-write, remove it.

      - Instruction 3 stalls for decode logic, move it up.

      - Instruction 6 does not have read-after-write dependency and can be executed before
instr. 5. However, it cannot execute before instruction 4 as it would change the value
of R7.
New total execution time is 17 cycles instead of 18.

Instr. Instructions Cycles

No 1 2 3 4 5 6 7 8 9 10

0 MUL R5, R6, R7 F D E1 E2 E3 E4 M W

3 MUL R4, R7, R7 F D E1 E2 E3 E4 M W

2 ADD R5, R5, R6 F D     -     - E1 E2 E3 M

4 ADD R6, R7, R5 F     -     - D     -     - E1

6 ADD R7, R1, R4 F     -     - D

5 ADD R3, R0, R6 F

11 12 13 14 15 16 17 18 19 20

0 MUL R5, R6, R7

3 MUL R4, R7, R7

2 ADD R5, R5, R6 W

4 ADD R6, R7, R5 E2 E3 M W

6 ADD R7, R1, R4 E1 E2 E3 M W

5 ADD R3, R0, R6 D     - E1 E2 E3 M W

Final Exam Page 12 of 24

|Instr. No|Instructions|Cycles 1 2 3 4 5 6 7 8 9 10|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|0|MUL R5, R6, R7|F|D|E1|E2|E3|E4|M|W|||
|3|MUL R4, R7, R7||F|D|E1|E2|E3|E4|M|W||
|2|ADD R5, R5, R6|||F|D|-|-|E1|E2|E3|M|
|4|ADD R6, R7, R5||||F|-|-|D|-|-|E1|
|6|ADD R7, R1, R4|||||||F|-|-|D|
|5|ADD R3, R0, R6||||||||||F|
|||||||||||||
|||||||||||||
|||||||||||||
|||11|12|13|14|15|16|17|18|19|20|
|0|MUL R5, R6, R7|||||||||||
|3|MUL R4, R7, R7|||||||||||
|2|ADD R5, R5, R6|W||||||||||
|4|ADD R6, R7, R5|E2|E3|M|W|||||||
|6|ADD R7, R1, R4|E1|E2|E3|M|W||||||
|5|ADD R3, R0, R6|D|-|E1|E2|E3|M|W||||
|||||||||||||
|||||||||||||
|||||||||||||


-----

Initials: Design of Digital Circuits August 23rd, 2019

### 7 Tomasulo’s Algorithm [[36 points]]

In this problem, we consider an in-order fetch, out-of-order dispatch, and out-of-order retirement execution engine that employs Tomasulo’s algorithm. This engine behaves as follows:

  - The engine has four main pipeline stages: Fetch (F), Decode (D), Execute (E), and Write-back
(W).

  - The engine can fetch FW instructions per cycle, decode DW instructions per cycle, and write
back the result of RW instructions per cycle.

  - The engine has two execution units: 1) an integer ALU for executing integer instructions (i.e.,
addition and multiplication) and 2) a memory unit for executing load/store instructions.

  - Each execution unit has an R-entry reservation station.

  - An instruction always allocates the first available entry of the reservation station (in top-to-bottom
order) of the corresponding execution unit.

The reservation stations are all initally empty. The processor fetches and executes six instructions.
Table 2 shows the six instructions and their execution diagram.

Using the information provided above and in Table 2 (see the next page), fill in the blanks below with the
configuration of the out-of-order microarchitecture. Write “Unknown” if the corresponding configuration
cannot be determined using the information provided in the question.

The latency of the ALU and memory unit instructions: ALU - 2 cycles, MU - 10 cycles

In which pipeline stage is an instruction dispatched? Decode (D) stage

Number of entries of each reservation station (R): Two entries each

Fetch width (FW): 2

Decode width (DW): 2

Retire width (RW): Unknown

Is the integer ALU pipelined? Unknown

Is the memory unit pipelined? Yes

If applicable, between which stages is data forwarding implemented? No data forwarding

Final Exam Page 13 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

Final Exam Page 14 of 24

|33|Col2|Col3|Col4|Col5|Col6|W|
|---|---|---|---|---|---|---|
|32||||||E10|
|31||||||E9|
|30||||||E8|
|29||||||E7|
|28||||||E6|
|27||||||E5|
|26||||||E4|
|25||||||E3|
|24||||||E2|
|23||||||E1|
|22|||||W|-|
|21|||||E2|-|
|20|||||E1|-|
|19||||W|-|-|
|18||||E10|-|-|
|17||||E9|-|D|
|16||W||E8|-|-|
|15||E10||E7|-|-|
|14||E9||E6|-|-|
|13||E8||E5|-|-|
|12||E7||E4|-|-|
|11||E6||E3|-|-|
|10||E5||E2|-|-|
|9||E4||E1|-|-|
|8||E3|W|-|-|-|
|7||E2|E2|-|-|-|
|6||E1|E1|-|D|-|
|5|W|-|-|-|-|-|
|4|E2|-|-|-|-|-|
|3|E1|-|D|D|F|F|
|2|D|D|F|F|||
|1|F|F|||||
|Instruction/Cycle:|1: ADD R1 R1 ←R0,|2: LD R2 ←[R1]|3: ADDI R1 #4 ←R1,|4: LD R3 ←[R1]|5: MUL R4 R3 ←R2,|6: ST [R0] ←R4|


-----

Initials: Design of Digital Circuits August 23rd, 2019

### 8 Systolic Arrays [[30 points]]

A systolic array consists of 3x4 Processing Elements (PEs), interconnected as shown in Figure 1. The
inputs of the systolic array are labeled as H0, H1, H2 and V0,V1,V2,V3. Figure 2 shows the PE logic,
which performs a multiply and accumulate operation (MAC), and it saves the result in an internal register
(reg). Figure 2 also shows how each PE propagates its inputs. We make the following assumptions:

  - The latency of each MAC is one cycle.

  - The propagation of the values from i0 to o0, and from i1 to o1, takes one cycle.

  - The initial value of all registers is zero.

  - You can input a value more than once in the systolic array.

V0 V1 V2 V3

Processing Element (PE)

H0 PE00 PE01 PE02 PE03 i1

H1 PE10 PE11 PE12 PE13 i0 oo01 = i = i01 reg o0

reg = i0*i1+ reg

H2 PE20 PE21 PE22 PE23 o1

Figure 1: PE array Figure 2: Processing Element (PE)

Your goal is to use this systolic array to perform the convolution of a 3x3 image (matrix I) with three
2x2 filters (matrices F, G, and H), to obtain three outputs (matrices O, U, and E):

_II0010_ _II0111_ _II0212_ ⊛ _F00_ _F01_ = _O00_ _O01_
_I20_ _I21_ _I22_ _F10_ _F11_ _O10_ _O11_

_II0010_ _II0111_ _II0212_ ⊛ _G00_ _G01_ = _U00_ _U01_
_I20_ _I21_ _I22_ _G10_ _G11_ _U10_ _U11_

_II0010_ _II0111_ _II0212_ ⊛ _H00_ _H01_ = _E00_ _E01_
_I20_ _I21_ _I22_ _H10_ _H11_ _E10_ _E11_

As an example, the convolution of the matrix I with the filter F is computed as follows:

  - O00 = I00 _F00 + I01_ _F01 + I10_ _F10 + I11_ _F11_
_∗_ _∗_ _∗_ _∗_

  - O01 = I01 _F00 + I02_ _F01 + I11_ _F10 + I12_ _F11_
_∗_ _∗_ _∗_ _∗_

  - O10 = I10 _F00 + I11_ _F01 + I20_ _F10 + I21_ _F11_
_∗_ _∗_ _∗_ _∗_

  - O11 = I11 _F00 + I12_ _F01 + I21_ _F10 + I22_ _F11_
_∗_ _∗_ _∗_ _∗_

Final Exam Page 15 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

You should compute the three convolutions in the minimum possible amount of cycles. Fill the following
table with:

1. The input values (matrices I, F, G, and H) in the correct input ports of the systolic array (the
values can be repeated).

2. The output values and the corresponding PE where the outputs (matrices O, U, and E) are generated.

Fill the gaps only with relevant information.

**cycle H0 H1 H2 V0 V1 V2 V3 PE00 PE01 PE02 PE03 PE10 PE11 PE12 PE13 PE20 PE21 PE**

0 _F00_ _I00_

1 _F01 G00_ _I01 I01_

2 _F10 G01 H00 I10 I02 I10_

3 _F11 G10 H01 I11 I11 I11 I11_ _O00_

4 _G11 H10_ _I12 I20 I12_ _O01_ _U00_

5 _H11_ _I21 I21_ _O10_ _U01_ _E00_

6 _I22_ _O11_ _U10_ _E01_

7 _U11_ _E10_

8

9

10
11
12
13
14
15

Final Exam Page 16 of 24

|cycle|H0|H1|H2|V0|V1|V2|V3|PE 00|PE 01|PE 02|PE 03|PE 10|PE 11|PE 12|PE 13|PE 20|PE 21|PE 22|PE 23|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0|F 00|||I 00||||||||||||||||
|1|F 01|G 00||I 01|I 01|||||||||||||||
|2|F 10|G 01|H 00|I 10|I 02|I 10||||||||||||||
|3|F 11|G 10|H 01|I 11|I 11|I 11|I 11|O 00||||||||||||
|4||G 11|H 10||I 12|I 20|I 12||O 01|||U 00||||||||
|5|||H 11|||I 21|I 21|||O 10|||U 01|||E 00||||
|6|||||||I 22||||O 11|||U 10|||E 01|||
|7|||||||||||||||U 11|||E 10||
|8|||||||||||||||||||E 11|
|9||||||||||||||||||||
|10||||||||||||||||||||
|11||||||||||||||||||||
|12||||||||||||||||||||
|13||||||||||||||||||||
|14||||||||||||||||||||
|15||||||||||||||||||||


-----

Initials: Design of Digital Circuits August 23rd, 2019

### 9 GPUs and SIMD [[35 points]]

We define the SIMD utilization of a program that runs on a GPU as the fraction of SIMD lanes that are
kept busy with active threads during the run of a program. As we saw in lecture and practice exercises,
the SIMD utilization of a program is computed across the complete run of the program.

The following code segment is run on a GPU. Each thread executes a single iteration of the shown
loop. Assume that the data values of the arrays A and B are already in vector registers so there are no
loads and stores in this program. (Hint: Notice that there are 4 instructions in each iteration.) A warp
in the GPU consists of 32 threads, and there are 32 SIMD lanes in the GPU.

for (i = 0; i < 1026; i++) {
if (A[i] < 33) { // Instruction 1
B[i] = A[i] << 1; // Instruction 2
}
if (A[i] > 33) { // Instruction 3
B[i] = A[i] >> 1; // Instruction 4
}
}

Please answer the following five questions.

(a) [2 points] How many warps does it take to execute this program?

33 warps.

**Explanation:**
The number of warps is calculated as:
#Warps = ⌈ [#]#[T otal]W arp[_][threads]_size

_[⌉][,]_

where
#Total_threads = 1026 = 2[10] + 2 (i.e., one thread per loop iteration),

and
#Warp_size = 32 = 2[5] (given).

Thus, the number of warps needed to run this program is:
#Warps = ⌈ [2][10]2[5][+2] _⌉_ = 2[5] + 1 = 33.

(b) [10 points] What is the maximum possible SIMD utilization of this program? Show your work. (Hint:
The warp scheduler does not issue instructions where no threads are active).

3076
3136 [=][ 769]784 [.]

**Explanation:**
The maximum SIMD utilization is achieved when all threads of the complete warps follow
the same execution path and execute Instruction 2 or Instruction 4 (A[i] > 33
or A[i] < 33), and the two active threads of the last warp do not execute Instruction
2 or Instruction 4 (A[i] = 33).
The maximum SIMD utilization sums to [1026+32]1056+1024+1056[×][32+1026] [=][ 3076]3136 [.]

Final Exam Page 17 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

(c) [5 points] Please describe what needs to be true about array A to reach the maximum possible SIMD
utilization asked in part (b). (Please cover all cases in your answer.)

For every 32 consecutive elements of A out of the first 1024 elements, every element should
be lower than 33 (if(A[i] < 33)), or greater than 33 (if(A[i] > 33)). The last
two elements should be equal to 33. (NOTE: The solution is correct if the three cases are
given.)

(d) [13 points] What is the minimum possible SIMD utilization of this program? Show your work.

353
704 [.]

**Explanation:**
Instruction 1 is executed by every active thread ( [1026]1056 [utilization).]

The minimum SIMD utilization of Instruction 2 occurs if only one thread per warp
executes it.
Instruction 3 is again executed by every active thread ( [1026]1056 [utilization).]

Finally, the minimum SIMD utilization of Instruction 4 occurs if only one thread per
warp executes it.

The minimum SIMD utilization sums to [1026+1]1056+1056+1056+1056[×][33+1026+1][×][33] [=][ 353]704 [.]

(e) [5 points] Please describe what needs to be true about array A to reach the minimum possible SIMD
utilization asked in part (d). (Please cover all cases in your answer.)

For every 32 consecutive elements among the first 1024 elements of A, one element should
be lower than 33 (if(A[i] < 33)), one element should be greater than 33 (if(A[i]

     - 33)), and the remaining 30 elements should be equal to 33.
For the last 2 elements of A, one element should be lower than 33 (if(A[i] < 33)), and
the other element should be greater than 33 (if(A[i] > 33)).

Final Exam Page 18 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

### 10 Reverse Engineering Caches [[40 points]]

You are trying to reverse-engineer the characteristics of a cache in a system, so that you can design
a more efficient, machine-specific implementation of an algorithm you are working on. To do so, you
have come up with three sequences of memory accesses to various bytes in the system in an attempt to
determine the following four cache characteristics:

  - Cache block size (8, 16, 32, 64, or 128 B).

  - Cache associativity (1-, 2-, 4-, or 8-way).

  - Cache size (4 or 8 KB).

  - Cache replacement policy (LRU or FIFO).

The only statistic that you can collect on this system is cache hit rate after performing each sequence of
memory accesses. Here is what you observe:

Sequence Addresses Accessed (Oldest → Youngest) Hit Rate

1. 31 8192 63 16384 4096 8192 64 16384 3/8
2. 32768 0 129 1024 3072 8192 0
3. 0 4 8 4096 64 128 1

Assume that the cache is initially empty at the beginning of the first sequence, but not at the beginning
of the second and third sequences. The sequences are executed back-to-back, i.e., no other accesses take
place in between the three sequences. Thus, at the beginning of the second (third) sequence, the
**contents are the same as at the end of the first (second) sequence.**

Based on what you observe, what are the following characteristics of the cache? Explain to get points.
If a characteristic cannot be known, then write "Unknown" and explain.

(a) [10 points] Cache block size (8, 16, 32, 64, or 128 B)?

64 B.

**Explanation:**
Cache hit rate is 3/8 in sequence 1. This means that there are 3 hits. As two of them
should be the second accesses to 8192 and 16384, the other hit is the access to 63. With a
cache block of 64 B, the access to address 64 results in a miss.

Final Exam Page 19 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

(b) [10 points] Cache associativity (1-, 2-, 4-, or 8-way)?

4-way.

**Explanation:**
We already know that the cache block size is 64 B. Thus, there are 6 offset bits.

Regardless of cache size or associativity, addresses 0, 8192, 16384, and 32768 map to the
same set. Thus, the cache cannot be 1-way, because we would not see hits on 8192 and
16384 in sequence 1.

If the cache were 2-way, 4096 would also map to the same set as 0, 8192, 16384, and
32768. This would make impossible a cache hit on 8192 in sequence 1.

If the cache were 8-way, 0, 1024, 3072, 4096, 8192, 16384, and 32768 would all map to set
0. With 8 ways, address 0 would not be replaced, so it would hit in sequence 2.

Therefore, the cache is 4-way associative.

(c) [10 points] Cache size (4 or 8 KB)?

8 KB.

**Explanation:**
We know that the cache is 4-way associative. In the beginning of sequence 2, 32768
replaces 0 (regardless of the replacement policy).

The fact that 8192 misses in sequence 2 can be explained by two possible cases:
1. If the replacement policy is FIFO, the access to 0 in sequence 2 replaces 8192. Thus,
the cache size can be either 4 or 8 KB.

2. If the replacement policy is LRU, the access to 0 in sequence 2 replaces 4096. If the
cache size is 4 KB, 1024 and 3072 map to the same set as 0 and 8192, and 1024 replaces
8192.

Since there is a hit on 4096 in sequence 3, the size should be 8 KB. Otherwise, 3072 would
have replaced 4096.

(d) [10 points] Cache replacement policy (LRU or FIFO)?

FIFO.

**Explanation:**
As explained above, if the cache size is 8 KB, only FIFO can make address 0 replace
address 8192 in sequence 2.

Final Exam Page 20 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

### 11 Dataflow [[30 points]]

  - We define the switch node in Figure 3 to have 2 inputs (I, Ctrl) and 1 output (O). The Ctrl input
always enters perpendicularly to the switch node. If the Ctrl input has a True token (i.e., a token
with a value of 1), the O wire propagates the value on the I wire. Else, the 2 input tokens (I,
**Ctrl) are consumed, and no token is generated at the output (O).**

  - We define the inverter node in Figure 4 to have 1 input (I) and 1 output (O). The node negates
the input token (i.e., O = !I).

  - We define the TF node in Figure 5 to have 3 inputs (IF, IT, Ctrl) and 1 output (O). When Ctrl
is set to True, O takes IT . When Ctrl is set to False, O takes IF .

  - The ≥ node outputs True only when the left input is greater than or equal to the right input.

  - The +1 node outputs the input plus one.

  - The + node outputs the sum of the two inputs.

  - A node generates an output token when tokens exist at every input, and all input tokens are
consumed.

  - Where a single wire splits into multiple wires, the token travelling on the wire is replicated to all
wires.


_all input tokens are_


O


I


Ctrl

Figure 3: Switch Node


Consider the dataflow graph on the following page. Numbers in dashed boxes represent tokens (with the
value indicated by the number) in the initial state. The X and Y inputs automatically produce tokens as
soon as the previous token on the wire is consumed. The order of these tokens follows the pattern (note,
_the following are all single digit values spaced appropriately for the reader to easily notice the pattern):_


**X: 0 01 011 0111 01111**

**Y: 1 22 333 4444 55555**


Consider the dataflow graph on the following page. Please clearly describe the sequence of tokens
generated at the output (OUT).

1, 4, 9, 16, 25

Final Exam Page 21 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

## +1 > Y

0

F T

0

0

1

T F

**X**

## >

OUT + **Y**

0

F T

0

**X: 0 01 011 0111 01111 ….**

Final Exam Page 22 of 24


-----

Initials: Design of Digital Circuits August 23rd, 2019

### 12 BONUS: Branch Prediction [[30 points]]

Assume a machine with a two-bit global history register (GHR) shared by all branches, which starts with
Not Taken, Not Taken (2’b00). Each pattern history table entry (PHTE) contains a 2-bit saturating
counter. The saturating counter values are as follows:

2’b00 - Strongly Not Taken
2’b01 - Weakly Not Taken
2’b10 - Weakly Taken
2’b11 - Strongly Taken

Assume the following piece of code runs on this machine. The code has two branches (labeled B1 and
B2). When we say that a branch is taken, we mean that the code inside the curly brackets is executed.
For the following questions, assume that this is the only block of code that will ever be run, and the
loop-condition branch (B1) is resolved first in the iteration before the if-condition branch (B2).

for (int i = 0; i < 1000000; i++) { /* B1 */
/* TAKEN PATH for B1 */
if (i % 3 == 0) { /* B2 */
j[i] = k[i] -1; /* TAKEN PATH for B2 */
}
}

(a) [20 points] Is it possible to observe that the branch predictor mispredicts 100% of the times in the
first 5 iterations of the loop? If yes, fill in the table below with all possible initial values each entry
can take. We represent Not Taken with N, and Taken with T.

Table 3: PHT

PHT Entry Value

TT 01

TN 00

NT 01

NN 00 or 01

Show your work here.

Yes, it is possible.
The pattern after 5 iterations: TTTNTNTTTN.
In order to be more clear, we add indices to each branch outcome in the pattern above, to
represent their positions in the pattern: T1 T2 T3 N4 T5 N6 T7 T8 T9 N10

      - For GHR=NN, the only observed branch is T1. Therefore, the PHTE for NN has to
be either 00 or 01 so that the branch predictor mispredicts the taken branch.

     - For GHR=TT, the observed branches are T3 N4 T9 N10. The PHTE for TT has to
be initialized to 01 in order to cause the predictor to always mispredict. This way,
each N and T moves the saturating counter to their respective direction. This will
cause misprediction for the next branch which is always in the opposite direction.

      - For GHR=TN, the observed branches are T5 T7. Thus, the initial PHTE value for
TN has to be 00 to mispredict both taken branches.

      - For GHR=NT, the observed branches are T2 N6 T8. Similar to the TT entry, NT’s
PHTE has to be initialized 01.

Final Exam Page 23 of 24

|PHT Entry|Value|
|---|---|
|TT|01|
|TN|00|
|NT|01|
|NN|00 or 01|


-----

Initials: Design of Digital Circuits August 23rd, 2019

(b) [10 points] At steady-state, we observe the following pattern which repeats over time: TTTNTN,
with T representing Taken, and N representing Not Taken. When GHR pattern equals to NT or
TT, the predictor will observe that the branch outcome will be either T or N. Therefore, no matter
what the initial values for these two entries are in the pattern history table (PHT), only one of
the branches can be predicted correctly. Thus prediction accuracy will never reach 100%. Explain
how using local history registers instead of the global history register will help bring the prediction
accuracy up to 100% during the steady state, by showing what each PHTE will saturate to.

For the outer loop, we will keep observing all Ts, and the counters will be set to 2’b11 for
TT and lead to 100% accuracy for this branch.
The second branch will keep observing this repeated pattern: TNN. So entry TN will be
saturated to 2’b00, entry NN will saturate to 2’b11, and entry NT will saturate to 2’b00.

Final Exam Page 24 of 24


-----

