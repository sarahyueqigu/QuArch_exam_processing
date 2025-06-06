#### CMU 18-447 Introduction to Computer Architecture, Spring 2015
## Final Exam

Date: Tue., 5/5

Instructor: Onur Mutlu
TAs: Rachata Ausavarungnirun, Kevin Chang, Albert Cho, Jeremie Kim, Clement Loh

Name:

Problem 1 (50 Points):

Problem 2 (50 Points):

Problem 3 (50 Points):

Problem 4 (50 Points):

Problem 5 (40 Points):

Problem 6 (50 Points):

Problem 7 (60 Points):

Bonus (50 Points):

Total (400 Points):

**Instructions:**

1. This is a closed book exam. You are allowed to have three letter-sized cheat sheets.

2. No electronic devices may be used.

3. This exam lasts 3 hours.

4. Clearly indicate your final answer for each problem.

5. Please show your work when needed.

6. Please write your initials at the top of every page.

7. Please make sure that your answers to all questions (and all supporting work that is required)
are contained in the space required.

**Tips:**

_• Be cognizant of time. Do not spend too much time on one question._

_• Be concise. You will be penalized for verbosity and unnecessarily long answers._

_• Show work when needed. You will receive partial credit at the instructors’ discretion._

_• Write legibly. Show your final answer._


-----

Initials:

#### 1. Virtual Memory and Caches [[50 points]]

Assume that we have a byte-addressable processor that implements paging-based virtual memory
using a three-level hierarchical page table organization. The virtual address is 46 bits, and the
physical memory is 4GB. The page table base register (PTBR) stores the base address of the firstlevel table (PT1 ). All the page tables have the same size of one physical page for the first-level
(PT1 ), second-level (PT2 ), and third level (PT3 ). Each PT1 /PT2 entry stores the base address of
a second/third-level table (PT2 /PT3 ). In contrast to PT1 and PT2, each PT3 entry stores a page
table entry (PTE). The PTE is 4-bytes in size.

The processor has a 64KB virtually-indexed physically-tagged (VIPT) L1 cache that is direct
mapped with a cache line size of 128 bytes, and a 64-entry TLB.

(a) What is the physical page size? Show all your work.

1. First, the physical address space is log2 4GB = 32bits. So each PT1 and PT2 entry
stores 32bits (4bytes).
2. Since the virtual address space is 46 bits and assume the page size is P, then there
are [2]P[46] possible mappings that the page tables can store.

3. Each page table can store _[P]4_ [mappings because each entry is 4 bytes and the table]

is P bytes. The three-level hierarchical page table can in total store ( _[P]4_ [)(][ P]4 [)(][ P]4 [) =][ 2]P[46]

mappings.
4. P = 2[13].

(b) How many bits of the virtual page number are used to index the L1 cache?

The cache requires log2 64KB = 16 bits from the address for indexing. So 3 bits are
overlapped with the VPN.

(c) What kind of aliasing problem does this processor’s L1 cache have?


-----

Initials:

(d) In lecture, we learned multiple techniques to resolve this particular aliasing problem (in part (c)
above) in a VIPT cache. One of them is to increase the associativity of the cache. To address
this aliasing problem for this processor’s VIPT cache, what is the minimum associativity that is
required for the cache? Show your work.

2[3] = 8

(e) We also learned another technique that searches all possible sets that can contain the same physical
block. For this VIPT cache, how many sets need to be searched to fix the aliasing problem? Show
your work.


-----

Initials:

#### 2. Register Renaming [[50 points]]

In this problem, we will give you the state of the Register Alias Table (RAT), Reservation Stations
(RS), and Physical Register File (PRF) for a Tomasulo-like out-of-order execution engine.

The out-of-order machine in this problem has the following characteristics:

The processor is fully pipelined with four stages: Fetch, decode, execute, and writeback.

_•_

For all instructions, fetch takes 1 cycle, decode takes 1 cycle, and writeback takes 1 cycle.

_•_

The processor implements ADD and MUL instructions only. Both the adder and multiplier are

_•_
fully pipelined. ADD instructions take 3 cycles and MUL instructions take 4 cycles in the execute
stage. Note that the adder and multiplier have separate common data buses (CDBs), which
allow both the adder and multiplier to broadcast results in the same cycle.

An instruction always allocates the first reservation station that is available (in top-to-bottom

_•_
order) at the required functional unit.

