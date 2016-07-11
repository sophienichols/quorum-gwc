# Wordcloud Project
For this project, we're going to take a word or phrase and a set of documents and find out which words are used most frequently at the same time when mentioned by Members.

##Overall Process
1. First we're going to do this the easy way: we're going to use the wordcloud function built into the Quorum API to return results. To do this, we're going to subclass the QuorumAPI class to make one that supports making wordclouds.
2. Then, we're going to roll our own WordCloud function to transform a list of documents into the counts of the most common words.
3. Finally, we'll visualize this using a pre-built wordcloud visualization.

## How to Run Your Localserver
1. `cd` into the approprate directory (wordcloud/, for example)
2. Run `python -m SimpleHTTPServer`
3. Go to `localhost:8000` in your local browser
4. Rejoice!