3/2/2021

##### Problem M5.1: Fully-Bypassed Simple 5-Stage Pipeline

We have reproduced the fully bypassed 5-stage MIPS processor pipeline from Lecture 7 in
Figure M5.1-A. In this problem, we ask you to write equations to generate correct bypass and
stall signals. Feel free to use any symbol introduced in the lecture.

**Problem M5.1.A** **Stall**

Do we still need to stall this pipeline? If so, explain why. (1) Write down the correct equation for
the stall condition and (2) give an example instruction sequence which causes a stall.

**Problem M5.1.B** **Bypass Signal**

In Lecture 7, we gave you an example of bypass signal (ASrc) from EX stage to ID stage. In the
fully bypassed pipeline, however, the mux control signals become more complex, because we
have more inputs to the muxes in the ID stage.

Write down the bypass condition for each bypass path in Mux 1. Please indicate the priority of
the signals; that is, if all bypass conditions are met, indicate which signals have the highest and
the lowest priorities.

##### Bypass EX->ID ASrc = (rsD=wsE).we-bypassE.re1D (given in Lecture 7)
 Bypass MEM->ID =
 Bypass WB->ID =
 Priority: 

**Problem M5.1.C** **Partial Bypassing**

While bypassing gives us a performance benefit, it may introduce extra logic in critical paths and
may force us to lower the clock frequency. Suppose we can afford to have only one bypass in the
datapath. How would you justify your choice? Argue in favor of one bypass path over another.


-----

3/2/2021

|Col1|PC|Col3|
|---|---|---|

|addr inst Inst Memory|IR|
|---|---|


rdata
###### Data  Memory

wdat


###### PC for JAL, ...


Imm
Ext


### ASrc


0x4


### W


rdata


addr


MD2


31


### E


inst


rd1


rs1


wd rd2


we


PC


IR


IR


A


B


Figure M5.1-A: Fully-Bypassed MIPS Pipeline


###### Inst Memory


### BSrc


wdatwdata


### D


MD1


Add


wd rd2


we


ws


IR


Y


-----

3/2/2021

##### Problem M5.2: Basic Pipelining

Unlike the Harvard-style (separate instruction and data memories) architectures, machines using
the Princeton-style have a shared instruction and data memory. In order to reduce the memory
cost, Ben Bitdiddle has proposed the following two-stage Princeton-style MIPS pipeline to
replace a single-cycle Harvard-style pipeline from our lectures.

Every instruction takes exactly two cycles to execute (i.e., instruction fetch and execute) and
there is no overlap between two sequential instructions; that is, fetching an instruction occurs in
the cycle following the previous instruction’s execution (no pipelining).

Assume that the new pipeline does not contain a branch delay slot. Also, don’t worry about selfmodifying code for now.

**PCen** **PCSrc1** **PCSrc2** **RegWrite** **MemWrite** **WBSrc**

**0x4** **Add**

**Add** **0x4**

**Add**

**clk**

**we**

**clk** **rs1** **clk**

**rs2**

**PC** **31** **rd1** **we**

**IR** **ws** **addr**

**wd [rd2]** **ALU**

**clk** **GPRs** **z** **rdata**

**Data**

**Imm** **Memory**
**Ext** **wdata**

**ALU**

**Control**

**IRen** **OpCode** **RegDst** **ExtSel** **OpSel** **BSrc** **zero?** **AddrSrc**

Figure M5.2-A: Two-stage pipeline, Princeton-style

|Col1|Col2|
|---|---|


-----

3/2/2021

**Problem M5.2.A** **Mux Control Signals (1)**

Please complete the following control signals. You are allowed to use any internal signals (e.g.,
OpCode, PC, IR, zero?, rd1, data, etc.) but not other control signals (ExtSel, IRSrc, PCSrc, etc.).

_Example syntax: PCEn = (OpCode == ALUOp) or ((ALU.zero?) and (not (PC == 17)))_

You may also use the variable S which indicates the pipeline’s operation phase at a given time.
```
      S := I-Fetch | Execute (toggles every cycle)

#### PCEn = 
 IREn = 

##### AddrSrc = Case _____________
 ____________ => PC
 ____________ => ALU

```

-----

3/2/2021

**Problem M5.2.B** **Modified pipeline**

After having implemented his proposed architecture, Ben has observed that a lot of datapath is
not in use because only one phase (either I-Fetch or Execute) is active at any given time. So he
has decided to fetch the next instruction during the Execute phase of the previous instruction.

Figure M5.2-B: Modified Two-stage Princeton-style MIPS Pipeline

