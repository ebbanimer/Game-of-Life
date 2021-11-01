# Project

## Environment & Tools 
Microsoft Windows 10 Home 64-bit, PyCharm Professional, Command Prompt, Python version 3.9.7 & Git version 2.33.0


## Purpose 
The purpose of this project assignment is to apply all knowledge gathered from previous modules. To show an understanding 
of when and how to use the different approaches and concepts and identify issues along the way and finding a solution how to 
have them solved. 


My goal has been to formally achieve grade B or A, but minimum to not fail. But most importantly, my main goal is 
to learn how to apply each technique and concepts we have learnt and especially learn how to solve issues along the way. 
This in order to be on the path to become a highly skilled developer. 
## Procedures 
At first glance, this project would be quite challenging and extensive compared to previous assignments. I had to start
with reading through the PDF multiple times in order to wrap my head around it, and in order to set up a plan of how 
to front it. 


I did each function more or less in order, with a lot of testing and using the debugger throughout the journey of 
solving each function, and adding features along the way. Some parts were easier than expected, and vice versa. 
When I started out with parsing out the tuple in first function, it was quite challenging at first with setting 
up the try- and except block, as I have never applied it before. The different if-statements were fairly straightforward 
as they are very familiar to us by now, but I had to think twice how to convert and test the string to tuple. For some 
reason, I did not realize I could also include an else statement in the try-block, but eventually I chose to determine 
if the string had two elements, and if so, convert them to integers. 


The populate_world was also quite straightforward and did not require too much testing and debugging in order to work. 
However, when I was done with this function, I only had to print out the population dictionary to make sure that all 
values and the structure were correct. Later on, once I started to print out the world grid, it did not make sense why 
the shape wasn't the desired shape. After plenty of testing and trying out different methods, I had a look in codebase 
and at the coordinates, and there I saw that the axes were flipped. The coordinates were not formatted as width, 
height - in fact, they were flipped. Therefore, the function is written with the coordinate format (y, x) instead of (x, y).
As this was the function which would produce a dictionary with cells, states and neighbours, it had to be combined with 
code_base functions for patterns (or randomization) and the calculate_neighbour function, which was self-explanatory.


I did the project step by step, and I first completed grade E and later on grade D. The iteration in grade E was quite
straightforward, as well as the recursive version of it. Luckily, in our previous laboration, we had the opportunity 
to practice recursion, as this subject can be tricky to wrap your head around if you are a beginner. But importantly,
I had to make sure that I hade a base-case, the nth_generation was decreasing with -1 and the return statement was
the function. But, as I continued to grade B, this was no longer relevant as the decorated function would take care
of the simulations, which I will comment down below. Run_simulation only had to contain a return statement including 
update_world.


To update the population, update_world together with calculating alive neighbours were necessary. Without a doubt, 
update_world was the most challenging part of this project. The reason why was because I did not get desired shape and 
a simulation that looked like to examples given on Moodle. I was so sure that my code was right, and it made all the sense 
to me, both in calculating alive neighbours and update_world, but for some reason it did not produce the result I aimed for. 
By using the debugger, I knew that the printing in console was right, the determination of next generation cells had to be 
right, and the linebreak had to happen where the rimcells take place and after the length of rows were counted. I tried 
with the enumerate method together with modulus, but neither that worked. As mentioned above, I realized that I had to 
flip the coordinates to (y, x), and that is when I got the desired result. 


Moving on to grade C, this was very familiar as we worked with file handling in json very recently. To copy/populate
a dictionary wasn't a big challenge either, as this had been done in earlier functions. I just had to make sure that 
the elements in the dictionary were converted to tuples and populated with rimcells and coordinates with given status 
and neighbours. Once the 'pop' dictionary and world_size conformed to the right format, these were returned as one tuple.
At grade A, I just had to make sure to add an age key/value pair. 


Grade B included creating a logger and let the decorator function take care of the simulation. Creating the logger
wasn't the real challenge here, but the decorator function was. I was unsure of how to be able to gather the information -
how would I reach population, world size, alive/dead cells and generation? But, shortly I realized, I could access
all that information by calling the decorated function (run_simulation) to access all arguments. After this,
the rest was fairly straightforward, and I just had to apply once again concepts used priorly in the program, such as
the alive_cells counter and so forth. 

Lastly, grade A was just to add additional features in four functions and to make sure that the calculation of
cells also included elder and prime elder states.

## Discussion
This has been a great project in many ways, but at times I would have wished that grade E wouldn't be this difficult to 
achieve. I felt at times almost close to give up even though I knew I was so close to achieve grade E, but yet far away, 
since I did not get the desired output. Overall, my code looked good and the thought of failing because of not flipping 
the coordinates would have bothered me. Luckily, I managed to realize what was going on in codebase and locate where 
and how to flip the coordinates. I did have time to achieve grade D-A, and I know my capabilities were more
than achieving the lowest grade E. Grade E was definitely the most challenging, and I could have wished that perhaps
grade C, B and A would be the most difficult ones. At least, I hope I have learnt from my mistakes not looking carefully 
in functions already provided, in this case, codebase. If I had seen the details of the coordinates there, I would
have saved myself from a lot of stress. 

Looking at my own code, I realize that I have plenty of if- and else-statements. Would there be another method I could 
have used that could have shortened down my code? Or make it less redundant? What is interesting with programming, you 
realize that there are multiple ways to approach different problems, as long as you get the correct output. For instance, 
in update_world, I solved the problem both with enumerate + modulus and regular for loop. In this case, I chose the latter, 
since it was most straightforward. But I am sure that along the way, I have had the possibilities to find other efficient 
ways to construct the function, but I hope with more experience, I will be able to find shorter and faster ways to build 
programs. In the end of the day, this is how you become a skilled programmer, by testing different methods and failing 
along the way to learn from your errors. 




