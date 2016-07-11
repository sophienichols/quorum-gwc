# Trends Project
For this project, we're going to create trend graphs of Congressional productivity over time. We want to find the number and percent of bills in the House that:

1. were introduced
2. got out of committee
3. passed the House
4. passed the Senate
5. went to the President
6. were enacted

Then, we're going to graph these over time, and, if you'd like, further filter them by a word or phrase.

##Overall Process
1. Create a QuorumAPI object that only grabs House Bills
2. Iterate over all of the Congresses since 1989, finding how many bills were in each category per Congress.
3. Generate a list of dictionaries with the counts and percentages of each category.
4. Print out this list of dictionaries and visualize them through presskit.

##How to Use Quorum's PressKit
1. In Chrome, navigate to www.quorum.us/generatepdf/presskit/.
2. Copy your data (in JSON format -- a list of dictionaries) into the page.
3. Click submit, and use the sliders to change what you are visualizing.