Name:

First Name:

Student ID:

### 2nd session examination
# Design of Digital Circuits SS2013

### (252-0014-00S)

#### Markus P¨uschel, Frank K. G¨urkaynak

Examination Rules:

1. Written exam, 90 minutes total.

2. No books, no calculators, no computers or communication devices. Five pages of
handwritten notes are allowed.

3. Write all your answers on this document, space is reserved for your answers after each
question. Blank pages are available at the end of the exam.

4. Put your Student ID card visible on the desk during the exam.

5. If you feel disturbed, immediately call an assistant.

6. Answers will only be evaluated if they are readable

7. Write with a black or blue pen (no pencil, no green or red color).

8. Show all your work. For some questions, you may get partial credit even if the end
result is wrong due to a calculation mistake.

|Question:|1|2|3|4|5|6|7|Total|
|---|---|---|---|---|---|---|---|---|
|Points:|5|16|15|18|5|10|6|75|
|Score:|||||||||


-----

Design of Digital Circuits 5th of February 2014

_This page intentionally left blank_

Second Session Exam Page 1 of 17


-----

Design of Digital Circuits 5th of February 2014

1. (a) (2 points) For the following four numbers given in decimal or hexadecimal notation, write the corresponding binary number using the indicated format.

(−6)10 using 6-bit sign magnitude: (10 0110)2

(37)10 using 6-bit unsigned: (10 0101)2

(−28)10 using 6-bit two’s complement: (10 0100)2

(2B)16 using 6-bit unsigned: (10 1011)2

(b) (3 points) State whether the following statements about the binary representation
of numbers are true or false. Give brief explanations for the statements that are
_false._

     - Both two’s complement and sign/magnitude representation can be used to represent negative numbers in binary.

**Solution: True, however it is more difficult to design arithmetic circuits**
that work with sign/magnitude format. Still they are used.

      - Using N bits it is possible to represent 2[N] different numbers when an unsigned
number system is used.

**Solution: True.**

      - While there are methods to represent both positive and negative integers, it is
not possible to represent fractions or real numbers using binary numbers.

**Solution: False, fixed and floating point number systems can be used to**
represent such numbers.

Second Session Exam Page 2 of 17


-----

Design of Digital Circuits 5th of February 2014

2. Consider the following state diagram of an FSM with 1-bit input (I) and 1-bit output
(Z).

```
 Reset

```
**A**
```
  Z=1
I=1

```
```
I=1

```

The state has been coded using a 3-bit vector S = S2 S1 S0 according to the following
table:

**State**

name _S2_ _S1_ _S0_

A 0 0 0

B 0 0 1

C 0 1 0

D 0 1 1

E 1 0 0

F 1 0 1

(a) (1 point) Is this a Moore or Mealy type FSM? Briefly explain.

**Solution: Moore, outputs depend only on the present state and nothing else.**

Second Session Exam Page 3 of 17

|State|Col2|Col3|Col4|
|---|---|---|---|
|name|S 2|S 1|S 0|
|A|0|0|0|
|B|0|0|1|
|C|0|1|0|
|D|0|1|1|
|E|1|0|0|
|F|1|0|1|


-----

Design of Digital Circuits 5th of February 2014

(b) (6 points) Fill in the following state transition table that determines the next state
vector N = N2 N1 N0 based on the current state S and the input I.

**State** **Input** **Next State**

name _S2_ _S1_ _S0_ _I_ name _N2_ _N1_ _N0_

A 0 0 0 X B 0 0 1

B 0 0 1 0 C 0 1 0

B 0 0 1 1 E 1 0 0

C 0 1 0 0 D 0 1 1

C 0 1 0 1 A 0 0 0

D 0 1 1 0 D 0 1 1

D 0 1 1 1 A 0 0 0

E 1 0 0 X F 1 0 1

F 1 0 1 0 E 1 0 0

F 1 0 1 1 C 0 1 0

_Note that there are different ways of writing this table to represent the same result._

