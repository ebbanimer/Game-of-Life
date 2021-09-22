# Laboration 2

## Environment & Tools
Microsoft Windows 10 Home 64-bit, PyCharm Professional, Command Prompt, Python version 3.9.7 & Git version 2.33.0
## Purpose
The purpose of this assignment is to apply what we have learnt regarding datatypes and methods, functions and iterators. To understand how they work in practice and in which circumstances we may use them.  
## Procedures
- First things first, I made sure that I fully understood the assignment and identified which topics would be most relevant to this assignment. I identified that functions and loops would be necessary together with datatypes such as strings, lists and dictionaries. 
- After this, I made up a plan and a structure of how to tackle this assignment, as it was quite complex. It was important to conduct the task step by step to be able to test out different methods along the way. 
- I started out with completing the first function. As understood, the input would be in string-format and I would need to split up the string in two parts - username and password. The method I used for this was to convert the string into a list with three items, and followed by splitting up the list into two lists and variables - one for username and one for password. 
- Then it was time to pass over the variables to respective function by passing in the argument and calling the function.
- Since I knew the end-goal of the task, I decided to implement the True and False operation to have this in mind throughout the task. 


- Then I started with the formatting function. It was fairly straightforward formatting the username converting it to a string and modify it. 
- I passed the result to the user_tmp variable and returned the variable so it could be used in the authentication function. 


- Now it was time for the decryption of the password. I started out with identifying that I would need a for loop to go through the password, with some if & else statements. In order to do this, I would need to have an emtpy string to pass in the new password. 
- Now I constructed the for loop to loop through each character. I chose the method enumerate() to keep track on the indexes as I would need them as well for determination of even/odd index. 
- As it would be two conditions for even/odd indexes, I started out with those. But since there were two additional conditionals if the character was a vowel or not, I had to create nested if/else inside the outer if/else. 
- In the outer if/else, I had to determine if the index was even or odd and decide which rotation variable to use. 
- Within the inner if/else, I did the decryption of the password with ord() and char() with respective rotation. If it was a vowel, I added "0" on each side of the character. I passed in the end result in the emtpy pass_tmp string. 
- Now the decryption corresponded with the end-result, so I returned the pass_tmp to authenticate_user. 


- In the authenticate_user I had already prepared for the end-result. I had to adjust the if/else to make sure that the user would type in its corresponding password, and not another users password, therefore the value (pass_tmp) had to belong to the right key. 


## Discussion
At first, the assignment looked quite complex for being only three weeks in the program. It was tough to get started and to fully understand what I had to do, since I have more experience with Javascript I believed I had to have an input() to extract the username. I was stuck in the start, but I managed to get started with starting to create a list and as I was testing out the methods with using a print() function I got the desired output. 


At some points throughout the assignment I got stuck. The format_user function was quite simple and straightforward, but the decryption_password was trickier. I managed to determine if the index was even or odd and act upon that, but once I had to do the method for vowels or not, I got stuck. I didn't get the desired output when I was trying out method after method, but at some point I realize I would have to do a nested if/else for the outer if/else statement. 


At first glance, the assignment felt almost impossible to complete. I did not know where to start so I decided to redo the exercises and it got clearer what I had to use. Once I started to make a plan, it went quite well as the confidence grew. With motivation and telling myself that I would learn a lot from this assignment and it was a positive thing that it was tough, the confidence grew when I got the correct outputs. 


All in all, I'm happy with the assignment and I'm glad I've practiced problem-solving and learnt more about respective topic. 