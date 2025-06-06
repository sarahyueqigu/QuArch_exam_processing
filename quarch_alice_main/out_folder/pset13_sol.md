10/30/2021

## Problem M13.1: Sequential Consistency 

**Problem M13.1.A**

Can X hold value of 4 after all three threads have completed? Please explain briefly.

Yes  /  No

C1-C4, B1-B3, A1-A4, B4- B6

**Problem M13.1.B**

Can X hold value of 5 after all three threads have completed?

Yes  /  No

All results must be even!

**Problem M13.1.C**

Can X hold value of 6 after all three threads have completed?

Yes  /  No

All of C, All of A, All of B

**Problem M13.1.D**

For this particular program, can a processor that reorders instructions but follows local
dependencies produce an answer that cannot be produced under the SC model?

Yes  /  No

All stores/loads must be done in order because they’re to the same address, so no new results are
possible.


-----

10/30/2021

## Problem M13.2: Relaxed Memory Models [? Hours]

We will study the interaction between two processes on different processors on such a system:
```
            P1 P2
       P1.1: LW R2, 0(R8) P2.1: LW R4, 0(R9)
       P1.2: SW R2, 0(R9) P2.2: SW R5, 0(R8)
       P1.3: LW R3, 0(R8) P2.3: SW R4, 0(R8)

```
**Problem M13.2.A**

Memory contents

M[R8] 7

M[R9] 6

**Yes     No**

P1.1 P2.1 P1.2 P1.3 P2.2 P2.3

**Problem M13.2.B**

memory Contents

M[R8] 6

M[R9] 7

**Yes     No**

The result would require that the memory contents don’t change. Since each thread reads a data
value and writes it to another address, this simply impossible here.

**Problem M13.2.C**

Is it possible for M[R8] to hold 0?

**Yes     No**

The only way that M[R8] could end up with 0 is if P2.3 is completed before P2.1 and P2.2. This
violates Weak Ordering, so it is not possible.

Now consider the same program, but with two MEMBAR instructions.

|P1|P2|
|---|---|
|P1.1: LW R2, 0(R8)|P2.1: LW R4, 0(R9)|
|P1.2: SW R2, 0(R9)|P2.2: SW R5, 0(R8)|
|P1.3: LW R3, 0(R8)|P2.3: SW R4, 0(R8)|

|Memory|contents|
|---|---|
|M[R8]|7|
|M[R9]|6|

|memory|Contents|
|---|---|
|M[R8]|6|
|M[R9]|7|


-----

10/30/2021
```
            P1 P2
       P1.1: LW R2, 0(R8) P2.1: LW R4, 0(R9)
       P1.2: SW R2, 0(R9)  MEMBARRW
           MEMBARWR P2.2: SW R5, 0(R8)
       P1.3: LW R3, 0(R8) P2.3: SW R4, 0(R8)

```
We want to compare execution of the two programs on our system.

Here the intention was to keep the starting conditions the same as in first three questions, and ask
about the final conditions. This wasn’t clear, so we accepted both solutions. The yes/no
answers don’t actually change, but Questions 11 for 12 become simpler.

**Problem M13.2.D**

If both M[R8] and M[R9] contain 6, is it possible for R3 to hold 8?

Without MEMBAR instructions? **Yes    No**

With MEMBAR instructions? **Yes    No**

Following sequence works with and without MEMBAR instructions:
P1.1 -> P1.2 -> P2.1 -> P2.2 -> P1.3 -> P2.3

**Problem M13.2.E**

If both M[R8] and M[R9] contain 7, is it possible for R3 to hold 6?

Without MEMBAR instructions? **Yes    No**

With MEMBAR instructions? **Yes    No**

If M[R8] and M[R9] are to end up with 7, we have to execute P2.3 before we execute P1.1 Since
P1.3 has to come after P1.1 (Weak Ordering), R3, has to end up with 7 not 6.

