# Sample Final: CS 204 Advanced Computer Networks

 University of California, Riverside

 Fall 2023

 Name:

 Student ID:

**Question** **Points**

**1** **/??**

**2** **/??**

**3** **/??**

**4** **/??**

**5** **/??**

**6** **/??**

**7** **/??**

**Total** **100**

**Instructions:**

1. This examination contains 8 pages in total, including this page.

2. This is a sample final. It is used to give you a sense of what types of questions might appear in the
final. The actual final will have more questions.

3. You have three (3) hours to complete the examination.

4. Write your answers in this exam paper. The draft papers will not be accepted.

5. You are allowed to bring a one-page cheatsheet (US Letter Size, both-sided). You cannot use any
**electronics.**

6. Please finish the final independently. If you have any question, please raise your hand.

7. There will be partial credit for each question.

8. Best of luck!

|Question|Points|
|---|---|
|1|/??|
|2|/??|
|3|/??|
|4|/??|
|5|/??|
|6|/??|
|7|/??|
|Total|100|


-----

## Question 1: Short Questions

(a) Briefly explain what a Distributed Hash Table (DHT) is and how it is employed for Peer-to-Peer (P2P)
communication.

(b) List two deficiencies present in HTTP 1.1 and explain how SPDY (or HTTP/2) design addresses these
issues.

(c) Discuss common goals and considerations in designing a reliable transport layer protocol. Please
provide at least two goals. Subsequently, briefly describe how TCP CUBIC achieves these identified
goals.

(a) DHT distributes (key, value) pairs over millions of peers; Used by P2P to store the owner of different
data (i.e., key: hash of data; value: Peer ID that has data)

(b) Latency due to head-of-line blocking (SPDY: stream-based connection), Only client could initiate
request (SPDY: Server push allowed), Large header (SPDY: Compressed HTTP header), ...

(c) Efficient rate control (CUBIC: Window control using a cubic function), Fairness (CUBIC: window
growth function is independent of RTT), ...


-----

## Question 2: Cross-Layer Design

(a) Explain what constitutes a cross-layer design for network protocols. Provide an example (excluding
the exact example used in (c)) to illustrate this concept. Elaborate on its major advantage and
disadvantage.

(b) Given a scenario where the physical layer in a wireless network experiences significant disruption time
during handovers, discuss the potential issues this may introduce to TCP.

(c) Propose a cross-layer solution that addresses the limitation described in (b). That is, you could assume
TCP is aware of an incoming handover, and elaborate on how this new cross-layer approach allows
TCP to overcome the identified problem.

(a) Cross-layer design basically breaks the layered principle and let different protocols exchange information
to achieve certain design goal. There are many examples, and you mention anything that comes to
your mind. Some examples: TCP learns wireless throughput and adjusts congestion window, video
adapts bitrate based on wireless throughput, ... Cross-layer design could surely boost performance
given additional information, but will make the design unstable (e.g., only works in certain scenarios)
and unnecessarily complicated (extra interfaces among protocols, which is even considered impossible
in certain scenarios).

(b) Long disruption time might be considered as a timeout, while all packets are simply buffered and
waiting for handover to finish. That said, it could trigger a false packet loss indicator, and thus
negatively and unnecessarily affect congestion window.

(c) If TCP could be aware of the incoming handover, it could temporarily enlarge its timer to avoid
triggering timeout.


-----

## Question 3: Protocol Design Principles

As we mentioned in the lectures, often times the new protocol design is driven by physical layer innovation.
That said, let’s consider the following hypothetical new physical layer designs. Elaborate on how they might
impact the Link (or Transport, if necessary) layers. Develop a plan for designing protocols in these layers
considering the characteristics of the new PHY protocol. Feel free to base your designs on existing protocols.

(a) A new PHY protocol that offers exclusive access to the user but introduces very high latency.

(b) A new PHY protocol where multiple users share the channel, but the latency is exceptionally low.

(c) A new PHY protocol that has a substantial variance in both throughput and latency.

Note: There could be many answers to each question.

(a) The link layer no longer needs to handle collisions given the exclusive link; Long latency is not a major
issue if no one else is contending the channel. Long latency will be capture by TCP timer adjustment
which is based on RTT.

(b) Since latency is exceptionally low, link layer could consider a random-access-based approach, since the
penalty for collision and retx is very small.

(c) If latency variance is large, it might trigger more false timeouts on TCP. TCP might want to change
the timeout timer update algorithm to allow higher variance.


-----

## Question 4: Protocol Analysis

The following paragraphs are Wikipedia’s short description of a network protocol.

**The Resource Reservation Protocol (RSVP) is a transport layer protocol designed to reserve resources**
across a network using the integrated services model. RSVP operates over an IPv4 or IPv6 and provides
receiver-initiated setup of resource reservations for multicast or unicast data flows. It does not transport
application data but is similar to a control protocol, like Internet Control Message Protocol (ICMP) or
Internet Group Management Protocol (IGMP). RSVP is described in RFC 2205. RSVP can be used by
hosts and routers to request or deliver specific levels of quality of service (QoS) for application data streams.
RSVP defines how applications place reservations and how they can relinquish the reserved resources once
no longer required. RSVP operations will generally result in resources being reserved in each node along
a path. RSVP is not a routing protocol but was designed to interoperate with current and future routing
protocols.

