






BSc: Control Theory
===================






Contents
--------


* [1 Control Theory](#Control_Theory)
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
		- [2.2.2 Final assessment](#Final_assessment)
		- [2.2.3 The retake exam](#The_retake_exam)



Control Theory
==============


* **Course name**: Control Theory
* **Code discipline**: [S20]
* **Subject area**: Sensors and actuators; Robotic control.


Short Description
-----------------


This course covers the following concepts: Introduction to Linear Control, Stability of linear dynamical systems; Controller design; Sensing, observers, Adaptive control.



Prerequisites
-------------


### Prerequisite subjects


* [CSE204 - Geometry And Linear Algebra II](https://eduwiki.innopolis.university/index.php/BSc:AnalyticGeometryAndLinearAlgebraI): Semidefinite matrices, Eigenvalues, Eigendecomposition (weak prerequisite), matrix exponentials (weak prerequisite), SVD (weak prerequisite)
* [CSE205 - Differential Equations](https://eduwiki.innopolis.university/index.php/BSc:DifferentialEquations)


### Prerequisite topics


Course Topics
-------------




Course Sections and Topics
| Section | Topics within the section
 |
| --- | --- |
| Introduction to Linear Control, Stability of linear dynamical systems | 1. Control, introduction. Examples.
2. Single input single output (SISO) systems. Block diagrams.
3. From linear differential equations to state space models.
4. DC motor as a linear system.
5. Spring-damper as a linear system.
6. The concept of stability of the control system. Proof of stability for a linear system with negative real parts of eigenvalues.
7. Multi input multi output (MIMO) systems.
8. Linear Time Invariant (LTI) systems and their properties.
9. Linear Time Varying (LTV) systems and their properties.
10. Transfer function representation.
 |
| Controller design. | 1. Stabilizing control. Control error.
2. Proportional control.
3. PD control. Order of a system and order of the controller.
4. PID control.
5. P, PD and PID control for DC motor.
6. Trajectory tracking. Control input types. Standard inputs (Heaviside step function, Dirac delta function, sine wave).
7. Tuning PD and PID. Pole placement.
8. Formal statements about stability. Lyapunov theory.
9. Types of stability; Lyapunov stability, asymptotic stability, exponential stability.
10. Eigenvalues in stability theory. Reasoning about solution of the autonomous linear system.
11. Stability proof for PD control.
12. Stability in stabilizing control and trajectory tracking.
13. Frequency response. Phase response.
14. Optimal control of linear systems. From Hamilton-Jacobi-Bellman to algebraic Riccati equation. LQR.
15. Stability of LQR.
16. Controllability.
 |
| Sensing, observers, Adaptive control | 1. Modelling digital sensors: quantization, discretization, lag.
2. Modelling sensor noise. Gaussian noise. Additive models. Multiplicative models. Dynamic sensor models.
3. Observability.
4. Filters.
5. State observers.
6. Optimal state observer for linear systems.
7. Linearization of nonlinear systems.
8. Linearization along trajectory.
9. Linearization of Inverted pendulum dynamics.
10. Model errors. Differences between random disturbances and unmodeled dynamics/processes.
11. Adaptive control.
12. Control for sets of linear systems.
13. Discretization, discretization error.
14. Control for discrete linear systems.
15. Stability of discrete linear systems.
 |


Intended Learning Outcomes (ILOs)
---------------------------------


### What is the main purpose of this course?


Linear Control Theory is both an active tool for modern industrial engineering and a prerequisite for most of the state-of-the-art level control techniques and the corresponding courses. With this in mind, the Linear Control course is both building a foundation for the following development of the student as a learner in the fields of Robotics, Control, Nonlinear Dynamics and others, as well as it is one of the essential practical courses in the engineering curricula.



### ILOs defined at three levels


#### Level 1: What concepts should a student know/remember/explain?


By the end of the course, the students should be able to ...



* methods for control synthesis (linear controller gain tuning)
* methods for controller analysis
* methods for sensory data processing for linear systems


#### Level 2: What basic practical skills should a student be able to perform?


By the end of the course, the students should be able to ...



* State-space models
* Eigenvalue analysis for linear systems
* Proportional and PD controllers
* How to stabilize a linear system
* Lyapunov Stability
* How to check if the system is controllable
* Observer design
* Sources of sensor noise
* Filters
* Adaptive Control
* Optimal Control
* Linear Quadratic Regulator


#### Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?


By the end of the course, the students should be able to ...



* Turn a system of linear differential equations into a state-space model.
* Design a controller by solving Algebraic Riccati eq.
* Find if a system is stable or not, using eigenvalue analysis.


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
| C. Satisfactory | 50-69 | -
 |
| D. Poor | 0-49 | -
 |


### Course activities and grading breakdown





| Activity Type | Percentage of the overall course grade
 |
| --- | --- |
| Labs/seminar classes | 30
 |
| Interim performance assessment | 20
 |
| Exams | 50
 |


### Recommendations for students on how to succeed in the course


Resources, literature and reference materials
---------------------------------------------


### Open access resources


* Ogata, K., 1994. Solving control engineering problems with MATLAB. Englewood Cliffs, NJ: Prentice-Hall.
* Williams, R.L. and Lawrence, D.A., 2007. Linear state-space control systems. John Wiley & Sons.
* Ogata, K., 1995. Discrete-time control systems (Vol. 2, pp. 446-480). Englewood Cliffs, NJ: Prentice Hall.


### Closed access resources


### Software and tools used within the course


Teaching Methodology: Methods, techniques, & activities
=======================================================


Activities and Teaching Methods
-------------------------------




Activities within each section
| Learning Activities | Section 1 | Section 2 | Section 3
 |
| --- | --- | --- | --- |
| Homework and group projects | 1 | 1 | 1
 |
| Testing (written or computer based) | 1 | 0 | 0
 |
| Reports | 1 | 1 | 1
 |
| Midterm evaluation | 0 | 1 | 0
 |
| Discussions | 0 | 1 | 0
 |


Formative Assessment and Course Activities
------------------------------------------


### Ongoing performance assessment


#### Section 1





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | What is a linear dynamical system? | 1
 |
| Question | What is an LTI system? | 1
 |
| Question | What is an LTV system? | 1
 |
| Question | Provide examples of LTI systems. | 1
 |
| Question | What is a MIMO system? | 1
 |
| Question | Simulate a linear dynamic system as a higher order differential equation or in state-space form (Language is a free choice, Python and Google Colab are recommended. Use built-in solvers or implement Runge-Kutta or Euler method. | 0
 |


#### Section 2





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | What is stability in the sense of Lyapunov? | 1
 |
| Question | What is stabilizing control? | 1
 |
| Question | What is trajectory tracking? | 1
 |
| Question | Why the control for a state-space system does not include the derivative of the state variable in the feedback law? | 1
 |
| Question | How can a PD controller for a second-order linear mechanical system can be re-written in the state-space form? | 1
 |
| Question | Write a closed-loop dynamics for an LTI system with a proportional controller. | 1
 |
| Question | Give stability conditions for an LTI system with a proportional controller. | 1
 |
| Question | Provide an example of a LTV system with negative eigenvalues that is not stable. | 1
 |
| Question | Write algebraic Riccati equation for a standard additive quadratic cost. | 1
 |
| Question | Derive algebraic Riccati equation for a given additive quadratic cost. | 1
 |
| Question | Derive differential Riccati equation for a standard additive quadratic cost. | 1
 |
| Question | What is the meaning of the unknown variable in the Riccati equation? What are its property in case of LTI dynamics. | 1
 |
| Question | What is a frequency response? | 1
 |
| Question | What is a phase response? | 1
 |
| Question | Design control for an LTI system using pole placement. | 0
 |
| Question | Design control for an LTI system using Riccati (LQR). | 0
 |
| Question | Simulate an LTI system with LQR controller. | 0
 |


#### Section 3





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | What are the sources of sensor noise? | 1
 |
| Question | How can we combat the lack of sensory information? | 1
 |
| Question | When it is possible to combat the lack of sensory information? | 1
 |
| Question | How can we combat the sensory noise? | 1
 |
| Question | What is an Observer? | 1
 |
| Question | What is a filter? | 1
 |
| Question | How is additive noise different from multiplicative noise? | 1
 |
| Question | Simulate an LTI system with proportional control and sensor noise. | 0
 |
| Question | Design an observer for an LTI system with proportional control and lack of sensory information. | 0
 |


### Final assessment


**Section 1**



1. Convert a linear differential equation into a state space form.
2. Convert a transfer function into a state space form.
3. Convert a linear differential equation into a transfer function.
4. What does it mean for a linear differential equation to be stable?


**Section 2**



1. You have a linear system: 








x
˙



=
A
x
+
B
u




{\displaystyle {\displaystyle {\dot {x}}=Ax+Bu}}

![{\displaystyle {\displaystyle {\dot {x}}=Ax+Bu}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e4bf3ada8bafed299cdfaacc34637b816d2b4477) and a cost function: a) 





J
=
∫
(

x

⊤


Q
x
+

u

⊤


I
u
)
d
t




{\displaystyle {\textstyle J=\int (x^{\top }Qx+u^{\top }Iu)dt}}

![{\displaystyle {\textstyle J=\int (x^{\top }Qx+u^{\top }Iu)dt}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c274707dff116b2105e84a0125a9197b45760f83) b) 





J
=
∫
(

x

⊤


I
x
+

u

⊤


R
u
)
d
t




{\displaystyle {\textstyle J=\int (x^{\top }Ix+u^{\top }Ru)dt}}

![{\displaystyle {\textstyle J=\int (x^{\top }Ix+u^{\top }Ru)dt}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2e39947b7aa2e15bcf70da52199efe8a4bd24514) Write Riccati eq. and find LQR gain analytically.
2. You have a linear system a) 







[







x
˙




1










x
˙




2





]


=


[



1


10




−
3


4



]




[




x

1







x

2





]






{\displaystyle {\textstyle {\begin{bmatrix}{\dot {x}}\_{1}\\{\dot {x}}\_{2}\end{bmatrix}}={\begin{bmatrix}1&10\\-3&4\end{bmatrix}}{\begin{bmatrix}x\_{1}\\x\_{2}\end{bmatrix}}}}

![{\displaystyle {\textstyle {\begin{bmatrix}{\dot {x}}_{1}\\{\dot {x}}_{2}\end{bmatrix}}={\begin{bmatrix}1&10\\-3&4\end{bmatrix}}{\begin{bmatrix}x_{1}\\x_{2}\end{bmatrix}}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d1bc5bdf4ddf06f4fa774d9346aca4a2728a0b50) b) 







[







x
˙




1










x
˙




2





]


=


[



−
2


1




2


40



]




[




x

1







x

2





]






{\displaystyle {\textstyle {\begin{bmatrix}{\dot {x}}\_{1}\\{\dot {x}}\_{2}\end{bmatrix}}={\begin{bmatrix}-2&1\\2&40\end{bmatrix}}{\begin{bmatrix}x\_{1}\\x\_{2}\end{bmatrix}}}}

![{\displaystyle {\textstyle {\begin{bmatrix}{\dot {x}}_{1}\\{\dot {x}}_{2}\end{bmatrix}}={\begin{bmatrix}-2&1\\2&40\end{bmatrix}}{\begin{bmatrix}x_{1}\\x_{2}\end{bmatrix}}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/eb9e56fd8715942dddcf766918860bea58b3ab17) Prove whether or not it is stable.
3. You have a linear system a) 







[







x
˙




1










x
˙




2





]


=


[



1


10




−
3


4



]




[




x

1







x

2





]


+


[




u

1







u

2





]






{\displaystyle {\displaystyle {\begin{bmatrix}{\dot {x}}\_{1}\\{\dot {x}}\_{2}\end{bmatrix}}={\begin{bmatrix}1&10\\-3&4\end{bmatrix}}{\begin{bmatrix}x\_{1}\\x\_{2}\end{bmatrix}}+{\begin{bmatrix}u\_{1}\\u\_{2}\end{bmatrix}}}}

![{\displaystyle {\displaystyle {\begin{bmatrix}{\dot {x}}_{1}\\{\dot {x}}_{2}\end{bmatrix}}={\begin{bmatrix}1&10\\-3&4\end{bmatrix}}{\begin{bmatrix}x_{1}\\x_{2}\end{bmatrix}}+{\begin{bmatrix}u_{1}\\u_{2}\end{bmatrix}}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/87faecb7b594fc89188ec0b29cc1549a60a38168) b) 







[







x
˙




1










x
˙




2





]


=


[



−
2


1




2


40



]




[




x

1







x

2





]


+


[




u

1







u

2





]






{\displaystyle {\displaystyle {\begin{bmatrix}{\dot {x}}\_{1}\\{\dot {x}}\_{2}\end{bmatrix}}={\begin{bmatrix}-2&1\\2&40\end{bmatrix}}{\begin{bmatrix}x\_{1}\\x\_{2}\end{bmatrix}}+{\begin{bmatrix}u\_{1}\\u\_{2}\end{bmatrix}}}}

![{\displaystyle {\displaystyle {\begin{bmatrix}{\dot {x}}_{1}\\{\dot {x}}_{2}\end{bmatrix}}={\begin{bmatrix}-2&1\\2&40\end{bmatrix}}{\begin{bmatrix}x_{1}\\x_{2}\end{bmatrix}}+{\begin{bmatrix}u_{1}\\u_{2}\end{bmatrix}}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f501668baf1f22b9200a11c2465d2ef3d73d270f) Your controller is: a) 







[




u

1







u

2





]


=


[



100


1




1


20



]




[




x

1







x

2





]






{\displaystyle {\textstyle {\begin{bmatrix}u\_{1}\\u\_{2}\end{bmatrix}}={\begin{bmatrix}100&1\\1&20\end{bmatrix}}{\begin{bmatrix}x\_{1}\\x\_{2}\end{bmatrix}}}}

![{\displaystyle {\textstyle {\begin{bmatrix}u_{1}\\u_{2}\end{bmatrix}}={\begin{bmatrix}100&1\\1&20\end{bmatrix}}{\begin{bmatrix}x_{1}\\x_{2}\end{bmatrix}}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/91b22a42571dee07244b61cd734f77245322356a) b) 







[




u

1







u

2





]


=


[



7


2




2


5



]




[




x

1







x

2





]






{\displaystyle {\textstyle {\begin{bmatrix}u\_{1}\\u\_{2}\end{bmatrix}}={\begin{bmatrix}7&2\\2&5\end{bmatrix}}{\begin{bmatrix}x\_{1}\\x\_{2}\end{bmatrix}}}}

![{\displaystyle {\textstyle {\begin{bmatrix}u_{1}\\u_{2}\end{bmatrix}}={\begin{bmatrix}7&2\\2&5\end{bmatrix}}{\begin{bmatrix}x_{1}\\x_{2}\end{bmatrix}}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4872fd9ba71d2c96d6a2fe5237bcdf4933f44566) Prove whether the control system is stable.
4. You have linear dynamics:


a) 





2



q
¨



+
3



q
˙



−
5
q
=
u




{\displaystyle {\textstyle 2{\ddot {q}}+3{\dot {q}}-5q=u}}

![{\displaystyle {\textstyle 2{\ddot {q}}+3{\dot {q}}-5q=u}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/bbd10b4b71db048873878c3a52d3a8e7cb3a3efc) 
b) 





10



q
¨



−
7



q
˙



+
10
q
=
u




{\displaystyle {\textstyle 10{\ddot {q}}-7{\dot {q}}+10q=u}}

![{\displaystyle {\textstyle 10{\ddot {q}}-7{\dot {q}}+10q=u}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cdf9789ac84e4d4747fe46f29e7a19293789d1aa) 
c) 





15



q
¨



+
17



q
˙



+
11
q
=
2
u




{\displaystyle {\textstyle 15{\ddot {q}}+17{\dot {q}}+11q=2u}}

![{\displaystyle {\textstyle 15{\ddot {q}}+17{\dot {q}}+11q=2u}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/22376da4802494e1e78b5b811b2dafa40ce3c981) 
d) 





20



q
¨



−



q
˙



−
2
q
=
−
u




{\displaystyle {\textstyle 20{\ddot {q}}-{\dot {q}}-2q=-u}}

![{\displaystyle {\textstyle 20{\ddot {q}}-{\dot {q}}-2q=-u}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c7cac19e27fe1c85ac14a726fd2cb931c1a9858a) 
If 





u
=
0




{\displaystyle {\textstyle u=0}}

![{\displaystyle {\textstyle u=0}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b9fd97947cd2d67a0459307e8fa3680b8872db21) , which are stable (a - d)?
Find 





u




{\displaystyle {\textstyle u}}

![{\displaystyle {\textstyle u}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5862c118ef85972552f0f1f2c3993b65b46a2714) that makes the dynamics stable.
Write transfer functions for the cases 





u
=
0




{\displaystyle {\textstyle u=0}}

![{\displaystyle {\textstyle u=0}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b9fd97947cd2d67a0459307e8fa3680b8872db21) and 





u
=
−
100
x




{\displaystyle {\textstyle u=-100x}}

![{\displaystyle {\textstyle u=-100x}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/912419475f3d35d59dc17db8af0df6724143568b) .



1. What is the difference between exponential stability, asymptotic stability and optimality?


**Section 3**



1. Write a model of a linear system with additive Gaussian noise.
2. Derive and implement an observer.
3. Derive and implement a filter.


### The retake exam


**Section 1**


**Section 2**


**Section 3**











