






BSTE: The Security and Interpretability of Machine Learning
===========================================================






Contents
--------


* [1 The Security and Interpretability of Machine Learning](#The_Security_and_Interpretability_of_Machine_Learning)
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



The Security and Interpretability of Machine Learning
=====================================================


* **Course name**: The Security and Interpretability of Machine Learning
* **Code discipline**: CSE324
* **Subject area**: Data Science and AI


Short Description
-----------------


This course gives a general overview of the robustness of Machine Learning (ML) in general with main focus on neural networks. Despite the fact that ML achieved remarkable performance when applied in different domains, ML systems have shown a susceptibility to adversarial attacks in the form of small purposely created perturbations leading to misclassication. In this course, students will learn about adversarial attacks, defenses to increase the robustness of the model, and how this might be related to the interpretability of model.
The main goal of this course is to practice creating attacks against white-box and black-box models, and how to consider this issue when training the model. Working individually and in teams, students will create deep neural networks models for different domains, create attacks on them, and investigate how to increase the robustness of these models.



Prerequisites
-------------


### Prerequisite subjects


* CSE302
* CSE206


### Prerequisite topics


* Probability and Statistics.
* Machine learning.


Course Topics
-------------




Course Sections and Topics
| Section | Topics within the section
 |
| --- | --- |
| Recap, deep neural networks, and statistical learning | 1. Recap of learning from the data theory.
2. Deep neural networks.
3. Definition of adversarial attacks.
 |
| Adversarial attacks and their implementation | 1. Open-box adversarial attacks.
2. Black-box adversarial attacks.
3. Different L\_p norms attacks.
 |
| Defenses against adversarial attacks and their implementation | 1. Different defenses against previous attacks
2. Robustness certification
 |
| Interpretability and the relation with robustness | 1. Interpretability definition
2. The relation between interpretability and robustness
 |


Intended Learning Outcomes (ILOs)
---------------------------------


### What is the main purpose of this course?


What is the main goal of this course formulated in one sentence?
The main goal of this course is to introduce students to new issues might appear when applying ML models in real-life making these models unreliable, and how to consider these issue when training the model.



### ILOs defined at three levels


#### Level 1: What concepts should a student know/remember/explain?


By the end of the course, the students should be able to ...



* Understand how adversarial attacks could decrease the performance of deep neural networks models.
* Consider the robustness of neural networks models when designing real life solutions.
* Differentiate between robust and non-robust models.
* Differentiate between interpretable and non-interpretable models.
* Design explainable models.


#### Level 2: What basic practical skills should a student be able to perform?


By the end of the course, the students should be able to ...



* Define different adversarial attacks
* Implement attacks on different neural networks systems
* Increase the robustness of neural networks by using different defenses.
* Define interpretable models.
* Implement explainable models.


#### Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?


By the end of the course, the students should be able to ...



* Apply different adversarial attacks on different models
* Evaluate the performance and robustness of these systems under adversarial attacks
* Apply different defenses on different systems.
* Visualize the feature space to examine the relation between robustness and interpretability.


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
| D. Fail | 0-59 | -
 |


### Course activities and grading breakdown





| Activity Type | Percentage of the overall course grade
 |
| --- | --- |
| Assignment | 60
 |
| Quizzes | 10
 |
| midterm exam | 20
 |
| Demo day | 10
 |


### Recommendations for students on how to succeed in the course


Having basic knowledge in machine learning is essential for this course.  
Review lecture materials before classes to do well in quizzes.  
Reading the recommended literature is optional, but will give you a deeper understanding of the material.



Resources, literature and reference materials
---------------------------------------------


### Open access resources


* Adversarial Robustness - Theory and Practice
* <https://adversarial-ml-tutorial.org/introduction/>
* Recommended papers:
* <https://nicholas.carlini.com/papers>


### Closed access resources


### Software and tools used within the course


* Provide at least 3 open/freemium access tools
* Python , <https://www.python.org/download/releases/3.0//>
* Jupyter notebook, <https://jupyter.org/>
* Pytorch, <https://pytorch.org/>


Teaching Methodology: Methods, techniques, & activities
=======================================================


Activities and Teaching Methods
-------------------------------




Teaching and Learning Methods within each section
| Teaching Techniques | Section 1 | Section 2 | Section 3 | Section 4
 |
| --- | --- | --- | --- | --- |
| Problem-based learning (students learn by solving open-ended problems without a strictly-defined solution) | 1 | 1 | 1 | 1
 |
| Project-based learning (students work on a project) | 1 | 1 | 1 | 1
 |
| Differentiated learning (provide tasks and activities at several levels of difficulty to fit students needs and level) | 1 | 1 | 1 | 1
 |
| Contextual learning (activities and tasks are connected to the real world to make it easier for students to relate to them); | 1 | 1 | 1 | 1
 |
| развивающего обучения (задания и материал "прокачивают" ещё нераскрытые возможности студентов); | 1 | 1 | 1 | 1
 |
| концентрированного обучения (занятия по одной большой теме логически объединяются); | 1 | 1 | 1 | 1
 |
| inquiry-based learning | 1 | 1 | 1 | 1
 |
| Task-based learning | 1 | 1 | 1 | 1
 |




Activities within each section
| Learning Activities | Section 1 | Section 2 | Section 3 | Section 4
 |
| --- | --- | --- | --- | --- |
| Lectures | 1 | 1 | 1 | 1
 |
| Interactive Lectures | 1 | 1 | 1 | 1
 |
| Lab exercises | 1 | 1 | 1 | 1
 |
| Experiments | 1 | 1 | 1 | 0
 |
| Development of individual parts of software product code | 1 | 1 | 1 | 1
 |
| Individual Projects | 1 | 1 | 1 | 0
 |
| Quizzes (written or computer based) | 1 | 1 | 1 | 1
 |
| Discussions | 1 | 1 | 1 | 1
 |
| Written reports | 1 | 1 | 1 | 1
 |


Formative Assessment and Course Activities
------------------------------------------


### Ongoing performance assessment


#### Section 1





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Quiz | 1. What are adversarial attacks?2. What is the difference between black-box and white-box attacks?3. the objective function of adversarial attacks | 1
 |
| Individual Assignments | In this assignment, students should build the model that will be used during this course for the upcoming homeworks and final project. The students are encouraged to choose building a model for a task that they find interesting.For those who do not decide a task, they are asked to build, train, and evaluate one of the models that will be provided. | 1
 |


#### Section 2





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Quiz | 1. Write the formula for different attacks2. Define the difference between recursive and non-recursive attacks. | 1
 |
| Individual Assignments | In this assignment, students should attack and defend the model they built in the first homework. Students should write the code for the three known adversarial attacks : FGSM, PGD, CW. Then, test these attacks on the model.Then, write the code for adversarial training and show how to use it to defend the model. | 1
 |
| Midterm | Theoretical questions on adversarial attacks and their formulas. | 1
 |


#### Section 3





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Quiz | 1. Define the formula for adversarial training.2. Define certified robustness methods | 1
 |
| Individual Assignment | In this assignment, students should attack and defend the model with adapted attacks. Implement one of the following defenses and attacks:1. Adversarial Retraining (Adversarial samples detection)2. Kernel Density Estimation3. Dropout Randomization | 1
 |


#### Section 4





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Quiz | 1. Define interpretability concepts.2. Define interpretability methods | 1
 |


### Final assessment


**Section 1**



1. Grading criteria for the final project presentation:
2. One slide about the problem statement and why it’s important to consider it.
3. A comprehensive description of each student’s specific task and how it was solved.
4. The chosen model’s architecture.
5. Estimating the mode’s performance.


**Section 2**



1. Explaining the used adversarial attacks.
2. The model’s performance after applying the attacks.


**Section 3**


**Section 4**


  




### The retake exam


**Section 1**



1. The retake is project-based as well. Students need to apply what they learned through the course on a pacific model. The grading criteria for each section are the same as for the final project presentation. There has to be a meeting before the retake itself to plan and agree on the project ideas, and to answer questions.
2. P7. Activities and Teaching Methods by Sections
3. Mark what techniques and methods are used in each section (1 is used, 0 is not used).
4. Table A1: Teaching and Learning Methods within each section
5. Table A2: Activities within each section


**Section 2**


**Section 3**


**Section 4**











