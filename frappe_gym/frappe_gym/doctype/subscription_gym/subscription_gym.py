import frappe
from frappe.model.document import Document
from frappe.utils import getdate, date_diff

class SubscriptionGym(Document):
	pass

@frappe.whitelist()
def get_daysleft_in_plan(start_date,end_date):
	start_date= getdate()
	days_left=date_diff(end_date,start_date)
	return days_left
	
@frappe.whitelist()
def get_total_plan_day(start_date,end_date):
    days=date_diff(end_date,start_date)
    return days

