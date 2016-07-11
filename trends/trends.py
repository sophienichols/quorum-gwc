# this sets your path correctly so the imports work
import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))

from api import QuorumAPI
from enums import BillType, BillStatus

# grab all the legsessions at the federal level

# then for each legsession, store the count of house bills at each level

# return a list of dictionaries of the format:
# [
#   {"congress": 112, "Bills Introduced": 46, "Bills Out Of Committee": 21, ...},
# ]
