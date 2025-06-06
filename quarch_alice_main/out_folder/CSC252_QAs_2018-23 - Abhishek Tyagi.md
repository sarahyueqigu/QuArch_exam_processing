**Final Exam**

**CSC 252**

**1 May 2023**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
**TAs: Yifan Zhu, Matthew Nappo, Yekai Pan, Toranosuke Ozawa, Zeyu Nie, Yumeng He, Stela**
Ciko, Nisarg Ujjainkar

**Name: ____________________________________**

Problem 0 (3 points):

Problem 1 (17 points):

Problem 2 (20 points):

Problem 3 (24 points):

Problem 4 (48 points):

Problem 5 (16 points)

Problem 6 (12 points)

Total (140 points):

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 180 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK and Have a Good Summer Break!!!**


-----

**Problem 0: Warm-up (3 Points)**

Are you grateful that 252 is not an elective?

**Problem 1: Miscellaneous (17 points)**

**(3 points) Write 0xFACE in binary.**

1111 1010 1100 1110

**(3 points) The fork() system call spawns a new thread in the parent process; True or False?**

False

**(3 points) malloc() allocates physical memory in DRAM; True or False?**

False

**(4 points) List two advantages of using virtual memory over physical memory.**

Enable multitasking, good for safety, easy-to-use
continuous addresses, enable swapping with disk, …

**(4 points) What can happen if multiple threads access resources held by multiple locks?**


-----

**Problem 2: Floating-Point Arithmetics (20 points)**

**Part a) (6 points) Basic Arithmetics**
**(3 points) Write the result of 6+(16/64) in the normalized binary form**

1.1001 * 2^2

**(3 points) Compute 1.1 × 2[-2]** × 1.001 × 2[4]. Write the result in the normalized binary form. Show
your work to earn partial credit.

1.1 * 2^(-2) * 1.001 * 2^(4) = 1.1 * 1.001 * 2^(-2+4) = (1.001 + 0.1001) * 2^(-2) = 1.1011 *
2^(2)

**Part b) (6 points) True or False questions.**
**(3 points) The IEEE 754 single precision floating point representation can be used to precisely**
represent all rational numbers between 0 and 1.

False

**(3 points) The IEEE 754 double precision floating point representation can be used to precisely**
represent all real numbers between 0 and 1.

False

**Part c) (4 points) Consider the following C code.**
```
int x = 0x8f7;
int* pi = &x;
float* pf = (float*) pi;

```
Assume data is stored in little-endian format and int variables are 4 bytes aligned. Now we
dereference pf and print its value, what will we get?


-----

(a) It will give a Nan
(b) It will give a floating point number equal to the integer 0x8f7
**(c) It will give a subnormal number**
(d) There is a syntax error because we cannot cast an int pointer to a float pointer

**Part d) (4 points) In most programming languages when we want to calculate 0.3 × 3.0, we**
won’t get 9.0; instead we might get something like 0.89999999999999991. What is the most
likely cause of this?


-----

**Problem 3: Assembly Programming (24 points)**

**Conventions:**

1. For this section, the assembly shown uses the AT&T/GAS syntax opcode src, dst for
instructions with two arguments where src is the source argument and dst is the
destination argument. For example, this means that mov a, b moves the value a into b
and cmp a, b then jge c would compare b to a then jump to c if b ≥a.

2. All C code is compiled on a 64-bit machine, where arrays grow toward higher
addresses.

3. We use the x86 calling convention. That is, for functions that take two arguments, the
first argument is stored in %edi (%rdi) and the second is stored in %esi (%rsi) at the
time the function is called; the return value of a function is stored in %eax (%rax) at the
time the function returns.

4. We use the Little Endian byte order when storing multi-byte variables in memory.

The declaration of function y() is given below; its function body is intentionally incomplete.
The first parameter of the function, arr, is the pointer to an array of 5 elements. y() will iterate
over each element in the arr array exactly once and update each element if and only if a
condition is met.

Consider the following assembly code. Before executing the code, %rdi contains a pointer to an
array [17, 7, 10, 8, 15] and %rsi contains the value 10.

C code:
```
void y(long* arr, long b){
   …
}

```
Assembly code:
```
<irrelevant code omitted>
13 movq %rdi, -24(%rbp)
14 movq %rsi, -32(%rbp)
15 movq $0, -8(%rbp)
16 jmp .L2
17 .L4:
18 movq -8(%rbp), %rax
19 leaq 0(,%rax,8), %rdx
20 movq -24(%rbp), %rax
21 addq %rdx, %rax
22 movq (%rax), %rax
23 movq %rax, -16(%rbp)
24 movq -16(%rbp), %rax

```

-----

```
25 cmpq -32(%rbp), %rax
26 jge .L3
27 movq -32(%rbp), %rax
28 movq %rax, -16(%rbp)
29 .L3:
30 _A_ $1, -8(%rbp)
31 .L2:
32 cmpq $_B_, -8(%rbp)
33 jle .L4
34 ret

```
**(4 points) Which line between line 18 and line 30 is responsible for computing the offset of**
each array element in arr?

19

**(3 points) At the first iteration of the loop (hint: that’s when the value stored in -8(%rbp)is 0)**
, what is stored in %rax at the end of line 22?

17

**(3 points) What kind of programming structure is used in this function?**

a. Do-while
**b. While/for**
c. Switch statement
d. None of the above

**(6 points) Fill in A and B with the proper instruction so that the function behaves as desired.**

A:

addq

B:

4

**(4 points) Describe briefly what the condition is when updating each array element.**


-----

**(4 points) What are the updated array values at the end of this function execution?**


-----

**Problem 4: Microarchitecture/ISA (48 points)**

You are working at Intel and are on the team for designing a new microarchitecture. Your
manager gives you components for the standard five-stage pipeline: (F)etch, (D)ecode,
(E)xecute, (M)emory and (W)riteback stages, with the same functionality as discussed in the
class. The pipelined processor specification you manager give you is as follows:

  - (F)etch, (D)ecode, (E)xecute stages take 15 ns

  - The (M)emory stage takes 100 ns.

  - The (W)riteback stage takes 135 ns

  - After each stage there is a pipeline register which has a delay of 15 ns.

**Part a) (12 points)**
**(3 points) What is the order of the 5 pipeline stages in a typical processor?**

(F)etch, (D)ecode, (E)xecute, (M)emory, (W)riteback

(3 points) What is the shortest possible clock period for the specification your manager gives
you?

150 ns

(3 points) Assuming no stalls or control dependencies of any kind, using the clock frequency
you suggested, and that all the stages are occupied with instructions, how many instructions can
this processor finish in 750 ns?

5

(3 points) At the end of which stage is the branch target resolved?

(E)xecute

**Part b) (20 points)**
Now you want to design an ISA for this machine assuming the following:

  - 5 bit address space

  - Memory is byte addressable

  - Addresses are physical addresses (i.e., no virtual memory)

  - Each instruction is 1-byte long; instructions can be padded with 0 at the end if needed

  - 4 general purpose registers encoded as:


-----

|Register|Binary|
|---|---|
|r0|00|
|r1|01|
|r2|10|
|r3|11|



  - Three opcodes encoded as:

Name Opcode Behavior

`cmp` 001 Performs bitwise AND on two operands

`jif` 010 Conditional jump

`nop` 011 A no-op instruction

(8 points) Encode the following program in binary, assuming the instructions start at an
absolute address of 0.
```
   0: cmp r0 r1
   1: jif 3
   2: nop
   3: nop

```
0: 0010 0010
1: 0100 0011 (or 0101 1000)
2: 0110 0000
3: 0110 0000

(4 points) How many cycles are expected to be lost when a branch is mispredicted? Write your
explanation to earn partial credit.

2

(4 points) Assuming full pipelining, that there are no branch mispredictions, and that all jump
instructions are not taken, how many cycles will it take to execute these instructions repeated 10
times? Show your math to earn partial credit.

|Name|Opcode|Behavior|
|---|---|---|
|cmp|001|Performs bitwise AND on two operands|
|jif|010|Conditional jump|
|nop|011|A no-op instruction|


-----

(4 points) Assuming EVERY branch is mispredicted and that all jump instructions are not
taken, how many cycles will it take to execute these instructions repeated 10 times? Show your
math to earn partial credit.

4 + 40 + 20 = 64

**Part c) (16 points)**
Now you want to optimize the processor microarchitecture. You are told that you can split any of
the stages (except the execute stage) into two stages, and each new stage will be half its original
delay. These new stages cannot be split further. ANY number of consecutive stages can also be
combined together and the delay of a so-combined stage is the sum of the constituting stages.

Reminder:

  - When you split a stage into two pipeline stages, a new pipeline register must be inserted
between the two new stages

  - When you combine multiple stages into one stage, the pipeline stages between the
constituting stages are no longer needed.

(4 points) Suppose you combine the first 4 stages. What is the shortest possible clock period
after doing so? Show your math to earn partial credit.

160 ns

(4 points) Assuming no stalls or control dependencies of any kind and all the stages are
occupied with instructions, which stage(s) do you need to combine or split so you can maximize
the instructions executed per second? Write your explanation to earn partial credit.

Split the (M)emory and (W)riteback stages.

(8 points) On top of the decisions you made for your last question, which stage(s) should you
split or combine if you are also concerned with minimizing the time lost from branch
mispredictions? Write your explanation to earn partial credit.


-----

**Problem 5: Cache (16 points)**

For all the questions in this problem, assume that we are using a 16-bit machine with a
byte-addressable memory and a N-way set-associative LRU cache (for some unknown N). The
cache can hold up to 16 cache lines. Each cache line is 32 bytes (256 bits). There are 8 sets in
total.

(3 points) How many bits do you need for the offset?

log(32) = 5

(3 points) How many bits do you need for the set?

log(8) = 3

(2 points) How many cachelines are there in each set?

2

(8 points) The following sequence of memory accesses generates the hits/misses as shown.
Some miss/hit entries are intentionally left blank for you to figure out. The cache is initially
empty. Note that addresses are written in binary with spaces added between each 4 bits for
readability — these splitting points are not necessarily the tag/index/offset boundaries.

Fill in the blanks.

|#|Address|Hit/Miss|
|---|---|---|
|1|1100 1111 0000 0000|Miss|
|2|1101 1101 0010 0000|Miss|
|3|1101 1100 0010 0000|Miss|
|4|1100 1101 0001 1011|Miss|
|5|1100 1111 0000 0011|Hit|
|6|1100 1111 1001 0001|Miss|


-----

|7|1100 1101 0000 1111|Hit|
|---|---|---|
|8|1101 1100 0000 0000|Miss|
|9|1100 1111 0001 1111|Miss|
|10|1111 1111 0010 0000|Miss|
|11|1101 1101 0010 0000|Miss|
|12|0101 1001 0011 0100|Miss|
|13|1101 1101 0010 0100|Hit|


-----

**Problem 6: Virtual Memory (12 points + 4 points extra credit)**

Assume a byte addressable memory with the following characteristics:

1. Size of the virtual memory is 16 MB (1 MB = 2[20] B)

2. Size of the physical memory is 4 MB

3. Page size is 256 Bytes

4. It uses one-level page table

Format of the PTE is shown below:

Metadata <2 bits> PPN <n bits>

(3 points) How many bits do you need to represent the virtual page number (VPN)

16 bits

(3 points) How many bits do you need to represent the physical page number (PPN)

14 bits

(3 points) How many PTEs can you store in a page?

256/2=128

(3 points) How many pages does the page table occupy?

2^16/2^7 = 512

(4 points extra credit) Now we add a TLB to the machine above. The TLB has 16 entries and
is direct-mapped. Which bits in the virtual address are used to index the TLB?

|Metadata <2 bits>|PPN <n bits>|
|---|---|


-----

**Final Exam**

**CSC 252**

**1 May 2023**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
**TAs: Yifan Zhu, Matthew Nappo, Yekai Pan, Toranosuke Ozawa, Zeyu Nie, Yumeng He, Stela**
Ciko, Nisarg Ujjainkar

**Name: ____________________________________**

Problem 0 (3 points):

Problem 1 (17 points):

Problem 2 (20 points):

Problem 3 (24 points):

Problem 4 (48 points):

Problem 5 (16 points)

Problem 6 (12 points)

Total (140 points):

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 180 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK and Have a Good Summer Break!!!**


-----

**Problem 0: Warm-up (3 Points)**

Are you grateful that 252 is not an elective?

**Problem 1: Miscellaneous (17 points)**

**(3 points) Write 0xFACE in binary.**

**(3 points) The fork() system call spawns a new thread in the parent process; True or False?**

**(3 points) malloc() allocates physical memory in DRAM; True or False?**

**(4 points) List two advantages of using virtual memory over physical memory.**

**(4 points) What can happen if multiple threads access resources held by multiple locks?**


-----

**Problem 2: Floating-Point Arithmetics (20 points)**

**Part a) (6 points) Basic Arithmetics**
**(3 points) Write the result of 6+(16/64) in the normalized binary form**

**(3 points) Compute 1.1 × 2[-2]** × 1.001 × 2[4]. Write the result in the normalized binary form. Show
your work to earn partial credit.

**Part b) (6 points) True or False questions.**
**(3 points) The IEEE 754 single precision floating point representation can be used to precisely**
represent all rational numbers between 0 and 1.

**(3 points) The IEEE 754 double precision floating point representation can be used to precisely**
represent all real numbers between 0 and 1.

**Part c) (4 points) Consider the following C code.**
```
int x = 0x8f7;
int* pi = &x;
float* pf = (float*) pi;

```
Assume data is stored in little-endian format and int variables are 4 bytes aligned. Now we
dereference pf and print its value, what will we get?


-----

(a) It will give a Nan
(b) It will give a floating point number equal to the integer 0x8f7
**(c) It will give a subnormal number**
(d) There is a syntax error because we cannot cast an int pointer to a float pointer

**Part d) (4 points) In most programming languages when we want to calculate 0.3 × 3.0, we**
won’t get 9.0; instead we might get something like 0.89999999999999991. What is the most
likely cause of this?


-----

**Problem 3: Assembly Programming (24 points)**

**Conventions:**

1. For this section, the assembly shown uses the AT&T/GAS syntax opcode src, dst for
instructions with two arguments where src is the source argument and dst is the
destination argument. For example, this means that mov a, b moves the value a into b
and cmp a, b then jge c would compare b to a then jump to c if b ≥a.

2. All C code is compiled on a 64-bit machine, where arrays grow toward higher
addresses.

3. We use the x86 calling convention. That is, for functions that take two arguments, the
first argument is stored in %edi (%rdi) and the second is stored in %esi (%rsi) at the
time the function is called; the return value of a function is stored in %eax (%rax) at the
time the function returns.

4. We use the Little Endian byte order when storing multi-byte variables in memory.

The declaration of function y() is given below; its function body is intentionally incomplete.
The first parameter of the function, arr, is the pointer to an array of 5 elements. y() will iterate
over each element in the arr array exactly once and update each element if and only if a
condition is met.

Consider the following assembly code. Before executing the code, %rdi contains a pointer to an
array [17, 7, 10, 8, 15] and %rsi contains the value 10.

C code:
```
void y(long* arr, long b){
   …
}

```
Assembly code:
```
<irrelevant code omitted>
13 movq %rdi, -24(%rbp)
14 movq %rsi, -32(%rbp)
15 movq $0, -8(%rbp)
16 jmp .L2
17 .L4:
18 movq -8(%rbp), %rax
19 leaq 0(,%rax,8), %rdx
20 movq -24(%rbp), %rax
21 addq %rdx, %rax
22 movq (%rax), %rax
23 movq %rax, -16(%rbp)
24 movq -16(%rbp), %rax

```

-----

```
25 cmpq -32(%rbp), %rax
26 jge .L3
27 movq -32(%rbp), %rax
28 movq %rax, -16(%rbp)
29 .L3:
30 _A_ $1, -8(%rbp)
31 .L2:
32 cmpq $_B_, -8(%rbp)
33 jle .L4
34 ret

```
**(4 points) Which line between line 18 and line 30 is responsible for computing the offset of**
each array element in arr?

**(3 points) At the first iteration of the loop (hint: that’s when the value stored in -8(%rbp)is 0)**
, what is stored in %rax at the end of line 22?

**(3 points) What kind of programming structure is used in this function?**

a. Do-while
**b. While/for**
c. Switch statement
d. None of the above

**(6 points) Fill in A and B with the proper instruction so that the function behaves as desired.**

A:

B:

**(4 points) Describe briefly what the condition is when updating each array element.**


-----

**(4 points) What are the updated array values at the end of this function execution?**


-----

**Problem 4: Microarchitecture/ISA (48 points)**

You are working at Intel and are on the team for designing a new microarchitecture. Your
manager gives you components for the standard five-stage pipeline: (F)etch, (D)ecode,
(E)xecute, (M)emory and (W)riteback stages, with the same functionality as discussed in the
class. The pipelined processor specification you manager give you is as follows:

  - (F)etch, (D)ecode, (E)xecute stages take 15 ns

  - The (M)emory stage takes 100 ns.

  - The (W)riteback stage takes 135 ns

  - After each stage there is a pipeline register which has a delay of 15 ns.

**Part a) (12 points)**
**(3 points) What is the order of the 5 pipeline stages in a typical processor?**

(3 points) What is the shortest possible clock period for the specification your manager gives
you?

(3 points) Assuming no stalls or control dependencies of any kind, using the clock frequency
you suggested, and that all the stages are occupied with instructions, how many instructions can
this processor finish in 750 ns?

(3 points) At the end of which stage is the branch target resolved?

**Part b) (20 points)**
Now you want to design an ISA for this machine assuming the following:

  - 5 bit address space

  - Memory is byte addressable

  - Addresses are physical addresses (i.e., no virtual memory)

  - Each instruction is 1-byte long; instructions can be padded with 0 at the end if needed

  - 4 general purpose registers encoded as:


-----

|Register|Binary|
|---|---|
|r0|00|
|r1|01|
|r2|10|
|r3|11|



  - Three opcodes encoded as:

Name Opcode Behavior

`cmp` 001 Performs bitwise AND on two operands

`jif` 010 Conditional jump

`nop` 011 A no-op instruction

(8 points) Encode the following program in binary, assuming the instructions start at an
absolute address of 0.
```
   0: cmp r0 r1
   1: jif 3
   2: nop
   3: nop

```
(4 points) How many cycles are expected to be lost when a branch is mispredicted? Write your
explanation to earn partial credit.

(4 points) Assuming full pipelining, that there are no branch mispredictions, and that all jump
instructions are not taken, how many cycles will it take to execute these instructions repeated 10
times? Show your math to earn partial credit.

|Name|Opcode|Behavior|
|---|---|---|
|cmp|001|Performs bitwise AND on two operands|
|jif|010|Conditional jump|
|nop|011|A no-op instruction|


-----

(4 points) Assuming EVERY branch is mispredicted and that all jump instructions are not
taken, how many cycles will it take to execute these instructions repeated 10 times? Show your
math to earn partial credit.

**Part c) (16 points)**
Now you want to optimize the processor microarchitecture. You are told that you can split any of
the stages (except the execute stage) into two stages, and each new stage will be half its original
delay. These new stages cannot be split further. ANY number of consecutive stages can also be
combined together and the delay of a so-combined stage is the sum of the constituting stages.

Reminder:

  - When you split a stage into two pipeline stages, a new pipeline register must be inserted
between the two new stages

  - When you combine multiple stages into one stage, the pipeline stages between the
constituting stages are no longer needed.

(4 points) Suppose you combine the first 4 stages. What is the shortest possible clock period
after doing so? Show your math to earn partial credit.

(4 points) Assuming no stalls or control dependencies of any kind and all the stages are
occupied with instructions, which stage(s) do you need to combine or split so you can maximize
the instructions executed per second? Write your explanation to earn partial credit.

(8 points) On top of the decisions you made for your last question, which stage(s) should you
split or combine if you are also concerned with minimizing the time lost from branch
mispredictions? Write your explanation to earn partial credit.


-----

**Problem 5: Cache (16 points)**

For all the questions in this problem, assume that we are using a 16-bit machine with a
byte-addressable memory and a N-way set-associative LRU cache (for some unknown N). The
cache can hold up to 16 cache lines. Each cache line is 32 bytes (256 bits). There are 8 sets in
total.

(3 points) How many bits do you need for the offset?

(3 points) How many bits do you need for the set?

(2 points) How many cachelines are there in each set?

(8 points) The following sequence of memory accesses generates the hits/misses as shown.
Some miss/hit entries are intentionally left blank for you to figure out. The cache is initially
empty. Note that addresses are written in binary with spaces added between each 4 bits for
readability — these splitting points are not necessarily the tag/index/offset boundaries.

Fill in the blanks.

|#|Address|Hit/Miss|
|---|---|---|
|1|1100 1111 0000 0000|Miss|
|2|1101 1101 0010 0000|Miss|
|3|1101 1100 0010 0000|Miss|
|4|1100 1101 0001 1011|Miss|
|5|1100 1111 0000 0011|Hit|
|6|1100 1111 1001 0001|Miss|


-----

|7|1100 1101 0000 1111|Hit|
|---|---|---|
|8|1101 1100 0000 0000|Miss|
|9|1100 1111 0001 1111|Miss|
|10|1111 1111 0010 0000||
|11|1101 1101 0010 0000||
|12|0101 1001 0011 0100||
|13|1101 1101 0010 0100||


-----

**Problem 6: Virtual Memory (12 points + 4 points extra credit)**

Assume a byte addressable memory with the following characteristics:

1. Size of the virtual memory is 16 MB (1 MB = 2[20] B)

2. Size of the physical memory is 4 MB

3. Page size is 256 Bytes

4. It uses one-level page table

Format of the PTE is shown below:

Metadata <2 bits> PPN <n bits>

(3 points) How many bits do you need to represent the virtual page number (VPN)

(3 points) How many bits do you need to represent the physical page number (PPN)

(3 points) How many PTEs can you store in a page?

(3 points) How many pages does the page table occupy?

(4 points extra credit) Now we add a TLB to the machine above. The TLB has 16 entries and
is direct-mapped. Which bits in the virtual address are used to index the TLB?

|Metadata <2 bits>|PPN <n bits>|
|---|---|


-----

**Midterm Exam**

**CSC 252**

**3 March 2023**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
**TAs: Yifan Zhu, Matthew Nappo, Yekai Pan, Toranosuke Ozawa, Zeyu Nie, Yumeng He, Stela**
Ciko, Nisarg Ujjainkar

**Name: ____________________________________**

Problem 0 (2 points):

Problem 1 (9 points):

Problem 2 (20 points):

Problem 3 (10 points):

Problem 4 (24 points):

Problem 5 (25 points)

Total (90 points):

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 75 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (2 Points)**
Have you been to TA office hours before?

YES/NO

**Problem 1: Fixed-Point Arithmetics (9 points + 2 points extra credit)**

**Part a) (2 points) Represent decimal number 24 in hexadecimal form.**

18

**Part b) (3 points) Represent octal (base 8) number 53 in decimal form and binary form.**

43;101011

**Part c) (4 points + 2 points extra credit) Consider two unsigned binary numbers A = 1011**
and B = 0101. Do the math below. Use as many bits as needed to precisely represent the results.

**(2 points) What’s the result of A+B?**

10000

**(2 points) What’s the result of A-B?**

0110

**(2 points extra credit) What’s the result of A * B?**


-----

**Problem 2: Floating-Point Arithmetics (20 points)**

**Part a) (6 points) Consider a decimal number F = -100.50:**

**(2 points) Give the binary representation of F:**

-1100100.1

**(2 points) Put F into the normalized scientific notation:**

-1.1001001 x 2^6

**(2 points) Write the significand in binary:**

1001001

**Part b) (4 points) Consider a hex value F = 0x7f800000 that represents a floating point**
number encoded using the IEEE 754 single-precision format.

**(2 points) What is the exponent value (in decimal)?**

128

**(2 points) What does F represent?**

**Positive infinity**

**Part c) (10 points) Professor Bob teaches a computer science course, and he is designing the**
scoring system of a midterm exam. The exam consists of 64 multiple choice questions and
students will receive 1 point for each correct answer, 0 point for leaving it blank, and -0.25
points for a wrong answer.

To store all the possible scores, Bob wants to incorporate knowledge from CSC 252 to improve
the space efficiency by designing a new floating point representation, which should meet three
criteria:


-----

1. The characteristics are compliant with the floating-point representations we discussed in
class;
2. Can accurately represent any valid score;
3. Use as few bits as possible.

**(2 points) How many bits are used for the significand in this new floating point**
representation?

7
(We need at most 8 bits for all of them but the first bit
comes for free.)

**(2 points) How many bits are used for the exponent fields in this new floating point**
representation?

4
(2^-2 to 2^6, where 3 bits is not enough for exponents
3,4,5,6)

**(2 points) What’s the bias?**

7 = (2^(4-1)) - 1

**(4 points) Can you use a fixed point representation for the same purpose? If yes, at least how**
many bits do you need? If not, explain the reason.


-----

**Problem 3: Logic Design (10 points + 3 points extra credit)**

Consider the following circuit. Each square-shaped component represents a 1-bit full adder: A
and B are its two 1-bit inputs, Cin is the 1-bit carry in, Σ is 1 one-bit output, and Cout is the 1-bit
the carry out. A3, A2, A1, A0, B3, B2, B1, B0 are all 1-bit inputs.P3, P2, P1, P0 are the outputs of the
four XOR gates. Σ3, Σ2, Σ1, Σ0 are 1-bit outputs of the four full adders.

The truth table of a 1-bit full adder is below:

|A|B|C in|Σ|C out|
|---|---|---|---|---|
|0|0|0|0|0|
|0|0|1|1|0|
|0|1|o|1|0|
|0|1|1|0|1|
|1|0|0|1|0|
|1|0|1|0|1|
|1|1|0|0|1|
|1|1|1|1|1|


-----

**Part a) (4 points) Assuming A3A2A1A0 = (1001)2 and B3B2B1B0 = (0001)2:**

**(2 points) If X = 0, what is the value of P3P2P1P0?**

0001

**(2 points) If X = 1, what is the value of P3P2P1P0?**

1110

**Part b) (4 points) Still assuming A3A2A1A0 = (1001)2 and B3B2B1B0 = (0001)2:**

**(2 points) If X = 0, what is the value of Σ3Σ2Σ1Σ0?**

1010

**(2 points) If X = 1, what is the value of Σ3Σ2Σ1Σ0?**

1000

**Part c) (2 points + 3 points extra credit) Assume that the 1-bit full adder is implemented**
as shown in the figure below. The delay at each gate is 1ps.


-----

**(2 points) What is the propagation delay of the 1-bit full adder?**

3 ps

**(3 points extra credit) What is the total propagation delay of the entire circuit shown at the**
beginning of this problem? Assuming that the XOR gates outside the full adder have a delay of
1ps, too.


-----

**Problem 4: Assembly Programming (24 points)**

**Conventions:**

1. For this section, the assembly shown uses the AT&T/GAS syntax opcode src, dst for
instructions with two arguments where src is the source argument and dst is the
destination argument. For example, this means that mov a, b moves the value a into b
and cmp a, b then jge c would compare b to a then jump to c if b ≥a.

2. All C code is compiled on a 64-bit machine, where arrays grow toward higher
addresses.

3. We use the x86 calling convention. That is, for functions that take two arguments, the
first argument is stored in %edi (%rdi) and the second is stored in %esi (%rsi) at the
time the function is called; the return value of a function is stored in %eax (%rax) at the
time the function returns.

4. We use the Little Endian byte order when storing multi-byte variables in memory.

**Part a) (9 points)**

Consider the following C code:
```
   struct Car{
       char *model;
       int year;
       long mpg;
   };
   struct Car myCars[2];

```
The following assembly is part of a function print_info(), which, as you can see, calls another
function get_cars(), which initializes myCars and returns the pointer that points to myCars.

1: call get_cars

2: movq %rax, -8(%rbp)

3: movq -8(%rbp), %rax

4: addq $24, %rax

5: movq 16(%rax), %rax

6: movq %rax, -16(%rbp)

7: movq -8(%rbp), %rax

8: movq (%rax), %rax

9: movb 3(%rax), %al

**(3 points) What is the size (number of bytes) of struct Car, assuming proper alignment?**


-----

**(3 points) At the end of line 5, what C variable does %rax contain? Express in C syntax.**

myCars[1].mpg

**(3 points) At the end of line 9, what C variable does %rl contain? Express in C syntax.**

myCars[0].model[3]

**Part b) (15 points)**

Consider the following function p2. Its C code and assembly code are both partially given.
Assuming that the input arguments to p2are x=4, y=4.

Then, use the rest of the assembly to find the return value of p2() given
```
   unsigned long p2(unsigned long x, unsigned long y){
       unsigned long t1= x + 2*y;
       unsigned long t2= . . . ; // intentionally hidden
       return t2;
   }
   // some irrelevant instructions at the beginning omitted

```
1: `movq` `%rdi, -24(%rbp)`

2: `movq` `%rsi, -32(%rbp)`

3: `movq` `-32(%rbp), %rax`

4: ­ A `(%rax,%rax), %rdx`

5: `movq` `-24(%rbp), %rax`

6: `addq` **B, C**

7: `movq` `%rax, -8(%rbp)`

8: `movq` `-8(%rbp), %rax`

9: `shrq` `$2, %rax`

10: `movq` `%rax, -16(%rbp)`

11: `movq` `-16(%rbp), %rax`

12: `ret`


-----

Complete the three missing pieces in the assembly code.

**(3 points) A:**

leaq

**(3 points) B:**

%rdx

**(3 points) C:**

%rax

**(3 points) What is the byte contained in -8(%rbp) after line 7?**

0xC

**(3 points) What is the return value of p2?**


-----

**Problem 5: Processor architecture (25 points + 2 points extra credit)**

**Part a) (4 Points)**
Consider a microarchitecture that is designed for an ISA with 256 instructions and 16
general-purpose registers. The ISA has a 16-bit address space. Assuming the opcode fields in all
the instructions are encoded using the same amount of bits.

(2 Points) If an instruction in this ISA takes the form of ins r1,r2,r3, where ins is the
opcode, and r1, r2, and r3 are three general-purpose registers. How many bits are required to
encode this instruction?

20

(2 Points) Assuming the jump instructions in this ISA are encoded using absolute addresses.
What is the number of bits needed to encode a jump instruction?

24

**Part b) (21 Points + 2 points extra credit)**
A single-cycle processor has a cycle time of 30 ns. Consider two different pipelined
implementations of the same processor, each with 5 and 10 stages, respectively. Assume that the
stages divide the computation uniformly. In both pipelined processors, it takes 1 ns for the
output of a stage to latch on to the pipeline registers.

(3 Points) What is the shortest plausible clock period for the 5-stage pipelined processor?

7 ns

(3 Points) What is the shortest clock period for the 10-stage pipelined processor?

4 ns

(3 Points) What is the execution time per instruction in the 10-stage pipelined processor?


-----

(3 Points) Assuming no pipeline stall of any kind, how long does it take to execute 50
instructions in the 5-stage pipeline?

54*7 = 378 ns

(3 Points) Assuming no pipeline stall of any kind, how long does it take to execute 50
instructions in the 10-stage pipeline?

59*4 = 236 ns

(3 Points) Assuming no pipeline stall of any kind, express the total execution time of 50
instructions as a function of the pipeline stages T.

(x-1+50)*(30/x+1)

(2 Points Extra Credit) What number of pipeline stages will give you the minimum total
execution time for 50 instructions?


-----

**Midterm Exam**

**CSC 252**

**3 March 2023**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
**TAs: Yifan Zhu, Matthew Nappo, Yekai Pan, Toranosuke Ozawa, Zeyu Nie, Yumeng He, Stela**
Ciko, Nisarg Ujjainkar

