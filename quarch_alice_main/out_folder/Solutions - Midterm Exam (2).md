# Solutions - Midterm Exam

```
              (February 14[th] @ 7:30 pm)
  Presentation and clarity are very important! Show your procedure!

## PROBLEM 1 (20 PTS)

```
- Compute the result of the following operations. The operands are signed fixed-point numbers. The result must be a signed
fixed point number. For the division, use 𝑥= 5 fractional bits.

|1.010001 + 1.011|1001.1101 - 1.011101|0.010101 + 01.11111|
|---|---|---|
|10.101  0.10011|1.011  1.0101|10.10010  0.101|

```
1 1.0 1 0 0 0 1 +
1 1.0 1 1 0 0 0
1 0.1 0 1 0 0 1

```
```
0 0 0.0 1 0 1 0 1 +
0 0 1.1 1 1 1 1 0
0 1 0.0 1 0 0 1 1

```
```
1 0 0 1.1 1 0 1 0 0 1 1 1 1.0 1 1 1 0 1

```
```
1 0 0 1.1 1 0 1 0 0 +
0 0 0 0.1 0 0 0 1 1
1 0 1 0.0 1 0 1 1 1

```
```
 1.011 x
1.0101

```
```
 10.101 x
0.10011 

```
```
 01.011 x
0.10011 

```
```
1 0 0 1 1 x
 1 0 1 1 

```
```
 0.101 x
0.1011 

```
```
1 0 1 1 x
 1 0 1 

```
```
     1 0 0 1 1 
    1 0 0 1 1  
  0 0 0 0 0   
 1 0 0 1 1    
0 1 1 0 1 0 0 0 1 

```
```
     1 0 1 1 
    0 0 0 0  
  1 0 1 1   
0 0 1 1 0 1 1 1 

```
```
0.0 1 1 0 1 1 1

```
```
0.1 1 0 1 0 0 0 1
1.0 0 1 0 1 1 1 1

```

01.0111

00.1010 [=]


010111

001010 [≡]


10111

1010


✓


10.10010 01.0111

0.101 [: To unsigned (numerator) and then alignment, ][𝑎 = 4][: ] 0.101 [=]
```
    0001001001

```
`1010` `1011100000` Append 𝑥 = 5 zeros: 10111𝟎𝟎𝟎𝟎𝟎1010

`1010` Integer Division:
```
      1100

```
𝑄= 1001001, 𝑅= 110
```
      1010
```
→𝑄𝑓= 10.01001 (𝑥= 5)

```
10000
 1010

```

Final result (2C):


01.01110 = 2𝐶(010.01001) = 101.10111

1.011

```
           110

## PROBLEM 2 (10 PTS)

```
- Represent these numbers in Fixed Point Arithmetic (signed numbers). Select the minimum number of bits in each case.

✓ `-16.375` ✓ `32.3125`
```
    +16.375 = 010000.011 +32.3125 = 0100000.0101

```
 -16.375 = 101111.101



- Complete the table for the following fixed point formats (signed numbers): (6 pts.)

**Integer bits** **Fractional Bits** **FX Format** **Range** **Resolution**

6 3 [9 3] [−2[5], 2[5] −2[−3]] 2[−3]

8 5 [13 5] [−2[7], 2[7] −2[−5]] 2[−5]

|Integer bits|Fractional Bits|FX Format|Range|Resolution|
|---|---|---|---|---|
|6|3|[9 3]|[−25, 25 −2−3]|2−3|


-----

## PROBLEM 3 (40 PTS)

- Calculate the result (provide the 32-bit result) of the following operations with 32-bit floating point numbers. Truncate the
results when required. When doing fixed-point division, use 4 fractional bits. Show your procedure.

✓ `C1500000 + 436A0000` ✓ `D0A90000 – CF480000` ✓ `80400000  7AB80000` ✓ `FBB80000  49400000`

