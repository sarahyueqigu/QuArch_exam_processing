# Solutions - Midterm Exam
```
              (February 16[th] @ 5:30 pm)
  Presentation and clarity are very important! Show your procedure!

## PROBLEM 1 (24 PTS)
```
a) Complete the following table. The decimal numbers are unsigned: (5 pts.)

**Decimal** **BCD** **Binary** **Reflective Gray Code**
```
          31 00110001 11111 10000
          33 00110011 100001 110001
          247 001001000111 11110111 10001100

```
b) Complete the following table. The decimal numbers are signed. Use the fewest number of bits in each case: (15 pts.)

**REPRESENTATION**

**Decimal** **Sign-and-magnitude** **1's complement** **2's complement**
```
          -10 11010 10101 10110
          -15 11111 10000 10001
          13 01101 01101 01101
          -11 11011 10100 10101
          -31 111111 100000 100001
          -25 111001 100110 100111

```
c) Convert the following decimal numbers to their 2’s complement representations. (4 pts)

✓ `-31.5` ✓ `25.25`
```
      +31.5 = 011111.1  -31.5 = 100000.1 +25.25 = 011001.01

## PROBLEM 2 (18 PTS)

```
- Complete the timing diagram of the following circuit. The VHDL code (tst.vhd) corresponds to the shaded circuit.

##### P3 x1 w1 y3 3 𝑑= 𝑑1𝑑0, 𝑤= 𝑤1𝑤0, 𝑟= 𝑟2𝑟1𝑟0, 𝑦= 𝑦3𝑦2𝑦1𝑦0

|Decimal|BCD|Binary|Reflective Gray Code|
|---|---|---|---|
|31|00110001|11111|10000|
|33|00110011|100001|110001|
|247|001001000111|11110111|10001100|

|REPRESENTATION|Col2|Col3|Col4|
|---|---|---|---|
|Decimal|Sign-and-magnitude|1's complement|2's complement|
|-10|11010|10101|10110|
|-15|11111|10000|10001|
|13|01101|01101|01101|
|-11|11011|10100|10101|
|-31|111111|100000|100001|
|-25|111001|100110|100111|


##### P2 PRIORITY x0 w0 y2 2 P1 ENCODER z E DECODER y1 1
 P0 P=0000 → z=0 y0 0
```
          u
            r2
d1 tst.vhd r1 s1 s0
d0 r0
library ieee;
use ieee.std_logic_1164.all;
entity tst is
 port (d: in std_logic_vector(1 downto 0);
    r: out std_logic_vector(2 downto 0);
    u: in std_logic);
end tst;
 d 10 10 01 10 11
 P3
 P2
 P1
 P0
 z

```
```
architecture bhv of tst is
begin 
 process (d, u)
 begin
   r <= “11”&d(0);
   if u = ‘0’ then
    r <= d&’0’;
   end if;
 end process;
end bhv;

```
|tst;|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|10|10|01|10|11|10|11|00|01|11|10|
||||||||||||
||||||U||||||
|||||||nknown|||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||

```
tst.vhd

```
```
w 01

```
```
end tst;

```
```
r
y

```
```
110
0010

```
```
 11 00 10 11 11 00 00 10 11 10
110 010 110 111 110 111 000 111 111 110
1000 0000 0100 1000 1000 0001 0000 0100 1000 0100

```

-----

## PROBLEM 3 (12 PTS)

- Complete the timing diagram (signals 𝐷𝑂 and 𝐷𝐴𝑇𝐴) of the following circuit. The circuit in the blue box treats the input T
as a 5-bit signed (2C) number and converts it to the sign-and-magnitude representation with 5 bits.
✓ Example: if T = 10110, then DO = 11010.
```
                     5 5
                  DI DATA

```

##### DO 5 2C to

```
OE

```
```
DATA 10001 01110 01111
 DI 00000 01110

```
```
       DO 11111 01111 10011

## PROBLEM 4 (11 PTS)

```
- A microprocessor has a memory space of 512 KB. Each memory address occupies one byte.
a) What is the address bus size (number of bits of the address) of this microprocessor?

Since 512 KB = 2[19] bytes, the address bus size is 19 bits.

|Col1|Col2|DO|Col4|SM T|OE|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||10001||01111||11101 10011||10010||
|||01110 01110||01010||10101||10100|
||||||||||
||00000|||01010||10101||10100|
||||||||||
||||||||||
||11111||01111||||11110||
||||||||||


b) What is the range (lowest to highest, in hexadecimal) of the memory space for this

microprocessor?
With 19 bits, the address range is 0x0000 to 0x7FFFF.

