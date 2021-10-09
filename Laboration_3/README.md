# Laboration 3

## Environment & Tools
Microsoft Windows 10 Home 64-bit, PyCharm Professional, Command Prompt, Python version 3.9.7 & Git version 2.33.0
## Purpose
The purpose of this assignment is to get a deeper understanding of how to work with recursive functions, loggers, decorators and containers. Of how to streamline algorithms and program executions and the perks with utilizing loggers instead of print-statement. 
## Procedures
I started out with following the instructions and made a sketch of the new recursive function that was about to get implemented. Quick enough, I realized it would be hard to test it without logger and measurement decorator.
The logger was the first function that was finalized. I repeated the documentation about loggers and it went fairly smooth to create the logger. I used the json file and once I confirmed that the ass_3.logg was created, I continued with decorator.
As given in the instructions, I started with stating an empty list, start-time and logger info. In the loop, I created a range to loop through the max-number down to 0. With help from the functions created for calculated the values, I stored the values in the stated list until the loop was done. The results were going to be debugged every 5th execution, which I solved by modulus. The duration and values were returned as a tuple to be utilized later on. 
After making sure that the logger and the decorator was done, it was time to finalize fibonacci_memory. 

Now it was time to go for the print_statistict function, which would also confirm whether it was a faster solution or not. I followed the instruction based on the fib_details dictionary in the main function. I had to retrieve the name of the function from the key, and the duration from position 0 in the tuple that was created earlier. Once I got correct numbers, I created a loop to go through each fibonacci function and print it as an f-string. 
Lastly, it was time for write_to_file. With a context manager, I created the file based on the given filepath and opened in write mode. The values from the calculations I could find in position 1 in the tuple in fib_details dictionary, and the sequences could be determined on the length of values, which would give 0-30. As stated, to match, this sequence had to be reversed and put in a list in order to zip the lists together. To match them, this was done with a zip() built-in function.  

## Discussion

