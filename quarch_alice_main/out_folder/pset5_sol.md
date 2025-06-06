3/2/2021

#### Problem M5.1: Fully-Bypassed Simple 5-Stage Pipeline

**Problem M5.1.A** **Stall**

We still need the logic for stalls, because we cannot prevent load-use hazard. If a load instruction is followed by an
instruction which takes the loaded value as a source operand, we cannot avoid stalling for a cycle. The following
instruction sequence illustrates this hazard.
```
LW R1, 0(R2)  # R1 <- M[R2]
ADD R3, R5, R1  # R1 is a source operand of ADD (data dependency)
          # The correct value of R1 is not available when
          # ADD is in ID stage. So it has to stall for a cycle.

```
**Problem M5.1.B** **Bypass Signal**

Here are the bypass conditions.

Bypass EX->ID ASrc = (rsD=wsE).we-bypassE.re1D

Bypass MEM->ID = (rsD=wsM).weM.re1D

Bypass WB->ID = (rsD=wsW).weW.re1D

Priority: Bypass EX->ID > Bypass MEM->ID > Bypass WB->ID
(In order to execute a given program correctly, the value from the latest producer must be taken if multiple bypass
paths are active.)

**Problem M5.1.C** **Partial Bypassing**

It is an open question and there is no single correct answer. Here are a couple of issues to consider as a guideline.

First, you may consider the penalty for not having all the bypass paths. If we don’t have the bypass path EX→ID,
we have to stall for three cycles for the hazard to be resolved. Likewise, not having MEM→ID results in a stall of
two cycles, and not having WB→ID, in one. Therefore, you can conclude that the bypass path between EX→ID is
the most beneficial.

Secondly, the best bypass path depends on the access patterns of data. The EX→ID bypass path is effective if a
producer instruction is followed by a consumer, except load-use cases (See solution for M5.1.A). On the other hand,
the MEM→ID bypass path works best if there are many load-use cases or many (producer, consumer) pairs have an
independent instruction between them. Likewise, the WB→ID bypass path helps when many (producer, consumer)
pairs are separated by exactly two independent instructions.


-----

3/2/2021

#### Problem M5.2: Basic Pipelining

**Problem M5.2.A** **Mux Control Signals (1)**

### PCEn = (S==Execute)
 IREn = (S==I-Fetch)

#### AddrSrc = Case S
 I-Fetch => PC
 Execute => ALU

**Problem M5.2.B** **Modified pipeline**

A stall can occur in 2 different cases.

1. A structural hazard in the shared memory.

LD R1, 16(R2)
Any instruction following this LD instruction should be stalled.

2. The other is caused by a control hazard, because we don’t have a delay slot.

J 200
Any instruction following this J instruction should be flushed.

**Problem M5.2.C** **Mux Control Signals (2)**

### PCEnable = not ((opcode == LW) or (opcode == SW))

#### AddrSrc = Case opcode
 not (LW or SW) => PC
 (LW or SW) => ALU


-----

3/2/2021


#### IRSrc = Case opcode
 LW or SW or Jump or Brtaken => nop
 Else => Mem

**Problem M5.2.D**

**Time** **PC** **“IR”** **PCenable** **PCSrc1** **AddrSrc** **IRSrc**
```
 t0 I1:100 - 1 pc+4 PC Mem
 t1 I2:104 I1 1 Pc+4 PC Mem
 t2 I3:108 I2 0 * ALU Nop
 t3 I3:108 - 1 pc+4 PC Mem
 t4 I4:112 I3 1 jabs PC Nop
 t5 I7:312 - 1 pc+4 PC Mem
 t6 I8:316 I7 1 pc+4 PC Mem

```
**Problem M5.2.E** **Self-Modifying Code**

The answer is no. The hazard is resolved by the datapath itself because (1) memory accesses are
serialized by the stall logic at the shared memory and (2) memory write takes only one cycle.

**Problem M5.2.F**

Due to this rerouting we will now have to stall even if it is an ALU instruction.

**Problem M5.2.G** **Architecture Comparison**

