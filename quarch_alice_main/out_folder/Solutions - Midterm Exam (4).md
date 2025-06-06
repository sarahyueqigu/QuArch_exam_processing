# Solutions - Midterm Exam
```
   (February 16[th] @ 7:30 pm)

```
```
  Presentation and clarity are very important! Show your procedure!

### PROBLEM 1 (20 PTS)

```
- Compute the result of the following operations. The operands are signed fixed-point numbers. The result must be a signed
fixed-point number. For the division, use 𝑥= 5 fractional bits.

|1.0111 + 1.101001|1.010101 – 1000.0101|01.11111 + 0.10001|
|---|---|---|
|10.101  1.01101|0.111  1.0101|10.101  0.101|

```
(February 16[th] @ 7:30 pm)

```
```
1.0 1 1 1 0 0 +
1.1 0 1 0 0 1

```
```
1 1 1 1.0 1 0 1 0 1 1 0 0 0.0 1 0 1 0 0

```
```
0 0 1.1 1 1 1 1 +
0 0 0.1 0 0 0 1
0 1 0.1 0 0 0 0

```
```
1 1 1 1.0 1 0 1 0 1 +
0 1 1 1.1 0 1 1 0 0
0 1 1 1.0 0 0 0 0 1

```
```
1.0 0 0 1 0 1
 10.101 x
1.01101 

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
 0.111 x
0.1011 

```
```
1 0 1 1 x
 1 1 1 

```
```
 0.111 x
1.0101

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
    1 0 1 1  
  1 0 1 1   
0 1 0 0 1 1 0 1 

```
```
0.1 0 0 1 1 0 1
1.0 1 1 0 0 1 1

```

✓

```
            0.1 1 0 1 0 0 0 1

```
10.1010 01.0110 01.011 1011

0.101 [: To unsigned (numerator) and then alignment, ][𝑎 = 3][: ] 0.101 [=] 00.101 [≡] 101
```
    001000110

```
`101` `101100000` Append 𝑥 = 5 zeros: 1011𝟎𝟎𝟎𝟎𝟎101

`101` Integer Division:
```
     01000

```
𝑄= 1000110, 𝑅= 10
```
      101
```
→𝑄𝑓= 10.00110 (𝑥= 5)
```
       110

```
`101` Final result (2C): 10.1010

0.101 [= 2𝐶(010.0011) = 101.1101]
```
        10

```

### PROBLEM 2 (10 PTS)

- Represent these numbers in Fixed Point Arithmetic (signed numbers). Use the FX format [12 4].

✓ `-16.125` ✓ `19.25`
```
  +16.125 = 010000.001  -16.125 = 11101111.1110 +19.25 = 00010011.0100

```
- Complete the table for the following fixed point formats (signed numbers): (6 pts.)

|Integer bits|Fractional Bits|FX Format|Range|Resolution|
|---|---|---|---|---|
|8|6|[14 6]|[−27, 27 −2−6]|2−6|
|6|4|[10 4]|[−25, 25 −2−4]|2−4|


-----

### PROBLEM 3 (40 PTS)

- Perform the following 32-bit floating point operations. For fixed-point division, use 4 fractional bits. Truncate the result when
required. Show your work: how you got the significand and the biased exponent bits of the result. Provide the 32-bit result.

✓ `40D00000 + C2EA0000` ✓ `50A90000 – 4F480000` ✓ `80200000  7AB80000` ✓ `FB380000  48C00000`

✓ 𝑋 = 40D00000 + C2EA0000:
```
    40D00000: 0100 0000 1101 0000 1000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 10000001 = 129 →𝑒= 129 −127 = 2 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.101
```
     40D00000 = 1.101 × 2[2]

```
|✓ 40D00000 + C2EA0000|✓ 50A90000 – 4F480000|✓ 80200000  7AB80000|✓ FB380000  48C00000|
|---|---|---|---|

```
C2EA0000: 1100 0010 1110 1010 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 10000101 = 133 →𝑒= 133 −127 = 6 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.110101
```
  C2EA0000 = −1.110101 × 2[6]

```
𝑋= 1.101 × 2[2] −1.110101 × 2[6] = + [1.101] × 2[6] −1.110101 × 2[6] = (0.0001101 −1.110101) × 2[6]

2[4]


To subtract these numbers, we first convert to 2C:

𝑅= 0.0001101 −01.110101 = 0.0001101 + 10.001011 (2C addition)

The result in 2C is: 𝑅= 10.0100011, −𝑅= 01.1011101

_* Note that you can also do unsigned subtraction: 𝑋= −(1.110101 −0.0001101 −) × 2[6]_

For floating point, we need to convert to sign-and-magnitude:
 𝑅(𝑆𝑀) = −1.1011101

𝑋= −1.1011101 × 2[6], 𝑒+ 𝑏𝑖𝑎𝑠= 6 + 127 = 133 = 10000101
𝑋 = 1100 0010 1101 1101 0000 0000 0000 0000 = `C2DD0000`

```
0 0.0 0 0 1 1 0 1 +
1 0.0 0 1 0 1 1 0
1 0.0 1 0 0 0 1 1

```

✓ 𝑋 = 50A90000 – 4F480000:
```
  50A90000: 0101 0000 1010 1001 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 10100001 = 161 →𝑒= 161 −127 = 34 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.0101001
```
    50A90000 = 1.0101001 × 2[34]
  4F480000: 0100 1111 0100 1000 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 10011110 = 158 →𝑒= 158 −127 = 31 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.1001
```
    4F480000 = 1.1001 × 2[31]

```

𝑋= 1.0101001 × 2[34] −1.1001 × 2[31] = 1.0101001 × 2[34] − [1.1001] × 2[34]