**Types of messages**

Path messages (path): The path message is sent from the sender host along the data path and stores the
path state in each node along the path. The path state includes the IP address of the previous node, and
some data objects: sender template to describe the format of the sender data in the form of a Filterspec
sender tspec to describe the traffic characteristics of the data flow adspec that carries advertising data.

Reservation messages (resv): The resv message is sent from the receiver to the sender host along the reverse
data path. At each node the IP destination address of the resv message will change to the address of the
next node on the reverse path and the IP source address to the address of the previous node address on the
reverse path. The resv message includes the flowspec data object that identifies the resources that the flow
needs.

(a) Explore and identify potential usage scenarios where RSVP would be particularly beneficial.

(b) Given the description of RSVP, outline the possible steps a host needs to take when intending to send
a data flow with specific Quality of Service (QoS) using RSVP.

(c) Describe the modifications required for routers to support RSVP. (e.g., adding new capacity so it could
handle xxx messages, and execute yyy consequently)

(d) Examine the potential conflicts or compatibility issues RSVP might face when coexisting with other
transport layer protocols that run simultaneously.

Note: Just like this question - if an unfamiliar concept appears in the actual final, I will put description first
for your reference.

(a) Any applications with QoS requirement could potentially leverage RSVP: VoIP, video, AR/VR, ...

(b) (As long as the steps sound reasonable, the answer will be considered correct) 1) The host application
identifies and determines the QoS it requires; 2) It will notify RSVP protocol to create an object that
describes the traffic characteristics; 3) RSVP on host will send the “path” message with the object;
4) It waits for the “resv” message to confirm the successful reservation; 5) If no “resv” received after
certain timer, retransmit the “path”; ...

(c) Each router is expected to recognize “path” and “resv” messages. Router needs to follow “path” to
store path state and follow “resv” to reserve resources.

(d) You could discuss this from multiple perspectives: RSVP messages might be delivered over TCP if its
reliable deliver is requested; RSVP might cause fairness issue if co-exist with TCP, ...


-----

## Question 5: Network Layer

(a) Describe the key differences between Inter-AS (BGP) and Intra-AS routing.

(b) Recall that ISPs have two types of relationships in BGP: Peering and Transit. Peering ISPs jointly pay
for equipment and traffic costs. In Transit relationship, a payment is made from customer to provider
for both upstream and downstream traffic. Please consider the following ISP relationship figure (an
arrow points from the customer to the provider), and answer the following questions:

    - Can C see B through D or F?

    - Will traffic from A to D go through C, F, and/or E?

(c) Design a scheme for “mobile IPv4” that allows a host to seamlessly move from one subnet to another
without requiring an IP address change. You are free to involve as many network components as needed
in your design.

(a) Inter-AS routing decides the routes across different ASes, while intra-AS handles the routing within
single ASes. Inter-AS focuses more on policy, while intra-AS is performance-centric. (You could
mention other differences as well)

(b)  - C can see B through D, but not F. 1) F will not notify C that it could reach B. As a customer to
C, data between C and B through F will cost additional cost from F. 2) On the other hand, B is
D’s customer - for any data between C and B through D, B will pay D. As this is beneficial, D
will tell C that B is reachable.

    - For the same reason, A could see D through C, but not F. Besides, E will definitely let A and D
be visible to each other. This is because both will pay E if there’s traffic between A and D.

(c) There are multiple design ideas. One possible way is to use a translation service outside old and new
subnets. The service works as a global NAT - even when the user moves and changes the IP within
the subnet, the node will acquire the same global IP.


-----

## Question 6: Link Layer and Wireless

(a) Designing protocols for wireless networks is a complex task. Elaborate on two significant challenges
encountered in this process.

(b) Identify and explain if there are hidden or exposed terminals in the following scenarios

    - Consider A transmits to B, and if C transmits to D

    - Consider C transmits to D, and if A transmits to B

(c) Imagine your powerful smartphone with the capability to simultaneously transmit data over both WiFi
and 5G connectivity. WiFi offers superior performance but may be intermittently unavailable, while
5G is consistently accessible albeit with a higher loss rate. Assume you are on a moving bus, and an
HTTP protocol is downloading a very large webpage which takes at least 1 minute. Propose a new
link layer protocol that could intelligently select and utilize the available channels to achieve optimal
performance.

(a) Wireless and Mobility

(b) 1) C is a hidden sender; 2) B is an exposed receiver. For explanation you shall first describe what is
considered a hidden/exposed terminal, and put it in the context.

(c) Feel free to design your protocol. One possible way is, consider the always-on 5G connectivity to
transfer critical data such as ACK, so that packet loss could be quickly detected even when WiFi
certainly becomes unavailable. The actual data could be sent on both links, but prioritize WiFi when
it’s available.


-----

## Question 7: Paper Review

(a) Provide a brief overview of the networking-related technology discussed in the paper you presented.
Explain the significance of this technology in the networking domain.

(b) Outline two advantages and one limitation associated with the described technology.

(c) Consider a scenario where you send a packet from your smartphone to google.com. Discuss the potential
involvement of the technology you presented in the paper. Provide a concise explanation of how this
technology could or could not be relevant in the given context.

Answer the question based on your paper presentation.


-----

