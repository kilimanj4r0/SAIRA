






MSc: Computational Intelligence
===============================



(Redirected from [MSc:Computational Intelligence](/index.php?title=MSc:Computational_Intelligence&redirect=no "MSc:Computational Intelligence"))


Contents
--------


* [1 Computational intelligence](#Computational_intelligence)
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



Computational intelligence
==========================


* **Course name**: Computational intelligence
* **Code discipline**: R-02
* **Subject area**: Computer Science and Engineering


Short Description
-----------------


This course covers the following concepts: Convex Optimization; Global Optimization; Machine Learning and function approximation.



Prerequisites
-------------


### Prerequisite subjects


* CSE202 — Analytical Geometry and Linear Algebra I
* CSE204 — Analytic Geometry And Linear Algebra II: SVD, least squares, pseudoinverse, semidefinite matrices, solving systems of linear eq., dot product, norms. Basic Geometry (ellipsoids, planes, normal, tangent).
* Basic multivariable Calculus (extremum and minimum of a function, derivatives, Jacobians)
* Programming (Python/Matlab)


### Prerequisite topics


Course Topics
-------------




Course Sections and Topics
| Section | Topics within the section
 |
| --- | --- |
| Introduction to optimization methods | 1. Optimization problem types.
2. Constraint types.
3. Cost function (Reward function) types.
4. Practical examples of optimization problems.
5. Basic optimization algorithms and their limitations.
6. Lagrange multipliers.
7. Gradient descent.
 |
| Convex Optimization. | 1. Convex sets.
2. Convex functions.
3. Convex optimization problems.
4. Properties of the convex optimizations.
5. Linear Programming
6. Quadratic Programming.
7. Second Order Cone Programming.
8. Semidefinite Programming.
9. Vertical Stability of a bipedal robot as an optimization.
10. Quadrotor path planning as an optimization.
11. Controller design as an optimization.
12. CVX.
 |
| Global Optimization | 1. Properties of non-convex problems.
2. Problems with multiple solutions.
3. Problems with weak local minima.
4. Problems with computationally expensive gradients.
5. Path planning on non-convex maps.
6. Controller design as a non-convex problem.
7. Relaxations.
8. Mixed integer programming.
9. PSO.
10. RRT.
11. Genetic Algorithm.
12. Machine Learning.
 |


Intended Learning Outcomes (ILOs)
---------------------------------


### What is the main purpose of this course?


Computational Intelligence serves as a combined multidisciplinary subject, encompassing a wide range of topics. These include numeric optimization, especially convex optimization, which is the necessary and required topic for most of the modern engineering and scientific work. The course also covers global non-convex optimization methods, which are important instruments in a number of areas: product design and manufacturing, control, and others. Basic information from a number of other areas, such as machine learning, are added to complete the picture of modern intelligent computational tools that serve the same set of goals.



### ILOs defined at three levels


#### Level 1: What concepts should a student know/remember/explain?


By the end of the course, the students should be able to ...



* Convexity, Convex Sets, Convex optimization
* Quadratic programming, Second Order Cone Programming, Semidefinite Programming
* Optimization in Controller design, Optimization in path planning, Optimization in Mechanical Engineering
* Nonlinear non-convex optimization, RRT algorithm, Genetic Algorithm, Particle Swarm Optimization, Function approximation.


#### Level 2: What basic practical skills should a student be able to perform?


By the end of the course, the students should be able to ...



* Structure of optimization problems
* Convexity criteria
* Properties of convex optimization
* Types of problems that cab be transformed into Linear Programs
* Types of problems that cab be transformed into Quadratic Programs
* Types of problems that cab be transformed into Second Order Cone Programs
* Types of problems that cab be transformed into Semidefinite Programs
* Types of non-convex problems that can be approximated by a convex relaxation
* Mixed-integer Optimization
* Path planning as an optimization
* Controller design as an optimization
* Optimal parameter choice
* RRT implementation
* PSO implementation


#### Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?


By the end of the course, the students should be able to ...



* Design Control using Convex Optimization.
* Implement iterative non-linear controllers with inequality constraints.
* Find optimal parameter choice for processes
* proof convexity of a problem
* program optimization in CVX
* make RRT-based algorithms, understand their limitations
* make PSO-based algorithms, understand their limitations
* make GA-based algorithms, understand their limitations


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


* Engelbrecht, A.P., 2007. Computational intelligence: an introduction. John Wiley & Sons.
* Pedrycz, W., 1997. Computational intelligence: an introduction. CRC press.
* Konar, A., 2006. Computational intelligence: principles, techniques and applications. Springer Science & Business Media.


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
| Question | Describe an engineering problem as an optimization problem. | 1
 |
| Question | What is the domain of an optimization problem? | 1
 |
| Question | What is the difference between Convex and Non-convex optimization? | 1
 |
| Question | Formulate a linear system with multi-dimensional solution space and inequality constraints. | 0
 |
| Question | Solve a linear system with inequality constraints via gradient descent. | 0
 |


#### Section 2





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Provide examples of convex problems. | 1
 |
| Question | What is a convex domain? | 1
 |
| Question | Examples of problems with a convex cost but non-convex domain? | 1
 |
| Question | What is the difference between quadratic and conic programming? | 1
 |
| Question | What is the hierarchy of convex optimization problems? | 1
 |
| Question | What solvers can solve quadratic programs? | 1
 |
| Question | What solvers can solve SOCP? | 1
 |
| Question | What solvers can solve LP? | 1
 |
| Question | What solvers can solve SDP? | 1
 |
| Question | What kinds of inequality constraints make the problem non-convex? | 0
 |
| Question | What kinds of inequality constraints make the problem non-feasible? | 0
 |
| Question | Show an example of a problem where the cost is a 2-norm. Show that it is a SOCP. | 0
 |
| Question | Show an example of a problem where the cost is a 2-norm. Prove that it can be equivalently solved as a QP. | 0
 |
| Question | Solve trajectory planning for a quadrotor as a SOCP. | 0
 |
| Question | Solve vertical stability check for a biped as a QP. | 0
 |
| Question | implement ZMP trajectory planning as a QP. | 0
 |
| Question | implement LTI controller design as a SDP. | 0
 |


#### Section 3





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Provide examples of non-convex problems? | 1
 |
| Question | Why non-convex problems can have multiple solutions? | 1
 |
| Question | What are local minima? | 1
 |
| Question | What is global optimization? | 1
 |
| Question | Provide an example of a non-convex path planning problems? | 1
 |
| Question | What are the limitations of PSO? | 1
 |
| Question | Implement PSO for a parameter optimization problem. | 0
 |
| Question | Make a comparative study of PSO, GA and Random Search. | 0
 |
| Question | What is the difference between random search, Sobol sequences-based methods and PSO? Show it in the numerical examples. | 0
 |
| Question | Implement RRT | 0
 |
| Question | Implement GA | 0
 |


### Final assessment


**Section 1**


**Section 2**


**Section 3**



1. Solve minimum distance to a plane problem, when the domain is non-convex.
2. Find optimal controller parameters for a given trajectory of a non-linear system.
3. Which non-linear algorithms can solve problems with non-convex domains?


### The retake exam


**Section 1**


**Section 2**


**Section 3**











