Name:


# CS232 Midterm Exam 2 April 9, 2001

Mini-Me



- This exam has 8 pages, including this cover.

- There are four questions, each worth 25 points.

- You have 50 minutes. Budget your time!

- No written references or calculators are allowed.

- To make sure you receive full credit, write clearly and show your work.

- We will not answer questions regarding course material.

|Question|Maximum|Your Score|
|---|---|---|
|1|25|25|
|2|25|25|
|3|25|25|
|4|25|25|
|Total|100|100|


-----

**Question 1: Single-cycle datapath**

Let’s say we want to execute the following immediate addition instruction in the single-cycle datapath:

addi $29, $29, 16

The single-cycle datapath diagram below shows the execution of this instruction. Several of the datapath
values are filled in already. You are to provide values for the twelve remaining signals in the diagram, which
are marked with a ? symbol. (2 points each)

You should:

- Write your answers directly on the diagram, but write clearly.

- Show decimal values.

- Assume register $29 initially contains the number 129.

- If a value cannot be determined, mark it as ‘X.’

_Notice that we didn’t actually discuss immediate arithmetic instructions in lecture. However, it’s pretty_
_straightforward with this datapath. This problem is supposed to test your knowledge of the datapath, but it’s_
_possible to fill in values intuitively. For example, you know that the destination register is $29, so the “Write_
_Register” input of the register file should clearly be 29. You are supposed to show as many values as_
_possible, only filling ‘X’s for undeterminable values, but some people used ‘X’ as a don’t care instead._

**2000**

|Col1|Col2|
|---|---|
|||


-----

**Question 2: Multicycle CPU implementation**

We would like to add a “scaled” addressing mode to the MIPS multicycle architecture:

lws rd, rs, rt # rd = Mem[rt + (4 × rs)]

For example, if $a0 contains 1000 and $a1 contains 10, then “lws $t0, $a1, $a0” loads $t0 with the value at
address 1040 (1000 + 4×10).

You need to show the correct control signals necessary to implement the lws instruction, by either:

- completing the finite state machine diagram on page 4, or

- filling in the microprogramming table on page 5.
_You only need to do one or the other, not both._

The multicycle datapath from lecture is shown below, with one important change: the ALUOut register is
connected to the ALUSrcA mux (shown with a dotted line), which now has three inputs instead of two. No
other changes to the datapath are needed.

You may assume that ALUOp = 100 performs an integer multiplication, and 010 performs an addition.

Finally, here is the instruction format, for your reference (shamt and func are not used):

Field op rs rt rd shamt func

Bits 31-26 25-21 20-16 15-11 10-6 5-0

PCWrite

ALUSrcA

PC

IorD

0

RegDst RegWrite

1

MemRead

0 0

**M** Read Read A 2 **ALU** **M**
**u** Address reg 1 data 1 **u**

Zero

**x** **x**

Read ALU

1 **Memory** IRWrite 0 reg 2 Read B Result Out 1

data 2 0

**M** Write

[31-26] 4 1 PCSrc

Write Mem **u** register
data Data [25-21] **x** 2 ALUOp

[20-16] Write

1 **Registers** 3

[15-11] data

MemWrite [15-0]

**Instr** 0 ALUSrcB
**register**

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

Complete this finite state machine diagram for the lws instruction, or fill in the microprogramming table on
the next page, but not both!

You can show the control values in either binary or decimal, whichever is more convenient for you.

Branch

Instruction fetch

completion

and PC increment ALUSrcA = 1
Register fetch and Op = BEQ ALUSrcB = 00

IorD = 0 branch computation ALUOp = 110
MemRead = 1 PCSource = 1
IRWrite = 1 PCWrite = Zero
ALUSrcA = 0 ALUSrcA = 0
ALUSrcB = 01 ALUSrcB = 11
ALUOp = 010 ALUOp = 010

R-type Write
PCSource = 0

execution back

