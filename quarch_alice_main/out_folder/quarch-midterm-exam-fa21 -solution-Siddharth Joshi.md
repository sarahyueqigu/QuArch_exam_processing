### As a member of the Notre Dame community, I acknowledge that it is my responsibility to learn and abide by principles of intellectual honesty and academic integrity, and therefore I will not participate in or tolerate academic dishonesty.

## By writing my name below, I agree to uphold the honor code.

# Name (print clearly): Siddharth Joshi

**CSE 20221 Logic Design**

**Midterm Exam, October 07, 2021**

**75 minutes**

**Closed book, closed notes, no calculator**

|Problem|Points|Score|
|---|---|---|
|1|10||
|2|10||
|3|10||
|4|10||
|5|10||
|6|10||
|7|10||
|8|10||
|9|10||
|10|10||
|Total|100||


1


-----

### Problem 1 (10 points)


2


-----

### Problem 2 (10 points)
```
inputs to your circuit.
 A B C
 0 0 0
 0 0 1
 0 1 0
 0 1 1
 1 0 0
 1 0 1
 1 1 0
 1 1 1
Ans : C

```
|A|B|C|F|
|---|---|---|---|
|0|0|0|1|
|0|0|1|1|
|0|1|0|0|
|0|1|1|0|
|1|0|0|1|
|1|0|1|1|
|1|1|0|1|
|1|1|1|0|


3


-----

### Problem 3 (10 points)


4


-----

### Problem 4 (10 points)


5


-----

### Problem 5 (10 points)


6


-----

### Problem 6 (10 points)


7


-----

8


-----

9


-----

### Problem 7 (10 points)

|00|01|11|10|
|---|---|---|---|
||1|1|1|
|||||
|||||
|1|||1|


10


-----

|A|B|C|F|
|---|---|---|---|
|0|0|0|0|
|0|0|1|0|
|0|1|0|1|
|0|1|1|0|
|1|0|0|0|
|1|0|1|1|
|1|1|0|1|
|1|1|1|0|


11


-----

### Problem 8 (10 points)


12


-----

|A[0]|B[0]|gt_in|lt_in|eq_in|gt_out|lt_out|eq_out|
|---|---|---|---|---|---|---|---|
|x|x|1|x|x|1|0|0|
|x|x|x|1|x|0|1|0|
|0|0|x|x|1|0|0|1|
|0|1|x|x|1|0|1|0|
|1|0|x|x|1|1|0|0|
|1|1|x|x|1|0|0|1|


13


-----

### Problem 9 (10 points)


14


-----

```
iii.​ (2 points) Select all the true statements about the testbench for this

```

15


-----

### Problem 10 (10 points)

|Addr|Label|Pseudocode|Assembly|Hex|
|---|---|---|---|---|
|0||||7000|
|1||||7101|
|2||||7222|
|3||||3312|
|4||||B033|
|5||||0001|
|6||||6331|
|7||||AFD0|
|8||||F000|


16


-----

**_albaCore Instruction Set and Encoding_**

|Assembly Language Syntax|Behavior|
|---|---|
|add rw ra rb|R[rw] ← R[ra] + R[rb]|
|sub rw ra rb|R[rw] ← R[ra] - R[rb]|
|and rw ra rb|R[rw] ← R[ra] & R[rb]|
|or rw ra rb|R[rw] ← R[ra] | R[rb]|
|not rw ra|R[rw] ← ~R[ra]|
|shl rw ra shamt4|R[rw] ← R[ra] << shamt4|
|shr rw ra shamt4|R[rw] ← R[ra] >> shamt4|
|ldi rw imm8|R[rw] ← {4’h0, imm8}|
|ld rw rb offset 4|R[rw] ← M[R[rb]+offset4]|
|st ra rb offset 4|M[R[rb]+offset4] ← R[ra]|
|br disp8|pc ← pc + signExtend(disp8)|
|bz rb disp|if (R[rb] == 0) pc ← pc + signExtend(disp8) else pc ← pc + 1|
|bn rb disp|if (R[rb] < 0) pc ← pc + signExtend(disp8) else pc ← pc + 1|
|jal target1 2|pc ← {pc[15:12, target12} R[15] ← pc + 1|
|jr ra|pc ← R[ra]|
|quit|pc freezes|

|Instruction|Col2|Col3|Col4|Encoding|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|mnemonic|arg1|arg2|arg3|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0||
|add|rw|ra|rb|opcode = 0||||rw||||ra||||rb|||||
|sub|rw|ra|rb|opcode = 1||||rw||||ra||||rb|||||
|and|rw|ra|rb|opcode = 2||||rw||||ra||||rb|||||
|or|rw|ra|rb|opcode = 3||||rw||||ra||||rb|||||
|not|rw|ra||opcode = 4||||rw||||ra|||||||||
|shl|rw|ra|shamt|opcode = 5||||rw||||ra||||shamt|||||
|shr|rw|ra|shamt|opcode = 6||||rw||||ra||||shamt|||||
|ldi|rw|imm||opcode = 7||||rw||||imm|||||||||
|ld|rw|rb|offset_ld|opcode = 8||||rw||||offset_ld||||rb|||||
|st|ra|rb|offset_st|opcode = 9||||offset_st||||ra||||rb|||||
|br|disp|||opcode = 10||||displacement|||||||||||||
|bz|rb|disp||opcode = 11||||displacement||||||||rb|||||
|bn|rb|disp||opcode = 12||||displacement||||||||rb|||||
|jal|target|||opcode = 13||||target|||||||||||||
|jr|ra|||opcode = 14||||||||ra|||||||||
|quit||||opcode = 15||||||||imm|||||||||


17


-----