Suppose the pipeline is initially empty and the machine fetches exactly 5 instructions. The diagram
below shows the snapshot of the machine at a particular point in time.


**Register Alias Table**
ID V Tag

R0 1 P1

R1 1 P8

R2 1 P12

R3 1 P4

R4 0 P7

R5 1 P5

R6 0 P11

R7 1 P14

ADD Reservation Station

V Tag V Tag

1 P12 1 P7

1 P5 0 P13

ADD CDB


**Physical Register File**

V Data ID V Data

0 2 P8 1 88

1 11 P9 0 90

0 2 P10 0 91

0 30 P11 1 110

1 3 P12 1 33

1 50 P13 1 130

0 5 P14 1 17

1 70 P15 1 159

MUL Reservation Station

ID V Tag V Tag

0 – 0 –

1 P12 1 P4

1 P7 1 P7

MUL CDB

|ID|V|Tag|
|---|---|---|
|R0|1|P1|
|R1|1|P8|
|R2|1|P12|
|R3|1|P4|
|R4|0|P7|
|R5|1|P5|
|R6|0|P11|
|R7|1|P14|

|ID|V|Data|ID|V|Data|
|---|---|---|---|---|---|
|P0|0|2|P8|1|88|
|P1|1|11|P9|0|90|
|P2|0|2|P10|0|91|
|P3|0|30|P11|1|110|
|P4|1|3|P12|1|33|
|P5|1|50|P13|1|130|
|P6|0|5|P14|1|17|
|P7|1|70|P15|1|159|

|ID|V|Tag|V|Tag|Dest. Tag|
|---|---|---|---|---|---|
|A|1|P12|1|P7|P15|
|B|1|P5|0|P13|P11|

|ID|V|Tag|V|Tag|Dest. Tag|
|---|---|---|---|---|---|
|X|0|–|0|–|–|
|Y|1|P12|1|P4|P7|
|Z|1|P7|1|P7|P13|


-----

Initials:

(a) Your first task is to use only the supplied information to draw the data flow graph for the five
instructions which have been fetched. Label nodes with the operation (+ or *) being performed
and edges with the architectural register alias numbers (e.g., R0).

### R0 R3

# * R3

### R2

# *

### R4
 + * R5
 R6
 R6
 +

 R6

(b) Now, use the data flow graph to fill in the table below with the five instructions being executed
on the processor in program order. The source registers can be specified in either order. Give
instructions in the following format: “opcode, source1, source2, destination.”

OP Src 1 Src 2 Dest

MUL R0 R3 R2

MUL R2 R3 R4

ADD R2 R4 R6

MUL R4 R4 R6

ADD R5 R6 R6

(c) Now, show the full pipeline timing diagram below for the sequence of five instructions that you
determined above, from the fetch of the first instruction to the writeback of the last instruction.
Assume that the machine stops fetching instructions after the fifth instruction.

As we saw in class, use F for fetch, D for decode, En to signify the nth cycle of execution
for an instruction, and W to signify writeback. You may or may not need all columns shown.
Finally, identify the cycle after which the snapshot of the microarchitecture was taken. Shade the
corresponding cycle in the last row of the table.

|OP|Src 1|Src 2|Dest|
|---|---|---|---|
|MUL|R0|R3|R2|
|MUL|R2|R3|R4|
|ADD|R2|R4|R6|
|MUL|R4|R4|R6|
|ADD|R5|R6|R6|

|Cycle:|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Instruction 1|F|D|E1|E2|E3|E4|W|||||||||||||
|Instruction 2||F|D||||E1|E2|E3|E4|W|||||||||
|Instruction 3|||F|D|||||||E1|E2|E3|W||||||
|Instruction 4||||F|D||||||E1|E2|E3|E4|W|||||
|Instruction 5|||||F|D|||||||||E1|E2|E3|W||
|Snapshot cycle||||||||||X||||||||||


-----

Initials:

#### 3. Branch Prediction [[50 points]]

Assume the following piece of code that iterates through two large arrays, j and k, each populated
with completely (i.e., truly) random positive integers. The code has two branches (labeled B1 and
B2). When we say that a branch is taken, we mean that the code inside the curly brackets is executed.
Assume the code is run to completion without any errors (there are no exceptions). For the following
questions, assume that this is the only block of code that will ever be run, and the loop-condition
branch (B1) is resolved first in the iteration before the if-condition branch (B2).

