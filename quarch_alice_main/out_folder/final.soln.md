Name: ____________________________

**CS 6/75101** **Final Exam** **Adv. Comp. Arch.**

**Friday 6 May 2011**

**This test is open-book, open-notes, meaning you may look at any notes that you have**
**brought with you, or you may use a laptop. You may NOT share your notes or laptop with**
**a friend.  You may NOT use your cell phone, or talk to a friend.  Since you have access to**
**the papers discussed in class, be careful to answer the question that was asked INSTEAD of**
**copying text from the paper that may or may not answer the question.**

**1.** **What is the primary market for each of these processors?**

**a. ARM Cortex-A9 (5 points)**

Consumer electronics, in particular mobile phones, but also electronic games, set-top
boxes, networking products, cameras, etc.

**b. TM3270 Media Processor (5 points)**

Standard definition video processing and audio processing for consumer electronics, sich
as set-top boxes.

**c. ClearsSpeed CSX700 (5 points)**

Data-intensive systems requiring high-performance computing, with applications in
finance, radar systems, bio-informatics, signal processing, and medical imaging.

**d. Cell Multiprocessor (5 points)**

Electronic games with network connectivity, such as the Sony PlayStation2.

**2.** **What type(s) of parallelism do each of these architectures support?**

**a. ARM Cortex-A9 (8 points)**

The single-core A9 just supports instruction-level parallelism though superscalar
execution, but the mult-core A9 MPCore allows 1-4 processor cores on a single chip,
which would operate in MIMD fashion. Additional SIMD parallelism can be added
through the NEON Media Processing Engine.

**b. TM3270 Media Processor (8 points)**

VLIW instruction-level parallelism (MIDD), though the architecture also supports some
SIMD-style instructions to compete with Intel MMX instructions.


-----

Name: ____________________________

**c. ClearsSpeed CSX700 (8 points)**

Two MTAP cores, each operating in SIMD fashion with 96 processing elements.
Additionally, the mono (scalar) controller provides hardware support for up to eight
threads.

**d. Simultaneous Multithreading (8 points)**

Simultaneous multithreading allows multiple threads to use the processor’s superscalar
execution units in the same cycle. Note that this is more than multithreading, which only
allows a one thread at a time to use the superscalar resources in each cycle.

**e. Cell Multiprocessor (8 points)**

Each cell processor supports SIMD parallelism, with the PPE executing the scalar portion
of the code, and the eight SPEs executing the parallel portion in SIMD fashion. Multiple
cell processors can be combined into various forms of multiprocessors.

**3.** **Earlier CISC architectures added complicated instructions to perform operations such**

**as evaluating polynomials, only to find those instructions were rarely used. The**
**TM3270 Media Processor adds some very specific and complicated instructions such as**
**two versions of a CABAC instruction. What are the advantages and disadvantages of**
**adding this instruction? (10 points)**

**Advantages:**

This instruction performs the CABAC operation more efficiently than other methods, and
that CABAC operation is a “significant part” of the computation in processing H.264/AVC
video, so adding that instruction should make video processing more efficient. Performance
measurements show the new instruction provides a speedup between 1.5-1.7.

**Disadvantages:**

If the next video processing standard after H.264 does not use the CABAC operation, but
requires some other operation instead, a new version of the media processor must be
designed to support that new operation — thus this processor is at least somewhat tied to
processing H.264 video.

**4.** **What is “horizontal waste” and how does simultaneous multithreading help overcome**

**that waste? (10 points)**

Horizontal waste refers to unused (wasted) issue slots in a single cycle of a superscalar
processor, meaning some execution units are being used, but others are left idle.

Simultaneous multithreading helps overcome this waste by filling those unused slots from
other threads, allowing multiple threads to be processed simultaneously within a single cycle.


-----

Name: ____________________________

**5.** **What does it mean to say the ClearsSpeed CSX700 processor “supports” 8 threads? (5**

**points)**

Hardware support is provided for switching between threads, for maintaining the context (PC
and general register contents) of each thread while it is not executing, and for restoring that
context when the thread starts executing again. Additionally, semaphores allow threads to
cooperatively manage shared resources.

**6.** **The Cell Multiprocessor was an ambitious project aimed at achieving 100 times the**

**PlayStation2 performance, and could easily have taken 10 years to develop. How did**
**they cut that development time to less than five years? (5 points)**

Instead of developing a completely new instruction set architecture, they used the existing
Power Architecture as the basis for the Cell processor’s instruction set architecture. Doing
that also allowed them to reuse existing software from the Power on the Cell, including its
operating system.

**7.** **What is the “memory wall” and how does the Cell Multiprocessor try to avoid its**

**problems? (5 points)**

The “memory wall” refers to the growing difference in speeds between CPUs and DRAM
memory, with processor speeds continuing to grow but DRAM access times not keeping
pace. As a result, the number of cycles required to access DRAM memory continues to rise.

The Cell tried to overcome this problem by providing the SPE’s fast access to shared
memory via DMA commands, by adding another level of memory hierarchy (the “local
store”), and by supporting next-generation Rambus XDR DRAM memory.

**8.** **What is the point the author of “Spending Moore’s Dividend” is trying to make in his**

**Windows95 print spooler example? (5 points)**

Even though processor power has increased over the years, the Windows print spooler does
not run appreciably faster than it did in 1995 due to increased code complexity: new security
and notification functionality, new color management and text/graphics improvements,
increased printer resolution and color depth, and the memory wall limiting color lookup
tables and graphical rendering.


-----

