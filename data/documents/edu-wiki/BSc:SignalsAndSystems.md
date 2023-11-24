






BSc: Signals And Systems
========================



(Redirected from [BSc:SignalsAndSystems](/index.php?title=BSc:SignalsAndSystems&redirect=no "BSc:SignalsAndSystems"))


Contents
--------


* [1 Signals and Systems](#Signals_and_Systems)
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



Signals and Systems
===================


* **Course name**: Signals and Systems
* **Code discipline**: XYZ
* **Subject area**: Electric Engineering


Short Description
-----------------


This course covers the following concepts: discrete(-time) signals, their impulse and frequency domains; classification of (discrete) systems (bound-input-bound-output, linear and shift-invariant); filters and filtering, finite and infinite impulse response filters; discrete(-time) Fourier transform and fast Fourier transform.



Prerequisites
-------------


### Prerequisite subjects


* [CSE202 — Analytical Geometry and Linear Algebra](https://eduwiki.innopolis.university/index.php/BSc:AnalyticGeometryAndLinearAlgebraI): complex numbers, vecrors and matrix operations, basis and basis decomposition, concept of eigen values and vectors.
* [CSE201 — Mathematical Analysis I](https://eduwiki.innopolis.university/index.php/BSc:MathematicalAnalysisI): limits and absolutly summabale series, exponent function, besic integration.
* [CSE113 — Philosophy I - (Discrete Math and Logic)](https://eduwiki.innopolis.university/index.php/BSc:Logic_and_Discrete_Mathematics): Algorithm time and space complexity.


### Prerequisite topics


Course Topics
-------------




Course Sections and Topics
| Section | Topics within the section
 |
| --- | --- |
| Complex numbers and functions, vector and Hilbert Spaces, computational aspects | 1. Complex numbers and their matrix representation
2. Vector spaces with dot-product
3. Metrics and convergence, Hilbert spaces
4. Algorithms and their computational (space and time) complexity
 |
| Discrete Fourier Transform and Fast Fourier Transforms (DFT and FFT) | 1. Circular convolution, eigen vectors and values of the circular convolution
2. Discrete Fourier Transform (DFT) and its inverse
3. Circutate filters and filtering
4. Fast Fourier Transform (FFT),its inverse, and computational aspects of DFT and fast FFT
 |
| Discrete-time signals and systems: properties and classification | 1. Kotelnikov-Whittaker–Nyquist–Shannon sampling Theorem.
2. Discrete signals as sequences, spaces of absolutely summable and bounded sequences.
3. Auto- and cross-correlation; memoryless, causal and shift-invariant systems
4. Linear systems, their matrix representation and properties
5. Convolution and its relations to linear shift-invariant systems
 |
| Convolution, Discrete-time Fourier Transformation, filtering | 1. Math preliminaries on complex exponent and Euler formulas.
2. Introduction of the discrete-time Fourier transform via convolution eigen values and vectors.
3. Discrete-time Fourier transform as the frequency response of a linear shift-invariant system.
4. Inverse discrete-time Fourier transform.
5. DTFT properties (including convolution theorem).
6. Elements of ideal Filter Design.
 |


Intended Learning Outcomes (ILOs)
---------------------------------


### What is the main purpose of this course?


The goal of the course is to present mathematical foundations of digital signal processing altogether with practical experience to design finite and infinite impulse response filters. The course is aimed to provide basic mathematical knowledge and practical skills needed for further studies of applied signal processing and digital signal processing from engineering as well as from mathematical perspective.



### ILOs defined at three levels


#### Level 1: What concepts should a student know/remember/explain?


By the end of the course, the students should be able to ...



* discrete (time) signals and systems, their classification
* linear shift-invariant systems, filters and filtering
* Discrete Fourier Transformation (DFT)
* Fast discrete Fourier Transformation (FFT)
* Discrete-Time Fourier Transformation (DTFT),


#### Level 2: What basic practical skills should a student be able to perform?


By the end of the course, the students should be able to ...



* relations between analog and digital signals (sampling)
* relations between convolution, correlation, and filtering of discrete signals
* role of impulse and frequency domains of discrete signals
* differences between infinite and finite discrete signals
* role of discrete time Fourier transform and its inverse
* role of discrete Fourier transform (DFT) and fast DFT (FFT)


#### Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?


By the end of the course, the students should be able to ...



* basic numerical tools from mathematical package SciLab/Octave
* classify discrete signals and systems
* design and implement infinite and finite impulse response filters
* implement and use discrete time Fourier transform,
* implement and use discrete Fourier transform and fast DFT.


Grading
-------


### Course grading range





| Grade | Range | Description of performance
 |
| --- | --- | --- |
| A. Excellent | 104-130 | -
 |
| B. Good | 84-103 | -
 |
| C. Satisfactory | 65-83 | -
 |
| D. Poor | 0-64 | -
 |


### Course activities and grading breakdown





| Activity Type | Percentage of the overall course grade
 |
| --- | --- |
| Labs/seminar classes | 20
 |
| Interim performance assessment | 90
 |
| Exams | 20
 |


### Recommendations for students on how to succeed in the course


Resources, literature and reference materials
---------------------------------------------


### Open access resources


* Martin Vetterli, Jelena Kovacevic, and Vivek K Goyal.Foundations of Signal Processing.Cambridge University Press, 2014. ISBN 10703860X
* Oppenheim, Alan V., and A. S. Willsky. Signals and Systems (2nd ed.) Prentice Hall, 1996. ISBN 0-13-814757-4.
* Richard G. Lyons.UnderstandingDigitalSignalProcessing. Prentice Hall, 2010. ISBN 978-0137027415


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
| Homework and group projects | 1 | 1 | 1 | 1
 |
| Testing (written or computer based) | 1 | 0 | 0 | 0
 |
| Reports | 1 | 1 | 1 | 1
 |
| Discussions | 1 | 1 | 1 | 1
 |
| Development of individual parts of software product code | 0 | 1 | 1 | 1
 |
| Midterm evaluation | 0 | 1 | 1 | 1
 |


Formative Assessment and Course Activities
------------------------------------------


### Ongoing performance assessment


#### Section 1





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Prove that each complex number has a square root. | 1
 |
| Question | Prove that the neutral element is unique in a vector space. | 1
 |
| Question | Prove that pixel (Manhattan) and Euclidean norms are equivalent in finite-dimensional real (complex) spaces. | 1
 |
| Question | Is the set of integers complete in the discrete metrics? | 1
 |
| Question | What is space and time complexity of dot product in a complex n-dimensional vector space? | 1
 |
| Question | Prove that each complex number but zero has the inverse. | 0
 |
| Question | Prove that each vector of a vector space has unique opposite element. | 0
 |
| Question | Prove that pixel and the universal norms are equivalent in finite-dimensional real(complex) spaces. | 0
 |
| Question | Is the set of rational numbers complete in the discrete metrics? | 0
 |
| Question | What is space and time complexity of finite matrices multiplication (according to the definition)? | 0
 |


#### Section 2





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Compute circular convolution of given two short integer signals. | 1
 |
| Question | Explain Discrete Fourier Transform as orthogonal vector decomposition. | 1
 |
| Question | Compute DFT and FFT for given short integer signal. | 1
 |
| Question | Prove circular impulse shift property. | 0
 |
| Question | Study commutativity, linearity and associativity of the circular convolution. | 0
 |
| Question | Give matrix representation for the circular convolution for several small dimensions. | 0
 |
| Question | Recall 2-redex fast Fourier transform and draw its matrices for several small dimensions. | 0
 |


#### Section 3





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Give examples of (infinite) absolutely summable/non-summable, bounded/unbounded,etc., signals. | 1
 |
| Question | Is autocorrelation linear system? Is it shift-invariant? | 1
 |
| Question | Prove that a linear system is memoryless iff its matrix is diagonal. | 1
 |
| Question | Prove that a linear system is causal iff its matrix is low-triangle. | 0
 |
| Question | A linear system is shift-invariant iff its matrix consists (exclusively) of diagonals of some constant (individual for each diagonal). | 0
 |
| Question | Prove that product of finite power series is convolution of the finite signals consisting of the coefficients of these series. | 0
 |


#### Section 4





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Do there exists a periodic function with non-commensurable periods? | 1
 |
| Question | Prove that product of two exponents is equal to the exponent with sum of powers. | 1
 |
| Question | Prove conjugate property for DTFT. | 1
 |
| Question | Prove DTFT-correspondence for impulse shift. | 0
 |
| Question | Prove DTFT-correspondence for frequency shift. | 0
 |
| Question | Design a low-band filter with a given spectrum consisting of a single box. | 0
 |


### Final assessment


**Section 1**



1. Build if possible (or prove that it isn’t) ...


**Section 2**



1. Assume that a finite signal ...


**Section 3**



1. Compute cross-correlation of two box signals.
2. Study properties (linearity, causality, stability, etc.) of a weighted accumulator


**Section 4**



1. Show that exponent with imaginary power is a periodic function, find the smallest period.
2. Prove sampling and scaling properties for the Dirac Delta function.


### The retake exam


**Section 1**


**Section 2**


**Section 3**


**Section 4**











