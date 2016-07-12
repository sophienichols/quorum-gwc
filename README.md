# quorum-gwc
## Code for the Girls Who Code Hackathon

Welcome to the Girls Who Code Congressional Hackathon! We've put together three different types of projects that you can work on. All three of these projects depend on the QuorumAPI class that we built together earlier today, and we're excited to let you start using it.

##Projects

1. *Trends*: Generate a trend graph of the number of bills introduced, that left committee, that passed the House/Senate, etc. per chamber over the last few years.
2. *Choropleth*: Generate a map with each state colored by the number of times a given word or phrase has been mentioned in Congress.
3. *Wordcloud*: Generate a wordcloud of the words used by Members of Congress when they talk about a given topic.

##Directory Structure
Each project has its own folder, appropriately named "trends", "choropleth", and "wordcloud". You can switch into those projects by running `cd <projectname>`, and once there, further instructions will await you in the README associated with each project. In this folder are the following files:

- *api.py*: This file contains our global API class. Go spend some time reading through this file -- you'll be using it in all
- *enums.py*: This file contains a set of enums, or helpful classes that we use to organize data in Quorum.

##Setting Up this Git Repository on Your Computer

One common tool used in most software engineering is Github. We'll walk you through the basic steps of getting set up in Github here today, but you may also want to look into https://try.github.io/levels/1/challenges/1

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
2. Run `git checkout -b [name\_of\_your\_branch]
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

