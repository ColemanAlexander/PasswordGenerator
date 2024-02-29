# [PasswordGenerator](https://drive.google.com/file/d/1o3Om24UFlfxUWt_1_rVjS78mnZNwoped/view?usp=sharing)

## Part 1

The first part of the assignment is to modify the code given to input a 
user defined password (of arbitrary string length) and output (to file) a new random 
generated password (of the same string length). To do this, the function random will 
need to be initialised or ‘seeded’ with the input password using the Python code:
random.seed(input_password)
In this context, the input parameter length in the Python code provided must be placed with input variable input_password.

## Part 2

The second part of the project is to convert the command line script in to a Python app 
using a simple Graphical User Interface (GUI). The GUI will need to include fields to:
• input the user define password – first text field;
• output the new password – second text field;
• state that the new password has been successfully output to file,
specifying the (default) name of the file and its (path) location.

## Part 3

The final component of the assignment concerns the use of the random function which 
is an intrinsic function of a Python library. The aim is to replace this function with one 
generated using the evolutionary computing (symbolic regression) system TuringBot:
• Use random.org to produce a stream of random numbers in [0,1].


• Use this sequence to seed the data for implementation of the 
TuringBot system to produce a unique nonlinear formula.
• Use this ‘formula’ to generate a new function to replace function 
random.