**Name: ____________________________________**

Problem 0 (2 points):

Problem 1 (9 points):

Problem 2 (20 points):

Problem 3 (10 points):

Problem 4 (24 points):

Problem 5 (25 points)

Total (90 points):

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 75 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (2 Points)**
Have you been to TA office hours before?

**Problem 1: Fixed-Point Arithmetics (9 points + 2 points extra credit)**

**Part a) (2 points) Represent decimal number 24 in hexadecimal form.**

**Part b) (3 points) Represent octal (base 8) number 53 in decimal form and binary form.**

**Part c) (4 points + 2 points extra credit) Consider two unsigned binary numbers A = 1011**
and B = 0101. Do the math below. Use as many bits as needed to precisely represent the results.

**(2 points) What’s the result of A+B?**

**(2 points) What’s the result of A-B?**

**(2 points extra credit) What’s the result of A * B?**


-----

**Problem 2: Floating-Point Arithmetics (20 points)**

**Part a) (6 points) Consider a decimal number F = -100.50:**

**(2 points) Give the binary representation of F:**

**(2 points) Put F into the normalized scientific notation:**

**(2 points) Write the significand in binary:**

**Part b) (4 points) Consider a hex value F = 0x7f800000 that represents a floating point**
number encoded using the IEEE 754 single-precision format.

**(2 points) What is the exponent value (in decimal)?**

**(2 points) What does F represent?**

**Part c) (10 points) Professor Bob teaches a computer science course, and he is designing the**
scoring system of a midterm exam. The exam consists of 64 multiple choice questions and
students will receive 1 point for each correct answer, 0 point for leaving it blank, and -0.25
points for a wrong answer.

To store all the possible scores, Bob wants to incorporate knowledge from CSC 252 to improve
the space efficiency by designing a new floating point representation, which should meet three
criteria:


-----

1. The characteristics are compliant with the floating-point representations we discussed in the
class;
2. Can accurately represent any valid score;
3. Use as few bits as possible.

**(4 points) How many bits are used for the significand and the exponent fields in this new**
floating point representation?

**(2 points) What’s the bias?**

**(4 points) Can you use a fixed point representation for the same purpose? If yes, at least how**
many bits do you need? If not, explain the reason.


-----

**Problem 3: Logic Design (10 points + 3 points extra credit)**

Consider the following circuit. Each square-shaped component represents a 1-bit full adder: A
and B are its two 1-bit inputs, Cin is the 1-bit carry in, Σ is 1 one-bit output, and Cout is the 1-bit
the carry out. A3, A2, A1, A0, B3, B2, B1, B0 are all 1-bit inputs.P3, P2, P1, P0 are the outputs of the
four XOR gates. Σ3, Σ2, Σ1, Σ0 are 1-bit outputs of the four full adders.

The truth table of a 1-bit full adder is below:

|A|B|C in|Σ|C out|
|---|---|---|---|---|
|0|0|0|0|0|
|0|0|1|1|0|
|0|1|o|1|0|
|0|1|1|0|1|
|1|0|0|1|0|
|1|0|1|0|1|
|1|1|0|0|1|
|1|1|1|1|1|


-----

**Part a) (4 points) Assuming A3A2A1A0 = (1001)2 and B3B2B1B0 = (0001)2:**

**(2 points) If X = 0, what is the value of P3P2P1P0?**

**(2 points) If X = 1, what is the value of P3P2P1P0?**

**Part b) (4 points) Still assuming A3A2A1A0 = (1001)2 and B3B2B1B0 = (0001)2:**

**(2 points) If X = 0, what is the value of Σ3Σ2Σ1Σ0?**

**(2 points) If X = 1, what is the value of Σ3Σ2Σ1Σ0?**

**Part c) (2 points + 3 points extra credit) Assume that the 1-bit full adder is implemented**
as shown in the figure below. The delay at each gate is 1ps.


-----

**(2 points) What is the propagation delay of the 1-bit full adder?**

**(3 points extra credit) What is the total propagation delay of the entire circuit shown at the**
beginning of this problem? Assuming that the XOR gates outside the full adder have a delay of
1ps, too.


-----

**Problem 4: Assembly Programming (24 points)**

**Conventions:**

1. For this section, the assembly shown uses the AT&T/GAS syntax opcode src, dst for
instructions with two arguments where src is the source argument and dst is the
destination argument. For example, this means that mov a, b moves the value a into b
and cmp a, b then jge c would compare b to a then jump to c if b ≥a.

2. All C code is compiled on a 64-bit machine, where arrays grow toward higher
addresses.

3. We use the x86 calling convention. That is, for functions that take two arguments, the
first argument is stored in %edi (%rdi) and the second is stored in %esi (%rsi) at the
time the function is called; the return value of a function is stored in %eax (%rax) at the
time the function returns.

4. We use the Little Endian byte order when storing multi-byte variables in memory.

**Part a) (9 points)**

Consider the following C code:
```
   struct Car{
       char *model;
       int year;
       long mpg;
   };
   struct Car myCars[2];

```
The following assembly is part of a function print_info(), which, as you can see, calls another
function get_cars(), which initializes myCars and returns the pointer that points to myCars.

1: call get_cars

2: movq %rax, -8(%rbp)

3: movq -8(%rbp), %rax

4: addq $24, %rax

5: movq 16(%rax), %rax

6: movq %rax, -16(%rbp)

7: movq -8(%rbp), %rax

8: movq (%rax), %rax

9: movb 3(%rax), %al

**(3 points) What is the size (number of bytes) of struct Car, assuming proper alignment?**


-----

**(3 points) At the end of line 5, what C variable does %rax contain? Express in C syntax.**

**(3 points) At the end of line 9, what C variable does %al contain? Express in C syntax.**

**Part b) (15 points)**

Consider the following function p2. Its C code and assembly code are both partially given.
Assuming that the input arguments to p2are x=4, y=4.

Then, use the rest of the assembly to find the return value of p2() given
```
   unsigned long p2(unsigned long x, unsigned long y){
       unsigned long t1= x + 2*y;
       unsigned long t2= . . . ; // intentionally hidden
       return t2;
   }
   // some irrelevant instructions at the beginning omitted

```
1: `movq` `%rdi, -24(%rbp)`

2: `movq` `%rsi, -32(%rbp)`

3: `movq` `-32(%rbp), %rax`

4: ­ A `(%rax,%rax), %rdx`

5: `movq` `-24(%rbp), %rax`

6: `addq` **B, C**

7: `movq` `%rax, -8(%rbp)`

8: `movq` `-8(%rbp), %rax`

9: `shrq` `$2, %rax`

10: `movq` `%rax, -16(%rbp)`

11: `movq` `-16(%rbp), %rax`

12: `ret`


-----

Complete the three missing pieces in the assembly code.

**(3 points) A:**

**(3 points) B:**

**(3 points) C:**

**(3 points) What is the byte contained in -8(%rbp) after line 7?**

**(3 points) What is the return value of p2?**


-----

**Problem 5: Processor architecture (25 points + 2 points extra credit)**

**Part a) (4 Points)**
Consider a microarchitecture that is designed for an ISA with 256 instructions and 16
general-purpose registers. The ISA has a 16-bit address space. Assuming the opcode fields in all
the instructions are encoded using the same amount of bits.

(2 Points) If an instruction in this ISA takes the form of ins r1,r2,r3, where ins is the
opcode, and r1, r2, and r3 are three general-purpose registers. How many bits are required to
encode this instruction?

(2 Points) Assuming the jump instructions in this ISA are encoded using absolute addresses.
What is the number of bits needed to encode a jump instruction?

**Part b) (21 Points + 2 points extra credit)**
A single-cycle processor has a cycle time of 30 ns. Consider two different pipelined
implementations of the same processor, each with 5 and 10 stages, respectively. Assume that the
stages divide the computation uniformly. In both pipelined processors, it takes 1 ns for the
output of a stage to latch on to the pipeline registers.

(3 Points) What is the shortest plausible clock period for the 5-stage pipelined processor?

(3 Points) What is the shortest clock period for the 10-stage pipelined processor?

(3 Points) What is the execution time per instruction in the 5-stage pipelined processor?

(3 Points) What is the execution time per instruction in the 10-stage pipelined processor?


-----

(3 Points) Assuming no pipeline stall of any kind, how long does it take to execute 50
instructions in the 5-stage pipeline?

(3 Points) Assuming no pipeline stall of any kind, how long does it take to execute 50
instructions in the 10-stage pipeline?

(3 Points) Assuming no pipeline stall of any kind, express the total execution time of 50
instructions as a function of the pipeline stages T.

(2 Points Extra Credit) What number of pipeline stages will give you the minimum total
execution time for 50 instructions?


-----

**Final Exam**

**CSC 252**

**4 May 2022**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
**TAs: Nisarg Ujjainkar, Abhishek Tyag, Kalen Frieberg, Gunnar Hammonds, Mandar Juvekar,**
Zihao Lin, Vladimir Maksimovski, Yiyao (Jack) Yu

**Name: ____________________________________**

Problem 0 (3 points):

Problem 1 (12 points):

Problem 2 (18 points):

Problem 3 (25 points):

Problem 4 (20 points):

Problem 5 (26 points)

Problem 6 (26 points):

Total (130 points):

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 180 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (3 Points)**

Do you think 252 could be taught in high school?

**Problem 1: Miscellaneous (12 points)**

**Part a) (3 points) Write down the sum of 328 and 0x32 in base 2.**

01001100

**Part b) (3 points) Generally, the access time of a direct-mapped cache is ___ than that of a**
fully associative cache that is the same total size. Answer with <, >, =, <=, or >=.

<=

**Part c) (3 points) (True or False) Virtual memory has no size limitation.**

False

**Part d) (3 points) Consider the following C struct Person:**
```
struct Person{
   long id;
   float age;
   float weight;
   float height;
   char name[20];
   char sex[7];
   struct Person * nextPerson;
};

```
What’s the size of the struct Person?


-----

**Problem 2: ISA (18 points)**

A stack-based ISA is designed. The ISA uses a hardware stack, and instructions in this ISA
manipulate this stack. Each entry on the stack is one byte long, and the memory is
byte-addressable. All instructions are 8-bit long, and are classified into two categories.

**R Category**

Binary encoding:

OpCode<7-5 bits> 00000<4-0 bits>

Instruction list:

**Instruction** **OpCode** **Role**

`pop` 001 Remove the item at the top of the stack.

`halt` 001 Halt the processor.

**I Category**

Binary encoding:

OpCode<7-5 bits> Immediate value in 2’s component<4-0 bits>

Instruction list:

|OpCode<7-5 bits>|00000<4-0 bits>|
|---|---|

|Instruction|OpCode|Role|
|---|---|---|
|pop|001|Remove the item at the top of the stack.|
|halt|001|Halt the processor.|

|OpCode<7-5 bits>|Immediate value in 2’s component<4-0 bits>|
|---|---|

|Instruction|OpCode|Role|
|---|---|---|
|pushi|000|Push sign-extended immediate value on the stack.|
|load|101|Let the top entry of the stack be A. Compute Address = A + sign-extended immediate value; Pop A from the stack; Use Address to load a byte from the main memory and push the byte on the stack.|
|store|100|Let the top entry of the stack be A, and the second entry of the stack be B. Compute Address = A + sign-extended immediate value; Pop A from the stack; Store B at the memory location Address; Pop B from the stack.|


-----

|loadd|110|Address = sign-extended immediate value. Load a byte from the memory using Address and push the byte on the stack.|
|---|---|---|


**Part a) (12 points) Encode the following instructions in binary.**

**(4 points) store -8**

###### 10011000

**(4 points) pushi 7**

###### 00000111

**(4 points) halt**

###### 00100000

**Part b) (6 points) You want to implement a function that pops the top value from the stack**
and then pushes it back on the stack twice. Memory location at address 0 is reserved for this
instruction to use temporarily. Write an assembly program using the existing instructions to
implement this function.


-----

**Problem 3: Floating-Point Arithmetic (25 points)**

Suppose that the IEEE decided to add a new n-bit floating-point standard, with its main
characteristics consistent with the other IEEE standards. This n-bit standard can precisely

represent the value 6 [3], but cannot precisely represent 11 7 . The smallest positive

16 16


−30

**normalized value that can be represented in this standard is** 2 .

**Part a) (3 points) Convert** 6 [3] to Binary Normalized Form

16


**Part b) (3 points) How many of the n bits are fraction bits?**

6

**Part c) (3 points) What’s the bias of this standard?**

31

**Part d) (3 points) How many of the n bits are exponent bits?**

6

**Part e) (3 points) What is n?**

13

**Part f) (10 points) Suppose that using this new IEEE standard you perform two separate**
calculations, assume nearest-even rounding is used:

1. (256 + 2 [1]

4 [) −256]


2. (256 −256) + 2 [1]

4

What would be the result of these calculations? Do they both result in equivalent mathematically
precise answers? Show your math to earn partial credit.


-----

-----

**Problem 4: Cache (20 points)**

For all the questions in this problem, assume that we are using a 12-bit machine with a
byte-addressable memory and a direct-mapped cache. The cache can hold up to 16 cache lines.

**Part a) (3 points) How many bits do you need for the set index?**

4

**Part b) (17 points) The following sequence of 9 memory accesses generates the hits/misses**
shown. Some miss/hit entries are intentionally left blank. The cache is initially empty. Note that
the addresses are written in binary with spaces added between each 4 bits for readability. These
are not necessarily the tag/index/offset boundaries.

**#** **Address** **Hit/Miss**

`1` `1101 1111 0000` Miss

`2` `0000 1101 1111` Miss

`3` `1101 0111 0101` Miss

`4` `0000 1101 1100` Hit

`5` `1101 1111 0011` Miss

`6` `1111 0111 0010` Miss

`7` `1101 1111 0000` Miss

`8` `0000 1101 1101` Hit

`9` `1111 0111 0100` Miss

**(3 points) What is the number of tag bits?**

5

**(3 points) What is the number of offset bits?**

|#|Address|Hit/Miss|
|---|---|---|
|1|1101 1111 0000|Miss|
|2|0000 1101 1111|Miss|
|3|1101 0111 0101|Miss|
|4|0000 1101 1100|Hit|
|5|1101 1111 0011|Miss|
|6|1111 0111 0010|Miss|
|7|1101 1111 0000|Miss|
|8|0000 1101 1101|Hit|
|9|1111 0111 0100|Miss|


-----

**(3 points) What is the size of each cache line (ignore the valid bit, dirty bit, and tag bits etc.)?**
Show the formula you used to calculate this, and the value you get from it.

size of cache line = associativity * block size = 1 * 2^3 Bytes = 8 Bytes

**(8 points) Fill the miss/hit for each of the blank entries.**


-----

**Problem 5: Assembly Programming (26 points)**

**Conventions:**

1. For this section, the assembly shown uses the AT&T/GAS syntax opcode src, dst
for instructions with two arguments where src is the source argument and dst is the
destination argument. For example, this means that mov a, b moves the value a into b.

2. All C code is compiled on a 64-bit machine, where arrays grow toward higher
addresses.

3. For functions that take an argument, the argument is stored in %rdi at the time the
function is called. The return value of this function is stored in %rax at the time the
function returns.

Consider the assembly of a C function void foobar(int *x) which takes a single int
pointer parameter x.
```
0000000000001159 <foobar>:
   1159: mov (%rdi),%eax
   115b: inc %eax
   115d: mov %eax,(%rdi)
   115f: lea 0x2ecf,%rdi
   1166: cmp $0x1,%eax
   1169: je 1177 <foobar+0x1e>
   116b: cmp $0x2,%eax
   116e: jne 117c <foobar+0x23>
   1170: lea 0x2eb4,%rdi
   1177: call 1030 <puts@plt>
   117c: ret

```
The addresses 0x2ecf and 0x2eb4 contain the beginning of character strings “foo” and
```
“bar” respectively. puts() is a standard C function that prints a character string given the

```
string start address as a parameter.

**Part a) (9 points)**

**(3 points) When the initial value of *x is 0, what is printed by the program?**

foo

**(3 points) When the initial value of *x is 1, what is printed by the program?**


-----

**(3 points) The call on line 1177 is replaced with a jmp. Would this program still run**
correctly? Explain your answer.

Yes. foobar() immediately returns after calling put() and does not put anything on its stack
frame. Using jmp makes puts() return from foobar()’s stack frame cleanly.

**Part b) (17 points)**

Assuming that there are two threads, each of which executes the same foobar() function with
the same exact parameter x. *x is initially set to 0. For the sake of this problem, assume that the
instructions inside the puts() function are always executed as an atomic unit (they are either
executed together without interruption or not executed at all).

**(4 points) What are all the possible values of *x after both threads finish execution of**
```
foobar()?

```
1 or 2

**(4 points) What are all the possible strings printed by this multi-threaded program?**


-----

**(3 points) Suppose the first three instructions (1159 to 115d) could be replaced with a single**
atomic instruction called csc252. Would this guarantee that the program always ends with x
containing the value 2? Show you work to earn partial credit.

x will always be 2 in the end. It is impossible for both threads to write back 1 to *x.

**(3 points) Would this guarantee that the program always prints the same string no matter how**
many times you run it? Show you work to earn partial credit.

The program output can be either “foobar” or “barfoo” since the puts() can still be executed
in any order.

**(3 points) Assuming that the two threads execute on two different processors, each with a**
separate cache. What is something that the processor designers have to pay attention to in order
to correctly implement the csc252 instruction?


-----

**Problem 6: Virtual Memory (26 points)**


Assume a virtual memory system that has the following characteristics:


1. The virtual address space is 32 KB and is byte addressable

2. Physical memory size is 8 KB and is byte addressable

3. Page size is 128 Bytes

4. One level page table, where each page table entry contains a valid bit, a dirty bit, and the
physical page number

5. PTBR is 0x3ADC

6. There is a data TLB that stores only the last page table entry

The format of a PTE is as shown below. MSB is the valid bit followed by the dirty bit. Last few
bits are the physical page number (PPN).

|valid<1 bit>|dirty<1 bit>|PPN<n bits>|
|---|---|---|


-----

|Address|Data|
|---|---|
|3ADC|B8|
|3ADD|3A|
|3ADE|CD|
|3ADF|78|
|3AE4|F9|
|3CDC|B6|
|3DDC|4F|
|3EDC|F0|


**Part c) (4 points) How many pages does array ‘a’ occupy?**

2

**Part d) (4 points) To read a[1], what virtual page number(s) is(are) accessed?**

0x8

**Part e) (8 points) What physical memory addresses are accessed when reading a[1]?**

First physical memory access is for the PTE. The address is PTBR + VPN = 0x3AE4
Then we access the actual data.
The PTE (at 0x3AE4) has the data 0xF9, i.e., 1111 1001. So the physical page number is the last
6 bits, which are 111001. The page offset of the virtual address at 0x404 is 0000100, so the
two concatenated gives us the physical address 1110010000100, which is 0x1C84. Since a[1]
takes 4 bytes, accessing the data will reference four physical addresses: 0x1C84, 0x1C85,
0x1C86, 0x1C87.

**Part f) (4 points) How many data TLB misses will occur in the execution of the program?**
Assume the access order of the line “a[i] = a[i-2] + a[i-1];” is a[i-2], a[i-1],
```
a[i] with no other accesses in between.

```

-----

-----

**Final Exam**

**CSC 252**

**4 May 2022**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
**TAs: Nisarg Ujjainkar, Abhishek Tyag, Kalen Frieberg, Gunnar Hammonds, Mandar Juvekar,**
Zihao Lin, Vladimir Maksimovski, Yiyao (Jack) Yu

**Name: ____________________________________**

Problem 0 (3 points):

Problem 1 (12 points):

Problem 2 (18 points):

Problem 3 (25 points):

Problem 4 (20 points):

Problem 5 (26 points)

Problem 6 (26 points):

Total (130 points):

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 180 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (3 Points)**

Do you think 252 could be taught in high school?

**Problem 1: Miscellaneous (12 points)**

**Part a) (3 points) Write down the sum of 328 and 0x32 in base 2.**

**Part b) (3 points) Generally, the access time of a direct-mapped cache is ___ than that of a**
fully associative cache that is the same total size. Answer with <, >, =, <=, or >=.

**Part c) (3 points) (True or False) Virtual memory has no size limitation.**

**Part d) (3 points) Consider the following C struct Person:**
```
struct Person{
   long id;
   float age;
   float weight;
   float height;
   char name[20];
   char sex[7];
   struct Person * nextPerson;
};

```
What’s the size of the struct Person?


-----

**Problem 2: ISA (18 points)**

A stack-based ISA is designed. The ISA uses a hardware stack, and instructions in this ISA
manipulate this stack. Each entry on the stack is one byte long, and the memory is
byte-addressable. All instructions are 8-bit long, and are classified into two categories.

**R Category**

Binary encoding:

OpCode<7-5 bits> 00000<4-0 bits>

Instruction list:

**Instruction** **OpCode** **Role**

`pop` 001 Remove the item at the top of the stack.

`halt` 001 Halt the processor.

**I Category**

Binary encoding:

OpCode<7-5 bits> Immediate value in 2’s component<4-0 bits>

Instruction list:

|OpCode<7-5 bits>|00000<4-0 bits>|
|---|---|

|Instruction|OpCode|Role|
|---|---|---|
|pop|001|Remove the item at the top of the stack.|
|halt|001|Halt the processor.|

|OpCode<7-5 bits>|Immediate value in 2’s component<4-0 bits>|
|---|---|

|Instruction|OpCode|Role|
|---|---|---|
|pushi|000|Push sign-extended immediate value on the stack.|
|load|101|Let the top entry of the stack be A. Compute Address = A + sign-extended immediate value; Pop A from the stack; Use Address to load a byte from the main memory and push the byte on the stack.|
|store|100|Let the top entry of the stack be A, and the second entry of the stack be B. Compute Address = A + sign-extended immediate value; Pop A from the stack; Store B at the memory location Address; Pop B from the stack.|


-----

|loadd|110|Address = sign-extended immediate value. Load a byte from the memory using Address and push the byte on the stack.|
|---|---|---|


**Part a) (12 points) Encode the following instructions in binary.**

**(4 points) store -8**

**(4 points) pushi 7**

**(4 points) halt**

**Part b) (6 points) You want to implement a function that pops the top value from the stack**
and then pushes it back on the stack twice. Memory location at address 0 is reserved for this
instruction to use temporarily. Write an assembly program using the existing instructions to
implement this function.


-----

**Problem 3: Floating-Point Arithmetic (25 points)**

Suppose that the IEEE decided to add a new n-bit floating-point standard, with its main
characteristics consistent with the other IEEE standards. This n-bit standard can precisely

represent the value 6 [3], but cannot precisely represent 11 7 . The smallest positive

16 16


−30

**normalized value that can be represented in this standard is** 2 .

**Part a) (3 points) Convert** 6 [3] to Binary Normalized Form

16


**Part b) (3 points) How many of the n bits are fraction bits?**

**Part c) (3 points) What’s the bias of this standard?**

**Part d) (3 points) How many of the n bits are exponent bits?**

**Part e) (3 points) What is n?**

**Part f) (10 points) Suppose that using this new IEEE standard you perform two separate**
calculations, assume nearest-even rounding is used:

1. (256 + 2 [1]

4 [) −256]


2. (256 −256) + 2 [1]

4

What would be the result of these calculations? Do they both result in equivalent mathematically
precise answers? Show your math to earn partial credit.


-----

-----

**Problem 4: Cache (20 points)**

For all the questions in this problem, assume that we are using a 12-bit machine with a
byte-addressable memory and a direct-mapped cache. The cache can hold up to 16 cache lines.

**Part a) (3 points) How many bits do you need for the set index?**

**Part b) (17 points) The following sequence of 9 memory accesses generates the hits/misses**
shown. Some miss/hit entries are intentionally left blank. The cache is initially empty. Note that
the addresses are written in binary with spaces added between each 4 bits for readability. These
are not necessarily the tag/index/offset boundaries.

**#** **Address** **Hit/Miss**

`1` `1101 1111 0000` Miss

`2` `0000 1101 1111` Miss

`3` `1101 0111 0101` Miss

`4` `0000 1101 1100` Hit

`5` `1101 1111 0011` Miss
```
6 1111 0111 0010
7 1101 1111 0000
8 0000 1101 1101
9 1111 0111 0100

```
**(3 points) What is the number of tag bits?**

**(3 points) What is the number of offset bits?**

|#|Address|Hit/Miss|
|---|---|---|
|1|1101 1111 0000|Miss|
|2|0000 1101 1111|Miss|
|3|1101 0111 0101|Miss|
|4|0000 1101 1100|Hit|
|5|1101 1111 0011|Miss|
|6|1111 0111 0010||
|7|1101 1111 0000||
|8|0000 1101 1101||
|9|1111 0111 0100||


-----

**(3 points) What is the size of each cache line (ignore the valid bit, dirty bit, and tag bits etc.)?**
Show the formula you used to calculate this, and the value you get from it.

**(8 points) Fill the miss/hit for each of the blank entries.**


-----

**Problem 5: Assembly Programming (26 points)**

**Conventions:**

1. For this section, the assembly shown uses the AT&T/GAS syntax opcode src, dst
for instructions with two arguments where src is the source argument and dst is the
destination argument. For example, this means that mov a, b moves the value a into b.

2. All C code is compiled on a 64-bit machine, where arrays grow toward higher
addresses.

3. For functions that take an argument, the argument is stored in %rdi at the time the
function is called. The return value of this function is stored in %rax at the time the
function returns.

Consider the assembly of a C function void foobar(int *x) which takes a single int
pointer parameter x.
```
0000000000001159 <foobar>:
   1159: mov (%rdi),%eax
   115b: inc %eax
   115d: mov %eax,(%rdi)
   115f: lea 0x2ecf,%rdi
   1166: cmp $0x1,%eax
   1169: je 1177 <foobar+0x1e>
   116b: cmp $0x2,%eax
   116e: jne 117c <foobar+0x23>
   1170: lea 0x2eb4,%rdi
   1177: call 1030 <puts@plt>
   117c: ret

```
The addresses 0x2ecf and 0x2eb4 contain the beginning of character strings “foo” and
```
“bar” respectively. puts() is a standard C function that prints a character string given the

```
string start address as a parameter.

**Part a) (9 points)**

**(3 points) When the initial value of *x is 0, what is printed by the program?**

**(3 points) When the initial value of *x is 1, what is printed by the program?**


-----

**(3 points) The call on line 1177 is replaced with a jmp. Would this program still run**
correctly? Explain your answer.

**Part b) (17 points)**

Assuming that there are two threads, each of which executes the same foobar() function with
the same exact parameter x. *x is initially set to 0. For the sake of this problem, assume that the
instructions inside the puts() function are always executed as an atomic unit (they are either
executed together without interruption or not executed at all).

**(4 points) What are all the possible values of *x after both threads finish execution of**
```
foobar()?

```
**(4 points) What are all the possible strings printed by this multi-threaded program?**


-----

**(3 points) Suppose the first three instructions (1159 to 115d) could be replaced with a single**
atomic instruction called csc252. Would this guarantee that the program always ends with x
containing the value 2? Show you work to earn partial credit.

**(3 points) Would this guarantee that the program always prints the same string no matter how**
many times you run it? Show you work to earn partial credit.

**(3 points) Assuming that the two threads execute on two different processors, each with a**
separate cache. What is something that the processor designers have to pay attention to in order
to correctly implement the csc252 instruction?


-----

**Problem 6: Virtual Memory (26 points)**


Assume a virtual memory system that has the following characteristics:


1. The virtual address space is 32 KB and is byte addressable

2. Physical memory size is 8 KB and is byte addressable

3. Page size is 128 Bytes

4. One level page table, where each page table entry contains a valid bit, a dirty bit, and the
physical page number

5. PTBR is 0x3ADC

6. There is a data TLB that stores only the last page table entry

The format of a PTE is as shown below. MSB is the valid bit followed by the dirty bit. Last few
bits are the physical page number (PPN).

|valid<1 bit>|dirty<1 bit>|PPN<n bits>|
|---|---|---|


-----

|Address|Data|
|---|---|
|3ADC|B8|
|3ADD|3A|
|3ADE|CD|
|3ADF|78|
|3AE4|F9|
|3CDC|B6|
|3DDC|4F|
|3EDC|F0|


**Part c) (4 points) How many pages does array ‘a’ occupy?**

**Part d) (4 points) To read a[1], what virtual page number(s) is(are) accessed?**

**Part e) (8 points) What physical memory addresses are accessed when reading a[1]?**

**Part f) (4 points) How many data TLB misses will occur in the execution of the program?**
Assume the access order of the line “a[i] = a[i-2] + a[i-1];” is a[i-2], a[i-1],
```
a[i] with no other accesses in between.

```

-----

**Midterm Exam**

**CSC 252**

**3 March 2022**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
**TAs: Nisarg Ujjainkar, Abhishek Tyag, Kalen Frieberg, Gunnar Hammonds, Mandar Juvekar,**
Zihao Lin, Vladimir Maksimovski, Yiyao (Jack) Yu

**Name: ____________________________________**

Problem 0 (2 points):

Problem 1 (16 points):

Problem 2 (10 points):

Problem 3 (16 points):

Problem 4 (30 points):

Problem 5 (16 points)

Total (90 points):

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 75 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (2 Points)**
What’s the most unexpected thing you’ve learned in 252 so far?

While you might have seen some unexpected things, I hope none is magic once you *think*
about them.

**Problem 1: Fixed-Point Arithmetics (16 points)**

**Part a) (3 points) Represent decimal number 42 in hexadecimal form.**

0x2A

**Part b) (3 points) Represent octal (base 8) number 35 in decimal form and binary form.**

29, 11101

**Part c) (10 points)**

**(2 points) Represent signed integer values -25, -18 in 2’s complement form, assuming a 6-bit**
representation.

100111, 101110

**(6 points) If -25 and -18 are stored in two 6-bit registers R1 and R2, respectively, what are the**
values of the zero flag, sign flag, and overflow flag after the operation “add R1, R2”?

Zero flag: 0; sign flag: 0; overflow flag: 1

**(2 points) What is the value in R2 after “add R1, R2”? Expressed the result in binary.**


-----

**Problem 2: Floating-Point Arithmetics (10 points)**

**Part a) (2 points) Write -35.75 in the normalized scientific notation.**

###### -1.0001111 * 2^5

**Part b) (4 points)**

Suppose we are using a new 13-bit floating-point standard whose characteristics are compliant
with the floating-point representations we discussed in the class. For this representation,
exponent bias is 7.

**(2 points) How many bits are used for exponent and fraction?**

Exponent = 4
Fraction = 8

**(2 points) What is the floating point representation of 0xoA90 in this format?**

###### 1.1001 * 2^3

**Part c) (4 points) Consider two numbers f1 and f2, where f1 < f2. Now we express f1 and**
```
f2 in the IEEE single-precision format and interpret the resulting bitstreams as unsigned

```
integers. Let’s call the unsigned integers i1 and i2. Can we say i1 < i2? If not, provide a
counter-example. If yes, explain.


-----

**Problem 3: Logic Design (16 points)**

**Part a) (4 points)**

**(2 points) What is the result of a bitwise NAND operation between 101101 and 010110?**

111011

**(2 points) What is the result of a bitwise XOR operation between 101010 and 111011?**

010001

**Part b) (6 points)**

The given circuit consists of N XOR gates cascaded as shown.

**(4 points) What is the output of the circuit for the following values of N? You can write the**
output as a function of A.

N = 50

1

N = 63


-----

**(2 points) Can you find a relationship between values of N and the output in terms of A?**

N odd -> NOT(A)
N even -> 1

**Part c) (6 points)**