Do we need to stall this pipeline? If so, for each cause (1) write down the cause in one sentence
and (2) give an example instruction sequence. If not, explain why. (Remember there is no delay
slot.)


-----

3/2/2021

**Problem M5.2.C** **Mux Control Signals (2)**

Please complete the following control signals in the modified pipeline. As before, you are
allowed to use any internal signals (e.g., OpCode, PC, IR, zero?, rd1, data, etc.) but not other
control signals (ExtSel, IRSrc, PCSrc, etc.)

#### PCEnable = 

##### AddrSrc = Case _____________
 ____________ => PC
 ____________ => ALU
 IRSrc = Case _____________
 ____________ => nop
 ____________ => Mem


-----

3/2/2021

**Problem M5.2.D**

Now we are ready to put Ben’s machine to the test. We would like to see a cycle-by-cycle
animation of Ben’s two-stage pipelined, Princeton-style MIPS machine when executing the
instruction sequence below. In the following table, each row represents a snapshot of some
control signals and the content of some special registers for a particular cycle. Ben has already
finished the first two rows. Complete the remaining entries in the table. Use * for “don’t care”.

Label Address Instruction

|Label|Address|Instruction|
|---|---|---|
|I 1|100|ADD|
|I 2|104|LW|
|I 3|108|J I 7|
|I 4|112|LW|
|I 5|116|ADD|
|I 6|120|SUB|
|I 7|312|ADD|
|I 8|316|ADD|

|Time|PC|“IR”|PCenable|PCSrc1|AddrSrc|IRSrc|
|---|---|---|---|---|---|---|
|t 0|I :100 1|-|1|pc+4|PC|Mem|
|t 1|I :104 2|I 1|1|Pc+4|PC|Mem|
|t 2|||||||
|t 3|||||||
|t 4|||||||
|t 5|||||||
|t 6|||||||


-----

3/2/2021

**Problem M5.2.E** **Self-Modifying Code**

Suppose we allow self-modifying code to execute, i.e., store instructions can write to the portion
of memory that contains executable code. Does the two-stage Princeton pipeline need to be
modified to support such self-modifying code? If so, please indicate how. You may use the
diagram below to draw modifications to the datapath. If you think no modifications are required,
explain why.


-----

3/2/2021

**Problem M5.2.F**

To solve a chip layout problem Ben decides to reroute the input of the WB mux to come from
after the AddrSrc MUX rather than ahead of the AddrSrc MUX. (The new path is shown with a
bold line, the old in a dotted line.) The rest of the design is unaltered.

How does this break the design? Provide a code sequence to illustrate the problem and explain in
one sentence what goes wrong.

**Problem M5.2.G** **Architecture Comparison**

Give one advantage of the Princeton architecture over the Harvard architecture.

Give one advantage of the Harvard architecture over the Princeton architecture.


-----

3/2/2021

##### Problem M5.3: Processor Design (Short Yes/No Questions)

The following statements describe two variants of a processor which are otherwise identical. In
each case, circle "Yes" if the variants might generate different results from the same compiled
program, circle "No" otherwise. You must also briefly explain your reasoning. Ignore differences
in the time that each machine takes to execute the program.

**Problem M5.3.A** **Interlock vs. Bypassing**

Pipelined processor A uses interlocks to resolve data hazards, while pipelined processor B has
full bypassing.

**Yes / No**

**Problem M5.3.B** **Delay Slot**

Pipelined processor A uses branch delay slots to resolve control hazards, while pipelined
processor B kills instructions following a taken branch.

**Yes / No**

**Problem M5.3.C** **Structural Hazard**

Pipelined processor A has a single memory port used to fetch instructions and data, while
pipelined processor B has no structural hazards.

**Yes / No**


-----

3/2/2021

##### Problem M5.4: HAL 180 ISA and 6-Stage Pipelined Implementation (Spring 2015 Quiz 1, Part C)

Inspired by how the IBM 360 uses condition codes, Ben Bitdiddle designs the HAL 180
architecture, which features two flag registers. Table C-1 describes these flags.

**Name** **Description**

Sign Flag (SF) Stores 1 if the result of the _last arithmetic or comparison_
_instruction was negative, 0 if it was positive_

Zero Flag (ZF) Stores 1 if the result of the _last_ _arithmetic, logical, or_
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


-----

3/2/2021

**Problem M5.4.B**

Ben’s HAL 180 6-stage pipeline (Figure M5.4-A) stalls to avoid data hazards through registers, but does not yet handle hazards due to
status flags. To illustrate why this is problematic, consider the following instruction sequence:

##### I0: ADD R1, R2
 I1: JG _L2
 I2: XOR R1, R3
 I3: JL _L2
 I4: _L1: SUB R1, R2
 I5: _L2: ADD R3, R1

Assume that when the program start, R1 = -1, R2 = -2, R3 = -3, and all the status flags are zero. Fill out the following instruction flow
diagram to incur the minimum amount of stalls while maintaining correct operation (i.e., use stalls to respect both data and status flag
dependences). Use “X”s to denote pipeline bubbles.

|Col1|T0|T1|T2|T3|T4|T5|T6|T7|T8|T9|
|---|---|---|---|---|---|---|---|---|---|---|
|FD|I0|I1|||||||||
|E1||I0|||||||||
|E2|||||||||||
|E3|||||||||||
|M|||||||||||
|W|||||||||||


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
 JMPstall = 
 JGstall =
 JLstall = 

```
Finally, write down the new stall signal (stall’) by using the old stall signal (stall) and stall conditions you derive.
```
stall’ =

```

-----

3/2/2021


**Problem M5.4.D**

Does this 6-stage pipeline add more challenges to precise exception handling? If so, please explain.


-----

3/2/2021

##### Problem M5.5: Pipelined Cache Access

_This problem requires the knowledge of Lecture 3. Please, review it before answering the_
_following questions. You may also want to take a look at pipeline lectures if you do not feel_
_comfortable with the topic._

**Problem M5.5.A**

Ben Bitdiddle is designing a five-stage pipelined MIPS processor with separate 32 KB directmapped primary instruction and data caches. He runs simulations on his preliminary design, and
he discovers that a cache access is on the critical path in his machine. After remembering that
pipelining his processor helped to improve the machine’s performance, he decides to try
applying the same idea to caches. Ben breaks each cache access into three stages in order to
reduce his cycle time. In the first stage the address is decoded. In the second stage the tag and
data memory arrays are accessed; for cache reads, the data is available by the end of this stage.
However, the tag still has to be checked—this is done in the third stage.

After pipelining the instruction and data caches, Ben’s datapath design looks as follows:

Instruction

I-Cache I-Cache I-Cache D-Cache D-Cache D-Cache

Decode & Write
Address Array Tag Execute Address Array Tag

Register back

Decode Access Check Decode Access Check

Fetch

Alyssa P. Hacker examines Ben’s design and points out that the third and fourth stages can be
combined, so that the instruction cache tag check occurs in parallel with instruction decoding and
register file read access. If Ben implements her suggestion, what must the processor do in the
event of an instruction cache tag mismatch? Can Ben do the same thing with load instructions by
combining the data cache tag check stage with the write-back stage? Why or why not?

**Problem M5.5.B**

Alyssa also notes that Ben’s current design is flawed, as using three stages for a data cache
access won’t allow writes to memory to be handled correctly. She argues that Ben either needs to
add a fourth stage or figure out another way to handle writes. What problem would be
encountered on a data write? What can Ben do to keep a three-stage pipeline for the data cache?

|I-Cache Address Decode|I-Cache Array Access|I-Cache Tag Check|Instruction Decode & Register Fetch|Execute|D-Cache Address Decode|D-Cache Array Access|D-Cache Tag Check|Write- back|
|---|---|---|---|---|---|---|---|---|


-----

3/2/2021

**Problem M5.5.C**

With help from Alyssa, Ben streamlines his design to consist of eight stages (the handling of data
writes is not shown):

I-Cache Tag

Check,

I-Cache I-Cache D-Cache D-Cache

Instruction D-Cache Write
Address Array Execute Address Array

Decode & Tag Check Back

Decode Access Decode Access

Register

Fetch

Both the instruction and data caches are still direct-mapped. Would this scheme still work with a
set-associative instruction cache? Why or why not? Would it work with a set-associative data
cache? Why or why not?

**Problem M5.5.D**

After running additional simulations, Ben realizes that pipelining the caches was not entirely
beneficial, as now the cache access latency has increased. If conditional branch instructions
resolve in the Execute stage, how many cycles is the processor’s branch delay?

**Problem M5.5.E**

Assume that Ben’s datapath is fully-bypassed. When a load is executed, the data becomes
available at the end of the D-cache Array Access stage. However, the tag has not yet been
checked, so it is unknown whether the data is correct. If the load data is bypassed immediately,
before the tag check occurs, then the instruction that depends on the load may execute with
incorrect data. How can an interlock in the Instruction Decode stage solve this problem? How
many cycles is the load delay using this scheme (assuming a cache hit)?

**Problem M5.5.F**

Alyssa proposes an alternative to using an interlock. She tells Ben to allow the load data to be
bypassed from the end of the D-Cache Array Access stage, so that the dependent instruction can
execute while the tag check is being performed. If there is a tag mismatch, the processor will
wait for the correct data to be brought into the cache; then it will re-execute the load and all of
the instructions behind it in the pipeline before continuing with the rest of the program. What
processor state needs to be saved in order to implement this scheme? What additional steps need
to be taken in the pipeline? Assume that a DataReady signal is asserted when the load data is
available in the cache, and is set to 0 when the processor restarts its execution (you don’t have to
worry about the control logic details of this signal). How many cycles is the load delay using this
scheme (assuming a cache hit)?

|I-Cache Address Decode|I-Cache Array Access|I-Cache Tag Check, Instruction Decode & Register Fetch|Execute|D-Cache Address Decode|D-Cache Array Access|D-Cache Tag Check|Write- Back|
|---|---|---|---|---|---|---|---|


-----

3/2/2021

**Problem M5.5.G**

Ben is worried about the increased latency of the caches, particularly the data cache, so Alyssa
suggests that he add a small, unpipelined cache in parallel with the D-cache. This “fast-path”
cache can be considered as another level in the memory hierarchy, with the exception that it will
be accessed simultaneously with the “slow-path” three-stage pipelined cache. Thus, the slowpath cache will contain a superset of the data found in the fast-path cache. A read hit in the fastpath cache will result in the requested data being available after one cycle. In this situation, the
simultaneous read request to the slow-path cache will be ignored. A write hit in the fast-path
cache will result in the data being written in one cycle. The simultaneous write to the slow-path
cache will proceed as normal, so that the data will be written to both caches. If a read miss
occurs in the fast-path cache, then the simultaneous read request to the slow-path cache will
continue to be processed—if a read miss occurs in the slow-path cache, then the next level of the
memory hierarchy will be accessed. The requested data will be placed in both the fast-path and
slow-path caches. If a write miss occurs in the fast-path cache, then the simultaneous write to the
slow-path cache will continue to be processed as normal. The fast-path cache uses a no-write
allocate policy, meaning that on a write miss, the cache will remain unchanged—only the slowpath cache will be modified.

Ben’s new pipeline design looks as follows after implementing Alyssa’s suggestion:

Fast-Path D
I-Cache Tag Cache

Check, Access and Slow-Path

I-Cache I-Cache Slow-Path

Instruction Tag Check D-Cache Write
Address Array Execute D-Cache

Decode & & Slow Path Array Back

Decode Access Tag Check

Register D-Cache Access

Fetch Address

Decode

The number of processor pipeline stages is still eight, even with the addition of the fast-path
cache. Since the processor pipeline is still eight stages, what is the benefit of using a fast-path
cache? Give an example of an instruction sequence and state how many cycles are saved if the
fast-path cache always hits.

|I-Cache Address Decode|I-Cache Array Access|I-Cache Tag Check, Instruction Decode & Register Fetch|Execute|Fast-Path D- Cache Access and Tag Check & Slow Path D-Cache Address Decode|Slow-Path D-Cache Array Access|Slow-Path D-Cache Tag Check|Write- Back|
|---|---|---|---|---|---|---|---|


-----

3/2/2021

##### Problem M5.6: Write Buffer for Data Cache (2005 Fall Part C)

In order to boost the performance of memory writes, Ben Bitdiddle has proposed to add a write
buffer to our 5-stage fully-bypassed MIPS pipeline as shown below. Assuming a writethrough/write no-allocate cache, every memory write request will be queued in the write buffer
in the MEM stage, and the pipeline will continue execution without waiting for writes to be
completed. A queued entry in the write buffer gets cleared only after the write operation
completes, so the maximum number of outstanding memory writes is limited by the size of the
write buffer.

Please answer the following questions.

stall PC for JAL, ...

0x4 nop IR _E_ IR _M_ IRW

Add

ASrc 31

we

rs1
rs2

PC addr _D_ rd1 A we

inst IR ws ALU Y addr

wd rd2

Inst GPRs B rdata
Cache Data

Imm Cache R
Ext wdatawdata

BSrc

MD1 MD2

Popcount(WBuf)

WBuf To main memory

**Problem M5.6.A**

Ben wants to determine the size of the write buffer, so he runs benchmark X to get the
observation below. What will be the average number of writes in flight (=the number of valid
entries in the write buffer on average)?

1) The CPI of the benchmark is 2.
2) On average, one of every 20 instructions is a memory write.
3) Memory has a latency of 100 cycles, and is fully pipelined.


-----

3/2/2021

**Problem M5.6.B**

Based on the experiment in the previous question, Ben has added the write buffer with N entries
to the pipeline. (Do not use your answer in M5.6A to replace N.) Now he wants to design a stall
logic to prevent a write buffer overflow. The structure of the write buffer is shown in the figure
below. `Popcount(WBuf) gives the number of valid entries in the write buffer at any given`
moment.


Valid


WAddr WData


Size
= N


Popcount(WBuf)

valid entries

|V|Valid|WAddr|WData|
|---|---|---|---|
||0|||
||0|||
|||||
||1|ADDR0|DATA0|


Please write down the stall condition to prevent write buffer overflows. You should derive the
condition without assuming any modification of the given pipeline. You can use Boolean and
arithmetic operations in your stall condition.

#### Stall =


-----

3/2/2021

**Problem M5.6.C**

In order to optimize the stall logic, Ben has decided to add a predecode bit to detect store
instructions in the instruction cache (I-Cache). That is, now every entry in the I-Cache has a store
bit associated with it, and it propagates through the pipeline with an Sstage bit added to each
pipeline register (except the one between MEM and WB stages) as shown below.
```
Popcount(Pipeline) gives the number of store instructions that are in flight (= number of

```
Sstage bits set to 1).

stall PC for JAL, ...

Popcount
(pipeline)

0x4 nop IR _E_ IR _M_ IRW

Add

ASrc 31

SE SM

we

rs1
rs2

PC addr _D_ rd1 A we

inst IR ws ALU Y addr

wd rd2

Inst GPRs B rdata
Cache SD Data

Imm Cache R
Ext wdatawdata

BSrc

MD1 MD2

Popcount(WBuf)

WBuf To main memory

How will this optimization change the stall condition, if at all?

#### Stall = 


-----

3/2/2021

##### Problem M5.7: Instruction Pipelining (Spring 2016 Quiz 1, Part C)

_This problem requires the knowledge of Handout #8 (LMIPS) and Lecture 6 and 7. Please, read_
_these materials before answering the following questions._

Consider the following MIPS code sequence:

I1  LW R1, 0(R3)

I2  XOR R1, R1, R4
I3 MUL  R2, R1, R4

I4 LW R4, 5(R2)

I5 XOR R4, R4, R5

I6 SW R2, 0(R3)

**Problem M5.7.A**

Assume the classic 5-stage MIPS pipeline as discussed in lecture, with **full bypassing and**
correct stall logic. Which instructions in the above sequence would have to stall?

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

|Col1|PC|Col3|
|---|---|---|

|we rs1 rs2 rd1 ws wd rd2 GPRs|Col2|
|---|---|

|addr inst Inst Memory|IR|
|---|---|


-----

3/2/2021

**Problem M5.7.C**

Complete the instruction flow diagram for the new sequence of instructions for Ben’s pipelined L-MIPS processor. **Assume no**
**bypassing and correct stall logic. (In case you need it, page 18 has an extra/scratch instruction flow diagram.)**

|0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|I1|F|D|A|M|X|||||||||||||||
|I2||||||||||||||||||||
|I3||||||||||||||||||||
|I4||||||||||||||||||||
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

stall

0x4 nop 1 IR _A_ 4 IR _M_ 7 IRX

Add

31

we

rs1rs2 2

addr inst IR _D_ wswd rd2rd1 0 A **+** 5 Y addrwerdata 8 A

Inst GPRs B
Memory 3 Data

Imm 6 Memory 10 B
Ext 11 wdatawdata

MD1 MD2

MD3

## From To From To

|Col1|PC|Col3|
|---|---|---|

|we rs1 rs2 rd1 ws wd rd2 GPRs|Col2|
|---|---|

|addr inst Inst Memory|IR|
|---|---|

|From|To|
|---|---|
|9|8|
|||
|||
|||
|||
|||
|||

|From|To|
|---|---|
|||
|||
|||
|||
|||
|||
|||


-----

3/2/2021

**Problem M5.7.E**

Complete the instruction flow diagram for the new sequence of instructions for the L-MIPS pipeline. **Assume full bypassing and**
correct stall logic this time. Use arrows to show forwarding of values from one stage to another. (In case you need it, page 18 has an
extra/scratch instruction flow diagram.)

|0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|I1|F|D|A|M|X|||||||||||||||
|I2||||||||||||||||||||
|I3||||||||||||||||||||
|I4||||||||||||||||||||
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


-----