|P1|P2|
|---|---|
|P1.1: LW R2, 0(R8)|P2.1: LW R4, 0(R9)|
|P1.2: SW R2, 0(R9)|MEMBAR RW|
|MEMBAR WR|P2.2: SW R5, 0(R8)|
|P1.3: LW R3, 0(R8)|P2.3: SW R4, 0(R8)|


-----

10/30/2021

**Problem M13.2.F**

Is it possible for both M[R8] and M[R9] to hold 8?

Without MEMBAR instructions? **Yes    No**

P2.2 P1.1 P1.2 P2.1 P2.3 P1.3

With MEMBAR instructions? **Yes    No**

The sequence above violates the MEMBAR in P2—P2.2 executes before P2.1. That is the only
way to get 8 into both memory locations, thus the result is impossible with MEMBARs insterted.


-----

10/30/2021

## Problem M13.3: Memory Models

Consider a system which uses Sequential Consistency (SC). There are three processes, P1, P2
and P3, on different processors on such a system (the values of RA, RB, RC were all zeros
before the execution):
```
     P1 P2 P3
P1.1: ST (A), 1 P2.1: ST (B), 1  P3.1: ST (C), 1
P1.2: LD RC, (C) P2.2: LD RA, (A) P3.2: LD RB, (B)

```
**Problem M13.3.A**

After all processes have executed, it is possible for the system to have multiple machine states. For
example, {RA, RB, RC}= {1,1,1} is possible if the execution sequence of instructions is
```
P1.1→P2.1→P3.1→P1.2→P2.2→P3.2. Also, {RA, RB, RC}= {1,1,0} is possible

```
if the sequence is P1.1 → P1.2 → P2.1 → P3.1 → P2.2 → P3.2.

For each state of {RA, RB, RC} below, specify the execution sequence of instructions that
results in the corresponding state. If the state is NOT possible with SC, just put X.

# {0,0,0} : X
 {0,1,0} : P2.1 P2.2 P1.1P1.2P3.1 P3.2
 {1,0,0} : P1.1 P1.2 P3.1 P3.2 P2.1 P2.2
 {0,0,1} : P3.1 P3.2 P2.1 P2.2 P1.1 P1.2

|P1|P2|P3|
|---|---|---|
|P1.1: ST (A), 1 P1.2: LD R , (C) C|P2.1: ST (B), 1 P2.2: LD R , (A) A|P3.1: ST (C), 1 P3.2: LD R , (B) B|


-----

10/30/2021

**Problem M13.3.B**

Now consider a system which uses **Weak Ordering(WO), meaning that a read or a write may**
complete before a read or a write that is earlier in program order if they are to different addresses
and there are no data dependencies.

Does WO allow the machine state(s) that is not possible with SC? If yes, provide an execution
sequence that will generate the machine states(s).

Yes. {0,0,0} by P1.2→P2.2→P3.2→P1.1→P2.1→P3.1

**Problem M13.3.C**

The WO system in Problem M13.3.B provides four fine-grained memory barrier instructions.
Below is the description of these instructions.
```
- MEMBARRR guarantees that all read operations initiated before the MEMBARRR will be seen

```
before any read operation initiated after it.
```
- MEMBARRW guarantees that all read operations initiated before the MEMBARRW will be seen

```
before any write operation initiated after it.
```
- MEMBARWR guarantees that all write operations initiated before the MEMBARWR will be seen

```
before any read operation initiated after it.
```
- MEMBARWW guarantees that all write operations initiated before the MEMBARWW will be seen

```
before any write operation initiated after it.

Using the minimum number of memory barrier instructions, rewrite P1, P2 and P3 so the machine
state(s) that is not possible with SC by the original programs is also not possible with WO by your
programs.

|P1|P2|P3|
|---|---|---|
|P1.1: ST (A), 1 MEMBAR WR P1.2: LD R , (C) C|P2.1: ST (B), 1 MEMBAR WR P2.2: LD R , (A) A|P3.1: ST (C), 1 MEMBAR WR P3.2: LD R , (B) B|


-----

10/30/2021

## Problem M13.4: Memory consistency models (Spring 2016 Quiz 3, Part B)

Consider two processes P1 and P2 running on two different processors.
**Assume that memory locations X and Y contain initial value 0.**

