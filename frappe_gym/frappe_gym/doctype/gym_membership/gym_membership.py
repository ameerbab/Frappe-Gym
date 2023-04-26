import frappe
from frappe.utils import getdate, date_diff
from frappe.model.document import Document

class GymMembership(Document):
	@property
	def contract_status(self):
		return get_contract_status(self.start_date, self.end_date)
@frappe.whitelist()
def get_contract_status(start_date, end_date):
	today = getdate()
	end = getdate(end_date)
	start = getdate(start_date)
	if end < today:
		return "Expired"
	elif start > today:	
		return "Not Started"
	else:
		return "Active"	
@frappe.whitelist()
def get_daysleft_in_plan(start_date,end_date):
	start_date= getdate()
	days_left=date_diff(end_date,start_date)
	return days_left
	