# Copyright (c) 2022, Warren Eiserman and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class ClassBooking(WebsiteGenerator):
	def before_save(self):
		if not self.route:
			self.route = f"/{self.name}"
@frappe.whitelist()
def validate_booking(capacity,class_data):
	slot_available=int(capacity)-1
	if int(slot_available) <=0:
		frappe.throw("slots is not available for this class")
	
	frappe.db.sql(f"""UPDATE `tabClass` SET available_capacity={slot_available} WHERE name='{class_data}';""")
	return int(slot_available)
    
	
	   