for (int i = 0; i < 1000000; i++) { /* B1 */
/* TAKEN PATH for B1 */
if (i % 3 == 0) { /* B2 */
j[i] = k[i] - i; /* TAKEN PATH for B2 */
}
}

You are running the above code on a machine with a two-bit global history register (GHR) shared
by all branches, which starts with Not Taken, Not Taken (2’b00). Each pattern history table entry
(PHTE) contains a 2-bit saturating counter.
The saturating counter values are as follows:
2’b00 - Strongly Not Taken
2’b01 - Weakly Not Taken
2’b10 - Weakly Taken
2’b11 - Strongly Taken

(a) You observe that the branch predictor mispredicts 100% of the time in the first 5 iterations of the
loop. Is this possible? Fill in the table below with all possible initial values each entry can take.
Leave the table blank if this is not possible.

**PHT**

PHT Entry Value

TT 01

TN 00

NT 01

NN 00 or 01

Show your work here:

|Col1|PHT|
|---|---|
|PHT Entry|Value|
|TT|01|
|TN|00|
|NT|01|
|NN|00 or 01|


-----

Initials:

(b) Please read the entire question first before answering any part.

Rachata believes that the misprediction rate can become 0% during the steady state.

Is this possible?

Circle one: YES NO

If it is possible (YES), fill in one possible set of initial PHTE values that can lead to a 0%
misprediction rate.

**PHT**

PHT Entry Value

TT
TN
NT
NN

If it is not possible (NO), what is the lowest misprediction rate that can be achieved during the
steady state?

The lowest misprediction rate is 33.33%.

Show all your work here below:

|Col1|PHT|
|---|---|
|PHT Entry|Value|
|TT||
|TN||
|NT||
|NN||


-----

Initials:

#### 4. Interconnects [[50 points]]

The following diagrams show four different topologies. In this question, assume that a packet can
move from one node to the adjacent node in 1 cycle. Also, assume that the routing mechanism uses
the shortest path from the source to the destination.

#### a) Uni-Directional Ring b) Bi-Directional Ring

##### c) 2-D Torus d) 3-D Torus


-----

Initials:

(a) What is the average latency of a uni-directional ring of size n, assuming a uniform traffic pattern
where every node has an equal probability of sending a packet to every other node without traffic
_contention? No traffic contention means that a packet can always move toward its destination_
every cycle on its shortest path. For this and the following questions, assume that n is an odd
**number. Show your work.**

_Avg(1 + 2 + 3 + ... + n −_ 1) [(][n]2([)(]n[n]−[−]1)[1)] [=][ n]2

(b) What is the average latency of a bi-directional ring of size n, assuming a uniform traffic pattern
without traffic contention? Show your work.


-----

Initials:

(c) What is the average latency of a n _n torus, assuming a uniform traffic pattern without traffic_
_∗_
contention? Show your work. (Hint: each ring in a torus is a bi-directional ring.)

2 ∗ [(][n][+1)]4 = [(][n][+1)]2

(d) What is the average latency of a n _n_ _n 3-D torus, assuming a uniform traffic pattern without_
_∗_ _∗_
traffic contention? Show your work.


-----

Initials:

#### 5. Memory Consistency [[40 points]]

There are 2 threads with 4 instructions. The two threads are executed concurrently on a dual-core
processor. Assume that registers in both cores are initialized with the values shown in the table below.
The instructions of each thread are also shown below.

R1 1

R2 2

R3 3

R4 4

Thread A Thread B

ST R1, 0x1000 ST R3, 0x1000

LD R5, 0x1000 LD R5, 0x1000

ADD R5, R5, R2 ADD R5, R5, R4

ST R5, 0x1000 ST R5, 0x1000

(a) Assume the dual-core processor implements sequential consistency. List all the possible values
that can be stored in address 0x1000, assuming both threads run to completion.

3, 5, 7, 9

(b) How many different memory instruction interleavings of the 2 threads will guarantee a value of
0x9 in address 0x1000, assuming both threads run to completion? Show your work.

|R1|1|
|---|---|
|R2|2|
|R3|3|
|R4|4|

|Thread A|Thread B|
|---|---|
|ST R1, 0x1000|ST R3, 0x1000|
|LD R5, 0x1000|LD R5, 0x1000|
|ADD R5, R5, R2|ADD R5, R5, R4|
|ST R5, 0x1000|ST R5, 0x1000|


