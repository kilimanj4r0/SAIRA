






MSc: Fundamentals of Robot Control
==================================






Contents
--------


* [1 Fundamentals of Robot Control](#Fundamentals_of_Robot_Control)
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
			* [2.2.1.5 Section 5](#Section_5)
		- [2.2.2 Final assessment](#Final_assessment)
		- [2.2.3 The retake exam](#The_retake_exam)



Fundamentals of Robot Control
=============================


* **Course name**: Fundamentals of Robot Control
* **Code discipline**: F19
* **Subject area**:


Short Description
-----------------


This course covers the following concepts: Introductory nonlinear control over dynamic systems with the focus on robotics; Stability, pros and cons of nonlinear control systems.



Prerequisites
-------------


### Prerequisite subjects


* python,
* numpy library,
* Google Colab environment
* CSE201 — Mathematical Analysis I and CSE203 — Mathematical Analysis II]: integration and differentiation, exponentials, gradient.
* CSE202 — Analytical Geometry and Linear Algebra I
* CSE204 — Analytic Geometry And Linear Algebra II: matrix multiplication, eigenvector and eigenvalue.
* CSE205 — Differential Equations: state-space representation, homogeneous and nonhomogeneous equations, general solution of linear 1st and 2nd order ODEs, stability of solutions.
* Linear control theory: concepts of feedback, open- and closed-loop systems, linear controllers (PD, PID)


### Prerequisite topics


Course Topics
-------------




Course Sections and Topics
| Section | Topics within the section
 |
| --- | --- |
| Motion. Kinematics. Dynamics. | 1. Free body motion
2. Manipulator position and orientation
3. Homogeneous transformations
4. Forward and inverse kinematics
5. Kinetic and potential energy
6. Euler-Lagrange equations
 |
| Linear systems. Stability | 1. State-space equations
2. Eigenvalues and eigenvectors
3. Phase plane analysis
4. Energy and stability
5. Lyapunov’s direct method
6. Lyapunov stability analysis
 |
| Feedback control systems | 1. Feedback and building control loops
2. Stabilization and trajectory tracking
3. Linear regulators (P, PD, PID)
 |
| Feedback linearization | 1. Joint-space inverse dynamics of serial manipulators
2. Stabilization and trajectory tracking problems
3. Input-state linearization
 |
| Robust control | 1. Sliding modes in dynamic systems
2. Robust control in scalar and matrix form
3. Stability and tuning of robust controllers
4. Control law smoothening.
 |


Intended Learning Outcomes (ILOs)
---------------------------------


### What is the main purpose of this course?


Control theory is an integral part of modern robotics, and there is a high chance that most students majoring in Robotics would face the problems of controlling a physical plant (a robot, manipulator, drone, autonomous vehicle) in their research and graduation work as well as their professional careers. Therefore, the main purpose of this course is to prepare the students for solving practical control problems by teaching the most fundamental approaches of nonlinear control used in modern robotics applications.



### ILOs defined at three levels


#### Level 1: What concepts should a student know/remember/explain?


By the end of the course, the students should be able to ...



* Basic structure of differential equations describing motion of robotic manipulators,
* Motivation behind and the basic structure of feedback control systems,
* How to find control system’s error dynamics and methods to analyze it,
* General structure of linear controllers (P, PD, PID),
* Physical motivation behind Lyapunov stability analysis,
* Basic structure of robust control system.


#### Level 2: What basic practical skills should a student be able to perform?


By the end of the course, the students should be able to ...



* Name the main sources of nonlinearities in physical systems,
* Explain the cons of applying PID controllers to nonlinear systems,
* Understand pros and cons of feedback linearization method,
* Name pros and cons of robust control approach,
* Numerically solve differential equations in MATLAB environment.


#### Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?


By the end of the course, the students should be able to ...



* Know how to analyze stability of physical systems with Lyapunov direct method,
* Design feedback linearization systems,
* Synthesize robust control systems and tune them,
* Implement nonlinear control in MATLAB environment to simulate the behavior of multi-DOF robotic systems.


Grading
-------


### Course grading range





| Grade | Range | Description of performance
 |
| --- | --- | --- |
| A. Excellent | 80-100 | -
 |
| B. Good | 60-79 | -
 |
| C. Satisfactory | 40-59 | -
 |
| D. Poor | 0-39 | -
 |


### Course activities and grading breakdown





| Activity Type | Percentage of the overall course grade
 |
| --- | --- |
| Labs/seminar classes | 0
 |
| Interim performance assessment | 60
 |
| Exams | 40
 |


### Recommendations for students on how to succeed in the course


Resources, literature and reference materials
---------------------------------------------


### Open access resources


* “Applied nonlinear control,” J.-J. Slotine & Weiping Li. Pearson, 1991.
* “Robotics: modelling, planning and control,” Bruno Siciliano, Lorenzo Sciavicco, Luigi Villani, and Giuseppe Oriolo. Springer Science & Business Media, 2010.
* “Robot modeling and control,” Mark Spong, Seth Hutchinson, M. Vidyasagar. John Wiley & Sons, 2006.
* “Modern Control Systems” (13th Edition), Richard Dorf & Robert H. Bishop. Pearson, 2016.
* “Modern Robotics: Mechanics, Planning, and Control,” Kevin Lynch, Frank Park. Cambridge University Press, 2017 (also, check out their video materials on YouTube).


### Closed access resources


### Software and tools used within the course


Teaching Methodology: Methods, techniques, & activities
=======================================================


Activities and Teaching Methods
-------------------------------




Activities within each section
| Learning Activities | Section 1 | Section 2 | Section 3 | Section 4 | Section 5
 |
| --- | --- | --- | --- | --- | --- |
| Homework and group projects | 1 | 1 | 0 | 1 | 1
 |
| Testing (written or computer based) | 1 | 1 | 0 | 1 | 0
 |
| Discussions | 1 | 1 | 1 | 1 | 1
 |
| Oral polls | 0 | 1 | 1 | 1 | 1
 |
| Reports | 0 | 0 | 0 | 0 | 1
 |


Formative Assessment and Course Activities
------------------------------------------


### Ongoing performance assessment


#### Section 1





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Given initial and final object position and orientations, obtain the corresponding transformation matrix. | 1
 |
| Question | Find the Jacobian for a given manipulator. | 1
 |
| Question | For a given differential equation describing a physical system, and for given kinetic (K) and potential energies (U) do the following:Show that there always exists a solution with respect to acceleration and that it is unique;Demonstrate that the system’s Hamiltonian H = K + U remains constant in the absence of external torques and forces;Show that the rate of change of the total energy equals instantaneous mechanical power. | 1
 |
| Question | For a given manipulator with known Jacobian, do the following:Find kinetic and potential energies of the robot;Drive the Euler-Lagrange differential equation of motion. | 1
 |
| Question | Do the following with MATLAB Robotics Toolbox:Compute basic rotation and homogeneous transformation matrices;Create a two-link manipulator and solve its forward kinematics;Simulate forward dynamics;Compute inertial, Coriolis and gravitational forces for the manipulator. | 0
 |
| Question | Compute and analyze inertial tensor for a given robotic manipulator; | 0
 |
| Question | For manipulators with different kinematic configurations, analytically derive their Jacobian matrices; | 0
 |
| Question | Derive and analyze Euler-Lagrange equations describing dynamics of a given manipulator (required torques, singularities). | 0
 |


#### Section 2





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Convert given differential equation into state-space form | 1
 |
| Question | Find eigenvalue for a given matrix | 1
 |
| Question | Show that given a constant matrix 







M






{\displaystyle {\textstyle {\textbf {M}}}}

{\displaystyle {\textstyle {\textbf {M}}}} and any time-varying vector 







x






{\displaystyle {\textstyle {\textbf {x}}}}

{\displaystyle {\textstyle {\textbf {x}}}} , the time derivative of the scalar 







x


T



M
x





{\displaystyle {\textstyle \mathbf {x} ^{T}\mathbf {Mx} }}

{\displaystyle {\textstyle \mathbf {x} ^{T}\mathbf {Mx} }} can be written in the given form. | 1
 |
| Question | For a given system of differential equations:Find equilibria points;Given a Lyapunov function, analyze system stability using Lyapunov’s direct method;Analyze system stability in a given range. | 1
 |
| Question | For a given differential equation, find the values of coefficients 






k

1






{\displaystyle {\textstyle k\_{1}}}

{\displaystyle {\textstyle k_{1}}} and 






k

2






{\displaystyle {\textstyle k\_{2}}}

{\displaystyle {\textstyle k_{2}}} that would make it critically damped. | 0
 |
| Question | Convert a given system of differential equations into state-space form. | 0
 |
| Question | For an equation given in the state space form, write it as an ordinary differential equation for specified input and output variables. | 0
 |
| Question | Analyze system’s stability given equation of its full energy. | 0
 |
| Question | Apply Lyapunov’s direct method to analyze stability of a physical system. | 0
 |


#### Section 3





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Give an example of using feedback in activities of daily life | 1
 |
| Question | Drive error dynamics equations for a given feedback control law | 1
 |
| Question | What are the physical analogies for the individual terms of PD-controller? | 1
 |
| Question | How to implement PD regulator in MATLAB software? | 1
 |
| Question | Solve numerically in MATLAB a second-order ODE for the following controller types: P, PD, PID. | 0
 |
| Question | Analyze stability of a given linear control system. | 0
 |
| Question | How individual gains of PD and PID controllers affect transient and steady-state response? | 0
 |
| Question | How does underestimation of system parameters affect performance of linear controllers and how to improve it? | 0
 |


#### Section 4





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | For a given differential equation that describes pendulum dynamicsm do the following:Find control law transforming original dynamics into that of a linear mass-spring-damper system;Write position error dynamics for the designed control law (inverse dynamics);Repeat the previous steps if there are uncertainties in some of the system’s parameters. | 1
 |
| Question | For a given general form of dynamics equation, demonstrate that the following control laws guarantee system stability. | 1
 |
| Question | Simulate dynamics of given nonlinear system in MATLAB for given control law. | 1
 |
| Question | Perform input-state linearization for a given system of differential equations. | 1
 |
| Question | Find control law that linearizes a given differential equation. | 0
 |
| Question | Analyze stability of given nonlinear systems and contribution of individual terms to system stability. | 0
 |
| Question | Find general feedback linearization law for a given system of differential equations. | 0
 |
| Question | Analyze stability and limitations of a given feedback linearization control law over a two-link manipulator. | 0
 |


#### Section 5





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Name uncertainties typical for mechanical systems | 1
 |
| Question | Analyze system behavior in sliding mode | 1
 |
| Question | Simulate system behavior with robust control in MATLAB | 1
 |
| Question | Numerically implement control law smoothening for a robust controller. | 1
 |
| Question | How to synthesize robust controller for a given range of system parameters’ deviations? | 0
 |
| Question | Describe the effect of robust gain coefficient 





k




{\displaystyle {\textstyle k}}

{\displaystyle {\textstyle k}} on system stability, control output and resulting system behavior. | 0
 |
| Question | Design robust controller for a dynamical system described by a given set of differential equations and implement it in MATLAB. | 0
 |
| Question | Analyze stability of robust control system for a robotic manipulator with given equation of motion. | 0
 |


### Final assessment


**Section 1**



1. What is a rotation matrix and what does it describe?
2. How to find a homogeneous transformation matrix? How is it different from rotation matrix?
3. What is manipulator Jacobian? How does it relate static forces and torques? How can one use the Jacobian to analyze manipulator singularities?
4. What is physical nature of the terms of Euler-Lagrange equations of robot motion?
5. What are the main properties of the basic terms of differential equations of motion (invertibility, positive definiteness, singularities, limits).


**Section 2**



1. Evaluate stability of a linear system whose dynamics is written in the state-space form.
2. What must be the properties of Lyapunov function candidate and its time derivative to confirm


Local stability,
Global stability of the system.



1. How to analyze system’s stability based on its phase portrait (with examples)?
2. Describe physical motivation behind Lyapunov’s direct method and how it used to analyze stability of dynamical systems.


**Section 3**



1. What is the physical analog of PD-regulator in application to control over second-oder mechanical systems?
2. For a given system described by differential equations, design a linear control system and analyze its stability.
3. Describe pros and cons of linear controllers in application to nonlinear system control.


**Section 4**



1. What are the pros and cons of feedback linearization approach?
2. Provide examples of systems (differential equations) for which feedback linearization can result in infinite control effort.
3. What are the typical issues when applying feedback linearization approach to control over robotic manipulators?


**Section 5**



1. Describe typical sources of uncertainties and parameter deviations in models of physical and mechanical systems, their typical ranges and influence on system behavior.
2. Name pros and cons of robust control systems with and without control law smoothening.
3. How to tune robust controller terms to compensate for system uncertainties?


### The retake exam


**Section 1**


**Section 2**


**Section 3**


**Section 4**


**Section 5**