The combinatorial circuit shown below takes three 1-bit inputs: A, B, and C, and produces one
1-bit output. The relationship between the inputs and the output is shown below as a truth table.

The circuit contains two identical, unknown gates X.

**A** **B** **C** **Out**

0 0 0 0

0 0 1 1

0 1 0 1

0 1 1 0

1 0 0 0

1 0 1 0

1 1 0 0

1 1 1 0

**(3 points) What is gate X?**

XOR
plugging in C = 1 and looking at the table gives the value of X(A,1). Using that, one can
figure out X(B,0) which gives the gate

**(3 points) Assuming the delay of each gate is 1ps, what is the delay of the entire circuit?**

|A|B|C|Out|
|---|---|---|---|
|0|0|0|0|
|0|0|1|1|
|0|1|0|1|
|0|1|1|0|
|1|0|0|0|
|1|0|1|0|
|1|1|0|0|
|1|1|1|0|


-----

**Problem 4: Assembly Programming (30 points)**

**Conventions:**

1. For this section, the assembly shown uses the AT&T/GAS syntax opcode src, dst
for instructions with two arguments where src is the source argument and dst is the
destination argument. For example, this means that mov a, b moves the value a into b
and cmp a, b then jge c would compare b to a then jump to c if b ≥ a.

2. All C code is compiled on a 64-bit machine, where arrays grow toward higher
addresses.

3. For functions that take two arguments, the first argument is stored in %edi and the
second is stored in %esi at the time the function is called. The return value of this
function is stored in %eax at the time the function returns.

**Part a) (20 points)**

The following is the C definition of struct Data:
```
struct Data {
  int matrix[3][3];
  int *value;
};

```
**(4 points) What is the size of struct Data?**

48

**(4 points) If the start of struct Data d1 is stored at -0x30(%rbp), where in memory is**
```
d1.matrix[2][1] stored?

```
-0x14

**(6 points) Still assuming the struct Data d1 is stored at -0x30(%rbp). Complete the**
instructions below used to access *(d1.value).
```
mov A (%rbp),%rdx
 B (%rdx),%eax

```
**A:**


-----

**B:**

mov

Consider the C function is_equal():
```
int is_equal(struct Data *p1, struct Data *p2) {
  char *ptr1 = (char *) p1;
  char *ptr2 = (char *) p2;
  for (int i = 0; i < sizeof(struct Data); i++) {
    if (ptr1[i] != ptr2[i]) return 0;
  }
  return 1;
}

```
**(3 points) What does is_equal() do?**

Return 1 if all bytes in two struct Data are equal (including the padding), 0 if otherwise

Now assuming d1 and d2 are initialized as follows:
```
struct Data d1 = {
 .matrix = {
  {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9}
 },
 .value = NULL
};
struct Data d2 = {
 .matrix = {
  {1, 2, 3},
  {4, 5, 6},

```

-----

```
  {7, 8, 9}
 },
 .value = NULL
};

```
**(3 points) Will is_equal(&d1, &d2) always return 1? Explain.**

No. The padding can be different since it is undefined.

(The initialization for d2.value is missing for the online exam. This would also result in no
since undefined is not the same as NULL in C. It can be any value)

**Part b) (10 points) The following is the assembly code for a mystery function foo():**
```
0000000000000000 <foo>:
  0: xor %eax,%eax
  2: xor %ecx,%ecx
  5: mov %esi,%edx
  7: add (%rdi,%eax,4),%ecx
  b: sub %eax,%edx
  d: dec %edx
  f: jle 16 <foo+0x16>
 11: inc %eax
 14: jmp 5 <foo+0x5>
 16: mov %ecx,%eax
 19: ret

```
At the beginning of execution, the value stored in %esi is 4, and %rdi contains the start address
of a 4-element integer array [9, 8, 7, 6].

**(3 points) What is the value of %ecx after the second execution of add**
```
(%rdi,%eax,4),%ecx?

```
17

**(3 points) How many times is jmp 5 executed?**


-----

**(4 points) Does this function terminate? If not, why? If so, what value does the function**
return?


-----

**Problem 5: Processor architecture (16 points)**

**Part a) (6 points)**

We have two processors:

  - Processor 1 has a 5 stage pipeline with stages: Fetch, Decode, Execute, Memory, Write
Back and a 2.5 GHz clock frequency (i.e., 400 ps per cycle). The functionalities of the five
stages are the same as we discussed in the class.

  - Processor 2 has a 3 stage pipeline with stages: Fetch, Decode, EMW, where the EMW
stage combines the Execute, Memory, and Write Back stages in Processor 1. This
processor has a clock frequency of 1.6 GHz (i.e., 625 ps per cycle)

Note that there are 10[12] ps per second.

**(4 points) What’s the throughput (in instructions per second) for Processor 1 and Processor 2,**
respectively, assuming no stalls?

Processor 1: 2.5 billion instructions per second
Processor 2: 1.6 billion instructions per second

**(2 points) For what reasons would you expect processor 2 to have a higher clock frequency**
than processor 1? You should assume that everything between the processors are the same other
than clock frequency and pipeline structure.

This question was a typo should be 2 faster than 1. Was given as extra credit.
Processor 1 has a higher clock speed since its last stage groups together less components and
can therefore takes less time to execute.

**Part b) (10 points)**

Assume a processor architecture implementing the x86 ISA that is pipelined in 5 stages (fetch,
decode, execute, memory, and write back) as discussed in lectures. The program is executing the
piece of assembly shown below on the left. Assuming the pipeline is empty at the start of the
program, and %rip points to the first instruction.


-----

|Assembly Code|Relevant part of the memory & registers at the start of the program|
|---|---|
|.L1: incq %rax .L2: cmpq %rax, %rbx .L3: jge .L8 .L4: addq $0x3, $rax .L5: xorq %rax, %rbx .L6: cmpq %rbx, %rax .L7: jmp .L9 .L8: nop .L9: leaq -0x8(rcx), %rdx .L10: addq (%rdx), %rax .L11: movq 0x8(%rcx), %rbx .L12: cmpq %rax, %rbx .L13: jle .L15 .L14: negq %rax .L15: addq %rax, %rbx|Registers: %rax: 0x196 %rbx: 0x200 %rcx: 0x40000810 %rdx: 0 Memory: 0x40000800: 0x205 0x40000808: 0x207 0x40000010: 0x352 0x40000018: 0x595 0x40000020: 0x400|


**(3 points) Which jump instructions get executed and are taken (i.e., do not fall-through)? List**
them by their labels, e.g. L3, L7, L13.

L3

**(5 points) Write down the list of stalls due to control dependencies. Write down the labels**
of all the pairs of instructions creating such stalls, e.g., L1 -> L2 if L1 and L2 create a control
dependency.

L3 -> L4
L3->L8
L7 -> L9
L13-> L14
L13-> L15

**(2 points) Where in the pipeline is a control dependency resolved?**


-----

**Midterm Exam**

**CSC 252**

**3 March 2022**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
**TAs: Nisarg Ujjainkar, Abhishek Tyag, Kalen Frieberg, Gunnar Hammonds, Mandar Juvekar,**
Zihao Lin, Vladimir Maksimovski, Yiyao (Jack) Yu

**Name: ____________________________________**

Problem 0 (2 points):

Problem 1 (16 points):

Problem 2 (10 points):

Problem 3 (16 points):

Problem 4 (30 points):

Problem 5 (16 points)

Total (90 points):

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 75 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (2 Points)**
What’s the most unexpected thing you’ve learned in 252 so far?

**Problem 1: Fixed-Point Arithmetics (16 points)**

**Part a) (3 points) Represent decimal number 42 in hexadecimal form.**

**Part b) (3 points) Represent octal (base 8) number 35 in decimal form and binary form.**

**Part c) (10 points)**

**(2 points) Represent signed integer values -25, -18 in 2’s complement form, assuming a 6-bit**
representation.

**(6 points) If -25 and -18 are stored in two 6-bit registers R1 and R2, respectively, what are the**
values of the zero flag, sign flag, and overflow flag after the operation “add R1, R2”?

**(2 points) What is the value in R2 after “add R1, R2”? Expressed the result in binary.**


-----

**Problem 2: Floating-Point Arithmetics (10 points)**

**Part a) (2 points) Write -35.75 in the normalized scientific notation.**

**Part b) (4 points)**

Suppose we are using a new 13-bit floating-point standard whose characteristics are compliant
with the floating-point representations we discussed in the class. For this representation,
exponent bias is 7.

**(2 points) How many bits are used for exponent and fraction?**

**(2 points) What is the floating point representation of 0xoA90 in this format?**

**Part c) (4 points) Consider two numbers f1 and f2, where f1 < f2. Now we express f1 and**
```
f2 in the IEEE single-precision format and interpret the resulting bitstreams as unsigned

```
integers. Let’s call the unsigned integers i1 and i2. Can we say i1 < i2? If not, provide a
counter-example. If yes, explain.


-----

**Problem 3: Logic Design (16 points)**

**Part a) (4 points)**

**(2 points) What is the result of a bitwise NAND operation between 101101 and 010110?**

**(2 points) What is the result of a bitwise XOR operation between 101010 and 111011?**

**Part b) (6 points)**

The given circuit consists of N XOR gates cascaded as shown.

**(4 points) What is the output of the circuit for the following values of N? You can write the**
output as a function of A.

N = 50

N = 63


-----

**(2 points) Can you find a relationship between values of N and the output in terms of A?**

**Part c) (6 points)**

The combinatorial circuit shown below takes three 1-bit inputs: A, B, and C, and produces one
1-bit output. The relationship between the inputs and the output is shown below as a truth table.

The circuit contains two identical, unknown gates X.

**A** **B** **C** **Out**

0 0 0 0

0 0 1 1

0 1 0 1

0 1 1 0

1 0 0 0

1 0 1 0

1 1 0 0

1 1 1 0

**(3 points) What is gate X?**

**(3 points) Assuming the delay of each gate is 1ps, what is the delay of the entire circuit?**

|A|B|C|Out|
|---|---|---|---|
|0|0|0|0|
|0|0|1|1|
|0|1|0|1|
|0|1|1|0|
|1|0|0|0|
|1|0|1|0|
|1|1|0|0|
|1|1|1|0|


-----

**Problem 4: Assembly Programming (30 points)**

**Conventions:**

1. For this section, the assembly shown uses the AT&T/GAS syntax opcode src, dst
for instructions with two arguments where src is the source argument and dst is the
destination argument. For example, this means that mov a, b moves the value a into b
and cmp a, b then jge c would compare b to a then jump to c if b ≥ a.

2. All C code is compiled on a 64-bit machine, where arrays grow toward higher
addresses.

3. For functions that take two arguments, the first argument is stored in %edi and the
second is stored in %esi at the time the function is called. The return value of this
function is stored in %eax at the time the function returns.

**Part a) (20 points)**

The following is the C definition of struct Data:
```
struct Data {
  int matrix[3][3];
  int *value;
};

```
**(4 points) What is the size of struct Data?**

**(4 points) If the start of struct Data d1 is stored at -0x30(%rbp), where in memory is**
```
d1.matrix[2][1] stored?

```
**(6 points) Still assuming the struct Data d1 is stored at -0x30(%rbp). Complete the**
instructions below used to access *(d1.value).
```
mov A (%rbp),%rdx
 B (%rdx),%eax

```
**A:**


-----

**B:**

Consider the C function is_equal():
```
int is_equal(struct Data *p1, struct Data *p2) {
  char *ptr1 = (char *) p1;
  char *ptr2 = (char *) p2;
  for (int i = 0; i < sizeof(struct Data); i++) {
    if (ptr1[i] != ptr2[i]) return 0;
  }
  return 1;
}

```
**(3 points) What does is_equal() do?**

Now assuming d1 and d2 are initialized as follows:
```
struct Data d1 = {
 .matrix = {
  {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9}
 },
 .value = NULL
};
struct Data d2 = {
 .matrix = {
  {1, 2, 3},
  {4, 5, 6},

```

-----

```
  {7, 8, 9}
 },
 .value = NULL
};

```
**(3 points) Will is_equal(&d1, &d2) always return 1? Explain.**

**Part b) (10 points) The following is the assembly code for a mystery function foo():**
```
0000000000000000 <foo>:
  0: xor %eax,%eax
  2: xor %ecx,%ecx
  5: mov %esi,%edx
  7: add (%rdi,%eax,4),%ecx
  b: sub %eax,%edx
  d: dec %edx
  f: jle 16 <foo+0x16>
 11: inc %eax
 14: jmp 5 <foo+0x5>
 16: mov %ecx,%eax
 19: ret

```
At the beginning of execution, the value stored in %esi is 4, and %rdi contains the start address
of a 4-element integer array [9, 8, 7, 6].

**(3 points) What is the value of %ecx after the second execution of add**
```
(%rdi,%eax,4),%ecx?

```
**(3 points) How many times is jmp 5 executed?**


-----

**(4 points) Does this function terminate? If not, why? If so, what value does the function**
return?


-----

**Problem 5: Processor architecture (16 points)**

**Part a) (6 points)**

We have two processors:

  - Processor 1 has a 5 stage pipeline with stages: Fetch, Decode, Execute, Memory, Write
Back and a 2.5 GHz clock frequency (i.e., 400 ps per cycle). The functionalities of the five
stages are the same as we discussed in the class.

  - Processor 2 has a 3 stage pipeline with stages: Fetch, Decode, EMW, where the EMW
stage combines the Execute, Memory, and Write Back stages in Processor 1. This
processor has a clock frequency of 1.6 GHz (i.e., 625 ps per cycle)

Note that there are 10[12] ps per second.

**(4 points) What’s the throughput (in instructions per second) for Processor 1 and Processor 2,**
respectively, assuming no stalls?

**(2 points) For what reasons would you expect processor 2 to have a higher clock frequency**
than processor 1? You should assume that everything between the processors are the same other
than clock frequency and pipeline structure.

**Part b) (10 points)**

Assume a processor architecture implementing the x86 ISA that is pipelined in 5 stages (fetch,
decode, execute, memory, and write back) as discussed in lectures. The program is executing the
piece of assembly shown below on the left. Assuming the pipeline is empty at the start of the
program, and %rip points to the first instruction.


-----

|Assembly Code|Relevant part of the memory & registers at the start of the program|
|---|---|
|.L1: incq %rax .L2: cmpq %rax, %rbx .L3: jge .L8 .L4: addq $0x3, $rax .L5: xorq %rax, %rbx .L6: cmpq %rbx, %rax .L7: jmp .L9 .L8: nop .L9: leaq -0x8(rcx), %rdx .L10: addq (%rdx), %rax .L11: movq 0x8(%rcx), %rbx .L12: cmpq %rax, %rbx .L13: jle .L15 .L14: negq %rax .L15: addq %rax, %rbx|Registers: %rax: 0x196 %rbx: 0x200 %rcx: 0x40000810 %rdx: 0 Memory: 0x40000800: 0x205 0x40000808: 0x207 0x40000010: 0x352 0x40000018: 0x595 0x40000020: 0x400|


**(3 points) Which jump instructions get executed and are taken (i.e., do not fall-through)? List**
them by their labels, e.g. L3, L7, L13.

**(5 points) Write down the list of stalls due to control dependencies. Write down the labels**
of all the pairs of instructions creating such stalls, e.g., L1 -> L2 if L1 and L2 create a control
dependency.

**(2 points) Where in the pipeline is a control dependency resolved?**


-----

###### Final Exam

**CSC 252**

**12 May 2021**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
**TAs: Rongcui Dong, Elana Elman, Kalen Frieberg, Sudhanshu Gupta, Yiyao (Jack) Yu, Vladimir**
Maksimovski, Nathan Reed, Rafaello Sanna

**Name: ____________________________________**

Problem 0 (3 points):

Problem 1 (14 points):

Problem 2 (15 points):

Problem 3 (16 points):

Problem 4 (22 points):

Problem 5 (30 points)

Total (100 points):

Extra Credit (15 points)

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 3 hours to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (3 Points)**
What’s the most surprising thing about computers you learned from 252?

**Problem 1: Miscellaneous (14 points + 12 points extra credit)**
**Part a) (3 points) Convert the decimal number 334 to hexadecimal.**

0x14E

**Part b) (3 points) Why wouldn't a user program that contains an infinite loop freeze the entire**
computer even if the computer has only one processor?

OS preempts processes periodically to context-switch and execute other processes.

**To get full points, the answer must show:**

1. Operating System

2. Context switch

3. Preemption

**Part c) (8 points) Consider a shell in Linux, sh, that supports basic foreground/background**
job control, just like the one you implemented in Assignment 4. Initially, myprogA is running in
the foreground, myprogB is running in the background as job 1, and myprogC is stopped in the
background as job 2. Assume this initial state for each question below.

**(4 points) The user presses Ctrl-C and kills the foreground process. List all signals that are**
generated and the receivers of these signals.


-----

**(4 points) myprogA finishes, then the user presses Ctrl-Z at the shell's command prompt.**
List all the signals that are generated and the receivers of these signals.

SIGCHLD to sh; SIGTSTP to sh

**Part d) (this entire part is extra credit; 12 points) You are designing a new ISA called**
URISA, which supports the following instructions.

Instruction Semantics

`ADDI rd, rs1, imm` Sum immediate imm and register rs1, store the sum in register rd

`ADD rd, rs1, rs2` Sum two registers rs1 and rs2, store the result in register rd

`LW rd, delta(rs1)` Load 4 bytes to register rd from memory location specified by
```
             rs1 + delta

```
`SW rd, delta(rt)` Store 4 bytes from register rd to memory location specified by rt
```
             + delta

```
`BLTU rs, rt, label` Jump to label if register rs < rt; both rs and rt are
interpreted as unsigned numbers.

In addition, these registers are supported in URISA:

Register(s) Description X86 Equivalent

`zero` Always reads zero; write ignored 
`ra` Return address of a function On stack

`a1` Return value of a function `%eax`

`sp` Stack pointer `%esp`

`t0-6` Temporary registers Any free register, e.g., %ecx, %edx

Translate each of the following x86 instructions to the equivalent URISA instructions using only
the instructions listed above. You may use any register above, but no new memory location other

|Instruction|Semantics|
|---|---|
|ADDI rd, rs1, imm|Sum immediate imm and register rs1, store the sum in register rd|
|ADD rd, rs1, rs2|Sum two registers rs1 and rs2, store the result in register rd|
|LW rd, delta(rs1)|Load 4 bytes to register rd from memory location specified by rs1 + delta|
|SW rd, delta(rt)|Store 4 bytes from register rd to memory location specified by rt + delta|
|BLTU rs, rt, label|Jump to label if register rs < rt; both rs and rt are interpreted as unsigned numbers.|

|Register(s)|Description|X86 Equivalent|
|---|---|---|
|zero|Always reads zero; write ignored|-|
|ra|Return address of a function|On stack|
|a1|Return value of a function|%eax|
|sp|Stack pointer|%esp|
|t0-6|Temporary registers|Any free register, e.g., %ecx, %edx|


-----

than what is used in the original x86 instruction. Note that the x86 instructions use the
AT&T/GAS syntax, i.e., opcode src, dst.

For example, the x86 instruction pop (%eax) would be equivalent to:
```
LW t0, 0(sp)
SW t0, 0(a1)
ADDI sp, sp, 4

```
**(3 points extra credit) add $0x8, %esp**

ADDI sp, sp, 0x8

**(3 points extra credit) add %eax, 8(%esp)**

LW t0, 8(sp)
ADD t0, a1, t0
SW t0, 8(sp)
// Or equivalent

**(3 points extra credit) push $0x252**

ADDI t0, zero, 0x252
ADDI sp, sp, -4
SW t0, 0(sp)
// Or equivalent

**(3 points extra credit) This processor does not have an Overflow flag. Fill in the following**
assembly so that if the ADD instruction causes an unsigned overflow, the program jumps to the
```
overflow label.
ADD t3, t1, t2
_____BLTU t3, t1, overflow ; or BLTU t3, t2, overflow
;… code omitted
overflow:
;… code omitted

```

-----

**Problem 2: Floating-Point Arithmetics (15 points)**

**Part a) (3 points) Put6** [5] into the binary normalized form.

16

2

1. 100101 × 2

**Part b) (12 points) The IEEE has decided to introduce a floating-point standard of some**
unknown size, whose main characteristics are consistent with existing floating-point number
representations that we discussed in the class.


The following bit sequence contains the exact encoding of 6 [5] in this new standard, but is

16

padded with arbitrary bits at the beginning and in the end: 10010100110010110.

**(3 points) How many bits are used for the fraction in this new standard?**

6

**(3 points) How many bits are used for the exponent in this new standard?**

4

**(3 points) What is the bias in this new standard?**

7

**(3 points) What is the smallest positive value that can be precisely expressed using this new**
floating-point format? You can write your answer either in the binary-normalized form or as a
bit sequence.


-----

**Problem 3: Assembly Programming (16 points)**

**Conventions:**

1. For this section, the assembly shown uses the AT&T/GAS syntax opcode src, dst
for instructions with two arguments where src is the source argument and dst is the
destination argument. For example, this means that mov a, b moves the value a into b
and cmp a, b then jge c would compare b to a then jump to c if b ≥ a.

2. All C code is compiled on a 64-bit machine, where arrays grow toward higher addresses.

3. For functions that take two arguments, the first argument is stored in %edi and the
second is stored in %esi at the time the function is called. The return value of this
function is stored in %eax at the time the function returns.

**Part a) (9 points) The following is assembly code for a C function find_next():**
```
0000000000001169 <find_next>:
   1169:  mov %edi,%eax
   116b:  inc %eax
   116d:  mov $0x2,%edx
   1172:  cmp %eax,%edx
   1174:  jge 1184 <find_next+0x1b>
   1176:  mov %eax,%ecx
   1178:  sub %edx,%ecx
   117a:  test %ecx,%ecx
   117c:  jg 1178 <find_next+0xf>
   117e:  je 116b <find_next+0x2>
   1180:  inc %edx
   1182:  jmp 1172 <find_next+0x9>
   1184:  ret

```
**(3 points) What is the return value of find_next(2)?**

3

**(3 points) What is returned when a non-positive x is provided to find_next(x)? Show your**
answer in terms of x.


-----

**(3 points) For positive values of x as input, what does find_next(x) do?**

Finds the smallest prime larger than x

**Part b) (7 points) Some students wrote a CSC252 project in assembly. They discover right**
before submission that the machine used for grading has a faulty call instruction. They decide
to rewrite the project without using call. The behavior of a call can be reproduced with
**exactly two other instructions.**

**(3 points) On a correct 64-bit machine, which register(s) does call 1169 update?**
Explain how the register value(s) change.

%rsp = %rsp - 8
%rip = 1169

**(4 points) Which instructions would they use to replace the faulty call? Provide just the**
**names of the instructions in the order they are used.**


-----

**Problem 4: Cache (22 points)**

You are designing a cache for an 8-bit machine that has a byte-addressable memory. Remember
that an 8-bit machine means that the length of a memory address is 8 bits. The cache line size is
2 bytes. As a first attempt, you design a 4-way set associative cache with 2 sets and a random
replacement policy. A random replacement policy chooses a line to replace at random within the
set. To reduce memory traffic, you design it to be a write-back cache.

Assuming that the machine runs only one program, which will generate the following memory
access sequence.

Access Address

1 `00110000`

2 `10100010`

3 `10011001`

4 `01011101`

5 `00110111`

6 `10011010`

7 `01011110`

8 `01101100`

9 `10100010`

**(6 points) How many bits do you need for the tag, the set index, and the cache line offset?**

6 bits tag, 1 bit set, 1 bit offset
(Of the 8 bits in an address, 1 bit decides which byte of the cache line it is, 1 bit decides which
set it’s in, and the remaining 6 bits must be the tag.)

**(3 points) How many overhead bits does this cache have? Recall that overhead includes the tag**
bits, the dirty bits (if needed), and the replacement bits (if needed). Show you work to earn full
credit.

|Access|Address|
|---|---|
|1|00110000|
|2|10100010|
|3|10011001|
|4|01011101|
|5|00110111|
|6|10011010|
|7|01011110|
|8|01101100|
|9|10100010|


-----

**(3 points) Assuming the cache is initially empty. How many cache misses will the program**
generate when it’s run for the first time?

8 (all but the last access miss)

**(3 points) How many cache misses will the program generate when it’s run for the second**
time?

0 (All addresses were loaded into the cache on the first run, and none were replaced.)

**(4 points) Looking carefully at the access pattern, you realize that it is possible to design a**
cache with a smaller overhead that achieves a 100% hit rate for the program after the initial run.

Without changing the cache line size, explain the new design of your cache, i.e., its associativity
and the number of sets.

4 sets, 2-associative

(An 8 set direct-mapped cache causes some misses, and a fully associative cache does not
reduce overhead because set index bits are not part of the overhead.)

**(3 points) What is the overhead of your new cache design?**


-----

**Problem 5: Virtual Memory (30 points + 3 points extra credit)**

You are building a machine with virtual memory support. The virtual address space is 256 KB
(2^18 bytes). The physical memory size is 32KB. The system uses a one-level page table.

**Part a) Basic organization (13 points + 3 points extra credit)**
**(4 points) Assume the page size is 1KB. How many bits are used for the physical page number**
(PPN), and how many for the virtual page number (VPN)?

PPN: 5
VPN: 8

**(3 points) What is the size of one PTE, assuming that the only overhead in the PTE is one valid**
bit and that the disk address is 2 bits longer than the PPN.

Disk address + 1 = 8

**(3 points) You decide to experiment with changing the page size to 4KB. What is the size of one**
PTE now? Continue to assume that the only overhead in the PTE is one valid bit and that the
disk address is 2 bits longer than the PPN.

Disk address + 1 = 6

**(3 points) The system has a TLB. What is likely to happen to the TLB hit rate when we increase**
the page size to 4KB? Will it increase or decrease? Explain your answer to receive ANY credit.

It will increase.

1. Since PTEs are smaller, more of them can be stored in a cache of the same size.

2. Since there are fewer pages, the TLB will store a higher proportion of PTEs.

3. Spatial locality properties make it likely that TLB hit rate will increase.

**(3 points extra credit) If the machine were to use a two-level page table with a 4KB page size,**
how many PTE entries are there in the level 1 page table?


-----

**Part b) Protection (8 points)**
The major customer for your system is the US Government. They want a secure system that is
safer from buffer overflow attacks. The memory protection system should help protect against
arbitrary code execution in the event that someone manages to exploit a buffer overflow.

**(4 points) Briefly explain the mechanism by which an attacker exploits a buffer overflow. Your**
answer must cover 1) where in memory the attacker can place the code and 2) how the injected
code can be executed.

1. Attacker uses buffer that is too short/input is not bounds checked to store encoded
machine instructions.
2. Attacker input overwrites return address. When vulnerable function returns, it will return
to the attacker-controlled return address, which will point to the start of the attacker’s code.

**(4 points) Now you want to augment the PTE structure with permission information to defend**
against buffer overflow attacks. In order to keep the overhead low, you decide that you will use a
maximum of 2 permission bits, which will indicate whether a page can be written to, whether a
page can be read from, and whether a page’s contents can be executed as code. Assuming
defending buffer overflow attacks is your sole goal in this design process, how will you use the 2
permission bits? Explain the semantics of each bit to receive full credit.

Use 1 bit for read permission (1 = can read, 0 = no read)
Use 1 bit for write/execute (1 = write, no execute, 0 = execute, no write)

The key insight is that we don’t want user-writable memory to also be executable, so we can
use one bit to handle both write and execute permission, since if it’s writable, it can’t be
executable, and if it’s executable, it can’t be writable.

**Part c) Performance (9 points)**

Management decided to go with the 1KB page size for this machine and removed the TLB to cut
costs. Consider the C code below. Assume:

1. A 1-level page table translation scheme with the page table starting empty, and

2. `arr is aligned such that it starts 8 bytes before a page boundary.`
```
void func() {
   int arr[2048];

```

-----

```
   for(int i = 0; i < 8; i++) {
       if(rand_0_1() == 1) {
          printf("%d\n", arr[(i << 8) + 1]);
          printf("%d\n", arr[(i << 8) + 2]);
       } else {
          printf("%d\n", arr[i]);
          printf("%d\n", arr[i + 2]);
       }
   }
}
rand_0_1() is a function that returns either 0 or 1, at random.

```
For the following 3 questions, only count page faults generated by accessing elements of arr.

**(3 points) What is the maximum number of page faults that this code could possibly generate?**
Explain.

**9. 2 on the first iteration. Then if the function returns 1 every time, it will cause 1 additional**
page fault, because the first access for each iteration will be on the page that was loaded for
the second access of the last iteration. The second access on each iteration will cause a fault.

**(3 points) What is the minimum number of page faults that this code could possibly generate?**
Explain.

**2, if the function returns 0 every time. The 2 are from the first iteration, everything after that**
is on the same page.

**(3 points) Suppose that the rand_0_1() function is faulty and it returns 0 40% of the time**
and 1 60% of the time. How many page faults, on average, will this code generate? Explain.


-----

###### Final Exam

**CSC 252**

**12 May 2021**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
**TAs: Rongcui Dong, Elana Elman, Kalen Frieberg, Sudhanshu Gupta, Yiyao (Jack) Yu, Vladimir**
Maksimovski, Nathan Reed, Rafaello Sanna

**Name: ____________________________________**

Problem 0 (3 points):

Problem 1 (14 points):

Problem 2 (15 points):

Problem 3 (16 points):

Problem 4 (22 points):

Problem 5 (30 points)

Total (100 points):

Extra Credit (15 points)

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 3 hours to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (3 Points)**
What’s the most surprising thing about computers you learned from 252?

**Problem 1: Miscellaneous (14 points + 12 points extra credit)**
**Part a) (3 points) Convert the decimal number 334 to hexadecimal.**

**Part b) (3 points) Why wouldn't a user program that contains an infinite loop freeze the entire**
computer even if the computer has only one processor?

**Part c) (8 points) Consider a shell in Linux, sh, that supports basic foreground/background**
job control, just like the one you implemented in Assignment 4. Initially, myprogA is running in
the foreground, myprogB is running in the background as job 1, and myprogC is stopped in the
background as job 2. Assume this initial state for each question below.

**(4 points) The user presses Ctrl-C and kills the foreground process. List all signals that are**
generated and the receivers of these signals.


-----

**(4 points) myprogA finishes, then the user presses Ctrl-Z at the shell's command prompt.**
List all the signals that are generated and the receivers of these signals.

**Part d) (this entire part is extra credit; 12 points) You are designing a new ISA called**
URISA, which supports the following instructions.

Instruction Semantics

`ADDI rd, rs1, imm` Sum immediate imm and register rs1, store the sum in register rd

`ADD rd, rs1, rs2` Sum two registers rs1 and rs2, store the result in register rd

`LW rd, delta(rs1)` Load 4 bytes to register rd from memory location specified by
```
             rs1 + delta

```
`SW rd, delta(rt)` Store 4 bytes from register rd to memory location specified by rt
```
             + delta

```
`BLTU rs, rt, label` Jump to label if register rs < rt; both rs and rt are
interpreted as unsigned numbers.

In addition, these registers are supported in URISA:

Register(s) Description X86 Equivalent

`zero` Always reads zero; write ignored 
`ra` Return address of a function On stack

`a1` Return value of a function `%eax`

`sp` Stack pointer `%esp`

`t0-6` Temporary registers Any free register, e.g., %ecx, %edx

Translate each of the following x86 instructions to the equivalent URISA instructions using only
the instructions listed above. You may use any register above, but no new memory location other