PCWrite = 1 Op = R-type ALUSrcA = 1 RegDst = 1

ALUSrcB = 00 MemToReg = 0
ALUOp = func RegWrite = 1

Op = LWS

Effective address
computation

Memory

Op =

write

ALUSrcA = 01 LW/SW ALUSrcA = 1 Op = SW

IorD = 1

ALUSrcB = 01 ALUSrcB = 10

MemWrite = 1

ALUOp = 100 ALUOp = 010

Op = LW

lw register

Memory

write

ALUSrcA = 10 read RegDst = 0

IorD = 1

ALUSrcB = 00 MemToReg = 1

MemRead = 1

ALUOp = 010 RegWrite = 1

RegDst = 1

IorD = 1

MemToReg = 1

MemRead = 1

RegWrite = 1

_See the comments on the next page._


-----

**Question 2 continued**

Fill in this microprogramming table for the lws instruction, or complete the finite state machine diagram on
the previous page, but not both!

You may need to make up new values for some of these fields, but just make sure your intentions are clear.

**ALU** **Register** **PCWrite**

**Label** **Control** **Src1** **Src2** **control** **Memory** **control** **Next**

Fetch Add PC 4 Read PC ALU Seq

Add PC Extshift Read Dispatch 1

BEQ1 Sub A B ALU-Zero Fetch

Rtype1 Func A B Seq

Write ALU Fetch

Mem1 Add A Extend Dispatch 2

SW2 Write ALU Fetch

LW2 Read ALU Seq

Write MDR Fetch

LWS1 Multiply A 4 Seq

ALU
Add B Seq
Out

Read ALU Seq

Write MDR
Fetch
to register rd

_You should only need to add a few symbols such as “Multiply” to get the ALU to multiply, and “ALUOut” to_
_set the value of the expanded ALUSrcA mux._

_Otherwise, the solution here is basically the same as the one on the previous page. The “lws” instruction has_
_a more complicated addressing mode, so two cycles are required to compute the effective address. The first_
_new cycle computes (4 * rs), and the second computes (4 * rs) + rt. The final two stages of the “lws” are_
_almost the same as for the original “lw” instruction, but we need to store in register rd instead of rt._

_Since we’ve split this datapath into five distinct parts, you cannot combine any of the stages of the “lws”_
_instruction together. For example, “Write MDR to register rd” in the microprogram requires an address to_
_be supplied from the ALUOut register, but that must be produced in the previous clock cycle._

_Finally, we said that the intermediate registers A, B, ALUOut and MDR are implicitly written to on every_
_clock cycle. In this situation it’s all right to use B (in “Add ALUOut B”) two cycles after it’s written (in the_
_Register control “Read” stage)—within those two cycles, IR does not change, so none of the inputs to the_
_register file change, so the register file outputs will not change either._

|Label|ALU Control|Src1|Src2|Register control|Memory|PCWrite control|Next|
|---|---|---|---|---|---|---|---|
|Fetch|Add|PC|4||Read PC|ALU|Seq|
||Add|PC|Extshift|Read|||Dispatch 1|
|BEQ1|Sub|A|B|||ALU-Zero|Fetch|
|Rtype1|Func|A|B||||Seq|
|||||Write ALU|||Fetch|
|Mem1|Add|A|Extend||||Dispatch 2|
|SW2|||||Write ALU||Fetch|
|LW2|||||Read ALU||Seq|
|||||Write MDR|||Fetch|
|LWS1|Multiply|A|4||||Seq|
||Add|ALU Out|B||||Seq|
||||||Read ALU||Seq|
|||||Write MDR to register rd|||Fetch|


-----

**Question 3: Pipelining and forwarding**

**Part (a)**
Show or list all of the dependencies in this program. For each dependency, indicate which instructions and
register are involved. (5 points)

## add $8, $5, $5

 add $2, $5, $8

 sub $3, $8, $4

 add $2, $2, $3

