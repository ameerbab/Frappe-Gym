from datetime import datetime 
import frappe
from frappe.website.website_generator import WebsiteGenerator

class LockerBooking(WebsiteGenerator):
	pass
@frappe.whitelist()
def validate_locker_availability(date_of_booking,locker_start_time,locker_end_time,end_time,start_time):
	if locker_start_time >= start_time and locker_end_time < end_time :
		frappe.msgprint(f"plz enter start time and endtime between {locker_start_time} and {locker_end_time}")
	booking_list = frappe.db.get_list("Locker Booking", filters={'date_of_booking': date_of_booking}, fields=['date_of_booking','start_time', 'end_time'])
	booking_data={}
	for booking in booking_list:
			if booking['date_of_booking'] == booking_data.get('date_of_booking'):
				frappe.throw('plz choose another date for locker')
			else:
				booking_data.update({'date_of_booking':booking['date_of_booking']})
	
	
@frappe.whitelist()
def validate_no_of_lockers(no_of_lockers,locker_name):
	locker_data=frappe.db.get_value("Locker Details",locker_name,'locker_name')
	lockers=int(no_of_lockers)-1
	if int(lockers) < 1:
		frappe.throw("locker is not available for this date Plz choose another date")
	frappe.db.sql(f"""UPDATE `tabLocker Details` SET no_of_lockers={lockers} WHERE locker_name='{locker_data}';""")
	return int(lockers)
	