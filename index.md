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

The changes demonstrating these outcomes can be found here: have been pushed to the 'software_design_engineering' branch https://github.com/felixt-snhu/felixt-snhu.github.io.git


### Algorithms and Data Structures 

The artifact I have enhanced for the algorithms and data structures checkpoint builds on the “stock ticker” application submitted in Module 3, which is a complete redesign of the application developed in my final project in CS340 Client Server Development. 

For this milestone, I have submitted: 1. a driver application (final_api.py) that uses the classes submitted in Module 3 – this constitutes the entry point for the application and user interface; 2. a helper utility file (chr2hex.py) that implements the algorithm and data structure for the user authentication scheme; 3. A modified from Module 3 management class file (management.py) with the algorithm that implements the user menu with command operations for each individual class type (trader vs manager); 4. A file with some unit tests (tests.py) which will continue to get updated during the course – this is more to demonstrate best engineering practices and code testing strategies.

The driver application implements the user interface which prompts the user to authenticate with a user name and password which are checked against a credentials file (users.json). The algorithm checks that the values provided by the users match the values in the credentials file, then prompts the user to make a choice to execute commands either as a Trader or as a Manager. The prompt is generated using an algorithm designed in a standalone function (request_prompt) that continuously prompts the user for either an ‘m’ option for manager, or ‘t’ option for trader using a regex expression to match these values. Once one of them was matched, the function returns the prompt which will be used by the driver application to instantiate the correct class object.

The authentication algorithm uses a dictionary structure to map characters to a hexadecimal value, where each ASCII character (key) maps to a byte (value) in the dictionary. Two functions have been implemented to implement this functionality, one to encode the password using the dictionary and one to decode it. The decoding algorithm splits the input string to decode into value pairs, adds them to the list, then for each pair, we look up their value in the dictionary and create a new string with the decoded value.

The management class was also enhanced to implement the menu system for each of the class objects, manager or trader. This was accomplished using inheritance, the menu being generated in the parent class which makes it such that only options for the instantiated object to be displayed in the menu.
The algorithm for creating the menu uses a list comprehension structure to extract class attributes matching names starting with “m” which correspond to the function names of each class object, meaning that options in this menu list will be picked from the class object that will get instantiated (Trader or Manager).

When the class object is instantiated, this menu list is displayed in a loop until the user types the function name/operation to execute or presses the ‘q’ button to quit.
These changes demonstrate completion of data structures and algorithms section of this project and represent all enhancements I had planned for this milestone. 

Implementing the algorithms for the menus and prompts required both thought and some trial and error and debugging, which was an iterative process. To verify functionality was correct, I had done both functional testing and created some unit tests. Debugging issues for the algorithms was done using the Pycharm IDE debugger, which allowed stepping through each line of the code and inspecting state of variables and objects.  This is how I was able to address issues found in the algorithm logic that builds the option menu for the user. Another challenge which I have yet to fix was in creating a more user-friendly option menu. 

My plan was to construct a dictionary out of the function names and map them to numbers, such that instead of typing the function name to execute, the user would only type the number associated with the option. The challenge was not implementing this with a dictionary structure which I have done successfully, but when using it would return program execution from the management class back to the driver application. I have commented out the code for now and will revisit it later for further debugging.

The changes demonstrating these outcomes can be found here: have been pushed to the 'algorithms_and_data_structures' branch https://github.com/felixt-snhu/felixt-snhu.github.io.git