✓ 𝑋 = C1500000 + 436A0000:
```
    C1500000: 1100 0001 0101 0000 1000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 10000010 = 130 →𝑒= 130 −127 = 3 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.101
```
     C1500000 = −1.101 × 2[3]

```
|✓ C1500000 + 436A0000|✓ D0A90000 – CF480000|✓ 80400000  7AB80000|✓ FBB80000  49400000|
|---|---|---|---|

```
436A0000: 0100 0011 0110 1010 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 10000110 = 134 →𝑒= 134 −127 = 7 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.110101
```
  436A0000 = 1.110101 × 2[7]

```
𝑋= −1.101 × 2[3] + 1.110101 × 2[7] = − [1.101] × 2[7] + 1.110101 × 2[7]

2[4]

𝑋= (−0.0001101 + 1.110101) × 2[7]

To subtract these unsigned numbers, we first convert to 2C:

𝑅= 01.110101 −0.0001101 = 01.110101 + 1.1110011
The result in 2C is: 𝑅= 01.1011101
For floating point, we need to convert to sign-and-magnitude:
 𝑅(𝑆𝑀) = +1.1011101

- You can also do unsigned subtraction: 𝑋= (1.110101 −0.0001101) × 2[7]

𝑋= 1.1011101 × 2[7], 𝑒+ 𝑏𝑖𝑎𝑠= 7 + 127 = 134 = 10000110
𝑋 = 0100 0011 0101 1101 0000 0000 0000 0000 = `435D0000`

```
0 1.1 1 0 1 0 1 0 +
1 1.1 1 1 0 0 1 1
0 1.1 0 1 1 1 0 1

```
```
1.1 1 0 1 0 1 0 0.0 0 0 1 1 0 1
1.1 0 1 1 1 0 1

```

✓ 𝑋 = D0A90000 – CF480000:
```
  D0A90000: 1101 0000 1010 1001 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 10100001 = 161 →𝑒= 161 −127 = 34 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.0101001
```
    D0A90000 = −1.0101001 × 2[34]
  CF480000: 1100 1111 0100 1000 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 10011110 = 158 →𝑒= 158 −127 = 31 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.1001
```
    CF480000 = −1.1001 × 2[31]

```

𝑋= −1.0101001 × 2[34] + 1.1001 × 2[31] = −1.0101001 × 2[34] + [1.1001] × 2[34]

2[3]

𝑋= −(1.0101001 −0.0011001) × 2[34] (unsigned subtraction)
𝑋= −1.001 × 2[34], 𝑒+ 𝑏𝑖𝑎𝑠= 34 + 127 = 161 = 10100001
𝑋 = 1101 0000 1001 0000 0000 0000 0000 0000 = `D0900000`


✓ 𝑋 = 80400000  7AB80000:
```
  80400000: 1000 0000 0100 0000 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 00000000 = 0 →𝐷𝑒𝑛𝑜𝑟𝑚𝑎𝑙 𝑛𝑢𝑚𝑏𝑒𝑟→𝑒= −126 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 0.1
```
    80400000 = −0.1 × 2[−126]
  7AB80000: 0111 1010 1011 1000 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 11110101 = 245 →𝑒= 245 −127 = 118 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.0111
```
    7AB80000 = 1.0111 × 2[118]

```
```
1.0 1 0 1 0 0 1 0.0 0 1 1 0 0 1
1.0 0 1 0 0 0 0

```

𝑋= (−0.1 × 2[−126]) × (1.0111 × 2[118]) = −0.10111 × 2[−8] = −1.0111 × 2[−9]
𝑒+ 𝑏𝑖𝑎𝑠= −9 + 127 = 118 = 01110110
𝑋 = 1011 1011 0011 1000 0000 0000 0000 0000 = `BB380000`


✓ 𝑋 = FBB80000  49400000:
```
  FBB80000: 1111 1011 1011 1000 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 11110111 = 247 →𝑒= 247 −127 = 120 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.0111
```
    FBB80000 = −1.0111 × 2[120]
  49400000: 0100 1001 0100 0000 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 10010010 = 146 →𝑒= 146 −127 = 19 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.1
