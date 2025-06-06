10/30/2021

##### Problem M12.1: Networks-on-Chip

**Problem** **M12.1.A**

Consider a flow control method similar to circuit switching but where the request message 'reserves'
each channel for a fixed period of time in the future (for example, for 10 cycles since a reservation is
made). At each router along the path, a reservation is made if a request from a neighbor can be
accommodated. If the request cannot be accommodated a NACK is sent that cancels all previous
recommendations for the connection, and the request is retired. If a request reaches the destination, an
acknowledgement is sent back to the source, confirming all reservations.

Draw a time-space diagram of a situation that demonstrates the advantage of reservation circuit
switching over conventional circuit switching.


-----

10/30/2021

**Problem** **M12.1.B**

Determine whether the following oblivious routing algorithms are deadlock-free for the 2-D
mesh. There is only one virtual channel per link and no 180-degree turns are allowed for (c).

(a) Randomized dimension-order: All packets are routed minimally. Half of the packets are routed
completely in the X dimension before the Y dimension and the other packets are routed Y before X.

(b) Less randomized dimension-order: All packets are routed minimally. Packets whose minimal
direction is increasing in both X and Y, always route X before Y. Packets whose minimal direction
is decreasing in both X and Y, always route Y before X. All other packets randomly choose between
X before Y and vice versa.

(c) All packets are prohibited to take the two turns in dash:


-----

10/30/2021

##### Problem M12.2: Non-mesh Networks

We have the following network topology with 4 network nodes and 10 links.

#### A

 B D

 C

Note that each link is unidirectional, and only one link exists between A and C (only a link from C
to A (not from A to C), and only from D to B between B and D. Each link can transfer 1 flit per
cycle and there is only one virtual channel per link. For all parts, 180-degree turns are not allowed.

**Problem** **M12.2.A**

Fill in the following table of the properties of this network.

**Diameter**

**Average Distance**

**Bisection Bandwidth**

**Problem** **M12.2.B**

Draw the channel dependency graph of this network.

|Diameter|Col2|
|---|---|
|Average Distance||
|Bisection Bandwidth||


-----

10/30/2021

**Problem** **M12.2.C**

Is a minimal routing on this network deadlock-free? Show your reasoning and give a deadlock
scenario if it is not deadlock -free.

**Problem** **M12.2.D**

Now, we use a possibly non-minimal routing on this network. Plus, we prohibited the following
two movements on the non-minimal routing: 1) A to D then D to C and 2) B to C then C to D.

Is this routing deadlock-free? Show your reasoning and give a deadlock scenario if it is not
deadlock -free.

**Problem** **M12.2.E**

**Still having the two movements in M12.2.D prohibited, we added another restriction in routing:**
the link from C to A can be used only by packets generated at C, before the packets are
transferred to any other nodes (it should be the first link those packets ever take). Also, the link
from D to B can be used only by packets generated at D with the same condition (however, routes
may be non-minimal).

Is this routing deadlock-free? Show your reasoning and give a deadlock scenario if it is not
deadlock -free.


-----

10/30/2021

##### Problem M12.3: Network Effects (Spring 2014 Quiz 4, Part A)

You are choosing between several network topologies for your on-chip network, shown below.

Ring:

Mesh:

Binary tree:

Legend:


-----

10/30/2021

**Problem M12.3.A**

Your first task is to evaluate these topologies along several important dimensions. Fill in the
table below as a function of the number of nodes in the network, N. You can safely assume N is
an even power of 2, giving a complete mesh and binary tree. _For partial credit, give the_
_asymptotic growth instead._

|Col1|Ring|Mesh|Tree|
|---|---|---|---|
|Number of links||||
|Diameter||||
|Average distance||||
|Bisection bandwidth||||


-----

10/30/2021

In a sudden flash of inspiration, you decide to use the following topology:

Having decided upon a topology, you now want to make sure your system works properly. All
links are bidirectional.

**Problem M12.3.B**

Show how deadlock could arise in the network by drawing an example on the graph above.
Explain your answer in one or two sentences.


-----

10/30/2021


**Problem M12.3.C**

Draw the channel dependency graph (CDG) for your topology.

Show an example of how to eliminate routes to prevent deadlock on the CDG.


-----

10/30/2021

##### Problem M12.4: The Truth Will Set You Free (Spring 2014 Quiz 4, Part III)

**Problem M12.4.A** **Peanuts**

Snoopy coherence protocols rely on broadcast communication to detect sharing and updates.
These are conventionally implemented using bus networks that allow for one message to be sent
at a time to all nodes on the network.

Ben Bitdiddle is implementing a bus-based snoopy coherence protocol. One fifth of instructions
access memory, and one quarter of these miss in the core’s local cache (either because the line is
invalid or doesn’t have necessary permissions). Assuming each memory operation consists of a

! !

request and acknowledgement, the network traffic per core is therefore:

" [×] # [× 2 =]

! %&''()&'

!$ *+',-./,*0+[. Assume all messages fit within a single network flit. ]


Assuming a fixed IPC of 1, perfect bus arbitration, and infinite buffers, how many cores can the
bus support?


-----

10/30/2021

**Problem M12.4.B** **... To rule them all**

