
# Laboration 1
## Environment & Tools / Utvecklingsmiljö & Verktyg
Microsoft Windows 10 Home 64-bit, PyCharm Professional, Command Prompt, Python version 3.9.7 & Git version 2.33.0
## Purpose / Syfte
Learn how to use the version control with Git, how to clone repo's from Bitbucket and commit changes. This is to make collaboration more efficient and make sure that your repo's are up to date.
## Procedures / Genomförande
- First I went into Bitbucket and cloned the link to the repo into my command line; git clone https://ebbanimer@bitbucket.org/miun_dt179g/ebni2100_solutions_ht21.git
- Secondly, I created the laboration_1 branch; git branch laboration_1
- I checkouted from master branch to the new laboration_1 branch; git checkout laboration_1
- I set up the upstream to my remote repository; git push --set-upstream origin laboration_1 
- I started with the changes in the assignment, and once the first task was done, I saved it (git add .) and committed the change; git commit -m"First task done"
- Once the second task was done, I saved (git add .) committed the change; git commit -m"Second task done"
- Once finalizing the README file, the final change needs to be committed and pushed to the remote repository; git push -u origin laboration_1
- The final step of the exercise is to merge laboration_1 with master
## Discussion / Diskussion
I think the assignment with the git version control was valuable, especially in this early start of the course, as it will be essential to know the least of basics of how to utilize git. At first, it was a bit tricky to get started and it would be great to have a supervisor assisting, but it was a good lesson trying to sort everything out searching on internet and going through the literature. 
