from enum import Enum


class RoleType(Enum):
    senator = 1
    representative = 2


class BillType(Enum):
    senate_bill = 2
    house_bill = 3
    senate_resolution = 4
    house_resolution = 1
    senate_concurrent_resolution = 6
    house_concurrent_resolution = 5
    senate_joint_resolution = 8
    house_joint_resolution = 7


class BillStatus(Enum):
    introduced = 1
    out_of_committee = 2
    passed_first = 3
    passed_second = 4
    to_executive = 5
    enacted = 6

    at_least_out_of_committee = (out_of_committee, passed_first, passed_second, to_executive, enacted)
    at_least_passed_first = (passed_first, passed_second, to_executive, enacted)
    at_least_passed_second = (passed_second, to_executive, enacted)
    at_least_to_executive = (to_executive, enacted)
    at_least_enacted = (enacted,)

class DocumentType(Enum):
    press_release = 5
    floor_statement = 7
    dc_letter = 10
    tweet = 6
    facebook_post = 9
    constituent_email = 24