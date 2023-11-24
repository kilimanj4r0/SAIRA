






BSc: Software Systems Design
============================



(Redirected from [BSc:SoftwareSystemsDesign](/index.php?title=BSc:SoftwareSystemsDesign&redirect=no "BSc:SoftwareSystemsDesign"))


Contents
--------


* [1 Software Systems Design](#Software_Systems_Design)
	+ [1.1 Administrative details](#Administrative_details)
	+ [1.2 Prerequisites](#Prerequisites)
	+ [1.3 Course outline](#Course_outline)
	+ [1.4 Expected learning outcomes](#Expected_learning_outcomes)
	+ [1.5 Expected acquired core competences](#Expected_acquired_core_competences)
	+ [1.6 Textbook](#Textbook)
	+ [1.7 Reference material](#Reference_material)
	+ [1.8 Required computer resources](#Required_computer_resources)
	+ [1.9 Evaluation](#Evaluation)



Software Systems Design
=======================


* **Course name:** Software Systems Design
* **Course number:** XYZ
* **Knowledge area:** Software Development Fundamentals, Software Engineering, Systems Fundamentals


Administrative details
----------------------


* **Faculty:** Computer Science and Engineering
* **Year of instruction:** 3rd year of BS
* **Semester of instruction:** 1st semester
* **No. of Credits:** 4 ECTS
* **Total workload on average:** 144 hours overall
* **Class lecture hours:** 2 per week
* **Class tutorial hours:** 2 per week
* **Lab hours:** 2 per week
* **Individual lab hours:** 0
* **Frequency:** weekly throughout the semester
* **Grading mode:** letters: A, B, C, D


Prerequisites
-------------


* Data Structures and Algorithms I
* Data Structures and Algorithms II (merge with [this\_course <https://eduwiki.innopolis.university/index.php/BSc:IntroductionToProgrammingII.S22>])
* Discrete Math/Logic
* Introduction to Programming I
* Introduction to Programming II


Course outline
--------------


The need for building large scale Software has been increased in the last two decades. Nowadays, Software engineers are less likely to design data structures and algorithms from scratch. They are required to build systems from library and framework components. The Software System Design course aims to teach students the m ain concepts related to the construction of software systems. The course covers technical topics such as concepts of design for complex systems, object oriented programming, UML notation, among others.


  

Software system design and analysis 2023


Jan 24. Lecture 1



* Introductory remarks.
* Evolution of the language: versions. ISO standards.
* C/C++ memory model: program code, heap & stack.
* The notion of type & the evolution of the notion.
* The C++ type system.
* Type modifiers & constant types.
* Reference types.


Tutorial 1



* Organizational rules and regulations.
* The very first C++ program and its detailed explanation.
* C++ program overall structure. Namespaces & qualified names.
* Arrays vs vectors; range for-loops.


Lab 1. Hello Lab - Introduction to C++


  
 
Jan 31. Lecture 2



* Data & data types.
* Type & data declaration & initialization. Auto specifier & type deducing.
* Type conversions.
* Initialization forms.
* More on constant expressions.
* Structured binding.


Tutorial 2



* A series of simple programs using pointers & references.
* Various ways of object declarations: illustrations.
* Example: standard and user-defined conversions.


Lab 2 - Pointers and References.


Feb 7. Lecture 3



* The notion of a user-defined type: classes without OOP.
* What do we need to specify a new type? – detailed consideration.
* Class detailed characterization: data, operations on data (member functions)
* A class: interface and implementation.
* Class declarations and class instances: the ways of creating objects.
* Object destruction. Delete operators.
* Important extensions: operator functions
* Important extensions: user-defined type conversions (conversion functions).


Tutorial 3



* Example; a typical program structure with headers/bodies & include’s.
* An example with namespaces
* Program example of function overloading


Lab 3. Functions in C++, algorithm problems that can be solved via functions


Feb 14. Lecture 4


Basics of C++ OOP:



* Encapsulation: access control.
* Inheritance; single & multiple inheritance; virtual inheritance.
* OOP implementation: the notion of sub-object.
* Polymorphism & virtual functions.
* Abstract classes & pure virtual functions.
* Constructors & destructors; virtual destructors
* Ctor- & mem-initializers
* this pointer


Tutorial 4



* An example with inheritance.
* Upcasting and downcasting. Cast operators.
* Extended example of polymorphism (shapes).
* What’s inherited – interface and/or implementation?
* An example about abstract classes: two Airbus models


Lab 4. OOP principles using C++ (Inheritance, Encapsulation)


Feb 21. Lecture 5



* Initializing bases & members
* Delegating Constructors
* this pointer (Why it’s duplicated)
* Constant member functions
* “Deleted” and “defaulted” functions
* Functions & member functions: declarations & definitions


Tutorial 5



* Example with functions and member functions
* Example with constructor & Initializing
* Example with this pointer


Lab 5. OOP principles using C++ ( Polymorphism, Abstract)


Feb 28. Lecture 6



* Functional programming: what’s this?
* C++: functional approach in the imperative language.
* Pointers to functions.
* Functional types & functional objects.
* FP implementation in C++: lambda expressions.


Tutorial 6. UML basics (to remind: Use case diagrams, Class diagram)


Lab 6 UML practical example with coding (Class diagram, Use case diagram)


Mar 7. Lecture 7



* Generic programming: introduction to the paradigm.
* C++ approach: templates. Template parameters: type & non-type.


-\* Templates: declaration & using. Template instantiation.



* Function & class templates.
* Implicit & explicit instantiation; partial specialization.


Tutorial 7



* Generic programming (continued).
* Implicit & explicit instantiation; partial specialization.
* The new notion: concept. Template parameter constraints.
* (Optional) Variadic template parameters; the SFINAE principle.
* (Optional) Decltype specifier & trailing return type specifier.


Lab 7. Templates in practice


Mar 14. Lecture 8 Midterm examination


Tutorial 8. No tutorial (due to midterm)


Lab 8. No labs


Mar 21. Lecture 9



* Introduction to the C++ standard library.
* STL: the structure and the basic design principles.
* The notion of C++ STL iterator.
* How iterators are used: the detailed five-step consideration.
* An extended example: reverse iterator.
* Iterator categories.
* RANGE – the first simple template: detailed explanation.
* An advanced template example.


Tutorial 9. SOLID, GRASP Principles


Lab 9. Practical application on SOLID.


Mar 28. Lecture 10



* Introduction to System software design and Design Patterns-
* Taxonomy of patterns
* Patterns and anti-patterns
* First two patterns: Prototype, Singleton


Tutorial 10. Factory method, Singleton, Builder


Lab 10. Builder, Factory, Singleton


Lecture 11. Adapter, Bridge, Composite


Tutorial 11. Decorator, Facade, Flyweight, Proxy


Lab 11. Adapter, Bridge, Composite, Facade


Lecture 12. Chain of responsibility, Command, Iterator


Tutorial 12. Memento, Observer, Chain of responsibility


Lab 12. Chain of responsibility, Command, Iterator


Apr 18. Lecture 13 - State, Strategy


Tutorial 13. Mediator, Memento, Observer, Template method, Visitor


Lab 13. Observer, Momento


Apr 25. Lecture 14 TBA


Tutorial 14



* BLOC
* Guest from industry (Explain patterns with UI)


Lab 14. Mediator, Template method


May 02. Lecture 15



* Best practices, clean code
* When to use (and when not to use) design patterns
* Anti-patterns


Tutorial 15. Individual exam (Students will be given a problem and they should apply a design pattern on the problem)


Lab 15. Code review, Best practices, Anti patterns


May. Final Examination


PS: Some topics might changed a bit



Expected learning outcomes
--------------------------


After taking the course, students will



* understand and apply object-oriented design techniques;
* develop and evaluate software systems;
* express the specifications and design of an application using UML;
* specify parts of the design using a formal design language (OCL);
* have experience designing medium-scale systems with patterns;
* have experience testing and analysing software.


Expected acquired core competences
----------------------------------


* Formal Models and Semantics
* Requirements Engineering
* Software Design
* Software Engineering
* Software Evolution


Textbook
--------


* Grady Booch, Robert Maksimchuk, Michael Engle, Bobbi Young, Jim Conallen, and Kelli Houston. 2007. Object-Oriented Analysis and Design with Applications, Third Edition (Third ed.). Addison-Wesley Professional.
* Hans-Erik Eriksson, Magnus Penker, Brian Lyons, David Fado, UML 2 Toolkit, OMG Press, 2004


Reference material
------------------


* Lecturing and lab slides and material will be provided


Required computer resources
---------------------------


Students should have laptops with basic software for reading and editing document.



Evaluation
----------


* Course Project (30%)
* Mid-term Exam (30%)
* Final Exam (30%)
* Class and lab participation (10%)