|Instruction|Semantics|
|---|---|
|ADDI rd, rs1, imm|Sum immediate imm and register rs1, store the sum in register rd|
|ADD rd, rs1, rs2|Sum two registers rs1 and rs2, store the result in register rd|
|LW rd, delta(rs1)|Load 4 bytes to register rd from memory location specified by rs1 + delta|
|SW rd, delta(rt)|Store 4 bytes from register rd to memory location specified by rt + delta|
|BLTU rs, rt, label|Jump to label if register rs < rt; both rs and rt are interpreted as unsigned numbers.|

|Register(s)|Description|X86 Equivalent|
|---|---|---|
|zero|Always reads zero; write ignored|-|
|ra|Return address of a function|On stack|
|a1|Return value of a function|%eax|
|sp|Stack pointer|%esp|
|t0-6|Temporary registers|Any free register, e.g., %ecx, %edx|


-----

than what is used in the original x86 instruction. Note that the x86 instructions use the
AT&T/GAS syntax, i.e., opcode src, dst.

For example, the x86 instruction pop (%eax) would be equivalent to:
```
LW t0, 0(sp)
SW t0, 0(a1)
ADDI sp, sp, 4

```
**(3 points extra credit) add $0x8, %esp**

**(3 points extra credit) add %eax, 8(%esp)**

**(3 points extra credit) push $0x252**

**(3 points extra credit) This processor does not have an Overflow flag. Fill in the following**
assembly so that if the ADD instruction causes an unsigned overflow, the program jumps to the
```
overflow label.
ADD t3, t1, t2
___________ // Your answer here
;… code omitted
overflow:
;… code omitted

```

-----

**Problem 2: Floating-Point Arithmetics (15 points)**

**Part a) (3 points) Put6** [5] into the binary normalized form.

16

**Part b) (12 points) The IEEE has decided to introduce a floating-point standard of some**
unknown size, whose main characteristics are consistent with existing floating-point number
representations that we discussed in the class.


The following bit sequence contains the exact encoding of 6 [5] in this new standard, but is

16

padded with arbitrary bits at the beginning and in the end: 10010100110010110.

**(3 points) How many bits are used for the fraction in this new standard?**

**(3 points) How many bits are used for the exponent in this new standard?**

**(3 points) What is the bias in this new standard?**

**(3 points) What is the smallest positive value that can be precisely expressed using this new**
floating-point format? You can write your answer either in the binary-normalized form or as a
bit sequence.


-----

**Problem 3: Assembly Programming (16 points)**

**Conventions:**

1. For this section, the assembly shown uses the AT&T/GAS syntax opcode src, dst
for instructions with two arguments where src is the source argument and dst is the
destination argument. For example, this means that mov a, b moves the value a into b
and cmp a, b then jge c would compare b to a then jump to c if b ≥ a.

2. All C code is compiled on a 64-bit machine, where arrays grow toward higher addresses.

3. For functions that take two arguments, the first argument is stored in %edi and the
second is stored in %esi at the time the function is called. The return value of this
function is stored in %eax at the time the function returns.

**Part a) (9 points) The following is assembly code for a C function find_next():**
```
0000000000001169 <find_next>:
   1169:  mov %edi,%eax
   116b:  inc %eax
   116d:  mov $0x2,%edx
   1172:  cmp %eax,%edx
   1174:  jge 1184 <find_next+0x1b>
   1176:  mov %eax,%ecx
   1178:  sub %edx,%ecx
   117a:  test %ecx,%ecx
   117c:  jg 1178 <find_next+0xf>
   117e:  je 116b <find_next+0x2>
   1180:  inc %edx
   1182:  jmp 1172 <find_next+0x9>
   1184:  ret

```
**(3 points) What is the return value of find_next(2)?**

**(3 points) What is returned when a non-positive x is provided to find_next(x)? Show your**
answer in terms of x.


-----

**(3 points) For positive values of x as input, what does find_next(x) do?**

**Part b) (7 points) Some students wrote a CSC252 project in assembly. They discover right**
before submission that the machine used for grading has a faulty call instruction. They decide
to rewrite the project without using call. The behavior of a call can be reproduced with
**exactly two other instructions.**

**(3 points) On a correct 64-bit machine, which register(s) does call 1169 update?**
Explain how the register value(s) change.

**(4 points) Which instructions would they use to replace the faulty call? Provide just the**
**names of the instructions in the order they are used.**


-----

**Problem 4: Cache (22 points)**

You are designing a cache for an 8-bit machine that has a byte-addressable memory. Remember
that an 8-bit machine means that the length of a memory address is 8 bits. The cache line size is
2 bytes. As a first attempt, you design a 4-way set associative cache with 2 sets and a random
replacement policy. A random replacement policy chooses a line to replace at random within the
set. To reduce memory traffic, you design it to be a write-back cache.

Assuming that the machine runs only one program, which will generate the following memory
access sequence.

Access Address

1 `00110000`

2 `10100010`

3 `10011001`

4 `01011101`

5 `00110111`

6 `10011010`

7 `01011110`

8 `01101100`

9 `10100010`

**(6 points) How many bits do you need for the tag, the set index, and the cache line offset?**

**(3 points) How many overhead bits does this cache have? Recall that overhead includes the tag**
bits, the dirty bits (if needed), and the replacement bits (if needed). Show you work to earn full
credit.

|Access|Address|
|---|---|
|1|00110000|
|2|10100010|
|3|10011001|
|4|01011101|
|5|00110111|
|6|10011010|
|7|01011110|
|8|01101100|
|9|10100010|


-----

**(3 points) Assuming the cache is initially empty. How many cache misses will the program**
generate when it’s run for the first time?

**(3 points) How many cache misses will the program generate when it’s run for the second**
time?

**(4 points) Looking carefully at the access pattern, you realize that it is possible to design a**
cache with a smaller overhead that achieves a 100% hit rate for the program after the initial run.

Without changing the cache line size, explain the new design of your cache, i.e., its associativity
and the number of sets.

**(3 points) What is the overhead of your new cache design?**


-----

**Problem 5: Virtual Memory (30 points + 3 points extra credit)**

You are building a machine with virtual memory support. The virtual address space is 256 KB
(2^18 bytes). The physical memory size is 32KB. The system uses a one-level page table.

**Part a) Basic organization (13 points + 3 points extra credit)**
**(4 points) Assume the page size is 1KB. How many bits are used for the physical page number**
(PPN), and how many for the virtual page number (VPN)?

**(3 points) What is the size of one PTE, assuming that the only overhead in the PTE is one valid**
bit and that the disk address is 2 bits longer than the PPN.

**(3 points) You decide to experiment with changing the page size to 4KB. What is the size of one**
PTE now? Continue to assume that the only overhead in the PTE is one valid bit and that the
disk address is 2 bits longer than the PPN.

**(3 points) The system has a TLB. What is likely to happen to the TLB hit rate when we increase**
the page size to 4KB? Will it increase or decrease? Explain your answer to receive ANY credit.

**(3 points extra credit) If the machine were to use a two-level page table with a 4KB page size,**
how many PTE entries are there in the level 1 page table?


-----

**Part b) Protection (8 points)**
The major customer for your system is the US Government. They want a secure system that is
safer from buffer overflow attacks. The memory protection system should help protect against
arbitrary code execution in the event that someone manages to exploit a buffer overflow.

**(4 points) Briefly explain the mechanism by which an attacker exploits a buffer overflow. Your**
answer must cover 1) where in memory the attacker can place the code and 2) how the injected
code can be executed.

**(4 points) Now you want to augment the PTE structure with permission information to defend**
against buffer overflow attacks. In order to keep the overhead low, you decide that you will use a
maximum of 2 permission bits, which will indicate whether a page can be written to, whether a
page can be read from, and whether a page’s contents can be executed as code. Assuming
defending buffer overflow attacks is your sole goal in this design process, how will you use the 2
permission bits? Explain the semantics of each bit to receive full credit.

**Part c) Performance (9 points)**

Management decided to go with the 1KB page size for this machine and removed the TLB to cut
costs. Consider the C code below. Assume:

1. A 1-level page table translation scheme with the page table starting empty, and

2. `arr is aligned such that it starts 8 bytes before a page boundary.`
```
void func() {
   int arr[2048];
   for(int i = 0; i < 8; i++) {
       if(rand_0_1() == 1) {

```

-----

```
   printf("%d\n", arr[(i << 8) + 1]);
   printf("%d\n", arr[(i << 8) + 2]);
} else {
   printf("%d\n", arr[i]);
   printf("%d\n", arr[i + 2]);
}

```
```
   }
}
rand_0_1() is a function that returns either 0 or 1, at random.

```
For the following 3 questions, only count page faults generated by accessing elements of arr.

**(3 points) What is the maximum number of page faults that this code could possibly generate?**

**(3 points) What is the minimum number of page faults that this code could possibly generate?**

**(3 points) Suppose that the rand_0_1() function is faulty and it returns 0 40% of the time**
and 1 60% of the time. How many page faults, on average, will this code generate?


-----

###### Midterm Exam

**CSC 252**

**25 March 2021**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
**TAs: Rongcui Dong, Elana Elman, Kalen Frieberg, Sudhanshu Gupta, Yiyao (Jack) Yu, Vladimir**
###### Maksimovski, Nathan Reed, Rafaello Sanna

**Name: ____________________________________**

Problem 0 (2 points):

Problem 1 (15 points):

Problem 2 (10 points):

Problem 3 (17 points):

Problem 4 (13 points):

Problem 5 (6 points)

Problem 6 (12 points):

Total (75 points):

Extra Credit (10 points)

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
does not apply to extra credit questions.l

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 75 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (2 Points)**
Is assembly programming more fun than programming in Java?

**Problem 1: Fixed-Point Arithmetics (15 points)**
**Part a) (4 points) Represent the decimal number 92 in binary.**

1011100

**Part b) (4 points) What is the decimal representation of the base 5 number 243?**

73

**Part c) (4 points) What is the 2’s complement representation of the decimal value -92?**
Assuming an 8-bit representation. Express your answer in hexadecimal.

0xA4

**Part d) (3 points) If 4-bit registers R1 and R2 contain the values 1100 and 0111 respectively,**
what are the values of the carry, overflow, and sign flags after the operation “add R1, R2”?


-----

**Problem 2: Floating-Point Arithmetics (10 points + 4 points extra credit)**

**Part a) (4 points) Put19** [3] into the binary normalized form.

8

10011.011 => 1.0011011 * 2^4

**Part b) (6 points) The IEEE has decided to introduce a new 14-bit floating-point standard,**
whose main characteristics are consistent with existing floating-point number representations
that we discussed in the class.

17
The following is the encoding of in this 14-bit standard: 00110100010000
64

How many bits are used for the exponent? How many for the fraction?

Exponent: 5 bits, Fraction: 8 bits

**Part c) (4 points extra credit)**

The IEEE 754 floating-point standard states that a NaN is considered “quiet” if its most
significant fractional bit is 1, and “signaling” if its most significant fractional bit is 0. Some
programming languages take advantage of this feature to encode pointers. In particular, a
pointer is stored as the fractional bit of a quiet NaN. This technique is called “NaN boxing.”

NaNs used for “NaN boxing” (i.e., store pointers) always have their second most significant
fractional bit set to 1, whereas NaNs that are meant to store actual NaN values set that bit to 0.

Suppose a programming language were to use NaN boxing. The language uses the IEEE 754
32-bit floating point representation. What’s the maximum number of bits in a pointer that can
be stored in a NaN using NaN boxing?

21 bits (23 - 2 for metadata)

Suppose we wanted to store a pointer value 0xF3CB in a 32-bit NaN. Write the binary encoding
of this NaN value. Pad any bits that are irrelevant to this problem with zeros.


-----

**Problem 3: Logic Design (17 points)**

**Part a) (6 points)**

**(3 points) What is the result of a bit-wise XOR between 0101 and 1001?**

1100

**(3 points) What is the result of a bit-wise NOR between 0101 and 1001?**

0010

**Part b) (6 points)**

A two-input MUX selects between the two inputs (In0 and In1) according to the select signal S.
The diagram and truth table of a 2-input MUX are shown below. A MUX gate simply sets its
output OUT to In0 if S is 0 and sets OUT to In1 if S is 1.

We can construct other basic logic gates using only MUXes. For instance, we can construct a
2-input OR gate that computes A OR B using a two-input MUX by setting its inputs as follows:

  - `In0 = B`

  - `In1 = constant value of 1`

  - `S = A`

This will give us A OR B at OUT.

**(3 points) Construct a NOT gate that computes !A using only one two-input MUX. A is the**
input signal to the NOT gate. Specify what In0, In1, and S should be in this MUX.


-----

```
In0 is:

```
1
```
In1 is:

```
0
```
S is:

```
A

**(3 points) Construct a two-input AND gate that computes A AND B using only one two-input**
MUX. A and B are the input signals to the AND gate. Specify what In0, In1, and S should be in
this MUX.
```
In0 is:

```
0
```
In1 is:

```
B
```
S is:

```
A

**Part c) (5 points)**

**(3 points) The combinational circuit shown below takes in three 1-bit inputs: A, B, and C, and**
produces one 1-bit output: Out. The relationship between A, B, C, and Out is shown in the
accompanying truth table.

This circuit contains two identical but unknown gates X. What is gate X so that the circuit
matches the given truth table?


-----

X is:

OR

**(2 points) Assuming the delay of each gate is 1ps, what is the delay of the entire circuit?**


-----

**Problem 4: Assembly Programming I (13 points)**

**Conventions:**

1. For this section, the assembly shown uses the syntax opcode src, dst for
instructions with two arguments where src is the source argument and dst is the
destination argument. For example, this means that mov a, b moves the value a into b
and sub a, b computes the value (b - a) and stores it in b. All C code is compiled on a
64-bit machine, where arrays grow towards higher addresses.

2. Also, for functions that take two arguments, the first argument is stored in %rdi and the
second is stored in %rsi at the time the function is called. The return value of this
function is stored in %eax at the time the function returns.

Consider the following code:
```
typedef struct {
   char netid[12];
   char *name;
   int sid;
   double gpa;
} Student;
void print_ten_students() {
 Student[10] students;
 print_gpa(students[0].gpa);
 print_netid(students[3].netid);
 print_studentid(students[3].sid);
}

```
Assume that the beginning address of students is stored in %rbx. Also assume that the
compiler doesn’t reorder struct fields.

**(10 points) The following table contains source code lines from print_ten_students()**
and the corresponding assembly snippets. The letters A, B, C, D, and E represent blanks in the
assembly code. Fill in the blanks with appropriate instructions or hexadecimal offsets so that the
function call succeeds.


-----

|C function|Assembly (Fill in the blanks)|
|---|---|
|print_gpa(students[0].gpa);|movq A (%rbx),%rdi callq 40118e <print_gpa>|
|print_netid(students[3].netid);|B (%rbx,0x3, C ),%rdi callq 401136 <print_netid>|
|print_studentid(students[3].sid);|lea (%rbx,0x3, D ),%rdi movq E (%rdi),%edi callq 40116c <print_studentid>|


**A:**

0x20

**B:**

lea

**C:**

0x28

**D:**

0x28

**E:**

0x18

**(3 points) How to reorder fields in the struct to be more space efficient? Explain your answer.**


-----

**Problem 5: Assembly Programming II (6 points + 2 points extra credit)**

The assembly code of a function is shown below, along with the relevant part of the memory. For
**all questions in this part, assume %rdi = 0x7ffffffee3f0 at the beginning of the code.**

The jns label is a jump instruction that jumps to label if and only if the sign bit is set to 0.
**The same assembly programming conventions in the previous problem still apply.**

###### Assembly Code Data (memory position: 8-byte value)
```
.L2: 0x7ffffffee3f0: 0x000000000000000c
   testq   %rdi, %rdi 0x7ffffffee3f8: 0x00007ffffffee408
   je     .L6 0x7ffffffee400: 0x0000000000000000
   cmpq    %rsi, (%rdi) 0x7ffffffee408: 0xfffffffffffffff9
   jns    .L4 0x7ffffffee410: 0x00007ffffffee438
   movq    0x10(%rdi), 0x7ffffffee418: 0x00007ffffffee420
%rdi 0x7ffffffee420: 0x0000000000000000
   jmp    .L2 0x7ffffffee428: 0x0000000000000000
.L4: 0x7ffffffee430: 0x0000000000000000
   je     .L7 0x7ffffffee438: 0xfffffffffffffff4
   movq    0x8(%rdi), %rdi 0x7ffffffee440: 0x0000000000000000
   jmp    .L2 0x7ffffffee448: 0x00007ffffffee3f0
.L6:
   xorl    %eax, %eax
   ret
.L7:
   movl    $0x1, %eax
   ret

```
**(2 points) When the function is called with argument %rsi = 0, does the program terminate?**
If so, what is the value stored in %eax after the function returns?

Yes, it terminates. Register %eax will be set to 1.

**(2 points) For what values of %rsi does this procedure run into an infinite loop? Include the**
previous question’s %rsi, if you found the program not to terminate under that %rsi. Write all
```
%rsi values in decimal, and in increasing order.

```
|Assembly Code|Data (memory position: 8-byte value)|
|---|---|
|.L2: testq %rdi, %rdi je .L6 cmpq %rsi, (%rdi) jns .L4 movq 0x10(%rdi), %rdi jmp .L2 .L4: je .L7 movq 0x8(%rdi), %rdi jmp .L2 .L6: xorl %eax, %eax ret .L7: movl $0x1, %eax ret|0x7ffffffee3f0: 0x000000000000000c 0x7ffffffee3f8: 0x00007ffffffee408 0x7ffffffee400: 0x0000000000000000 0x7ffffffee408: 0xfffffffffffffff9 0x7ffffffee410: 0x00007ffffffee438 0x7ffffffee418: 0x00007ffffffee420 0x7ffffffee420: 0x0000000000000000 0x7ffffffee428: 0x0000000000000000 0x7ffffffee430: 0x0000000000000000 0x7ffffffee438: 0xfffffffffffffff4 0x7ffffffee440: 0x0000000000000000 0x7ffffffee448: 0x00007ffffffee3f0|


-----

**(2 points) How would you fix all infinite loop cases by modifying exactly one 8-byte value in**
memory (must be aligned)? You can modify that 8-byte data to whatever you want. The function
output should stay the same for %rsi values for which the function was working correctly. In
other words, for all %rsi, if the function returned before the modification, the function should
return the same value before and after the modification.
```
0x7ffffffee448 = 0x0

```
**(2 points extra credit) What kind of data structure does this function most likely**
manipulate? Be specific: answering “array” gets no points.


-----

**Problem 6: ISA + Microarchitecture (12 points + 4 points extra credit)**

**Part a) (12 points)**
Consider the following x86 assembly code fragment:
```
mov $0x02, %rax
nop
nop
.L1:
cmpq %rax, $0x01
jle .L2
sub $0x01, %rax
nop
nop
cmpq %rax, $0x01
jge .L1
.L2:
xchg %rdi, %rdi
add $0x99, %rsi
mov %rsi, %rax
ret

```
**(3 points) How many cycles does it take to execute this code on a single-cycle, sequential**
machine?

16

We will now execute the program on two CPUs that are pipelined differently. Assume that both
CPUs have a simple 1-bit branch predictor and that the branch predictor is initialized to predict
“taken”. The 1-bit branch predictor works by storing a single bit somewhere in the CPU. All the
jumps in the program (no matter where they occur) are predicted by this one single bit.

The first CPU has a 5-stage pipeline similar to the one discussed in class with (F)etch, (D)ecode,
(E)xecute, (M)emory, and (W)riteback stages. With this CPU, the jump outcome, i.e., whether
the jump will be taken or not, is not known until the jump instruction itself finishes the E stage.

The second CPU has a 3-stage pipeline with Fetch (F), Decode (D), and Memory/Execute (MX)
stages. With this CPU, the jump outcome is not known until the jump instruction completes the
D stage.


-----

Hints:

  - Recall how a 1-bit branch predictor works: it simply stores whether the last jump was
taken or not taken and uses that information to predict whether a future jump will be
taken or not taken (e.g., if the last jump was taken, we predict that a future jump will be
taken). It is updated as soon as we know if a jump will actually be taken or not.

  - If a jump is mispredicted, the correct next instruction will enter Fetch in the cycle after
the jump outcome is known.

  - A CPU, with branch prediction, will always fetch the next instruction (that the CPU
predicts to be the correct next instruction) the cycle after it fetches the jump instruction.

**(3 points) During the execution of the code fragment, how many instructions get fetched as a**
result of a misprediction for the 5-stage pipeline? How many get fetched as a result of
misprediction for the 3-stage pipeline?

5-stage: 4, 3-stage: 2

**(3 points) How many cycles does each CPU lose/waste every time it mispredicts?**

5-stage: 2, 3-stage: 1

**(3 points) Assume the first CPU is running at 1GHz (cycle time 1 ns) and the second CPU is**
running at 600MHz (cycle time 1.6666... ns). Which CPU executes the code fragment faster (in
less time, from fetching the first instruction to finishing the last instruction)? Explain.


-----

**Part b) (4 points extra credit)**

Consider a 3-stage pipeline with Fetch (F), Decode (D), and Memory/Execute (MX) stages. The
diagram is given below.

The three stages take 100 ps, 82.5 ps, and 476 ps, respectively. The fastest clock frequency this
pipeline is capable of is 2.0 GHz. How long must it take to latch data into each of the 3
intermediate pipeline registers? Answer in picoseconds. A picosecond (ps) is 10[-12] second.


-----

###### Midterm Exam

**CSC 252**

**25 March 2021**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
**TAs: Rongcui Dong, Elana Elman, Kalen Frieberg, Sudhanshu Gupta, Yiyao (Jack) Yu, Vladimir**
Maksimovski, Nathan Reed, Rafaello Sanna

**Name: ____________________________________**

Problem 0 (2 points):

Problem 1 (15 points):

Problem 2 (10 points):

Problem 3 (17 points):

Problem 4 (13 points):

Problem 5 (6 points)

Problem 6 (12 points):

Total (75 points):

Extra Credit (10 points)

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 75 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (2 Points)**
Is assembly programming more fun than programming in Java?

**Problem 1: Fixed-Point Arithmetics (15 points)**
**Part a) (4 points) Represent the decimal number 92 in binary.**

**Part b) (4 points) What is the decimal representation of the base 5 number 243?**

**Part c) (4 points) What is the 2’s complement representation of the decimal value -92?**
Assuming an 8-bit representation. Express your answer in hexadecimal.

**Part d) (3 points) If 4-bit registers R1 and R2 contain the values 1100 and 0111 respectively,**
what are the values of the carry, overflow, and sign flags after the operation “add R1, R2”?


-----

**Problem 2: Floating-Point Arithmetics (10 points + 4 points extra credit)**

**Part a) (4 points) Put19** [3] into the binary normalized form.

8

**Part b) (6 points) The IEEE has decided to introduce a new 14-bit floating-point standard,**
whose main characteristics are consistent with existing floating-point number representations
that we discussed in the class.

17
The following is the encoding of in this 14-bit standard: 00110100010000
64

How many bits are used for the exponent? How many for the fraction?

**Part c) (4 points extra credit)**

The IEEE 754 floating-point standard states that a NaN is considered “quiet” if its most
significant fractional bit is 1, and “signaling” if its most significant fractional bit is 0. Some
programming languages take advantage of this feature to encode pointers. In particular, a
pointer is stored as the fractional bit of a quiet NaN. This technique is called “NaN boxing.”

NaNs used for “NaN boxing” (i.e., store pointers) always have their second most significant
fractional bit set to 1, whereas NaNs that are meant to store actual NaN values set that bit to 0.

Suppose a programming language were to use NaN boxing. The language uses the IEEE 754
32-bit floating point representation. What’s the maximum number of bits in a pointer that can
be stored in a NaN using NaN boxing?

Suppose we wanted to store a pointer value 0xF3CB in a 32-bit NaN. Write the binary encoding
of this NaN value. Pad any bits that are irrelevant to this problem with zeros.


-----

**Problem 3: Logic Design (17 points)**

**Part a) (6 points)**

**(3 points) What is the result of a bit-wise XOR between 0101 and 1001?**

**(3 points) What is the result of a bit-wise NOR between 0101 and 1001?**

**Part b) (6 points)**

A two-input MUX selects between the two inputs (In0 and In1) according to the select signal S.
The diagram and truth table of a 2-input MUX are shown below. A MUX gate simply sets its
output OUT to In0 if S is 0 and sets OUT to In1 if S is 1.

We can construct other basic logic gates using only MUXes. For instance, we can construct a
2-input OR gate that computes A OR B using a two-input MUX by setting its inputs as follows:

  - `In0 = B`

  - `In1 = constant value of 1`

  - `S = A`

This will give us A OR B at OUT.

**(3 points) Construct a NOT gate that computes !A using only one two-input MUX. A is the**
input signal to the NOT gate. Specify what In0, In1, and S should be in this MUX.


-----

```
In0 is:
In1 is:
S is:

```
**(3 points) Construct a two-input AND gate that computes A AND B using only one two-input**
MUX. A and B are the input signals to the AND gate. Specify what In0, In1, and S should be in
this MUX.
```
In0 is:
In1 is:
S is:

```
**Part c) (5 points)**

**(3 points) The combinational circuit shown below takes in three 1-bit inputs: A, B, and C, and**
produces one 1-bit output: Out. The relationship between A, B, C, and Out is shown in the
accompanying truth table.

This circuit contains two identical but unknown gates X. What is gate X so that the circuit
matches the given truth table?


-----

X is:

**(2 points) Assuming the delay of each gate is 1ps, what is the delay of the entire circuit?**


-----

**Problem 4: Assembly Programming I (13 points)**

**Conventions:**

1. For this section, the assembly shown uses the syntax opcode src, dst for
instructions with two arguments where src is the source argument and dst is the
destination argument. For example, this means that mov a, b moves the value a into b
and sub a, b computes the value (b - a) and stores it in b. All C code is compiled on a
64-bit machine, where arrays grow towards higher addresses.

2. Also, for functions that take two arguments, the first argument is stored in %rdi and the
second is stored in %rsi at the time the function is called. The return value of this
function is stored in %eax at the time the function returns.

Consider the following code:
```
typedef struct {
   char netid[12];
   char *name;
   int sid;
   double gpa;
} Student;
void print_ten_students() {
 Student[10] students;
 print_gpa(students[0].gpa);
 print_name(students[3].name);
 print_studentid(students[3].sid);
}

```
Assume that the beginning address of students is stored in %rbx. Also assume that the
compiler doesn’t reorder struct fields.

**(10 points) The following table contains source code lines from print_ten_students()**
and the corresponding assembly snippets. The letters A, B, C, D, and E represent blanks in the
assembly code. Fill in the blanks with appropriate instructions or hexadecimal offsets so that the
function call succeeds.


-----

|C function|Assembly (Fill in the blanks)|
|---|---|
|print_gpa(students[0].gpa);|movq A (%rbx),%rdi callq 40118e <print_gpa>|
|print_netid(students[3].netid);|B (%rbx,0x3, C ),%rdi callq 401136 <print_netid>|
|print_studentid(students[3].sid);|lea (%rbx,0x3, D ),%rdi movq E (%rdi),%edi callq 40116c <print_studentid>|


**A:**

**B:**

**C:**

**D:**

**E:**

**(3 points) How to reorder fields in the struct to be more space efficient? Explain your answer.**


-----

**Problem 5: Assembly Programming II (6 points + 2 points extra credit)**

The assembly code of a function is shown below, along with the relevant part of the memory. For
**all questions in this part, assume %rdi = 0x7ffffffee3f0 at the beginning of the code.**

The jns label is a jump instruction that jumps to label if and only if the sign bit is set to 0.
**The same assembly programming conventions in the previous problem still apply.**

###### Assembly Code Data (memory position: 8-byte value)
```
.L2: 0x7ffffffee3f0: 0x000000000000000c
   testq   %rdi, %rdi 0x7ffffffee3f8: 0x00007ffffffee408
   je     .L6 0x7ffffffee400: 0x0000000000000000
   cmpq    %rsi, (%rdi) 0x7ffffffee408: 0xfffffffffffffff9
   jns    .L4 0x7ffffffee410: 0x00007ffffffee438
   movq    0x10(%rdi), 0x7ffffffee418: 0x00007ffffffee420
%rdi 0x7ffffffee420: 0x0000000000000000
   jmp    .L2 0x7ffffffee428: 0x0000000000000000
.L4: 0x7ffffffee430: 0x0000000000000000
   je     .L7 0x7ffffffee438: 0xfffffffffffffff4
   movq    0x8(%rdi), %rdi 0x7ffffffee440: 0x0000000000000000
   jmp    .L2 0x7ffffffee448: 0x00007ffffffee3f0
.L6:
   xorl    %eax, %eax
   ret
.L7:
   movl    $0x1, %eax
   ret

```
**(2 points) When the function is called with argument %rsi = 0, does the program terminate?**
If so, what is the value stored in %eax after the function returns?

**(2 points) For what values of %rsi does this procedure run into an infinite loop? Include the**
previous question’s %rsi, if you found the program not to terminate under that %rsi. Write all
```
%rsi values in decimal, and in increasing order.

```
|Assembly Code|Data (memory position: 8-byte value)|
|---|---|
|.L2: testq %rdi, %rdi je .L6 cmpq %rsi, (%rdi) jns .L4 movq 0x10(%rdi), %rdi jmp .L2 .L4: je .L7 movq 0x8(%rdi), %rdi jmp .L2 .L6: xorl %eax, %eax ret .L7: movl $0x1, %eax ret|0x7ffffffee3f0: 0x000000000000000c 0x7ffffffee3f8: 0x00007ffffffee408 0x7ffffffee400: 0x0000000000000000 0x7ffffffee408: 0xfffffffffffffff9 0x7ffffffee410: 0x00007ffffffee438 0x7ffffffee418: 0x00007ffffffee420 0x7ffffffee420: 0x0000000000000000 0x7ffffffee428: 0x0000000000000000 0x7ffffffee430: 0x0000000000000000 0x7ffffffee438: 0xfffffffffffffff4 0x7ffffffee440: 0x0000000000000000 0x7ffffffee448: 0x00007ffffffee3f0|


-----

**(2 points) How would you fix all infinite loop cases by modifying exactly one 8-byte value in**
memory (must be aligned)? You can modify that 8-byte data to whatever you want. The function
output should stay the same for %rsi values for which the function was working correctly. In
other words, for all %rsi, if the function returned before the modification, the function should
return the same value before and after the modification.

**(2 points extra credit) What kind of data structure does this function most likely**
manipulate? Be specific: answering “array” gets no points.


-----

**Problem 6: ISA + Microarchitecture (12 points + 4 points extra credit)**

**Part a) (12 points)**
Consider the following x86 assembly code fragment:
```
mov $0x02, %rax
nop
nop
.L1:
cmpq %rax, $0x01
jle .L2
sub $0x01, %rax
nop
nop
cmpq %rax, $0x01
jge .L1
.L2:
xchg %rdi, %rdi
add $0x99, %rsi
mov %rsi, %rax
ret

```
**(3 points) How many cycles does it take to execute this code on a single-cycle, sequential**
machine?

We will now execute the program on two CPUs that are pipelined differently. Assume that both
CPUs have a simple 1-bit branch predictor and that the branch predictor is initialized to predict
“taken”. The 1-bit branch predictor works by storing a single bit somewhere in the CPU. All the
jumps in the program (no matter where they occur) are predicted by this one single bit.

The first CPU has a 5-stage pipeline similar to the one discussed in class with (F)etch, (D)ecode,
(E)xecute, (M)emory, and (W)riteback stages. With this CPU, the jump outcome, i.e., whether
the jump will be taken or not, is not known until the jump instruction itself finishes the E stage.

