# CS232 Midterm Exam 2 November 12, 2003

Name: Darth Vader

Section: Imperial Star Ship

� This exam has 7 pages including the pipelined datapath diagram on the last
page, which you are free to tear off.
� You have 50 minutes, so budget your time carefully!
� No written references or calculators are allowed.
� To make sure you receive credit, please write clearly and show your work.
� We will not answer questions regarding course material.

|Question|Maximum|Your Score|
|---|---|---|
|1|50||
|2|20||
|3|30||
|Total|100||


-----

Consider extending the MIPS architecture with the instruction below, which adds three registers together and
stores the result in a register.

add3 rd, rs, rt, ru # rd = rs + rt + ru

This will use the same format as R-type instructions---shown here for reference---where the shamt field is used
to hold ru.

Field op rs rt rd shamt/ru func

Bits 31-26 25-21 20-16 15-11 10-6 5-0

An example of the usage of the add3 instruction is shown in part (c) of question 1.

**Part (a)**
The multicycle datapath from lecture appears below. Show what changes are needed to support _add3. You_
should only add wires and muxes to the datapath; do not modify the main functional units themselves (the
memory, register file and ALU). Try to keep your diagram neat! (15 points)

_Note: While we’re primarily concerned about correctness, full points will only be rewarded to solutions that_
_use a minimal number of cycles and do not lengthen the clock cycle. Assume that the ALU, Memory and_
_Register file all take 2ns, and everything else is instantaneous._

PCWrite

ALUSrcA

PC

**_RegSrcB_** **2**

IorD

0

RegDst RegWrite **M**

MemRead **u**

0 0

**x**

**M** Read Read **M**

A 1 **ALU**

**u** Address **1** reg 1 data 1 **u**

Zero

**x** **x**

IRWrite

**0** Read ALU

1 **Memory** 0 reg 2 Read B Result Out 1

0

data 2

**M** Write

[31-26] 4 1 PCSrc

Write Mem **u** register
data Data [25-21] **x** 2 ALUOp

[20-16] Write

1 **Registers** 3

[15-11] data

MemWrite [15-0]

**[10-6]**
**Instr** 0 ALUSrcB
**register**

**M**
**u** **Sign** **Shift**

**Memory** **x** **extend** **left 2**
**data**

1

**register**

MemToReg

|op|rs|rt|rd|shamt/ru|func|
|---|---|---|---|---|---|

|Col1|Col2|
|---|---|
|PC||


-----

**Part (b)**
Complete this finite state machine diagram for the add3 instruction. Control values not shown in each stage are
assumed to be 0. Remember to account for any control signals that you added or modified in the previous part
of the question! (20 points)

Branch

Instruction fetch

completion

|Col1|Memory read IorD = 1 MemRead = 1|Col3|
|---|---|---|
|Memory read IorD = 1 ALUSrcA = 10 MemRead = 1 ALUSrcB = 00 ALUOp = ADD|Memory read IorD = 1 MemRead = 1||
||||


-----

**Part (c)**

The _add3 instruction can be used in place of two dependent add instruction, reducing the number of_
instructions that need to be executed. Below are two functionally equivalent programs; the second of which
uses the add3 instruction:

**Program 1** **Program 2**


**5**

**5**

**5**

**4**

**4**

**4**


lw $t0, 0($a0)
lw $t1, 4($a0)
lw $t2, 8($a0)
add $t3, $t0, $t1
add $t3, $t2, $t3
sw $t3, 0($a1)


**5**

**5**

**5**

**5**

**4**


lw $t0, 0($a0)
lw $t1, 4($a0)
lw $t2, 8($a0)
add3 $t3, $t0, $t1, $t2
sw $t3, 0($a1)


Assuming the datapath and control that you implemented in parts (a) and (b), how much faster (or slower) is
program 2 than program 1? You may leave your answer as a fraction. (10 points)

## Program 2 is faster by 3/24 = 12.5%

**Part (d)**
Implementing the add3 instruction in the pipelined datapath we discussed in class (shown on page 7) would
be much more difficult. Give two specific reasons why. (5 points)

# There are two main structural hazards

 •The ALU is used twice (would need a second adder)

 •There are 3 register reads (would need a 3[rd] read port)


-----

The pipeline datapath diagram on page 7 (feel free to tear it off) has a number of wires/buses annotated. For
each annotation (5 points per annotation):

  - describe the purpose of the wire/bus and

  - give an instruction or (instruction sequence) that requires it.

# Purpose:This bus sends PC+4 back to MUX that

**1** updates PC

# Instr: Everyone in IF stage e.g.,

 add $a1,$t1, $s1

 Purpose:This bus sends extended immediate value to

**2**

# ALU

 Instr: lw and sw and addi e.g.,

 lw $t1, 8($a0)

 Purpose:Data Bus to send Data to Memory

**3**

# Instr: Stores e.g.,

 sw $a2, 0($t0)

 Purpose:Forward Data from WB stage to EX

**4** stage

# Instr: Any R-Type, Stores and Loads e.g.,

 lw $t1, 0($a0)

 lw $t3, 4($a0)

 add $s1, $t1, $t2


-----

**Part (a)**

instruction latency.
Pipelining primarily improves: (circle one, 5 points)
instruction throughput.

**For parts b, c, and d, refer to the pipelined datapath on page 7.**

**Part (b)**
What is the penalty for taken branches (in number of cycles flushed)? How do you know? (10 points)

**One cycle because branches are determined in ID stage (see the little = box)**

**Also, only the IF register has a flush signal.**

**Part (c)**
Describe (in English) the situations that require a load stall. (5 points)

**Load immediately followed by an instruction uses the result of the load**

**Part (d)**
Complete the control equation for load stalls. Hint: use the forwarding equation as a guide. (10 points)

**if ( ID/EX.MemRead == 1 AND**
**((ID/EX.rt == IF/ID.rs) OR (ID/EX.rt == IF/ID.rt)))**

then PC_Write = 0, IF/ID.Write = 0, and ControlMux = 0

_Note: by default, PC_Write, IF/ID.Write, and ControlMux are 1._


-----

Here is the final datapath that we discussed in class.

- Forwarding is performed from the EX/MEM and MEM/WB latches to the ALU inputs. The control
equation for the Rs register input to the ALU is shown at the bottom of the page. The Rt input is similar.

- Branches are assumed to be not taken.

- A hazard unit inserts stalls for lw instructions

ID/EX.RegisterRt

**Hazard** ID/EX.MemRead

**ControlMux**

Rs Rt

0

0 0

1

1 **Control** 1

4

**+**

**P**

**+**

**C**

×××× 4 **=**

R1 1

0

Adrs

R2 1

**Registers** 2

**Instr.** Zero

Wr

**RAM**

Data 2 0 Result Adrs

|Col1|Col2|Col3|
|---|---|---|
||EX/Mem.RegWrite Adrs Data RAM Data EX/Mem.RegRd||
||||
||||
|||EX/Mem.RegRd|

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


if ((EX/MEM.RegWrite == 1) and
(EX/MEM.RegisterRd == ID/EX.RegisterRs))
then ForwardA = 1
else if ((MEM/WB.RegWrite == 1) and
(MEM/WB.RegisterRd == ID/EX.RegisterRs))
then ForwardA = 2


-----