(c) (3 points) Write the Next State Equations from the table you have filled above
using either Product of Sums (POS) or Sum of Products (SOP) form. Do not
**spend time minimizing the equations, this will be next question.**

**Solution:**
_N0 = S2 S1 S0 + S2 S1 S0 I + S2 S1 S0 I + S2 S1 S0_

_N1 = S2 S1 S0 I + S2 S1 S0 I + S2 S1 S0 I + S2 S1 S0 I_

_N2 = S2 S1 S0 I + S2 S1 S0 + S2 S1 S0 I_

Second Session Exam Page 4 of 17

|State|Col2|Col3|Col4|Input|Next State|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|name|S 2|S 1|S 0|I|name|N 2|N 1|N 0|
|A|0|0|0|X|B|0|0|1|
|B|0|0|1|0|C|0|1|0|
|B|0|0|1|1|E|1|0|0|
|C|0|1|0|0|D|0|1|1|
|C|0|1|0|1|A|0|0|0|
|D|0|1|1|0|D|0|1|1|
|D|0|1|1|1|A|0|0|0|
|E|1|0|0|X|F|1|0|1|
|F|1|0|1|0|E|1|0|0|
|F|1|0|1|1|C|0|1|0|


-----

Design of Digital Circuits 5th of February 2014

(d) (6 points) Minimize the Next State Equations from the previous part. Note that
the FSM requires only six states. This means that there are several State (S) /
Input(I) combinations for which the outputs can be treated as Don’t Care, which
should help minimizing the boolean equations.
_Hint: Consider using Karnaugh diagrams to solve this problem._

**Solution:**
It is important to note that for S2 S1 = 11 the next state N can be taken as
_N2 N1 N0 = XXX. This can simplify the Boolean equations significantly. It is_
best to use a Karnaugh map to find the simplifications.
```
        S0I S0I S0I
      S2S1 00 01 11 10 S2S1 00 01 11 10 S2S1 00 01 11 10

```
`00` **1** **1** 0 0 `00` 0 0 0 **1** `00` 0 0 **1** 0

`01` **1** 0 0 **1** `01` **1** 0 0 **1** `01` 0 0 0 0

`11` **X** **X** **X** **X** `11` **X** X **X** **X** `11` **X** **X** X **X**

`10` **1** **1** 0 0 `10` 0 0 **1** 0 `10` **1** **1** 0 **1**
```
      N0 N1 N2

```
_N0 = S1 S0 + S1 I_

_N1 = S1 I + S2 S0 I + S2 S0 I_

_N2 = S2 S0 + S2 I + S2 S1 S0 I_

Second Session Exam Page 5 of 17

|1|1|0|0|
|---|---|---|---|
|1|0|0|1|
|X|X|X|X|
|1|1|0|0|

|0|0|0|1|
|---|---|---|---|
|1|0|0|1|
|X|X|X|X|
|0|0|1|0|

|0|0|1|0|
|---|---|---|---|
|0|0|0|0|
|X|X|X|X|
|1|1|0|1|


-----

Design of Digital Circuits 5th of February 2014

_This page intentionally left blank_

Second Session Exam Page 6 of 17


-----

Design of Digital Circuits 5th of February 2014

3. (15 points) In this question you are required to write the Verilog code that implements
the following block diagram.
```
   Reset
                        InstLeft
    In1 A
                                Left

```
`In2` `B` **comb** `Z`
```
    In3 C
                                                 reset
                                       0

```
**MUX** `MuxOut` **DFF** `Result`
```
                        InstRight
                                       1
                    A
                                Right

```
`B` **comb** `Z`
```
                    C
    Sel
    Clk

```
The block called Controller has six 1-bit inputs and a single 1-bit output (Result).
It contains two instances of a combinational block called (comb). The following is the
declaration part of this module:

1 **module comb ( input A, input B, input C, output Z);**

2 _// definition of the combinational circuit comb_

3

4 **endmodule**

Notes:

    - The flip-flop and the multiplexer will not be instantiated, you will have to write