The Princeton architecture is cheaper than the Harvard architecture, but the Harvard architecture
is faster than the Princeton architecture.

|Time|PC|“IR”|PCenable|PCSrc1|AddrSrc|IRSrc|
|---|---|---|---|---|---|---|
|t 0|I :100 1|-|1|pc+4|PC|Mem|
|t 1|I :104 2|I 1|1|Pc+4|PC|Mem|
|t 2|I :108 3|I 2|0|*|ALU|Nop|
|t 3|I :108 3|-|1|pc+4|PC|Mem|
|t 4|I :112 4|I 3|1|jabs|PC|Nop|
|t 5|I :312 7|-|1|pc+4|PC|Mem|
|t 6|I :316 8|I 7|1|pc+4|PC|Mem|


-----

3/2/2021

#### Problem M5.3: Processor Design (Short Yes/No Questions)

**Problem M5.3.A** **Interlock vs. Bypassing**

**No.** Data dependencies are preserved with either interlocks or bypassing, so the processors
always generate the same results. Bypassing improves performance by eliminating stalls.

**Problem M5.3.B** **Delay Slot**

**Yes. The instruction following a taken branch is executed on processor A, but killed on**
processor B so the processors can generate different results.

**Problem M5.3.C** **Structural Hazard**

**No.** Both processors retrieve the same data values. There is only a performance difference
because processor A must stall an instruction fetch to allow a load instruction to access memory.


-----

3/2/2021

#### Problem M5.4: HAL 180 ISA and 6-Stage Pipelined Implementation (Spring 2015 Quiz 1, Part C)

Inspired by how the IBM 360 uses condition codes, Ben Bitdiddle designs the HAL 180
architecture, which features two flag registers. Table C-1 describes these flags.

**Name** **Description**

Sign Flag (SF) Stores 1 if the result of the last arithmetic or comparison
_instruction was negative, 0 if it was positive_

Zero Flag (ZF) Stores 1 if the result of the last _arithmetic, logical, or_
_comparison instruction was zero, and 0 if it was non-zero_

**Table C-1. HAL 180 status flags.**

Table C-2 summarizes the different instruction types and the flags they read or write. The SF and
ZF columns have an “R” when the instruction reads the status flag, a “W” if it writes the flag
(and does not read it), or a blank if the instruction does not affect the status flag. For example, JL
(jump if less than) reads SF; ADD writes all flags; and JMP (unconditional jump) does not affect
any flag. Some instructions, like CMP, write the status flags but do not return any result.

**Instruction** **Description** **SF** **ZF**

**Arithmetic Instructions**

ADD s1, s2 _s1_ ¬ _s1 + s2_ W W

SUB s1, s2 _s1_ ¬ _s1 - s2_ W W

MUL s1, s2 _s1_ ¬ _s1 × s2_ W W

**Logical Instructions**

AND s1, s2 _s1_ ¬ _s1 & s2_ W

OR s1, s2 _s1_ ¬ _s1 | s2_ W

XOR s1, s2 _s1_ ¬ _s1 ^ s2_ W

**Comparison Instructions**

CMP s1, s2 _temp_ ¬ _s1 - s2_ W W

**Jump Instructions**

JMP target jump to the address specified by target

JL target jump to target if SF == 1 R

JG target jump to target if SF == 0 and ZF == 0 R R

**Memory Instructions**

LD s1, s2 _s1¬ M[s2]_

ST s1, s2 M[s1] ¬ _s2_

**Table C-2. HAL 180 instruction set.**

|Name|Description|
|---|---|
|Sign Flag (SF)|Stores 1 if the result of the last arithmetic or comparison instruction was negative, 0 if it was positive|
|Zero Flag (ZF)|Stores 1 if the result of the last arithmetic, logical, or comparison instruction was zero, and 0 if it was non-zero|

