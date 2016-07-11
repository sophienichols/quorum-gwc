from enum import Enum

class RoleType(Enum):
	senator = 1
	representative = 2

class BillStatus(Enum):
	introduced = 1
	out_of_committee = 2
