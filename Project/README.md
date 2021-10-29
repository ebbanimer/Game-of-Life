# Project

## Environment & Tools 
Microsoft Windows 10 Home 64-bit, PyCharm Professional, Command Prompt, Python version 3.9.7 & Git version 2.33.0


## Purpose 
The purpose of this project assignment is to apply all knowledge gathered from previous modules. To show an understanding of when and how to use the different approaches and concepts and identify issues along the way and finding a solution how to have them solved. 


My goal has been to formally achieve grade B or A, but minimum to not fail. But most importantly, my main goal is to learn how to apply each technique and concepts we have learnt and especially learn how to solve issues along the way. This in order to be on the path to become a highly skilled developer. 
## Procedures 
At first glance, this project would be quite challenging and extensive compared to previous assignments. I had to start with reading through the PDF multiple times in order to wrap my head around it and it order to set up a plan of how to front it. 


I did each function more or less in order, with a lot of testing and using the debugger throughout the journey of solving each function. Some parts were easier than expected, and vice versa. When I started out with parsing out the tuple in first function, it was quite challenging at first with setting up the try- and except block, as I have never applied it before. The different if-statements were fairly straightforward as they are very familiar to us by now, but I had to think twice how to convert and test the string to tuple. For some reason, I did not realize I could also include an else statement in the try-block, so I chose to determine if the string had two elements, and if so, convert them to integers. 


The populate_world was also quite straightforward and did not require too much testing and debugging in order to work. However, when I was done with this function, I only had to print out the population dictionary to make sure that all values and the structure were correct. Later on, once I started to print out the world grid, it did not make sense why the shape wasn't the desired shape. After plenty of testing and trying out different methods, I had a look in codebase and at the coordinates, and there I saw that the axes were flipped. The coordinates were not formatted as width, height - in fact, they were flipped. Therefore, the function is written with the coordinate format (y, x) instead of (x, y). As this was the function which would produce a dictionary with cells, states and neighbours, it had to be combined with code_base functions for patterns (or randomization) and the calculate_neighbour function, which was self explainatory.


As I wanted first to complete grade E before achieving higher levels, I first completed run_simulation with an iteration, which was fairly straightforward and I do not have more comments on that, as I decided to modify it to grade D. I was already familiar with recursion from assignment 3, this was also fairly straightforward. Although,, at first, I wasn't sure if I should have created an additional inner function solely for a recursion, but I decided to aim for only populating the existing. The base-cases and the inner function took not much effort to create, and I knew the return statement had to contain a function. Obviously, it had to contact the function itself with all mandatory arguments. World_size was constant, the population was updated and stored in population, and the nth_generation had to increment to fulfill recursion. 


To update the population, update_world together with calculating alive neighbours were necessary. Without a doubt, update_world was the most challenging part of this project. The reason why was because I did not get desired shape and a simulation that looked like to examples given on Moodle. I was so sure that my code was right and it made all the sense to me, both in calculating alive neighbours and update_world, but for some reason it did not produce the result I aimed for. By using the debugger, I knew that the printing in console was right, the determination of next generation cells had to be right, and the linebreak had to happen where the rimcells take place and after the length of rows were counted. I tried with the enumerate method together with modulus, but neither that worked. As mentioned above, I realized that I had to flip the coordinates to (y, x), and that is when I got the desired result. 


Now, when I was finally done with grade E and grade D, I could finally tackle grade C. This was very familiar as we worked with file handling in json very recently. To copy/populate a dictionary wasn't a big challenge either, as this had been done in earlier functions. I just had to make sure that the elements in the dictionary were converted to tuples and populated with rimcells and coordinates with given status and neighbours. Once the 'pop' dictionary and world_size conformed to the right format, these were returned as one tuple.

## Discussion
This has been a great project in many ways, but at times I would have wished that grade E wouldn't be this difficult to achieve. I felt at times almost close to give up even though I knew I was so close to achieve grade E, but yet far away, since I did not get the desired output. Overall, my code looked good and the thought of failing because of not flipping the coordinates would have bothered me. Luckily, I managed to realize what was going on in codebase and locate where and how to flip the coordinates. I did have time to achieve grade D and C, but I would have wished to aim for B and A as well. Due to lack of time because of being stuck on the coordinates, unfortunately this was not managable, and I hope I have learnt from my mistakes to not look carefully in the functions already provided. I thought I had looked closely, but missed this detail. 


What is interesting with programming, you realize that there are multiple ways to approach different problems, as long as you get the correct output. For instance, in update_world, I solved the problem both with enumerate + modulus and regular for loop. In this case, I chose the latter, since it was most straightforward. But I am sure that along the way, I have had the possibilities to find other efficient ways to construct the function, but I hope with more experience, I will be able to find shorter and faster ways to build programs. In the end of the day, this is how you become a skilled programmer, by testing different methods and failing along the way to learn from your errors. 