c) The figure to the right shows four memory chips that are placed in the given positions:

✓ Complete the address ranges (lowest to highest, in hexadecimal) for each of the

memory chips. 8 bits

Address


8 bits
Address

`0x________` 0
```
  ...
        128KB
  ...
0x________

```
`0x________` 1
```
  ...
        128KB
  ...
0x________

```
`0x________` 2
```
  ...
        128KB
  ...
0x________

```
`0x________` 3
```
  ...
        128KB
  ...
0x________

```
```
000 0000 0000 0000 0000: 0x00000
000 0000 0000 0000 0001: 0x00001
  ...           ...
001 1111 1111 1111 1111: 0x1FFFF
010 0000 0000 0000 0000: 0x20000
010 0000 0000 0000 0001: 0x20001
  ...           ...
011 1111 1111 1111 1111: 0x3FFFF
100 0000 0000 0000 0000: 0x40000
100 0000 0000 0000 0001: 0x40001
  ...           ...
101 1111 1111 1111 1111: 0x5FFFF

```

`110 0000 0000 0000 0000: 0x60000` 3
```
             110 0000 0000 0000 0001: 0x60001 128KB
              ...           ...
             111 1111 1111 1111 1111: 0x7FFFF

## PROBLEM 5 (18 PTS)
```
a) Perform the binary unsigned subtraction of these unsigned integers. Use the fewest number of bits 𝑛 to represent both

operators. Indicate every borrow from b0 to bn. Determine whether we need to keep borrowing from a higher byte. (6 pts)

✓ `31 – 37`


Borrow out!
```
  31 = 0x1F = 0 1 1 1 1 1   37 = 0x25 = 1 0 0 1 0 1
         1 1 1 0 1 0

```

-----

b) Perform the binary operation of these numbers, where numbers are represented in 2's complement. Indicate every carry

from c0 to cn. Use the fewest number of bits to represent the summands and the result so that overflow is avoided. (8 pts)

✓ `31 – 37`
```
       n = 7 bits

```

c7c6=0

No Overflow

```
 31 = 0 0 1 1 1 1 1 +
-37 = 1 0 1 1 0 1 1
 -6 = 1 1 1 1 0 1 0

```

`31 - 37 = -6 ` `[-2[6], 2[6]-1] →` no overflow

c) Perform binary multiplication of the following numbers that are represented in 2’s complement arithmetic. (4 pts)

✓ `-11 x 7`

```
1 0 1 0 1 x
0 0 1 1 1

```
```
1 0 1 1 x
0 1 1 1 

```
```
     1 0 1 1 
    1 0 1 1  
  1 0 1 1   
 0 0 0 0    
0 1 0 0 1 1 0 1 

```
```
                1 0 1 1 0 0 1 1

## PROBLEM 6 (17 PTS)

```
- A 3-input majority gate has an output value 𝑓 that is 1 if there are more 1’s than 0’s on its inputs. The output 𝑓 is 0 otherwise.
a) Provide the simplified expression for 𝑓 and sketch this circuit using logic gates. (5 pts)

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
0
0
0
1
0
1
1
1

```

𝑥𝑦


𝑥

𝑦

𝑧


𝑓

|𝑥𝑦 00 01 11 10 𝑧 0 0 0 1 0 1 0 1 1 1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||0|0|1||0|
||0|1||1|1|
|||||||


##### 𝑓= 𝑥𝑦+ 𝑦𝑧+ 𝑥𝑧


b) Implement the previous circuit using ONLY 2-to-1 MUXs (AND, OR, NOT, XOR gates are not allowed). (12 pts)

𝑓(𝑥, 𝑦, 𝑧) = 𝑥̅𝑓(0, 𝑦, 𝑧) + 𝑥𝑓(1, 𝑦, 𝑧) = 𝑥̅(𝑦𝑧) + 𝑥(𝑦+ 𝑦𝑧+ 𝑧) = 𝑥̅𝑔(𝑦, 𝑧) + 𝑥ℎ(𝑦, 𝑧)


𝑔(𝑦, 𝑧) = 𝑦̅𝑔(0, 𝑧) + 𝑦𝑔(1, 𝑧) = 𝑦̅(0) + 𝑦(𝑧)

ℎ(𝑦, 𝑧) = 𝑦̅ℎ(0, 𝑧) + 𝑦ℎ(1, 𝑧) = 𝑦̅(𝑧) + 𝑦(1)


𝑓

|0 0 1 𝑔 0 ℎ 1 0 1 1|Col2|Col3|Col4|
|---|---|---|---|
|||||


𝑧


𝑦 𝑥


-----