The second CPU has a 3-stage pipeline with Fetch (F), Decode (D), and Memory/Execute (MX)
stages. With this CPU, the jump outcome is not known until the jump instruction completes the
D stage.


-----

Hints:

  - Recall how a 1-bit branch predictor works: it simply stores whether the last jump was
taken or not taken and uses that information to predict whether a future jump will be
taken or not taken (e.g., if the last jump was taken, we predict that a future jump will be
taken). It is updated as soon as we know if a jump will actually be taken or not.

  - If a jump is mispredicted, the correct next instruction will enter Fetch in the cycle after
the jump outcome is known.

  - A CPU, with branch prediction, will always fetch the next instruction (that the CPU
predicts to be the correct next instruction) the cycle after it fetches the jump instruction.

**(3 points) During the execution of the code fragment, how many instructions get fetched as a**
result of a misprediction for the 5-stage pipeline? How many get fetched as a result of
misprediction for the 3-stage pipeline?

**(3 points) How many cycles does each CPU lose/waste every time it mispredicts?**

**(3 points) Assume the first CPU is running at 1GHz (cycle time 1 ns) and the second CPU is**
running at 600MHz (cycle time 1.6666... ns). Which CPU executes the code fragment faster (in
less time, from fetching the first instruction to finishing the last instruction)? Explain.


-----

**Part b) (4 points extra credit)**

Consider a 3-stage pipeline with Fetch (F), Decode (D), and Memory/Execute (MX) stages. The
diagram is given below.

The three stages take 100 ps, 82.5 ps, and 476 ps, respectively. The fastest clock frequency this
pipeline is capable of is 2.0 GHz. How long must it take to latch data into each of the 3
intermediate pipeline registers? Answer in picoseconds. A picosecond (ps) is 10[-12] second.


-----

###### Final Exam

**CSC 252**

**6 May 2020**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
​
**TAs: Daniel Busaba, Sudhanshu Gupta, Mandar Juvekar, Max Kimmelman, Weituo Kong,**
​
Jiahao Lu, Vladimir Maksimovski, Nathan Reed, Yawo Alphonse Siatitse, Yudi Yang, Shuang
Zhai, Prikshet Sharma

**Name: ____________________________________**
​ ​

Problem 0 (2 points):

Problem 1 (28 points):

Problem 2 (20 points):

Problem 3 (28 points):

Problem 4 (24 points):

Total (100 points):

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
​ ​
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 3 hours to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**

**Have a great summer break!**


-----

**Problem 0: Warm-up (2 Points) What’s your favourite register?**
​

Any register is accepted.

**Problem 1: Miscellaneous (26 points)**

**Part a)​** **(6 points)​** What is the result of adding the value 11​ 2​ to the value 0x40? Express your ​
answer in octal (base 8).

103

**Part b) (8 points) Consider the following assembly program. The value 5 is contained in ​** `rcx​`
and the value 2 is contained in rdx​ when execution starts. ​
```
       add rcx, rdx
       mov 3, r11
   .L1: dec rcx
       mov r8, r9
       cmp 0,1
       beq 0x584fc0
       inc r11
   .L2: cmp rcx, 0
       jne .L1
   .L3: add r8, r9

```
**(4 points) What is the value stored in ​** `r11​` when ​ `.L3​` is reached? ​

10

**(4 points) What is an instruction that could be substituted in at ​** `.L2​` without changing the ​
functionality of the program?

“test rcx”, “and rcx, rcx”, others


-----

**Part c) (4 points) Give code for a C function that takes one integer as input and returns that**
​
integer multiplied by 5. You may not use the * operator and you may not use a loop of any kind.
You may use at most three operators.
```
int mul5(int num) {
  return (num << 2) + num;
}

```
**Part d) (4 points) Give two reasons the pipeline may stall during execution.**
​

Data dependency, control dependency, cache miss, etc.

**Part e) (4 points) Consider the following C program. Assume that it executes on a CSUG**
​
machine. Reminder: the “gets​ ” function reads a string, ending with a newline, from standard ​
input into the given buffer (it will read until it sees a newline). Assume that you (the user who is
giving input to the program) can figure out the address of every function in memory (e.g., from
disassembly/debugger).


-----

Which of the following is a possible output of this program? Select ALL correct answers (there
may be multiple).

**A**
hello from function 2
What is the airspeed velocity of an unladen swallow?

**B**
hello from function 1
What is the airspeed velocity of an unladen swallow?
hello from function 2

**C**
hello from function 2
What is the airspeed velocity of an unladen swallow?
this is a neat function

**D**
hello from function 2
What is the airspeed velocity of an unladen swallow?
hello from function 1
this is a neat function

**E**
hello from function 2
What is the airspeed velocity of an unladen swallow?
<program crashes after user input>

A, C, D, E


-----

**Problem 2: Floating-Point Arithmetic (20 points)**

**Part a) (4 points) Express 4 ⅜ in binary normalized form.**
​

1.00011 * 2^2

**Part b) (16 points) A new IEEE-consistent floating-point representation is being developed**
​
which uses 8 bits. Given below are the binary representations of 4 floating-point numbers in this
representation.
```
     A. 1111 1011
     B. 0010 0100
     C. 0011 0001
     D. 1011 0001

```
Below are 2 floating-point numbers that are the sum of some pairs of the numbers above:
```
     1. 0000 0000
     2. 0011 0100

```
**(4 points) Which 2 numbers in A, B, C, and D generate the sum 2 above ? (You can do this**
​
without calculating anything) (Choose two from A, B, C, or D)

B and C

**(4 points) How many exponent bits are used?**
​

4

**(4 points) How many fraction bits are used?**
​

3

**(4 points) What is the bias?**
​

7


-----

**Problem 3: Cache (28 points)**

You have been asked to design a byte-addressable, 4-way associative cache (meaning that each
set in the cache can hold 4 cache lines). You have decided that since it is complicated to
implement a Least Recently Used (LRU) policy for a set of 4 cache lines, you will use another
replacement policy.

The policy you chose to use instead is a variant of a replacement policy called Not Most Recently
Used (NMRU). This policy guarantees that the most recently used cache line in each set will not
​
be replaced, and instead, some other cache line is selected for replacement.

The way you will implement this policy is by assigning an index to each line in the set (either 0,
1, 2, or 3), and keeping track of the index of the most recently used cache line in each set with
MRU bits that are cache overhead (the only overhead in the cache will be valid, tag, and MRU
bits). If the cache set is not full, new cache lines will be placed in the set at the lowest free index.
If the cache set is full, the table below indicates the replacement policy.

Index of most recently used cache line 0 1 2 3

Index of cache line that will be replaced next 3 0 1 2

You took notes of all the rest of the specifications of your cache on a whiteboard, but you
accidentally left it next to an open window when it rained, and some of your notes washed away.
Here are your remaining notes:

  - the size of each cache line is 4 bytes

  - the number of overhead bits required for each cache set is 26

  - the cache will hold a total of 512 cache lines.

**Part a) (4 points) How many bits per set are needed to implement the NMRU policy?**
​

2

**Part b) (4 points) How many bits are needed for a tag?**
​

5

|Index of most recently used cache line|0|1|2|3|
|---|---|---|---|---|
|Index of cache line that will be replaced next|3|0|1|2|


-----

**Part c) (4 points) What is the total physical memory on the machine that you are designing**
​
this cache for?

16 KB

**Part d) (16 points) Now we want to compare memory access behavior under two different**
​
policies: NMRU and LRU. Assume that both of them have the same cache configuration as
previous questions. The only difference is the replacement policy. Given the following sequence
of memory accesses, please indicate whether a particular memory access will result in a cache hit
or miss (Please fill in Hit or Miss).
​ ​ ​ ​ ​ ​

Assume that the cache is initially empty. The hit/miss behaviors of the first seven accesses under
both replacement policies are given.

|Address|NMRU|LRU|
|---|---|---|
|0000 1010 0100 1001|Miss|Miss|
|0001 1000 0110 0100|Miss|Miss|
|0001 0010 0100 1010|Miss|Miss|
|0000 1100 0100 1001|Miss|Miss|
|0001 0010 0110 0111|Miss|Miss|
|0000 1010 0110 0101|Miss|Miss|
|0001 1000 0100 1010|Miss|Miss|
|0001 1110 0100 1011|Miss|Miss|
|0000 1010 0100 1011|Hit|Miss|
|0000 1100 0100 1000|Miss|Hit|
|0001 1000 0100 1011|Miss|Hit|


-----

**Problem 4: Virtual Memory (24 points)**

Assume a system which has the following characteristics:

1. Virtual address space is 64 KB and is byte addressable

2. Physical RAM is 16 KB and is byte addressable

3. Page size is 256 Byte

4. One level page table, where each page table entry contains a valid bit, a dirty bit, and the
physical page number

5. Integer is 32 bits

6. PTBR is 0x2F5C ​

7. There is a data TLB that stores two page table entries

**Part a) (4 points) What is the size of each page table entry?**
​

6 (PPN) + 1 (valid) + 1 (dirty) = 8 bits

**Part b) (4 points) What would be the size of the page table?**
​

256 * 8 bits = 256 bytes

**Part c) (4 points) Does the system use a write-through policy or a write-back policy for writes**
​
to pages?

Write back

**Part d) (12 points) Consider the following C program:**
​
```
void square(int a[16][16]) {
 for (int j=0; j < 16; j++) {
  for (int i=0; i < 16; i++) {
   a[i][j] = a[i][j] * a[i][j];
  }
 }
}

```

-----

Suppose that the virtual address of matrix ‘a​ ’ is ​ `0x0300​` . Assume the data TLB is empty when ​
the code starts execution. Assume the following layout for each page table entry:

Valid bit Dirty bit Physical page number

The table below shows a part of the main memory before the code executes.

**Address** **Data**
```
       2F5B 8B
       2F5C 8C
       2F5D CD
       2F5E 8E
       2F5F CF
       2F60 C0

```
**(4 points) To read the data in ​** `a[3][10]​`, what physical memory addresses are accessed by the ​
program?

1. PTBR + VPN = 2F5F

2. 0F00 + ((16 * 3) + 10) * 4 = 0FE8

**(4 points) How many data TLB misses does executing ​** `square()​` incur? ​

64

**(4 points) How can you improve the program to have fewer TLB misses? Write both the**
​
technique and the new number of misses.

Switch the loop order. New misses = 4

|Valid bit|Dirty bit|Physical page number|
|---|---|---|

|Address|Data|
|---|---|
|2F5B|8B|
|2F5C|8C|
|2F5D|CD|
|2F5E|8E|
|2F5F|CF|
|2F60|C0|


-----

###### Final Exam

**CSC 252**

**6 May 2020**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
​
**TAs: Daniel Busaba, Sudhanshu Gupta, Mandar Juvekar, Max Kimmelman, Weituo Kong,**
​
Jiahao Lu, Vladimir Maksimovski, Nathan Reed, Yawo Alphonse Siatitse, Yudi Yang, Shuang
Zhai, Prikshet Sharma

**Name: ____________________________________**
​ ​

Problem 0 (2 points):

Problem 1 (28 points):

Problem 2 (20 points):

Problem 3 (28 points):

Problem 4 (24 points):

Total (100 points):

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
​ ​
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 3 hours to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**

**Have a great summer break!**


-----

**Problem 0: Warm-up (2 Points) What’s your favourite register?**
​

**Problem 1: Miscellaneous (26 points)**

**Part a)​** **(6 points)​** What is the result of adding the value 11​ 2​ to the value 0x40? Express your ​
answer in octal (base 8).

**Part b) (8 points) Consider the following assembly program. The value 5 is contained in ​** `rcx​`
and the value 2 is contained in rdx​ when execution starts. ​
```
       add rcx, rdx
       mov r11, 3
   .L1: dec rcx
       mov r8, r9
       cmp 0,1
       beq 0x584fc0
       inc r11
   .L2: cmp rcx, 0
       jne .L1
   .L3: add r8, r9

```
**(4 points) What is the value stored in ​** `r11​` when ​ `.L3​` is reached? ​

**(4 points) What is an instruction that could be substituted in at ​** `.L2​` without changing the ​
functionality of the program?


-----

**Part c) (4 points) Give code for a C function that takes one integer as input and returns that**
​
integer multiplied by 5. You may not use the * operator and you may not use a loop of any kind.
You may use at most three operators.

**Part d) (4 points) Give two reasons the pipeline may stall during execution.**
​

**Part e) (4 points) Consider the following C program. Assume that it executes on a CSUG**
​
machine. Reminder: the “gets​ ” function reads a string, ending with a newline, from standard ​
input into the given buffer (it will read until it sees a newline). Assume that you (the user who is
giving input to the program) can figure out the address of every function in memory (e.g., from
disassembly/debugger).


-----

Which of the following is a possible output of this program? Select ALL correct answers (there
may be multiple).

**A**
hello from function 2
What is the airspeed velocity of an unladen swallow?

**B**
hello from function 1
What is the airspeed velocity of an unladen swallow?
hello from function 2

**C**
hello from function 2
What is the airspeed velocity of an unladen swallow?
this is a neat function

**D**
hello from function 2
What is the airspeed velocity of an unladen swallow?
hello from function 1
this is a neat function

**E**
hello from function 2
What is the airspeed velocity of an unladen swallow?
<program crashes after user input>


-----

**Problem 2: Floating-Point Arithmetic (20 points)**

**Part a) (4 points) Express 4 ⅜ in binary normalized form.**
​

**Part b) (16 points) A new IEEE-consistent floating-point representation is being developed**
​
which uses 8 bits. Given below are the binary representations of 4 floating-point numbers in this
representation.
```
     A. 1111 1011 
     B. 0010 0100
     C. 0011 0001
     D. 1011 0001

```
Below are 2 floating-point numbers that are the sum of some pairs of the numbers above:
```
     1. 0000 0000
     2. 0011 0100

```
**(4 points) Which 2 numbers in A, B, C, and D generate the sum 2 above ? (You can do this**
​
without calculating anything) (Choose two from A, B, C, or D)

**(4 points) How many exponent bits are used?**
​

**(4 points) How many fraction bits are used?**
​

**(4 points) What is the bias?**
​


-----

**Problem 3: Cache (28 points)**

You have been asked to design a byte-addressable, 4-way associative cache (meaning that each
set in the cache can hold 4 cache lines). You have decided that since it is complicated to
implement a Least Recently Used (LRU) policy for a set of 4 cache lines, you will use another
replacement policy.

The policy you chose to use instead is a variant of a replacement policy called Not Most Recently
Used (NMRU). This policy guarantees that the most recently used cache line in each set will not
​
be replaced, and instead, some other cache line is selected for replacement.

The way you will implement this policy is by assigning an index to each line in the set (either 0,
1, 2, or 3), and keeping track of the index of the most recently used cache line in each set with
MRU bits that are cache overhead (the only overhead in the cache will be valid, tag, and MRU
bits). If the cache set is not full, new cache lines will be placed in the set at the lowest free index.
If the cache set is full, the table below indicates the replacement policy.

Index of most recently used cache line 0 1 2 3

Index of cache line that will be replaced next 3 0 1 2

You took notes of all the rest of the specifications of your cache on a whiteboard, but you
accidentally left it next to an open window when it rained, and some of your notes washed away.
Here are your remaining notes:

  - the size of each cache line is 4 bytes

  - the number of overhead bits required for each cache set is 26

  - the cache will hold a total of 512 cache lines.

**Part a) (4 points) How many bits per set are needed to implement the NMRU policy?**
​

**Part b) (4 points) How many bits are needed for a tag?**
​

|Index of most recently used cache line|0|1|2|3|
|---|---|---|---|---|
|Index of cache line that will be replaced next|3|0|1|2|


-----

**Part c) (4 points) What is the total physical memory on the machine that you are designing**
​
this cache for?

**Part d) (16 points) Now we want to compare memory access behavior under two different**
​
policies: NMRU and LRU. Assume that both of them have the same cache configuration as
previous questions. The only difference is the replacement policy. Given the following sequence
of memory accesses, please indicate whether a particular memory access will result in a cache hit
or miss (Please fill in Hit or Miss).
​ ​ ​ ​ ​ ​

Assume that the cache is initially empty. The hit/miss behaviors of the first seven accesses under
both replacement policies are given.

|Address|NMRU|LRU|
|---|---|---|
|0000 1010 0100 1001|Miss|Miss|
|0001 1000 0110 0100|Miss|Miss|
|0001 0010 0100 1010|Miss|Miss|
|0000 1100 0100 1001|Miss|Miss|
|0001 0010 0110 0111|Miss|Miss|
|0000 1010 0110 0101|Miss|Miss|
|0001 1000 0100 1010|Miss|Miss|
|0001 1110 0100 1011|||
|0000 1010 0100 1011|||
|0000 1100 0100 1000|||
|0001 1000 0100 1011|||


-----

**Problem 4: Virtual Memory (24 points)**

Assume a system which has the following characteristics:

1. Virtual address space is 64 KB and is byte addressable

2. Physical RAM is 16 KB and is byte addressable

3. Page size is 256 Byte

4. One level page table, where each page table entry contains a valid bit, a dirty bit, and the
physical page number

5. Integer is 32 bits

6. PTBR is 0x2F5C ​

7. There is a data TLB that stores two page table entries

**Part a) (4 points) What is the size of each page table entry?**
​

**Part b) (4 points) What would be the size of the page table?**
​

**Part c) (4 points) Does the system use a write-through policy or a write-back policy for writes**
​
to pages?

**Part d) (12 points) Consider the following C program:**
​
```
void square(int a[16][16]) {
 for (int j=0; j < 16; j++) {
  for (int i=0; i < 16; i++) {
   a[i][j] = a[i][j] * a[i][j];
  }
 }
}

```

-----

Suppose that the virtual address of matrix ‘a​ ’ is ​ `0x0300​` . Assume the data TLB is empty when ​
the code starts execution. Assume the following layout for each page table entry:

Valid bit Dirty bit Physical page number

The table below shows a part of the main memory before the code executes.

**Address** **Data**
```
       2F5B 8B
       2F5C 8C
       2F5D CD
       2F5E 8E
       2F5F CF
       2F60 C0

```
**(4 points) To read the data in ​** `a[3][10]​`, what physical memory addresses are accessed by the ​
program?

**(4 points) How many data TLB misses does executing ​** `square()​` incur? ​

**(4 points) How can you improve the program to have fewer TLB misses? Write both the**
​
technique and the new number of misses.

|Valid bit|Dirty bit|Physical page number|
|---|---|---|

|Address|Data|
|---|---|
|2F5B|8B|
|2F5C|8C|
|2F5D|CD|
|2F5E|8E|
|2F5F|CF|
|2F60|C0|


-----

###### Midterm Exam

**CSC 252**

**5 March 2020**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
​
**TAs: Daniel Busaba, Sudhanshu Gupta, Mandar Juvekar, Max Kimmelman, Weituo Kong,**
​
Jiahao Lu, Vladimir Maksimovski, Nathan Reed, Yawo Alphonse Siatitse, Yudi Yang, Shuang
Zhai, Prikshet Sharma

**Name: ____________________________________**
​ ​

Problem 0 (2 points):

Problem 1 (13 points):

Problem 2 (14 points):

Problem 3 (11 points):

Problem 4 (24 points):

Problem 5 (11 points):

Total (75 points):

Extra Credit (20 points)

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
​ ​
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 75 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (2 Points) What’s your favourite instruction?**
​

Any instruction here works.

**Problem 1: Fixed-Point Arithmetics (13 points)**
**Part a) (3 points) Represent the decimal number 683 in hexadecimal.**
​

2AB

**Part b) (3 points) Represent the binary value 10000111 in the base-6 number system.**
​

343

**Part c) (3 points) Represent the binary value 1101.101 in decimal.**
​

13.625

**Part d) (4 points) Is it possible to add two registers and set Carry Flag to 1, Zero Flag to 0,**
​
Signed Flag to 1, and Overflow Flag to 1? If yes, show an example; otherwise, explain.

It is not possible. If both overflow and signed flags are set, it means we added two positive
numbers and got a negative result. Adding two positive numbers cannot generate a carry,
so carry flag can’t be set.


-----

**Problem 2: Floating-Point Arithmetics (14 points + 4 points extra credit)**

19

**Part a) (4 points) Put​** 7 64 in the binary normalized form.

1.11010011 x (2^2)

**Part b) (4 points) According to the IEEE754 single-precision format, which of the following is**
​
NaN?
```
  A. 0111 1111 1100 1010 0100 1001 0001 0010
  B. 1111 1111 0100 1010 0100 1001 0001 0010
  C. 0000 0000 0000 0000 0000 0000 0000 0000
  D. 0111 1111 1000 0000 0000 0000 0000 0000

```
A

**Part c) (6 points + 4 points extra credits) IEEE decided to add a new 12-bit**
​
representation, with its main characteristics consistent with the other IEEE standards.


25

Under this 12-bit representation, the value 3 32 is represented exactly as 010000111001​ .​

**(3 points) How many bits are needed for fraction?**
​

6

**(3 points) What is the bias?**
​

15

**(4 points extra credit) In this 12-bit representation, what is the result of the following**
​
operation?
1110 1011 0010 x​ 0111 0100 1001 ​

-inf


-----

**Problem 3: Logic Design (11 points + 5 points extra credit)**

The functionality of a two-input NOR gate is specified by the following truth table:

**A** **B** **A NOR B**

0 0 1

0 1 0

1 0 0

1 1 0

**Part a) (9 points) Construct the binary NOT, OR and AND gates using only NOR gates.**
​
**(3 points) NOT Gate:**
​

A NOR A

**(3 points) OR Gate:**
​

(A NOR B) NOR (A NOR B)

**(3 points) AND Gate:**
​

((A NOR A) NOR (B NOR B))

|A|B|A NOR B|
|---|---|---|
|0|0|1|
|0|1|0|
|1|0|0|
|1|1|0|


-----

**Part b) (2 points) A binary (2-input-1-output) logic gate is said to be “complete” if every other**
​
binary logic gate can be made using one or more copies of it. For instance, the NAND gate is
known to be complete. Explain very briefly why the NOR gate is complete.

Since we can construct NOT and AND gates, we can construct NAND gates by just inverting the
output of the AND gate using a NOT gate. Since NAND is complete, NOR must be complete as
well.

**Part c) (5 points extra credit) The U.S. government wants to reconstruct a supercomputer**
​
developed by one of its enemies. For this they have asked their top spy, Jonathan, to go
undercover looking for information. While snooping around, Jonathan recovered the following
schematic. But to his dismay, part of the circuit was removed from the diagram. He knows,
however, that the circuit takes two 1-bit inputs (A​ and ​ `B​` ) and gives a single 1-bit output (​ `Out​` ). ​
Furthermore, he knows that the circuit outputs TRUE for every input.

Help Jonathan recover the logic by expressing logic X using only NOT, OR, and AND operations.
You don’t have to draw the schematic; just show the logic expression.

X = (A AND B) OR ((NOT A) AND (NOT B))


-----

**Problem 4: Assembly Programming (24 points + 6 points extra credit)**

For the following parts, the assembly shown uses the syntax opcode src, dst​ for ​
instructions with two arguments where src​ is the source argument and ​ `dst​` is the destination ​
argument. For example, this means that mov a, b​ moves the value ​ `a​` into ​ `b​` and ​ `sub a, b​`
computes the value (b​ - ​ `a​` ) and stores it in ​ `b​` . ​

Also, for functions that take two arguments, the first argument is stored in %rdi​ and the second ​
is stored in %rsi​ at the time the function is called. The return value of this function is stored in ​
```
%eax at the time the function returns. ​

```
**Part a) (18 points) Below is the assembly code for a mystery function in C.**
​
```
0x0000000000401170 <+0>: mov  (%rdi),%eax
0x0000000000401172 <+2>: mov  (%rsi),%edx
0x0000000000401174 <+4>: mov  %edx,(%rdi)
0x0000000000401176 <+6>: mov  %eax,(%rsi)
0x0000000000401178 <+8>: add  (%rdi),%eax
0x000000000040117a <+10>: retq

```
**(3 points) What is one possible data type for the value in %rdi?**
​

int*, long*, short*, ...

**(3 points) What is one possible data type for the value in %eax when func returns?**
​

int, long, short, ...

**(8 points) Suppose that the state of the memory before this function is called is as shown**
​
below, and that the registers %rdi​ = 0x48c and ​ `%rsi​` = 0x484. ​

**State of memory before: (addresses on the left, values on the right)**

|0x480|0x5|
|---|---|
|0x484|0x2|
|0x488|0x20|
|0x48c|0x9|


-----

Fill in the state of the memory after the function is called as well as its return value below.

**State of memory after: (addresses on the left, values on the right)**

`0x480` 0x5

`0x484` 0x9

`0x488` 0x20

`0x48c` 0x2

**(4 points) Return value is:**
​

0xb

|0x480|0x5|
|---|---|
|0x484|0x9|
|0x488|0x20|
|0x48c|0x2|


-----

**Part b) (6 points) Below is the definition of a struct called ​** `student​` in C. Below the definition ​
are three C functions that access certain fields or parts of fields from this struct as well as their
disassembled assembly in random order. Refer to the struct definition to match these functions
with their assembly counterparts in the table below. Assuming that this is a 64-bit machine.
```
typedef struct student{
   short year;
   char major [4];
   int *id;
   struct location {
       char country [3];
       int areacode;
   } home;
   struct student *nextstudent;
} student;

```
|A|B|C|
|---|---|---|
|mov 0x18(%rdi),%rax mov 0x8(%rax),%rax mov (%rax),%eax retq|movsbl 0x11(%rdi),%eax retq|lea 0x14(%rdi),%eax retq|

|C function|Assembly (either A/B/C for each)|
|---|---|
|int* field1(student* s){ return &((s -> home).areacode); }|C|
|char field2(student* s){ return (s -> home).country[1]; }|B|
|int field3(student* s){ return *(s -> nextstudent -> id); }|A|


-----

**Part c) (6 points extra credit) Below is the assembly code for another mystery function in C**
​
called loop​ . Refer to this code when answering questions below. ​
```
0x000000000040119f <+0>:   push  %rbp
0x00000000004011a0 <+1>:   mov  %rsp,%rbp
0x00000000004011a3 <+4>:   movl  $0x0,-0x4(%rbp)
0x00000000004011aa <+11>:  movl  $0x5,-0x8(%rbp)
0x00000000004011b1 <+18>:  jmp  0x4011bc <loop+29>
0x00000000004011b3 <+20>:  mov  -0x8(%rbp),%eax
0x00000000004011b6 <+23>:  imul  %eax,%eax
0x00000000004011b9 <+26>:  add  %eax,-0x4(%rbp)
0x00000000004011bc <+29>:  subl  $0x1,-0x8(%rbp)
0x00000000004011c0 <+33>:  jg   0x4011b3 <loop+20>
0x00000000004011c2 <+35>:  mov  -0x4(%rbp),%eax
0x00000000004011c5 <+38>:  nop
0x00000000004011c6 <+39>:  pop  %rbp
0x00000000004011c7 <+40>:  retq

```
**(3 points) What does ​** `loop()​` return? ​

30

**(3 points) How many instructions are executed in the entire execution of ​** `loop()​` (including ​
```
nop’s)? ​

```
31


-----

**Problem 5: ISA (11 points + 5 points extra credit)**
The designers of a new ISA are thinking about how to encode jump instructions. Instead of
having different opcodes for all the different kinds of jumps (jle, jg, jz, etc), they want to have
one opcode for all jumps, and the kind of jump will be encoded in the instruction (see below).

In this ISA, there are 4 condition codes (C0, C1, C2, and C3), whose values can be either 0 or 1.
These are similar to the status flags on x86 in that they reflect the status of the last instruction
executed. The meanings of the condition codes for the add​ and ​ `sub​` (subtract) instructions in ​
this ISA are given below. The mov​ instruction does not change the condition codes. ​

**Condition Code** **Meaning when codes are set for Add/Subtract instruction**

C0 Result zero; no overflow

C1 Result less than zero; no overflow

C2 Result greater than zero; no overflow

C3 Overflow

The jump instruction encoding includes a 4 bit long mask as part of its encoding. The mask is
from bits 12-15, as shown in the table.

**Condition Code** **Set Bit Position in**
**the Instruction**

C0 12

C1 13

C2 14

C3 15

A 1 in a certain bit position indicates that that condition code is selected when deciding whether
to take the jump or not. To determine if the jump should be taken, the CPU computes the OR​ of ​
the values of all the condition codes selected by the mask, and takes the jump if the result of the
`OR is 1. For example, a mask​` ​ `0110​` ​ selects C1 and C2, and it indicates that the jump will be taken ​
if C1 OR​ C2 is 1. ​

The entire jump instructions is 48-bit long, and it is encoded as follows:

00000111 Padding (all 1) Mask Destination (jump target address)

0               7 8                  11 12            15 16                             47

Bits 0-7 for the opcode, bits 8-11 for the padding (these bits are all 1), bits 12-15 for the mask (as
described above), and bits 16-47 for the destination address (i.e., the jump target).

Finally, all the registers in this ISA are 64-bit wide.

|Condition Code|Meaning when codes are set for Add/Subtract instruction|
|---|---|
|C0|Result zero; no overflow|
|C1|Result less than zero; no overflow|
|C2|Result greater than zero; no overflow|
|C3|Overflow|

|Condition Code|Set Bit Position in the Instruction|
|---|---|
|C0|12|
|C1|13|
|C2|14|
|C3|15|

|00000111|Padding (all 1)|Mask|Destination (jump target address)|
|---|---|---|---|


-----

**Part a) (8 points) Consider the following code (the syntax is​** ​ `opcode src, dest​` ) for this ​
hypothetical ISA:
```
add r2, r1
sub r1, r2
sub 0x0c, r1
mov r1,r2

```
Suppose for this part that when this code starts executing, the value​ `0x0e​` ​ is stored in​ ​ `r1​` ​ and ​
the value​ `0x02​` ​ is stored in​ ​ `r2​` . ​ What is the value of each condition code bit after executing these ​
instructions?

**Condition Code** **Value**

C0 0

C1 0

C2 1

C3 0

**Part b) (3 points) Give the complete encoding (in hexadecimal) of a jump instruction, which**
​
jumps to address​ `0xffff3d00​` ​ if the result of the previous instruction is less than or equal to 0. ​
Assume that the target address is placed directly in the destination field in big-endian order.

0x07fcffff3d00

**Part c) (5 points extra credit) Now suppose that when the code in part a) starts executing,**
​
the value​ `0x04​` ​ is stored​ in ​ `r1​` ​ and the value​ ​ `0x0d​` ​ is stored in​ ​ `r2​` . ​ Suppose that your jump ​
instruction from part b) is executed after the instructions from part a). Will the jump be taken?
Why or why not? Explain.

No. The jump is taken when the condition codes indicate the result was less than or equal to
0. In this case, with those numbers, the last result that set the condition codes was 0x5, which
is greater than 0, so the condition codes will not be set properly for the jump to happen.

|Condition Code|Value|
|---|---|
|C0|0|
|C1|0|
|C2|1|
|C3|0|


-----

###### Midterm Exam

**CSC 252**

**5 March 2020**

**Computer Science Department**

**University of Rochester**

**Instructor: Yuhao Zhu**
​
**TAs: Daniel Busaba, Sudhanshu Gupta, Mandar Juvekar, Max Kimmelman, Weituo Kong,**
​
Jiahao Lu, Vladimir Maksimovski, Nathan Reed, Yawo Alphonse Siatitse, Yudi Yang, Shuang
Zhai, Prikshet Sharma

**Name: ____________________________________**
​ ​

Problem 0 (2 points):

Problem 1 (13 points):

Problem 2 (14 points):

Problem 3 (11 points):

Problem 4 (24 points):

Problem 5 (11 points):

Total (75 points):