-----

Initials:

(c) Assume now that the dual-core processor does not support sequential consistency. List all the
**possible values that can be stored in address 0x1000, assuming both threads run to completion.**
Explain your answer briefly.


-----

Initials:

#### 6. Memory Interference [[50 points]]

During the lectures, we introduced a variety of ways to tackle memory interference. In this problem,
we will look at the Blacklisting Memory Scheduler (BLISS) to reduce unfairness. There are two key
aspects of BLISS that you need to know.

When the memory controller services η consecutive requests from a particular application, this

_•_
application is blacklisted. We name this non-negative integer η the Blacklisting Threshold.

The blacklist is cleared periodically every 10000 cycles starting at t=0.

_•_

To reduce unfairness, memory requests in BLISS are prioritized in the following order:

Non-blacklisted applications’ requests

_•_

Row-buffer hit requests

_•_

Older requests

_•_

The memory system for this problem consists of 2 channels with 2 banks each. Tables 1 and 2 show
the memory request stream in the same bank for both applications at varying times. The memory
requests are labeled with numbers that represent the row position of the data within the accessed
bank. Assume the following for all questions:

A row buffer hit takes 50 cycles.

_•_

A row buffer miss/conflict takes 200 cycles.

_•_

All the row buffers are closed at time t=0.

_•_

Application A (Channel 0, Bank 0)
Application B (Channel 0, Bank 0) Row 1 Row 1 Row 1 Row 1 Row 1 Row 1 Row 1

Table 1: Memory requests of the two applications at t=0

Application A (Channel 0, Bank 0) Row 3 Row 7 Row 2 Row 0 Row 5

Application B (Channel 0, Bank 0) Row 1 Row 1 Row 1 Row 1 Row 1 Row 1 Row 1

Table 2: Memory requests of the two applications at t=10


-----

Initials:

(a) Compute the slowdown of each application using the FR-FCFS scheduling policy after both
threads ran to completion. We define slowdown = _[mem latency with others]mem latency alone_ . Show your work.

Slowdown of A: [(200+6]5[∗]∗[50)+5]200 _[∗][200]_ = [1500]1000 [= 1.50]

Slowdown of B: 200+6[200+6][∗]∗[50]50 [=][ 500]500 [= 1.00]

(b) For what value(s) of η (the Blacklisting Threshold) will the slowdowns for both applications be
equivalent to those obtained with FR-FCFS?


-----

Initials:

(c) For what value(s) of η (the Blacklisting Threshold) will the slowdown for A be <1.4?

Impossible. Slowdown for A will always be 1.4.
_≥_
If you trace the schedule carefully, you will observe that A will be the fastest when η=5,
where slowdown of A=1.4. η=5 is the smallest η where A does not get blacklisted.

(d) For what value(s) of η (the Blacklisting Threshold) will B experience maximum slowdown it can
experience with the Blacklisting Scheduler?

_η=5 or η=6_
We observe that as long as B gets blacklisted at least once, B will incur an additional
miss and hence an extra of 200 cycles. Thus, we want 2 conditions to be satisfied: B to
miss at least once AND an η such that B completes last. These conditions are satisfied
only when η=5 or η=6. MaximumSlowdownofB = [1650]500 [= 3][.][3]

(e) What is a simple mechanism (that we discussed in lectures) that will make the slowdowns of both
A and B 1.00?


-----

Initials:

#### 7. Memory Latency Tolerance [[60 points]]

Assume an in-order processor that employs runahead execution, with the following specifications:

The processor enters Runahead mode when there is a cache miss.

_•_

There is a 64KB cache. The cache block size is 64 Bytes.

_•_

The cache is 2-way set associative and uses the LRU replacement policy.

_•_

A cache hit is serviced instantaneously.

_•_

A cache miss is serviced after X cycles.

_•_

The cache replacement policy chooses to evict a cache block serviced by Runahead requests over

_•_
non-runahead requests. The processor does not evict the request that triggers Runahead mode
until after Runahead mode is over.

The victim for cache eviction is picked at the same time a cache miss occurs.

_•_

Whenever there is a cache miss, the processor always generates a new cache request and enters

_•_
Runahead mode.

There is no penalty for entering and leaving Runahead mode.

_•_

ALU instructions and Branch instructions take one cycle each and never stall the pipeline.

_•_

Consider the following program. Each element of array A is one byte.

