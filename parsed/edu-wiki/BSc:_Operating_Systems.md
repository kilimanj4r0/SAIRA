






BSc: Operating Systems
======================






Contents
--------


* [1 Operating Systems](#Operating_Systems)
	+ [1.1 Short Description](#Short_Description)
	+ [1.2 Prerequisites](#Prerequisites)
		- [1.2.1 Prerequisite subjects](#Prerequisite_subjects)
		- [1.2.2 Prerequisite topics](#Prerequisite_topics)
	+ [1.3 Course Topics](#Course_Topics)
	+ [1.4 Intended Learning Outcomes (ILOs)](#Intended_Learning_Outcomes_.28ILOs.29)
		- [1.4.1 What is the main purpose of this course?](#What_is_the_main_purpose_of_this_course.3F)
		- [1.4.2 ILOs defined at three levels](#ILOs_defined_at_three_levels)
			* [1.4.2.1 Level 1: What concepts should a student know/remember/explain?](#Level_1:_What_concepts_should_a_student_know.2Fremember.2Fexplain.3F)
			* [1.4.2.2 Level 2: What basic practical skills should a student be able to perform?](#Level_2:_What_basic_practical_skills_should_a_student_be_able_to_perform.3F)
			* [1.4.2.3 Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?](#Level_3:_What_complex_comprehensive_skills_should_a_student_be_able_to_apply_in_real-life_scenarios.3F)
	+ [1.5 Grading](#Grading)
		- [1.5.1 Course grading range](#Course_grading_range)
		- [1.5.2 Course activities and grading breakdown](#Course_activities_and_grading_breakdown)
		- [1.5.3 Recommendations for students on how to succeed in the course](#Recommendations_for_students_on_how_to_succeed_in_the_course)
	+ [1.6 Resources, literature and reference materials](#Resources.2C_literature_and_reference_materials)
		- [1.6.1 Open access resources](#Open_access_resources)
		- [1.6.2 Closed access resources](#Closed_access_resources)
		- [1.6.3 Software and tools used within the course](#Software_and_tools_used_within_the_course)
* [2 Teaching Methodology: Methods, techniques, & activities](#Teaching_Methodology:_Methods.2C_techniques.2C_.26_activities)
	+ [2.1 Activities and Teaching Methods](#Activities_and_Teaching_Methods)
	+ [2.2 Formative Assessment and Course Activities](#Formative_Assessment_and_Course_Activities)
		- [2.2.1 Ongoing performance assessment](#Ongoing_performance_assessment)
			* [2.2.1.1 Section 1](#Section_1)
			* [2.2.1.2 Section 2](#Section_2)
			* [2.2.1.3 Section 3](#Section_3)
			* [2.2.1.4 Section 4](#Section_4)
		- [2.2.2 Final assessment](#Final_assessment)
		- [2.2.3 The retake exam](#The_retake_exam)



Operating Systems
=================


* **Course name**: Operating Systems
* **Code discipline**: R-01
* **Subject area**:


Short Description
-----------------


This course covers the following concepts: Structure of an operating system; Specific mechanisms, policies, and algorithms used to implement the different parts of an operating system.



Prerequisites
-------------


### Prerequisite subjects


### Prerequisite topics


Course Topics
-------------




Course Sections and Topics
| Section | Topics within the section
 |
| --- | --- |
| Revision of programming fundamentals for OS | 1. Revision of the structure of a C program
2. Overall organization of the computation in C
3. Preprocessing
4. Simulating function calls in preprocessing
5. Analogies between macros and call by name
6. Meaning of a variable in C
7. Scope and extent of a variable
8. Managing data structures with variable length
9. Allocation and deallocation of memory
10. Pointers and pointer arithmentics
11. Pointers to functions
12. Usage of pointers to function to simulate virtual functions
13. Examples of usage of pointers to function in real life scenarios
14. Pointers to functions to perform map and reduce
 |
| Processes and Threads | 1. Process models
2. Process creation and termination
3. Process hierarchies
4. Process states
5. Implementation of processes
6. Threads
7. Interprocess communication
8. Races
9. Critical regions, busy waiting, sleep and wakeup
10. Semaphores
11. Monitors
12. Principles of scheduling
13. Categories of scheduling algorithms
14. Most common approaches for scheduling in interactive systems
 |
| Memory management | 1. Address space
2. Memory abstraction
3. Based and limit registers
4. Swapping
5. Virtual memory
6. Paging
7. Implementation of paging
8. Page replacement algorithms
9. Page faults
10. Segmentation
11. Segmentation with paging
 |
| File system, I/O, and management of resources | 1. File system
2. Files and files types, attributes, and operations
3. Paths
4. File system layout
5. Shared files
6. File system backups
7. FIle system performances
8. General structure of I/O
9. Block devices and character devices
10. Device drivers
11. Memory mapped I/O and Direct Memory Access
12. Interrupts
13. Programmed I/O
14. Deadlocks
15. Conditions for deadlocks
16. Strategies to deal with dealocks
 |


Intended Learning Outcomes (ILOs)
---------------------------------


### What is the main purpose of this course?


Operating systems are the core part of a computing device and computing devices are an integral part of our life, not only as programmers, but also just as human being – it is enough to think at smart homes infrastructures, now available at accessible prices to everyone, at car devices, like smart navigator and cruise control systems, at other infrastructures. Therefore, a fundamental understanding of the structure of an operating systems has a paramount role in the curriculum of a student in computer science and engineering. The purpose of this course is to provide such understanding. This is a core course, so it is not among its goals to explore the details of the various proposal for operating systems that are now emerging: this is the subject of more advanced endeavours.



### ILOs defined at three levels


#### Level 1: What concepts should a student know/remember/explain?


By the end of the course, the students should be able to ...



* fundamental components of an Operating Systems,
* organization of primary memory and the associated concept of virtual memory, with techniques based on paging and segmenting,
* structure of secondary memory (file systems),
* management of the processor(s) and of the connected scheduling algorithms,
* allocation of resources and the associated problems (deadlocks),
* approaches to handle I/O.


#### Level 2: What basic practical skills should a student be able to perform?


By the end of the course, the students should be able to ...



* strategies and algorithms for allocating processor(s) time to processes,
* strategies and algorithms for allocating primary memory to processes,
* the fundamental states of a process and how they are reached,
* concept and implementation of the address space of a process, both in the single threaded and in the multi threaded cases.
* techniques to organize files and directories in secondary memory,
* algorithms for a safe concurrent access to resources, preventing or avoiding deadlocks,
* methods for attaching different kind of devices to a computer, also considering different kind of buses.


#### Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?


By the end of the course, the students should be able to ...



* strategies for programming at the Operating System level,
* fundamental system calls for process creation, termination,
* fundamental system calls to allocate, change, and deallocate primary memory to processes,
* libraries to handle buffered and unbuffered interconnections with the computer, including files and I/O devices,
* the identification of the most suitable algorithms for process, memory, and I/O management depending on the context in which their target operating system is working.


Grading
-------


### Course grading range





| Grade | Range | Description of performance
 |
| --- | --- | --- |
| A. Excellent | 96-100 | -
 |
| B. Good | 66-95 | -
 |
| C. Satisfactory | 56-65 | -
 |
| D. Poor | 0-55 | -
 |


### Course activities and grading breakdown





| Activity Type | Percentage of the overall course grade
 |
| --- | --- |
| Labs/seminar classes (weekly evaluations) | 30
 |
| Interim performance assessment (class participation) | 5
 |
| Exams | 65
 |
| Labs/seminar classes (weekly evaluations) | 20
 |
| Interim performance assessment (class participation) | 5
 |
| Solutions to questions of Bach directly in the text | 50
 |
| Exams | 25
 |


### Recommendations for students on how to succeed in the course


Resources, literature and reference materials
---------------------------------------------


### Open access resources


* Textbook: Andrew S. Tanenbaum and Herbert Bos. Modern Operating Systems (5th Edition), Pearson
* Reference: Andrew S. Tanenbaum and David J. Wetherall. Computer Networks (5th Edition), Pearson
* Reference: Brian W. Kernighan, Dennis M. Ritchie. The C Programming Language - 2nd Edition, Prentice Hall
* Reference: Maurice J.Bach. The design of the Unix Operating System, PRENTICE-HALL, INC., Englewood Cliffs, New Jersey 07632


### Closed access resources


### Software and tools used within the course


Teaching Methodology: Methods, techniques, & activities
=======================================================


Activities and Teaching Methods
-------------------------------




Activities within each section
| Learning Activities | Section 1 | Section 2 | Section 3 | Section 4
 |
| --- | --- | --- | --- | --- |
| Development of individual parts of software product code | 1 | 1 | 1 | 1
 |
| Homework and group projects | 1 | 1 | 1 | 1
 |
| Testing (written or computer based) | 1 | 1 | 1 | 1
 |
| Oral polls | 1 | 1 | 1 | 1
 |
| Discussions | 1 | 1 | 1 | 1
 |


Formative Assessment and Course Activities
------------------------------------------


### Ongoing performance assessment


#### Section 1





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Explain the difference between an include file and a library. | 1
 |
| Question | Is a parameter of a macro a “real” parameter? | 1
 |
| Question | Discuss the importance of the conditional compilation. | 1
 |
| Question | What happens when a function returning a pointer returns the address of a local variable? | 1
 |
| Question | Detail the meaning of the keyword static and external for supporting information hiding. | 1
 |
| Question | Describe how the use of virtual functions can make the code more flexible. | 1
 |
| Question | Given a source .c file including a .h header file, show the results of preprossing in terms of the generated c file. | 0
 |
| Question | Write a macro and a function in C for the same purpose and discuss pros and cons of both approaches. | 0
 |
| Question | Show how you can write a generic swap function as a macro. | 0
 |
| Question | Write the code allocating dynamic memory for a 2 dimensional array and initializing it. | 0
 |
| Question | Provide an example of how with pointers it is possible in the called function to alter values of variable located in the calling function. | 0
 |
| Question | Using function pointers, write a sorting function having the sorting rule as a parameter of such function. | 0
 |


#### Section 2





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Outline the typical life of a process from creation to termination | 1
 |
| Question | Present the different possible models of waiting | 1
 |
| Question | Define the concept of a semaphore and how it can be implemented | 1
 |
| Question | Explain the concept of a monitor from a programming standpoint and how it relates to modern programming paradigms. | 1
 |
| Question | Discuss advantages and disadvantages of the different scheduling algorithms | 1
 |
| Question | Write a shell script that produces a file of sequential numbers by reading the last number in the file, adding 1 to it, and then appending it to the file. Run one instance of the script in the background and one in the foreground, each accessing the same file. Answer the following questions: (a) How long does it take before a race condition manifests itself? (b) What is the critical region? (c) How you can modify the script to prevent the race | 0
 |
| Question | Write a producer-consumer problem that uses threads and shares a common buffer. However, do not use semaphores or any other synchronization primitives to guard the shared data structures. Just let each thread access them when it wants to. Use sleep and wakeup to handle the full and empty conditions. See how long it takes for a fatal race condition to occur. For example, you might have the producer print a number once in a while. Do not print more than one number every minute because the I/O could affect the race conditions. | 0
 |
| Question | Write a program that creates a pipe. Have two strings – one should contain some text, the other one should be empty. Transfer a text from the first string to another one using the pipe you created. Show the result. | 0
 |
| Question | Write a C program that forks a child process, waits for 10 seconds and then sends a SIGTERM signal to the child. The child process should run an infinite loop and print “I’m alive” every second | 0
 |
| Question | Write the solution for the produced-consumer problem using monitors. | 0
 |


#### Section 3





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | What are the base and limit registers and what are the problems related to their usage? | 1
 |
| Question | Can you have swapping in absence of paging? And paging in absence of swapping? | 1
 |
| Question | What mechanisms and algorithms are available to handle effectively paging? | 1
 |
| Question | Details advantages and disadvantages of the different page replacement algorithms. | 1
 |
| Question | Describe the difference between paging and segmenting. | 1
 |
| Question | Is it possible to combine segmenting and paging? If so, how? | 1
 |
| Question | Run ‘free -t -h‘ in a Linux shell or ‘vmstat‘ in a macOS one. Discuss the output. | 0
 |
| Question | Write a C program that runs for 10 seconds. Every second it should: (a) allocate 10 MB of memory – fill it with zeros, (b) sleep for 1 second. Then, compile and run the program in the background (./ex2 &) and run ‘vmstat 1’ at the same time. Observe what happens to the memory. Pay attention to si and so fields. Hint: use memset(ptr, value, size) to fill the allocated memory. | 0
 |
| Question | Write a program that simulates a paging system using the ageing algorithm. The number of page frames is a parameter. The sequence of page references should be read from a file. For a given input file, your program should print Hit/Miss ratio. | 0
 |
| Question | Try to construct a sequence of references that will result in increased or decreased Hit/Miss ratio. | 0
 |
| Question | From the textbook: A machine has 16-bit virtual addresses. Pages are 8 KB. How many entries are needed for a single-level linear page table? Explain your computations. | 0
 |


#### Section 4





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | What is the overall structure of a file system | 1
 |
| Question | How are files and directories organized on a disk and what are the roles of i-nodes, when they are used | 1
 |
| Question | What are the key differences between block and character devices. | 1
 |
| Question | How does DMA speeds up the computations? | 1
 |
| Question | List the major classes of strategies to handle deadlock. | 1
 |
| Question | Create tmp directory with two empty files (file1, file2). Then, create one hard link named link1 to file1. Write a program that scans tmp directory, locates all i-nodes with a hard link count of two or more and for each such file it should display together all file names that point to the file. | 0
 |
| Question | Implement a simulated file system that will be fully contained in a single regular file stored on the disk. This disk file will contain directories, i-nodes, free- block information, file data blocks, etc. Choose appropriate algorithms for maintaining free-block information and for allocating data blocks (contiguous, indexed, linked). Your program will accept system commands from the user to create/delete directories, create/delete/open files, read/write from/to a selected file, and to list directory contents. | 0
 |
| Question | Create a file ex1.txt with a random string in it. Write a C program (ex1.c) that changes the string in ex1.txt to “This is a nice day” by using mmap(). Hints: (a) open the file in O\_RDWR mode, (b) use stat() or fstat() to get the size of the file. | 0
 |
| Question | Write a C program (ex2.c) using line buffer. Write your code according to the instructions: (a) each of the 5 characters of “Hello” string should be put in separate printf(), (b) add a 1 sec sleep after every printf(). The output should be a 5 sec wait and then “Hello” printed instantaneously. | 0
 |
| Question | The tee command reads its standard input until end-of- file, writing a copy of the input to standard output and to the files named in its command-line arguments. Implement tee using I/O system calls. By default, tee overwrites any existing file with the given name. Implement the -a command-line option (tee -a file), which causes tee to append text to the end of a file if it already exists. | 0
 |
| Question | Write a C program for deadlock detection algorithm reading the resources available form a file (input.txt). For testing purposes consider 5 processes and 3 type of resources. However, your program must be able to process as many processes and resource types, as needed (check next slide for input file structure description). The output of your program should either say that no deadlock is detected or print out the numbers of processes that are deadlocked. | 0
 |


### Final assessment


**Section 1**



1. Discuss the difference in the compiled code when using function and when using macros instead.
2. Provide examples of functions that cannot be transformed into macros, also discussing the motivation for such impossibility.
3. Describe the rules for scope and extent for local variables, static variables (in all cases), and pointers, supplying also code examples of them.
4. Detail the structure of the address space of a process when using a three dimensional array allocated as a local variable of a function and when such array is allocated dynamically, also describe the types of the variables in use and how the compiler checks them.
5. Outline the assembly code for a function calling another function passed as a parameter of it.


**Section 2**



1. From the textbook: Multiple jobs can run in parallel and finish faster than if they had run sequentially. Suppose that two jobs, each needing 20 minutes of CPU time, start simultaneously. How long will the last one take to complete if they run sequentially? How long if they run in parallel? Assume 50% I/O wait.
2. From the textbook: The readers and writers problem can be formulated in several ways with regard to which category of processes can be started when. Carefully describe three different variations of the problem, each one favoring (or not favoring) some category of processes. For each variation, specify what happens when a reader or a writer becomes ready to access the database, and what happens when a process is finished?
3. From the textbook: Consider a system in which threads are implemented entirely in user space, with the run-time system getting a clock interrupt once a second. Suppose that a clock interrupt occurs while some thread is executing in the run-time system. What problem might occur? Can you suggest a way to solve it?
4. From the textbook: In this problem you are to compare reading a file using a single-threaded file server and a multithreaded server. It takes 12 msec to get a request for work, dispatch it, and do the rest of the necessary processing, assuming that the data needed are in the block cache. If a disk operation is needed, as is the case one-third of the time, an additional 75 msec is required, during which time the thread sleeps. How many requests/sec can the server handle if it is single threaded? If it is multithreaded?
5. From the textbook: There are five batch jobs: A through E, they arrive at a computer center at almost the same time. They have estimated running times of 10, 6, 2, 4, and 8 minutes. Their (externally determined) priorities are 3, 5, 2, 1, and 4, respectively, with 5 being the highest priority. Consider the following scheduling algorithms: (a) Round robin, (b) Priority scheduling, (c) First-come, first-served (run in order 10, 6, 2, 4, 8), (d) Shortest job first. For each mentioned scheduling algorithms, determine the mean process turnaround time. Ignore process switching overhead. For (a), assume that the system is multi-programmed, and that each job gets its fair share of the CPU. For (b) through (d), assume that only one job at a time runs, until it finishes. All jobs are completely CPU bound.


**Section 3**



1. From the textbook: A computer provides each process with 65,536 bytes of address space divided into pages of 4096 bytes each. A particular program has a text size of 32,768 bytes, a data size of 16,386 bytes, and a stack size of 15,870 bytes. Will this program fit in the machine’s address space? Suppose that instead of 4096 bytes, the page size were 512 bytes, would it then fit? Each page must contain either text, data, or stack, not a mixture of two or three of them.
2. From the textbook: You are given the following data about a virtual memory system: 1. The TLB can hold 1024 entries and can be accessed in 1 clock cycle (1 nsec). 2. A page table entry can be found in 100 clock cycles or 100 nsec. 3.The average page replacement time is 6 msec. If page references are handled by the TLB 99% of the time, and only 0.01% lead to a page fault, what is the effective address-translation time?
3. From the textbook: A small computer on a smart card has four page frames. At the first clock tick, the R bits are 0111 (page 0 is 0, the rest are 1). At subsequent clock ticks, the values are 1011, 1010, 1101, 0010, 1010, 1100, and 0001. If the aging algorithm is used with an 8-bit counter, give the values of the four counters after the last tick.
4. From the textbook: A computer with a 32-bit address uses a two-level page table. Virtual addresses are split into a 9-bit top-level page table field, an 11-bit second-level page table field, and an offset. How large are the pages and how many are there in the address space?
5. From the textbook: A computer has 32-bit virtual addresses and 4-KB pages. The program and data together fit in the lowest page (0–4095) The stack fits in the highest page. How many entries are needed in the page table if traditional (one-level) paging is used? How many page table entries are needed for two-level paging, with 10 bits in each part?


**Section 4**



1. From the textbook: Two computer science students, Carolyn and Elinor, are having a discussion about i-nodes. Carolyn maintains that memories have gotten so large and so cheap that when a file is opened, it is simpler and faster just to fetch a new copy of the i-node into the i-node table, rather than search the entire table to see if it is already there. Elinor disagrees. Who is right? Why?
2. From the textbook: A typical printed page of text contains 50 lines of 80 characters each. Imagine that a certain printer can print 6 pages per minute and that the time to write a character to the printer’s output register is so short it can be ignored. Does it make sense to run this printer using interrupt-driven I/O if each character printed requires an interrupt that takes 50 





μ




{\displaystyle {\textstyle \mu }}

![{\displaystyle {\textstyle \mu }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/585e07e65d8eabf45a5c4b271ffad09d5e17dcbc) sec all-in to service?
3. From the textbook: Consider a disk that has 10 data blocks starting from block 14 through 23. Let there be 2 files on the disk: f1 and f2. The directory structure lists that the first data blocks of f1 and f2 are respectively 22 and 16. The FAT table is as follows: (14,18), (15,17), (16,23), (17,21), (18,20), (19,15), (20,-1), (21,-1), (22,19), (23,14), where (x,y) indicates that the value stored in table entry x points to data block y. What are the data blocks allotted to f1 and f2?
4. From the textbook: Explain how hard links and soft links differ with respective to i-node allocations.
5. From the textbook: When a user program makes a system call to read or write a disk file, it provides an indication of which file it wants, a pointer to the data buffer, and the count. Control is then transferred to the operating system, which calls the appropriate driver. Suppose that the driver starts the disk and terminates until an interrupt occurs. In the case of reading from the disk, obviously the caller will have to be blocked (because there are no data for it). What about the case of writing to the disk? Need the caller be blocked awaiting completion of the disk transfer?
6. From the textbook: The banker’s algorithm is being run in a system with m resource classes and n processes. In the limit of large m and n, the number of operations that must be performed to check a state for safety is proportional to m








a






{\displaystyle {\textstyle ^{a}}}

![{\displaystyle {\textstyle ^{a}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/816bd6b322edfd90f9aa1b8bf720fd80fd85e1c5) n








b






{\displaystyle {\textstyle ^{b}}}

![{\displaystyle {\textstyle ^{b}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e1c103623f6d6dfd18ab85506e97c9c31229529e) . What are the values of a and b ?


### The retake exam


**Section 1**


**Section 2**


**Section 3**


**Section 4**











