# Solutions - Midterm Exam
```
              (February 14[th] @ 5:30 pm)
  Presentation and clarity are very important! Show your procedure!

## PROBLEM 1 (22 PTS)
```
a) Complete the following table. The decimal numbers are unsigned: (3 pts.)

**Decimal** **BCD** **Binary** **Reflective Gray Code**
```
          50 01010000 110010 101011
          128 000100101000 10000000 11000000

```
b) Complete the following table. The decimal numbers are signed. Use the fewest number of bits in each case: (15 pts.)

**REPRESENTATION**

**Decimal** **Sign-and-magnitude** **1's complement** **2's complement**
```
          -17 110001 101110 101111
          -16 110000 101111 10000
          -32 1100000 1011111 100000
          -1 11 10 1111
          41 0101001 0101001 0101001
           0 10 1111 0

```
c) Convert the following decimal numbers to their 2’s complement representations. (4 pts)

✓ `-17.25` ✓ `16.75`
```
      +17.25 = 010001.01  -17.25= 101110.11 +16.75 = 010000.11

## PROBLEM 2 (15 PTS)

```
- Complete the timing diagram of the following circuit. The VHDL code (tst.vhd) corresponds to the shaded circuit.
𝑞= 𝑞1𝑞0, 𝑃= 𝑝3𝑝2𝑝1𝑝0, 𝑥= 𝑥1𝑥0
```
                               architecture bhv of tst is
              P3
            32 P2 x1  signal t: std_logic;

```
`a` `P1` PRIORITY `x0` `begin`

##### 1 ENCODER

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
 q 01 00 11 10 01 10 00 00 10 01 11
 P 0010 0001 1000 0100 0010 0000 0001 0000 0100 0000 1000
 x 01 00 11 10 01 00 00 00 10 00 11

```
|Decimal|BCD|Binary|Reflective Gray Code|
|---|---|---|---|
|50|01010000|110010|101011|
|128|000100101000|10000000|11000000|

|REPRESENTATION|Col2|Col3|Col4|
|---|---|---|---|
|Decimal|Sign-and-magnitude|1's complement|2's complement|
|-17|110001|101110|101111|
|-16|110000|101111|10000|
|-32|1100000|1011111|100000|
|-1|11|10|1111|
|41|0101001|0101001|0101001|
|0|10|1111|0|

|nd|tst;|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||01|00|11|10|01|10|00|00|10|01|11||
||||||||||||||
||0010|0001|1000|0100|0010|0000|0001|0000|0100|0000|1000||
||||||||||||||
||01|00|11|10|01|00|00|00|10|00|11||
||||||||||||||

```
(February 14[th] @ 5:30 pm)

```

-----

## PROBLEM 3 (12 PTS)

- Complete the timing diagram (signals 𝐷𝑂 and 𝐷𝐴𝑇𝐴) of the following circuit. The circuit in the blue box computes the
signed operation T-7, with the result having 5 bits. T is a 4-bit signed (2C) number.
✓ Example: if T=1010: `4` `4`

DO = 1010-0111 = 11010 + 11001 `DI` `DATA`
DO = 10011 `5` `4`

##### DO T-7
```
                         T
                             OE

```
```
OE

```
```
DATA 1001 1000 0111
 DI 1011 1000

```
```
     DO 10010 00000 11101

## PROBLEM 4 (10 PTS)

```
- A microprocessor has a memory space of 1 MB. Each memory address occupies one byte.
1KB = 2[10] bytes, 1MB = 2[20] bytes, 1GB = 2[30] bytes.
a) What is the address bus size (number of bits of the address) of the microprocessor?

Size of memory space: 1 MB = 2[20] bytes. Thus, we require 20 bits to address the
memory space.

|Col1|1001 1011 10010|1000 1000|0111 00000|1101 1101|0100 11101|1110 1110|1000 10001|0101 0101|
|---|---|---|---|---|---|---|---|---|


Address 8 bits

`0x________` 0


b) What is the range (lowest to highest, in hexadecimal) of the memory space for this

microprocessor? (1 pt.)
With 20 bits, the address range is 0x00000 to 0xFFFFF.

c) The figure to the right shows four memory chips that are placed in the given positions:

✓ Complete the address ranges (lowest to highest, in hexadecimal) for each of the

memory chips. (8 pts)

8 bits
Address

```
0x________
0x________
0x________
0x________

```
```
0x________
0x________
0x________

```
```
1111 1111 1111 1111 1111: 0xFFFFF

```
|0000 0000 0000 0000 0000: 0x00000 0000 0000 0000 0000 0001: 0x00001 ... ... 0011 1111 1111 1111 1111: 0x3FFFF|0 256KB|
|---|---|
|0100 0000 0000 0000 0000: 0x40000 0100 0000 0000 0000 0001: 0x40001 ... ... 0111 1111 1111 1111 1111: 0x7FFFF|1 256KB|
|1000 0000 0000 0000 0000: 0x80000 1000 0000 0000 0000 0001: 0x80001 ... ... 1011 1111 1111 1111 1111: 0xBFFFF|2 256KB|
|1100 0000 0000 0000 0000: 0xC0000 1100 0000 0000 0000 0001: 0xC0001 ... ... 1111 1111 1111 1111 1111: 0xFFFFF|3 256KB|


## PROBLEM 5 (15 PTS)
a) Perform the following additions and subtractions of the following unsigned integers. Use the fewest number of bits 𝑛 to

represent both operators. Indicate every carry (or borrow) from c0 to cn (or b0 to bn). For the addition, determine whether
there is an overflow. For the subtraction, determine whether we need to keep borrowing from a higher bit. (6 pts)

✓ `37 + 41` ✓ `37 - 41`

Borrow out!

```
37 = 0x25 = 1 0 0 1 0 1 41 = 0x29 = 1 0 1 0 0 1

