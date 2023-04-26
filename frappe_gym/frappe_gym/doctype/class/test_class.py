import frappe
from frappe.tests.utils import FrappeTestCase

def create_doc():
	doc=frappe.new_doc('Class')
	doc.class_name="Class 5"
	doc.class_type="Boxing and Kickboxing"
	doc.trainer="trainer-8998"
	doc.status="open"
	doc.class_date="20-04-2023"
	doc.class_time="10:31:42"
	doc.save()
	 
	 
class TestClass(FrappeTestCase):
	def setUp(self):
		create_doc()
