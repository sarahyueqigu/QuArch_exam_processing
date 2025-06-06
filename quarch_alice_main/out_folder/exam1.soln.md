Name: ____________________________

**CS 6/75101** **Midterm Exam #1** **Adv. Comp. Arch.**

**Monday 7 March 2011**

**This test is open-book, open-notes, meaning you may look at any paper notes that you have**
**brought with you. You may NOT share your notes with a friend.  You may NOT use your**
**laptop, your cell phone, or talk to a friend.  Since you have access to the papers discussed**
**in class, be careful to answer the question that was asked instead of copying text from the**
**paper that may or may not answer the question.**

**1.** **Many early computers, such as the VAX, supported memory-memory instructions,**

**while in later computers, memory-register or register-register instructions became**
**more common. What is a memory-memory instruction, and what are its**
**disadvantages? (5 points)**

A memory-memory insruction reads its operands directly from memory, performs the
operation, and writes its results back to memory.

The primary disadvantage is that memory operations are very slow, and in worst case, may
require two full memory reads (if those operands are not available in the cache) plus a
memory write. A secondary disadvantage is that the instruction contains three full memory
addresses, and thus requires a very large instruction format.

**2.** **The Digital Equipment Corporation VAX, quite possibly the epitome of CISC**

**architectures, supported an instruction to evaluate a floating point polynomial to an**
**arbitrary degree. This sounds like a really useful instruction — why did later**
**processors such as the Intel Pentium, Alpha 21164, etc. not support powerful**
**instructions like this? (5 points)**

These highly-specific but rarely-used instructions were rarely supported by compilers, which
concentrated more on supporting a smaller set of more frequently used instructions.

**3.** **Unlike the Intel 486, the Intel Pentium supported superscalar execution. What**

**functionality was added by this superscalar execution, and what were its limitations?**
**(10 points)**

It allowed two “simple” integer instructions and one floating point instruction to execute in
parallel. The integer instruction in the V pipeline was limited to ALU operations, memory
references, and jumps, while the one in the U pipeline could also include barrel shifting.


-----

Name: ____________________________

Instructions with some kinds of data dependencies could be executed in parallel, but not all
data dependencies. Resource dependencies and control dependencies must also be avoided.

**4.** **As defined by David Patterson, RISC computers had a register-register LOAD/STORE**

**architecture, had a reduced instruction set and addressing modes, had simple**
**instruction formats, and avoided pipeline penalties. How did the architecture avoid**
**pipeline penalties, and what were the implications of this solution? (10 points)**

It redefined branch operations to perform the branch after the following instruction instead of
after the current instruction, in what they called a “delayed branch”. This meant the
instruction following the branch would either need to be an instruction that would have
otherwise execute before the branch, but without producing results needed by the branch
instruction, or would have to be a no-op. RISC processors assume the complier or other
software will reorder instructions as necessary to fill this branch delay slot.

**5.** **As defined by Colwell et. al. in “Computers, Complexity, and Controversy”, RISC**

**computers have six characteristics: single-cycle operation, load/store design, hardwired**
**control, relatively few instructions and addressing modes, fixed instruction format, and**
**more compile-time effort. Though this definition is very similar to the earlier one by**
**Patterson, Colwell et. al. argue that Patterson’s RISC processor also included another**
**important architectural feature that is orthogonal to the basic RISC definitions but that**
**can, by itself, increase the processor’s performance. What is this other feature, and**
**what is Colwell’s point? (15 points)**

This other feature is multiple overlapped register sets, which can greatly simplify the process
of passing parameters to functions. However, these overlapped register sets can be added to
any processor that uses registers, whether it be RISC or CISC. Colwell argued that the use of
these overlapped register sets was orthogonal to the RISC vs CISC issue, and a fair RISC /
CISC comparison of must remove their effect.

**6.** **What is the maximum number of x86 instructions that the Intel P6 can decode in each**

**instruction cycle, and under what conditions will it do so? What can prevent it from**
**reaching that maximum? (15 points)**

There are three instruction decoders, so it can decode at most three instructions. However,
the second and third decoder can decode only simple (register-to-register) instructions.
Further, instructions are decoded in program order, so if the first decoder is busy and the next
instructions not a simple instruction, decoding must stall until the first decoder becomes free
and can process the non-simple instruction.


-----

Name: ____________________________

**7.** **What is the maximum number of ups that the Intel P6 can dispatch and process in each**

**instruction cycle, and under what conditions will it do so? What can prevent it from**
**reaching that maximum? (15 points)**

The superscalar core executes uops out of order, and can process up to five uops per cycle.
However, it is limited to one store data uop, one store address uop, one load address uop, one
(limited) integer ALU uops, and one more uop which can be either an integer or floating
point uop. Integer multiply and divide takes longer than one cycle, which can further limit
the engine.

Performance of the superscalar core is also limited by the reservation station, which holds at
most 20 uops to execute. Those uops do not leave the reservation station until their source
operations are available,

**8.** **Digital Equipment Corporation’s Alpha 21164 did not support out-of-order execution,**

**but it tried to overcome that deficiency. How did it do so? (10 points)**

It did not support full out-of-order execution, but it did support limited out-of-order
execution by allowing instructions to execute while cache misses are being serviced. This is
handled by the “merge logic” and dispatch unit, which allow instruction execution to
proceed, but prevent instructions from being dispatched until all their operands are available.
The merge logic also tried to merge loads in its Miss Address File to reduce the number of
accesses to the L2 cache.

The Alpha 21164 also made extensive use of caching, and even had a L2 cache on the chip.

**9.** **Non-hierarchical branch prediction methods can be classified into static prediction,**

**dynamic prediction using associative memory, and dynamic prediction using random**
**access memory. Briefly describe each of these three sets of methods. (15 points)**

Static prediction: make a prediction without considering branch history, such as predicting
that all branches will be taken, or all branches with certain operation codes will be taken, or
all backward branches will be taken.

Dynamic prediction using associative memory: make a prediction using branch history table,
where instructions and their previous outcome are stored in an associative memory.

Dynamic prediction with RAM: make a prediction using a hashed branch history table,
where instructions and their previous outcome are stored in RAM based on the hashed
address.


-----