Extra Credit (20 points)

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
​ ​
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 75 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:_________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (2 Points) What’s your favourite instruction?**
​

**Problem 1: Fixed-Point Arithmetics (13 points)**
**Part a) (3 points) Represent the decimal number 683 in hexadecimal.**
​

**Part b) (3 points) Represent the binary value 10000111 in the base-6 number system.**
​

**Part c) (3 points) Represent the binary value 1101.101 in decimal.**
​

**Part d) (4 points) Is it possible to add two registers and set Carry Flag to 1, Zero Flag to 0,**
​
Signed Flag to 1, and Overflow Flag to 1? If yes, show an example; otherwise, explain.


-----

**Problem 2: Floating-Point Arithmetics (14 points + 4 points extra credit)**

19

**Part a) (4 points) Put​** 7 64 in the binary normalized form.

**Part b) (4 points) According to the IEEE754 single-precision format, which of the following is**
​
NaN?
```
  A. 0111 1111 1100 1010 0100 1001 0001 0010
  B. 1111 1111 0100 1010 0100 1001 0001 0010
  C. 0000 0000 0000 0000 0000 0000 0000 0000
  D. 0111 1111 1000 0000 0000 0000 0000 0000

```
**Part c) (6 points + 4 points extra credits) IEEE decided to add a new 12-bit**
​
representation, with its main characteristics consistent with the other IEEE standards.


25

Under this 12-bit representation, the value 3 32 is represented exactly as 010000111001​ .​

**(3 points) How many bits are needed for fraction?**
​

**(3 points) What is the bias?**
​

**(4 points extra credit) In this 12-bit representation, what is the result of the following**
​
operation?
1110 1011 0010 x​ 0111 0100 1001 ​


-----

**Problem 3: Logic Design (11 points + 5 points extra credit)**

The functionality of a two-input NOR gate is specified by the following truth table:

**A** **B** **A NOR B**

0 0 1

0 1 0

1 0 0

1 1 0

**Part a) (9 points) Construct the binary NOT, OR and AND gates using only NOR gates.**
​
**(3 points) NOT Gate:**
​

**(3 points) OR Gate:**
​

**(3 points) AND Gate:**
​

|A|B|A NOR B|
|---|---|---|
|0|0|1|
|0|1|0|
|1|0|0|
|1|1|0|


-----

**Part b) (2 points) A binary (2-input-1-output) logic gate is said to be “complete” if every other**
​
binary logic gate can be made using one or more copies of it. For instance, the NAND gate is
known to be complete. Explain very briefly why the NOR gate is complete.

**Part c) (5 points extra credit) The U.S. government wants to reconstruct a supercomputer**
​
developed by one of its enemies. For this they have asked their top spy, Jonathan, to go
undercover looking for information. While snooping around, Jonathan recovered the following
schematic. But to his dismay, part of the circuit was removed from the diagram. He knows,
however, that the circuit takes two 1-bit inputs (A​ and ​ `B​` ) and gives a single 1-bit output (​ `Out​` ). ​
Furthermore, he knows that the circuit outputs TRUE for every input.

Help Jonathan recover the logic by expressing logic X using only NOT, OR, and AND operations.
You don’t have to draw the schematic; just show the logic expression.


-----

**Problem 4: Assembly Programming (24 points + 6 points extra credit)**

For the following parts, the assembly shown uses the syntax opcode src, dst​ for ​
instructions with two arguments where src​ is the source argument and ​ `dst​` is the destination ​
argument. For example, this means that mov a, b​ moves the value ​ `a​` into ​ `b​` and ​ `sub a, b​`
computes the value (b​ - ​ `a​` ) and stores it in ​ `b​` . ​

Also, for functions that take two arguments, the first argument is stored in %rdi​ and the second ​
is stored in %rsi​ at the time the function is called. The return value of this function is stored in ​
```
%eax at the time the function returns. ​

```
**Part a) (18 points) Below is the assembly code for a mystery function in C.**
​
```
0x0000000000401170 <+0>: mov  (%rdi),%eax
0x0000000000401172 <+2>: mov  (%rsi),%edx
0x0000000000401174 <+4>: mov  %edx,(%rdi)
0x0000000000401176 <+6>: mov  %eax,(%rsi)
0x0000000000401178 <+8>: add  (%rdi),%eax
0x000000000040117a <+10>: retq

```
**(3 points) What is one possible data type for the value in %rdi?**
​

**(3 points) What is one possible data type for the value in %eax when func returns?**
​

**(8 points) Suppose that the state of the memory before this function is called is as shown**
​
below, and that the registers %rdi​ = 0x48c and ​ `%rsi​` = 0x484. ​

**State of memory before: (addresses on the left, values on the right)**

|0x480|0x5|
|---|---|
|0x484|0x2|
|0x488|0x20|
|0x48c|0x9|


-----

Fill in the state of the memory after the function is called as well as its return value below.

**State of memory after: (addresses on the left, values on the right)**
```
 0x480
 0x484
 0x488
 0x48c

```
**(4 points) Return value is:**
​

|0x480|Col2|
|---|---|
|0x484||
|0x488||
|0x48c||


-----

**Part b) (6 points) Below is the definition of a struct called ​** `student​` in C. Below the definition ​
are three C functions that access certain fields or parts of fields from this struct as well as their
disassembled assembly in random order. Refer to the struct definition to match these functions
with their assembly counterparts in the table below. Assuming that this is a 64-bit machine.
```
typedef struct student{
   short year;
   char major [4];
   int *id;
   struct location {
       char country [3];
       int areacode;
   } home;
   struct student *nextstudent;
} student;

```
|A|B|C|
|---|---|---|
|mov 0x18(%rdi),%rax mov 0x8(%rax),%rax mov (%rax),%eax retq|movsbl 0x11(%rdi),%eax retq|lea 0x14(%rdi),%eax retq|

|C function|Assembly (either A/B/C for each)|
|---|---|
|int* field1(student* s){ return &((s -> home).areacode); }||
|char field2(student* s){ return (s -> home).country[1]; }||
|int field3(student* s){ return *(s -> nextstudent -> id); }||


-----

**Part c) (6 points extra credit) Below is the assembly code for another mystery function in C**
​
called loop​ . Refer to this code when answering questions below. ​
```
0x000000000040119f <+0>:   push  %rbp
0x00000000004011a0 <+1>:   mov  %rsp,%rbp
0x00000000004011a3 <+4>:   movl  $0x0,-0x4(%rbp)
0x00000000004011aa <+11>:  movl  $0x5,-0x8(%rbp)
0x00000000004011b1 <+18>:  jmp  0x4011bc <loop+29>
0x00000000004011b3 <+20>:  mov  -0x8(%rbp),%eax
0x00000000004011b6 <+23>:  imul  %eax,%eax
0x00000000004011b9 <+26>:  add  %eax,-0x4(%rbp)
0x00000000004011bc <+29>:  subl  $0x1,-0x8(%rbp)
0x00000000004011c0 <+33>:  jg   0x4011b3 <loop+20>
0x00000000004011c2 <+35>:  mov  -0x4(%rbp),%eax
0x00000000004011c5 <+38>:  nop
0x00000000004011c6 <+39>:  pop  %rbp
0x00000000004011c7 <+40>:  retq

```
**(3 points) What does ​** `loop()​` return? ​

**(3 points) How many instructions are executed in the entire execution of ​** `loop()​` (including ​
```
nop’s)? ​

```

-----

**Problem 5: ISA (11 points + 5 points extra credit)**
The designers of a new ISA are thinking about how to encode jump instructions. Instead of
having different opcodes for all the different kinds of jumps (jle, jg, jz, etc), they want to have
one opcode for all jumps, and the kind of jump will be encoded in the instruction (see below).

In this ISA, there are 4 condition codes (C0, C1, C2, and C3), whose values can be either 0 or 1.
These are similar to the status flags on x86 in that they reflect the status of the last instruction
executed. The meanings of the condition codes for the add​ and ​ `sub​` (subtract) instructions in ​
this ISA are given below. The mov​ instruction does not change the condition codes. ​

**Condition Code** **Meaning when codes are set for Add/Subtract instruction**

C0 Result zero; no overflow

C1 Result less than zero; no overflow

C2 Result greater than zero; no overflow

C3 Overflow

The jump instruction encoding includes a 4 bit long mask as part of its encoding. The mask is
from bits 12-15, as shown in the table.

**Condition Code** **Set Bit Position in**
**the Instruction**

C0 12

C1 13

C2 14

C3 15

A 1 in a certain bit position indicates that that condition code is selected when deciding whether
to take the jump or not. To determine if the jump should be taken, the CPU computes the OR​ of ​
the values of all the condition codes selected by the mask, and takes the jump if the result of the
`OR is 1. For example, a mask​` ​ `0110​` ​ selects C1 and C2, and it indicates that the jump will be taken ​
if C1 OR​ C2 is 1. ​

The entire jump instructions is 48-bit long, and it is encoded as follows:

00000111 Padding (all 1) Mask Destination (jump target address)

0               7 8                  11 12            15 16                             47

Bits 0-7 for the opcode, bits 8-11 for the padding (these bits are all 1), bits 12-15 for the mask (as
described above), and bits 16-47 for the destination address (i.e., the jump target).

Finally, all the registers in this ISA are 64-bit wide.

|Condition Code|Meaning when codes are set for Add/Subtract instruction|
|---|---|
|C0|Result zero; no overflow|
|C1|Result less than zero; no overflow|
|C2|Result greater than zero; no overflow|
|C3|Overflow|

|Condition Code|Set Bit Position in the Instruction|
|---|---|
|C0|12|
|C1|13|
|C2|14|
|C3|15|

|00000111|Padding (all 1)|Mask|Destination (jump target address)|
|---|---|---|---|


-----

**Part a) (8 points) Consider the following code (the syntax is​** ​ `opcode src, dest​` ) for this ​
hypothetical ISA:
```
add r2, r1
sub r1, r2
sub 0x0c, r1
mov r1,r2

```
Suppose for this part that when this code starts executing, the value​ `0x0e​` ​ is stored in​ ​ `r1​` ​ and ​
the value​ `0x02​` ​ is stored in​ ​ `r2​` . ​ What is the value of each condition code bit after executing these ​
instructions?

**Condition Code** **Value**

C0

C1

C2

C3

**Part b) (3 points) Give the complete encoding (in hexadecimal) of a jump instruction, which**
​
jumps to address​ `0xffff3d00​` ​ if the result of the previous instruction is less than or equal to 0. ​
Assume that the target address is placed directly in the destination field in big-endian order.

**Part c) (5 points extra credit) Now suppose that when the code in part a) starts executing,**
​
the value​ `0x04​` ​ is stored​ in ​ `r1​` ​ and the value​ ​ `0x0d​` ​ is stored in​ ​ `r2​` . ​ Suppose that your jump ​
instruction from part b) is executed after the instructions from part a). Will the jump be taken?
Why or why not? Explain.

|Condition Code|Value|
|---|---|
|C0||
|C1||
|C2||
|C3||


-----

###### Final Exam

**CSC 252**

**8 May 2019**

**Computer Science Department**

**University of Rochester**

Instructor: Yuhao Zhu
TAs: Jessica Ervin, Yu Feng, Max Kimmelman, Olivia Morton, Yawo Alphonse Siatitse,
Yiyang Su, Amir Taherin, Samuel Triest, Minh Tran

**Name: ____________________________________**
​ ​

Problem 0 (3 points):

Problem 1 (17 points):

Problem 2 (10 points):

Problem 3 (20 points):

Problem 4 (20 points):

Problem 5 (30 points):

Total (100 points):

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
​ ​
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. The lengths of the boxes
should be more or less indicative of the lengths of your answers. Use spare space to show all
supporting work to earn partial credit.

You have 2 hours 45 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:___________________________________________________________

**GOOD LUCK!!!**

**And have a great summer break.**


-----

**Problem 0: Warm-up (3 Points)**

Some people say 252 shouldn’t be required for the BS. What say you? (Hint: the correct answer
is YES, IT SHOULD BE, but we are not necessarily looking for the correct answer here.)

**Problem 1: Floating-Point Arithmetics (17 points)**

In this problem, we assume that IEEE decided to add a new N-bit representation, with its main
characteristics consistent with the other IEEE standards. This N-bit representation could

1 1
represent the value 12 exactly, but cannot represent the value 34 exactly. The smallest
8 4

positive normalized value it can represent is 2 .
​[-62][​]

1
**Part a) (3 points) Put​** 12 8 in binary normalized form.

1.100001 x 2^3

**Part b) (3 points) Of the N bits, how many bits are fraction bits?**
​

6

**Part c) (3 points) Of the N bits, how many bits are exponent bits?**
​

7

**Part d) (4 points) What is N?**
​

14

**Part e) (4 points) What is the bias?**
​

63


-----

**Problem 2: Pipelining (10 points)**

A pipelined processor has 5 stages with delays as follows:

Stage 1 28 ns

Stage 2 59 ns

Stage 3 23 ns

Stage 4 34 ns

Stage 5 36 ns

The delay of pipeline registers between two stage is 1 ns.

**Part a) (4 points) What is the cycle time of this processor? Recall the cycle time refers to the**
​
delay of a single clock cycle.

60 ns

**Part b) (6 points) Now we execute 8 instructions on this pipelined processor. What is the**
​
speedup that the pipeline achieves compared to a non-pipelined design? Assume that there are
no pipeline stalls. Show your work to earn partial credit.

Without pipeline: Delay is (28 + 59 + 23 + 34 + 36) * 8
With pipeline: Delay is 60 * 5 + 7 * 60

Speedup = 2

|Stage 1|28 ns|
|---|---|
|Stage 2|59 ns|
|Stage 3|23 ns|
|Stage 4|34 ns|
|Stage 5|36 ns|


-----

**Problem 3: Assembly Programming (20 points)**

Clark Kent has taken CSC 252 and is working on research project on ISA. Clark defines
Kryptonian numbers and Xenonian numbers as follows.

  - A binary number is said to be Kryptonian if and only if there are more 0’s than 1’s when
​ ​
we discard the leading zeros. For example, 1001002​ is Kryptonian and 000001111​ 2​ is not. ​

  - A binary number is said to be Xenonian if and only if there are exactly 4 1’s. For example,
​ ​
1101102​ is Xenonian and 11111​ 2​ is not. ​

**Part a) (8 points) Consider the 32-bit two’s complement representation. Is 18​** 10​ a Kryptonian, ​
and is -1810 ​ a Xenonian? Show your work to earn partial credit. ​

18 is a Kryptonian
-18 is not a Xenonian

**Part b) (12 points) Clark wants to add two new flags to the standard x86-64 ISA.**
​

  - Krypton Flag: set if a number is Kryptonian.

  - Xenon Flag: set if a number is Xenonian.

According to Clark’s ISA specification, the addl​ instruction sets these two flags according to the ​
addition result, and the movl​ instruction sets these two flags according to the content of the ​
source operand, i.e., the content that is being moved. No other instructions change these two
flags. Other flags are set as in the standard x86-64 ISA.

Further, Clark implemented the following two instructions:

  - `jkr addr: jump to the address specified by ​` `addr​` if the Krypton flag is set and the ​
Overflow flag is not set.

  - `jxn addr: jump to the address specified by ​` `addr​` if the Xenon flag is set and the ​
Overflow flag is not set.

He wrote the following function in assembly language to test his work. Recall from the
programming assignments that movl​ instructions move a 4 byte integer to the destination, and ​
the size of the data moved by the mov​ instructions is implicit in the operands. We assume an ​
assembly syntax where the source is the first operand and the destination is the second operand.
```
00000000000005fa <foo>:
 5fa: 55 push  %rbp
 5fb: 48 89 e5 mov  %rsp,%rbp

```

-----

```
 5fe: 89 7d ec mov  %edi,-0x14(%rbp)
 601: 48 89 75 e0 mov  %rsi,-0x20(%rbp)
 605: c7 45 f8 00 00 00 00 movl  $0x0,-0x8(%rbp)
 60c: c7 45 fc 12 00 00 00 movl  $0x12,-0x4(%rbp)
 613: eb 0e jmp  61f
 615: 7e 04 jkr  61b
 617: 83 45 f8 01 addl  $0x1,-0x8(%rbp)
 61b: 83 45 fc 01 addl  $0x1,-0x4(%rbp)
 61f: 83 7d fc 35 cmpl  $0x35,-0x4(%rbp)
 624: 7e ec jle  615 <foo+0x1b>
 626: b8 00 00 00 00 mov  $0x0,%eax
 62b: 5d pop  %rbp
 62c: c3 retq

```
Unfortunately, he made a small mistake in his implementation such that the machine will jump
to the designated address on any jkr​ /​ `jxn​` instruction regardless of the flags. ​

**(4 points) On this faulty machine, what is the value of ​** `-0x18(%rsp)​` after the ​ `foo​` function ​
returns? Hint: what do pop​ and ​ `retq​` do to ​ `%rsp​` ? ​

0

**(4 points) He then fixes the mistake, and runs the same program again on this correct**
​
machine. What is the value of -0x18(%rsp)​ now after the ​ `foo​` function returns? ​

26

**(4 points) To test the Xenon flag and the ​** `jxn​` instruction, Clark replaces the instruction at ​
`0x61f with four ​` `nop​` instructions, and replaces the instruction at ​ `0x624​` with ​ `jxn 615​` . What ​
is the value of -0x18(%rsp)​ after the ​ `foo​` function returns? ​

3


-----

**Problem 4: Cache (20 points)**

Solar radiation can randomly flip bits in the computer system. Therefore, a cache on a
space-faring vehicle, which is exposed to solar radiation, utilizes error-correcting codes (ECC)
_for each of its cache blocks to detect if bits have been flipped. These ECC bits add to the_
​
overhead of the cache, in addition to the usual overhead bits such as valid bits and tags, etc.

On a memory access, the cache operates as normal, but in addition to checking hit/miss it will
also check if the content in the cache block has been corrupted. This is done by checking the ECC
bits. How exactly ECC bits are used to detect corruption is irrelevant to this problem. If the ECC
bits associated with a block indicate that the data in the block is corrupted, that cache access is
regarded as a cache miss. For the sake of the problem, assume that the memory is incorruptible.

The physical memory is byte addressable, and is 64 KB in size. Each cache block is 4B, and
requires 6 extra bits for the error-correcting codes. The cache is 2-way associative with the LRU
replacement policy. The entire cache has an overhead of 3712 bits.

**Part a) (4 points) For this cache to function properly, should it use a write-back policy or a**
​
write-through policy upon a write hit?

Write through

**Part b) (4 points) Determine the number of offset bits.**
​

2

**Part c) (4 points) Determine the number of tag bits.**
​

7

Hint: how many bits does each set have to have to implement the LRU replacement policy? Use
the box below to show your work to earn partial credit.


-----

**Part d) (8 points) Given the following sequence of 9 cache accesses; some cache accesses**
​
result in loads from the physical memory. Assume that the initial state of the cache is empty.

**Address** **Load From Memory?**

a) 0x3420 Yes

b) 0x3423 Yes

c) 0x062e Yes

d) 0x1e2f Yes

e) 0x73ec Yes

f) 0x062f No

g) 0x0e2f Yes

h) 0x1e2e Yes

i) 0x0e2e Yes

Determine which accesses were necessarily a result of cache corruption due to solar radiation.
Write the letters corresponding to the memory addresses below:

b) and i)

|Address|Load From Memory?|
|---|---|
|a) 0x3420|Yes|
|b) 0x3423|Yes|
|c) 0x062e|Yes|
|d) 0x1e2f|Yes|
|e) 0x73ec|Yes|
|f) 0x062f|No|
|g) 0x0e2f|Yes|
|h) 0x1e2e|Yes|
|i) 0x0e2e|Yes|


-----

**Problem 5: Virtual Memory (30 points)**

The diagram below shows the interactions between components of a computer system resulting
from a single virtual memory access from the CPU. You are given the following information:
​ ​

  - Assume a single-level virtual memory system.

  - The virtual address space is 128 KB.

  - The physical memory size is 32 KB.

  - The L1 cache block size is 2 B.

  - The value stored in the Page Table Base Register (PTBR) is 0x260.

  - Each Page Table Entry (PTE) takes 2 B and has the following structure:

Valid <1-bit> Padding of zeros Physical page number

**Part a) (22 points) Fill in the right column of the table below with answers to the questions ​**
###### about each step in the diagram above. “I don’t know” is accepted at each entry.

|Valid <1-bit>|Padding of zeros|Physical page number|
|---|---|---|

|1|CPU reads virtual address 0x_______|0x488|
|---|---|---|
|2|MMU checks TLB. Is this a hit or a miss?|miss|
|3|MMU accesses memory at physical address 0x2F0. Is this a hit or a miss?|hit|
|4|What is the most significant bit of the data returned to the MMU and TLB?|0|
|5|What happens at this step? (Answer in 15 words or fewer)|Page fault handler evicts a victim page from physical memory|


-----

|6|16 bytes are returned.|(no question)|
|---|---|---|
|7|CPU reads virtual address 0x_______|0x488|
|8|MMU checks TLB. Is this a hit or a miss?|hit|
|9|Data returned from TLB to MMU is 0x______|0x80A4|
|10|MMU accesses memory at physical address 0xA48. Is this a hit or a miss?|miss|
|11|Is this an access to the page table?|no|
|12|How many bytes of data are returned here?|2B|
|13|Requested data is returned to the CPU.|(no question)|


**Part b) (3 points) How many pages does the entire page table occupy? ​**

###### 2^10 = 1024

**Part c) (3 points) How many physical memory accesses were made during this single virtual ​**
###### memory access?

 2 or 3 (depending on how you count)

**Part d) (2 points) What would the system do differently at step 3 and 4 if the L1 cache block ​**
###### size is 1 B?

 The system would request and receive two cache blocks from the L1 cache and concatenate them instead of just accessing one cache block in order to get the PTE


-----

###### Final Exam

**CSC 252**

**8 May 2019**

**Computer Science Department**

**University of Rochester**

Instructor: Yuhao Zhu
TAs: Jessica Ervin, Yu Feng, Max Kimmelman, Olivia Morton, Yawo Alphonse Siatitse,
Yiyang Su, Amir Taherin, Samuel Triest, Minh Tran

**Name: ____________________________________**
​ ​

Problem 0 (3 points):

Problem 1 (17 points):

Problem 2 (10 points):

Problem 3 (20 points):

Problem 4 (20 points):

Problem 5 (30 points):

Total (100 points):

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
​ ​
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. The lengths of the boxes
should be more or less indicative of the lengths of your answers. Use spare space to show all
supporting work to earn partial credit.

You have 2 hours 45 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:___________________________________________________________

**GOOD LUCK!!!**

**And have a great summer break.**


-----

**Problem 0: Warm-up (3 Points)**

Some people say 252 shouldn’t be required for the BS. What say you? (Hint: the correct answer
is YES, IT SHOULD BE, but we are not necessarily looking for the correct answer here.)

**Problem 1: Floating-Point Arithmetics (17 points)**

In this problem, we assume that IEEE decided to add a new N-bit representation, with its main
characteristics consistent with the other IEEE standards. This N-bit representation could

1 1
represent the value 12 exactly, but cannot represent the value 34 exactly. The smallest
8 4

positive normalized value it can represent is 2 .
​[-62][​]

1
**Part a) (3 points) Put​** 12 8 in binary normalized form.

**Part b) (3 points) Of the N bits, how many bits are fraction bits?**
​

**Part c) (3 points) Of the N bits, how many bits are exponent bits?**
​

**Part d) (4 points) What is N?**
​

**Part e) (4 points) What is the bias?**
​


-----

**Problem 2: Pipelining (10 points)**

A pipelined processor has 5 stages with delays as follows:

Stage 1 28 ns

Stage 2 59 ns

Stage 3 23 ns

Stage 4 34 ns

Stage 5 36 ns

The delay of pipeline registers between two stage is 1 ns.

**Part a) (4 points) What is the cycle time of this processor? Recall the cycle time refers to the**
​
delay of a single clock cycle.

**Part b) (6 points) Now we execute 8 instructions on this pipelined processor. What is the**
​
speedup that the pipeline achieves compared to a non-pipelined design? Assume that there are
no pipeline stalls. Show your work to earn partial credit.

|Stage 1|28 ns|
|---|---|
|Stage 2|59 ns|
|Stage 3|23 ns|
|Stage 4|34 ns|
|Stage 5|36 ns|


-----

**Problem 3: Assembly Programming (20 points)**

Clark Kent has taken CSC 252 and is working on research project on ISA. Clark defines
Kryptonian numbers and Xenonian numbers as follows.

  - A binary number is said to be Kryptonian if and only if there are more 0’s than 1’s when
​ ​
we discard the leading zeros. For example, 1001002​ is Kryptonian and 000001111​ 2​ is not. ​

  - A binary number is said to be Xenonian if and only if there are exactly 4 1’s. For example,
​ ​
1101102​ is Xenonian and 11111​ 2​ is not. ​

**Part a) (8 points) Consider the 32-bit two’s complement representation. Is 18​** 10​ a Kryptonian, ​
and is -1810 ​ a Xenonian? Show your work to earn partial credit. ​

**Part b) (12 points) Clark wants to add two new flags to the standard x86-64 ISA.**
​

  - Krypton Flag: set if a number is Kryptonian.

  - Xenon Flag: set if a number is Xenonian.

According to Clark’s ISA specification, the addl​ instruction sets these two flags according to the ​
addition result, and the movl​ instruction sets these two flags according to the content of the ​
source operand, i.e., the content that is being moved. No other instructions change these two
flags. Other flags are set as in the standard x86-64 ISA.

Further, Clark implemented the following two instructions:

  - jkr addr: jump to the address specified by ​ addr​ if the Krypton flag is set and the ​
Overflow flag is not set.

  - jxn addr: jump to the address specified by ​ addr​ if the Xenon flag is set and the ​
Overflow flag is not set.

He wrote the following function in assembly language to test his work. Recall from the
programming assignments that movl​ instructions move a 4 byte integer to the destination, and ​
the size of the data moved by the mov​ instructions is implicit in the operands. We assume an ​
assembly syntax where the source is the first operand and the destination is the second operand.

00000000000005fa <foo>:
5fa: 55 push  %rbp

5fb: 48 89 e5 mov  %rsp,%rbp


-----

5fe: 89 7d ec mov  %edi,-0x14(%rbp)

601: 48 89 75 e0 mov  %rsi,-0x20(%rbp)

605: c7 45 f8 00 00 00 00 movl  $0x0,-0x8(%rbp)
60c: c7 45 fc 12 00 00 00 movl  $0x12,-0x4(%rbp)
613: eb 0e jmp  61f

615: 7e 04 jkr  61b

617: 83 45 f8 01 addl  $0x1,-0x8(%rbp)

61b: 83 45 fc 01 addl  $0x1,-0x4(%rbp)

61f: 83 7d fc 35 cmpl  $0x35,-0x4(%rbp)

624: 7e ec jle  615 <foo+0x1b>

626: b8 00 00 00 00 mov  $0x0,%eax

62b: 5d pop  %rbp

62c: c3 retq

Unfortunately, he made a small mistake in his implementation such that the machine will jump
to the designated address on any jkr​ /​ jxn​ instruction regardless of the flags. ​

**(4 points) On this faulty machine, what is the value of ​** -0x18(%rsp)​ after the ​ foo​ function ​
returns? Hint: what do pop​ and ​ retq​ do to ​ %rsp​ ? ​

**(4 points) He then fixes the mistake, and runs the same program again on this correct**
​
machine. What is the value of -0x18(%rsp)​ now after the ​ foo​ function returns? ​

**(4 points) To test the Xenon flag and the ​** jxn​ instruction, Clark removes the instruction at ​
0x61f and replaces the instruction at ​ 0x624​ with ​ jxn 615​ . What is the value of ​
-0x18(%rsp) after the ​ foo​ function returns? ​


-----

**Problem 4: Cache (20 points)**

Solar radiation can randomly flip bits in the computer system. Therefore, a cache on a
space-faring vehicle, which is exposed to solar radiation, utilizes error-correcting codes (ECC)
_for each of its cache blocks to detect if bits have been flipped. These ECC bits add to the_
​
overhead of the cache, in addition to the usual overhead bits such as valid bits and tags, etc.

On a memory access, the cache operates as normal, but in addition to checking hit/miss it will
also check if the content in the cache block has been corrupted. This is done by checking the ECC
bits. How exactly ECC bits are used to detect corruption is irrelevant to this problem. If the ECC
bits associated with a block indicate that the data in the block is corrupted, that cache access is
regarded as a cache miss. For the sake of the problem, assume that the memory is incorruptible.

The physical memory is byte addressable, and is 64 KB in size. Each cache block is 4B, and
requires 6 extra bits for the error-correcting codes. The cache is 2-way associative with the LRU
replacement policy. The entire cache has an overhead of 3712 bits.

**Part a) (4 points) For this cache to function properly, should it use a write-back policy or a**
​
write-through policy upon a write hit?

**Part b) (4 points) Determine the number of offset bits.**
​

**Part c) (4 points) Determine the number of tag bits.**
​

Hint: how many bits does each set have to have to implement the LRU replacement policy? Use
the box below to show your work to earn partial credit.


-----

**Part d) (8 points) Given the following sequence of 9 cache accesses; some cache accesses**
​
result in loads from the physical memory. Assume that the initial state of the cache is empty.

**Address** **Load From Memory?**

a) 0x3420 Yes

b) 0x3423 Yes

c) 0x062e Yes

d) 0x1e2f Yes

e) 0x73ec Yes

f) 0x062f No

g) 0x0e2f Yes

h) 0x1e2e Yes

i) 0x0e2e Yes

Determine which accesses were necessarily a result of cache corruption due to solar radiation.
Write the letters corresponding to the memory addresses below:

|Address|Load From Memory?|
|---|---|
|a) 0x3420|Yes|
|b) 0x3423|Yes|
|c) 0x062e|Yes|
|d) 0x1e2f|Yes|
|e) 0x73ec|Yes|
|f) 0x062f|No|
|g) 0x0e2f|Yes|
|h) 0x1e2e|Yes|
|i) 0x0e2e|Yes|


-----

**Problem 5: Virtual Memory (30 points)**

The diagram below shows the interactions between components of a computer system resulting
from a single virtual memory access from the CPU. You are given the following information:
​ ​

  - Assume a single-level virtual memory system.

  - The virtual address space is 128 KB.

  - The physical memory size is 32 KB.

  - The L1 cache block size is 2 B.

  - The value stored in the Page Table Base Register (PTBR) is 0x260.

  - Each Page Table Entry (PTE) takes 2 B and has the following structure:

Valid <1-bit> Padding of zeros Physical page number

**Part a) (22 points) Fill in the right column of the table below with answers to the questions ​**
###### about each step in the diagram above. “I don’t know” is accepted at each entry.

|Valid <1-bit>|Padding of zeros|Physical page number|
|---|---|---|

|1|CPU reads virtual address 0x_______|Col3|
|---|---|---|
|2|MMU checks TLB. Is this a hit or a miss?||
|3|MMU accesses memory at physical address 0x2F0. Is this a hit or a miss?||
|4|What is the most significant bit of the data returned to the MMU and TLB?||
|5|What happens at this step? (Answer in 15 words or fewer)||


-----

|6|16 bytes are returned.|(no question)|
|---|---|---|
|7|CPU reads virtual address 0x_______||
|8|MMU checks TLB. Is this a hit or a miss?||
|9|Data returned from TLB to MMU is 0x______||
|10|MMU accesses memory at physical address 0xA48. Is this a hit or a miss?||
|11|Is this an access to the page table?||
|12|How many bytes of data are returned here?||
|13|Requested data is returned to the CPU.|(no question)|


