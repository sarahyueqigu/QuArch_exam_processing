###### ECE4100/ECE6100/CS4290/CS6290
 Advanced Computer Architecture
 Homework 1

**Due: Sunday, September 22nd 2019 (11:55 pm)**

________________________________________________________________________

###### Part A: Pipelining
-----------------------------------------------------------------------------------------------------------
Consider the 5-stage pipeline discussed in class.
The critical path for each stage is shown below

**Problem A.1:**
What is the highest frequency at which this pipeline can operate correctly?

max : Ins->citical
###### latency
 -- : HE = 1 highest frequency 103" 21
The stall time of a pipelined design can be reduced by Data Bypassing/Forwarding.
Performance Evaluations showed that implementing data forwarding reduces the CPI
(Clock cycle Per Instruction) by 15%. However, forwarding adds an additional mux to

###### 
the ID stage or the EX stage that adds 0.4ns to the critical path.

   
**Problem A.2:**
If we implement data forwarding by adding the mux to the ID stage, what will be the new
operating frequency, and overall speedup?

[Speedup = Old Run Time / New Run Time]

2PI = 0 . 85


.
4=1


.
2ns


###### critical path=


.
0 8 +0


=
###### 83MAE


###### operating frequency


= 2x1023 "t


###### speedup


: -1x I

1 .2x0558


1


-----

**Problem A.3:**
If we implement data forwarding by adding the mux to the EX stage, what will be the
new operating frequency, and overall speedup?

###### critical path : 1 .3us
 operating frequency : x10-9 * *MUZ

:

:

###### speedup

0 .85 0943

**Problem A.4:**
Select one recommendation from below based on the answers above
(a) Implement data forwarding by adding the mux to the ID stage
(b) Implement data forwarding by adding the mux to the EX stage
(c) Do not implement data forwarding

###### ~

without
###### forwarding-lowest [total][ time]

**Problem A.5:**
How would your answers for A.2, A.3 and A.4 change if the mux delay was 0.2 ns?

1x I
###### -. 1 .

