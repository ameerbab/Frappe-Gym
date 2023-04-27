from datetime import datetime 
import frappe
from frappe.website.website_generator import WebsiteGenerator

class LockerBooking(WebsiteGenerator):
	pass
@frappe.whitelist()
def validate_locker_availability(locker_start_time,locker_end_time,slot_time):
	lstarttime=locker_start_time[:2]
	lendtime=locker_end_time[:2]
	sst=slot_time[:2]
	if int(sst)<int(lstarttime) or int(sst)>=int(lendtime):
		frappe.throw(f"plz enter the slot time between {locker_start_time} and {locker_end_time} ")

@frappe.whitelist()
def validate_no_of_lockers(no_of_lockers,locker_name):
	locker_data=frappe.db.get_value("Locker Details",locker_name,'locker_name')
	lockers=int(no_of_lockers)-1
	if int(lockers) < 1:
		frappe.throw("locker is not available for this date Plz choose another date")
	frappe.db.sql(f"""UPDATE `tabLocker Details` SET no_of_lockers={lockers} WHERE locker_name='{locker_data}';""")
	return int(lockers)
	