**Part b) (3 points) How many pages does the entire page table occupy? ​**

**Part c) (3 points) How many physical memory accesses were made during this single virtual ​**
###### memory access?

**Part d) (2 points) What would the system do differently at step 3 and 4 if the L1 cache block ​**
###### size is 1 B?


-----

###### Midterm Exam

**CSC 252**

**7 March 2019**

**Computer Science Department**

**University of Rochester**

Instructor: Yuhao Zhu
TAs: Jessica Ervin, Yu Feng, Max Kimmelman, Olivia Morton, Yawo Alphonse Siatitse,
Yiyang Su, Amir Taherin, Samuel Triest, Minh Tran

**Name: ____________________________________**
​ ​

Problem 0 (2 points):

Problem 1 (15 points):

Problem 2 (16 points):

Problem 3 (14 points):

Problem 4 (14 points):

Problem 5 (14 points):

Total (75 points):

Extra Credit (20 points)

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
​ ​
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. The lengths of the boxes
should be more or less indicative of the lengths of your answers. Use spare space to show all
supporting work to earn partial credit.

You have 75 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:___________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (2 Points)**

Who do you usually study CSC 252 with?

Hopefully you have a study group when studying 252. When you are able to clearly explain
something to others, that’s when you know you really understand it.

**Problem 1: Fixed-Point Arithmetics (15 points + 3 points extra credit)**
**Part a) (4 points) Represent the decimal value 92 in hexadecimal.**
​

0x5c

**Part b) (4 points) Represent the binary value 1110110111 in hexadecimal.**
​

0x3b7

**Part c) (4 points) Octal is the base-8 number system, and uses the digits 0 to 7. Represent the**
​
octal value 273 in binary.

10111011

**Part d) (3 points) Suppose the registers ​** **%esi​**, ​ **%ebx​**, and ​ **%edx​** are initialized with the values ​
shown below.

**%esi** **%ebx** **%edx (before) ​**

0xA2E058 0x800 0x0

What would the value of %edx​ be after the instruction: ​ **lea (%esi, %ebx, 8), %edx​** ? ​

0xA32058

|%esi|%ebx|%edx​ (before)|
|---|---|---|
|0xA2E058|0x800|0x0|


-----

**Part e) (3 points extra credit) Let A and B be two unknown 8-bit 2’s complement numbers.**
​
We know the results of A ^ B and A & B as shown below:

A ^ B 00110100

A & B 11001001

**(1 point) What is the sum A + B expressed in the 8-bit two’s complement notation?**
​

11000110

On an x86 system, would the carry flag be set after A + B? What about the overflow flag?

|A ^ B|00110100|
|---|---|
|A & B|11001001|

|Will carry flag be set? (1 point) ​|Yes|
|---|---|
|Will overflow flag be set? (1 point) ​|No|


-----

**Problem 2: Floating-Point Arithmetics (16 points + 2 points extra credit)**

**Part a) (4 points) Put​** 4 16[3] in binary normalized form.

1.000011 x (2^+2)

**Part b) (12 points + 2 points extra credits) In this problem, we assume that IEEE decided**
​
to add a new 12-bit representation, with its main characteristics consistent with the other IEEE
standards.

In this 12-bit representation, the value 155/256 is represented exactly as 001000110110.

**(4 points) How many bits are needed for exponent?**
​

3

**(4 points) How many bits are needed for fraction?**
​

8

**(4 points) In this 12-bit representation, what is the smallest positive number that can be**
​
represented?

2^-10

**(2 points extra credit) You want to calculate the sum of the following three numbers that are**
​
represented using this 12-bit floating point format: (A) 110111100100, (B) 010101110000, and
(C) 011011000000. Give an order in which the addition will generate the expected sum.

Anything that isn’t BCA or CBA.


-----

**Problem 3: Logic Design (14 points)**

The following is the schematic of a NAND gate, which takes in two 1-bit inputs A​ and ​ **B​**, and ​
generates one 1-bit output Out​ . The NAND gate functions in such a way that ​ **Out = !(A & B)​** . ​

**Part a) (3 points) Now we build the following piece of combinational logic using the NAND**
​
gate, which takes in one 1-bit input A​, and generates one 1-bit output ​ **Out​** . What’s the ​
relationship between Out​ and ​ **A​** ? ​

Out = !A

**Part b) (11 points) We have the combinational circuit shown below with part of its logic**
​
hidden. It takes in one 1-bit input: A​, and produces one 1-bit output: ​ **Out​** . The relationship ​
between A​ and ​ **Out​** is shown in the accompanying truth table. ​

**A** **Out**

0 0

1 0

**(3 points) What is the functionality of the hidden logic in the circuit? You can denote the two**
​
inputs to the hidden logic as In1​ and ​ ​In2. ​

AND, NOR

|A|Out|
|---|---|
|0|0|
|1|0|


-----

**(5 points) Implement the hidden logic using only NAND gates. Draw its schematic below.**
​

(IN1, IN2) -> NAND -> IN3 then (IN3, IN3) -> NAND -> OUT

**(3 points) Given your above implementation and assuming the delay of a NAND gate is 1ps,**
​
what is the delay of the entire combinational circuit?

3ps.


-----

**Problem 4: Assembly Programming (14 points + 6 points extra credits)**

Below is the assembly code for a mystery function in C. Assume this function takes in an
unsigned integer from 1 ~ 8 in %edi​ and returns a value to ​ **%eax​** . The function prototype is the ​
following: unsigned int mystery(unsigned int); ​

Assembly code:

0x0000000000400556 <+0>: push  %rbp

0x0000000000400557 <+1>: mov  %rsp,%rbp

0x000000000040055a <+4>: sub  $0x10,%rsp

0x000000000040055e <+8>: mov  %edi,-0x4(%rbp)

0x0000000000400561 <+11>: cmpl  $0x2,-0x4(%rbp)

0x0000000000400565 <+15>: jne  0x40056e <mystery+24>

0x0000000000400567 <+17>: mov  $0x2,%eax

0x000000000040056c <+22>: jmp  0x4005a5 <mystery+79>

0x000000000040056e <+24>: cmpl  $0x1,-0x4(%rbp)

0x0000000000400572 <+28>: jg   0x400583 <mystery+45>

0x0000000000400574 <+30>: mov  -0x4(%rbp),%eax

0x0000000000400577 <+33>: sub  $0x1,%eax

0x000000000040057a <+36>: mov  %eax,%edi

0x000000000040057c <+38>: callq 0x400556 <mystery>

0x0000000000400581 <+43>: jmp  0x4005a5 <mystery+79>

0x0000000000400583 <+45>: cmpl  $0x1,-0x4(%rbp)

0x0000000000400587 <+49>: jle  0x4005a5 <mystery+79>

0x0000000000400589 <+51>: mov  -0x4(%rbp),%eax

0x000000000040058c <+54>: sub  $0x2,%eax

0x000000000040058f <+57>: mov  %eax,%edi

0x0000000000400591 <+59>: callq 0x400556 <mystery>

0x0000000000400596 <+64>: imul  -0x4(%rbp),%eax

0x000000000040059a <+68>: mov  -0x4(%rbp),%edx

0x000000000040059d <+71>: sub  $0x1,%edx

0x00000000004005a0 <+74>: imul  %edx,%eax

0x00000000004005a3 <+77>: jmp  0x4005a5 <mystery+79>

0x00000000004005a5 <+79>: leaveq

0x00000000004005a6 <+80>: retq


-----

**Part a) (4 points) Assume 2 is stored in ​** **%edi​** at the beginning of the function execution. ​
Which lines of assembly will have been executed after the function finishes execution (denote as
function offset e.g. <+24>)?

0, 1, 4, 8, 11, 15, 17, 22, 79, 80

**Part b) (5 points) This function produces integer over/underflow for some input values. What**
​
are these values? Recall that the input is an unsigned integer from 1 ~ 8 stored in %edi​ . ​

1, 3, 5, 7

**Part c) (5 points) For the input values that do not cause integer over/underflow, what does**
​
this function return? Please express it as a closed-form function of the input (you could denote
the input as x).

x!


-----

**Part d) (6 points extra credit)** There are some ways to modify this assembly program to
​ ​
make the function work for all input values 1 ~ 8. What is one set of 3 or fewer lines of changes
you can make? Note that deletion and replacement are valid changes, insertion is not.

Line# (denote as function offset):

36 OR 15

Change to:

mov 0x01, %eax OR jg 0x400583

Line# (denote as function offset):

38 OR 17

Change to:

delete/ret OR mov-0x4(%rbp), %eax

Line# (denote as function offset):

N/A (hopefully)

Change to:


-----

**Problem 5: ISA and Microarchitecture (14 points + 9 points extra credits)**

Suppose you are working for a microprocessor company RoCChip. You take on the job of
designing the ISA and microarchitecture for a new computer. You want the ISA to have two
types of instructions detailed below.

The first type of instructions (Type A) has the following general format:
**Opcode Ra,Rb,Imm**

Instructions of this type operate as follows. We perform an operation between the values in
registers Ra​ and ​ **Rb​**, and store the result to the memory address specified by the immediate ​
value Imm​ . The immediate value is treated as an absolute (as opposed to relative) memory ​
address. The exact operation to be performed between Ra​ and ​ **Rb​** depends on the specific ​
Opcode. ​

The binary encoding for this type of instructions is the following. The most significant bit is
always 0, indicating that that this is a Type A instruction.

**0 Opcode** **Ra** **Rb** **Imm**

The second type of instructions (Type B) has the following general format:
**Opcode Ra,Rb,Rc**

Instructions of this type operate as follows. We perform an operation between the values in
registers Ra​ and ​ **Rb​**, and store the result to the memory address specified by value in register ​ **Rc​** . ​
Similarly, the exact operation to be performed between Ra​ and ​ **Rb​** depends on the specific ​
Opcode. ​

The binary encoding for this type of instructions is the following. The most significant bit is
always 1, indicating that that this is a Type B instruction.

**1 Opcode** **Ra** **Rb** **Rc**

You want your machine to be byte addressable (i.e., each addressable memory location is one
byte, just like x86). The total memory capacity is 2 Bytes. Each register in this machine hold 4
​[20 ][​]
bytes of data.

For each instruction type, you plan to support 8 different arithmetic and logic operations (same
8 for each type). You also have the limitation that the length of Type A instructions must be 4
bytes.

|0|Opcode|Ra|Rb|Imm|
|---|---|---|---|---|

|1|Opcode|Ra|Rb|Rc|
|---|---|---|---|---|


-----

**Part a) (3 points) What is the minimum number of bits to represent the ​** **Opcode​** field in both ​
types of instructions?

3

**Part b) (3 points) What is the minimum number of bits to represent the ​** **Imm​** field in Type A? ​

20

**Part c) (4 points) Using the number of bits for ​** **Opcode​** and ​ **Imm​** that you came up with in (a) ​
and (b), what is the maximum number registers that your ISA can support?

16

**Part d) (4 points) Assume that we have a program with 1000 instructions. 20% of them are of**
​
Type A, and 80% of Type B. How much space in the memory is occupied by this program?

200*32 + 800*16 = 19,200 bits =
2,400 bytes

**Part e) (9 points extra credit)** Now that you finish designing the ISA, you start working on
​ ​
the microarchitecture, which only has to support the two types of instructions. Below is the
partially complete schematic of the microarchitecture.

The “Address” port of the memory takes the memory address to be written to, and the “Data”
port of the memory takes the data to be written to the memory.

The register file has three read ports and can read three registers, Ra​, ​ **Rb​**, and ​ **Rc​** ​,
simultaneously. How the three Read Reg. IDs are generated is irrelevant to this problem.

There are three hidden logics in this partially complete microarchitecture. You job: determine
the functionalities of the three hidden logics. Note that not all the input signals to the logics are
shown. You need to figure out what signals each logic needs.


-----

**(3 points)** Logic 1 generates the select signal to the MUX that produces the memory address.
​ ​
Briefly explain how Logic 1 generates the select signal.

Select bet. rC and imm. Look @ first bit of instruction. 0->imm, 1->register

**(3 points)​** Logic 2 takes the value of ​ **Rc​** and generates one of the two pieces of data that go into ​
the MUX. Briefly explain how Logic 2 generates its output.

Truncate rC to get 20 lsb from the 32 bits in rC


-----

**(3 points)** Logic 3 generates the next PC (nPC), which contains the address of the next
​ ​
instruction to be fetched and executed. Briefly explain how Logic 3 generates nPC.

Length of each instr. Depends on first bit. Add offset equal to instruction length, which is
determined w/ the bit in PC.


-----

###### Midterm Exam

**CSC 252**

**7 March 2019**

**Computer Science Department**

**University of Rochester**

Instructor: Yuhao Zhu
TAs: Jessica Ervin, Yu Feng, Max Kimmelman, Olivia Morton, Yawo Alphonse Siatitse,
Yiyang Su, Amir Taherin, Samuel Triest, Minh Tran

**Name: ____________________________________**
​ ​

Problem 0 (2 points):

Problem 1 (15 points):

Problem 2 (16 points):

Problem 3 (14 points):

Problem 4 (14 points):

Problem 5 (14 points):

Total (75 points):

Extra Credit (20 points)

Remember “I don’t know” is given 15% partial credit, but you must erase everything else. This
​ ​
does not apply to extra credit questions.

Your answers to all questions must be contained in the given boxes. The lengths of the boxes
should be more or less indicative of the lengths of your answers. Use spare space to show all
supporting work to earn partial credit.

You have 75 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:___________________________________________________________

**GOOD LUCK!!!**


-----

**Problem 0: Warm-up (2 Points)**

Who do you usually study CSC 252 with?

**Problem 1: Fixed-Point Arithmetics (15 points + 3 points extra credit)**
**Part a) (4 points) Represent the decimal value 92 in hexadecimal.**
​

**Part b) (4 points) Represent the binary value 1110110111 in hexadecimal.**
​

**Part c) (4 points) Octal is the base-8 number system, and uses the digits 0 to 7. Represent the**
​
octal value 273 in binary.

**Part d) (3 points) Suppose the registers ​** **%esi​**, ​ **%ebx​**, and ​ **%edx​** are initialized with the values ​
shown below.

**%esi** **%ebx** **%edx (before) ​**

0xA2E058 0x800 0x0

What would the value of %edx​ be after the instruction: ​ **lea (%esi, %ebx, 8), %edx​** ? ​

|%esi|%ebx|%edx​ (before)|
|---|---|---|
|0xA2E058|0x800|0x0|


-----

**Part e) (3 points extra credit) Let A and B be two unknown 8-bit 2’s complement numbers.**
​
We know the results of A ^ B and A & B as shown below:

A ^ B 00110100

A & B 11001001

**(1 point) What is the sum A + B expressed in the 8-bit two’s complement notation?**
​

On an x86 system, would the carry flag be set after A + B? What about the overflow flag?

|A ^ B|00110100|
|---|---|
|A & B|11001001|

|Will carry flag be set? (1 point) ​|Col2|
|---|---|
|Will overflow flag be set? (1 point) ​||


-----

**Problem 2: Floating-Point Arithmetics (16 points + 2 points extra credit)**

**Part a) (4 points) Put​** 4 16[3] in binary normalized form.

**Part b) (12 points + 2 points extra credits) In this problem, we assume that IEEE decided**
​
to add a new 12-bit representation, with its main characteristics consistent with the other IEEE
standards.

In this 12-bit representation, the value 155/256 is represented exactly as 001000110110.

**(4 points) How many bits are needed for exponent?**
​

**(4 points) How many bits are needed for fraction?**
​

**(4 points) In this 12-bit representation, what is the smallest positive number that can be**
​
represented?

**(2 points extra credit) You want to calculate the sum of the following three numbers that are**
​
represented using this 12-bit floating point format: (A) 110111100100, (B) 010101110000, and
(C) 011011000000. Give an order in which the addition will generate the expected sum.


-----

**Problem 3: Logic Design (14 points)**

The following is the schematic of a NAND gate, which takes in two 1-bit inputs A​ and ​ **B​**, and ​
generates one 1-bit output Out​ . The NAND gate functions in such a way that ​ **Out = !(A & B)​** . ​

**Part a) (3 points) Now we build the following piece of combinational logic using the NAND**
​
gate, which takes in one 1-bit input A​, and generates one 1-bit output ​ **Out​** . What’s the ​
relationship between Out​ and ​ **A​** ? ​

**Part b) (11 points) We have the combinational circuit shown below with part of its logic**
​
hidden. It takes in one 1-bit input: A​, and produces one 1-bit output: ​ **Out​** . The relationship ​
between A​ and ​ **Out​** is shown in the accompanying truth table. ​

**A** **Out**

0 0

1 0

**(3 points) What is the functionality of the hidden logic in the circuit? You can denote the two**
​
inputs to the hidden logic as In1​ and ​ ​In2. ​

|A|Out|
|---|---|
|0|0|
|1|0|


-----

**(5 points) Implement the hidden logic using only NAND gates. Draw its schematic below.**
​

**(3 points) Given your above implementation and assuming the delay of a NAND gate is 1ps,**
​
what is the delay of the entire combinational circuit?


-----

**Problem 4: Assembly Programming (14 points + 6 points extra credits)**

Below is the assembly code for a mystery function in C. Assume this function takes in an
unsigned integer from 1 ~ 8 in %edi​ and returns a value to ​ **%eax​** . The function prototype is the ​
following: unsigned int mystery(unsigned int); ​

Assembly code:

0x0000000000400556 <+0>: push  %rbp

0x0000000000400557 <+1>: mov  %rsp,%rbp

0x000000000040055a <+4>: sub  $0x10,%rsp

0x000000000040055e <+8>: mov  %edi,-0x4(%rbp)

0x0000000000400561 <+11>: cmpl  $0x2,-0x4(%rbp)

0x0000000000400565 <+15>: jne  0x40056e <mystery+24>

0x0000000000400567 <+17>: mov  $0x2,%eax

0x000000000040056c <+22>: jmp  0x4005a5 <mystery+79>

0x000000000040056e <+24>: cmpl  $0x1,-0x4(%rbp)

0x0000000000400572 <+28>: jg   0x400583 <mystery+45>

0x0000000000400574 <+30>: mov  -0x4(%rbp),%eax

0x0000000000400577 <+33>: sub  $0x1,%eax

0x000000000040057a <+36>: mov  %eax,%edi

0x000000000040057c <+38>: callq 0x400556 <mystery>

0x0000000000400581 <+43>: jmp  0x4005a5 <mystery+79>

0x0000000000400583 <+45>: cmpl  $0x1,-0x4(%rbp)

0x0000000000400587 <+49>: jle  0x4005a5 <mystery+79>

0x0000000000400589 <+51>: mov  -0x4(%rbp),%eax

0x000000000040058c <+54>: sub  $0x2,%eax

0x000000000040058f <+57>: mov  %eax,%edi

0x0000000000400591 <+59>: callq 0x400556 <mystery>

0x0000000000400596 <+64>: imul  -0x4(%rbp),%eax

0x000000000040059a <+68>: mov  -0x4(%rbp),%edx

0x000000000040059d <+71>: sub  $0x1,%edx

0x00000000004005a0 <+74>: imul  %edx,%eax

0x00000000004005a3 <+77>: jmp  0x4005a5 <mystery+79>

0x00000000004005a5 <+79>: leaveq

0x00000000004005a6 <+80>: retq


-----

**Part a) (4 points) Assume 2 is stored in ​** **%edi​** at the beginning of the function execution. ​
Which lines of assembly will have been executed after the function finishes execution (denote as
function offset e.g. <+24>)?

**Part b) (5 points) This function produces integer over/underflow for some input values. What**
​
are these values? Recall that the input is an unsigned integer from 1 ~ 8 stored in %edi​ . ​

**Part c) (5 points) For the input values that do not cause integer over/underflow, what does**
​
this function return? Please express it as a closed-form function of the input (you could denote
the input as x).


-----

**Part d) (6 points extra credit)** There are some ways to modify this assembly program to
​ ​
make the function work for all input values 1 ~ 8. What is one set of 3 or fewer lines of changes
you can make? Note that deletion and replacement are valid changes, insertion is not.

Line# (denote as function offset):

Change to:

Line# (denote as function offset):

Change to:

Line# (denote as function offset):

Change to:


-----

**Problem 5: ISA and Microarchitecture (14 points + 9 points extra credits)**

Suppose you are working for a microprocessor company RoCChip. You take on the job of
designing the ISA and microarchitecture for a new computer. You want the ISA to have two
types of instructions detailed below.

The first type of instructions (Type A) has the following general format:
**Opcode Ra,Rb,Imm**

Instructions of this type operate as follows. We perform an operation between the values in
registers Ra​ and ​ **Rb​**, and store the result to the memory address specified by the immediate ​
value Imm​ . The immediate value is treated as an absolute (as opposed to relative) memory ​
address. The exact operation to be performed between Ra​ and ​ **Rb​** depends on the specific ​
Opcode. ​

The binary encoding for this type of instructions is the following. The most significant bit is
always 0, indicating that that this is a Type A instruction.

**0 Opcode** **Ra** **Rb** **Imm**

The second type of instructions (Type B) has the following general format:
**Opcode Ra,Rb,Rc**

Instructions of this type operate as follows. We perform an operation between the values in
registers Ra​ and ​ **Rb​**, and store the result to the memory address specified by value in register ​ **Rc​** . ​
Similarly, the exact operation to be performed between Ra​ and ​ **Rb​** depends on the specific ​
Opcode. ​

The binary encoding for this type of instructions is the following. The most significant bit is
always 1, indicating that that this is a Type B instruction.

**1 Opcode** **Ra** **Rb** **Rc**

You want your machine to be byte addressable (i.e., each addressable memory location is one
byte, just like x86). The total memory capacity is 2 Bytes. Each register in this machine hold 4
​[20 ][​]
bytes of data.

For each instruction type, you plan to support 8 different arithmetic and logic operations (same
8 for each type). You also have the limitation that the length of Type A instructions must be 4
bytes.

|0|Opcode|Ra|Rb|Imm|
|---|---|---|---|---|

|1|Opcode|Ra|Rb|Rc|
|---|---|---|---|---|


-----

**Part a) (3 points) What is the minimum number of bits to represent the ​** **Opcode​** field in both ​
types of instructions?

**Part b) (3 points) What is the minimum number of bits to represent the ​** **Imm​** field in Type A? ​

**Part c) (4 points) Using the number of bits for ​** **Opcode​** and ​ **Imm​** that you came up with in (a) ​
and (b), what is the maximum number registers that your ISA can support?

**Part d) (4 points) Assume that we have a program with 1000 instructions. 20% of them are of**
​
Type A, and 80% of Type B. How much space in the memory is occupied by this program?

**Part e) (9 points extra credit)** Now that you finish designing the ISA, you start working on
​ ​
the microarchitecture, which only has to support the two types of instructions. Below is the
partially complete schematic of the microarchitecture.

The “Address” port of the memory takes the memory address to be written to, and the “Data”
port of the memory takes the data to be written to the memory.

The register file has three read ports and can read three registers, Ra​, ​ **Rb​**, and ​ **Rc​** ​,
simultaneously. How the three Read Reg. IDs are generated is irrelevant to this problem.

There are three hidden logics in this partially complete microarchitecture. You job: determine
the functionalities of the three hidden logics. Note that not all the input signals to the logics are
shown. You need to figure out what signals each logic needs.


-----

**(3 points)** Logic 1 generates the select signal to the MUX that produces the memory address.
​ ​
Briefly explain how Logic 1 generates the select signal.

**(3 points)​** Logic 2 takes the value of ​ **Rc​** and generates one of the two pieces of data that go into ​
the MUX. Briefly explain how Logic 2 generates its output.


-----

**(3 points)** Logic 3 generates the next PC (nPC), which contains the address of the next
​ ​
instruction to be fetched and executed. Briefly explain how Logic 3 generates nPC.


-----

###### Final Exam

**CSC 252**

**8 May 2018**

**Computer Science Department**

**University of Rochester**

Instructor: Yuhao Zhu
TAs: Alan Beadle, Sayak Chakraborti, Michael Chavrimootoo, Alan Chiu,
Akshay Desai, Benjamin Nemeth, Eric Weiss, Jie Zhou

Name:____________________________________

Problem 0 (2 points):    ______________
Problem 1 (43 points):   ______________
Problem 2 (15 points):   ______________
Problem 3 (30 points):   ______________
Problem 4 (30 points):   ______________
Problem 5 (15 points):   ______________
Total (135 points):       ______________

Remember “I don’t know” is given 15% partial credit, but you must erase/cross everything else.

Please be sure your name is on each sheet of the exam.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 2 hours and 45 minutes to work (19:15 -- 22:00).

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:___________________________________________________________

**GOOD LUCK!!!**

**(And Have a Great Semester Break)**

1


-----

**Problem 0: Warm-up (2 points)**

Facebook is hiring hardware engineers. What do you think they are building?

Any answer is accepted.

**Problem 1 (43 points)**

**Part a (5 points): A microarchitecture is predicting whether a branch is taken or not taken**
​
using a 1-bit predictor. The last five branches were: taken, taken, taken, taken, not taken. What
does the branch predictor predict (choose): Taken or Not Taken?

Not Taken

**Part b (5 points): In a typical Linux/Unix terminal, when you hit Ctrl + Z, which state are you**
​
putting the foreground process to (choose): Running, Stopped, Terminated?

Stopped

**Part c (5 points): Cache blocking is a software-level performance optimization technique that**
​
improves what aspect of a program (choose): Locality, Parallelism, Concurrency, Security?

Locality

**Part d (5 points): An application that is 90% parallelizable is executed on a single processor in**
​
1.5 hours. If the application is allowed to run with an unlimited number of processors, what is
the lower bound on its execution time?

9 mins. With an unlimited number of processors, the parallelizable part of a program
​
would finish in no time, and the execution time is equivalent to the sequential part, which
is 90 mins * 0.1 = 9 mins.

**Part e (5 points): On a page fault, the operating system often loads a page from the disk into**
​
memory. How does the operating system know whether it is necessary to write the previously
occupied page in the memory back to the disk? Answer in fifteen words or fewer.

Check the dirty bit in the corresponding page table entry.

2


-----

**Part f (5 points): What is the cycle time of a 1 GHz processor?**
​

1 ns

**Part g (5 points): What is the fundamental reason that process context switch has a much**
​
higher overhead than thread context switch in Linux? Answer in twenty words or fewer.

Threads share virtual address space while processes have separate virtual address spaces.

**Part h (5 points): Suppose we have two 4-bit 2’s complement numbers:**
​

1111

1110

Does the sum of the two numbers result in an overflow?

No.

**Part i (3 points):Recall that the crux of tracing-based GC algorithms such as Mark-and-sweep**
​
and Mark-sweep-compact is to start from “root” variables and then identify all the reachable
variables. In the following code snippet, suppose the program just finishes executing L7, which
variables are regarded as “root”? Name only those that point to variables on the heap.

L1:  int *p3; ​

L2:  int* foo(int n) { ​
L3:   int i, *p1; ​
L4:   p1 = (int *) malloc(n * sizeof(int)); ​
L5:   for (i=0; i<n; i++) ​
L6:    p1[i] = i; ​
L7:   p3 = p1[2]; ​
L8:   return p1; ​
L9:  } ​

L10:  void bar() { ​
L11:   int *p2 = foo(5); ​
L12:  } ​

p1 and ​ p3​ . ​

3


-----

**Problem 2 (15 points)**

We assume that IEEE decided to add a new 8-bit representation with its main characteristics
consistent with the 32/64-bit representations. Consider the following four 8-bit numbers:

A: 11100101 ​
B: 00111001 ​
C: 00001100 ​
D: 00011101​

The decimal values represented by the above numbers are as follows, in no particular order:
​ ​

1 29 3

###### 3, -21,,
8 32 8

3
**Part a (3 points): Represent decimal value** in binary normalized form
​ 8

1.1 x 2^-2

**Part b (3 points): Which 8-bit floating point number represents -21 (choose from A, B, C, D)?**
​

A

29
**Part c (3 points): Which 8-bit floating point number represents** (choose from A, B, C, D)?
​ 32

D

**Part d (6 points): Given the above information, figure out the following:**
​
**(2 points) Number of bits needed for exponent:**
​

3

**(2 points) Number of bits needed for fraction:**
​

4

**(2 points) Bias:**
​

3

4


-----

order bits are

the same but


**Problem 3 (30 points)**

A byte-addressable, write-back cache of fixed total size and fixed cache line (a.k.a., block) size is
​ ​ ​ ​
implemented as both a direct mapped cache and also as an N-way set-associative cache. In both
cases, we will assume the cache is initially empty.

First, consider the cache organized as a direct mapped cache. The following sequence of 11
accesses generates the hits/misses shown. Some miss/hit entries are intentionally left blank.

