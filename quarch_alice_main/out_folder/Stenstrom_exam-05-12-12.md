2005-12-07

Exam in Computer Architecture (EDA111)

**Time: December 12, 2005 before lunch in the M building**

**Person in charge of the exam: Charlotta Bååth, phone: xxxxxxx**

**Supporting material/tools: None**

**Exam Review: January 9, 2005 between 9-11 in YYY**

**Grading intervals:**

- **Fail: Result < 20**

- **Grade 3: 20 <= Result < 29**

- **Grade 4: 30 <= Result < 39**

- **Grade 5: 40 <= Result**

**Important note: Answers can be given in Swedish. The reason this exam is presented in**
English is that the course is also offered to the International Master’s Program on
Dependable Computer Systems.

**GOOD LUCK!**
**_Per Stenström_**

CHALMERS UNIVERSITY OF TECHNOLOGY
_DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING_
412 96 Göteborg
Visiting address: Rännvägen 5
Phone: 031-772 1761 Fax: 031-772 3663
O N 556479 5598


-----

**ASSIGNMENT 1 (Each partial assignment gives 2 points)**

**A)** **How much has the computing speed increased annually because of clock**
**frequency improvements?**
**B) Suppose that an architectural enhancement can speedup 50% of the execution**
**by a factor of ten. How much faster will a program run after applying the**
**enhancement?**
**C) Suppose that computer A runs 50% more instructions than computer B but has**
**a cycle time that is half the cycle time of B. Further, CPI of A is 25% higher than**
**CPI of B. Which one is faster and by how much?**
**D) Show how the computation A:=B+C is carried out on a stack and on an**
**accumulator machine**
**E) Mention one advantage and one disadvantage of using condition codes.**

**ASSIGNMENT 2**

**A)** The diagram below shows the relative occurrence of conditional branches of
different types for integer and floating-point applications. Let’s assume the
following:

    - Every fifth instruction is a conditional branch

    - All conditional branches can be predicted with 100% accuracy, except for
the “branch less than” category that can be predicted with only 50%
accuracy.

    - CPI=1 for all instructions including the branches that are correctly predicted

    - The misprediction penalty is 10 cycles.
**What is the CPI for the integer applications?** **(4 points)**


-----

B) A computer system requires that the operands are aligned. Which of the following load
**operations are aligned if we assume that they all load 32-bit operands.** **(4 points)**
**Load instruction:** **Content of R2:**

`Load R1, 0(R2)` 0xffff0000

`Load R1, 0(R2)` 0xffff0002

`Load R1, 1(R2)` 0xffff0000

`Load R1, 1(R2)` 0xffff0003

C) What is the role of a register allocation algorithm? **(2 points)**

**ASSIGNMENT 3**

**A)** Consider the following program:
LF F1, 0(R1)
DIVF F4,F2, F1
MULT F2, F1, F0
Further, assume that a floating-point load, division, and multiplication takes 10, 50, and 40
cycles, respectively. **Compute the execution time of the above sequence under the**
**following assumptions:**
i) On a processor that can issue one instruction per cycle and that has no register
renaming capability
ii) On a processor that can issue 3 instructions per cycle and that has no register
renaming capability
iii) On a processor that can issue 3 instructions per cycle and that has register
renaming capability.

[Disclaimer: If you feel that more assumptions have to be made, feel free to do so. If they
are needed and reasonable, they will be accepted without any deduction on the score]
**(4 points)**

**B)** **Explain what happens in the following situations during speculative execution**
**using a reorder buffer?** **(4 points)**
i) Where does a speculatively executed instruction read its operands if they are
produced by another speculatively executed instruction that has not yet
committed?
ii) In what order are speculatively executed instructions inserted into the reorder
buffer?
iii) What actions are taken when an instruction is committed?
iv) What actions are taken when a branch is mispredicted?
**C)** **What is a branch target buffer? (2 points)**

**ASSIGNMENT 4**

**A)** Consider the following program loop:
for i=1 to 10 do
X[i+5]=X[i] + Y[i]
**List all iterations that have a loop-carried dependency with another and what causes**
**this dependency.** **(4 points)**

|Load instruction:|Content of R2:|
|---|---|
|Load R1, 0(R2)|0xffff0000|
|Load R1, 0(R2)|0xffff0002|
|Load R1, 1(R2)|0xffff0000|
|Load R1, 1(R2)|0xffff0003|


-----

**B)** Consider the following code code: if (A==0) then A=B else A=A+4 which is
translated into the following DLX code:
LW R1,0(R3)
BNEZ R1,L1
LW R1,0(R2)
J L2
L1 :     ADD R1,R1, 4
L2 :     SW 0(R3),R1

Assume that the most likely outcome is that the condition (A==0) is true. Rewrite the code
**using (software) speculation to move as many of the instructions corresponding to the**
**most likely code sequence in front of the branch. Make sure that the program**
**semantics is maintained also if the speculation fails.** **(4 points)**
```
C)Show the semantics of a predicated instruction by transforming the following

```
**conditional statement using the predicated ADD R1,R2,R3 instruction: CADD**
**R1,R2,R3,Rc** **(2 points)**

BEQZ Rc, L1
ADD R1,R2,R3
L1: ….
**ASSIGNMENT 5**

**A)** Consider the following diagram that shows the miss rate as a function of the cache
size for cache configurations with various degrees of associativity.

18%

16%

14%

1-way

12%

8-way

10%

8% 2-way

6%

4-way

4%

2% Capacity

0%

1 2 4 8 16 32 64 128
KB KB KB KB KB KB KB KB

**Cache size**

**Answer the following questions:**
**i)** **What is the conflict miss rate for an 8-Kbyte direct-mapped cache?**
**ii)** **What is the cold miss rate and why is it independent of the cache size?**
**iii)** **What is the ratio of the miss rates for a direct-mapped cache of size N**
**versus a 2-way set-associative cache of size N/2? (4 points)**
**B) An address translation look-aside buffer does two things: address translation**
**and protection checking. Explain how these operations are carried out by giving an**
**example assuming that the virtual address is 64 bits, the physical address is 48 bits**


-----

**amd the physical page offset is 16 bits and that a 2-bit protection code is used.**
**(2 points)**

**C) Explain what a test&set instruction does. (2 points)**

**C)** **What is a FLASH memory? (2 points)**

**_*** GOOD LUCK! ***_**


-----