_You can draw the dependencies like this, or describe them in words; something like “Source register $8 in_
_the second add and the sub both depend upon $8 in the first instruction,” and so forth._

**Part (b)**
The pipelined datapath on the next page shows the fifth cycle of executing this program, including values for
several of the stages. Fill in the ten remaining values, marked with a ? symbol, in the EX and MEM stages.
(20 points; 2 points each)

Again, please:

- Write your answers directly on the diagram, but write clearly.

- Show decimal values.

- Assume that registers initially contain their number plus 100: $2 contains 102, $8 contains 108, etc.

- Write ‘X’ for any numbers that cannot be determined.

_Your diagram should show the correct value of $8 (210) being forwarded to the second and third_
_instructions; the EX/MEM pipeline should contain 315 (210 + 105), and the ALU’s first input should be 210,_
_not 108._


-----

**Question 3 continued**

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
|||||

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||


-----

**Question 4: Pipelining performance**

IPG FET ROT EXP REN WLD REG EXE DET WRB

1 2 3 4 5 6 7 8 9 10

One CPU manufacturer has proposed the 10-stage pipeline above for a 500MHz (2ns clock cycle) machine.
Here are the correspondences between this and the MIPS pipeline:

 - Instructions are fetched in the FET stage.

 - Register reading is performed in the REG stage.

 - ALU operations and memory accesses are both done in the EXE stage.

 - Branches are resolved in the DET stage.

 - WRB is the writeback stage.

**Part (a)**
How much time is required to execute one million instructions on this processor, assuming there are no
dependencies or branches in the code? (5 points)

_It takes 9 cycles to fill the pipeline, and then 1,000,000 more cycles to complete the instructions, for a total_
_of 1,000,009 * 2 = 2,000,018 ns._

**Part (b)**
_Without forwarding, how many stall cycles are needed for the following code fragment? (5 points)_
lw $t0, 0($a0)
add $v1, $t0, $t0

_The “lw” would not store its result into $t0 until the WRB stage, but that value must be read by the “add,”_
_in its REG stage. The diagram below shows that 2 stall cycles would be necessary. (If you didn’t assume that_
_the register file could be written and read on the same cycle, then a 3-cycle stall is needed.)_

_lw_ _IPG_ _FET_ _ROT_ _EXP_ _REN_ _WLD_ _REG_ _EXE_ _DET_ _WRB_

_add_ _IPG_ _FET_ _ROT_ _EXP_ _REN_ _WLD_ _REG_ _EXE_ _DET_ _WRB_

**Part (c)**
If a branch is mispredicted, how many instructions would have to be flushed from the pipeline? (5 points)

_Branches aren’t resolved until the 9th (DET) stage, at which point there could be eight subsequent_
_instructions in the pipeline. They would all have to be flushed._

**Part (d)**
Assume that a program executes one million instructions. Of these, 15% are load instructions which stall,
and 10% of the instructions are branches. The CPU predicts branches correctly 75% of the time. How much
time will it take to execute this program? (10 points)

_One million instructions would take 1,000,009 cycles, as from Part (a). But now, 25,000 (2.5%) of those_
_instructions will be mispredicted branches, each of which would incur an 8-cycle penalty from flushing._
_Also, each of the 150,000 (15%) stalled loads results in 2 extra cycles. The total cycles is then 1,000,009 +_
(25,000 * 8) + (150,000 * 2) = 1,500,009, for a run time of 3,000,018ns. The performance is about 1.5 times
_worse, which emphasizes the importance of accurate branch prediction and minimizing stalls._

|IPG|FET|ROT|EXP|REN|WLD|REG|EXE|DET|WRB|
|---|---|---|---|---|---|---|---|---|---|

|IPG|FET|ROT|EXP|REN|WLD|REG|EXE|DET|WRB|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||IPG|FET|ROT|EXP|REN|WLD|||REG|EXE|DET|WRB|


-----

