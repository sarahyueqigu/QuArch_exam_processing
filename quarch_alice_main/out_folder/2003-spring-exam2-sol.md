# CS232 Midterm Exam 2 Solutions
 April 14, 2003

Name: Pooh

� This exam has 7 pages including the pipelined datapath diagram on the last
page, which you are free to tear off.
� You have 50 minutes, so budget your time carefully!
� No written references or calculators are allowed.
� To make sure you receive credit, please write clearly and show your work.
� We will not answer questions regarding course material.

|Question|Maximum|Your Score|
|---|---|---|
|1|35||
|2|30||
|3|35||
|Total|100||


-----

Consider extending the MIPS architecture with the instruction below, which loads two consecutive words of
data from memory and stores them into two destination registers.

ld rt, rd, rs # rt = Mem[rs]; rd = Mem[rs + 4]

This will use the same format as R-type instructions, shown here for reference (shamt and func are not used).

Field op rs rt rd shamt func

Bits 31-26 25-21 20-16 15-11 10-6 5-0

**Part (a)**
The multicycle datapath from lecture appears below. Show what changes are needed to support ld. You should
not need to modify the main functional units (the memory, register file and ALU), but you can make any other
changes or additions necessary. Try to keep your diagram neat! (10 points)

_The ld instruction can be split into several smaller single-cycle operations: fetch and decode the instruction_
_(as usual), read Mem[rs] and store it into register rt, compute rs + 4, and read Mem[rs + 4] and store that_
_into rd. There are a few possible solutions, so we’ll just show one of them. The sole datapath change we’ll_
_make is to connect A, which contains the value of register rs, to the memory’s address input to let us read_
_Mem[rs]. The IorD mux is expanded appropriately._

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

1 Address reg 1 data 1 **u**

Zero

**x**

2 **Memory** IRWrite 0 Readreg 2 Read B Result ALUOut 1

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

|op|rs|rt|rd|shamt|func|
|---|---|---|---|---|---|

|Col1|Col2|
|---|---|
|PC||
|||


-----

**Part (b)**
Complete this finite state machine diagram for the ld instruction. Control values not shown in each stage are
assumed to be 0. Remember to account for any control signals that you added or modified in the previous part
of the question! (25 points)

Branch

Instruction fetch

completion


-----

Here is a short MIPS assembly language loop. (This is a simpler version
of a very common operation in scientific applications.) Assume that we
run this code on the pipelined datapath shown on page 7.

**Part (a)**
Find the number of clock cycles needed to execute this code, accounting
for all possible stalls and flushes. Assume that $a3 is initially set to 100.
(20 points)


Elvis:

_1_ lw $t0, 0($a1)

_2_ mul $t0, $t0, $a2

_3_ lw $t1, 0($a0)

_4_ add $t0, $t0, $t1

_5_ sw $t0, 0($a0)

_6_ sub $a3, $a3, 1

_7_ addi $a0, $a0, 4

_8_ addi $a1, $a1, 4

_9_ bne $a3, $0, Elvis


_This is very similar to one of the homework problems. First, you should see that the dependencies which may_
_cause a problem are the ones between instructions 1 & 2, 3 & 4 and 4 & 5. Other dependencies, such as the_
_ones between lines 2 & 4 or lines 6 & 9, are too far apart to be potential hazards. The two “lw” dependencies_
_will force a stall, but the dependency in lines 4 & 5 will be resolved by forwarding from the EX/MEM register_
_of the “add” to the EX stage of the “sw.” Also, if we predict that branches are not taken as specified on page_
_7, each execution of “bne” except for the last one will result in a misprediction and one cycle lost to a flush_
_(branches are determined in the ID stage)._

_If you think about stalls and flushes in terms of “nop” instructions like in our Homework 5 solutions, then 12_
_instructions are executed for every loop iteration—there are nine instructions originally, plus two stalls and_
_one flush. So running the loop 100 times involves executing 1199 instructions. (We subtract one since the last_
_“bne” will be predicted correctly and does not result in a flush.) With a five-stage pipeline, 1199 instructions_
_would execute in 1199 + 4 = 1203 clock cycles._

**Part (b)**
Show how you can rearrange the instructions in the code above to eliminate as many stall cycles as possible.
You do not need to reduce the number of flushes. (10 points)

_Again, there are only two stalls in each loop iteration due to the “lw” instructions. The simplest solution is to_
_just swap instructions 2 and 3 of the loop. This will separate the load and use of registers $t0 and $t1 by one_
_extra cycle, which is enough to prevent the stalls. This idea is also very similar to one illustrated in Problem 3_
_of Homework 5, which had two versions of a loop that differed in the number of stalls needed._


-----

Here is a sequence of two instructions, with a dependency between them.

sub $s1, $s2, $s3

