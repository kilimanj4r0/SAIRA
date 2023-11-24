






MSc: Dynamics Of Non Linear Robotic Systems
===========================================






Contents
--------


* [1 Dynamics of Non Linear Robotic Systems](#Dynamics_of_Non_Linear_Robotic_Systems)
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



Dynamics of Non Linear Robotic Systems
======================================


* **Course name**: Dynamics of Non Linear Robotic Systems
* **Code discipline**: R-01
* **Subject area**:


Short Description
-----------------


This course covers the following concepts: Robotics; Robotic components; Robotic control..



Prerequisites
-------------


### Prerequisite subjects


* Matlab or Python
* numpy library
* Google Colab environment.
* CSE201 — Mathematical Analysis I
* CSE203 — Mathematical Analysis II: differentiation, exponentials, gradient.
* CSE202 — Analytical Geometry and Linear Algebra I
* CSE204 — Analytic Geometry And Linear Algebra II: matrix multiplication, change of the bases, orthonormal spaces, cross product and skew-symmetric matrices.
* Screw theory (optional).
* CSE402 — Physics I (Mechanics) and CSE410 — Physics II - Electrical Engineering: Kinematics, Statics and Dynamics.


### Prerequisite topics


Course Topics
-------------




Course Sections and Topics
| Section | Topics within the section
 |
| --- | --- |
| Introduction to robotics | 1. Introduction to Robotics, History of Robotics
2. Introduction to Drones
3. Introduction to Self driving cars
4. Programming of Industrial Robot
 |
| Kinematics | 1. Rigid body and Homogeneous transformation
2. Direct Kinematics
3. Inverse Kinematics
 |
| Differential kinematics | 1. Differential kinematics
2. Geometric calibration
3. Trajectory Planning
 |
| Dynamics | 1. Dynamics of Rigid body
2. Lagrange approach
3. Newton-Euler approach
 |


Intended Learning Outcomes (ILOs)
---------------------------------


### What is the main purpose of this course?


This course is an introduction to the field of robotics. It covers the fundamentals of kinematics, dynamics, and control of robot manipulators, robotic vision, and sensing. The course deals with forward and inverse kinematics of serial chain manipulators, the manipulator Jacobian, force relations, dynamics, and control. It presents elementary principles on proximity, tactile, and force sensing, vision sensors, camera calibration, stereo construction, and motion detection. The course concludes with current applications of robotics in active perception, medical robotics, autonomous vehicles, and other areas.



### ILOs defined at three levels


#### Level 1: What concepts should a student know/remember/explain?


By the end of the course, the students should be able to ...



* Model the kinematics of robotic systems.
* Compute end-effector position and orientation from joint angles of a robotic system.
* Compute the joint angles of a robotic system to reach the desired end-effector position and orientation.
* Compute the linear and angular velocities of the end-effector of a robotic system from the joint angle velocities.
* Convert a robot’s workspace to its configuration space and represent obstacles in the configuration space.
* Compute valid path in a configuration space with motion planning algorithms.
* Apply the generated motion path to the robotic system to generate a proper motion trajectory.
* Apply the learned knowledge to several robotic systems: including robotic manipulators, humanoid robots.


#### Level 2: What basic practical skills should a student be able to perform?


By the end of the course, the students should be able to ...



* Name various applications of robots
* Describe the current and potential economic and societal impacts of robot technology
* Use the Jacobian to transform velocities and forces from joint space to operational space
* Determine the singularities of a robot manipulator
* Formulate the dynamic equations of a robot manipulator in joint space and in Cartesian space
* List the major design parameters for robot manipulators and mobile robots
* List the typical sensing and actuation methods used in robots
* Analyze the workspace of a robot manipulator
* List the special requirements of haptic devices and medical robots
* Effectively communicate research results


#### Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?


By the end of the course, the students should be able to ...



* Describe rigid body motions using positions, orientations, frames, and mappings
* Describe orientations using Euler angles, fixed angles, and quaternions
* Develop the forward kinematic equations for an articulated manipulator
* Describe the position and orientations of a robot in terms of joint space, Cartesian space, and operational space
* Develop the Jacobian for a specific manipulator
* Determine the singularities of a robot manipulator
* Write the dynamic equations of a robot manipulator using the Lagrangian Formulation
* Analyze the workspace of a robot manipulator


Grading
-------


### Course grading range





| Grade | Range | Description of performance
 |
| --- | --- | --- |
| A. Excellent | 92-100 | -
 |
| B. Good | 80-91 | -
 |
| C. Satisfactory | 65-79 | -
 |
| D. Poor/Fail | 0-59 | -
 |


### Course activities and grading breakdown





| Activity Type | Percentage of the overall course grade
 |
| --- | --- |
| Weekly quizzes | 20
 |
| Home assignments | 20
 |
| Project | 20
 |
| Midterm Exam | 20
 |
| Final Exam | 20
 |


### Recommendations for students on how to succeed in the course


Resources, literature and reference materials
---------------------------------------------


### Open access resources


* Siciliano, Sciavicco, Villani, and Oriolo, Robotics: Modeling, Planning and Control, Springe


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
| Midterm evaluation | 1 | 1 | 1 | 1
 |
| Testing (written or computer based) | 1 | 1 | 1 | 1
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
| Question | What is the difference between the manipulator arm and manipulator wrist | 1
 |
| Question | What is Node in ROS | 1
 |
| Question | What are the disadvantages of ROS | 1
 |
| Question | Write sensors which are used in self driving cars. | 1
 |
| Question | Describe the classical approach for deign self driving car | 1
 |
| Question | Advantages and drawbacks of robotic manipulators | 0
 |
| Question | Programming industrial robots | 0
 |
| Question | Developing self driving car | 0
 |
| Question | Drones and controllers for them | 0
 |


#### Section 2





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Properties of Rotation Matrix | 1
 |
| Question | How to find Euler angles from rotation matrix | 1
 |
| Question | How to compute rotation matrix from knowing Euler angles | 1
 |
| Question | How to derive equations for direct kinematic problem | 1
 |
| Question | How to solve inverse kinematics problem | 1
 |
| Question | Structure, properties, and advantages of Homogeneous transformation | 0
 |
| Question | Expression for rotation around an arbitrary axis | 0
 |
| Question | Euler angles | 0
 |
| Question | Difference between Joint and Operational spaces | 0
 |
| Question | Direct kinematics for serial kinematic chain | 0
 |
| Question | Piper approach for inverse kinematics | 0
 |


#### Section 3





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Write the matrix of differential transformation | 1
 |
| Question | What is Jacobian matrix | 1
 |
| Question | Difference between parametric and non-parametric robot calibration. | 1
 |
| Question | Why we need complete and irreducible model | 1
 |
| Question | How trajectory planning is realised | 1
 |
| Question | What is trajectory junction | 1
 |
| Question | Jacobian matrix calculation | 0
 |
| Question | Jacobian matrices for typical serial manipulators | 0
 |
| Question | Robot calibration procedure | 0
 |
| Question | complete, irreducible geometric model | 0
 |
| Question | robot control strategies with offline errors compensation | 0
 |
| Question | Trajectory planning in joint and Cartesian spaces | 0
 |
| Question | Trajectory junction | 0
 |


#### Section 4





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Energy of rigid body | 1
 |
| Question | Dynamics of rigid body | 1
 |
| Question | What is Direct and Inverse Dynamics | 1
 |
| Question | Difference between Newton Euler and Lagrange Euler approaches | 1
 |
| Question | Dynamics of rigid body | 0
 |
| Question | Direct and Inverse Dynamic | 0
 |
| Question | Newton-Euler Approach | 0
 |
| Question | Lagrange-Euler Approach | 0
 |


### Final assessment


**Section 1**



1. Typical commands for programming industrial manipulator motions
2. Types of robots and their application ares
3. Control of self driving car


**Section 2**



1. Transformation between reference frames
2. Find Euler angles for given orientation matrix and transformation order
3. Transformation between Cartesian and operational spaces
4. Direct kinematic for SCARA robot
5. Inverse kinematic for SCARA robot


**Section 3**



1. Write Jacobian for Polarrobot
2. Advantages and disadvantages parametric and non-parametric robot calibration.
3. complete, irreducible geometric model for spherical manipulator
4. Compute the joint trajectory q(t) from q(0) = 1 to q(2) = 4 with null initial and final velocities and accelerations. (polynomial)
5. Obtain manipulator trajectory for given manipulator kinematics, initial and final states and velocity and acceleration limits/


**Section 4**



1. Solve inverse dynamics problem for Cartesian robot
2. Solve direct dynamics problem for RRR spherical manipulator
3. Moving frame approach for dynamics modelling


### The retake exam


**Section 1**


**Section 2**


**Section 3**


**Section 4**











