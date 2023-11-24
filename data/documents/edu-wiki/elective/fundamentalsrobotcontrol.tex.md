






Elective:FundamentalsRobotControl.tex
=====================================






Contents
--------


* [1 Fundamentals of Robot Control](#Fundamentals_of_Robot_Control)
	+ [1.1 Course Characteristics](#Course_Characteristics)
		- [1.1.1 Key concepts of the class](#Key_concepts_of_the_class)
		- [1.1.2 What is the purpose of this course?](#What_is_the_purpose_of_this_course.3F)
	+ [1.2 Prerequisites](#Prerequisites)
		- [1.2.1 Course objectives based on Bloom’s taxonomy](#Course_objectives_based_on_Bloom.E2.80.99s_taxonomy)
		- [1.2.2 - What should a student remember at the end of the course?](#-_What_should_a_student_remember_at_the_end_of_the_course.3F)
		- [1.2.3 - What should a student be able to understand at the end of the course?](#-_What_should_a_student_be_able_to_understand_at_the_end_of_the_course.3F)
		- [1.2.4 - What should a student be able to apply at the end of the course?](#-_What_should_a_student_be_able_to_apply_at_the_end_of_the_course.3F)
		- [1.2.5 Course evaluation](#Course_evaluation)
		- [1.2.6 Grades range](#Grades_range)
		- [1.2.7 Resources and reference material](#Resources_and_reference_material)
	+ [1.3 Course Sections](#Course_Sections)
		- [1.3.1 Section 1](#Section_1)
			* [1.3.1.1 Section title:](#Section_title:)
		- [1.3.2 Topics covered in this section:](#Topics_covered_in_this_section:)
		- [1.3.3 What forms of evaluation were used to test students’ performance in this section?](#What_forms_of_evaluation_were_used_to_test_students.E2.80.99_performance_in_this_section.3F)
		- [1.3.4 Typical questions for ongoing performance evaluation within this section](#Typical_questions_for_ongoing_performance_evaluation_within_this_section)
		- [1.3.5 Typical questions for seminar classes (labs) within this section](#Typical_questions_for_seminar_classes_.28labs.29_within_this_section)
		- [1.3.6 Test questions for final assessment in this section](#Test_questions_for_final_assessment_in_this_section)
		- [1.3.7 Section 2](#Section_2)
			* [1.3.7.1 Section title:](#Section_title:_2)
		- [1.3.8 Topics covered in this section:](#Topics_covered_in_this_section:_2)
		- [1.3.9 What forms of evaluation were used to test students’ performance in this section?](#What_forms_of_evaluation_were_used_to_test_students.E2.80.99_performance_in_this_section.3F_2)
		- [1.3.10 Typical questions for ongoing performance evaluation within this section](#Typical_questions_for_ongoing_performance_evaluation_within_this_section_2)
		- [1.3.11 Typical questions for seminar classes (labs) within this section](#Typical_questions_for_seminar_classes_.28labs.29_within_this_section_2)
		- [1.3.12 Test questions for final assessment in this section](#Test_questions_for_final_assessment_in_this_section_2)
		- [1.3.13 Section 3](#Section_3)
			* [1.3.13.1 Section title:](#Section_title:_3)
			* [1.3.13.2 Topics covered in this section:](#Topics_covered_in_this_section:_3)
		- [1.3.14 What forms of evaluation were used to test students’ performance in this section?](#What_forms_of_evaluation_were_used_to_test_students.E2.80.99_performance_in_this_section.3F_3)
		- [1.3.15 Typical questions for ongoing performance evaluation within this section](#Typical_questions_for_ongoing_performance_evaluation_within_this_section_3)
			* [1.3.15.1 Typical questions for seminar classes (labs) within this section](#Typical_questions_for_seminar_classes_.28labs.29_within_this_section_3)
			* [1.3.15.2 Test questions for final assessment in this section](#Test_questions_for_final_assessment_in_this_section_3)
		- [1.3.16 Section 4](#Section_4)
			* [1.3.16.1 Section title:](#Section_title:_4)
			* [1.3.16.2 Topics covered in this section:](#Topics_covered_in_this_section:_4)
		- [1.3.17 What forms of evaluation were used to test students’ performance in this section?](#What_forms_of_evaluation_were_used_to_test_students.E2.80.99_performance_in_this_section.3F_4)
		- [1.3.18 Typical questions for ongoing performance evaluation within this section](#Typical_questions_for_ongoing_performance_evaluation_within_this_section_4)
			* [1.3.18.1 Typical questions for seminar classes (labs) within this section](#Typical_questions_for_seminar_classes_.28labs.29_within_this_section_4)
			* [1.3.18.2 Test questions for final assessment in this section](#Test_questions_for_final_assessment_in_this_section_4)
		- [1.3.19 Section 5](#Section_5)
			* [1.3.19.1 Section title:](#Section_title:_5)
			* [1.3.19.2 Topics covered in this section:](#Topics_covered_in_this_section:_5)
		- [1.3.20 What forms of evaluation were used to test students’ performance in this section?](#What_forms_of_evaluation_were_used_to_test_students.E2.80.99_performance_in_this_section.3F_5)
		- [1.3.21 Typical questions for ongoing performance evaluation within this section](#Typical_questions_for_ongoing_performance_evaluation_within_this_section_5)
			* [1.3.21.1 Typical questions for seminar classes (labs) within this section](#Typical_questions_for_seminar_classes_.28labs.29_within_this_section_5)
			* [1.3.21.2 Test questions for final assessment in this section](#Test_questions_for_final_assessment_in_this_section_5)



Fundamentals of Robot Control
=============================


* **Course name:** Fundamentals of Robot Control
* **Course number:** F19


Course Characteristics
----------------------


### Key concepts of the class


* Introductory nonlinear control over dynamic systems with the focus on robotics
* Stability, pros and cons of nonlinear control systems


### What is the purpose of this course?


Control theory is an integral part of modern robotics, and there is a high chance that most students majoring in Robotics would face the problems of controlling a physical plant (a robot, manipulator, drone, autonomous vehicle) in their research and graduation work as well as their professional careers. Therefore, the main purpose of this course is to prepare the students for solving practical control problems by teaching the most fundamental approaches of nonlinear control used in modern robotics applications.



Prerequisites
-------------


The course will benefit if students already know some topics of mathematics and programming. 
Programming: python, numpy library, Google Colab environment.
Mathematics: 



* Calculus: integration and differentiation, exponentials, gradient.
* Linear Algebra: matrix multiplication, eigenvector and eigenvalue.
* Differential Equations: state-space representation, homogeneous and nonhomogeneous equations, general solution of linear 1st and 2nd order ODEs, stability of solutions.
* Linear control theory: concepts of feedback, open- and closed-loop systems, linear controllers (PD, PID)


How can students fill the gap?



* [3blue1brown playlist on Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) can help to overview selected topics.
* Most lectures of [Steve Brunton](https://youtu.be/Pi7l8mMjYVE) on linear control will be useful.
* Kick start your numpy with the official [quickstart guide](https://numpy.org/doc/stable/user/quickstart.html).


### Course objectives based on Bloom’s taxonomy


### - What should a student remember at the end of the course?


By the end of the course, the students should be able to remember and differentiate



* Basic structure of differential equations describing motion of robotic manipulators,
* Motivation behind and the basic structure of feedback control systems,
* How to find control system’s error dynamics and methods to analyze it,
* General structure of linear controllers (P, PD, PID),
* Physical motivation behind Lyapunov stability analysis,
* Basic structure of robust control system.


### - What should a student be able to understand at the end of the course?


By the end of the course, the students should be able to



* Name the main sources of nonlinearities in physical systems,
* Explain the cons of applying PID controllers to nonlinear systems,
* Understand pros and cons of feedback linearization method,
* Name pros and cons of robust control approach,
* Numerically solve differential equations in MATLAB environment.


### - What should a student be able to apply at the end of the course?


By the end of the course, the students should be able to ...



* Know how to analyze stability of physical systems with Lyapunov direct method,
* Design feedback linearization systems,
* Synthesize robust control systems and tune them,
* Implement nonlinear control in MATLAB environment to simulate the behavior of multi-DOF robotic systems.


### Course evaluation




Course grade breakdown
|  |  | **Proposed points** |
| --- | --- | --- |
| Labs/seminar classes
 | 20
 | 0
 |
| Interim performance assessment
 | 30
 | 60
 |
| Exams
 | 50
 | 40
 |


If necessary, please indicate freely your course’s features in terms of students’ performance assessment:


The course grades are given according to the following rules: Homework assignments (4) = 20 pts, Quizzes (4) = 40 pts, Term project = 40 pts.



### Grades range




Course grading range
|  |  | **Proposed range** |
| --- | --- | --- |
| A. Excellent
 | 90-100
 | 80-100
 |
| B. Good
 | 75-89
 | 60-79
 |
| C. Satisfactory
 | 60-74
 | 40-59
 |
| D. Poor
 | 0-59
 | 0-39
 |


If necessary, please indicate freely your course’s grading features: The first year master course students come with very diverse backgrounds, and therefore the grade requirements for this course are relaxed.



### Resources and reference material


The course is build based on these main textbooks:



* “Applied nonlinear control,” J.-J. Slotine & Weiping Li. Pearson, 1991.
* “Robotics: modelling, planning and control,” Bruno Siciliano, Lorenzo Sciavicco, Luigi Villani, and Giuseppe Oriolo. Springer Science & Business Media, 2010.


Other reference material:



* “Robot modeling and control,” Mark Spong, Seth Hutchinson, M. Vidyasagar. John Wiley & Sons, 2006.
* “Modern Control Systems” (13th Edition), Richard Dorf & Robert H. Bishop. Pearson, 2016.
* “Modern Robotics: Mechanics, Planning, and Control,” Kevin Lynch, Frank Park. Cambridge University Press, 2017 (*also, check out their video materials on YouTube*).


Course Sections
---------------


The main sections of the course and approximate hour distribution between them is as follows:





Course Sections
| **Section** | **Section Title** | **Teaching Hours** |
| --- | --- | --- |
| 1
 | Motion. Kinematics. Dynamics
 | 7
 |
| 2
 | Linear systems. Stability
 | 6
 |
| 3
 | Feedback control systems
 | 3
 |
| 4
 | Feedback linearization
 | 6
 |
| 5
 | Robust control
 | 8
 |


### Section 1


#### Section title:


Motion. Kinematics. Dynamics.



### Topics covered in this section:


* Free body motion
* Manipulator position and orientation
* Homogeneous transformations
* Forward and inverse kinematics
* Kinetic and potential energy
* Euler-Lagrange equations


### What forms of evaluation were used to test students’ performance in this section?



|a|c| & **Yes/No**  

Development of individual parts of software product code & 0  

Homework and group projects & 1  

Midterm evaluation & 0  

Testing (written or computer based) & 1  

Reports & 0  

Essays & 0  

Oral polls & 0  

Discussions & 1  



  





### Typical questions for ongoing performance evaluation within this section


1. Given initial and final object position and orientations, obtain the corresponding transformation matrix.
2. Find the Jacobian for a given manipulator.
3. For a given differential equation describing a physical system, and for given kinetic (K) and potential energies (U) do the following:
	* Show that there always exists a solution with respect to acceleration and that it is unique;
	* Demonstrate that the system’s Hamiltonian H = K + U remains constant in the absence of external torques and forces;
	* Show that the rate of change of the total energy equals instantaneous mechanical power.
4. For a given manipulator with known Jacobian, do the following:
	* Find kinetic and potential energies of the robot;
	* Drive the Euler-Lagrange differential equation of motion.


### Typical questions for seminar classes (labs) within this section


1. Do the following with MATLAB Robotics Toolbox:
	* Compute basic rotation and homogeneous transformation matrices;
	* Create a two-link manipulator and solve its forward kinematics;
	* Simulate forward dynamics;
	* Compute inertial, Coriolis and gravitational forces for the manipulator.
2. Compute and analyze inertial tensor for a given robotic manipulator;
3. For manipulators with different kinematic configurations, analytically derive their Jacobian matrices;
4. Derive and analyze Euler-Lagrange equations describing dynamics of a given manipulator (required torques, singularities).


### Test questions for final assessment in this section


1. What is a rotation matrix and what does it describe?
2. How to find a homogeneous transformation matrix? How is it different from rotation matrix?
3. What is manipulator Jacobian? How does it relate static forces and torques? How can one use the Jacobian to analyze manipulator singularities?
4. What is physical nature of the terms of Euler-Lagrange equations of robot motion?
5. What are the main properties of the basic terms of differential equations of motion (invertibility, positive definiteness, singularities, limits).


### Section 2


#### Section title:


Linear systems. Stability



### Topics covered in this section:


* State-space equations
* Eigenvalues and eigenvectors
* Phase plane analysis
* Energy and stability
* Lyapunov’s direct method
* Lyapunov stability analysis


### What forms of evaluation were used to test students’ performance in this section?



|a|c| & **Yes/No**  

Development of individual parts of software product code & 0  

Homework and group projects & 1  

Midterm evaluation & 0  

Testing (written or computer based) & 1  

Reports & 0  

Essays & 0  

Oral polls & 1  

Discussions & 1  



  





### Typical questions for ongoing performance evaluation within this section


1. Convert given differential equation into state-space form
2. Find eigenvalue for a given matrix
3. Show that given a constant matrix 





M




{\textstyle {\textbf {M}}}

![{\textstyle {\textbf {M}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c10cb11a1593a1bd46e0540350ff33377694def1) and any time-varying vector 





x




{\textstyle {\textbf {x}}}

![{\textstyle {\textbf {x}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/98dbe7268088c5e7fdb33d7ac08b743d5c4d5dfc), the time derivative of the scalar 





x


T



M
x



{\textstyle \mathbf {x} ^{T}\mathbf {Mx} }

![{\textstyle \mathbf {x} ^{T}\mathbf {Mx} }](https://wikimedia.org/api/rest_v1/media/math/render/svg/684fa1caacd58b55071857b03d5a427dae81cccf) can be written in the given form.
4. For a given system of differential equations:
	* Find equilibria points;
	* Given a Lyapunov function, analyze system stability using Lyapunov’s direct method;
	* Analyze system stability in a given range.


### Typical questions for seminar classes (labs) within this section


1. For a given differential equation, find the values of coefficients 




k

1




{\textstyle k\_{1}}

![{\textstyle k_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d6f9b2fbaa7850ed8769501088a6825203e38182) and 




k

2




{\textstyle k\_{2}}

![{\textstyle k_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/70fb0b47f460e1b089a5ed2b242f3f7103c7cc74) that would make it critically damped.
2. Convert a given system of differential equations into state-space form.
3. For an equation given in the state space form, write it as an ordinary differential equation for specified input and output variables.
4. Analyze system’s stability given equation of its full energy.
5. Apply Lyapunov’s direct method to analyze stability of a physical system.


### Test questions for final assessment in this section


1. Evaluate stability of a linear system whose dynamics is written in the state-space form.
2. What must be the properties of Lyapunov function candidate and its time derivative to confirm
	* Local stability,
	* Global stability of the system.
3. How to analyze system’s stability based on its phase portrait (with examples)?
4. Describe physical motivation behind Lyapunov’s direct method and how it used to analyze stability of dynamical systems.


### Section 3


#### Section title:


Feedback control systems



#### Topics covered in this section:


* Feedback and building control loops
* Stabilization and trajectory tracking
* Linear regulators (P, PD, PID)


### What forms of evaluation were used to test students’ performance in this section?



|a|c| & **Yes/No**  

Development of individual parts of software product code & 0  

Homework and group projects & 0  

Midterm evaluation & 0  

Testing (written or computer based) & 0  

Reports & 0  

Essays & 0  

Oral polls & 1  

Discussions & 1  



  





### Typical questions for ongoing performance evaluation within this section


1. Give an example of using feedback in activities of daily life
2. Drive error dynamics equations for a given feedback control law
3. What are the physical analogies for the individual terms of PD-controller?
4. How to implement PD regulator in MATLAB software?


#### Typical questions for seminar classes (labs) within this section


1. Solve numerically in MATLAB a second-order ODE for the following controller types: P, PD, PID.
2. Analyze stability of a given linear control system.
3. How individual gains of PD and PID controllers affect transient and steady-state response?
4. How does underestimation of system parameters affect performance of linear controllers and how to improve it?


#### Test questions for final assessment in this section


1. What is the physical analog of PD-regulator in application to control over second-oder mechanical systems?
2. For a given system described by differential equations, design a linear control system and analyze its stability.
3. Describe pros and cons of linear controllers in application to nonlinear system control.


### Section 4


#### Section title:


Feedback linearization



#### Topics covered in this section:


* Joint-space inverse dynamics of serial manipulators
* Stabilization and trajectory tracking problems
* Input-state linearization


### What forms of evaluation were used to test students’ performance in this section?



|a|c| & **Yes/No**  

Development of individual parts of software product code & 0  

Homework and group projects & 1  

Midterm evaluation & 0  

Testing (written or computer based) & 1  

Reports & 0  

Essays & 0  

Oral polls & 1  

Discussions & 1  



  





### Typical questions for ongoing performance evaluation within this section


1. For a given differential equation that describes pendulum dynamicsm do the following:
	* Find control law transforming original dynamics into that of a linear mass-spring-damper system;
	* Write position error dynamics for the designed control law (inverse dynamics);
	* Repeat the previous steps if there are uncertainties in some of the system’s parameters.
2. For a given general form of dynamics equation, demonstrate that the following control laws guarantee system stability.
3. Simulate dynamics of given nonlinear system in MATLAB for given control law.
4. Perform input-state linearization for a given system of differential equations.


#### Typical questions for seminar classes (labs) within this section


1. Find control law that linearizes a given differential equation.
2. Analyze stability of given nonlinear systems and contribution of individual terms to system stability.
3. Find general feedback linearization law for a given system of differential equations.
4. Analyze stability and limitations of a given feedback linearization control law over a two-link manipulator.


#### Test questions for final assessment in this section


1. What are the pros and cons of feedback linearization approach?
2. Provide examples of systems (differential equations) for which feedback linearization can result in infinite control effort.
3. What are the typical issues when applying feedback linearization approach to control over robotic manipulators?


### Section 5


#### Section title:


Robust control



#### Topics covered in this section:


* Sliding modes in dynamic systems
* Robust control in scalar and matrix form
* Stability and tuning of robust controllers
* Control law smoothening.


### What forms of evaluation were used to test students’ performance in this section?



|a|c| & **Yes/No**  

Development of individual parts of software product code & 0  

Homework and group projects & 1  

Midterm evaluation & 0  

Testing (written or computer based) & 0  

Reports & 1  

Essays & 0  

Oral polls & 1  

Discussions & 1  



  





### Typical questions for ongoing performance evaluation within this section


1. Name uncertainties typical for mechanical systems
2. Analyze system behavior in sliding mode
3. Simulate system behavior with robust control in MATLAB
4. Numerically implement control law smoothening for a robust controller.


#### Typical questions for seminar classes (labs) within this section


1. How to synthesize robust controller for a given range of system parameters’ deviations?
2. Describe the effect of robust gain coefficient 



k


{\textstyle k}

![{\textstyle k}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0d5595fc0c47452f8fc2aa6e29c3611f047714b0) on system stability, control output and resulting system behavior.
3. Design robust controller for a dynamical system described by a given set of differential equations and implement it in MATLAB.
4. Analyze stability of robust control system for a robotic manipulator with given equation of motion.


#### Test questions for final assessment in this section


1. Describe typical sources of uncertainties and parameter deviations in models of physical and mechanical systems, their typical ranges and influence on system behavior.
2. Name pros and cons of robust control systems with and without control law smoothening.
3. How to tune robust controller terms to compensate for system uncertainties?