beq $s1, $0, Pooh

If we execute this code using the datapath on page 7, where branches are determined in the ID stage, then the
new value of $s1 will be needed in the same cycle in which it is produced, as shown in the diagram below.

sub IF ID EX MEM WB

beq IF ID EX MEM WB

Our datapath doesn’t handle this situation properly because it doesn’t permit forwarding to the ID stage, so let’s
try to fix that.

1. Add multiplexers and a forwarding unit to the ID stage of the datapath on the next page (it’s the same as
the one on page 7). Be sure to show the mux and forwarding unit inputs and outputs clearly.

2. Give forwarding equations to explain how all your mux selections are made.

You can assume the register file and ALU have the same latency while muxes have negligible delays, so you
can forward the ALU output directly to the branch comparator. Also, you only need to consider dependencies
between R-type arithmetic instructions and branches as in the example above.

_See the next page!_

|IF|ID|EX|MEM|WB|
|---|---|---|---|---|

|IF|ID|EX|MEM|WB|
|---|---|---|---|---|


-----

ID/EX.RegisterRt

**Hazard** ID/EX.MemRead

Rs Rt

0

0 0

1 **Control** 1

4

0

**+**

1

**P**

**+**

**C** =

× 4 0

1

R1 1

0

Adrs R2 1

**Registers** 2

**Instr.** Zero

Wr

**RAM**

Data 2 0 Result Adrs

0
1
2 **Data RAM**

1

Data 0

IF.Flush **Ext**

1

Rt

0

EX/Mem.RegRd

Rd 1

FT FS

Rs

Forward **Forward** MEM/WB.RegWrite

MEM/WB.RegisterRd

_This problem is just asking you to apply the ideas of forwarding to a different stage of the pipeline. Our muxes_
_and forwarding unit are shown in red here; note that the setup is very similar to that of the existing forwarding_
_hardware in the EX stage. The branch comparator unit can then compare values from the register file or from_
_the ALU output of the previous instruction, when there is a dependency. The new muxes should be set to 1 only_
_if the ID/EX destination register Rd is the same as one of the ID source registers Rs/Rt. Following the style of_
_the equations shown on page 7:_

if (ID/EX.RegWrite = 1 and IF/ID.RegisterRs = ID/EX.RegisterRd)
then FS = 1

if (ID/EX.RegWrite = 1 and IF/ID.RegisterRt = ID/EX.RegisterRd)
then FT = 1

_Some people included an additional condition to check if the instruction in ID was “beq,” but this shouldn’t be_
_necessary since the Control unit only uses the comparator result for “beq” anyway._

|Col1|Col2|Col3|
|---|---|---|
||EX/Mem.RegWrite Adrs Data RAM Data EX/Mem.RegRd||
||||
||||
|||EX/Mem.RegRd|

|ID/EX.RegisterRt Hazard ID/EX.MemRead IF/ID.Write Write Rs Rt 0 PC 0 0 1 Control 1 4 0 ID/EX.RegWrite EX/Mem.RegWrite + 1 P + C = × 4 0 1 R1 1 0 Adrs R2 1 Registers 2 Instr. Zero Wr RAM Data 2 0 Result Adrs 0 1 2 Data RAM IF/ID ID/EX 1 Data 0 IF.Flush Ext 1 Rt 0 EX/Mem.RegRd Rd 1 EX/MEM MEM/WB FT FS Rs Forward Forward MEM/WB.RegWrite MEM/WB.RegisterRd|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||
||||||||||||ID/EX.RegWrite||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
|||||||||||ID/EX|||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||Rd||||||||||||||||||||
||Rs|||FT|||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||Forward||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||


-----

Here is the final datapath that we discussed in class.

� Forwarding for arithmetic operations is done from the EX/MEM and MEM/WB stages to the ALU.

� A hazard detection unit can insert stalls for lw instructions.

� Branches are assumed to be not taken, and branch determination is done in the ID stage.

� Equations for the ForwardA mux are given below; the ForwardB mux is similar.

ID/EX.RegisterRt


Result


0

1

|Col1|Col2|Col3|
|---|---|---|
||EX/Mem.RegWrite Adrs Data RAM Data EX/Mem.RegRd||
||||
||||
|||EX/Mem.RegRd|


MEM/WB.RegWrite


MEM/WB.RegisterRd

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
|Rd|||||||||
|Rs|||||||||
||||||||||
||||||||||
||||||||||
||||||||||


if (MEM/WB.RegWrite = 1

and MEM/WB.RegisterRd = ID/EX.RegisterRs
and EX/MEM.RegisterRd ≠ ID/EX.RegisterRs)

then ForwardA = 1

if (EX/MEM.RegWrite = 1

and EX/MEM.RegisterRd = ID/EX.RegisterRs)

then ForwardA = 2


-----

