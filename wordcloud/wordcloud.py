# this sets your path correctly so the imports work
import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))
from api import QuorumAPI
import re
from collections import Counter
from enums import DocumentType
from stop_words import stop_words


# first, we subclass the QuorumAPI to support wordclouds.
# to do this, we'll use the same approach as the count function
# in order to make the final API request have &word_cloud=true
class WordCloudAPI(QuorumAPI):

    def word_cloud(self, return_cloud=False):
        if return_cloud in [True, False]:
            self.filters["word_cloud"] = return_cloud
        else:
            raise Exception("Must be a Boolean value!")

        return self

# now that we've created that API, let's run it and store the results
quorum_api = WordCloudAPI(username="gwc", api_key="691e43c415d88cd16286edb1f78abb2e348688da")
quorum_api = quorum_api.set_endpoint("document") \
                       .word_cloud(True) \
                       .filter(advanced_search="girls AND code")


# if you did the previous two steps correctly, you should now have
# a list of dictionaries. This looks something like this:

# [
#   {'term': 'correlation', 'frequency': 9},
#   {'term': 'education', 'frequency': 4}
# ]

# And we want to make it look something like this:
# [
#   ["correlation", 9],
#   ["education", 4]
# ]


results = quorum_api.GET()


def convert_wordcloud_api_results(results):
    """
    Takes in list of results dicts and returns a
    lists of lists
    """
    import json
    pass


# Now lets look at the results:
print convert_wordcloud_api_results(results)

# now take those results, paste them into index.html,
# and take a look at them in your browser!


# Extra Credit:
# Now let's write our own wordcloud function that looks at documents directly.
### TODO


# We're now going to create a class that processes those results
class WordCloud(object):

    # regex to match urls within text
    URL_REGEX = r"((http|https)://[^ \n]+)"

    # regex to match punctuation within text. DOESN'T REPLACE #
    # or @
    PUNCTUATION_TO_ESCAPE = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~.'
    PUNCTUATION_REGEX = "[%s]" % re.escape(PUNCTUATION_TO_ESCAPE)
    limit = 200

    def clean_and_split(self, text):
        """
        This function takes in a string of text and returns a cleaned
        and split list of important words.
        """
        pass


    def process(self, api_results):
        """
        This function takes in the results from an API request
        and return a list of frequency tuples of words
        """
        pass


# Create a WordCloud object and get the results
### TODO
