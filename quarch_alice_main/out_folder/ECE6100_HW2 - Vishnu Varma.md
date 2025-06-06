###### ECE4100/ECE6100/CS4290/CS6290
 Advanced Computer Architecture
 Homework 2

________________________________________________________________________

###### Part A: Caches
-----------------------------------------------------------------------------------------------------------
###### Direct-mapped Cache

The following diagram shows how a direct-mapped cache is organized. To read a word from the
cache, the input address is set by the processor. Then the index portion of the address is decoded
to access the proper row in the tag memory array and in the data memory array. The selected tag
is compared to the tag portion of the input address to determine if the access is a hit or not. At the
same time, the corresponding cache block is read and the proper line is selected through a MUX.

= S
20
###### 25

**Input Address** **2[b]: cache line size (bytes)**

**Tag** **Index**

**.  .  .**

**Tag** **Status** **2[b-2]** **data words**

**•** **•** **Tag** **Data** **•** **•**

**•** **•** **Decoder** **Decoder** **•** **.  .  .** **•**

**•** **•** **•** **•**

**.  .  .**

**.  .  .**

**Valid Bit** **MUX**

**Comparator** **Data**

**Output Driver**

**Valid**
**Output Driver**

Figure A.1: A direct-mapped cache implementation

In the tag and data array, each row corresponds to a line in the cache. For example, a row in the
tag memory array contains one tag and two status bits (valid and dirty) for the cache line. For
direct-mapped caches, a row in the data array holds one cache line.
###### Four-way Set-associative Cache

|Tag|Index|Col3|Col4|Col5|
|---|---|---|---|---|

|Col1|Col2|
|---|---|
|Tag|Status|
|• • •|• • •|
|||

|Col1|. . .|Col3|
|---|---|---|
|2b-2 data words|||
|• • •|. . .|• • •|
||. . .||


-----

The implementation of a 4-way set-associative cache is shown in the following diagram. (An nway set-associative cache can be implemented in a similar manner.) The index part of the input
address is used to find the proper row in the data memory array and the tag memory array. In this
case, however, each row (set) corresponds to four cache lines (four ways). A row in the data
memory holds four cache lines (for 32-bytes cache lines, 128 bytes), and a row in the tag
memory array contains four tags and status bits for those tags (2 bits per cache line). The tag
memory and the data memory are accessed in parallel, but the output data driver is enabled only
if there is a cache hit.

**Input Address** **2[b]: cache line size (bytes)**

**Tag** **Index**

###### . . . . . . . .

**T** **S** **T** **S** **T** **S** **T** **S** **42[b-2]** **data words**

**•** **•** **•** **•** **•** **•** **•** **•** **Tag** **Data** **• • • •** **• • • •** **• • • •** **• • • •**

**•** **•** **•** **•** **•** **•** **•** **•** **Decoder** **Decoder** **• • • •** **• • • •** **• • • •** **• • • •**

**•** **•** **•** **•** **•** **•** **•** **•** **• • • •** **• • • •** **• • • •** **• • • •**

###### . . . . . . . .

**Valid Bit** **. .** **. .** **. .** **. .**

###### = = = = MUX MUX MUX MUX

**Comparator**

**Buffer Driver**

###### 
**Valid**
**Output Driver**

Figure A.2: A 4-way set-associative cache implementation

**Problem A.1:**

|Index|Col2|Col3|Col4|
|---|---|---|---|

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||T S|T S|T|S|T|S|
||• • • • • •|• • • • • •|• • •|• • •|• • •|• • •|
||||||||
||||||||
||||||||

|Col1|Col2|. .|Col4|Col5|. .|Col7|. .|Col9|. .|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||42b-2 data words||||||||||
||||||||||||
||• • • • • • • • • • • •||||• • • • • • • • • • • •||• • • • • • • • • • • •|• • • • • • • • • • • •|||
|||. .|||. .||. .||. .||
||||||||. .||||
|||. .|||. .||||||
||||||||||||

|-|-|Buffer -|
|---|---|---|
||||
||||


-----

N


###### &x 2 28 bit/cacheline 2 data words -> 6 = 5