**Address** **Read/** **Direct Mapped** - The hit must be because of the first
**Write** **(Hit/Miss)**

###### access because only the first address

0100001010 R has the same high order bits as the hit

###### address.

1100100111 R Miss - Comparing the hit address and the

###### first address, we know that offset is at

1110101000 R Miss

###### least 3 bits.

0011000101 R - From the last two misses we that the

Hit because offset is at most 4 bits.

of this miss

0110111100 R - The miss immediately before the hit

###### and the second miss have the same

1010110101 R Miss

###### first 7 bits. So there must be an access

1100100000 R Miss in-between that evicts the line brought

###### in by the second miss.

0100001111 R Hit - There also could not be a miss that

###### evicts the line brought in by the first

0101111111 W Miss

###### miss for the hit to be a hit.

0110110100 R - All these could only be possible if

###### offset is 4, index is 3.

0110100101 R Miss

**Part a (4 points): How many cache lines does each set have in a direct mapped cache?**
​

1

**Part b (2 points): What is the cache line (a.k.a., block) size?**
​

16 Bytes

**Part c (2 points): What are the number of index bits for the direct mapped cache?**
​

3

5

|Address|Read/ Write|Direct Mapped (Hit/Miss)|
|---|---|---|
|0100001010|R||
|1100100111|R|Miss|
|1110101000|R|Miss|
|0011000101|R||
|0110111100|R||
|1010110101|R|Miss|
|1100100000|R|Miss|
|0100001111|R|Hit|
|0101111111|W|Miss|
|0110110100|R||
|0110100101|R|Miss|


-----

Now consider the cache organized as a N-way set-associative cache, with the same total size and
same cache line size as before. The total size of “overhead” for this N-way set associative cache is
112 bits. Assume that in this particular cache, overhead in each cache line includes tag bits and
​ ​
10 additional bits for bookkeeping (e.g., the valid bit, modified bit, LRU bits) that do not affect
this problem. We have expanded the table to show the hit/misses for the same sequence of
accesses when the cache is organized as an N-way set-associative cache.

**Address** **Read/** **Direct Mapped** **N-way associative**
**Write** **(Hit/Miss)** **(Miss/Hit)**         - T bits for tag, I bits for set index; we

have (10+T) * 2^I * N = 112

0100001010 R **Miss** **Miss** - Since the cache line size is the same

as before, the offset must be 4, and so

1100100111 R Miss Miss we have T + I = 10 - 4 = 6.

                                 - 10<=10+T<=16. only 14 and 16 are

1110101000 R Miss **Miss** divisible by 112. So T is either 4 or 6.

                                        - If T is 6, then 2^I * N = 7, so I = 0 and

0011000101 R **Miss** Miss N = 7. If T is 4 then 2^I * N = 8, so I = 2

and N = 2 or I = 1 and N = 4.

0110111100 R **Miss** Miss - Since the total size is fixed and the

cache line size is fixed, the total number

1010110101 R Miss **Miss**

of cache lines 2^I * N must be 8, same
as before.

1100100000 R Miss **Hit**

                                   - So I must be 2 and N must be 2.

0100001111 R Hit **Hit**

0101111111 W Miss Miss

0110110100 R **Miss** Hit

0110100101 R Miss **Miss**

**Part d (4 points): What is N?**
​

2

**Part e (4 points): What is the number of index bits for the N-Way set associative cache?**
​

2

**Part f (4 points): Is this a write-allocate cache?**
​

No

**Part g (10 points; 1 point per blank): Please complete the second table above by filling in**
​
”Hit” or ”Miss” for each of the blank entries. “I Don’t Know” is accepted on a per blank basis.

6

|Address|Read/ Write|Direct Mapped (Hit/Miss)|N-way associative (Miss/Hit)|
|---|---|---|---|
|0100001010|R|Miss|Miss|
|1100100111|R|Miss|Miss|
|1110101000|R|Miss|Miss|
|0011000101|R|Miss|Miss|
|0110111100|R|Miss|Miss|
|1010110101|R|Miss|Miss|
|1100100000|R|Miss|Hit|
|0100001111|R|Hit|Hit|
|0101111111|W|Miss|Miss|
|0110110100|R|Miss|Hit|
|0110100101|R|Miss|Miss|


-----

**Problem 4 (30 points)**

We wish to enhance the x86 ISA by adding a new instruction. The new instruction is called STI​, ​
“Store Indirect”, and its format is:

STI Ra,Rb,Offset

The opcode of STI​ is 1010, and its binary encoding is (2-Byte long): ​

Opcode <4-bit> Ra <3-bit> Rb <3-bit> Offset <6-bit>
​ ​ ​ ​

STI operates as follows: We compute a virtual address (call it ​ A​ ) by adding the sign-extended ​
Offset to the contents of register ​ Rb​ . The memory location specified by ​ A​ contains the virtual ​
address B​ . We wish to store the contents of register ​ Ra​ into the address specified by ​ B​ . ​

The processor has a simple one-level virtual memory system. There is also a 2-entry TLB. You
are given the following information:

  - Virtual Address Space: 64 KB

  - Physical Memory Size: 4 KB

  - PTE Size: 2 Bytes

  - The format of a PTE is shown below. The MSB is the valid bit, and the lower several bits
are for the physical page number (PPN). Note that the exact number of bits for PPN is for
you to determine. The rest bits are always padded with 0.

Valid <1-bit> 0...0 Physical Page Number
​

  - %eax: 0x8000 ​

  - %ebx: 0x401E ​

  - Program Counter (%eip​ ): 0x3048 ​

The TLB state before any instructions related to this problem are executed:

Valid Virtual Page Number PTE

(VPN)

Valid Physical Page Number (PPN)

1 0x0C1 0000 1100 0001 1 0x01A

1 0x182 0001 1000 0010 1 0x024

7

|Opcode <4-bit> ​|Ra <3-bit> ​|Rb <3-bit> ​|Offset <6-bit> ​|
|---|---|---|---|

|Valid <1-bit> ​|0...0|Physical Page Number|
|---|---|---|

|Valid|Virtual Page Number (VPN)|PTE|Col4|
|---|---|---|---|
|||Valid|Physical Page Number (PPN)|
|1|0x0C1 0000 1100 0001|1|0x01A|
|1|0x182 0001 1000 0010|1|0x024|


-----

Fetch Inst.

Get PTE for A

Load from A

Get PTE for B

Write to B


**Part a (2 points): In this particular TLB, the Valid bit in the first column and the Valid bit in**
​
the third column are the same in both TLB entries. In general, is it possible that these two valid
bits have different values?

Yes

**Part b (6 points): What is binary encoding for ​** STI %eax,%ebx,0​ ? Assume that ​ %eax​ is ​
encoded as 0 and %ebx​ is encoded as 1. ​

1010 000 001 000000

**Part c (4 points): To process the ​** STI​ instruction, one must go through the Fetch, Decode, etc. ​
instruction cycle. What is the maximum number of physical addresses that can be accessed in
processing an STI​ instruction? ​

Hints:

1. Instruction fetch is the necessary first step in processing any instruction

2. In the one-level virtual memory system, the page table lives in the physical memory

This instruction accesses virtual memory three times:
fetch instruction, load from address A, and store to

6 address B. Each virtual memory access could at most

lead to 2 physical memory accesses: one for accessing
the PTE and the other for accessing the actual data.

**Part d (18 points): Now the processor executes ​** STI %eax,%ebx,0​ . It turned out that five ​
physical memory accesses were needed. The table below shows the Virtual Address (VA),
Physical Address (PA), Data, and whether or not there was a TLB hit for each of these five
physical memory accesses in the order they occurred. Some of the blanks are intentionally left
for you to fill in.

**Virtual Address** **Physical Address** **Data** **TLB Hit?**

0x3048 PC 0x4880x480 0xA040 Yes

**N/A** **0x660** **0x8040** No

0x401E %ebx (A) 0x81E **0x40FE** B No

**N/A** 0x66E 0x8040 0x800E No

0x40FE **0x1DE** 0x8000 %eax No

Complete the table and fill in the following three boxes. You can assume that no page faults
occurred.

8

|Virtual Address|Physical Address|Data|TLB Hit?|
|---|---|---|---|
|0x3048 PC|00xx448880|0xA040|Yes|
|N/A|0x660|0x8040|No|
|0x401E %ebx (A)|0x81E|0x40FE B|No|
|N/A|0x66E|00xx880004E0|No|
|0x40FE|0x1DE|0x8000 %eax|No|


-----

Hints:

1. What does the first TLB hit mean?

2. Recall how to use PTBR and VPN to access the page table.

3. Use the first and last accesses to figure out the page size first. Everything else will follow.

**(3 points): What is the page size?**
​

32 Bytes

**(3 points): What is the total number of physical pages?**
​

128

**(3 points): What is the data in the page table base register (PTBR)?**
​

0x260

**(9 points; 1 point per blank): Please complete the table above. “I Don’t Know” is accepted**
​
on a per blank basis.

- The first virtual memory access must be to fetch the instruction, so the first VA must be the PC, which is 0x3048.

- The first access is a TLB hit. Analyzing the VA and the two TLB entires, you would know that the page offset must
be either 5 or 6.

0x0C1:  0000 1100 0001
0x182:  0001 1000 0010
0x3048: 0011 0000 0100 1000

- The second access must be to get the PTE of virtual address A, which returns 0x8040 as the PTE. Using the PTE,
we form the physical address, which the third access uses to get the data 0x40FE, which is essentially B.

- The fourth access must be then to get the PTE of virtual address B and form its physical address, which is 0x1DE.
The fifth access must be to store %eax to 0x1DE (corresponding to virtual address B). So its VA must be 0x40FE,
same as the data returned from the third access. The data in the fifth access is 0x8000 (i.e., %eax).

- Focus on the last access. We know its VA is 0x40FE and the PA is 0x1DE. Their page offsets must match.
Analyzing the two address, we know the page offset must be 5 bits rather than 6.

0x1DE:      0001 1101 1110
0x40FE: 0100 0000 1111 1110

- If the page offset is 5 bits, we could easily get that the physical page number is 12-5=7 bits since the total physical
memory size is 4K = 2^12.

- Given the 5 bits page offset, we could also easily get know that the TLB hit in the first access hits on the second
TLB entry, which allows us to form the physical addresses of the first and the third access, which are 0x480 and
0x81E, respectively.

- To get the PTBR value, focus on the second physical address, which is calculated by PTBR + VPN * 2. Since we
know the page offset is 5, we would know that VPN in that access is 0x200, and so we can get the PTBR = 0x260.

- Given the PTBR, we could also get the physical address of the fourth access, which is PTBR + VPN * 2 = 0x66E.

9


-----

**Problem 5 (15 points)**

A programmer writes the following two C code segments. She wants to run them concurrently
on a multicore processor, called SC, using two different threads, each of which will run on a
different core.

Thread T1 ​
a = X[0];
b = a + Y[0]; Infinite loop until flag becomes 1,
while(*flag == 0); at which point Y[0] must be 1. So
Y[0] += 1; in the end Y[0] could only be 2.

Thread T2 ​
Y[0] = 1;
*flag = 1;
X[1] *= 2;
a = 0;

X, ​ Y​, and ​ flag​ have been allocated in main memory, while ​ a​ and ​ b​ are contained in the ​
processor registers. A read or write to any of these variables generates a single memory request.
The initial values of all memory locations and variables are 0. Assume each line of the C code
segment of each thread translates to a single machine instruction.

**Part a (5 points): Both threads have a variable ​** a​ . Are they referring to the same variable? ​

No

**Part b (5 points): What are the possible final value(s) of ​** Y[0]​ after both threads finish ​
execution? Consider all the possible thread interleavings.

2

**Part c (5 points): What are the possible final value(s) of ​** b​ after both threads finish execution? ​
Consider all the possible thread interleavings.

0 and 1

10


-----

###### Final Exam

**CSC 252**

**8 May 2018**

**Computer Science Department**

**University of Rochester**

Instructor: Yuhao Zhu
TAs: Alan Beadle, Sayak Chakraborti, Michael Chavrimootoo, Alan Chiu,
Akshay Desai, Benjamin Nemeth, Eric Weiss, Jie Zhou

Name:____________________________________

Problem 0 (2 points):    ______________
Problem 1 (43 points):   ______________
Problem 2 (15 points):   ______________
Problem 3 (30 points):   ______________
Problem 4 (30 points):   ______________
Problem 5 (15 points):   ______________
Total (135 points):       ______________

Remember “I don’t know” is given 15% partial credit, but you must erase/cross everything else.

Please be sure your name is on each sheet of the exam.

Your answers to all questions must be contained in the given boxes. Use spare space to show all
supporting work to earn partial credit.

You have 2 hours and 45 minutes to work (19:15 -- 22:00).

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:___________________________________________________________

**GOOD LUCK!!!**

**(And Have a Great Semester Break)**

1


-----

**Problem 0: Warm-up (2 points)**

Facebook is hiring hardware engineers. What do you think they are building?

**Problem 1 (43 points)**

**Part a (5 points): A microarchitecture is predicting whether a branch is taken or not taken**
​
using a 1-bit predictor. The last five branches were: taken, taken, taken, taken, not taken. What
does the branch predictor predict (choose): Taken or Not Taken?

**Part b (5 points): In a typical Linux/Unix terminal, when you hit Ctrl + Z, which state are you**
​
putting the foreground process to (choose): Running, Stopped, Terminated?

**Part c (5 points): Cache blocking is a software-level performance optimization technique that**
​
improves what aspect of a program (choose): Locality, Parallelism, Concurrency, Security?

**Part d (5 points): An application that is 90% parallelizable is executed on a single processor in**
​
1.5 hours. If the application is allowed to run with an unlimited number of processors, what is
the lower bound on its execution time?

**Part e (5 points): On a page fault, the operating system often loads a page from the disk into**
​
memory. How does the operating system know whether it is necessary to write the previously
occupied page in the memory back to the disk? Answer in fifteen words or fewer.

2


-----

**Part f (5 points): What is the cycle time of a 1 GHz processor?**
​

**Part g (5 points): What is the fundamental reason that process context switch has a much**
​
higher overhead than thread context switch in Linux? Answer in twenty words or fewer.

**Part h (5 points): Suppose we have two 4-bit 2’s complement numbers:**
​

1111

1110

Does the sum of the two numbers result in an overflow?

**Part i (3 points):Recall that the crux of tracing-based GC algorithms such as Mark-and-sweep**
​
and Mark-sweep-compact is to start from “root” variables and then identify all the reachable
variables. In the following code snippet, suppose the program just finishes executing L7, which
variables are regarded as “root”? Name only those that point to variables on the heap.

L1:  int *p3; ​

L2:  int* foo(int n) { ​
L3:   int i, *p1; ​
L4:   p1 = (int *) malloc(n * sizeof(int)); ​
L5:   for (i=0; i<n; i++) ​
L6:    p1[i] = i; ​
L7:   p3 = p1[2]; ​
L8:   return p1; ​
L9:  } ​

L10:  void bar() { ​
L11:   int *p2 = foo(5); ​
L12:  } ​

3


-----

**Problem 2 (15 points)**

We assume that IEEE decided to add a new 8-bit representation with its main characteristics
consistent with the 32/64-bit representations. Consider the following four 8-bit numbers:

A: 11100101 ​
B: 00111001 ​
C: 00001100 ​
D: 00011101​

The decimal values represented by the above numbers are as follows, in no particular order:
​ ​

1 29 3

###### 3, -21,,
8 32 8

3
**Part a (3 points): Represent decimal value** in binary normalized form
​ 8

**Part b (3 points): Which 8-bit floating point number represents -21 (choose from A, B, C, D)?**
​

29
**Part c (3 points): Which 8-bit floating point number represents** (choose from A, B, C, D)?
​ 32

**Part d (6 points): Given the above information, figure out the following:**
​
**(2 points) Number of bits needed for exponent:**
​

**(2 points) Number of bits needed for fraction:**
​

**(2 points) Bias:**
​

4


-----

**Problem 3 (30 points)**

A byte-addressable, write-back cache of fixed total size and fixed cache line (a.k.a., block) size is
​ ​ ​ ​
implemented as both a direct mapped cache and also as an N-way set-associative cache. In both
cases, we will assume the cache is initially empty.

First, consider the cache organized as a direct mapped cache. The following sequence of 11
accesses generates the hits/misses shown. Some miss/hit entries are intentionally left blank.

**Address** **Read/Write** **Direct Mapped (Hit/Miss)**

0100001010 R

1100100111 R Miss

1110101000 R Miss

0011000101 R

0110111100 R

1010110101 R Miss

1100100000 R Miss

0100001111 R Hit

0101111111 W Miss

0110110100 R

0110100101 R Miss

**Part a (4 points): How many cache lines does each set have in a direct mapped cache?**
​

**Part b (2 points): What is the cache line (a.k.a., block) size?**
​

**Part c (2 points): What are the number of index bits for the direct mapped cache?**
​

5

|Address|Read/Write|Direct Mapped (Hit/Miss)|
|---|---|---|
|0100001010|R||
|1100100111|R|Miss|
|1110101000|R|Miss|
|0011000101|R||
|0110111100|R||
|1010110101|R|Miss|
|1100100000|R|Miss|
|0100001111|R|Hit|
|0101111111|W|Miss|
|0110110100|R||
|0110100101|R|Miss|


-----

Now consider the cache organized as a N-way set-associative cache, with the same total size and
same cache line size as before. The total size of “overhead” for this N-way set associative cache is
112 bits. Assume that in this particular cache, overhead in each cache line includes tag bits and
​ ​
10 additional bits for bookkeeping (e.g., the valid bit, modified bit, LRU bits) that do not affect
this problem. We have expanded the table to show the hit/misses for the same sequence of
accesses when the cache is organized as an N-way set-associative cache.

**Address** **Read/Write** **Direct Mapped (Hit/Miss)** **N-way associative (Miss/Hit)**

0100001010 R

1100100111 R Miss Miss

1110101000 R Miss

0011000101 R Miss

0110111100 R Miss

1010110101 R Miss

1100100000 R Miss

0100001111 R Hit

0101111111 W Miss Miss

0110110100 R Hit

0110100101 R Miss

**Part d (4 points): What is N?**
​

**Part e (4 points): What is the number of index bits for the N-Way set associative cache?**
​

**Part f (4 points): Is this a write-allocate cache?**
​

**Part g (10 points; 1 point per blank): Please complete the second table above by filling in**
​
”Hit” or ”Miss” for each of the blank entries. “I Don’t Know” is accepted on a per blank basis.

6

|Address|Read/Write|Direct Mapped (Hit/Miss)|N-way associative (Miss/Hit)|
|---|---|---|---|
|0100001010|R|||
|1100100111|R|Miss|Miss|
|1110101000|R|Miss||
|0011000101|R||Miss|
|0110111100|R||Miss|
|1010110101|R|Miss||
|1100100000|R|Miss||
|0100001111|R|Hit||
|0101111111|W|Miss|Miss|
|0110110100|R||Hit|
|0110100101|R|Miss||


-----

**Problem 4 (30 points)**

We wish to enhance the x86 ISA by adding a new instruction. The new instruction is called STI​, ​
“Store Indirect”, and its format is:

STI Ra,Rb,Offset

The opcode of STI​ is 1010, and its binary encoding is (2-Byte long): ​

Opcode <4-bit> Ra <3-bit> Rb <3-bit> Offset <6-bit>
​ ​ ​ ​

STI operates as follows: We compute a virtual address (call it ​ A​ ) by adding the sign-extended ​
Offset to the contents of register ​ Rb​ . The memory location specified by ​ A​ contains the virtual ​
address B​ . We wish to store the contents of register ​ Ra​ into the address specified by ​ B​ . ​

The processor has a simple one-level virtual memory system. There is also a 2-entry TLB. You
are given the following information:

  - Virtual Address Space: 64 KB

  - Physical Memory Size: 4 KB

  - PTE Size: 2 Bytes

  - The format of a PTE is shown below. The MSB is the valid bit, and the lower several bits
are for the physical page number (PPN). Note that the exact number of bits for PPN is for
you to determine. The rest bits are always padded with 0.

Valid <1-bit> 0...0 Physical Page Number
​

  - %eax: 0x8000 ​

  - %ebx: 0x401E ​

  - Program Counter (%eip​ ): 0x3048 ​

The TLB state before any instructions related to this problem are executed:

Valid Virtual Page Number PTE

(VPN)

Valid Physical Page Number (PPN)

1 0x0C1 1 0x01A

1 0x182 1 0x024

7

|Opcode <4-bit> ​|Ra <3-bit> ​|Rb <3-bit> ​|Offset <6-bit> ​|
|---|---|---|---|

|Valid <1-bit> ​|0...0|Physical Page Number|
|---|---|---|

|Valid|Virtual Page Number (VPN)|PTE|Col4|
|---|---|---|---|
|||Valid|Physical Page Number (PPN)|
|1|0x0C1|1|0x01A|
|1|0x182|1|0x024|


-----

**Part a (2 points): In this particular TLB, the Valid bit in the first column and the Valid bit in**
​
the third column are the same in both TLB entries. In general, is it possible that these two valid
bits have different values?

**Part b (6 points): What is binary encoding for ​** STI %eax,%ebx,0​ ? Assume that ​ %eax​ is ​
encoded as 0 and %ebx​ is encoded as 1. ​

**Part c (4 points): To process the ​** STI​ instruction, one must go through the Fetch, Decode, etc. ​
instruction cycle. What is the maximum number of physical addresses that can be accessed in
processing an STI​ instruction? ​

Hints:

1. Instruction fetch is the necessary first step in processing any instruction

2. In the one-level virtual memory system, the page table lives in the physical memory

**Part d (18 points): Now the processor executes ​** STI %eax,%ebx,0​ . It turned out that five ​
physical memory accesses were needed. The table below shows the Virtual Address (VA),
Physical Address (PA), Data, and whether or not there was a TLB hit for each of these five
physical memory accesses in the order they occurred. Some of the blanks are intentionally left
for you to fill in.

**Virtual Address** **Physical Address** **Data** **TLB Hit?**

Yes

**N/A** **0x660** **0x8040** No

**0x40FE** No

**N/A** No

**0x1DE** No

Complete the table and fill in the following three boxes. You can assume that no page faults
occurred.

8

|Virtual Address|Physical Address|Data|TLB Hit?|
|---|---|---|---|
||||Yes|
|N/A|0x660|0x8040|No|
|||0x40FE|No|
|N/A|||No|
||0x1DE||No|


-----

Hints:

1. What does the first TLB hit mean?

2. Recall how to use PTBR and VPN to access the page table.

3. Use the first and last accesses to figure out the page size first. Everything else will follow.

**(3 points): What is the page size?**
​

**(3 points): What is the total number of physical pages?**
​

**(3 points): What is the data in the page table base register (PTBR)?**
​

**(9 points; 1 point per blank): Please complete the table above. “I Don’t Know” is accepted**
​
on a per blank basis.

9


-----

**Problem 5 (15 points)**

A programmer writes the following two C code segments. She wants to run them concurrently
on a multicore processor, called SC, using two different threads, each of which will run on a
different core.

Thread T1 ​
a = X[0];
b = a + Y[0];
while(*flag == 0);
Y[0] += 1;

Thread T2 ​
Y[0] = 1;
*flag = 1;
X[1] *= 2;
a = 0;

X, ​ Y​, and ​ flag​ have been allocated in main memory, while ​ a​ and ​ b​ are contained in the ​
processor registers. A read or write to any of these variables generates a single memory request.
The initial values of all memory locations and variables are 0. Assume each line of the C code
segment of each thread translates to a single machine instruction.

**Part a (5 points): Both threads have a variable ​** a​ . Are they referring to the same variable? ​

**Part b (5 points): What are the possible final value(s) of ​** Y[0]​ after both threads finish ​
execution? Consider all the possible thread interleavings.

**Part c (5 points): What are the possible final value(s) of ​** b​ after both threads finish execution? ​
Consider all the possible thread interleavings.

10


-----

###### Midterm Exam csc 252

**8March2018**
**Computer Science Department**

**University of Rochester**

###### Instructor: Yuhao Zhu
 TAs: Alan Beadle, Sayak Chakraborti, Michael Chavrimootoo, Alan Chiu, Akshay Desai, Ben[j]amin Nemeth, Eric Weiss, Jie Zhou

 Name:_...:..�' '-"['O]'-'[Lw]=---_[J][_][�][_][�][_][, \ ][___________ ]_

 Problem o (2 point): Problem 1 (12 points): Problem 2 (14 points): I q;
 Problem [3 ](14 points): Problem [4 ](20 points): Problem 5 (16 points): Problem 6 (22 points): Total (100 points): ( oo

 Remember "I don't know" is given 1[5]% partial credit, but you must erase[/]cross everything else.

 Please be sure your name is on each sheet of the exam.

 Your answers to all [q]uestions [(]and all supporting work[) ]must be contained in the given boxes.

 You have [7]5 minutes to work.

 Please sign the followin[g]. I have not given nor received any unauthorized help on this exam.

 Signature: ______________________________ _

**GOOD LUCK!!!**

1


-----

###### Problem o: Warm-up (2 points).

 Do you think Facebook will start making their own phones?

 Problem 1 (12 points. Suggeste time: 10 mins)

 Part a (3 points): Represent decimal value 66 in hexadecimal.
## I 4-Y I

###### Part b (3 points): Represent hexadecimal value oxu in binary

 I [ooc>/ I

 Part c (3 points): Octal is the base-8 number system, and uses the digits o to 7. Represent binary number 11110000 in octal.
 6,,
## I �

###### Part d (3 points): Suppose we have two 16-bit 2's complement numbers:

**0lXlX0XlXX000XXX**

**lO0XXXX00XXX0Xl0**

###### where some of the bits have not been identified, and they are represented by x.

 Could the sum of these two numbers possibly result in an overflow? If yes, give an example. If no, please explain.

**2**


-----

###### Problem 2 {14 points. Suggested time: 10 mins)

 Part a (6 points): Express the two floating point numbers 2� and� in fnary normalized

�

###### {3 points) 2 � in binary normalized form is:

 l - [0 ]q \\ "/.. 2 \

 (3 points)½ in binary normalized form is:

 Part b (4 points): As you know IEEE floating point standard has a 32-bit representation and a 64-bit representation. f v)
### &

###### {2 points) What is the bias used in the 32-bit representation? �; \ %f I j� ]

 L?,)
## I I

###### (2 points) What is the minimum gap between two representable subnormal numbers in the 32-bit representation?
##### .)
## I

###### Part c {4 points): In this problem, we assume that IEEE decided to add a new 10-bit representation, with its main characteristics consistent with the other two representations.

 In this 10-bit representation, the value 33/256 is represented exactly
 as <lg_1000�[0.9J. Your job: ]
 decide the number of bits needed for the exponent and for the fraction. +' � i;

**(2 points) Number of bits needed for exponent:** ),j� :rb        - _2 l--7;f 6 -- + ,�b '_ ).--} t2- _-o_

.-- 0 [.o., ][I ][�ooo ] [I ]

## I 4 I

###### (2 points) Number of bits needed for fraction:
 -- [ , Y.)O o l y 2.,-)

# I >


-----

-----

-----

-----

-----

-----

-----

-----

###### Midterm Exam

**CSC 252**

**8 March 2018**

**Computer Science Department**

**University of Rochester**

Instructor: Yuhao Zhu
TAs: Alan Beadle, Sayak Chakraborti, Michael Chavrimootoo, Alan Chiu,
Akshay Desai, Benjamin Nemeth, Eric Weiss, Jie Zhou

Name:____________________________________

Problem 0 (2 point):     ______________
Problem 1 (12 points):   ______________
Problem 2 (14 points):   ______________
Problem 3 (14 points):   ______________
Problem 4 (20 points):   ______________
Problem 5 (16 points):   ______________
Problem 6 (22 points):   ______________
Total (100 points):      ______________

Remember “I don’t know” is given 15% partial credit, but you must erase/cross everything else.

Please be sure your name is on each sheet of the exam.

Your answers to all questions (and all supporting work) must be contained in the given boxes.

You have 75 minutes to work.

Please sign the following. I have not given nor received any unauthorized help on this exam.

Signature:___________________________________________________________

**GOOD LUCK!!!**

1


-----

**Problem 0: Warm-up (2 points).**

Do you think Facebook will start making their own phones?

**Problem 1 (12 points. Suggested time: 10 mins)**

**Part a (3 points): Represent decimal value 66 in hexadecimal.**
​

**Part b (3 points): Represent hexadecimal value 0x11 in binary**
​

**Part c (3 points): Octal is the base-8 number system, and uses the digits 0 to 7. Represent**
​
binary number 11110000 in octal.

**Part d (3 points): Suppose we have two 16-bit 2’s complement numbers:**
​

01x1x0x1xx000xxx

100xxxx00xxx0x10

where some of the bits have not been identified, and they are represented by x.

Could the sum of these two numbers possibly result in an overflow? If yes, give an example. If
no, please explain.


2


-----

**Problem 2 (14 points. Suggested time: 10 mins)**

**Part a (6 points): Express the two floating point numbers ​** 2 1615 and 81 in binary normalized

form.

15
**(3 points)** 2 in binary normalized form is:
16

1
**(3 points)** in binary normalized form is:
8

**Part b (4 points): As you know IEEE floating point standard has a 32-bit representation and a**
​
64-bit representation.

**(2 points) What is the bias used in the 32-bit representation?**
​

**(2 points) What is the minimum gap between two representable subnormal numbers in the**
​
32-bit representation?

**Part c (4 points): In this problem, we assume that IEEE decided to add a new 10-bit**
​
representation, with its main characteristics consistent with the other two representations.

In this 10-bit representation, the value 33/256 is represented exactly as 0010000001. Your
job: decide the number of bits needed for the exponent and for the fraction.

**(2 points) Number of bits needed for exponent:**
​

**(2 points) Number of bits needed for fraction:**
​

3


-----

**Problem 3 (14 points. Suggested time: 5 mins)**

**Part a (6 points): Logic operations**
​
**(3 point) What is the result of bit-wise AND between 0101 and 1010?**
​

**(3 point) What is the result of bit-wise XOR between 0101 and 1010?**
​

**Part b (8 points): The combinational circuit with three logic gates shown below takes in three**
​
1-bit inputs: A, B, and C, and produces one 1-bit output: Out. The relationship between A, B, C,
​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​ ​
and Out is shown in the accompanying table, where the outputs for two of the input
​ ​
combinations are not specified (Out 1, Out 2). One of the logic gates in the circuit is already
identified as an AND gate.

You job: complete the two missing gates in the combinational logic as well as the two missing
outputs in the table. You can assume that the two missing gates will be either an AND gate or an
OR gate.

**(2 points) Gate 1:                                (2 points) Gate 2:**
​ ​ ​

**(2 points) Out 1:                                 (2 points) Out 2:**
​ ​ ​

4


-----

**Problem 4 (20 points. Suggested time: 15 mins)**

**Part a (6 points): Name three instructions that have zero operand, one operand, and two**
​
operands, respectively.

**(2 points) zero-operand instruction:**
​

**(2 points) one-operand instruction:**
​

**(2 points) two-operand instruction:**
​

**Part b (5 points): Consider the following C declaration of an array of struct, assuming that the**
​
address of variable A is 0x8000 and that this program is executed on a 64-bit machine.

struct S {
int i;
double v;
char j;
} A[10][10];

What is the address of A[2][3].j?

**Part c (9 points): The following assembly program adds the absolute value of a signed integer**
​
stored in memory location 0x4000 to the absolute value of another signed integer stored in
memory location 0x4004, and stores the sum to memory location 0x4008. Complete the three
missing instructions.

Hint: This problem might test you on the following things:

  - Register saving convention

  - Control transfer

  - Data movement

5


-----

.func
movq $0x4000, %rbx
movq (%rbx), %rdi
call .abs

movq $0x4004, %rbx
movq (%rbx), %rdi

call .abs
popq %rdx
addq %rdx, %rax
movq $0x4008, %rbx
movq %rax, (%rbx)
halt

.abs
movq $0x0, %rdx
addq %rdx, %rdi

.skip
negq %rdi
.done
movq %rdi, %rax
ret


**(3 points)**
​

**(3 points)**
​

**(3 points)**
​


6


-----

**Problem 5 (16 points. Suggested time: 15 mins)**

**Part a (4 points): (Fill in the blanks) Recall that the instruction cycle in the sequential**
​
implementation of a processor consists of six phases, not all of which are needed by all
instructions. However, all instructions do need the

stage and the

stage.

**Part b (6 points): Consider the following combinational circuit, where the logic block A takes**
​
100 ns, B takes 100 ns, C takes 200 ns, and D takes 100 ns; also assume that it takes 20 ns to
load data into a register.

**(3 points) What is the latency of this circuit from input to output?**
​

**(3 points) What is the overall throughput of this circuit?**
​

**Part c (6 points): A student who just took CSC 252 came up with a pipelined implementation.**
​
She used two additional pipeline registers, and the new design is shown below. All the registers
are connected to the clock signal, which is omitted in this figure for simplicity purpose.

7


-----

**(3 points) What is the latency now?**
​

**(3 points) What is the overall throughput now?**
​


8


-----

**Problem 6 (22 points. Suggested time: 20 mins)**
Consider the following assembly code (.L1 is a label. I1 ~ I7 are just notations we add so that we
can easily refer to an instruction; they are not part of the program):

I1:       movq $0, %rax
.L1:
I2:       movq %rdi, %rdx
I3:       andq $1, %rdx
I4:       addq %rdx, %rax
I5:       shrq $1, %rdi
I6:       jne .L1
I7:       ret

Assume that %rdi is loaded with 0x0F before the program starts.

**Part a (3 points): What is the value of %rax after the code returns?**
​

**Part b (3 points): In a single-cycle, sequential microarchitecture, how many cycles does this**
​
program take to finish?

**Part c (9 points): There are 4 pairs of read-after-write data dependencies. One of them is <I1,**
​
I4> because I1 writes to %rax and I4 reads from %rax. What are the other three pairs? Write the
answers in the form of <Im, In>.

**(3 points) Pair 1**
​

**(3 points): Pair 2**
​

**(3 points): Pair 3**
​

9


-----

**Part d (7 points): One student implemented a 5-stage pipeline processor as we described in**
​
the class as well as in the textbook. All data dependencies can be handled using data forwarding
in her design (i.e., no pipeline bubble due to data dependency). Also, she implemented a 1-bit
branch predictor as we discussed in the class, which always uses the last prediction result and
changes mind instantaneously after a misprediction. You can assume that the first prediction is
made as “taken.”

You job: determine how many cycles this particular processor takes to finish the above program.
Show your work to obtain partial credit.

10


-----

