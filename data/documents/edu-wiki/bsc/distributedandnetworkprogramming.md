






BSc: Distributed And Network Programming
========================================



(Redirected from [BSc:DistributedAndNetworkProgramming](/index.php?title=BSc:DistributedAndNetworkProgramming&redirect=no "BSc:DistributedAndNetworkProgramming"))


Contents
--------


* [1 Distributed and Network Programming](#Distributed_and_Network_Programming)
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



Distributed and Network Programming
===================================


* **Course name**: Distributed and Network Programming
* **Code discipline**: XYZ
* **Subject area**: xxx


Short Description
-----------------


This course covers the following concepts: Network programming concepts: Layered architecture, TCP and UDP sockets, multithreaded servers; Distributed systems concepts: system architecture, inter-process communication, remote procedure calls, peer-to-peer systems, coordination, replication, and fault tolerance..



Prerequisites
-------------


### Prerequisite subjects


* **Networks**: 1) Understanding Application, Transport, and Network layers, 2) Basic socket programming experience
* **Operating systems**


### Prerequisite topics


Course Topics
-------------




Course Sections and Topics
| Section | Topics within the section
 |
| --- | --- |
| Introduction to subject, computer networks basics, transport layer protocols, and socket programming | 1. General introduction to the course
2. Computer networks basic
3. Socket programming
4. UDP socket programming
5. TCP socket programming
 |
| Multithreaded socket programming, RPCs, and distributed system architecture | 1. Multithreading and multithreaded socket programming
2. Remote procedure calls (RPCs)
3. Distributed system architectures
 |
| Coordination, consistency, and replication in distributed systems | 1. Clock synchronization algorithms (NTP, Berkeley)
2. Logical clock (Lamport clocks)
3. Mutual exclusion algorithms: permission-based, token-based
4. Election algorithms: Bully, Ring
5. Consistency models
6. Replica management
7. Consistency protocols
 |
| Fault tolerance and security in distributed systems | 1. Intro to fault tolerance: Failure models, Failure masking by redundancy
2. Process resilience: process groups, process replication, consensus in faulty systems, failure detection
3. Reliable group communication: atomic multicast,
4. Distributed commit
5. Recovery: checkpointing
6. Intro to security: threats, design issues, cryptography
7. Secure channels: authentication, message integrity and confidentiality, secure group communication
8. Access control: general issues, firewalls, secure mobile code, denial of service
9. Secure naming
10. Security management: Key management, secure group management, authorization management
 |


Intended Learning Outcomes (ILOs)
---------------------------------


### What is the main purpose of this course?


Distributed and networked systems have become an integral part of our life, we use various applications such as chatting, online transactions, or cloud storage apps. All these popular applications are supported by an infrastructure (of servers) that is organized based on some concepts of distributed systems. The purpose of this course is to provide the students with the necessary concepts, models, and real-world problem-solving techniques of network programming and distributed systems.



### ILOs defined at three levels


#### Level 1: What concepts should a student know/remember/explain?


By the end of the course, the students should be able to ...



* Concepts of network programming
* Different distributed system architectures
* Various synchronization and coordination techniques
* Different consistency models and replication methods
* Approaches to achieve fault tolerance and security in distributed systems


#### Level 2: What basic practical skills should a student be able to perform?


By the end of the course, the students should be able to ...



* Difference between different transport protocols, when and why one is preferred over another
* Difference between different distributed system architectures (centralized, decentralized, and hybrid)
* How a mutual exclusion is achieved between concurrent servers (centralized, distributed, token-ring, and decentralized)
* How a new leader is elected in peer-to-peer systems (bully, ring)
* How to achieve a consistent replicas across distributed systems (consistency models and protocols, content replication and placement)
* Some methods to achieve the fault tolerance in distributed systems


#### Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?


By the end of the course, the students should be able to ...



* Building a custom application protocols on top of the existing transport protocols
* Writing multithreaded server and client apps with sockets
* Using RPC for inter-process communication: command execution, file transfer
* Building peer-to-peer systems with distributed protocol such as Chord
* Building fault-tolerant systems with failure detection and leader election


Grading
-------


### Course grading range





| Grade | Range | Description of performance
 |
| --- | --- | --- |
| A. Excellent | 90-100 | -
 |
| B. Good | 75-89 | -
 |
| C. Satisfactory | 60-74 | -
 |
| D. Poor | 0-59 | -
 |


### Course activities and grading breakdown





| Activity Type | Percentage of the overall course grade
 |
| --- | --- |
| Laboratory assignments | 55%
 |
| Final exam | 35%
 |
| Attendance | 10%
 |


### Recommendations for students on how to succeed in the course


Resources, literature and reference materials
---------------------------------------------


### Open access resources


