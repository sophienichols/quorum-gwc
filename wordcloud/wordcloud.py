# this sets your path correctly so the imports work
import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))
from api import QuorumAPI
import re
from collections import Counter
from enums import DocumentType

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

# results = quorum_api.GET()

# if you did the previous two steps correctly, you should now have
# a list of dictionaries. This looks something like this:
#
# [
#   {'term': 'correlation', 'frequency': 9},
#   {'term': 'education', 'frequency': 4}
# ]
#
# And we want to make it look something like this:
# [
#   ["correlation", 9],
#   ["education", 4]
# ]

def convert_wordcloud_api_results(results):
    import json

    list_of_lists = []
    for result in results:
        list_of_lists.append([result["term"], result["frequency"]])

    return json.dumps(list_of_lists)

# print convert_wordcloud_api_results(results)

# now take those results, paste them into index.html,
# and take a look at them in your browser!

# Extra Credit:
# Now let's write our own wordcloud function that looks at documents directly.
quorum_api = quorum_api.word_cloud(False) \
                       .limit(1) \
                       .filter(document_type = DocumentType.tweet)
new_results = quorum_api.GET()

print new_results


# We're now going to create a class that processes those results
class WordCloud(object):

    # regex to match urls within text
    URL_REGEX = r"((http|https)://[^ \n]+)"

    # regex to match punctuation within text. DOESN'T REPLACE #
    # or @
    PUNCTUATION_TO_ESCAPE = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~.'
    PUNCTUATION_REGEX = "[%s]" % re.escape(PUNCTUATION_TO_ESCAPE)
    limit = 200

    def __init__(self, api_results):
        self.documents = api_results["objects"]

    def clean_string(self, string):
        # remove all the urls from the text
        url_subbed_text = re.sub(self.URL_REGEX,
                                 "",
                                 text)

        # Remove all punctuation
        punctuation_subbed_text = re.sub(self.PUNCTUATION_REGEX,
                                         "",
                                         url_subbed_text)

        return punctuation_subbed_text

    def process(self):
        # first, combine all the documents into one giant string
        for document in self.documents:
            full_string += document.raw_content

        # now, remove all punctuation
        full_string = self.clean_string(full_string)

        frequency_tuples = Counter(full_string).most_common(self.limit)

        return frequency_tuples

wc = WordCloud(new_results)
print wc.process()