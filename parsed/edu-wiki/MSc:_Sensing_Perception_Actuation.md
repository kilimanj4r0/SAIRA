






MSc: Sensing Perception Actuation
=================================






Contents
--------


* [1 Sensing, Perception & Actuation](#Sensing.2C_Perception_.26_Actuation)
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



Sensing, Perception & Actuation
===============================


* **Course name**: Sensing, Perception & Actuation
* **Code discipline**: R-01
* **Subject area**: Visual Sensors, Data Analysis, Error Analysis, Theory of Measurements, Machine Vision, Inertial Sensors, Internal Sensors, Filtering, Sensor Fusion, Image Processing, Point Cloud Processing


Short Description
-----------------


This course covers the following concepts: Physical principles of sensors and their limitations; Measurements, Sensor Calibration, Data and Error analysis; Development of algorithms for image processing, feature extraction and object recognition; 3D Point cloud processing and scene reconstruction; Linear Kalman Filter and Sensor Fusion.



Prerequisites
-------------


### Prerequisite subjects


* CSE402 — Physics I (Mechanics)
* CSE410 — Physics II - Electrical Engineering
* CSE201 — Mathematical Analysis I
* CSE203 — Mathematical Analysis II
* CSE202 — Analytical Geometry and Linear Algebra I
* CSE204 — Analytic Geometry And Linear Algebra II
* CSE206 — Probability And Statistics


### Prerequisite topics


Course Topics
-------------




Course Sections and Topics
| Section | Topics within the section
 |
| --- | --- |
| Intro to Sensors. Data and Error Analysis | 1. Sensors’ classification and Applications
2. Sensors Characteristics: Dynamic range, Accuracy, Signal & Noise ratio
3. Error analysis: Systematic vs Statistical Errors, Accuracy and Precision, Central Limit Theorem, 3 sigma rule, outliers
4. Sensor calibration. Direct and indirect measurements
5. Introduction to Data Analysis: Linear Regression, Least-Squares Fitting, Curve fitting, and Smoothing
 |
| Perception | 1. Image sensors: camera matrix, characteristics. Color filters.
2. Pinhole camera model, lenses and distortions
3. Camera calibration, Intrinsic and Extrinsic matrices
4. Video camera: CCTV, IR & thermal imaging camera, Fish eye camera
5. Stereo vision: Stereosystem, Stereogeometry
6. Image rectification, Disparity map, 3D Point Cloud from Stereo
7. Point clouds processing, 3D reconstruction, Structure-from-Motion (SfM)
8. LIDAR: Laser rangefinders. Laser-camera systems. Airborne LIDAR
9. Depth, TOF, RGBD camera, MS Kinect: characteristics and calibration
10. SONAR. Piezocrystalls. Doppler effect. Doppler radar.
11. Acoustic sensor systems. Sound spectrogram
12. mm-RADAR, Long-Range RADAR, Short-range RADAR
 |
| Sensor Fusion and Filtering | 1. Filtering
2. Linear Kalman Filter (KF)
3. Sensor Fusion
4. Linear Kalman Filter vs Extended KF
5. MoCap system
6. Multicamera system
 |
| Actuators and Passive Sensors: GPS, IMU and Inertial Sensors | 1. GPS, differential GPS (dGPS)
2. Inertial sensors: IMU, accelerometers, gyroscopes
3. Magnetometers
4. Internal sensors: position, velocity, torque & force sensors, encoders
5. MEMS for robot applications
6. Actuators
7. Smart and Intelligent Sensors
 |


Intended Learning Outcomes (ILOs)
---------------------------------


### What is the main purpose of this course?


One of the most important tasks of an autonomous system of any kind is to acquire knowledge about its environment. This is done by taking measurements using various sensors and then extracting meaningful information from those measurements. In this course we present the most common sensors used in mobile robots and autonomous systems and then discuss strategies for extracting information from the sensors.



### ILOs defined at three levels


#### Level 1: What concepts should a student know/remember/explain?


By the end of the course, the students should be able to ...



* familiar with physical and sensing principles for Camera, Stereo vision, LIDAR, SONAR, Time-of-Flight camera, GPS, actuators, inertial and internal sensors
* acquainted with measurements and error analysis, data analysis, and sensor calibration
* familiar with triangulation principle, basics of image and point cloud processing methods


#### Level 2: What basic practical skills should a student be able to perform?


By the end of the course, the students should be able to ...



* Understand how to remove systematic error and how to decrease statistical error
* Recover depth information from stereo vision, structure-from-light and TOF cameras
* Explain how Linear Regression and Least-Squares Fitting allow to minimize measurement errors


#### Level 3: What complex comprehensive skills should a student be able to apply in real-life scenarios?


By the end of the course, the students should be able to ...



* Calibrate sensors to remove systematic errors
* Extract meaningful information from sensor’s data (features, objects, depth and accuracy information)
* Detect objects from 2D images
* Recover scene from 3D Point Cloud
* Filter noisy data
* Match models to datasets
* Fuse sensor’s data and apply Kalman Filtering
* Apply GPS, camera, LIDAR, RADAR, SONAR, IMU, Stereo camera for a mobile robot localization


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
| Labs/seminar classes | 10
 |
| Home assignments | 40
 |
| Interim performance assessment | 15
 |
| Quizzes | 20
 |
| Exams | 15
 |


### Recommendations for students on how to succeed in the course


Resources, literature and reference materials
---------------------------------------------


### Open access resources


* Roland Siegwart, Illah R. Nourbakhsh, and Davide Scaramuzza. Introduction to Autonomous Mobile Robots, MIT press, 2011.
* M. Chli, D. Scaramuzza, R. Siegwart, et al. Autonomous Mobile Robots, ETH Zurich, 2017, <http://www.asl.ethz.ch/education/lectures/autonomous_mobile_robots.html>
* Jacob Fraden. Handbook of modern sensors: physics, designs, and applications. Springer, 2010
* Alonzo Kelly. Mobile Robotics: Mathematics, Models, and Methods. Cambridge University Press, 2013
* Horn, Berthold K. P. Robot Vision. Cambridge, MA: MIT Press /McGraw-Hill, March 1986
* H. Choset, K. M. Lynch, et. al. “Principles of Robot Motion: Theory, Algorithms, and Implementations”, MIT press, 2005
* Gregory Dudek and Michael Jenkin. Computational Principles of Mobile Robotics, 2nd ed., Cambridge University Press, 2010


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
| Homework assignments | 1 | 0 | 0 | 0
 |
| Midterm evaluation | 1 | 1 | 1 | 1
 |
| Testing (written or computer based) | 1 | 1 | 1 | 1
 |
| Discussions | 1 | 1 | 1 | 1
 |
| Homework and group projects | 0 | 1 | 1 | 1
 |


Formative Assessment and Course Activities
------------------------------------------


### Ongoing performance assessment


#### Section 1





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | UAV flies through the strong wind and begins to oscillate. The pitch angle change was measured with the gyro during a few seconds. Exclude from the consideration rare random deviation (outliers) and estimate the true value of the roll angle. Calculate the confidence interval of error for 99.9% confidence level. Consider that the gyro errors are normally distributed, except for the rare random deviations. Proper regression technique should be applied so as to fit the data while excluding rare random deviations. | 1
 |
| Question | UAV flies through the strong wind and begins to oscillate. The roll angle change was measured with the gyro during a few seconds. Exclude from the consideration rare random deviation (outliers) and estimate the true value of the roll angle. Calculate the confidence interval of error for 95% confidence level. Consider that the gyro errors are normally distributed, except for the rare random deviations. Proper regression technique should be applied so as to fit the data while excluding rare random deviations. | 1
 |
| Question | The human CoM (center of mass) during the walking has been measured with Kinect sensors. Estimate the true value of the x-component of acceleration. For example, you can use a moving average filter. Calculate the confidence interval of error for 95% confidence level. Consider that the errors are normally distributed, except for the rare random deviations. Proper regression technique should be applied so as to fit the data while excluding rare random deviations. | 1
 |
| Question | UAV performs loop-the-loop. The pitch angle change was measured with the gyro during 1 seconds. Exclude from the consideration rare random deviation (outliers) and estimate the true value of the roll angle. Calculate the confidence interval of error for 95% confidence level. Consider that the gyro errors are normally distributed, except for the rare random deviations. Proper regression technique should be applied so as to fit the data while excluding rare random deviations. | 1
 |
| Question | You are given a dataset (select the dataset with corresponds to your ID), includes some data points in R








3






{\displaystyle {\textstyle ^{3}}}

{\displaystyle {\textstyle ^{3}}} . Your task is to estimate whether it represents a plane, line or something else. You must use the RANSAC for this task. Explain the way you selected your minimal sample set, number of iteration and the threshold level? It would be better to provide an analytical solution derivation as well as graphical interpretation. | 1
 |
| Question | Inside the right hand of the AR-601 robot there is an accelerometer. Engineers fixed the robot on the crane and went for a lunch. Robot was swinging by inertia for a few minutes. Engineers came back after lunch and read the data from accelerometer. Help them to understand what they measured. Exclude from the consideration rare random deviation (outliers) and estimate the true value of the y-component of acceleration. Calculate the confidence interval of error for 99.9% confidence level. Consider that the accelerometer errors are normally distributed, except the rare random deviations. Proper regression technique should be applied so as to fit the data while excluding rare random deviations. | 1
 |
| Question | Introduction to Confidence Interval (CI) | 0
 |
| Question | Introduction to Linear Regression | 0
 |
| Question | Introduction to Logistic Regression | 0
 |
| Question | Introduction to RANSAC | 0
 |
| Question | Introduction to Maximum Likelihood Estimation (MLE) | 0
 |


#### Section 2





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Place a 3d object such as a cube or a cylinder or something you like in an appropriate way with respect to Kinect. Then you are going to use Kinect 2 in order to get the depth map. Associate depth map with RGB information in order to isolate the object, which is to be extracted from the ground plane and other background. You may have to use RANSAC or some other algorithms to extract the object and find the center point of the object in the 3D space. It may be relative to Kinect or any known position in the world. | 1
 |
| Question | Calibrate a camera (your phone or computer camera should be utilized) using the chessboard pattern. It’s logically to switch off the auto focus mode of the camera, if it is enabled. The number of images should be at least 30 (with different chessboard positions). Obtain the intrinsic and extrinsic parameters. Once you have calibrated your camera, store intrinsic and extrinsic parameters. Then take a photo of some object (for example, a cup) using the calibrated camera, estimate the height and width of the selected object using both a ruler and an image from the calibrated camera. Calculate the distance between the camera image plane and the selected object. | 1
 |
| Question | The provided dataset contains left and right images in two different folders with the same name. For this task please select image pair corresponds to your id (0000[Id].png). You need to use 8 point algorithm in order to find the fundamental matrix. For the initial key points detection (minimum 8 corresponding points) you can either do it manually or use any key points detection technique. Next step is to estimate the disparity map for the selected image pair. You may assume the baseline of the stereo camera as the 10cm and focal length of both the left and right side cameras as 2.8mm. If you need any additional assumptions, please elaborate them in the report. | 1
 |
| Question | Build the hardware, and program and implement suitable code, for a simple color sensor suitable for an application of interest to you. An example of the principle you might employ is a hardware where the component in the center is a photo transistor; it detects light – with varying sensitivity – across the full visible spectrum, a little into the ultraviolet, and into the infrared to a little. Basic idea of the color meter is that LEDs are turned on and off in sequence, and the correspondingly detected signals are recorded. When all the LEDs are off the ambient (background) is recorded. In this way a ”signature” of any particular color patch placed in a location that is illuminated by the LEDs and seen by the phototransistor is generated. You could then, for example, compare the signature that you obtain from an ”unknown” item with the signatures of various items that you previously stored in a ”library”, hence identify (with some quantifiable degree of certainty) the ”unknown” item. Even If you do use this principle, you don’t have to use exactly these components. In your Arduino kit you probably have a variety of LEDs, probably including one ”tri-color” LED, and a phototransistor that you can use. | 1
 |
| Question | CCD vs CMOS technologies | 0
 |
| Question | Bayer mosaic filter vs Faveon capture color filter | 0
 |
| Question | Pinhole camera model | 0
 |
| Question | Stereo vision, Disparity map and Stereo image rectification | 0
 |
| Question | Multiple Camera Vision | 0
 |
| Question | Structure-from-Motion | 0
 |
| Question | ToF and multi-frequency phase-shift LIDAR technologies | 0
 |
| Question | SONAR sensing, SONAR transducer and transmitter | 0
 |
| Question | Distributed acoustic sensing (DAS) and applications | 0
 |
| Question | Doppler mm-wave RADAR | 0
 |


#### Section 3





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | UAV flies through the strong wind and begins to oscillate. The pitch angle change was measured with the gyro during a few seconds. Estimate proper trajectory for the pitch angle while considering the gyro reading are normally distributed by using Kalman filter. | 1
 |
| Question | UAV flies through the strong wind and begins to oscillate. The roll angle change was measured with the gyro during a few seconds. Estimate proper trajectory for the roll angle while considering the gyro reading are normally distributed by using Kalman filter. | 1
 |
| Question | UAV performs loop-the-loop. The pitch angle change was measured with the gyro during a few seconds. Estimate proper trajectory for the pitch angle while considering the gyro reading are normally distributed by using Kalman filter. | 1
 |
| Question | The human CoM (center of mass) during the walking has been measured with Kinect sensors. Estimate proper trajectory for the human CoM movement while considering reading are normally distributed by using Kalman filter. | 1
 |
| Question | Inside the right hand of the AR-601 robot there is an accelerometer. Engineers fixed the robot on the crane and went for a lunch. Robot was swinging by inertia for a few minutes. Engineers came back after lunch and read the data from accelerometer. Help them to understand what they measured. Estimate proper trajectory for the accelerometer reading while considering reading are normally distributed by using Kalman filter. | 1
 |
| Question | Expected Value and Variance of a Random Variable. Gaussian Distribution. | 0
 |
| Question | One Dimensional Kalman Filter | 0
 |
| Question | The main stages of Linear Kalman Filter (KF): Prediction and Update steps. KF initialization | 0
 |
| Question | Linear Kalman Filter vs Extended KF | 0
 |
| Question | KF, EKF, UKF and Particle Filter - main features and differences | 0
 |
| Question | Motion Capture (MoCap) system | 0
 |
| Question | Multicamera system | 0
 |


#### Section 4





| Activity Type | Content | Is Graded?
 |
| --- | --- | --- |
| Question | Take your smart phone and run for at least 100 meters with a constant speed. Your task is to estimate the trajectory where you ran with your phone which may be used to get some sensor reading such as accelerometer, gyroscope, GPS sensor and so on. You should use multidimensional Kalman filter with sensor fusion to solve this task. In the report clearly explain all the assumptions you made. | 1
 |
| Question | Inside the right hand of the AR-601 robot there is an accelerometer. Engineers fixed the robot on the crane and went for a lunch. Robot was swinging by inertia for a few minutes. Engineers came back after lunch and read the data from accelerometer. Help them to understand what they measured. Estimate proper trajectory for the accelerometer reading while considering reading are normally distributed by using Kalman filter. | 1
 |
| Question | GPS vs differential GPS (dGPS) | 0
 |
| Question | 9DOF IMU | 0
 |
| Question | Optical vs Mechanical Gyroscope | 0
 |
| Question | Laser vs Fiber Gyroscope | 0
 |
| Question | Absolute vs Incremental Encoders | 0
 |
| Question | MEMS for robot applications | 0
 |
| Question | What are the Smart and Intelligent Sensors? | 0
 |


### Final assessment


**Section 1**



1. Why do mobile robots need sensors?
2. Why do mobile robots need actuators?
3. What are the risks of not calibrating the robot sensors?
4. Why do we need to calibrate sensors?
5. What’s the difference between external and internal robot sensors?
6. What is the difference between Statistical and Systematic errors?
7. What is the difference between accuracy and precision?
8. Which type of error influences on accuracy and which type influences on precision?
9. Can we eliminate stochastic errors?
10. Can we eliminate systematic errors?
11. What is the difference between direct and indirect measurements?
12. How can we determine the uncertainty of indirect measurements?
13. Which type of error can be brought into measurements, if you did not perform the sensor calibration?
14. Sensors’ data contain rare random deviations (outliers), which are characterized a priori as unreliable values with unknown distribution law. Which algorithm can we apply for eliminating these unreliable values?
15. It is known that the instrumental error of the HOKUYO URG-04LX-UG01 laser rangefinder (LRF) is about ± 3% of measuring value. Let’s consider a quadcopter with the LRF, which flies in a corridor, making stops each 1 m to map the environment with the rangefinder. It is known that due to the quadcopter fluctuations, the total LRF measurement error increases up to ± 10% from the measurement value. How long does the quadcopter need to stay at each stop to map the environment with minimal error, if LRF performs 10 scans/sec?
16. Why do we use the regression analysis?
17. When we speak about regression data, what do we mean?
18. Can we use linear regression for variables with strong nonlinear relationships?
19. Can a least-squares fit be applied for polynomials?
20. Can we apply regression analysis for noisy wave described by sine function?
21. What is outlier?
22. What is the main idea of RANSAC?


**Section 2**



1. What’s the difference between CCD and CMOS?
2. Which advantages of CMOS technology do you know?
3. What’s the difference between Bayer mosaic filter and Faveon capture filter?
4. Why does the Bayer mosaic array have in two times more green color filters if compare with red and blue ones?
5. Why do we need to calibrate camera?
6. Which subjects or structures can we use for camera calibration?
7. What’s the difference between intrinsic and extrinsic parameters?
8. What’s the difference between radial and tangential distortions?
9. Can we calibrate a camera with autofocusing?
10. What is the pinhole camera model?
11. Does the pinhole camera model contain lens?
12. What’s the name of calibration parameters that reproject 3D world coordinate system to the 3D camera’s coordinate system?
13. What’s the name of calibration parameters that transform the 3D camera’s coordinates into the 2D image coordinates?
14. What is the optical center of a camera?
15. Which technology is widely used for producing a megapixel camera? CMOS or CCD?
16. What is the matrix name, which concludes focal length and a skew coefficient?
17. What are the applications of stereo vision?
18. What is the stereo vision?
19. Why do we calibrate the stereo camera system?
20. What is the output of stereo vision?
21. How do we get 3D reconstruction from binocular stereo?
22. Which visual cues (patterns) can provide 2D image with 3D information?
23. What is the triangulation?
24. What is the Stereo Image Rectification?
25. Why do we take multiple pairs of chessboard images from different angles during calibration?
26. What is the meaning of use an asymmetric chessboard as a calibration pattern?
27. Can we store the calibration images in a format with lossy compression?
28. What is the connection between anaglyph image and stereo image rectification?
29. What is the disparity map in stereo vision reconstruction process?
30. What is the result of Stereo Vision Scene Reconstruction?
31. What’s the difference between Time-of-flight & Structured-light sensors?
32. Give short description of Depth Measurement Techniques for Stereo Vision, ToF cameras, Kinect and LIDAR.
33. What is the motivation to use 3D sensors?
34. Which 3D sensing applications do you know?
35. What are the disadvantages of Multiple Camera Vision?
36. What is the ToF camera?
37. What’s the difference between ToF camera and scanning LIDAR?
38. What’s the difference of ToF imaging for Pulsed Modulation and Continuous Wave Modulation?
39. What do flying pixels mean?
40. What is the ToF Depth inhomogeneity?
41. What are the sources of systematic error for depth sensors?
42. Describe the main principle of Structured Light Imaging (e.g. for Kinect).
43. What’s the difference between LIDAR and Kinect?
44. What are the basic camera elements?
45. What is the focal length?
46. What are the Field of View and Angle of View?
47. Which Angle of View and Focal Length do you have at Zoom In?
48. What is the Depth of Field (DoF)?
49. What is Macro Photography (Close-up shooting) mode?
50. What is Fish eye camera?
51. What is Fish eye camera configuration concept?
52. What are the main characteristics of IR / thermal imaging camera?
53. What is the LIDAR?
54. What does a conventional LIDAR system involve?
55. What is the difference between incoherent and coherent LIDAR detection schemes?
56. How does LIDAR work?
57. Which optical components can LIDAR conclude?
58. What’s the advantage of low energy micro pulse LIDAR?
59. What is the difference between ToF and multi-frequency phase-shift LIDAR technologies?
60. Which achievements can we expect from LIDAR industry in the nearest future?
61. Give examples of LIDAR applications in surveillance and security.
62. What is the motivation to use LIDARs at the Airborne Laser Scanning?
63. What is SONAR?
64. How does SONAR work?
65. What are the main SONAR characteristics?
66. How can objects or surfaces’ features influence on SONAR sensing?
67. How does SONAR sensing change with work frequency increase?
68. What is the character of directional diagram for typical SONAR?
69. What are SONAR applications?
70. What is the typical material for the modern SONAR transducers?
71. How does piezo crystal work as the SONAR transducer and transmitter?
72. What is the piezoelectric effect? (direct and inverse)
73. How do Level Sensors work in tanks or cisterns?
74. How does Echo Sounders work?
75. What is the Doppler effect?
76. What is Distributed acoustic sensing (DAS)?
77. How can Distributed acoustic sensing (DAS) sense the acoustic signal?
78. What is Rayleigh scattering?
79. How does Doppler radar work?
80. Give examples of Distributed acoustic sensing (DAS) applications.
81. What is the mm-wave RADAR?
82. How does mm-wave RADAR work?


**Section 3**



1. What’s the difference between least square fitting and Kalman filtration?
2. What’s the difference between Conventional and Recursive Estimating the Mean?
3. What’s the difference between filtration and smoothing?
4. Does averaging deal with smoothing or filtration?
5. What are the advantages of Kalman filter implementation?
6. What can be the applications of Kalman filter?
7. What are the maximal and minimal values of Kalman gain (Kalman coefficient) and what they mean?
8. What is the difference between Kalman Filter (KF) and Extended Kalman Filter (EKF)?
9. The observations are processed using Kalman Filter. Imagine that State has 5 elements, and 1 observation data type. What is the size of the estimation error covariance matrix?
10. Describe two main steps of Kalman filter.
11. With what type of random variable distribution Kalman filter works?
12. What is the sensor fusion?
13. What is the advantage of sensor fusion?
14. Give an example of obtaining qualitatively new information from Sensor Fusion.
15. Give examples of Sensor fusion applications.
16. Why do we build multi-sensor systems instead of using a single sensor?
17. What is motivation to use Sensor Fusion in Robotics?
18. Why don’t we prefer averaging sensors’ data instead of fusion?
19. How can we combine (process) sensors’ data to get the best estimate of measurement value?
20. Can we fuse the sensors of different types with different measurement techniques and accuracies?
21. Why do we present the sensor’s models in terms of probability distributions?
22. What is the mean of a random variable? What is the variance of a random variable?
23. What is the Probability Density Function (PDF)? What is the Multi-modal Probability Density Function?
24. What are the advantages of using Gaussian PDF?
25. What does the central limit theorem state?
26. Let’s merge two Gaussian noise models. Is the standard deviation of the merged model bigger than for the initial noise models?
27. Having the sensor fusion, in which case the data averaging can be effective?
28. What’s the difference between the sensor fusion by Kalman Filter and Particle Filter?
29. Can we process non Gaussian Noise by Linear Kalman Filter?


**Section 4**



1. What can GPS module do?
2. Is GPS module typically able to work indoor?
3. What does the altimeter module include?
4. What can an altimeter module do?
5. What is inertia? What is inertial sensors?
6. Which types of inertial sensors do you know?
7. Which are two basic classes of rotation sensing gyros do you know?
8. What is the difference between Rate gyros and Rate integrating gyros?
9. What is IMU? What can it do?
10. What does accelerometer measure?
11. Can accelerometers measure the gravity?
12. What’s the difference between accelerometer and gyro?
13. What can 3D gyro measure?
14. Why is built-in temperature sensor used in modern gyros or accelerometers?
15. Why is embedded power down or sleep functions used in modern gyros?
16. What is the magnetometer?
17. What can magnetometer (compass module) do?
18. How does MEMS accelerometer work?
19. Which material is used for MEMS accelerometer’ spring and mass?
20. What is the Coriolis force?
21. Give examples of the Coriolis force appearance.
22. Does MEMS gyroscope contain of rotating mechanical parts?
23. How does MEMS gyro work?
24. Which optical gyros do you know?
25. Which components do you know in Laser Gyro?
26. How does laser gyro work?
27. What is Sagnac effect?
28. What is the advantages and disadvantages of Laser Gyro?
29. What is the difference between Ring-Laser Gyro (RLG) and Fibre optic gyro (FOG)?
30. Which position robot sensors do you know?
31. Which sensors can be used to measure mechanical quantities?
32. How do linear potentiometers work?
33. How do rotary potentiometers work?
34. What are the strain gauges?
35. What is the difference between strain gauges and tensometers?
36. How does differential pressure sensor work?
37. How do Force Measurement Resistors (FSR) work?
38. What are the Force Measurement Resistors (FSR)?
39. How do Capacitive sensors work?
40. What is the difference in position (displacement) measurements of conventional capacitive sensors and differential capacitive sensors?
41. Compare capacitive and inductive position sensors.
42. What is the principle of Inductive position sensor’s work?
43. What is piezoelectricity?
44. How does sensitivity depend on frequency in a typical piezoelectric sensor?
45. What does optical encoder measure?
46. What are the main components of optical encoder?
47. Can incremental encoders save angle position when power is switched off?
48. What is the difference between incremental and absolute optical encoders?
49. What is the Gray Code?
50. Does it have sense to apply the Gray code for incremental encoders?
51. What is the Resolver?
52. What is the difference between Resolvers and Optical Encoders?
53. What is MEMS?
54. What is the motivation to use MEMS?
55. Which materials can be used in MEMS fabrication?
56. Which basic MEMS fabrication techniques do you know?
57. What is the right order of fabrication process (etching, patterning, deposition)?
58. What is the patterning?
59. What is the etching?
60. Which types of micromachining do you know?
61. Which actuators do you know?
62. Give the examples of MEMS applications.
63. What are the typical MEMS dimensions?
64. What are the Smart sensors?
65. What is the motivation in Smart sensors?
66. What is the advantages of Smart sensors?


### The retake exam


**Section 1**


**Section 2**


**Section 3**


**Section 4**











