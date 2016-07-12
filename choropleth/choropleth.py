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

    # In order to query the API properly later on, we first create a
    # dictionary so that given a state id, we can get the list of
    # representatives and senators from that state. 
    # In this dictionary, the 'key' is the state's id, and the 'value'
    # is the list of associated members of Congress.

    def get_members_by_state(self):

        # First we create an empty dictionary that we will
        # populate with relevant information!

        # Next, we want to use the API to get information about the states.
        # Namely, we want the 'id' field associated with each state,
        # as this will help us get the associated members.


        # what we get back is a bunch of "state objects",
        # where each object contains information about a state
        # such as its id, abbreviation, geographical coordinates, etc.


        # Now we need to access the 'id' and 'name' fields of each state object from above.
        # The GET() call should have returned an object for every state,
        # so we now want to iterate over each of these objects to grab the id,
        # and then use this id to find members of congress from this state.
        


            # let's get the list of senators/representatives from each state!
            # remember, we can filter on the "most_recent_state" field, which
            # contains the id of the state where the member is from.
            # Don't forget to set the appropriate endpoint!




            # Now we have a list of member objects from this state,
            # but all we want to store is a list of id numbers of each member.
            # Let's construct a list of ids of the members from this state!

            # Now let us put the information in the dictionary we are building.
            # Remember that the state_id is the key and the list of member ids is the value.



    # this function saves the function above as a file in an efficient way
    # for quick future access and reuse.
    def save_members_by_state_json(self):






    # Below is a helper function which will try to open the file "members_by_state.json",
    # which contains a dictionary where you can look up lists of member ids
    # given a state. If it doesn't exist, it will run the above files and save it.
    # (tl;dr: use this to get the dictionary of member id lists for each state.)
    def parse_members_by_state_json(self):





    # Let's write a helper function that takes in a dictionary of (state, number)
    # key-value pairs and produces a csv file of the following format:
    # state,num
    # Alabama,9
    # Alaska, 5
    # ...etc.
    # We can use the csv class that we imported above.
    def save_state_csv(self, item_dict, file_name):
        # we want to use python's 'with...as' syntax because 
        # it is a safe way to open and write files.




    def get_word_mentions_per_state(self, word):
        """
        get the number of documents that the given word is mentioned in each state.
        Write this to the data.csv file that will then be used
        """
        # Use the provided parse function above to get a dictionary with key,value pairs of
        # state names and the lists of members from that state, respectively.


cv = ChoroplethVisualizer()
# the word that we are building the choropleth about!
word = "representation"

cv.get_word_mentions_per_state(word)