Speedup with mux in ID stage: [0 ___________________ .8 +0 [.] 23x0 85= 11647

=

Speedup with mux in EX stage: 2x0___________________ . 85 15


a is better
###### (speedup)

Recommendation (a/b/c) : ___________________

2


-----

###### Part B: Branch Prediction
-----------------------------------------------------------------------------------------------------------
Consider a CPU with a deep pipeline pictured below.

 
  
The first stage of the pipeline fetches the instruction. The **second stage of the pipeline**
recognizes branch instructions and decodes the branch target (which is present as part of
the instruction). The second stage also has a Global History Branch Predictor. _If the_
_branch is predicted to be Taken, it forwards the decoded target of the branch to the first_
stage, and kills the instruction in the first stage. The eighth stage of the pipeline reads the
registers and resolves the correct direction of the branch. If the branch direction was
mispredicted, the correct direction is forwarded to the first stage, and all instructions in
between are killed. The remaining stages finish the computation of the instruction.

The processor uses a single global history bit to remember whether the last branch was
taken or not. The global history bit is used to index into the **BHT (the address of the**
branch is not used for selecting the BHT entry).
The BHT has 2 entries. Each entry is a 2-bit saturating counter.
In state 1X, we will guess Taken; in state 0X, we will guess Not Taken.

3


 -

  -


-----

**Problem B.1:**

Fill out the following Table on the number of bubbles in the pipeline based on the
predicted and actual directions of the branch.

**Branch Prediction** **Actual Direction** **Pipeline Bubbles**

T T I

T NT 7

NT T 7

NT NT I

In the next two problems we will study execution of the following loop.

Instruction Address Instruction
Label

LOOP I1 BEQ R2, R5, NEXT     - NT

I2 ADD R4, R4, 1

NEXT I3 MULT R2, R2, 3847

         - T

I4 BNEZ R4, LOOP

I5 NOP

I6 NOP

I7 NOP

I8 NOP

I9 NOP

I10 NOP

I11 NOP

This processor has **no branch delay slots. You should assume that branch I1 is** **never**
taken, and that the branch I4 is always taken.
**Thus the correct instruction execution sequence will be:**
**I1, I2, I3, I4, I1, I2, I3, I4, I1, I2, I3, I4, …**

You should also disregard any possible structural hazards. The processor always runs
at full speed, and there are **no pipeline bubbles (except for those created by the**
branches).

4

|Branch Prediction|Actual Direction|Pipeline Bubbles|
|---|---|---|
|T|T|I|
|T|NT|7|
|NT|T|7|
|NT|NT|I|

|Instruction Label|Address|Instruction|
|---|---|---|
|LOOP|I1|BEQ R2, R5, NEXT -|
||I2|ADD R4, R4, 1|
|NEXT|I3|MULT R2, R2, 3847|
||I4|BNEZ R4, LOOP|
||I5|NOP|
||I6|NOP|
||I7|NOP|
||I8|NOP|
||I9|NOP|
||I10|NOP|
||I11|NOP|


-----

**Problem B.2:**

We study how well the history bit works, when it is being updated by the eighth stage
of the processor (i.e., upon branch resolution).

The eighth stage also updates the BHT based on the result of a branch. The same BHT
entry that was used to make the original prediction is updated.

Please fill in the entries of the table below from cycle #9 to 14. An instruction has to be
fetched very cycle. Only enter those entries that change. Cycles 0 to 9 are already filled
for you.

**The circled instructions are those which will be committed (i.e., are non-**
**speculative).**
The rest of the fetched instructions will become NOPs / pipeline bubbles.

**Branch Predictor State**

**Cycle** **Instruction** **Branch** **Prediction** **Branch** **Last Branch Not** **Last Branch**

**Fetched** **Prediction** **Correct?** **History** **Taken Predictor** **Taken Predictor**

0 - - 0T 10 ⑧01

1 **I1**

I1

2 I2 **NT** Yes

3 I3

4 I4

5 I5 NT No

6 I6

7 I7

8 I8 **NT** 10 000

9

###### 18

10

11 11 [I] I 10 0 I

12

13 NI yes

14

###### ⑲

5

|Cycle|Instruction Fetched|Branch Prediction|Prediction Correct?|Branch Predictor State|Col6|Col7|
|---|---|---|---|---|---|---|
|||||Branch History|Last Branch Not Taken Predictor|Last Branch Taken Predictor|
|0|-|-||0 T|10|⑧01|
|1|I1||||||
|2|I1 I2|NT|Yes||||
|3|I3||||||
|4|I4||||||
|5|I5|NT|No||||
|6|I6||||||
|7|I7||||||
|8|I8|||NT|10|0 00|
|9|||||||
|10|18||||||
|11|11 I|||I|10|0 I|
|12|||||||
|13|⑲|NI|yes||||
|14|||||||


-----

**Problem B.3**

Now we study how well the branch **history bit works, when it** **is being updated**
**speculatively by the second stage of the processor. If the branch is mispredicted, the**
eighth stage sets the branch history bit to the correct value.

_If an instruction in the second stage, and one in the eighth stage both want to update the_
_History Bit, the one in the eighth stage gets higher priority (since it is non-speculative)._

Finally, the eighth stage also updates the BHT based on the result of a branch. The same
BHT entry that was used to make the original prediction is updated.

Please fill in the entries of the table below from cycle #5 to 13. An instruction has to be
fetched very cycle. Only enter those entries that change. Cycles 0 to 5 are already filled
for you.

**The circled instructions are the ones which will be committed (i.e., are non**
**speculative).**
The rest of the fetched instructions will become NOPs / pipeline bubbles.

**Branch Predictor State**

**Cycle** **Instruction** **Branch** **Prediction** **Branch** **Last Branch Not** **Last Branch**

**Fetched** **Prediction** **Correct?** **History** **Taken Predictor** **Taken Predictor**

0 - - T 10 01

1 **I1**

I1

2 I2 **NT** Yes NT ⑩ 01

3 I3

4 I4

5 I5 T yes I 10 0 I

6 T- I

###### ⑧

7 T⑧- [2] NI Yes NT 70 0 I

8 ⑬T **NT** 10 00

9 ⑧T- 4

10 I5 T yes T 10 00

11 ⑰ T 11 00

12 -T [2] NT Yes NI 11 00

###### 0

13 I3 NI 11 00

###### ⑧

6

|Cycle|Instruction Fetched|Branch Prediction|Prediction Correct?|Branch Predictor State|Col6|Col7|
|---|---|---|---|---|---|---|
|||||Branch History|Last Branch Not Taken Predictor|Last Branch Taken Predictor|
|0|-|-||T|10|01|
|1|I1||||||
|2|I1 I2|NT|Yes|NT|⑩|01|
|3|I3||||||
|4|I4||||||
|5|I5|T|yes|I|10|0 I|
|6|⑧ T - I||||||
|7|⑧ T 2 -|NI|Yes|NT|70|0 I|
|8|⑬ T|||NT|10|00|
|9|⑧ T - 4||||||
|10|I5|T|yes|T|10|00|
|11|⑰|||T|11|00|
|12|0 -T 2|NT|Yes|NI|11|00|
|13|⑧ I3|||NI|11|00|


-----

###### Part C: Dependencies and Register Renaming
-----------------------------------------------------------------------------------------------------------
**Problem C.1**
Consider the following instruction sequence. An equivalent sequence of C-like
pseudocode is also provided.

I1: L.D   F1, 0 (R1)    ;  F1 = *r1;
I2: MUL.D  F2, F0, F2    ;  F2 = F0*F2;
I3: ADD.D  F1, F2, F2    ;  F1 = F2 + F2;
I4: L.D   F2, 0 (R2)    ;  F2 = *r2;
I5: ADD.D  F3, F1, F2    ;  F3 = F1 + F2;
I6: S.D   F3, 0 (R3)    ;  *r3 = F3;
……

Fill out the table below to identify all Read-After-Write (RAW), Write-After-Read
(WAR), and Write-After-Write (WAW) dependencies in the above sequence. Do not
worry about memory dependencies for this question. The dependency between I2 and I3
is already filled in for you.

**Earlier (Older) Instruction**

###### I1 I2 I3 I4 I5 I6

 I1 
 I2 ~
 

**Current**

**Instruction**


###### I3 WAW RAW 
WAW/

###### I4 - WAR WAR 
     -      
###### I5 RAW RAW 
        -         -         
###### I6 - RAW 
7

|I1|I2|I3|I4|I5|I6|
|---|---|---|---|---|---|
|-||||||
|~|-|||||
|WA W|RAW|-||||
|-|WAW/ WAR|WA R|-|||
|-|-|RA W|RA W|-||
|-|-|-|-|RA W|-|


-----

**Problem C.2**
Your task is to rewrite the code in C.1 using register renaming to remove as many
dependencies as you can. You may use an unlimited number of registers. Do not change
the order of instructions. For your convenience, the code in C.1 is repeated below.

I1: L.D   F1, 0 (R1)
I2: MUL.D  F2, F0, F2
I3: ADD.D  F1, F2, F2
I4: L.D   F2, 0 (R2)
I5: ADD.D  F3, F1, F2
I6: S.D   F3, 0 (R3)

**[After register renaming]**

I1: LD S1, 0 (R17
I2: MUL-D S2, FO, [F2]
I3: ADD - D S3, [52,52]
I4:  L . D Sh, [0(R2)]

I5: ADD - DSS, [S3], [Sh]
I6: S . D S5, 0(R3)

**C.3:**
Suppose we want to run the same code sequence under the system which is 2-wide
superscalar with the units shown in the table below.

One Memory Unit 1 cycle latency

One Floating-point Adder 2 cycle latency

One Floating-point Multiplier 8 cycle latency

All of these functional units are fully pipelined, but there is no bypassing so they have to
stall to deal with dependencies. Note that the issue stage and the writeback stage also take
one cycle to complete.

The system is an **out-of-order issue, out-of-order completion machine,** **with register**
**renaming. Many instructions can be issued and completed at one cycle and assume that**
it can rename as many registers as necessary as in C.2. Also assume that the Issue Queue
contains all 6 instructions at the beginning. Fill in the table to show which instruction(s)
is being dispatch, executed at each unit, and written back, for each cycle.

8

|One Memory Unit|1 cycle latency|
|---|---|
|One Floating-point Adder|2 cycle latency|
|One Floating-point Multiplier|8 cycle latency|


-----

Assume that I1 and I2 are issued at cycle 0, as indicated in the table. Remember it has to
deal with hazards by stalling (You may not need all the columns in the table).

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18

I1
I2 In I3 IS I6

###### I [1] In

 I3 I3 IS IS

 I2 I2 I2 [12 I2][ 12 12] 12

 I2
I1 In I3
###### IS

9

|Cycle:|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Dispatch (1)|I1 I2|I n|||||||||I 3||||I S||||I 6|||
|Memory Unit (1)||I 1|I n|||||||||||||||||I6||
|F-Adder (2)||||||||||||I 3|I 3|||IS|I S|||||
|F-Mult (8)||I2|I2|I2|12|I2|12|12|1 2|||||||||||||
|WriteBack (1)|||I1|In||||||I2||||I3||||IS|||I6|


-----

###### Part D: Out-of-Order Execution, Speculative Execution, and Recovery
-----------------------------------------------------------------------------------------------------------
This problem investigates the operation of a superscalar processor with branch prediction,
register renaming, and out-of-order execution. The processor holds all data values in a
**physical register file (PRF), and uses a** **register alias table (RAT)** to map from
architectural to physical register names. A **free list is used to track which physical**
registers are available for use. A **reorder buffer (ROB) contains the bookkeeping**
information for managing the out-of-order execution (but, it does not contain any register
data values).

When a branch instruction is encountered, the processor predicts the outcome and takes a
snapshot of the rename table. If a misprediction is detected when the branch instruction
later executes, the processor recovers by flushing the incorrect instructions from the
ROB, rolling back the “next available” pointer, updating the free list, and restoring the
earlier rename table snapshot.

We will investigate the execution of the following code sequence (assume that there is no
branch-delay slot):

**loop: lw  r1, 0(r2)  # load r1 from address in r2**
**addi r2, r2, 4  # increment r2 pointer**
**beqz r1, skip   # branch to “skip” if r1 is 0**
**addi r3, r3, 1  # increment r3**
**skip: bne  r2, r4, loop # loop until r2 equals r4**

The diagram on the next page shows the state of the processor during the execution of the
given code sequence. An instance of each instruction in the loop has been issued into the
ROB (the beqz instruction has been predicted not-taken), but none of the instructions
have begun execution. In the diagram, old values which are no longer valid are shown in
the following format: . The rename table snapshots and other bookkeeping

information for branch misprediction recovery are not shown.

10


-----

###### Register  Physical Free List
 Register File  Alias Table

        - P4 - -P7 P4 P0 8016 p

- -P5 ⑮ P5 P1 6823- -p

- -P6 P3 P2 8000- -p -P7

-P8

R4 P0 P3 7 p

|Register Alias Table R1 - P-4 -P7|Col2|Col3|Col4|
|---|---|---|---|
|R2 R3|- -|-P5 -P6|⑮ P3|
|R4|P0|||


P4 0 P P9

###### In 21, [0] (2) P5 8004 P Pl

P2
addi v2, [22][,][ H] P6 - I
P8

~I, P7
ship
###### begz

addi 23, [23], 1 P8

P9 47

bue 22, [wh][,] loop

↑6

###### Reorder Buffer (ROB)
 use ex op p1 PR1 p2 PR2 Rd LPRd PRd
 next to x W lw p P2 r1 P1 P4
 →
 commit x ~ addi p P2 r2 P2 P5
 next [to] - x beqz P P4
commet

next available[--]x [ ~] addi p P3 r3 P3 P6

###### next -x bne P5 p P0
 P
 available * Iw >I PS ~I ↑4 P7 →

-X addi P P5 U2 PS P8
### &

###### next -> A begz P7 available
## 
|hysical egister File 8016 -|p|
|---|---|
|- 6823 - 8000|-p -p|
|7|p|
|0|P|
|8004|P|
|-|I|
|||
|||
|||

|use|ex|op|p1|PR1|p2|PR2|Rd|LPRd|PRd|
|---|---|---|---|---|---|---|---|---|---|
|x|W|lw|p|P2|||r1|P1|P4|
|||||||||||
||~||||||||P5|
|x||addi|p|P2|||r2|P2||
|x||beqz|P|P4||||||
|- x|~|addi|p|P3|||r3|P3|P6|
|-x||bne|P|P5|p|P0||||
|*||Iw|> I|PS|||~I|↑4|P7|
|- X||a ddi|P|P5|||U2|PS|P8|
|A||begz||P7||||||
|||||||||||


11


-----

**Problem D.1:**

Assume that the following events occur in order (though not necessarily in a single
cycle):

**Step 1.** The first three instructions from the next loop iteration (lw, addi, beqz) are

written into the ROB (note that the bne instruction has been predicted taken).

**Step 2.** All instructions which are ready after Step 1 execute, write their result to the

physical register file, and update the ROB. Note that this step only occurs
**once.**

**Step 3.** As many instructions as possible commit.
**Step 4.** The processor detects that the beqz instruction has mispredicted the branch

outcome, and recovery action is taken to repair the processor state.

**Update the diagram to reflect the processor state after these events have occurred.**
**Cross out any entries which are no longer valid.  Note that the “ex” field should be**
**marked when an instruction executes, and the “use” field should be** **cleared when it**
commits. Be sure to update the “next to commit” and “next available” pointers. If the
**load executes, assume that the data value it retrieves is 0.**

**Problem D.2:**

Consider (1) a single-issue, in-order processor with no branch prediction and (2) a
multiple-issue, out-of-order processor with branch prediction. Assume that both
processors have the same clock frequency. Consider how fast the given loop executes on
each processor, assuming that it executes for many iterations.

Under what conditions, if any, might the loop execute at a faster rate on the in-order
processor compared to the out-of-order processor?

there are [two] branches in the code, [as] in the above case if the

branch is mispredicted then all [the] further instructions have to be

###### flushed-loss, So if the branch is not accurate of cycles predictor

loss              - branch resolution
###### enoughUnder what conditions, if any, might the loop execute at a faster rate on the out-of-order [and][ the] of cycles [due][ to]
##### tws###### cyclesprocessor compared to the in-order processor? [then] in order might have better performance .

B =@° ⑭}@°

# 

###### If the branch prediction accuracy is good then out of order performs

better because it executes many possible instructions parallely

12


B =@° ⑭}@°

###### If the branch prediction is good then out of order performs


.


-----