* Textbook: Maarten Van Steen, and Andrew S. Tanenbaum. Distributed systems (3rd Edition) Leiden, The Netherlands: Maarten van Steen, 2017. Available online: <https://www.distributed-systems.net/>
* Reference: George F. Coulouris, Jean Dollimore, and Tim Kindberg. Distributed systems: concepts and design (5th Edition) Addision Wesley, 2012. Available online: <https://www.cdk5.net/wp/>
* Reference: Sukumar Ghosh. Distributed systems: an algorithmic approach (2nd Edition) Chapman&Hall /CRC, Author’s own course material, Spring 2015. Available online: <http://homepage.divms.uiowa.edu/~ghosh/16615.html>


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
| Question | What are the distributed systems? | 1
 |
| Question | Give an example of distributed systems. | 1
 |
| Question | What are the advantages of layered architecture? | 1
 |
| Question | What are the roles of transport protocols? | 1
 |
| Question | How the TCP and UDP differ from each other? When one is preferred over the other? | 1
 |
| Question | What is socket programming? | 1
 |
| Question | How socket programming is different for UDP and TCP? | 1
 |
| Question | Write a simple UDP/TCP client-server echo program | 0
 |
| Question | Write a simple chatting program using UDP/TCP sockets | 0
 |
| Question | Given the simple echo server program, apply socket timeouts and catch timeout exceptions | 0
 |
| Question | Write a UDP-based reliable file transfer protocol | 0
 |
| Question | Write a program that parallelly executes the CPU-bound tasks using multiple processes | 0
 |


#### Section 2





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | How the threads differ from processes? | 1
 |
| Question | What are the I/O and CPU-bound tasks? | 1
 |
| Question | For what kind of tasks, using threads is preferred than using processes? | 1
 |
| Question | What is a remote procedure call? | 1
 |
| Question | What are some well-known distributed system architectures? | 1
 |
| Question | Discuss the structured and unstructured decentralized architectures. | 1
 |
| Question | You have a list of large numbers, and you need to find if they are prime or not. Would you use multithreading, multiprocessing, or sequential programming in order to complete the task asap? Prove it in practice. | 0
 |
| Question | You need to send multiple requests to a server and receive responses. Assume there is a few msecs of delay before you receive the response from the server. Would you use multithreading, multiprocessing, or sequential programming in order to complete the task asap? Prove it in practice. (Order of the requests/responses doesn't matter) | 0
 |
| Question | Discuss two ways of creating the threads using threading module in Python: 1) passing the worker function as a target, 2) subclassing the Thread class | 0
 |
| Question | Given the function implemented locally, make it available to be called through RPC from remote process? Use xmlRPC. | 0
 |


#### Section 3





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | How NTP protocol works? | 1
 |
| Question | How Berkeley protocol works? | 1
 |
| Question | Discuss the mutual exclusion algorithms. | 1
 |
| Question | Discuss the permanent and server-initiated replicas and their difference | 1
 |
| Question | Explain the Primary-backup protocol. | 1
 |
| Question | Given three machines with drifting clocks, adjust their clocks using Berkeley algorithm. | 0
 |
| Question | Explain how Bully algorithm for election works | 0
 |
| Question | Explain how Ring algorithm for election works | 0
 |
| Question | Explain the centralized (permission-based) method of mutual exclusion | 0
 |


#### Section 4





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Discuss the failure models | 1
 |
| Question | Discuss different failure masking techniques by redundancy | 1
 |
| Question | What is k-fault tolerant group? | 1
 |
| Question | What is general model of failure detection? | 1
 |
| Question | Explain basic reliable multicasting | 1
 |
| Question | Explain what is authentication | 1
 |
| Question | Explain what are message confidentiality and integrity | 1
 |
| Question | Same as above | 0
 |


### Final assessment


**Section 1**



1. Describe an advantage of layered architecture?
2. Describe the differences between TCP and UDP protocols?
3. Provide examples when using UDP can be more reasonable than TCP?
4. Describe how UDP and TCP socket programming differ from each other?


**Section 2**



1. Discuss the differences between the threads and processes.
2. What is the Race condition?
3. Discuss the ways to protect the shared data from the race condition
4. You're given the worker function that just sleeps for a second and quits, implement the same behavior in a subclass of the Thread.
5. Discuss the RPC and its advantages over using the low-level socket programming?
6. Discuss the decentralized architecture: structured and unstructured p2p systems.


**Section 3**



1. Discuss NTP and Berkeley protocols for synchronization and explain their key difference
2. Discuss permission-based and token-based solution for mutual exclusion.
3. Discuss content replication: permanent, server-initiated, and client-initiated replicas.
4. Explain the Primary-backup protocol, its advantages and disadvantages.


**Section 4**



1. Same as above


### The retake exam


**Section 1**


**Section 2**


**Section 3**


**Section 4**