Ben needs to build a larger system than the bus network will allow, so he changes the system to
use a unidirectional ring network. In this design, the core issuing the memory operation sends the
request around the ring, and each node along the way either forwards the request or replaces it
with its response. Assuming fixed IPC of 1 and a single-cycle per hop in the network, at how
many cores will this design saturate?


-----

10/30/2021

**Problem M12.4.C** **Matryoshka**

Ben next explores the tradeoffs in cache design between an inclusive cache, where the parent
always has a copy of every line in the child’s cache, and non-inclusive caches, where this isn’t
guaranteed.

Give one advantage and one disadvantage of a non-inclusive cache design.


-----

10/30/2021

##### Problem M12.5: Network-on-chip (Spring 2015 Quiz 3, Part A)

**Problem M12.5.A**

Consider the router in Handout 16. Assume this router **has one virtual channel per physical**
**link. Suppose two packets, A and B, are traversing the router. Both are routed to output unit 2, as**
shown in the following waterfall diagram.

Before cycle 1, packet B’s head flit has finished RC and VA. In the following cycles, packet B’s
four flits traverse SA and ST without stalls. Packet A’s head flit completes routing computation
at cycle 1 and tries to allocate an output virtual channel starting at cycle 2. Unfortunately, the
only output virtual channel compatible with its route is occupied by packet B, so packet A’s head
flit fails to allocate a VC and is unable to make progress until packet B’s tail flit releases the VC.

Fill in the following table showing the state of packet A’s input virtual channel.

|Cycle|G|R|O|
|---|---|---|---|
|1|R|-|-|
|2||||
|3||||
|4||||
|5||||
|6||||
|7||||
|8||||


-----

10/30/2021

**Problem M12.5.B**

Suppose the router in Handout 16 is improved with **speculative switch allocation. Head flits**
attempt VC and switch allocation in the same cycle. If both succeed, the head flit traverses the
switch on the next cycle, as shown in the waterfall diagram below.

Consider the same scenario as in question 1, with packets A and B going to the same output unit.
Assume that **non-speculative switch allocation requests are always prioritized over**
**speculative ones (i.e., those from flits without a VC). Fill in the following waterfall diagram to**
show how packet A is routed.

|Cycle|1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|---|
|A: Head Flit|RC||||||||
|A: Body Flit 1|||||||||
|A: Body Flit 2|||||||||
|B: Body Flit 1|SA|ST|||||||
|B: Body Flit 2|-|SA|ST||||||
|B: Body Flit 3|-|-|SA|ST|||||
|B: Tail Flit|-|-|-|SA|ST||||


-----

10/30/2021

**Problem M12.5.C**

Consider the same speculative switch allocation optimization as in question 2. Unfortunately,
always prioritizing non-speculative switch allocation requests over speculative ones increases the
critical path too much, so we opt for a simpler switch allocator that is oblivious to whether
**requests are speculative.**

We want to analyze the performance of this simpler design under the following scenario:

  - All packets in the router are single-flit packets.

  - The probability that a packet successfully obtains a VC on its first try is 75%.

  - The probability that a flit successfully allocates the switch on its first try is 80%.

  - If a packet fails either virtual channel or switch allocation on its first try, it always

succeeds on its second try.

1) What percentage of allocated timeslots on the switch goes unused?

2) What is the average latency to go through this speculative router?

3) Briefly explain the effect of this optimization on network performance at both very low

loads and very high loads (near saturation).


-----

10/30/2021

**Problem M12.5.D**

Ben Bitdiddle wants to implement the Valiant routing algorithm, which routes each packet
through a randomly-chosen intermediate node. He uses routers with two virtual channels per
physical link. He decides to use X-Y routing between the source node and intermediate node,
and Y-X routing between the intermediate node and the destination node. However, Alyssa
points out this routing algorithm will not work without further modification. Explain why this is
the case and provide a solution for Ben.


-----

10/30/2021

##### Problem M12.6: Network-on-chip (Spring 2016 Quiz 3, Part D)

**Problem M12.6.A**

Determine whether the following routing algorithms are deadlock-free for a 2D-mesh. State your
reasoning.

a) (3 points) Randomized dimension-order: All packets are routed minimally. Half of the

packets are routed completely in the X dimension before the Y dimension, and the other
packets are routed in the Y dimension before the X dimension.

b) (3 points) Less randomized dimension-order: All packets are routed minimally. Packets

whose minimal direction is increasing in both X and Y always route X before Y. Packets
whose minimal direction is decreasing in both X and Y always route Y before X. All
other packets choose randomly between X before Y and vice-versa.


-----

10/30/2021

**Problem M12.6.B**

Consider the following topology:

# A B

 F C

 E D

(a) (2 points) What is the diameter of this topology?

(b) (2 points) What is the bisection bandwidth (in flits/cycle) of this topology?

(c) (5 points) Assume that 180-degree turns are prohibited. No other turns are prohibited. Show
how deadlock could arise in the given topology.


-----

10/30/2021

(d) (10 points) We now restrict all routes to be minimal and disallow the following turns on the
mesh (among the nodes A, B, E, D): north-to-east, north-to-west, south-to-east, south-to-west. Is
the routing strategy deadlock-free? Draw the CDG to justify your answer.


-----

