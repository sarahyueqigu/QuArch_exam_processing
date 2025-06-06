# CS232 Midterm Exam 2 April 8, 2002

Name: Frodo Baggins

- This exam has 7 pages, including this cover.

- There are three questions worth a total of 100 points.

- You have 50 minutes. Budget your time!

- No written references or calculators are allowed.

- To make sure you receive full credit, write clearly and show your work.

- We will not answer questions regarding course material.

|Question|Maximum|Your Score|
|---|---|---|
|1|30||
|2|35||
|3|35||
|Total|100||


-----

**Question 1: Single-cycle datapath (30 points)**

Let’s simplify the MIPS instruction set architecture a little by removing the original lw and sw instructions
and replacing them with ones that do not contain a constant offset. Our new loads and stores will have the
following general forms.

lw rt, rs # rt = Mem[rs]
sw rt, rs # Mem[rs] = rt

These are I-type instructions, but you may not make any assumptions about the instructions’ constant fields.

**Part (a)**
Show what changes must be made to the single-cycle datapath below so the new lw and sw instructions can
avoid going through the ALU. Please try to keep your modifications as neat as possible! (10 points)

_Our modified diagram is shown below. Some people used multiplexers to select the memory addresses from_
_either the ALU output or the register file, which is all right. But since the problem says that we are removing_
_the original lw/sw instructions, we could completely eliminate the connections between the ALU and data_
_memory. Instead, we just use Read Data 1 from the register file (representing register rs) as the memory’s_
_Read and Write address inputs._


-----

**Question 1 continued**

**Part (b)**
Fill in the table below to show the correct control signals for the new lw and sw instructions. You must write
‘X’ to indicate any don’t-care conditions. (5 points)

_Since we’re not using the ALU anymore, the related signals should be don’t cares._

RegDst RegWrite ALUSrc ALUOp MemWrite MemRead MemToReg PCSrc

lw _0_ _1_ _X_ _X_ _0_ _1_ _1_ _0_

sw _X_ _0_ _X_ _X_ _1_ _0_ _X_ _0_

**Part (c)**
Assume that memories and the ALU have 2ns delays, and the registers have a 1ns delay. Find the minimum
clock cycle times for both the original single-cycle datapath and your modified one. (5 points)

_These are the same delays we used in some lecture examples. In the original ISA, lw would be the slowest_
_instruction, requiring 8ns total (2ns for instruction fetch, 1ns for reading registers, 2ns for effective address_
_computation, 2ns to read memory, and 1ns for writeback)._

_For our new ISA, lw can avoid the ALU step and complete in just 6ns instead. If you work through the other_
_delays, you’ll see that R-type instructions also require 6ns, while beq and sw need less time._

_The delay of the longest instruction will determine the minimum clock cycle time, so that would be 8ns in the_
_original system and 6ns with the modified lw/sw instructions._

**Part (d)**
What general conclusions can you draw, if any, about the performance of the original processor as compared
to your modified one? (10 points)

_In a single-cycle machine, each instruction takes one cycle to execute. By lowering the cycle time from 8ns_
_to 6ns, it seems like performance will always improve. However, we shouldn’t forget to think about the other_
_factors that affect performance, such as the number of instructions executed._

_A single lw instruction such as_

_lw_ _$t0, 4($sp)_

_in the original system would require 8ns to execute. In the new ISA though, this would have to be done with_
two instructions, in a total of 12ns:

_addi $sp, $sp, 4_
_lw_ _$t0, $sp_

_So if the original code contains many memory accesses with constant offsets, its equivalent code with the_
_simplified instruction set may actually take more time!_

|Col1|RegDst|RegWrite|ALUSrc|ALUOp|MemWrite|MemRead|MemToReg|PCSrc|
|---|---|---|---|---|---|---|---|---|
|lw|0|1|X|X|0|1|1|0|
|sw|X|0|X|X|1|0|X|0|


-----

**Question 2: Multicycle CPU implementation (35 points)**

MIPS is a register-register architecture, where arithmetic source and destinations must both be registers. But
let’s think about including a register-memory addition instruction.

addm rd, rs, rt # rd = rs + Mem[rt]