|Instruction|Description|SF|ZF|
|---|---|---|---|
|Arithmetic Instructions||||
|ADD s1, s2|s1 ¬ s1 + s2|W|W|
|SUB s1, s2|s1 ¬ s1 - s2|W|W|
|MUL s1, s2|s1 ¬ s1 × s2|W|W|
|Logical Instructions||||
|AND s1, s2|s1 ¬ s1 & s2||W|
|OR s1, s2|s1 ¬ s1 | s2||W|
|XOR s1, s2|s1 ¬ s1 ^ s2||W|
|Comparison Instructions||||
|CMP s1, s2|temp ¬ s1 - s2|W|W|
|Jump Instructions||||
|JMP target|jump to the address specified by target|||
|JL target|jump to target if SF == 1|R||
|JG target|jump to target if SF == 0 and ZF == 0|R|R|
|Memory Instructions||||
|LD s1, s2|s1¬ M[s2]|||
|ST s1, s2|M[s1] ¬ s2|||


-----

3/2/2021

Ben also designs a 6-stage pipelined implementation of the HAL 180. In this pipeline, the ALU
takes three pipeline stages (E1, E2, and E3), and status flags are updated in stage E3. Table C-3
describes each stage, and Figure C-4 shows the datapath of this 6-stage pipelined architecture,
highlighting the differences with a conventional MIPS pipeline. Note that this implementation
**does not have any data bypass paths.**

**Stage** **Description**

Fetch an instruction from the instruction memory, decode the

Fetch and Decode instruction, and fetch the register values from the register file.

Stage (FD) The status flag checking for conditional jumps is also done in

this stage.

The first stage of the execution phase. Generate partial results
Execute Stage 1 (E1)
and store them in the pipeline registers.

The second stage of the execution phase. Generate partial
Execute Stage 2 (E2)
results and store them in the pipeline registers.

The final stage of the execution phase. Final results are
Execute Stage 3 (E3)
generated and flag registers get updated if necessary.

Memory Stage (M) Perform load/store from/to the data memory if necessary.

Writeback Stage (WB) Write to the register file if necessary.

**Table C-3. HAL 180 pipeline stages.**

|Stage|Description|
|---|---|
|Fetch and Decode Stage (FD)|Fetch an instruction from the instruction memory, decode the instruction, and fetch the register values from the register file. The status flag checking for conditional jumps is also done in this stage.|
|Execute Stage 1 (E1)|The first stage of the execution phase. Generate partial results and store them in the pipeline registers.|
|Execute Stage 2 (E2)|The second stage of the execution phase. Generate partial results and store them in the pipeline registers.|
|Execute Stage 3 (E3)|The final stage of the execution phase. Final results are generated and flag registers get updated if necessary.|
|Memory Stage (M)|Perform load/store from/to the data memory if necessary.|
|Writeback Stage (WB)|Write to the register file if necessary.|


-----

3/2/2021


-----

3/2/2021

**Problem M5.4.A**

Write the HAL 180 assembly for the following program. For maximum credit, use the minimum number of comparison and jump
instructions.


if (a < b) {
c = c XOR b;
} else if (a > b) {
c = c XOR a;
} else {
c = 0;
}
a = 0;
b = 0;


Assume variables a, b, and c are stored in registers R1, R2, and R3 respectively.

|Col1|CMP|R1, R2|
|---|---|---|
||JL|_L1|
||JG|_L2|
||XOR|R3, R3|
||JMP|_L3|
|_L1:|XOR|R3, R2|


-----

3/2/2021

#### JMP _L3

 _L2: XOR R3, R1

 _L3: XOR R1, R1

 XOR R2, R2

**Problem M5.4.B**

Ben’s HAL 180 6-stage pipeline (Figure C-4) stalls to avoid data hazards through registers, but does not yet handle hazards due to
status flags. To illustrate why this is problematic, consider the following instruction sequence:

#### I0: ADD R1, R2 Set SF = 1 ZF = 0
 I1: JG _L2 Not Taken
 I2: XOR R1, R3 Set ZF = 0
 I3: JL _L2 Taken
 I4: _L1: SUB R1, R2
 I5: _L2: ADD R3, R1