for(int i=0;i<100;i++) \\ 2 ALU instructions and 1 branch instruction
{
int m = A[i*32*1024]+1; \\ 1 memory instruction followed by 1 ALU instruction
26 ALU instructions
}

(a) After running this program, you find that there are 50 cache misses. What are all the possible
values of X?

30 < X < 61.

(b) Is it possible that every cache access in the program misses in the cache? If so, what is the value
of X that will make all cache accesses in the program miss in the cache? If not, why? Show your
work.


-----

Initials:

(c) What is the minimum number of cache misses that this program can achieve? Show your work.

50 misses.

(d) Assume that each ALU instruction consumes 1uJ, a cache hit consumes 10uJ, and a cache miss
consumes Y uJ. Does there exist a combination of X and Y such that the dynamic energy
consumption of Runahead execution is better than a processor without Runahead execution?
Show your work.


-----

Initials:

(e) Assume the energy parameters in part d. What is the dynamic energy consumption of the processor with Runahead execution in terms of X and Y when X generates the minimum number
of cache misses? Show your work.

At most, this program will convert 50 cache misses to cache hits while leaving the other
50 be cache misses. This case will happen if and only if the cache latency (X) is between
31 < X < 60
With runahead: misses _Y + ALU_ 1 + hits 10+3 instructions at the end of the
_∗_ _∗_ _∗_
loop+100 ALU in Runahead mode
_∗_
With runahead: 3 + 30 1 100 + 50 10 + 100 _Y + 100X = 3503 + 100Y + 100(X_ 1)
_∗_ _∗_ _∗_ _∗_ _−_

(f) Assume the energy parameters in part d. What is the dynamic energy consumption of the processor with Runahead execution in terms of X and Y when X generates the maximum number
of cache misses? Show your work.


-----

Initials:

#### 8. [Bonus] Mystery Instruction Strikes Back [[50 points]]

That pesky engineer implemented yet another mystery instruction on the LC-3b. It is your job to
determine what the instruction does. The mystery instruction is encoded as:

15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

1010 DR SR1 0 0 0 0 0 0

The modifications we make to the LC-3b datapath and the microsequencer are highlighted in the
attached figures (see the next three pages after the question). We also provide the original LC-3b
state diagram, in case you need it.

In this instruction, we specify SR2OUT to always output REG[SR1], and SR2MUX to output value
from the REGFILE. Each register has a width of 16 bits.

The additional control signals are:

**GateTEMP1/1: NO, YES**

**GateTEMP2/1: NO, YES**

**LD.TEMP1/1: NO, LOAD**

**LD.TEMP2/1: NO, LOAD**

**ALUK/3: OR1 (A** 0x1), XOR (A ˆ B), LSHF1 (A<<1), PASSA, PASS0 (Pass value 0), PASS16
_|_
(Pass value 16)

**Reg IN MUX/2: BUS (passes value from BUS), EQ0 (passes the value from the ==0?** comparator). BUS is asserted if this signal is not specified.

**COND/4:**
COND0000 ;Unconditional
COND0001 ;Memory Ready
COND0010 ;Branch
COND0011 ;Addressing mode
COND0100 ;Mystery 1
COND1000 ;Mystery 2 (which is set based on the 0th bit of TEMP1)

The microcode for the instruction is given in the table on the next page.

|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1010||||DR|||SR1|||0|0|0|0|0|0|


-----

Initials:

State Cond J

001010 (10) COND0000 001011

001011 (11) COND0000 101000

101000 (40) COND0000 100101

100101 (37) COND1000 101101

111101 (61) COND0000 101101

101101 (45) COND0000 111111

111111 (63) COND0100 100101

110101 (53) COND0000 010010

Describe what this instruction does.

Determines if the 16-bit value stored in SR1 is a Palindrome itself.

**Code:**

State 10: DR 0
_←_
State 11: TEMP1 value(SR1)
_←_
State 40: TEMP2 16
_←_
State 37: DR = DR << 1
if (TEMP1[0] == 0)
goto State 45
else
goto State 61
State 61: DR = DR | 0x1
State 45: TEMP1 = TEMP1 >> 1
State 63: DEC TEMP2
if (TEMP2 == 0)
goto State 53
else
goto State 37
State 53: DR = DR ˆ SR1