```

-----

b) The figure shows two 8-bit operands represented in 2’s complement.

Perform the 8-bit addition operation, i.e., complete all the carries and
the summation bits. Also, indicate the corresponding decimal numbers
for the 8-bit operands and the 8-bit result.

Does this 8-bit operation incur in overflow? Yes No

Value of the overflow bit: c8c7=0

Value of carry out bit: c8 = 1

|1|1|0|0|0|0|0|0|0|
|---|---|---|---|---|---|---|---|---|

|1|1|0|1|0|1|1|1|
|---|---|---|---|---|---|---|---|

|1|1|1|0|1|0|0|0|
|---|---|---|---|---|---|---|---|

```
-65

```

Decimal

values
```
 -41
 -24

```
```
=
=
=

```
```
c8 c7 c6 c5 c4 c3 c2 c1 c0

```
```
+

```
|1|0|1|1|1|1|1|1|
|---|---|---|---|---|---|---|---|


c) Perform binary multiplication of the following numbers that are represented in 2’s complement arithmetic. (3 pts)

✓ `1001 x 01001`
```
                    1 0 0 1 x 1 0 0 1 x
                   0 1 0 0 1 0 1 1 1 
                             1 0 0 1 
                           1 0 0 1  
                          1 0 0 1   
                         0 0 0 0    
                         0 1 1 1 1 1 1 
                         1 0 0 0 0 0 1

## PROBLEM 6 (10 PTS)

```
- Sketch the circuit that computes |𝐴−𝐵|, where 𝐴, 𝐵 are 4-bit signed numbers. For example, 𝐴= 0101, 𝐵= 1101 →
|𝐴−𝐵| = |5 −(−3)| = 8. You can only use full adders (or multi-bit adders) and logic gates. Your circuit must avoid overflow:
design your circuit so that the result and intermediate operations have the proper number of bits.

𝐴= 𝑎3𝑎2𝑎1𝑎0, 𝐵= 𝑏3𝑏2𝑏1𝑏0
𝐴, 𝐵∈[−8,7] → 𝐴, 𝐵 require 4 bits in 2C representation.
✓ 𝑋= 𝐴−𝐵∈[−15,15] requires 5 bits in 2C. Thus, we need to zero-extend 𝐴 and 𝐵.
✓ |𝑋| = |𝐴−𝐵| ∈[0,15] requires 5 bits in 2C. Thus, the second operation 0 ± 𝑋 only requires 5 bits.

 If 𝑥4 = 1 → 𝑋< 0 → we do 0 −𝑋.

 If 𝑥4 = 0 → 𝑋≥0 → we do 0 + 𝑋.

✓ 𝑅= |𝐴−𝐵| ∈[0,15] requires 5 bits in 2C. Note that the MSB is always 0.

```
a3 b3

```
```
r3 r2 r1 r0

```
```
a2 b2

```
```
a1 b1

```
```
a0

```
```
b0

```

**FULL ADDER**

x y


cout


cin

```
a3 b3

##### FA
  x4

 FA
  s4
 r4

```

s


-----

## PROBLEM 7 (16 PTS)

- In a 4-to-2 priority encoder (like the one in Problem 2), it can be demonstrated that the output 𝑥0 = 𝑝̅̅̅ 𝑝3 ̅̅̅𝑝2 1 + 𝑝3.

✓ Provide the simplified expression for 𝑥0 and sketch this circuit using logic gates. (3 pts)

```
p3 p2 p1
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
x0
0
1
0
0
1
1
1
1

```
|00 01 11 10 0 0 0 1 1 1 1 0 1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||0|0|1|1|
||1|0|1||


✓ Implement 𝑥0 using ONLY an 8-to-1 MUX. (3 pts).

```
0
1
0
0
1
1
1
1

```

✓ Implement 𝑥0 using ONLY 2-to-1 MUXs (AND, OR, NOT, XOR gates are not allowed) (10 pts).

𝑥0(𝑝3, 𝑝2, 𝑝1) = 𝑝3 + 𝑝̅̅̅𝑝2 1
```
                                  0

```
𝑥0(𝑝3, 𝑝2, 𝑝1) = 𝑝̅̅̅𝑥3 0(0, 𝑝2, 𝑝1) + 𝑝3𝑥0(1, 𝑝2, 𝑝1) = 𝑝̅̅̅(3 𝑝̅̅̅𝑝2 1) + 𝑝3(1)

𝑥0(𝑝3, 𝑝2, 𝑝1) = 𝑝̅̅̅3𝑔(𝑝2, 𝑝1) + 𝑥0(1) `0` `1`

𝑔(𝑝2, 𝑝1) = 𝑝̅̅̅𝑔(0, 𝑝2 1) + 𝑝2𝑔(1, 𝑝1) = 𝑝̅̅̅(𝑝2 1) + 𝑝2(0)

|0 0 1 0 1 1|Col2|Col3|Col4|
|---|---|---|---|
|||||


-----

