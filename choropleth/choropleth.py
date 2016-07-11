# this sets your path correctly so the imports work
import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))

from api import QuorumAPI
import json
# this library will let us turn dictionaries into csv files
import csv


class ChoroplethVisualizer(object):

    # Since both the api_key and username stay the same so initialize API object once
    quorum_api = QuorumAPI(username="gwc", api_key="691e43c415d88cd16286edb1f78abb2e348688da")


    """
    create cache dictionary with lists of member ids keyed by state
    """
    # In order to query the API properly later on, we first create a
    # dictionary so that given a state id, we can get the list of
    # representatives and senators from that state. 
    # In this dictionary, the 'key' is the state's id, and the 'value'
    # is the list of associated members of Congress.

    def get_members_by_state(self):

        # First we create an empty dictionary that we will
        # populate with relevant information!
        members_by_state = {}

        # Next, we want to use the API to get information about the states.
        # Namely, we want the 'id' field associated with each state,
        # as this will help us get the associated members.
        quorum_api = self.quorum_api.set_endpoint("state") \
                        .count(True) \
                        .offset(20) \
                        .filter()
        # what we get back is a bunch of "state objects",
        # where each object contains information about a state
        # such as its id, abbreviation, geographical coordinates, etc.
        states = quorum_api.GET()
        # Now we need to access the 'id' field of each state object from above.
        # The GET() call should have returned an object for every state,
        # so we now want to iterate over each of these objects to grab the id,
        # and then use this id to find members of congress from this state.
        for state in states["objects"]:
            state_id = state["id"]
            print state_id
            # let's get the list of senators/representatives from each state!
            # remember, we can filter on the "most_recent_state" field, which
            # contains the id of the state where the member is from.
            # Don't forget to set the appropriate endpoint!
            quorum_api = self.quorum_api.set_endpoint("person") \
                            .count(True) \
                            .offset(20) \
                            .limit(100) \
                            .filter(most_recent_state = state_id, current=True)
            members = quorum_api.GET()

            # Now we have a list of member objects from this state,
            # but all we want to store is a list of id numbers of each member.
            # Let's construct a list of ids of the members from this state!
            member_ids = [member["id"] for member in members["objects"]]
            print member_ids
            # Now let us put the information in the dictionary we are building.
            # Remember that the state_id is the key and the list of member ids is the value.
            members_by_state[state_id] = member_ids

        return members_by_state

    # this function saves the function above as a file in an efficient way
    # for quick future access and reuse.
    def save_members_by_state_json(self):
        members_by_state = self.get_members_by_state()
        with open('member_by_state.json', 'wb') as f:
            json.dump(members_by_state, f)


    # A helper function which parses the file "members_by_state.json",
    # which contains a dictionary where you can look up lists of member ids
    # given a state.
    def parse_members_by_state_json(self):
        with open('member_by_state.json', 'rb') as f:
            data = json.load(f)
        return data


    # Let's write a helper function that takes in a dictionary of (state, number)
    # key-value pairs and produces a csv file of the following format:
    # state,num
    # Alabama,9
    # Alaska, 5
    # ...etc.
    # We can use the csv class that we imported above.
    def save_state_csv(self, item_dict):
        # we want to use python's 'with...as' syntax because 
        # it is a safe way to open and write files.
        with open('data_test.csv', 'wb') as f:
            w = csv.writer(f, delimiter=',')
            w.writerow(('state', 'num'))
            w.writerows(item_dict.items())


    def get_word_mentions_per_state(self, word):
        """
        get the number of documents that the given word is mentioned in each state.
        Write this to the data.csv file that will then be used
        """
        # get the dictionary of lists of members from each state
        members_by_state = self.get_members_by_state()

        # this is the dictionary that will be populated with the number of word mentions per state
        mentions_per_state = {}
        quorum_api = self.quorum_api.set_endpoint("document") \
                            .count(True) \
                            .offset(20) \
        # iterate over the lists in our dictionary, keyed by state
        for state, member_lst in members_by_state.iteritems():
            #comma_id_lst = ','.join(map(str, member_lst))
            # get all documents which mention the desired word from the state in question
            quorum_api = quorum_api.filter(advanced_search = word, source_person__in = member_lst)
            results = quorum_api.GET()

            # store the number of documents for this state
            mentions_per_state[state] = results["meta"]["total_count"]

        self.save_csv(mentions_per_state)

word = "potato"
member_lst = [300043, 300011]

quorum_api = QuorumAPI(username="gwc", api_key="691e43c415d88cd16286edb1f78abb2e348688da")
quorum_api = quorum_api.set_endpoint("document") \
                    .count(True) \
                    .offset(0) \
                    .limit(2) \
                    .filter(advanced_search = word, source_person__in = member_lst)
print quorum_api.GET()["meta"]["total_count"]

quorum_api = quorum_api.set_endpoint("person") \
                            .count(True) \
                            .offset(20) \
                            .limit(100) \
                            .filter(most_recent_state=51, current=True)
members = quorum_api.GET()





