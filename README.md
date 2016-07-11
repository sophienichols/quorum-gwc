# quorum-gwc
Code for the Girls Who Code Hackathon

##Git Repository Setup

###Cloning the Git repository
1. On this page, click on the green button on the right side of the page above which says "Clone or download".
2. Copy the URL.
3. In your terminal window, run `git clone [url]`, replacing "[url]" with the copied URL.
4. You should now have the repository on your local computer. Let's go check it out! `cd quorum-gwc`
5. You are now in the directory that you successfully cloned!

###Working on a separate branch
When using version control such as git, you often want to work on a separate branch from the master branch. Working on separate branches makes it much easier to organize different features or logic, test your code, and collaborate with your partners. 

To start a new branch:
1. Make sure you are in the `quorum-gwc` directory. If not, `cd` into it.
2. Run `git checkout -b [name_of_your_branch]
3. You're on your new branch!

###Committing, Pushing, and the Like
Once you've gotten to a place in your code where you want to "save", it's time to commit and push!

1. Make sure you are in the `quorum-gwc` directory. If not, `cd` into it.
2. To commit, run `git commit -am "message describing commit"`
3. Before pushing, make sure you have any changes others have pushed to the branch you are working on by running `git pull`.
4. If there are any merge conflicts, go to the specified locations and fix conflicts after <<<HEAD. Commit once again by running the command from step 2. 
5. Now it's time to push to your branch, which you can do by typing `git push`. 

###Submitting a Pull Request
1. Go to github and click on the "< >Code" tab near the top of the page.
2. You should see a line comparing your branch and the master branch with a "Pull Request" button. Click this button.
3. Double check to make sure that there are no merge conflicts. If there are any, you should pull the master branch, merge it into your branch, fix any conflicts, and then 
4. In the request that you submit, you should describe what you did as well as assign people who should review this code.
5. Congrats, you have submitted a pull request!

