from api import QuorumAPI
from enums import RoleType
from enums import BillStatus
import csv

class ChoroplethVisualizer(object):

    def __init__(self):
        self.members_by_state = self.get_members_by_state()

    """
    helper function which given a dictionary produces a CSV file.
    """
    def save_csv(item_dict):
        with open('data.csv', 'wb') as f:
            w = csv.writer(f, fieldnames=['state', 'num'], delimiter=',')
            w.writerow(('state', 'num'))
            w.writerows(item_dict.items())

    """
    create cache dictionary with lists of member ids keyed by state
    """
    def get_members_by_state(self):
        # the dictionary that we will populate with this info!
        members_by_state = {}

        # get state info using the api call
        quorum_api = QuorumAPI(username="gwc", api_key="691e43c415d88cd16286edb1f78abb2e348688da")
        quorum_api = quorum_api.set_endpoint("state") \
                        .count(True) \
                        .offset(20) \
        states = quorum_api.GET()

        # iterate over each state that was returned above
        for state in states:
            state_id = state.id
            fips_num = state.state_id

            # let's get the list of senators/representatives from each state
            quorum_api = quorum_api.set_endpoint("person") \
                            .count(True) \
                            .offset(20) \
                            .filter(most_recent_state = state_id, current=True) \
            members = quorum_api.GET()

            # construct a list of ids of the members from this state
            member_ids = [member.id for member in members]

            # add this list to the dictionary we are building, keyed by the state
            members_by_state[state_id] = member_ids

        return members_by_state

    def get_word_mentions_per_state(self, word):
        """
        get the number of documents that the given word is mentioned in each state.
        Write this to the data.csv file that will then be used
        """
        # get the dictionary of lists of members from each state
        members_by_state = getMembersByState()

        # this is the dictionary that will be populated with the number of word mentions per state
        mentions_per_state = {}
        quorum_api = QuorumAPI(username="gwc", api_key="691e43c415d88cd16286edb1f78abb2e348688da")
        quorum_api = quorum_api.set_endpoint("document") \
                            .count(True) \
                            .offset(20) \
        # iterate over the lists in our dictionary, keyed by state
        for state, member_lst in members_by_state.iteritems():
            comma_id_lst = ','.join(map(str, member_lst))
            # get all documents which mention the desired word from the state in question
            quorum_api = quorum_api.filter(advanced_search = word, source_members = member_lst)
            results = quorum_api.GET()

            # store the number of documents for this state
            mentions_per_state[state] = results['meta'].total_count

        save_csv(mentions_per_state)