|State|Cond|J|Asserted Signals|
|---|---|---|---|
|001010 (10)|COND 0000|001011|ALUK = PASS0, GateALU, LD.REG, DRMUX = DR (IR[11:9])|
|001011 (11)|COND 0000|101000|ALUK = PASSA, GateALU, LD.TEMP1, SR1MUX = SR1 (IR[8:6])|
|101000 (40)|COND 0000|100101|ALUK = PASS16, GateALU, LD.TEMP2|
|100101 (37)|COND 1000|101101|ALUK = LSHF1, GateALU, LD.REG, SR1MUX = DR, DRMUX = DR (IR[11:9])|
|111101 (61)|COND 0000|101101|ALUK = OR1, GateALU, LD.REG, SR1MUX = DR, DRMUX = DR (IR[11:9])|
|101101 (45)|COND 0000|111111|GateTEMP1, LD.TEMP1|
|111111 (63)|COND 0100|100101|GateTEMP2, LD.TEMP2|
|110101 (53)|COND 0000|010010|GateALU, ALUK = XOR, SR1MUX = DR (IR[11:9]) LD.REG, DRMUX = DR (IR[11:9]), Reg IN MUX = EQ0|


-----

|R2 UT SR1 OUT|Col2|
|---|---|
|16 16||
|||


LD.IR IR

|Col1|Col2|
|---|---|
|N|Z P|

|INPUT KBDR KBSR|Col2|Col3|OUTPUT DDR DSR|Col5|Col6|
|---|---|---|---|---|---|
|||||DSR||
|||||||
|||||||
|||||||

|Initials:|Col2|
|---|---|
|||
|GateMARMUX GatePC 16 == 0 ? 16 16 16 16 LD.TEMP2 16 REG_IN TEMP2 MUX LD.PC PC DEC +2 MARMUX 2 BY 1 PCMUX REG GateTEMP2 16 16 FILE 3 + LD.REG DR MYSTERY 3 SR2 SR1 3 SR2 OUT OUT SR1 SIGNAL 2 ZEXT & [0] LSHF1 LSHF1 ADDR1MUX 16 LD.TEMP1 16 TEMP1 [7:0] 2 RSHF ADDR2MUX 16 16 16 16 BY 1 16 16 16 16 [10:0] GateTEMP1 0 16 SEXT [8:0] SR2MUX SEXT [5:0] SEXT CONTROL [4:0] SEXT R IR Mystery SIGNAL 1 2 B A 6 LD.CC N Z P ALU SHF IR[5:0] 16 ALUK == 0 ? LOGIC 16 16 GateALU GateSHF 16||
|||


-----

Initials:


-----

Initials:


##### C.4. THE CONTROL STRUCTURE 11


IR[11:9]

111


DR


IR[11:9]

IR[8:6]

SR1MUX


SR1


DRMUX

(a)


(b)


IR[11:9]

N Logic BEN
Z
P

##### (c)

 Figure C.6: Additional logic required to provide control signals

|11:9]|Col2|Col3|
|---|---|---|
||Logic|BEN|
||||
||||
||||
||||


##### LC-3b to operate correctly with a memory that takes multiple clock cycles to read or store a value. Suppose it takes memory five cycles to read a value. That is, once MAR contains the address to be read and the microinstruction asserts READ, it will take five cycles before the contents of the specified location in memory are available to be loaded into MDR. (Note that the microinstruction asserts READ by means of three control signals: MIO.EN/YES, R.W/RD, and DATA.SIZE/WORD; see Figure C.3.) Recall our discussion in Section C.2 of the function of state 33, which accesses an instruction from memory during the fetch phase of each instruction cycle. For the LC-3b to operate correctly, state 33 must execute five times before moving on to state 35. That is, until MDR contains valid data from the memory location specified by the contents of MAR, we want state 33 to continue to re-execute. After five clock cycles, th h l t d th “ d ” lti i lid d t i MDR th


-----

Initials:

To 8

1

DR<! SR1+OP2*
set CC

To 18 5

DR<! SR1&OP2*
set CC

9

To 18

DR<! SR1 XOR OP2*

set CC

To 18 15


To 19


To 18


18, 19

33

35

LDW

6

MAR<! B+LSHF(off6,1)

MDR<! M[MAR]

R

DR<! MDR
set CC

To 18


To 18


##### Figure C.2: A state machine for the LC-3b


-----

Initials:

#### Scratchpad


-----

Initials:

#### Scratchpad


-----

