Name: ____________________________

**CS 6/75101** **Midterm Exam #2** **Adv. Comp. Arch.**

**Monday 4 April 2011**

**This test is open-book, open-notes, meaning you may look at any paper notes that you have**
**brought with you. You may NOT share your notes with a friend.  You may NOT use your**
**cell phone, or talk to a friend.  Since you have access to the papers discussed in class, be**
**careful to answer the question that was asked instead of copying text from the paper that**
**may or may not answer the question.**

**1.** **One of the primary tasks in high-level synthesis is what was first called control step**

**allocation, and later called scheduling. Give a short, concise, one-paragraph definition**
**of this task, preferably in your own words. (10 points)**

Control step scheduling is the assignment of operations (usually represented in a directed
acyclic graph) to control steps, where each control step corresponds to a state or machine
cycle. All of the operations in a control step execute concurrently, and then execution
proceeds to the next step. Scheduling is often done to minimize some parameter such as
schedule length, hardware used, or power consumed. (Note that this question only asked
about scheduling, not about functional unit allocation.)

**2.** **The DAA design automation system attempted to capture human knowledge about how**

**to design hardware from a behavioral description. Give a high-level overview of how**
**this system was organized. (10 points)**

It was an expert system, organized as a working memory, rule memory, and rule interpreter.
The working memory represented the design as it was being constructed – the functional
units, registers, interconnections, etc. The rule memory represented the rule, each stating that
if some condition is true, then modify the design in a specific way. Finally, the rule
interpreter matched the working memory against the rules to determine which rules were
applicable, and if more than one match was found, chose the most specific rule to apply.

**3.** **One of the major motivations for high-level synthesis, and the more complex tools that**

**followed, was to shorten the design cycle and search the design space. What do these**
**phrases mean, and why is this motivation important to companies? (10 points)**

To “shorten the design cycle” means reducing the time taken to design a product, thus getting
that product to the market more quickly. “Searching the design space” means trying and
comparing various design alternatives to find the best one, which is also possible with a short
design cycle. Taken together, they mean a company can explore several design alternatives


-----

Name: ____________________________

in a short period of time, produce and test one of those designs, and get a new product to
market every 12-18 months.

**4.** **What is the basic trade-off between list scheduling and force-directed scheduling? (10**

**points)**

Given a set of functional units, list scheduling minimizes the schedule length, whereas given
a schedule length, force-directed scheduling minimizes the number of function units. Thus
one tries to make the design faster, while the other tries to make the design smaller. (Note
that simply repeating the definitions back to me does not really answer the question asked.)

**5.** **What additional features are present in a hardware description language like VHDL**

**that are not present in programming languages like C or Pascal? (10 points)**

Sequential versus concurrent statements, modeling of clock signals, bit widths, increased
emphasis on hardware operators (e.g., shifts, rotates), 7 “states” for a “binary” variable, etc.
Further, these HDLs allow the hardware to be described at multiple levels of abstraction.

**6.** **A basic field-programmable logic device module has either an AND-OR array or a**

**lookup table, followed by a register, and the structure of that AND-OR array, lookup**
**table, and register can be customized. Multiple copies of that module are then**
**combined into a higher level module, and all of the interconnections can be customized.**
**What are the advantages of providing this customizability, and what are the**
**disadvantages? (20 points)**

Advantages: Designing and producing the chip is very quick so it is cost-effective to order
chips in small quantities, making it possible for small companies to produce and sell lowvolume products that contain customized hardware. Further, chips can be purchased easily
as commodity items instead of as custom orders, and can be purchased in various packages
and speed grades. This large selection of options means it is less likely that the customer will
have to pay for unneeded functionality on the chip.

Disadvantages: Providing all of this customizability adds chip area (unused components,
extra area for all the “fuses”). This means less of the chip is available to perform the
designed functionality, so for given functionality FPGAs may be larger than ASICs.
Furthermore, these customization points add delay, meaning FPGAs may be slower than
ASICs. Finally, if the chips are needed in very large quantities (large enough that the fixed
costs can be recovered), ASICs are cheaper than FPGAs.

**7.** **Summarize the basic methods for programming an interconnection point in a field-**

**programmable logic device. That is, if it is necessary to connect, or not connect, two**
**wires, what are the hardware options to do that? (10 points)**


-----

Name: ____________________________

Wires can be connected using anti-fuses – the connection is normally broken, but when
sufficient current is applied, the connection is made. Wire is essentially melted to connect
two points.

Wires can also be connected using memory bits – if the bit is 1, there is a connection, and if it
is 0, there is no connection. All of the normal memory technologies can be used – RAM,
ROM, EPROM, and EEPROM.

**8.** **What is an embedded system, an embedded control system, and an instruction set**

**processor? Definite these terms, and explain how they are different.  (20 points)**
**(CONTINUE YOUR ANSWER ON THE NEXT PAGE)**

An embedded system is part of a large system -- “embedded” as part of that larger system
and providing some functionality to that system.

An embedded control system provides control and monitoring functions, typically
monitoring external physical conditions through sensors, and controlling physical objects
through actuators

An instruction set processor is a programmable device such as a microprocessor or
microcontroller that can be programmed by an end user or application developer, and thus
can be used to implement a wide range of functionality.

Processors for embedded systems are typically much less expensive than instruction set
processors, and may have more stringent power requirements. They are usually available as
processors cores that can be placed onto a system on a chip, rather than as separate
components.


-----