Assume that when the program start, R1 = -1, R2 = -2, R3 = -3, and all the status flags are zero. Fill out the following instruction flow
diagram to incur the minimum amount of stalls while maintaining correct operation (i.e., use stalls to respect both data and status flag
dependences). Use “X”s to denote pipeline bubbles.

|Col1|JMP|_L3|
|---|---|---|
|_L2:|XOR|R3, R1|
|_L3:|XOR|R1, R1|
||XOR|R2, R2|


-----

3/2/2021

|Col1|T0|T1|T2|T3|T4|T5|T6|T7|T8|T9|
|---|---|---|---|---|---|---|---|---|---|---|
|FD|I0|I1|I1|I1|I1|I2|I3|I5|||
|E1||I0|X|X|X|I1|I2|I3|I5||
|E2|||I0|X|X|X|I1|I2|I3|I5|
|E3||||I0|X|X|X|I1|I2|I3|
|M|||||I0|X|X|X|I1|I2|
|W||||||I0|X|X|X|I1|


-----

3/2/2021

**Problem M5.4.C**

Let’s fix Ben’s implementation by extending the existing stall control signal, which already works for register hazards, to also stall on
status flag hazards.

First, derive the stall conditions for the different jumps: `JMPstall,` `JLstall, and` `JGstall. Use` `OpcodeX(Y)` to indicate the
condition when the instruction in X stage is Y. Y can be a specific instruction or an instruction class (see Table C-2). For example:
```
     OpcodeFD(JG): if the instruction in the FD stage is a JG instruction.
   OpcodeE1(Logic): if the instruction in the E1 stage belongs to the logical

```
instruction class (e.g. OR).
```
 OpcodeE2(CMP|Arith): if the instruction in the E2 stage is a CMP instruction or

```
belongs to the arithmetic instruction class.
```
 JMPstall =  0
 JGstall = OpcodeE1(logic|Arith|CMP)|OpcodeE2(logic|Arith|CMP)|
      OpcodeE3(logic|Arith|CMP)
 JLstall =  OpcodeE1(Arith|CMP)|OpcodeE2(Arith|CMP)|
      OpcodeE3(Arith|CMP)

```
Finally, write down the new stall signal (stall’) by using the old stall signal (stall) and stall conditions you derive.


-----

3/2/2021
```
stall’ = stall | (OpcodeFD(JL) & JLstall) | 
      (OpcodeFD(JG) & JGstall)| 

```
**Problem M5.4.D**

Does this 6-stage pipeline add more challenges to precise exception handling? If so, please explain.

Yes. Since the status flags are set in E3 stages, you will need some mechanism to roll back in order to handle exceptions after E3
stages.


-----

3/2/2021

#### Problem M5.5: Pipelined Cache Access

**Problem M5.5.A**

Ben’s initial datapath design is shown below:

I-Cache I-Cache I-Cache Instruction Execute D- D- D- WriteAddress Array Tag Decode & Cache Cache Cache back
Decode Access Check Register Address Array Tag

Fetch Decode Access Check

Alyssa suggests combining the third and fourth stages, which would result in the following
design (used in the MIPS R4000 processor discussed in Appendix A of the textbook):

I-Cache I-Cache I-Cache Execute D-Cache D-Cache D-Cache WriteAddress Array Tag Address Array Tag Back
Decode Access Check, Decode Access Check

Instruction
Decode &
Register
Fetch

This scheme allows an instruction to be read from the register file before it is known whether the
instruction is valid. However, reading values from the register file does not affect processor state
and thus does not affect the correctness of the program execution. If the tag check fails—
meaning that the fetched instruction is invalid—the incorrect instruction can be replaced with a
NOP in the Execute stage, and the processor can wait for the correct instruction to be brought
into the I-cache.

That raises the question of whether Ben can similarly combine the data cache tag check stage
with the write-back stage. Theoretically, the answer is yes, although the issues involved with
combining these two stages make it highly impractical. Thus, both answers are acceptable—the
important thing to consider is the reasoning used. Combining the last two stages would result in
the following pipeline:

I-Cache I-Cache I-Cache Execute D-Cache D-Cache D-Cache
Address Array Tag Check, Address Array Tag Check
Decode Access Instruction Decode Access & Write
|I-Cache Address Decode|I-Cache Array Access|I-Cache Tag Check|Instruction Decode & Register Fetch|Execute|D- Cache Address Decode|D- Cache Array Access|D- Cache Tag Check|Write- back|
|---|---|---|---|---|---|---|---|---|

|I-Cache Address Decode|I-Cache Array Access|I-Cache Tag Check, Instruction Decode & Register Fetch|Execute|D-Cache Address Decode|D-Cache Array Access|D-Cache Tag Check|Write- Back|
|---|---|---|---|---|---|---|---|

|I-Cache Address Decode|I-Cache Array Access|I-Cache Tag Check, Instruction Decode & Register Fetch|Execute|D-Cache Address Decode|D-Cache Array Access|D-Cache Tag Check & Write- Back|
|---|---|---|---|---|---|---|


-----

3/2/2021

The obvious problem with this scheme is that a load instruction that misses in the data cache will
write an incorrect value into the register file—therefore merging the stages does not work. This
is correct. However, one can also argue that the scheme can be made to work by modifying the
pipeline. This argument is based on the fact that even if a load instruction places incorrect data
into a register, the load can re-execute and place the correct data into the register, overwriting the
wrong value. As a side note, it should be pointed out that allowing processor state to be
incorrectly updated in a machine which implements precise interrupts would not work without
substantial hardware modifications. However, ignoring the issue of interrupts (which had not
been covered in lecture at the time of the problem set), there is a more fundamental issue with
this approach. Ben’s pipeline currently has no means of correctly re-executing the load
instruction. Simply flushing the pipeline on a data cache miss and restarting execution with the
load instruction does not work because of the following type of instruction:
```
LW R1, 0(R1)

```
If the load results in a D-cache miss, it will have overwritten the value in R1 before it reexecutes, meaning that the incorrect address will be calculated the second time around. Another
alternative is to store the address once it has been calculated in the Execute stage. This requires
special address registers in each pipeline stage starting with D-Cache Address Decode. But
another problem is the fact that cache access is pipelined, so a load in the write-back stage that
has caused a D-cache miss has to be sent backwards in the pipeline (along with the correct
address) in order to access the cache once the correct data has been fetched. This requires
additional bypass paths in the processor. In general, speculatively updating processor state
requires rollback mechanisms to be implemented. Backing up the pipeline is the approach used
in the MIPS R4000 in the event of a data cache miss, but the tag check and write-back stages are
separate.

**Problem M5.5.B**

Ben’s current design does not work for data writes because the tag needs to be checked before
the cache is updated. One solution is to add a fourth stage which handles the actual write in the
event of a cache hit. However, unless the cache can handle two simultaneous accesses, this
scheme does not allow a store to be in this fourth stage at the same time that another memory
operation is in the D-Cache Array Access stage. A better solution is to use a delayed write buffer
(also see Problem M5.6). The store data is written into the write buffer, and if a hit occurs in the
D-Cache Tag Check stage, the data will be written into the cache at a later time (for example,
when the next store instruction is processed)—the processor can continue execution as normal.
This requires load instructions to check the write buffer as well as the cache to ensure that the
correct value is read. With this scheme, a three-stage pipeline can be maintained for the data
cache.

**Problem M5.5.C**

Ben’s final 8-stage pipeline is shown below:


-----

3/2/2021

I-Cache I-Cache I-Cache Execute D-Cache D-Cache D-Cache WriteAddress Array Tag Address Array Tag Back
Decode Access Check, Decode Access Check

Instruction
Decode &
Register
Fetch

This pipeline uses direct-mapped instruction and data caches. Replacing these direct-mapped
caches with set-associative caches could potentially reduce the miss rate, at a possible cost in hit
time. However, a close examination of the pipeline and the diagram for a set-associative cache
(seen in Problem M2.1.B) shows that the I-cache must be direct-mapped. For a set-associative
cache, when a word is being read, the result of the tag check is used as an enable signal for the
value being read. However, in the above pipeline, the instruction is needed at the beginning of
the I-Cache Tag Check stage so that it can be decoded in parallel with the tag check. Thus, the Icache must be direct-mapped.

