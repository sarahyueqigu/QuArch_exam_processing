# Solutions - Midterm Exam
```
              (October 17[th] @ 5:30 pm)
  Presentation and clarity are very important! Show your procedure!

## PROBLEM 1 (24 PTS)
```
a) Complete the following table. The decimal numbers are unsigned: (5 pts.)

**Decimal** **BCD** **Binary** **Reflective Gray Code**
```
          27 00100111 11011 10110
          57 01010111 111001 100101
          133 000100110011 10000101 11000111

```
b) Complete the following table. The decimal numbers are signed. Use the fewest number of bits in each case: (15 pts.)

**REPRESENTATION**

**Decimal** **Sign-and-magnitude** **1's complement** **2's complement**
```
          -1 11 10 1111
          -7 1111 1000 1001
          11 01011 01011 01011
          -27 111011 100100 100101
           0 00 1111 0
          -64 11000000 10111111 1000000

```
c) Convert the following decimal numbers to their 2’s complement representations. (4 pts)

✓ `-27.25` ✓ `26.5`

`+27.25` `=` `011011.01`  `-27.25` `=` `100100.11` `26.5 = 011010.1`

## PROBLEM 2 (17 PTS)

- Complete the timing diagram of the following circuit. The VHDL code (tst.vhd) corresponds to the shaded circuit.
𝑞= 𝑞1𝑞0, 𝑃= 𝑝3𝑝2𝑝1𝑝0, 𝑥= 𝑥1𝑥0
```
                               architecture bhv of tst is
                P3
            3 P2 x1  signal t: std_logic;
            2

```
`a` `1` `P1` PRIORITYENCODER `x0` `begin`

`b` `q1` `s1 s00` `P0` P=0000 → z=0 `z` `t <= b xnor c;  process (b,c,t)`
```
  c tst.vhd q0  begin   q <= b & c;
                                 if t = ‘0’ then
 library ieee;     q <= c & b;
 use ieee.std_logic_1164.all;    end if;
                                end process;
 entity tst is
  port (b, c : in std_logic; end bhv;
     q: out std_logic_vector(1 downto 0));
 end tst;
 a
 b
 c
 t

```
|Decimal|BCD|Binary|Reflective Gray Code|
|---|---|---|---|
|27|00100111|11011|10110|
|57|01010111|111001|100101|
|133|000100110011|10000101|11000111|

|REPRESENTATION|Col2|Col3|Col4|
|---|---|---|---|
|Decimal|Sign-and-magnitude|1's complement|2's complement|
|-1|11|10|1111|
|-7|1111|1000|1001|
|11|01011|01011|01011|
|-27|111011|100100|100101|
|0|00|1111|0|
|-64|11000000|10111111|1000000|

```
tst.vhd

```
```
q
P
x
z

```
```
 01
1101
 11

```
```
00 11 10 01 10 00 00 10 01 11
1110 0111 1011 1101 1111 1110 1111 1011 1111 0111
11 10 11 11 11 11 11 11 11 10

```

-----

## PROBLEM 3 (12 PTS)

- Complete the timing diagram (signals 𝐷𝑂 and 𝐷𝐴𝑇𝐴) of the following circuit. The circuit in the blue box computes the
signed operation T-7, with the result having 5 bits. T is a 4-bit signed (2C) number.
```
                   4 4
                 DI DATA

```

###### DO T-7

```
OE

```
```
OE

```
```
DATA 1001 1000 0100
 DI 1011 1000

```
```
     DO 10010 11101 00000 10001

## PROBLEM 4 (12 PTS)

```
- The figure below depicts the entire memory space of a microprocessor. Each memory address occupies one byte. 1KB = 2[10]
bytes, 1MB = 2[20] bytes, 1GB = 2[30] bytes
✓ What is the size (in bytes, KB, or MB) of the memory space? What is the address bus size of the microprocessor? (3 pts.)

|Col1|1001 1011|Col3|Col4|Col5|0111 00000|Col7|1000 10001|Col9|
|---|---|---|---|---|---|---|---|---|
||||0100||||||
|||1000 1000||1101 1101||1110 1110||0101|
|||||||||0101|
||||||||||
||||||||||
||10010||11101||||||
||||||||||


Address Space: 0x000000 to 0x1FFFFF. To represent all these addresses, we require 21 bits. So, the address bus size
of the microprocessor is 21 bits. The size of the memory space is then 2[21] = 2 MB.