We want to compute the access time of the direct-mapped (DM) cache. Assume a 128-KB cache
with 8-word (32-byte) cache lines. The data output is also 32 bits, and the MUX selects one word
out of the eight words in a cache line. Using the delay equations given in Table A.1, fill in the
column for the direct-mapped (DM) cache in the table. In the equation for the data output driver,
_‘associativity’ refers to the associativity of the cache (1 for direct-mapped caches, A for A-way_
_set-associative caches)._

Component Delay equation (ps) DM (ps) SA (ps)

Decoder 200(# of index bits) + 1000 Tag 3400 3000

Data 3400 3 [000]

Memory array 200log2 (# of rows) + Tag 4217 4250
200log2 (# of bits in a row) + 1000 Data 5000 5000

Comparator 200(# of tag bits) + 1000 1000 4400

=
8 N-to-1 MUX 500log2 N + 1000 2500 2500

Buffer driver 2000 2000

Data output driver 500(associativity) + 1000 1500 3000

Valid output 1000

1000 1000

driver

Table A.1: Delay of each Cache Component

What is the critical path of this direct-mapped cache for a cache read? What is the access time of
the cache (the delay of the critical path)? To compute the access time, assume that a 2-input gate
(AND, OR) delay is 500 ps. If the CPU clock is 150 MHz, how many CPU cycles does a cache

  
access take?

=
3400 [+][ 5000][ +][ 2500][ +][ 1500=12400ps]

###### Data [side] =
 Tag [side] : 3400 [+] 4217 + 4000 +500 [+][ 1000] 13117ps

|Component|Delay equation (ps)|Col3|DM (ps)|SA (ps)|
|---|---|---|---|---|
|Decoder|200(# of index bits) + 1000|Tag|3400|3000|
|||Data|3400|3 000|
|Memory array|200log (# of rows) + 2 200log (# of bits in a row) + 1000 2|Tag|4217|4250|
|||Data|5000|5000|
|Comparator|200(# of tag bits) + 1000||1000|4 400|
|N-to-1 MUX|500log N + 1000 2||2500|2 500|
|Buffer driver|2000|||2000|
|Data output driver|500(associativity) + 1000||1500|3000|
|Valid output driver|1000||1000|1000|


###### x10r12 x 150x106
=> CPU 13117
###### cycles=
 =1 1 96753 : es !
 cycles


###### way: 

###### Tag


###### 500 = 12150

+
###### 4250+ knoot


: +

###### side 3000 4250+
 ~

+
###### 3000/
 + [2000]


###### side


+ 1000 [+][ 1000]


=> citical


=
###### 12150+5000 [:][ 17150]

=>
###### 17150x150x106


-----

**Problem A.2:**

We also want to investigate the access time of a set-associative (SA) cache using the 4-way setassociative cache. Assume the total cache size is still 128-KB (each way is 32-KB), a 4-input
gate delay is 1000 ps, and all other parameters (such as the input address, cache line, etc.) are the
same as part A.1. Compute the delay of each component, and fill in the column for a 4-way setassociative cache in Table A.1.
###### #of [bits][ in][ a][ voc]

= [Co][ cache] line 3

=128x2

###### B =indexing = 10 bit =>- 2106 [its]

=

###### ↳s 32-10-3=it tag


###### each way


:
32kB 4 ways-128kB

= 32B
###### each [cache][ line]


:
###### ⑬B IK [sets]
 32B


: 10 bits to index


-----

###### yes SX16B= [27] achesize

**Problem A.3:**

Now George P. Burdell is studying the effect of set-associativity on the cache performance.
Since he now knows the access time of each configuration, he wants to know the miss-rate of
each one. For the miss-rate analysis, George is considering two small caches: a direct-mapped
cache with 8 lines with 16 bytes/line, and a 4-way set-associative cache of the same size. For the
set-associative cache, George tries out two replacement policies – least recently used (LRU) and
round robin (FIFO).

George tests the cache by accessing the following sequence of hexadecimal byte addresses,
starting with empty caches. For simplicity, assume that the addresses are only 12 bits. Complete
the following tables for the direct-mapped cache and both types of 4-way set-associative caches
showing the progression of cache contents as accesses occur (in the tables, ‘inv’ = invalid, and
the column of a particular cache line contains the {tag,index} contents of that line). _You only_
_need to fill in elements in the table when a value changes._


:

###### index 3 bits

=

6 H 6 its


=

line in cache hit? 9 1001

L2 L3 L4 L5 L6 L7 A =

###### 10

inv inv inv inv inv inv no

13 no

no

###### %

1A no 10

no

36 no

no

yes

yes

17 no

no

no

###### yes

|D-map Address|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
||line in cache||||||||hit?|
||L0|L1|L2|L3|L4|L5|L6|L7||
|110|inv|11|inv|inv|inv|inv|inv|inv|no|
|136||||13|||||no|
|202|20||||||||no|
|1A3|||1A||||||no|
|102|10||||||||no|
|361|||||||36||no|
|204|20||||||||no|
|114|||||||||yes|
|1A4|||||||||yes|
|177||||||||17|no|
|301|30||||||||no|
|206|20||||||||no|
|135|||||||||yes|

|Col1|D-map|
|---|---|
|Total Misses|10|
|Total Accesses|13|


-----

6 = 46 it

LRU

line in cache hit?

Set 0 Set 1

**way1** **Way2** **way3** **way0** **way1** **way2** **way3**

Inv Inv inv 11 inv inv inv no

11 13 no

no

1A no

10 no

36 no

yes

###### yes
 yes
17 no

30 no
###### yes
 yes

**4-way LRU**

8

13

FIFO

line in cache hit?

Set 0 Set 1

**way1** **way2** **way3** **way0** **way1** **way2** **way3**

Inv Inv inv 11 inv inv inv no

13 no

no

1A no

10 no

36 no

yes

###### yes
 yes
17 no

no

20 no

###### yes

**4-way FIFO**

|4-way Address|LRU|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
||line in cache||||||||hit?|
||Set 0||||Set 1|||||
||way0|way1|Way2|way3|way0|way1|way2|way3||
|110|inv|Inv|Inv|inv|11|inv|inv|inv|no|
|136|||||11|13|||no|
|202|20||||||||no|
|1A3||1A|||||||no|
|102|||10||||||no|
|361||||36|||||no|
|204|||||||||yes|
|114|||||||||yes|
|1A4||||||||||
|177|||||||17||yes no|
|301|||30||||||no|
|206|||||||||yes|
|135|||||||||yes|

|Col1|4-way LRU|
|---|---|
|Total Misses|8|
|Total Accesses|13|

|4-way Address|FIFO|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
||line in cache||||||||hit?|
||Set 0||||Set 1|||||
||way0|way1|way2|way3|way0|way1|way2|way3||
|110|inv|Inv|Inv|inv|11|inv|inv|inv|no|
|136||||||13|||no|
|202|20||||||||no|
|1A3||1A|||||||no|
|102|||10||||||no|
|361||||36|||||no|
|204|||||||||yes|
|114|||||||||yes|
|1A4||||||||||
|177|||||||17||yes no|
|301|30||||||||no|
|206||20|||||||no|
|135|||||||||yes|

|Col1|4-way FIFO|
|---|---|
|Total Misses||
|Total Accesses|is|


-----

**Problem A.4:**

Assume that the results of the above analysis can represent the average miss-rates of the directmapped and the 4-way LRU 128-KB caches studied in Problems A.1 and A.2. What would be
the average memory access latency in CPU cycles for each cache (assume that a cache miss takes
20 cycles)?

cache [hit][ takes][ :][ 3] cycles

###### DM : + : 17 . 3846 ISOMHz
 - AMAT 2 110113) [(20)] cycles &

=18
###### cycles

 ↳-way + [=] 15 .3076 AMAT= [3] cycles &150MHZ
 LRU (8/13) (20)
=I6
###### - cycles

Which one is better?

set anociative cache is better !
###### ↳-way [LRU]

For the different replacement policies for the set-associative cache, which one has a smaller
cache miss rate for the address stream in Problem A.3? Explain why. Is that replacement policy
always going to yield better miss rates? If not, give a counter example using an address stream.


###### LRUS [FIFO] for[ the] given


address stream
!


###### counter example ! - in the
 20n-114-14 instead
above of
###### In [the] example
 stream if we had 100-361-1AU [then][ 204] address
 would would be evicted in LRU but if the initial entry

.

FIFO
be 102-113-202 [then] 20 [would] stay [in]

FIFO would be better than LRU so it is
###### stream In [this]
 better
not [fixed][ which][ is]

110 136 102 [-1A3-202-361-104-361-1A4-177-301-206-135]


-----

###### Part B: Multi-Level Caches
-----------------------------------------------------------------------------------------------------------
Suppose we have a physically-indexed, physically-tagged L1 cache.
All physical addresses are 12 bits. The L1 cache is direct-mapped, and has 4 sets.

       
The block size is 16 bytes.

i = 2
###### 4

**Problem B.1:** tagiz-2-4=
L1 Cache Size = ____________ bytes Ch 16B x 4 =
Index Size = ____________ bits bB

###### ⑤

Tag Size = ____________ bits


6 bit


**Problem B.2:**

Table B-1 tracks the contents of the L1 cache for a sequence of memory accesses.
The first entry shows the initial state of the cache.
**“X” represents an invalid/empty entry.**
To simplify things for you, valid entries in the cache are represented by the {Tag, Index}.

Complete the Table for the given sequence of addresses. The first two have been filled for you.
_You only need to fill the elements in the Table when a value changes, except for the “L1 Hit?”_
_column which needs to be filled out for all accesses._

**Access** **L1 Hit?** **L1 State after Access**

**Address** (Yes/No) {Tag, Index}

**Set0** **Set1** **Set2** **Set3**

... … X 45 F6 X

0x7B0 No 7B

10
###### I

1 180 0xDC4 No DC

0xDCF

1100- yes

0xF3C

###### 001 NO F3

0x8CB

1100 NO 82

0xB8B

1000- NO B8

**Table B-1: Contents of L1 Cac**

|Access Address|L1 Hit? (Yes/No)|L1 State after Access {Tag, Index}|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||Set0|Set1|Set2|Set3|
|...|…|X|45|F6|X|
|0x7B0|No||||7B|
|0xDC4|No|DC||||
|0xDCF|yes|||||
|0xF3C|NO||||F3|
|0x8CB|NO|82||||
|0xB8B|NO|B8||||


-----

**Problem B.3:**

In the current design, all misses from L1 need to go to Memory which takes hundreds of cycles.
To reduce the penalty of a L1 miss, we add an L2 cache after the L1 cache.

Now every L1 miss first performs a L2 lookup. If the line is found in L2, it is sent to L1. If not, it
is brought in from Memory.

We follow an Exclusive L2 policy: All lines in L1 CANNOT be present in L2 (i.e., L1 fills do
not result in L2 fills).

Assume that the L2 cache is 4-way set-associative, with 2 sets.
The block size is the same (16 bytes).

Fill out the L1 and L2 cache contents for the given access pattern.
The initial state of the L1 and L2 in each case is given to you.
“X” represents an invalid/empty entry.
Valid entries are represented by the {Tag, Index}.

**Each L2 entry also tracks its insertion time/last access time in order to implement LRU**
**replacement within each set.**
**The LRU way is the candidate for replacement only if all ways have valid data, otherwise**
**any of the ways with invalid data is replaced.**

_You only need to fill the elements in the Table when a value changes, except for the “L1 Hit?”_
_and “L2 Hit” columns which needs to be filled out for all accesses._


-----

###### Exclusive L2

_All lines in L1 should NOT be present in L2_

**Time** **Access** **L1** **L1 State after access** **L2**

**Unit** **Addr** **Hit?** {Tag, Index} **Hit?**

(Yes/ **Set0** **Set1** **Set2** **Set3** (Yes/ **Set0**

No) No/

NA)

**Way0 Way1 Way2 Way3 Way0 Way1**

… X 45 F6 X 90 (7) 8C (3) X

10 0x7B0 No 7B No

11 0xDC4 No DC No

12 0xDCF

Yes

13 0xF3C

NO F3 No

14 0x8CB

No 8C Yes X DClin)

15 0xB8B

NO B8 NO 80(is)

**Table B.2 : Contents of L1 and Excusive L2 Caches**

|Time Unit|Access Addr|L1 Hit? (Yes/ No)|L1 State after access {Tag, Index}|Col5|Col6|Col7|L2 Hit? (Yes/ No/ NA)|Exclusive L2 State after access {Tag, Index} (Access Time)|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||Set0|Set1|Set2|Set3||Set0||||Set1||||
|||||||||Way0|Way1|Way2|Way3|Way0|Way1|Way2|Way3|
|…|||X|45|F6|X||90 (7)|8C (3)|X|X|47(4)|4B(6)|E0(7)|X|
|10|0x7B0|No||||7B|No|||||||||
|11|0xDC4|No|DC||||No|||||||||
|12|0xDCF|Yes||||||||||||||
|13|0xF3C|NO||||F3|No|||||||zB(13)||
|14|0x8CB|No|8C||||Yes||X|DClin|)|||||
|15|0xB8B|NO|B8||||NO||80(is|)||||||


-----

###### Part C: Memory Hierarchy
-----------------------------------------------------------------------------------------------------------
**[All addresses in this Part at Physical Addresses].**
Suppose we are running the following code:
#define ARRAY_SIZE 4
for (int i = 0; i < ARRAY_SIZE; i++) {
S[i] = P[i] + Q[i]

}
The arrays S, P and Q have 4 entries each, and hold integer values (4 bytes at each entry).
The memory addresses for each are shown below:

Suppose this code translates to the following assembly instruction sequence.
**// Initial values:**
**// Rp = 0x1A20, Rq = 0x1C60, Rs = 0x2BA0**
**// Ri = 4**

**loop:** **LD R1, (Rp)** **// R1  Mem[Rp]**

**LD R2, (Rq)** **// R2  Mem[Rq]**

**ADD R3, R1, R2** **// R3 = R1 + R2**

**ST R3, (Rs)** **// Mem[Rs]  R3**

**ADDI Rp, 4** **// Rp  Rp + 0x4**

**ADDI Rq, 4** **// Rq  Rq + 0x4**

**ADDI Rs, 4** **// Rs  Rs + 0x4**

**SUBI Ri, 1** **// R4  R4 – 1**

**BNEZ Ri, loop** **// if R4 != 0, branch to loop**

This code produces the following 12 memory accesses to the cache hierarchy:
LD 0x1A20
LD 0x1C60
ST 0x2BA0
LD 0x1A24
LD 0x1C64
ST 0x2BA4


-----

LD 0x1A28
LD 0x1C68
ST 0x2BA8
LD 0x1A2C
LD 0x1C6C
ST 0x2BAC

We will construct multiple memory hierarchies and analyze the miss rates for each.


-----

###### Question C-1
Consider the following cache hierarchy with a L1 connected to a L2, which is connected to
DRAM.


All cache lines are 16B.
The L1 is Direct Mapped, with 4 sets. u
The L2 is 2-way Set Associative, with 4 sets.
The L2 is Non-Inclusive with L1.
The Non-Inclusion policy is as follows:


###### oh
, [zoit]



  - All L1 allocations also result in L2 allocations

  - All L1 evictions result in L2 allocations

  - L2 evictions do not result in L1 evictions

L1 is write-through with respect to L2 → i.e., any writes to addresses in L1 propagate data to
**L2 at the same time. Thus only the data in L2 is considered dirty.**
L2 is a write-back cache with respect to DRAM → **dirty data from L2 has to be written back**
**to DRAM when the line gets evicted.**

###### Question C-1.1 
On the next page, the initial state of the L1 and L2 are given. Dirty data is circled in L2.
Update the state of the L1 and L2 for each of the accesses. For each entry you can write the {tag,
index} for simplicity and circle the dirty data. The writeback column specifies the cache line
whose data is being written back to DRAM.


-----

###### 10 10 [10] oodex ! 
11

**Access** **L1 State After Access** **Non-Inclusive L2 State After Access** **Write-**

**{tag, index}** **{tag, index}** **back**

**Hit?** **Set 0** **Set 1** **Set 2** **Set 3** **Hit?** **Set 0** **Set 1** **Set 2** **Set 3**
**(Yes** **(Yes/**

**/** **No/** **Way 0 Way 1 Way 0 Way 1 Way 0 Way 1 Way 0 Way 1**

**No)** **NA)**

0x110 0x1A5 0x11E 0x1BB 0x110 0x11E 0x1BB

LD 0x1A20

NO 0x1A2 No 0X 1A2

LD 0x1C60

###### No OXIC6 No OXIC6 Ox IIE

ST 0x2BA0

No OX IB A No OXCBA
###### ⑧

LD 0x1A24

NO OX [1A2] No 0x1A2

LD 0x1C64

NO OXIC6 NO OXICG OX 2B A

ST 0x2BA4

No OXZBA No OX2B
###### &[A]

LD 0x1A28

NO 0x 1A2 NO OX 1A2

LD 0x1C68

###### No OX [1C6] NO 0x1[6 0x 2BA

ST 0x2BA8

NO OX2BA No
###### ⑭BA

LD 0x1A2C

No OX1A2 No 0X1A2

LD 0x1C6C

NO OXIC6 NO OXICG OX2BA

ST 0x2BA0C

###### No OX2BA NO BA

|Col1|Access|L1 State After Access {tag, index}|Col4|Col5|Col6|Col7|Non-Inclusive L2 State After Access {tag, index}|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Writ back|e-|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||Hit? (Yes / No)|Set 0|Set 1|Set 2|Set 3|Hit? (Yes/ No/ NA)|Set 0||Set 1||Set 2||Set 3||||
|||||||||Way 0|Way 1|Way 0|Way 1|Way 0|Way 1|Way 0|Way 1|||
||||0x110|0x1A5|0x11E|0x1BB||0x110||||0x11E|||0x1BB|||
|L|D 0x1A20|NO|||0x1A2||No||||||0X 1A2|||||
|L|D 0x1C60|No|||OXIC6||No|||||OXIC6||||II Ox|E|
|S|T 0x2BA0|No|||OX IB A||No||||||⑧ OXCBA|||||
|L|D 0x1A24|NO|||OX 1A2||No|||||0x1A2||||||
|L|D 0x1C64|NO|||OXIC6||NO||||||OXICG|||OX 2B|A|
|S|T 0x2BA4|No|||OXZBA||No|||||& OX2BA||||||
|L|D 0x1A28|NO|||0x 1A2||NO||||||OX 1A2|||||
|L|D 0x1C68|No|||OX 1C6||NO|||||0x1[6||||0x 2|BA|
|ST|0x2BA8|NO|||OX2BA||No||||||⑭BA|||||
|LD|0x1A2C|No|||OX1A2||No|||||0X1A|2|||||
|LD|0x1C6C|NO|||OXIC6||NO||||||OXICG|||OX2|BA|
|ST|0x2BA0C|No|||OX2BA||NO|||||B A||||||


-----

###### Question C-1.2 
What is the L1 Miss Rate (L1 Misses/L1 Accesses) ?

100%

###### Question C-1.3
What is the L2 Miss Rate (L2 Misses/L2 Accesses) ?

100
###### 
 Question C-1.4 
How many times does a write back from the L2 to the DRAM take place?

↳ [times]

###### Question C-2
We add a Victim Cache next to the L1 cache:

All evicted data from L1 goes to L2 as before, but a copy is also retained in the Victim Cache.
The victim cache has 4 entries, and is fully associative.
Upon a L1 miss, first the Victim Cache is checked, before going to L2.
**IF THE DATA IS FOUND IN EITHER THE DIRECT MAPPED CACHE OR THE**
**VICTIM CACHE, IT IS CONSIDERED A L1 HIT.**
The line is brought into L1 and the evicted line from L1 is added to the Victim Cache. Victim
Caches are Exclusive with respect to L1 – i.e., either L1 or the Victim Cache will have a cache
line, never both.


-----

###### Question C-2.1 
Suppose L1 has an overall hit rate of 90%. Of these hits, 70% hit in the direct mapped cache and
take 1-cycle, while 30% hit in the victim cache and take 4 cycles. A L1 miss takes 50 cycles to
bring the data into L1. What is the average memory access time?

###### AMAT [=] 0 . 9x0 [-] 7(1) [+] 0 . 9x0 [.] 3 (1+4) +0 . 1x50

= 6 . 5 cycles

###### 
 Question C-2.2
Update the state of the L1 and Victim Caches for the same set of memory accesses.


-----

NO OX [1A2] Yes X 0x 2 B A

|Access|L1 State After Access {tag, index}|Col3|Col4|Col5|Col6|Victim Cache State After Access {tag, index}|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||Hit? (Yes/ No)|Set 0|Set 1|Set 2|Set 3|Hit? (Yes/ No/ NA)|Way 0|Way 1|Way 2|Way 3|
|||0x110|0x1A5|0x11E|0x1BB||||||
|LD 0x1A20|No|||Ox 1A2||NO|OX1IE||||
|LD 0x1C60|wo|||0x IC6||No||0x1A2|||
|ST 0x2BA0|NO|||Ox 2B|A|No|||0x 1C6||
|LD 0x1A24|NO|||0x1A2||Yes||X||OXIBA|
|LD 0x1C64|NO|||OX1C6||yes||1A2 ox|X||
|ST 0x2BA4|NO|||OXIBA||yes|||OXIC6|X|
|LD 0x1A28|wo|||OX1A2||Yes||X||0x2BA|
|LD 0x1C68|NO|||0x1[6||yes||OX1A2|X||
|ST 0x2BA8|NO|||OXCBA||yes|||0x1C6|X|
|LD 0x1A2C|NO|||OX 1A2||Yes||X||0x 2 B A|
|LD 0x1C6C|NO|||Ox 1C6||Yes||OX1A2|X||
|ST 0x2BA0C|NO|||OX2BA||yes|||OXIC6|X|


-----

###### Question C-2.3 
What is the L1 Miss Rate (L1 Misses/L1 Accesses) ?

: 25 %

###### -12

 Question C-2.4
George P. Burdell is interested in designing a memory hierarchy optimized for this code.
He looks at the memory access pattern and the L1 Miss Rate and believes that he can
reduce it even further without increasing the size of any of the caches. His solution is to
reduce the size of the Victim Cache to two entries, and use the remaining two entries for
some other structure connected to L1, as shown below.


What structure do you think George has in mind? Briefly describe the function of this
structure, and a recipe to allocate it and access it.

###### From [the] previous part only [the][ initial] compulsory misses were seen
 all others were hit, in [order][ to] reduce the misses we compulsory

can [add][ a] access the initial addresses .
###### prefetcher [to] required

Even [with][ this][ method][ there][ will][ be] one miss [but] it i a better

###### design

11


-----

###### Part D: Hierarchical Page Table & TLB
-----------------------------------------------------------------------------------------------------------
Suppose there is a virtual memory system with 64KB page which has 2-level hierarchical
page table. The physical address of the base of the level 1 page table (0x01000) is stored
in a special register named Page Table Base Register. The system uses 20-bit virtual
address and 20-bit physical address. The following figure summarizes the page table
structure and shows the breakdown of a virtual address in this system. The size of both
level 1 and level 2 page table entries is 4 bytes and the memory is byte-addressed.
Assume that all pages and all page tables are loaded in the main memory. Each entry of
the level 1 page table contains the physical address of the base of each level 2 page
tables, and each of the level 2 page table entries holds the PTE of the data page (the
following diagram is not drawn to scale). As described in the following diagram, L1
index and L2 index are used as an index to locate the corresponding 4-byte entry in Level
1 and Level 2 page tables.

**2-level hierarchical page table**

A PTE in level 2 page tables can be broken into the following fields (Don’t worry about
status bits for the entire part).

↳ [bits]

12


-----

**Problem D.1:**

Assuming the TLB is initially at the state given
below and the initial memory state is to the right,
what will be the final TLB states after accessing the
virtual address given below? Please fill out the table
with the final TLB states. You only need to write
VPN and PPN fields of the TLB. The TLB has 4 slots
and is fully associative and if there are empty lines
they are taken first for new entries. Also, translate the
virtual address (VA) to the physical address (PA).
**_For your convenience, we separated the page_**
**_number from the rest with the colon “:”._** 
.

**VPN** **PPN** ->

0x8 0x3

###### 
**Initial TLB states**

18 [bitt]

###### -anything

18

**Virtual Address:** = 2

11 [2]

######   0xE:17B0  (1110:0001011110110000)
 pa 3 positions

|VPN|PPN|
|---|---|
|0x8|0x3|
|||
|||
|||


###### 
->

###### 

**VPN** **PPN** 100 -> 0x0y : [1020]

0x8 0x3

11 0000
OXE OXS 10
01

00

,

**Final TLB states**

###### 000a

: 6

VA 0xE17B0 => PA  ___________________  OXS 17 BO

|VPN|PPN|
|---|---|
|0x8|0x3|
|OX E|OX S|
|||
|||


13


-----

**Problem D.2:**

What is the total size of memory required to store both the level 1 and 2 page tables?

21 : lines each HB

###### -[Total][ :]
 ↳ [:] B = 16t64=
#### *

###### ⑪B

**Problem D.3:**

George Burdell wanted to reduce the amount of physical memory required to store the
page table, so he decided to only put the level 1 page table in the physical memory and
use the virtual memory to store level 2 page tables. Now, each entry of the level 1 page
table contains the virtual address of the base of each level 2 page tables, and each of the
level 2 page table entries contains the PTE of the data page (the following diagram is not
drawn to scale). Other system specifications remain the same. (The size of both level 1
and level 2 page table entries is 4 bytes.)

###### 
**George’s design with 2-level hierarchical page table**

14


###### -


-----

Assuming the TLB is initially at the state given
below and the initial memory state is to the right
(different from Problem C.1), what will be the final
TLB states after accessing the virtual address given
below? Please fill out the table with the final TLB

###### - 
states. You only need to write VPN and PPN fields
of the TLB. The TLB has 4 slots and it is fully ->
associative and if there are empty lines they are taken
first for new entries. Also, translate the virtual
address to the physical address. Again, we separated ->
**_the page number from the rest with the colon “:”._**
.

**VPN** **PPN**

0x8 0x1

###### I

**Initial TLB states**         
|VPN|PPN|
|---|---|
|0x8|0x1|
|||
|||
|||


###### - 
 ->

->

###### I
 

###### -> Ox 2 : 0010

**Virtual Address:** 
###### virtual [address]
 0xA:0708  (1010:0000011100001000)
 pT2 ox 0010
p [:] Pz

:

**VPN** **PPN** E0x8 1038 ->

0x8 0x1 -> 0x1 : 1038

###### - physical 0x2 0x1 address

Ox [A] OXE
###### 12 base


: 10

|VPN|PPN|
|---|---|
|0x8|0x1|
|0x2|0x 1|
|Ox A|OX E|
|||


**Final TLB states**

VA 0xA0708 => PA  _______________________ 0xF [:] 0708


=>
###### physical address


###### P2


:
###### 1040


###### ox 1


:
###### 1038

, [-0x1]

0 X [1] : 0 FFF


###### now, 0x1 : 0010, p2 = 2

:

ox 1 0018 -0010

15

###### oo ↳
## I


-----

**Problem D.4**

Buzz examines George’s design and points out that his scheme can result in infinite loops.
Describe the scenario where the memory access falls into infinite loops.

###### when [the] UPN to PPN translation from the VA obtained
 at LI to PA [to] be found at Le is not a TIB hit
 infinite an then this access pattern [will][ them][ into]

.

###### loop iterating [over][ and][ over]
 if [the] VPN of both [the][ initial] address and Lolp .
 hit->so to be a [TLB] loop vA is [the] same [there][ won't]

**Problem D.5**

Suppose we design a physically tagged, virtually indexed 2-way set associative cache that
we want to access in parallel to the TLB. Suppose the cache line size is 64B. What is the
largest possible cache we can design, and how many sets would it have?


###### 64B = 6 = 6 it can [have] 2 sets

= Iksets
###### Is !
 p offset bit

=>

###### [cache] largest possible
 k [+][ 6] = P

=> '
2                      - 2x64 B
=> +
k 6 16 -> [#][ of][ index][ bits]

###### x[=][ 10] =
 2 [+] B    
###### 0
 =128KB [cache] 
16


-----