For the data cache, the tag check occurs in its own stage. This makes it possible to use a setassociative cache, since the data for a load instruction isn’t needed until the beginning of the
Write-Back stage. However, in practice this would probably be a bad idea, since the extra delay
required to wait for the tag check before driving out the data might lengthen the clock period.

**Problem M5.5.D**

Pipelining the caches has a harmful effect on branches. If conditional branch instructions resolve
in the Execute stage, then the processor’s branch delay is 3 cycles, as shown by the following
example in which there are no delay-slot instructions and the datapath is fully-bypassed:
```
  ADDI R1, R0, #1
  BEQ R1, R0, L1
  SUB R2, R3, R4
L1: AND R5, R6, R7

```
**t1** **t2** **t3** **t4** **t5**

|I-Cache Address Decode|I-Cache Array Access|I-Cache Tag Check, Instruction Decode & Register Fetch|Execute|D-Cache Address Decode|D-Cache Array Access|D-Cache Tag Check|Write- Back|
|---|---|---|---|---|---|---|---|

|Col1|t1|t2|t3|t4|t5|
|---|---|---|---|---|---|
|IAD|BEQ||||SUB|
|IAA|ADDI|BEQ||||
|ITC/ID||ADDI|BEQ|||
|EX|||ADDI|BEQ||
|DAD||||ADDI|BEQ|
|DAA|||||ADDI|
|DTC||||||
|WB||||||


-----

3/2/2021

**Problem M5.5.E**

Since a data cache access takes 3 cycles, it will take more cycles (as compared to the five-stage
pipeline) to obtain the result of a load instruction. If an instruction depends on the load, a simple
scheme is to wait until after the D-Cache Tag Check stage before bypassing the load value. This
will ensure that the dependent instruction does not execute with incorrect data. An interlock can
be used to implement this solution. If an instruction in the Instruction Decode stage needs to read
the result of a load instruction that is either in the Execute, D-Cache Address Decode, D-Cache
Array Access, or D-Cache Tag Check stages, then that dependent instruction will be stalled until
the load reaches the Write-Back stage (at which point the load value will be bypassed to the
Execute stage). This is illustrated by the below example.
```
LW R1, 0(R2)
ADD R3, R1, R2

```
**t1** **t2** **t3** **t4** **t5** **t6** **t7**

IAD ADD

**IAA** LW ADD

**ITC/ID** LW ADD ADD ADD ADD

**EX** LW ADD

**DAD** LW

**DAA** LW

**DTC** LW

**WB** LW

As shown by the above resource usage diagram, the load delay for this scheme is 3 cycles.

**Problem M5.5.F**

Another alternative to waiting until after the D-Cache Tag Check stage before bypassing the load
value is to bypass the value at the end of the D-Cache Array Access stage. If there is a tag
mismatch, the processor will wait for the correct data to be brought into the cache; then it will reexecute the load and all of the instructions behind it in the pipeline. In order to implement this
scheme, only the program counter of the load instruction needs to be saved in the event of a tag
mismatch. The load instruction will be nullified (as well as instructions behind it in the pipeline).
When the DataReady signal is asserted (indicating that the load data is now available in the
cache), the processor can restart the load instruction and continue as normal. The benefit of this
scheme is that the load delay is now reduced to 2 cycles.

|Col1|t1|t2|t3|t4|t5|t6|t7|
|---|---|---|---|---|---|---|---|
|IAD|ADD|||||||
|IAA|LW|ADD||||||
|ITC/ID||LW|ADD|ADD|ADD|ADD||
|EX|||LW||||ADD|
|DAD||||LW||||
|DAA|||||LW|||
|DTC||||||LW||
|WB|||||||LW|


-----

3/2/2021

**Problem M5.5.G**

