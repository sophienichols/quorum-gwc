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

        # looking at legislative sessions
        legislative_sessions = self.quorum_api.set_endpoint('legsession')\
            .filter(number__gte=self.OLD_CONGRESS).GET()['objects']

        # initializing list of dictionaries to empty list
        dict_list = []
        for session in legislative_sessions:
            # initializing dictionary with key Congress associated with
            # number of the congress
            single_entry = {'Congress': session['number']}

            # looking at bills filtered by house by session
            all_bills = self.quorum_api.set_endpoint('bill')\
                .filter(bill_type=BillType.house_bill,
                        session=session['id'])

            # filtering for various levels of BillStatus
            single_entry['Introduced'] = all_bills.filter(
                current_general_status__in=BillStatus.at_least_introduced
            ).GET()['meta']['total_count']

            single_entry['Bills Out Of Committee'] = all_bills.filter(
                current_general_status__in=BillStatus.at_least_out_of_committee
            ).GET()['meta']['total_count']

            single_entry['At Least Passed House'] = all_bills.filter(
                current_general_status__in=BillStatus.at_least_passed_first
            ).GET()['meta']['total_count']

            single_entry['At Least Passed Senate'] = all_bills.filter(
                current_general_status__in=BillStatus.at_least_passed_second
            ).GET()['meta']['total_count']

            single_entry['At Least To Executive'] = all_bills.filter(
                current_general_status__in=BillStatus.at_least_to_executive
            ).GET()['meta']['total_count']

            single_entry['Enacted'] = all_bills.filter(
                current_general_status__in=BillStatus.at_least_enacted
            ).GET()['meta']['total_count']

            # adding to dictionary
            dict_list.append(single_entry)

        # return json of dictionary
        return json.dumps(dict_list)


