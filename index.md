## Welcome Section 

Welcome to my project page where you can read about the enhancements and features I have implemented to demonstrate knowledge in Software Design/Engineering, Algorithms and Data Structures and Databases. 

### Code review

{% include youtube_embed.html id="l-0Q9c3d8nE" %}

### Software Design/Engineering 

For this milestone I am redesigning the “stock ticker” application I have developed for my final project in CS340 Client Server Development and use software engineering paradigms like object-oriented programming to structure the code into separate modules, each performing a discrete function. 

I selected this artifact because it presented itself as opportunity to demonstrate skills in areas of software design, leveraging object-oriented programming concepts like classes and inheritance to transform monolithic code into a more scalable and reusable code base. 

The original artifact consisted of APIs implementing CRUD (create, read, update, delete) data base functions for MongoDB together with a driver program using the APIs.
To enhance the original artifact and demonstrate software design/engineering skills I have redesigned it such that CRUD API are moved to their own class (DbConnection), with the class object responsible for the connection to the server hosting the database upon class instantiation. I have also created connection configuration file this class will use upon instantiation to separate database setup from the rest of the application logic for better maintenance and readability. 

The goal for the enhanced application is to leverage the existing database of stock tickers and create a system where traders and hedge fund managers can interact with the data. To do this, I have implemented another class (management) to handle the logic for a Trader and Manager object using inheritance and subclass common functions to divide responsibilities among these two different class objects. This class acts as a wrapper for the CRUD class.

The enhancement for this module met almost all course objectives I had planned for in Module One except for having unit tests for the new class methods. These are still on my radar and should be completed while submitting final changes and polishing the final artifact.
Modifying the original artifact to demonstrate skills in software engineering and software design presented a couple of challenges. The first challenge was coming up with a plan and vision for the enhanced application to showcase these skills, considering the original version by itself did not provide a scaffolding to improve on. To work around this, I had to redesign the code around a completely new implementation and functionality to leverage these new outcomes. The second challenge was implementing and testing the new design, because it was using a different software design paradigm from the original version and the objects and classes created had to work together and preserve the original functionality of the application as well.

This was an exercise that tested my abilities to plan and implement new requirements using skills in software design and software engineering and provided an opportunity to learn about time management as well as analytical skills such as breaking up the task into smaller deliverables like creating the class for the trader and manager objects and creating the class for the database CRUD APIs.

The changes demonstrating these outcomes can be found here:

https://github.com/felixt-snhu/felixt-snhu.github.io/blob/master/capstone_project/DbConnection.py

https://github.com/felixt-snhu/felixt-snhu.github.io/blob/master/capstone_project/dbcfg.py

https://github.com/felixt-snhu/felixt-snhu.github.io/blob/master/capstone_project/management.py