Even with the scheme in Problem M5.5.F, the load delay is 2 cycles, while it was only 1 cycle in
the original 5-stage pipeline (although to be fair, the cycle time should be shorter in the 8-stage
pipeline). One solution to this problem is the addition of a fast-path cache that can be accessed in
one cycle. The resulting pipeline is shown below.

I-Cache I-Cache I-Cache Execute Fast-Path Slow- Slow-Path WriteAddress Array Tag Check, D-Cache Path D-Cache Back
Decode Access Instruction Access and D-Cache Tag Check

Decode & Tag Check Array
Register & Slow Access
Fetch Path

D-Cache
Address
Decode

The benefit of this approach is that a load instruction that hits in the fast-path cache will now
have its value available at the end of the Slow-Path D-Cache Address Decode stage, whereas
before it wasn’t available until the end of the Slow-Path D-Cache Array Access stage. We can
re-examine the instruction sequence from the solution to Problem M5.5.E:
```
LW R1, 0(R2)
ADD R3, R1, R2

```
If the fast-path cache always hits, the load delay will only be 1 cycle, which saves 1 cycle over
the scheme from Problem M5.5.F and 2 cycles over the scheme from Problem M5.5.E. This
scheme differs from having a single D-cache in the original 5-stage pipeline because the fastpath cache will be very small in order to avoid lengthening the cycle time. The idea is to keep the
low miss rate of a large primary cache, the shorter cycle time available with a pipelined cache,
and the single-cycle load delay associated with an unpipelined cache.

|I-Cache Address Decode|I-Cache Array Access|I-Cache Tag Check, Instruction Decode & Register Fetch|Execute|Fast-Path D-Cache Access and Tag Check & Slow Path D-Cache Address Decode|Slow- Path D-Cache Array Access|Slow-Path D-Cache Tag Check|Write- Back|
|---|---|---|---|---|---|---|---|


-----

3/2/2021

#### Problem M5.6: Write Buffer for Data Cache (2005 Fall Part C)

**Problem M5.6.A**

Little’s law: T = 1 / (20*2) = 1 / 40
L = 100
Therefore, N = T*L = 2.5 (entries on average)

**Problem M5.6.B**

**Stall = ( Popcount(Wbuf) >= (N – 2) ) . (IR == Store)**

If you assume that you can figure out the number of store instructions in flight by decoding the
IR in each stage, you will be able to eliminate (-2) in the answer above.

**Problem M5.6.C**

**Stall = ( Popcount(WBuf) + Popcount(Pipeline) >N )**

If you assume in the previous question that you can figure out the number of store instructions in
flight by decoding the IR in each stage, you may conclude the optimization does not make any
change.


-----

3/2/2021

#### Problem M5.7: Instruction Pipelining (Spring 2016 Quiz 1, Part C)

Consider the following MIPS code sequence:

I1  LW R1, 0(R3)

I2  XOR R1, R1, R4
I3 MUL  R2, R1, R4

I4 LW R4, 5(R2)

I5 XOR R4, R4, R5

I6 SW R2, 0(R3)

**Problem M5.7.A**

Assume the classic 5-stage MIPS pipeline as discussed in lecture, with full bypassing and
correct stall logic. Which instructions in the above sequence would have to stall?

I2, I5 will stall due to load-to-use hazards.

Ben is unhappy with the performance of the classic 5-stage MIPS pipeline discussed in 6.823
lectures. Ben uses the L-MIPS ISA, presented in the L-MIPS handout, and pipelines the singlecycle L-MIPS datapath in the handout as shown in the figure below. This is also a 5-stage
pipeline, with the following stages: instruction fetch (F), instruction decode and register file fetch
(D), address generation (A), memory access (M), and execute + write-back (X) stages. We will
**ignore branches and jumps for all following questions.**


-----

3/2/2021

stall

0x4 nop IR _A_ IR _M_ IRX

Add

31

we

rs1
rs2

addr _D_ rd1 A we

inst IR wswd rd2 0 **+** Y addrrdata A

Inst GPRs B
Memory Data

Imm Memory B
Ext wdatawdata

MD1 MD2

MD3

**Problem M5.7.B**

