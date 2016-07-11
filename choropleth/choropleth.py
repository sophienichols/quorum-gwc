from api import QuorumAPI
from enums import RoleType
from enums import BillStatus

class ChoroplethVisualizer(object):
    quorum_api = QuorumAPI(username="gwc", api_key="691e43c415d88cd16286edb1f78abb2e348688da")
    quorum_api.set_endpoint("person")

    def getSingleStateData(self, state, filters):
        quorum_api = quorum_api.set_endpoint("person") \
                        .count(True) \
                        .limit(100) \
                        .offset(20) \
                        .filter(most_recent_role_type = RoleType.senator, current=True) \
        results = quorum_api.GET()

    # counts the instances of the given word in string
    def wordCountPerString(text, word):
   
    #def saveCsv():

    # create cache dictionary with lists of member ids keyed by state
    def getMembersByState(self):
        # the dictionary that we will populate with this info!
        members_by_state = {}

        # get state info
        quorum_api = quorum_api.set_endpoint("state") \
                        .count(True) \
                        .offset(20) \
        states = quorum_api.GET()

        for state in states:
            state_id = state.id
            fips_num = state.state_id
            quorum_api = quorum_api.set_endpoint("person") \
                            .count(True) \
                            .offset(20) \
                            .filter(most_recent_state = state_id, current=True) \
            members = quorum_api.GET()
            member_ids = [member.id for member in members]
            members_by_state[state_id] = member_ids

        return members_by_state

    def getDocumentMentionsPerMember(self, word):
        members_by_state = getMembersByState()
        quorum_api = quorum_api.set_endpoint("document") \
        for state, member_lst in members_by_state:
            quorum_api = quorum_api.count(True) \
                            .offset(20) \
                            .filter(advanced_search = word)