In other words, register rt contains a memory address which is read to produce the ALU’s operand. The
instruction format is given here for your reference (shamt and func are not used).

Field op rs rt rd shamt func

Bits 31-26 25-21 20-16 15-11 10-6 5-0

It is possible to include addm in a multicycle processor by modifying the datapath and control unit presented
in class. Your implementation of addm should not need more than five stages for execution, and you should
be careful not to modify any registers other than rd.

**Part (a)**
The multicycle datapath from lecture appears below. Show the changes needed to support addm. Try to keep
your diagram neat! (10 points)

_Here we’ve connected the intermediate register B to the memory unit so we can read from address rt. We_
_also feed MDR (which will contain Mem[rt]) into the ALU, for addition with register rs. These are probably_
_the simplest set of changes; the control unit on the next page shows the details of how to get this to work._

PCWrite

ALUSrcA

PC

IorD

0

RegDst RegWrite **M**

MemRead **u**

0 0

**x**

Read Read **M**

A 1 **ALU**

**1** Address reg 1 data 1 **u**

Zero

**x**

Read ALU

**2** **Memory** IRWrite 0 reg 2 Read B Result Out 1

data 2 0

**M** Write

[31-26] 4 1 PCSrc

Write Mem **u** register
data Data [25-21] **x** 2 ALUOp

[20-16] Write

1 **Registers** 3

[15-11] data

MemWrite [15-0] 4

**Instr** 0
**register** ALUSrcB

**M**
**u** **Sign** **Shift**

**Memory** **x** **extend** **left 2**
**data**

1

**register**

MemToReg

|Field|op|rs|rt|rd|shamt|func|
|---|---|---|---|---|---|---|
|Bits|31-26|25-21|20-16|15-11|10-6|5-0|

|Col1|Col2|
|---|---|
|PC||


-----

**Question 2 continued**

**Part (b)**
Complete this finite state machine diagram for the addm instruction. Control values not shown in each stage
are assumed to be 0. Remember to account for any control signals that you added or modified in the previous
part of the question. (25 points)

Branch

Instruction fetch

completion


-----

**Question 3: Forwarding and stalling (35 points)**

**Part (a)**
Show or list all of the dependencies in the following code fragment. Make sure that you clearly indicate
which instructions and registers are involved in each dependency. (5 points)


_Lots of dependencies here!_
_Register $8 is read and_
_written several times, as_
_shown with the blue circles_
_and arrows. There is also a_
_dependency between the_
_third and fourth_
_instructions involving $6._

_Note that $8 is written to in_
_both the first and second_
_instructions. We didn’t talk_
_about this kind of “write_
_after write” dependency in_
_class, so it’s all write if you_
_did or didn’t show it._


## add $8, $5, $5

 sub $8, $8, $10

 lw $6, 4($8)

 add $4, $6, $8


**Part (b)**
The pipelined datapath on the next page shows the fifth cycle of executing this program. Fill in the correct
datapath values for the fifteen question mark symbols ? in the diagram. There is one ? in the IF stage, three
in the ID stage, eight in EX, two in MEM, and one in WB. (30 points; 2 points each)

- Assume that registers initially contain their number plus 100: $6 contains 106, $8 contains 108, etc.

- Write your values directly on the diagram, but please write clearly.

- Use decimal notation. You may write ‘X’ for any values that cannot be determined.

_Since the datapath on the next page shows forwarding and hazard units as discussed in class, we can assume_
_that dependencies between the first three instructions will be resolved correctly. For example, your answer_
_should show the correct value of $8 being forwarded from the sub instruction in the MEM stage to the lw in_
_the EX stage._

_A load stall is required between the third and fourth instructions; the hazard unit should detect this situation_
_and output the appropriate control signals to force a stall. Notice that the register file outputs in the ID_
_stage are an incorrect, old value for $6 and an incorrect, new value for $8. (The first add instruction is_
_writing 210 to $8 in this cycle, but the sub result isn’t available yet.)_


-----

**Question 3 continued**

|110|Col2|
|---|---|

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||
||||||||||||||||||
||||108||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||


-----