Using the new class of Load-ALU instructions available in L-MIPS, rewrite the assembly
sequence to produce a code sequence with minimum number of instructions. Do not change the
order of any operations as you do this.

I1: XORM R1, 0(R3), R4
I2: MUL R2, R1, R4
I3: XORM R4, 5(R2), R5
I4: SW  R2, 0(R3)

|Col1|PC|Col3|
|---|---|---|

|we rs1 rs2 rd1 ws wd rd2 GPRs|Col2|
|---|---|

|addr inst Inst Memory|IR|
|---|---|


-----

3/2/2021

**Problem M5.7.C**

Complete the instruction flow diagram for the new sequence of instructions for Ben’s pipelined L-MIPS processor. Assume no
**bypassing and correct stall logic. (In case you need it, page 18 has an extra/scratch instruction flow diagram.)**

|0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|I1|F|D|A|M|X|||||||||||||||
|I2||F|D|D|D|D|A|M|X|||||||||||
|I3|||F|F|F|F|D|D|D|D|A|M|X|||||||
|I4|||||||F|F|F|F|D|A|M|X||||||
|I5||||||||||||||||||||
|I6||||||||||||||||||||
|I7||||||||||||||||||||
|I8||||||||||||||||||||


-----

3/2/2021


**Problem M5.7.D**


Ben wants to improve performance by adding bypass paths to his pipeline. Help Ben by
indicating which locations he needs to insert bypass multiplexers. Ignore any bypasses needed
**for control-flow instructions.**

|Col1|PC|Col3|
|---|---|---|

|we rs1 rs2 rd1 ws wd rd2 GPRs|Col2|
|---|---|

|addr inst Inst Memory|IR|
|---|---|

|From|To|
|---|---|
|9|8|
|9|10|
|9|5|
|9|6|
|9|11|
|9|2|
|||

|From|To|
|---|---|
|8|5|
|8|6|
|8|11|
|8|2|
|||
|||
|||


-----

3/2/2021

**Problem M5.7.E**

Complete the instruction flow diagram for the new sequence of instructions for the L-MIPS pipeline. Assume full bypassing and
correct stall logic this time. Use arrows to show forwarding of values from one stage to another. (In case you need it, page 18 has an
extra/scratch instruction flow diagram.)

|0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|I1|F|D|A|M|X|||||||||||||||
|I2||F|D|A|M|X||||||||||||||
|I3|||F|D|D|D|A|M|X|||||||||||
|I4||||F|F|F|D|A|M|X||||||||||
|I5||||||||||||||||||||
|I6||||||||||||||||||||
|I7||||||||||||||||||||
|I8||||||||||||||||||||


-----

3/2/2021

**Problem M5.7.F**

Is it possible to reorder the instructions in your code sequence (without affecting correctness) to
improve performance in the fully-bypassed L-MIPS pipeline? If so, give the reordered code
sequence and explain why. Otherwise, briefly explain why this is not possible.

I1: XORM R1, 0(R3), R4
I2: MUL R2, R1, R4
I3: XORM R4, 5(R2), R5
I4: SW  R2, 0(R3)

Instructions I3 and I4 in the above sequence may be re-ordered without affecting correctness.
Note that both I3 and I4 have a dependence on I2. However, I3 requires the value from I2 in the
decode stage (D), whereas I4 requires the value from I2 only in the address generation stage (A).

I1’: XORM R1, 0(R3), R4
I2’: MUL R2, R1, R4
I3’: SW  R2, 0(R3)
I4’: XORM R4, 5(R2), R5

The re-ordered sequence of instructions completes one cycle earlier as shown in the diagram
below. I3’ proceeds to the address generation stage one cycle earlier as compared to I3. We
engage suitable bypass paths (9 à 6, 9 à 2) from I2’ to I3’ and I4’.

|0 1 2 3 4 5 6 7 8|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|I1’|F|D|A|M|X|||||
|I2’||F|D|A|M|X||||
|I3’|||F|D|A|A|M|X||
|I4’||||F|D|D|A|M|X|


-----

