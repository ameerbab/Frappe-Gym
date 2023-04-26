import frappe
from frappe.website.website_generator import WebsiteGenerator

class Class(WebsiteGenerator):
	def before_save(self):
		if not self.route:
			self.route = f"/{self.name}"
