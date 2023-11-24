






BSc: Robotic Systems
====================



(Redirected from [BSc:RoboticSystems](/index.php?title=BSc:RoboticSystems&redirect=no "BSc:RoboticSystems"))


Contents
--------


* [1 Robotic Systems](#Robotic_Systems)
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



Robotic Systems
===============


* **Course name**: Robotic Systems
* **Code discipline**:
* **Subject area**: Robotics; Robotic components; Robotic control.


Short Description
-----------------


This course covers the following concepts: Robot hardware; Feedback control in application to robotic systems; Trajectory tracking and advanced control algorithms.



Prerequisites
-------------


### Prerequisite subjects


* CSE201 — Mathematical Analysis I and CSE203 — Mathematical Analysis II: ordinary and partial derivatives, definite and indefinite integrals.
* CSE202 — Analytical Geometry and Linear Algebra I and ACSE204 — Analytic Geometry And Linear Algebra II: matrix operations, eigenvalues and eigenvectors
* CSE205 — Differential Equations: first- and second-order ODEs, state-space representation and modeling, concepts of stability (Lyapunov, asymptotic, exponential)
* What are the fundamental principles behind DC and BLDC motors,
* How to tune PD controllers to achieve critically damped response,
* What is gravity compensation and how it is implemented in robotic systems,
* What is inverse dynamics.
* What are the advantages of BLDC motors over DC motors,
* Why PD and PID controllers constitute the majority of industrial controllers,
* What methods exist for trajectory generation and tracking,
* How to design an inverse dynamics controller.
* Tune PD and PID controllers,
* Design stable position controllers for manipulators,
* Develop nonlinear controllers such as gravity compensation and inverse dynamics,
* Interface practical robotic hardware (BLDC motors, encoders, microcontrollers) and implement their control algorithms.


### Prerequisite topics


Course Topics
-------------




Course Sections and Topics
| Section | Topics within the section
 |
| --- | --- |
| Robot Hardware | 1. DC and BLDC motors
2. Position sensors (encoders)
3. CAN bus
 |
| Feedback Control | 1. Review of feedback control
2. PD controllers
3. PID controllers
4. Gravity compensation
5. Stability of linear systems
 |
| Position tracking in robots | 1. Linear feedback control in application to manipulators
2. Lyapunov stability analysis
3. Stabilization and trajectory tracking
 |
| Energy, impedance, and force control | 1. Joint-space inverse dynamics of serial manipulators
2. Energy-based control of compliant robots
3. Passivity-based control
4. Adaptive control of flexible joint manipulators
 |


Intended Learning Outcomes (ILOs)
---------------------------------


### What is the main purpose of this course?


The purpose of this course is to review the concepts of linear control theory and then learn some advanced control methods while applying them to practical simple robotic systems with 1 and 2 degrees of freedom. The course also presents all the necessary background of such fundamental components of robotic manipulators as DC and BLDC motors, encoders, microcontrollers and CAN bus (communication protocol). Based on these, the course teaches the student to design and implement on practice simple and advanced control approaches and teaches the students to tune and analyze stability of selected controllers in application to robotic systems.



### ILOs defined at three levels


#### Level 1: What concepts should a student know/remember/explain?


By the end of the course, the students should be able to ...



* What are the fundamental principles behind DC and BLDC motors,
* How to tune PD controllers to achieve critically damped response,
* What is gravity compensation and how it is implemented in robotic systems,
* What is inverse dynamics.


#### Level 2: What basic practical skills should a student be able to perform?


By the end of the course, the students should be able to ...



* What are the advantages of BLDC motors over DC motors,
* Why PD and PID controllers constitute the majority of industrial controllers,
* What methods exist for trajectory generation and tracking,
* How to design an inverse dynamics controller.


#### Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?


By the end of the course, the students should be able to ...



* Tune PD and PID controllers,
* Design stable position controllers for manipulators,
* Develop nonlinear controllers such as gravity compensation and inverse dynamics,
* Interface practical robotic hardware (BLDC motors, encoders, microcontrollers) and implement their control algorithms.


Grading
-------


### Course grading range





| Grade | Range | Description of performance
 |
| --- | --- | --- |
| A. Excellent | 85-100 | -
 |
| B. Good | 70-84 | -
 |
| C. Satisfactory | 55-69 | -
 |
| D. Poor | 0-54 | -
 |


### Course activities and grading breakdown





| Activity Type | Percentage of the overall course grade
 |
| --- | --- |
| Labs/seminar classes | 30
 |
| Quizzes | 30
 |
| Final exam | 40
 |


### Recommendations for students on how to succeed in the course


Resources, literature and reference materials
---------------------------------------------


### Open access resources


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
| Development of individual parts of software product code | 1 | 0 | 0 | 0
 |
| Homework and group projects | 1 | 1 | 1 | 1
 |
| Testing (written or computer based) | 1 | 1 | 1 | 1
 |
| Reports | 1 | 1 | 0 | 0
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
| Question | Describe the basic operation principle of DC motors. | 1
 |
| Question | What are the main advantages of BLDC motors over DC motors? | 1
 |
| Question | Describe operation principles of optical and magnetic encoders. | 1
 |
| Question | Rewrite the equation of DC motor in the state space form. | 0
 |
| Question | Rewrite the equation of cart pole system in the state space form with the state 






x

=
[
θ
,



θ
˙



,
x
,



x
˙




]

T






{\displaystyle {\textstyle \mathbf {x} =[\theta ,{\dot {\theta }},x,{\dot {x}}]^{T}}}

{\displaystyle {\textstyle \mathbf {x} =[\theta ,{\dot {\theta }},x,{\dot {x}}]^{T}}} . | 0
 |
| Question | Find eigen system (values and vectors) of following matrices by hand | 0
 |


#### Section 2





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | What are overshoot and settling time? | 1
 |
| Question | How do the gains of PD controller affect transient response parameters? | 1
 |
| Question | sdf | 1
 |
| Question | Find stiffness matrix of a given parallel robotic platform. | 0
 |
| Question | Perform matrix structural analysis of a cantilever beam. | 0
 |
| Question | Find stiffness matrix of a two-link manipulator with elastic joint. | 0
 |
| Question | Estimate identification accuracy for 3-link manipulator. | 0
 |
| Question | Comment on differences between compliance matrix of a manipulator obtained via CAD modeling and identification results. | 0
 |


#### Section 3





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Give an example of using feedback in activities of daily life. | 1
 |
| Question | Drive error dynamics equations for a given feedback control law. | 1
 |
| Question | For a given differential equation describing robot dynamics and several control laws, find which ones are stable using Lyapunov stability theory. | 1
 |
| Question | How does elasticity affect error dynamics in robot control applications? | 1
 |
| Question | What components of mechanical energy exist in robots with compliance? | 1
 |
| Question | Design PD controller for a rigid two-link manipulator. | 0
 |
| Question | Numerically model behavior of compliant robot with PID controller. | 0
 |
| Question | Compare performance of linear controllers in application to rigid and 2-link manipulator control. | 0
 |
| Question | Analyze stability of a given controller. | 0
 |


#### Section 4





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Provide examples of passive and active systems. | 1
 |
| Question | What are limit cycles? | 1
 |
| Question | What happens with the energy of passive systems with time? | 1
 |
| Question | For a given differential equation that describes pendulum dynamics, do the following: | 1
 |
| Question | Perform input-state linearization for a given system of differential equations. | 1
 |
| Question | Find limit cycles of a given robot with compliance. | 0
 |
| Question | Design gravity and compliance compensator for a robot with flexible joints. | 0
 |
| Question | Implement and simulate passivity-based control over given robot. | 0
 |
| Question | For a given differential equation that describes pendulum dynamics, do the following:Find control law transforming original dynamics into that of a linear mass-spring-damper system;Write position error dynamics for the designed control law (inverse dynamics);Repeat the previous steps if there are uncertainties in some of the system’s parameters. | 0
 |


### Final assessment


**Section 1**



1. Write a differential equation that describes the mechanical part of DC motor.
2. Write a differential equation that describes the electrical part of DC motor.
3. How many CPTs must a 2-channel magnetic encoder have if you want to measure the output displacement of a DC motor with the resolution of 0.1 degree?


**Section 2**



1. Describe main stiffness modeling approaches, their particularities, advantages and limitations.
2. Use variable joint model for a serial manipulator (assume all elements are flexible) to find stiffness matrix.
3. Describe particularities and difficulties of the elastostatic calibration.
4. Find the controller gains that will stabilize a system described by a second order differential equation.


**Section 3**



1. What challenges does robot compliance pose for a control system?
2. Design a position tracking controller for a given compliant system.
3. How does cable elasticity affect dynamics and control of tendon-driven robots?


**Section 4**



1. Provide examples of practical systems with non-collocated feedback. What unique challenges does this pose for control systems?
2. Design a position tracking controller for a given compliant system.
3. Analyze stability of a given system with passivity-based controller
4. What are the physical fundamentals behind the concept of passivity and passivity-based control?


### The retake exam


**Section 1**


**Section 2**


**Section 3**


**Section 4**