2[3]

𝑋= (1.0101001 −0.0011001) × 2[34] (unsigned subtraction)

𝑋= 1.001 × 2[34], 𝑒+ 𝑏𝑖𝑎𝑠= 34 + 127 = 161 = 10100001
𝑋 = 0101 0000 1001 0000 0000 0000 0000 0000 = `50900000`

```
1.0 1 0 1 0 0 1 0.0 0 1 1 0 0 1
1.0 0 1 0 0 0 0

```

✓ 𝑋 = 80200000  7AB80000:
```
  80200000: 1000 0000 0010 0000 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 00000000 = 0 →𝐷𝑒𝑛𝑜𝑟𝑚𝑎𝑙 𝑛𝑢𝑚𝑏𝑒𝑟→𝑒= −126 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 0.01
```
    80200000 = −0.01 × 2[−126]
  7AB80000: 0111 1010 1011 1000 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 11110101 = 245 →𝑒= 245 −127 = 118 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.0111
```
    7AB80000 = 1.0111 × 2[118]

```

𝑋= (−0.01 × 2[−126]) × (1.0111 × 2[118]) = −0.010111 × 2[−8] = −1.0111 × 2[−10]
𝑒+ 𝑏𝑖𝑎𝑠= −10 + 127 = 117 = 01110101
𝑋 = 1011 1010 1011 1000 0000 0000 0000 0000 = `BAB80000`


✓ 𝑋 = FB380000  48C00000:
```
  FB380000: 1111 1011 0011 1000 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 11110110 = 246 →𝑒= 246 −127 = 119 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.0111
```
    FB380000 = −1.0111 × 2[119]
  48C00000: 0100 1000 1100 0000 0000 0000 0000 0000

```
𝑒+ 𝑏𝑖𝑎𝑠= 10010001 = 145 →𝑒= 145 −127 = 18 𝑆𝑖𝑔𝑛𝑖𝑓𝑖𝑐𝑎𝑛𝑑= 1.1
```
    48C00000 = 1.1 × 2[18]

```

-----

𝑋= − [1.0111 × 2][119] = − [1.0111] × 2[101]

1.1 × 2[18] 1.1

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

Alignment:

1.0111

= [1.0111]
1.1 1.1000 [= 10111]11000

Append 𝑥 = 4 zeros: 10111𝟎𝟎𝟎𝟎

11000


Integer division

𝑄= 1111 →𝑄𝑓= 0.1111


Thus: 𝑋= −0.1111 × 2[101] = −1.111 × 2[100]
𝑒+ 𝑏𝑖𝑎𝑠= 100 + 127 = 227 = 11100011

𝑋 = `1111 0001 1111 0000 0000 0000 0000 0000 =` `F1F00000`

### PROBLEM 4 (30 PTS)

- **Greatest Common Divisor (GCD): This circuit computes the GCD of two 𝑛-bit unsigned numbers (A, B). For example:**

✓ A = 216, B = 192 → GCD = 24. ✓ A = 132, B = 72 → GCD = 12. ✓ A = 169, B = 63 → GCD = 1.

- The digital system is depicted below (FSM + Datapath) for 𝑛= 8. This iterative circuit is based on Euclid’s GCD algorithm.
✓ Input Data: DA, DB Output data: GCD

|✓ A = 216, B = 192 → GCD = 24.|✓ A = 132, B = 72 → GCD = 12.|✓ A = 169, B = 63 → GCD = 1.|
|---|---|---|

```
s

```

**FSM**


done


✓ z=1 when 𝑎𝑖 = 𝑏𝑖, else z=0.

**Sequential Algorithm**
```
  a,b: unsigned integers
  while a  b
    if a > b
      a  a-b
    else
      b  b-a
    end
  end while
  return a

```
```
GCD

```
```
   DA DB

```
8 8
```
         L
   1 1
          Eb

```
E

9 9

b b

+/- '1' '1' +/
9

**SA**
```
      AlB

```
**next_a=SA[7..0]** `AlB = SA`

**next_b=SB[7..0]**


-----

- Sketch the Finite State Machine diagram (in ASM form) given the sequential algorithm (for 𝑛= 8). (18 pts.)
✓ The process begins when 𝑠 is asserted, at this moment we capture DA and DB on register 𝑎𝑖 and 𝑏𝑖 (respectively). Then

the process continues by updating 𝑎𝑖 and 𝑏𝑖 and it is concluded when 𝑎𝑖 = 𝑏𝑖. The signal done is asserted when the
result is computed and appears on output GCD.

Finite State Machine:


**FSM**


resetn=0



- Complete the timing diagram where 𝑛= 8. DA and DB are provided as unsigned decimals. You can provide 𝑎𝑖 and 𝑏𝑖 as
unsigned decimals. (12 pts.)

```
 clock
resetn
  s
  DA
  DB
  z
 AlB
state
 done

```
|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||
||||||||||||||||||||
||||||||||||||||||||
||||||||||||||||||||
||||||||||||||||||||
||||||||||||||||||||
||||||||||||||||||||
||||||||||||||||||||
|0|0|216|24|24|24|24|24|24|24|24|24|24|15|5|5|5|5|5|
||||||||||||||||||||
|0|0|192|192|168|144|120|96|72|48|24|24|24|10|10|5|5|5|5|
||||||||||||||||||||
||||||||||||||||||||
||||||||||||||||||||
||||||||||||||||||||
||||||||||||||||||||
|S1|S1|S2|S2|S2|S2|S2|S2|S2|S2|S2|S3|S1|S2|S2|S2|S3|S1|S1|
||||||||||||||||||||


-----

