# this sets your path correctly so the imports work
import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))

from api import QuorumAPI


class WordCloudAPI(QuorumAPI):

    def word_cloud(self, return_cloud=False):
        if return_cloud in [True, False]:
            self.filters["word_cloud"] = return_cloud
        else:
            raise Exception("Must be a Boolean value!")

        return self

    def process_request(self, *args, **kwargs):
        """ We need to override process_request so that the
        return

quorum_api = WordCloudAPI(username="gwc", api_key="691e43c415d88cd16286edb1f78abb2e348688da")
quorum_api = quorum_api.set_endpoint("document") \
                       .word_cloud(True) \
                       .filter(advanced_search="girls AND code")
print quorum_api.GET()