## P1 P2

 P1.1: LD R1 ß (Y) P2.1: ST (X) ß 1 P1.2: LD R2 ß (X) P2.2: ST (Y) ß 1

**Problem M13.4.A**

Out of the following possible final values of (X, Y, R1, R2), circle the ones that could occur
if the system is Sequentially Consistent (SC).

## (0,0,0,0) (0,0,0,1) (0,0,1,0) (0,0,1,1)

 (1,1,0,0) (1,1,0,1) (1,1,1,0) (1,1,1,1)

**Problem M13.4.B**

Out of the following possible final values of (X, Y, R1, R2), circle the ones that could occur
if the system enforces RMO, a weak memory model where loads and stores can be reordered
**after prior loads or stores.**

## (0,0,0,0) (0,0,0,1) (0,0,1,0) (0,0,1,1)

 (1,1,0,0) (1,1,0,1) (1,1,1,0) (1,1,1,1)

|P1|P2|
|---|---|
|P1.1: LD R1 ß (Y) P1.2: LD R2 ß (X)|P2.1: ST (X) ß 1 P2.2: ST (Y) ß 1|


-----

10/30/2021

**Problem M13.4.C**

The RMO machine has the following fine-grained barrier instructions:

  - **MEMBARRR guarantees that all reads initiated before MEMBARRR will be performed before**

any read initiated after it.

  - **MEMBARRW guarantees that all reads initiated before MEMBARRW will be performed before**

any write initiated after it.

  - **MEMBARWR guarantees that all writes initiated before MEMBARWR will be performed before**

any read initiated after it.

  - **MEMBARWW guarantees that all writes initiated before MEMBARWW will be performed before**

any write initiated after it.

Use the minimum number of memory barrier instructions, rewrite P1 and P2 such that the
**RMO machine produces the same outputs as the SC machine for the given code.**

|P1|P2|
|---|---|
|P1.1: LD R1 ß (Y) MEMBAR RR P1.2: LD R2 ß (X)|P2.1: ST (X) ß 1 MEMBAR WW P2.2: ST (Y) ß 1|


-----

10/30/2021

Again, consider two processes P1 and P2 running the code below on two different processors.
**Assume that memory locations X, Y, and Z contain initial value 0.**

## P1 P2

 P1.1: LD R1 ß (Z) P2.1: ST (X) ß 1 P1.2: ST (Y) ß 1 P2.2: LD R3 ß (Y) P1.3: LD R2 ß (X) P2.3: ST (Z) ß 1

**Problem M13.4.D**

Out of the following possible final values of (R1, R2, R3), circle the ones that could occur if
the system is Sequentially Consistent (SC).

## (0,0,0) (0,1,0) (1,0,0) (1,1,0)

 (0,0,1) (0,1,1) (1,0,1) (1,1,1)

**Problem M13.4.E**

Out of the following possible final values of (R1, R2, R3), circle the ones that could occur if
the system enforces RMO (loads and stores can be reordered after prior loads or stores).

## (0,0,0) (0,1,0) (1,0,0) (1,1,0)

 (0,0,1) (0,1,1) (1,0,1) (1,1,1)

|P1|P2|
|---|---|
|P1.1: LD R1 ß (Z) P1.2: ST (Y) ß 1 P1.3: LD R2 ß (X)|P2.1: ST (X) ß 1 P2.2: LD R3 ß (Y) P2.3: ST (Z) ß 1|


-----

10/30/2021

**Problem M13.4.F**

Using the minimum number of memory barrier instructions (given in Question 3), rewrite P1
and P2 such that the RMO machine produces the same outputs as the SC machine for the
**given code.**

|P1|P2|
|---|---|
|P1.1: LD R1 ß (Z) MEMBAR RW P1.2: ST (Y) ß 1 MEMBAR WR P1.3: LD R2 ß (X)|P2.1: ST (X) ß 1 MEMBAR WR P2.2: LD R3 ß (Y) MEMBAR RW P2.3: ST (Z) ß 1|


-----

