






MSc: Optimization
=================






Contents
--------


* [1 Optimization](#Optimization)
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
		- [2.2.2 Final assessment](#Final_assessment)
		- [2.2.3 The retake exam](#The_retake_exam)



Optimization
============


* **Course name**: Optimization
* **Code discipline**: R-01
* **Subject area**:


Short Description
-----------------


This course covers the following concepts: Optimization of a cost function; Algorithms to find solution of linear and nonlinear optimization problems.



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
| Linear programming | 1. simplex method to solve real linear programs
2. cutting-plane and branch-and-bound methods to solve integer linear programs.
 |
| Nonlinear programming | 1. methods for unconstrained optimization
2. linear and nonlinear least-squares problems
3. methods for constrained optimization
 |


Intended Learning Outcomes (ILOs)
---------------------------------


### What is the main purpose of this course?


The main purpose of this course to make the student aware of basic notions of mathematical programming and of its importance in the area of engineering.



### ILOs defined at three levels


#### Level 1: What concepts should a student know/remember/explain?


By the end of the course, the students should be able to ...



* explain the goal of an optimization problem
* remind the importance of converge analysis for optimization algorithms
* draft solution codes in Python/Matlab.


#### Level 2: What basic practical skills should a student be able to perform?


By the end of the course, the students should be able to ...



* formulate a simple optimization problem
* select the appropriate solution algorithm
* find the solution.


#### Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?


By the end of the course, the students should be able to ...



* the simplex method
* algorithms to solve nonlinear optimization problems.


Grading
-------


### Course grading range





| Grade | Range | Description of performance
 |
| --- | --- | --- |
| A. Excellent | 86-100 | -
 |
| B. Good | 71-85 | -
 |
| C. Satisfactory | 56-70 | -
 |
| D. Poor | 0-55 | -
 |


### Course activities and grading breakdown





| Activity Type | Percentage of the overall course grade
 |
| --- | --- |
| Labs/seminar classes (weekly evaluations) | 0
 |
| Interim performance assessment (class participation) | 100/0
 |
| Exams | 0/100
 |


### Recommendations for students on how to succeed in the course


Resources, literature and reference materials
---------------------------------------------


### Open access resources


* Textbook: C.H. Papadimitriou, K. Steiglitz, Combinatorial Optimization, Dover, New York, 1982.
* Textbook: D. Bertsekas, Nonlinear Programming, Athena Scientific, 1999.


### Closed access resources


### Software and tools used within the course


Teaching Methodology: Methods, techniques, & activities
=======================================================


Activities and Teaching Methods
-------------------------------




Activities within each section
| Learning Activities | Section 1 | Section 2
 |
| --- | --- | --- |
| Midterm evaluation | 1 | 1
 |
| Testing (written or computer based) | 1 | 1
 |


Formative Assessment and Course Activities
------------------------------------------


### Ongoing performance assessment


#### Section 1





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | How a convex set and a convex function are defined? | 1
 |
| Question | What is the difference between polyhedron and polytope? | 1
 |
| Question | Why does always a linear program include constraints? | 1
 |
| Question | Consider the problem:






minimize 


c

1



x

1


+

c

2



x

2


+

c

3



x

3


+

c

4



x

4






{\displaystyle {\displaystyle {\text{minimize }}c\_{1}x\_{1}+c\_{2}x\_{2}+c\_{3}x\_{3}+c\_{4}x\_{4}}}

{\displaystyle {\displaystyle {\text{minimize }}c_{1}x_{1}+c_{2}x_{2}+c_{3}x_{3}+c_{4}x_{4}}} 






subject to 


x

1


+

x

2


+

x

3


+

x

4


=
2




{\displaystyle {\displaystyle {\text{subject to }}x\_{1}+x\_{2}+x\_{3}+x\_{4}=2}}

{\displaystyle {\displaystyle {\text{subject to }}x_{1}+x_{2}+x_{3}+x_{4}=2}} 





2

x

1


+
3

x

3


+
4

x

4


=
2




{\displaystyle {\displaystyle 2x\_{1}+3x\_{3}+4x\_{4}=2}}

{\displaystyle {\displaystyle 2x_{1}+3x_{3}+4x_{4}=2}} 






x

1


,

x

2


,

x

3


,

x

4


⩾
0




{\displaystyle {\displaystyle x\_{1},x\_{2},x\_{3},x\_{4}\geqslant 0}}

{\displaystyle {\displaystyle x_{1},x_{2},x_{3},x_{4}\geqslant 0}} Solve it using simplex method. | 0
 |
| Question | Consider the problem:






minimize 


x

1


+

x

2






{\displaystyle {\displaystyle {\text{minimize }}x\_{1}+x\_{2}}}

{\displaystyle {\displaystyle {\text{minimize }}x_{1}+x_{2}}} 






subject to 

−
5

x

1


+
4

x

2


≤
0




{\displaystyle {\displaystyle {\text{subject to }}-5x\_{1}+4x\_{2}\leq 0}}

{\displaystyle {\displaystyle {\text{subject to }}-5x_{1}+4x_{2}\leq 0}} 





6

x

1


+
2

x

2


 
≤
17




{\displaystyle {\displaystyle 6x\_{1}+2x\_{2}\ \leq 17}}

{\displaystyle {\displaystyle 6x_{1}+2x_{2}\ \leq 17}} 






x

1


,
 

x

2


≥
0




{\displaystyle {\displaystyle x\_{1},\ x\_{2}\geq 0}}

{\displaystyle {\displaystyle x_{1},\ x_{2}\geq 0}} Solve it using cutting-plane and branch-and-bound methods. | 0
 |


#### Section 2





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Which are the necessary and sufficient conditions of optimality of a generic minimization/maximization problem? | 1
 |
| Question | What is the goal of a descent algorithm? | 1
 |
| Question | What does it mean to fit some experimental data points | 1
 |
| Question | Consider the problem:






minimize 



1
2



(


x

1


1


+

x

2


2



)





{\displaystyle {\displaystyle {\text{minimize }}{\frac {1}{2}}\left(x\_{1}^{1}+x\_{2}^{2}\right)}}

{\displaystyle {\displaystyle {\text{minimize }}{\frac {1}{2}}\left(x_{1}^{1}+x_{2}^{2}\right)}} Solve it using the suitable method. | 0
 |
| Question | Consider the problem:






minimize 

−


(


x

1


−
2

)


2






{\displaystyle {\displaystyle {\text{minimize }}-\left(x\_{1}-2\right)^{2}}}

{\displaystyle {\displaystyle {\text{minimize }}-\left(x_{1}-2\right)^{2}}} 






subject to 

 

x

1


+

x

2


2


=
1




{\displaystyle {\displaystyle {\text{subject to }}\ x\_{1}+x\_{2}^{2}=1}}

{\displaystyle {\displaystyle {\text{subject to }}\ x_{1}+x_{2}^{2}=1}} 





−
1
≤

x

2


≤
1




{\displaystyle {\displaystyle -1\leq x\_{2}\leq 1}}

{\displaystyle {\displaystyle -1\leq x_{2}\leq 1}} Solve it using the suitable method. | 0
 |


### Final assessment


**Section 1**



1. Why does the simplex method require to be initialized with a correct basic feasible solution?
2. How one can test absence of solutions to a linear program?
3. How one can test unbounded solutions to a linear program?
4. How can the computational complexity of an optimization algorithm can be defined?


**Section 2**



1. How is it possible to compute the Lagrange multiplier of a constrained optimization problem?
2. Which are the convergence conditions of the steepest descent method?
3. Which are the convergence conditions of the Newton’s method?
4. How can one “penalize” a constraint?


### The retake exam


**Section 1**



1. Consider the problem:









minimize 


x

1


+

x

2






{\displaystyle {\displaystyle {\text{minimize }}x\_{1}+x\_{2}}}

![{\displaystyle {\displaystyle {\text{minimize }}x_{1}+x_{2}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/808d163d417155f5101d686f93115eae926bb8d7)







subject to 


x

1


+


2
x


2


+
2

x

3


≤
20




{\displaystyle {\displaystyle {\text{subject to }}x\_{1}+{2x}\_{2}+2x\_{3}\leq 20}}

![{\displaystyle {\displaystyle {\text{subject to }}x_{1}+{2x}_{2}+2x_{3}\leq 20}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c1077ebbebbf250ab80e25efd8ddc3c18c25d51a)






2

x

1


+

x

2


+
2

x

3


≤
20




{\displaystyle {\displaystyle 2x\_{1}+x\_{2}+2x\_{3}\leq 20}}

![{\displaystyle {\displaystyle 2x_{1}+x_{2}+2x_{3}\leq 20}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6b5b024408fcf315b7492cfa91381dc161bf368d)






2

x

1


+
2

x

2


+

x

3


≤
20




{\displaystyle {\displaystyle 2x\_{1}+2x\_{2}+x\_{3}\leq 20}}

![{\displaystyle {\displaystyle 2x_{1}+2x_{2}+x_{3}\leq 20}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5b2d32111e06f92af781a1e1b84925790e89d197)







x

1


,
 

x

2


,
 

x

3


≥
0




{\displaystyle {\displaystyle x\_{1},\ x\_{2},\ x\_{3}\geq 0}}

![{\displaystyle {\displaystyle x_{1},\ x_{2},\ x_{3}\geq 0}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9ed113ae3c350b50541bc8e10952e62acefa3d29) 
Solve it using simplex method.



1. Consider the problem:









maximize 

15

x

1


+


12
x


2


+
4

x

3


+
2

x

4






{\displaystyle {\displaystyle {\text{maximize }}15x\_{1}+{12x}\_{2}+4x\_{3}+2x\_{4}}}

![{\displaystyle {\displaystyle {\text{maximize }}15x_{1}+{12x}_{2}+4x_{3}+2x_{4}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/646d0a204c7a9ee65166e9a6a8779ec824e1b5b7)







subject to 

8

x

1


+
5

x

2


+
3

x

3


+
2

x

4


≤
10




{\displaystyle {\displaystyle {\text{subject to }}8x\_{1}+5x\_{2}+3x\_{3}+2x\_{4}\leq 10}}

![{\displaystyle {\displaystyle {\text{subject to }}8x_{1}+5x_{2}+3x_{3}+2x_{4}\leq 10}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6a191a3c077f363dd639ccf3f86adfa2815f9999)







x

i


∈
{
0
,
1
}




{\displaystyle {\displaystyle x\_{i}\in \{0,1\}}}

![{\displaystyle {\displaystyle x_{i}\in \{0,1\}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3bbf6cea8924f9c27b93c501fb163ac39c3fbeeb) 
Solve it using cutting-plane and branch-and-bound methods.


**Section 2**



1. Consider the problem:









minimize 

100


(


x

2


−

x

1


2



)


2


+


(

1
−

x

1



)


2






{\displaystyle {\displaystyle {\text{minimize }}100\left(x\_{2}-x\_{1}^{2}\right)^{2}+\left(1-x\_{1}\right)^{2}}}

![{\displaystyle {\displaystyle {\text{minimize }}100\left(x_{2}-x_{1}^{2}\right)^{2}+\left(1-x_{1}\right)^{2}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6f5022eea1bf6022a2b29e423cf08560c2d8217d)







subject to 


x

1


,
 

x

2


≥
0




{\displaystyle {\displaystyle {\text{subject to }}x\_{1},\ x\_{2}\geq 0}}

![{\displaystyle {\displaystyle {\text{subject to }}x_{1},\ x_{2}\geq 0}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/811f87fefb0b94139ff416f9363292e619e71bcb) 
Solve it using the suitable method.











