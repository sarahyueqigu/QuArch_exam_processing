# Solutions - Midterm Exam
```
   (February 17[th] @ 7:30 pm)

```
```
  Presentation and clarity are very important! Show your procedure!

## PROBLEM 1 (20 PTS)

```
- Compute the result of the following operations. The operands are signed fixed-point numbers. The result must be a signed
fixed point number. For the division, use 𝑥= 5 fractional bits.

|1.010001 + 1.011|1001.1101 - 1.011101|0.010101 + 01.11111|
|---|---|---|
|10.101  0.10011|1.011  1.0101|10.10010  0.101|

```
(February 17[th] @ 7:30 pm)

```
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
- Represent these numbers in Fixed Point Arithmetic (signed numbers). Use the FX format [12 4].

✓ `-16.375` ✓ `32.3125`
```
    +16.375 = 010000.011 +32.3125 = 00100000.0101

```
 -16.375 = 11101111.1010



- Complete the table for the following fixed point formats (signed numbers): (6 pts.)

**Integer bits** **Fractional Bits** **FX Format** **Range** **Resolution**

6 3 [9 3] [−2[5], 2[5] −2[−3]] 2[−3]

8 5 [13 5] [−2[7], 2[7] −2[−5]] 2[−5]

|Integer bits|Fractional Bits|FX Format|Range|Resolution|
|---|---|---|---|---|
|6|3|[9 3]|[−25, 25 −2−3]|2−3|


-----

## PROBLEM 3 (40 PTS)

- Perform the following 32-bit floating point operations. For fixed-point division, use 4 fractional bits. Truncate the result when
required. Show your work: how you got the significand and the biased exponent bits of the result. Provide the 32-bit result.

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

Append 𝑥 = 4 zeros: 10111𝟎𝟎𝟎𝟎

11000

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

Integer division

𝑄= 1111 →𝑄𝑓= 0.1111


Thus: 𝑋= −0.1111 × 2[101] = −1.111 × 2[100]
𝑒+ 𝑏𝑖𝑎𝑠= 100 + 127 = 227 = 11100011

𝑋 = `1111 0001 1111 0000 0000 0000 0000 0000 =` `F1F00000`

## PROBLEM 4 (30 PTS)

- “Counting 0’s” Circuit: It counts the number of bits in register 𝐴 with a ‘0’ value. The digital system is depicted below.
✓ Example: for 𝑛= 8: if 𝐴= 00110010, then 𝐶= 0101.
✓ The behavior (on the clock tick) of the generic components is as follows:

_m-bit counter (modulo-n+1): If E=0, the count stays._ _n-bit Parallel access shift register: If E=0, the output is kept._
```
    if E = 1 then if E = 1 then
      if sclr = 1 then   if s_l = ‘1’ then
       Q  0    Q  D
      else   else
       Q  Q+1    Q  shift in ‘din’ (to the right)
     end if;  end if;
    end if; end if;
                DA
    resetn
       1 din

```
`LAEA` `s_lE` `A` **ALGORITHM**

|m-bit counter (modulo-n+1): If E=0, the count stays.|n-bit Parallel access shift register: If E=0, the output is kept.|
|---|---|
|if E = 1 then if sclr = 1 then Q  0 else Q  Q+1 end if; end if;|if E = 1 then if s_l = ‘1’ then Q  D else Q  shift in ‘din’ (to the right) end if; end if;|


**C**

```
C  0
while A  11...1 (2[n]-1)
  if a0 = 0 then
    C  C + 1
  end if
  right shift A
end while

```

**DATAPATH CIRCUIT**

```
clock

```
|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|L E Rig|1 din A s_l A A E Parallel Access A ht Shift Register LA EA z a 0||EC E Q sclrC sclr counter: m bi||ts|
|||||||
|||FINITE STATE MACHINE||||
|||||||


**FINITE STATE**

**MACHINE**


-----

- Sketch the Finite State Machine diagram (in ASM form) given the algorithm (for n=8, m=4). (18 pts.)
✓ The process begins when 𝑠 is asserted, at this moment we capture 𝐷𝐴 on register 𝐴. Then, we shift 𝐴 one bit at a time.

The process ends when 𝐴= 2[𝑛] −1 (i.e., when z=1). The signal done is asserted when we finish counting.

✓ As 𝐴 is being shifted: we need to increase the count C every time 𝑎0 = 0.

Finite State Machine:

resetn=0

**S1**

EC, sclrC  1

0
s

1

EA, LA  1

**S2**

1 0

z EA  1

**S3**

done  1 a0 1

0

0 1

s

EC  1

- Complete the timing diagram (n=8, m=4). A is represented in hexadecimal format, while C is in binary format (12 pts.)
```
 clock
 resetn
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
|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||10101||110||||||||||||||||11110||101||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
|0|00||AE||D7||EB||F5||FA||FD||FE||FF||FF||FF||FF||FF||FF||FF||
||||||||||||||||||||||||||||||||
|S1|S1||S2||S2||S2||S2||S2||S2||S2||S2||S3||S1||S1||S1||S1||S1||
||||||||||||||||||||||||||||||||
|00|0000||0000||0001||0001||0001||0001||0010||0010||0011||0011||0011||0000||0000||0000||0000||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||


-----