```
    49400000 = 1.1 × 2[19]

```

-----

𝑋= − [1.0111 × 2][120] = − [1.0111] × 2[101]

1.1 × 2[19] 1.1


Alignment:

1.0111

= [1.0111]
1.1 1.1000 [= 10111]11000

```
11000

```
```
000001111
101110000
 11000
 101100
 11000
 101000
  11000
  100000
  11000
   1000

```

Append 𝑥 = 4 zeros: 10111𝟎𝟎𝟎𝟎

11000

Integer division

𝑄= 1111 →𝑄𝑓= 0.1111


Thus: 𝑋= −0.1111 × 2[101] = −1.111 × 2[100]
𝑒+ 𝑏𝑖𝑎𝑠= 100 + 127 = 227 = 11100011

𝑋 = `1111 0001 1111 0000 0000 0000 0000 0000 =` `F1F00000`

## PROBLEM 4 (30 PTS)

- “Counting 0’s” Circuit: It counts the number of bits in register A that has the value of ‘0’.
The digital system is depicted below: FSM + Datapath. Example: For 𝑛= 8: if 𝐴= 00110110, then 𝐶= 0100.
✓ m-bit counter: 𝑠𝑐𝑙𝑟. If 𝐸= 𝑠𝑐𝑙𝑟= 1, the count is initialized to zero. If 𝐸= 1, 𝑠𝑐𝑙𝑟= 0, the count is increased by 1.
✓ Parallel access shift register: If 𝐸= 1: 𝑠_𝑙 = 1 → Load, 𝑠_𝑙= 0 → Shift.

- Sketch the Finite State Machine diagram (in ASM form) given the algorithm (for 𝑛= 8, 𝑚= 4). (18 pts.)
✓ The process begins when 𝑠 is asserted, at this moment we capture 𝐷𝐴 on register 𝐴. Then the process starts by shifting

𝐴 one bit at a time. The process is concluded when 𝐴= 2[𝑛] −1. The signal 𝑑𝑜𝑛𝑒 is asserted when we finish counting.

✓ Note: If 𝐴= 2[𝑛] −1 → 𝑧= 1, else 𝑧= 0. As 𝐴 is being shifted, each time 𝑎0 = 0, we need to increase the count C.

- Complete the timing diagram (next page) where 𝑛= 8, 𝑚= 4. (12 pts.)
```
               DA

```
𝑛
```
  resetn

```
```
   1 din
  LA s_l
  EA E

```
Parallel Access

Right Shift (MSB to LSB)
```
 s_l = 1 → Load
s_l = 0 → Shift

```

##### ALGORITHM
```
C  0
while A  11...1 (2[n]-1)
  if a0 = 0 then
    C  C + 1
  end if
  right shift A
end while

```

**FINITE STATE MACHINE**


-----

Finite State Machine:

**S3**

0
```
 clock
 resetn

```

resetn=0

```
DA 10101110 11110101
 s

```
```
 A
state
 C

```
```
 00 00 AE D7 EB F5 FA FD FE FF FF FF FF FF FF FF
 S1 S1 S2 S2 S2 S2 S2 S2 S2 S2 S3 S1 S1 S1 S1 S1
0000 0000 0000 0001 0001 0001 0001 0010 0010 0011 0011 0011 0000 0000 0000 0000

```
```
sclrC
 EC
done
 z
 EA
 LA

```
|0 S1 00|10101 00 S1 0000|110 AE S2 0000|D7 S2 0001|EB S2 0001|F5 S2 0001|FA S2 0001|FD S2 0010|FE S2 0010|FF S2 0011|11110 FF S3 0011|101 FF S1 0011|FF S1 0000|FF S1 0000|FF S1 0000|FF S1 0000|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||


-----

