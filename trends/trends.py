# this sets your path correctly so the imports work
from api import QuorumAPI
from enums import BillType, BillStatus
import sys
import os
import json
sys.path.insert(1, os.path.dirname(os.getcwd()))


class LegislativeTrendViewer():

    # OLD CONGRESS is a final variable to indicate earliest legislative session
    OLD_CONGRESS = 101
    quorum_api = QuorumAPI(
        username="gwc",
        api_key="691e43c415d88cd16286edb1f78abb2e348688da"
    )

    def grab_bills_in_legislative_sessions(self):
        ''' Function to get bills at different statuses in
            legislative sessions '''

        # query for legisliatve session
        legislative_sessions = self.quorum_api.set_endpoint('legsession')\
            .filter(number__gte=self.OLD_CONGRESS).GET()['objects']

        # TODO: initialize empty list

        # TODO: loop through legislative sessions

            # initializing dictionary with key Congress associated
            # with number of the congress

            single_entry = {'Congress': session['number']}

            all_bills =  # TODO: looking at bills filtered by house by session

            # TODO: filtering for various levels of BillStatus
            # Introduced, At Least Out of Committee, At Least Passed House,
            # At Least Passed Senate, At Least to Executive, Enacted

            single_entry['Introduced'] = all_bills.filter(
                # TODO: filter by introduced bills
            ).GET()['meta']['total_count']

            # adding to dictionary

        # return json of dictionary
        return json.dumps(dict_list)