✓ If we have a memory chip of 256 KB, how many bits do we require to address those 256 KB of memory? (1 pt.)

256 KB memory device: 256KB = 2[18] bits. Thus, we require 18 bits to address the memory device.


✓ We want to connect the 256 KB memory chip to the microprocessor. For optimal implementation, we must place those

256 KB in an address range where every address shares some MSBs. Provide a list of all the possible address ranges that
the 256 KB memory chip can occupy. You can only use the non-occupied portions of the memory space as shown below.

 `0x080000 to 0x0BFFFF`  `0x100000 to 0x13FFFF`  `0x140000 to 0x17FFFF`  `0x180000 to 0x1BFFFF`


### ... ... ...
 ... ... ... ...


8 bits

## PROBLEM 5 (18 PTS)
a) Perform the binary unsigned subtraction of these unsigned integers. Use the fewest number of bits 𝑛 to represent both

operators. Indicate every borrow from b0 to bn. Determine whether we need to keep borrowing from a higher byte. (6 pts)

✓ `30 – 47`


Borrow out!
```
  30 = 0x1E = 0 1 1 1 1 0   47 = 0x2F = 1 0 1 1 1 1

```
```
1 0 1 1 1 1

```

-----

b) Perform the binary operation of these numbers, where numbers are represented in 2's complement. Indicate every carry

from c0 to cn. Use the fewest number of bits to represent the summands and the result so that overflow is avoided. (8 pts)

✓ `30 – 47`
```
    n = 7 bits

```

c7c6=0

No Overflow

```
 30 = 0 0 1 1 1 1 0 +
-47 = 1 0 1 0 0 0 1
-17 = 1 1 0 1 1 1 1

```

`30 - 47 = -17 ` `[-26, 26-1] →` no overflow

c) Perform binary multiplication of the following numbers that are represented in 2’s complement arithmetic. (4 pts)

✓ `-9 x 12`

```
1 0 1 1 1 x
0 1 1 0 0

```
```
1 0 0 1 x
1 1 0 0 

```
```
     0 0 0 0 
    0 0 0 0  
  1 0 0 1   
 1 0 0 1    
0 1 1 0 1 1 0 0 

```
```
                      1 0 0 1 0 1 0 0

## PROBLEM 6 (17 PTS)

```
- Given the following Boolean function: 𝑓(𝑥, 𝑦, 𝑧) = ∏𝑀(3,4)
a) Provide the simplified expression for 𝑓 and sketch this circuit using logic gates. (4 pts)

```
x y z
0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1

```
```
f
1
1
1
0
0
1
1
1

```

𝑥𝑦

```
00 0 11 10
1 1 1 0
1 1 1

###### 𝑓= 𝑥𝑦+ 𝑦̅𝑧+ 𝑥̅𝑧̅

```

𝑓


𝑥

𝑦

𝑧


𝑧
```
0

```
```
1

```
|1|1|1|0|
|---|---|---|---|
|1||1|1|


b) Implement the previous circuit using ONLY 2-to-1 MUXs (AND, OR, NOT, XOR gates are not allowed). (13 pts)

𝑓(𝑥, 𝑦, 𝑧) = 𝑥̅𝑓(0, 𝑦, 𝑧) + 𝑥𝑓(1, 𝑦, 𝑧) = 𝑥̅(𝑦̅𝑧+ 𝑧̅) + 𝑥(𝑦+ 𝑦̅𝑧) = 𝑥̅𝑔(𝑦, 𝑧) + 𝑥ℎ(𝑦, 𝑧)
𝑔(𝑦, 𝑧) = 𝑦̅𝑔(0, 𝑧) + 𝑦𝑔(1, 𝑧) = 𝑦̅(1) + 𝑦(𝑧̅)
ℎ(𝑦, 𝑧) = 𝑦̅ℎ(0, 𝑧) + 𝑦ℎ(1, 𝑧) = 𝑦̅(𝑧) + 𝑦(1)
```
                                    1 0

```
Also: 𝑧̅ = 𝑧̅(1) + 𝑧(0) `1`


𝑓

|1 0 1 0 𝑧̅ 1 𝑔 0 0 ℎ 𝑧 1 0 1 1|Col2|Col3|Col4|
|---|---|---|---|
|||||


𝑧


𝑦 𝑥


-----