the corresponding Verilog code.

    - The flip-flop uses an asynchronous reset, the output is zero when reset is one.

    - Note that Verilog is case sensitive.

    - Write legibly.

Second Session Exam Page 7 of 17


-----

Design of Digital Circuits 5th of February 2014

_This page intentionally left blank_

**Solution:**

1 **module Controller (**

2 **input Clk,**

3 **input Reset,**

4 **input In1,In2,In3,**

5 **input Sel,**

6 **output reg Result);**

7

8 _// Define internal signals_

9 **wire Left, Right, MuxOut;**

10

11 _// instantiate the module comb two times_

12 comb InstLeft (.A(In1), .B(In2), .C(In3), .Z(Left) );

13 comb InstRight (.A(In3), .B(In2), .C(In1), .Z(Right) );

14

15 _// The multiplexer_

16 **assign MuxOut = (Sel) ? Right: Left;**

17

18 _// The FF_

19 **always @ (posedge Clk, posedge Reset)**

20 **if (Reset) Result <= 1’b0;**

21 **else** Result <= MuxOut;

22

23 **endmodule**

Second Session Exam Page 8 of 17


-----

Design of Digital Circuits 5th of February 2014

4. In this question you are required to calculate different timing paths for the circuit given
below.

**A** **B** **C**
```
                                                0

```
**2:1**
**MUX**
```
                                                1

```
**B** **D**

Note that the block B is used twice. All the inputs are supplied from external registers.
The timing properties of all the blocks used in the circuit are given in the table below:

Block Propagation Delay Contamination Delay Setup Time

Register 0.0 ns 0.0 ns 0.1 ns

2:1 Multiplexer 0.3 ns 0.3 ns n.a.

A 0.6 ns 0.4 ns n.a.

B 1.8 ns 1.0 ns n.a.

C 1.2 ns 0.8 ns n.a.

D 1.0 ns 0.8 ns n.a.

_Hint:_ 1

1 ns [= 1][ GHz][, a clock with 1 GHz has a period of 1 ns. 1 GHz = 1000 MHz]

Second Session Exam Page 9 of 17

|Block|Propagation Delay|Contamination Delay|Setup Time|Hold Time|
|---|---|---|---|---|
|Register|0.0 ns|0.0 ns|0.1 ns|0.0 ns|
|2:1 Multiplexer|0.3 ns|0.3 ns|n.a.|n.a.|
|A|0.6 ns|0.4 ns|n.a.|n.a.|
|B|1.8 ns|1.0 ns|n.a.|n.a.|
|C|1.2 ns|0.8 ns|n.a.|n.a.|
|D|1.0 ns|0.8 ns|n.a.|n.a.|


-----

Design of Digital Circuits 5th of February 2014

(a) (2 points) What is the critical path of this circuit? Calculate its path delay.

**Solution:**
Critical path is the longest timing path in the circuit:

_CriticalPath =_ _tpd,A + tpd,B + tpd,C + tpd,mux + tsetup,FF_
= 0.6 + 1.8 + 1.2 + 0.3 + 0.1 ns
= 4.0 ns

(b) (1 point) What is the maximum operating frequency of this circuit?

**Solution: Maximum operating frequency is 1/Critical Path, 1/4 ns = 250 MHz.**

(c) (2 points) What is the shortest path of this circuit ?

**Solution: The short path is the fastest route a signal can propagate through**
the circuit. In this case it is the signal that goes through the select input of
the multiplexer and reaches the register. This signal only passes through the
multiplexer, so the short path is 0.3 ns.

Second Session Exam Page 10 of 17


-----

Design of Digital Circuits 5th of February 2014

(d) (8 points) In order to make the circuit faster, it is suggested to introduce pipelining.
Determine the best location between the blocks to place the pipeline registers
assuming a one stage pipeline implementation and redraw the schematic. (Hint:
_in a one stage pipeline, the latency increases only by 1 clock cycle)._

**Solution:**

**A** **B** **C**
```
                                                             0

```
**2:1**
**MUX**
```
                                                             1

```
**B** **D**

Note that you will have to insert a pipeline register in all paths, including the
multiplexer control register.

(e) (2 points) What is the critical path of this pipelined circuit and calculate its path
delay.

**Solution:**

_CriticalPath =_ _tpd,A + tpd,B + tsetup,FF_
= 0.6 + 1.8 + 0.1 ns
= 2.5 ns

Second Session Exam Page 11 of 17


-----

Design of Digital Circuits 5th of February 2014

(f) (1 point) What is the speed-up we have achieved by pipelining?

**Solution: Old critical path / New Critical path = 4.0 / 2.5 = 1.6. The new**
circuit has a 60% shorter critical path, therefore it can be clocked 60% faster.

(g) (2 points) Why did we not achieve the theoretical maximum speed-up from the
pipelining. State at least two reasons.

**Solution:**

1. It was not possible to place the pipeline registers at exactly half the previous critical path. Unless we move the pipeline registers into the blocks
themselves we can not improve any more.

2. The pipeline register has a small overhead (tsetup,FF > 0). Even if we
managed to divide the circuit in equal halves, this overhead would not
allow us to reach 100% speedup. The problem gets worse the shorter the
critical path is.

Second Session Exam Page 12 of 17


-----

Design of Digital Circuits 5th of February 2014

5. The questions 5, 6 and 7 are based on the MIPS assembly code given below.

#### addi $t0, $0, 8 xor $s0, $s0, $s0
 loop: beq $t0, $0, done
 lw $t1, 0x4($0)
 lw $t2, 0x24($0)
 add $t3, $t1, $s0
 add $s0, $t2, $t3
 addi $t0, $t0, -1 j loop
 done:

(a) (2 points) Briefly explain what the above MIPS assembly code does.

**Solution:**
The program will execute a loop 8 times. In each iteration of the loop, the
content of the address 0x0000 0004 and the content of the address 0x0000
0024 will be added together and added to the register $s0 which was initialized
to the value 0 (A xor A is 0).

(b) (1 point) Assuming the data at memory location 0x0000 0004 is decimal 16 and
at memory location 0x0000 0024 is decimal 32, what will be the content of the
register $s0 in hexadecimal when the program execution jumps to done:?

**Solution: The program calculates 8** (mem(0x00000004)+mem(0x00000024)).
_×_
This equals to 8 (32 + 16) == 384. In hexadecimal this will be 0x0180. It is
_×_
actually very easy to do the calculation if you do it in binary.

Second Session Exam Page 13 of 17


-----

Design of Digital Circuits 5th of February 2014

(c) (2 points) Briefly explain the three different MIPS instruction types (R, I, J) and
show one instruction of each type from the example code above.

**Solution:**

**R-type Uses up to three registers, two for source and one for destination.**
Example: xor $s0, $s0, $s0.

**I-type Uses a 16-bit constant as part of the instruction.**
Example: addi $t0, $0, 8.

**J-type Uses a 26-bit constant that can be used to calculate the address of**
the next instruction, allowing the program execution to jump to a new
location.
Example: j loop.

Second Session Exam Page 14 of 17


-----

Design of Digital Circuits 5th of February 2014

6. In this question you are required to make calculations regarding the processor’s speed.
For this question, use the MIPS assembly program from the previous section.

(a) (2 points) How many instructions are executed until the program finishes?

**Solution: There are two initial instructions, and the loop contains 7 instruc-**
tions which is executed 8 times, in addition there is one last beq command that
will be executed after the last loop. Ninstructions = 2 + (7 × 8) + 1 = 59 (56, or
58 could also be accepted)

(b) (1 point) Assume that you are using a single cycle microarchitecture running at
1 GHz. If the CPI (Cycles Per Instruction) is 1, how long will it take for the
program to finish execution?

**Solution: 59 instructions x 1 CPI = 59 clock cycles. At 1 GHz, 1 clock cycles**
is 1 ns, so the entire program will execute in 59 ns.

(c) (2 points) In a second microarchitecture, due to a very slow memory, every load
_word (lw) instruction requires 10 clock cycles._ Calculate the number of cycles
needed to execute the entire program.

**Solution: The loop contains 2 lw instructions each take 10 clock cycles. The**
remaining 5 instructions take 1 clock cycle. Every loop takes 25 clock cycles.
There are 8 iterations of the loop plus two additional initial instructions and
one last beq: Ncycles = 2 + (8 × (5 × 1 + 2 × 10) + 1 = 203 (200, or 202 could
also be accepted)

(d) (1 point) For this second microarchitecture, what is the average CPI? (approximate
_numbers_ _10% are ok )_
_±_

**Solution: There are 59 instructions that are executed in 203 clock cycles.**
_CPI = 203/59 = 3.44. Acceptable are also approximate calculations CPI =_
200/60 = 3.33 or CPI = 210/60 = 3.5

Second Session Exam Page 15 of 17


-----

Design of Digital Circuits 5th of February 2014

(e) (4 points) For the second microarchitecture with the slow memory, what can be
done in both the code and the processor to improve the speed of this particular
program other than using a faster memory. Write two short suggestions that would
have the largest impact and briefly explain why that would improve the performance.
_Note: The result of the program should depend on the two values stored in the_
_memory, these can not assumed to be constants._

**Solution:**

       - The most obvious problem is the slow memory access. Introducing a
proper cache could alleviate this problem. The first iterations would still
be slow, but the remaining accesses would be fast.

       - The program could be written more efficiently. The loop essentially multiplies the sum of the two values in memory by eight. Instead of a loop, a
shift left operation could be used.

#### lw $t1, 0x4($0)
 lw $t2, 0x24($0)
 add $s0, $t1, $s2
 sll $s0, $s0, 3

       - Standard pipelining will not work in this architecture, there are two consecutive memory accesses which are the problem, all other instructions
can already be calculated in a single cycle.

       - Using a better technology would increase the speed. However, this is not
one of the easiest solutions. The first two solutions are clearly better
suited.

Second Session Exam Page 16 of 17


-----

Design of Digital Circuits 5th of February 2014

7. (6 points) A friend suggests adding a cache system to speed up the execution of MIPS
assembly code on the micro-architecture from question 6 (slow load word (lw) instruction
that requires 10 clock cycles for memory access).

Which of the two cache design options would make the program in question 5 run faster?
Briefly explain why.

**Solution A A direct-mapped cache with a capacity of 8 words and an access time of**
_tcache = 1 clock cycle_

**Solution B A two-way set associative cache with the same capacity of 8 words, but**
with twice the access time tcache = 2 clock cycles.

_Note: The question is specific to the program in question 5 and not about speeding up_
_any arbitrary program._

**Solution:**

In a direct mapped cache, there is only one location where data can be placed in
a cache. In a direct mapped cache with 8 locations, the address 0x0000 0004
and 0x0000 0024 would map to the same cache location. If this cache is used,
every memory access would result in a cache miss. Using solution A would make the
program run even slower, as every memory access would have first a cache miss (1
clock cycle) followed by the actual memory access (10 cycles).
_Ncycles = 2 + (8 × (5 + 2 × 11)) = 218_

**Solution A can not be used to speed up the program.**

In a 2-way set associative memory, there are two locations where data can be placed
in a cache. Although the addresses 0x0000 0004 and 0x0000 0024 still map to
the same set, they can both be placed in the cache. The first two memory accesses
would be compulsory misses requiring 12 clock cyles (2 for the cache miss plus 10 for
the actual memory access). But for the following 7 iterations, every memory access
would be a cache hit, requiring only 2 clock cycles.
_Ncycles = 2 + (7 × (5 + 2 × 2)) + (5 + 2 × 12) = 94_

**Solution B is the only viable alternative, that would speed up the program by**
more than 2x.

Note that the program used is virtually identical to the one used in class notes to
explain the problems with Direct-mapped cache.

Second Session Exam Page 17 of 17


-----

