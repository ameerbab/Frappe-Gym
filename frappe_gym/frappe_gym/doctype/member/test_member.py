import frappe
import unittest
from frappe.tests.utils import FrappeTestCase
from frappe.utils import getdate
from frappe.tests.test_commands import BaseTestCommands
def create_doc():
	doc=frappe.new_doc("Member")
	doc.first_name="ashish"
	doc.last_name="koladiya"
	doc.sex="Male"
	doc.dob=getdate()
	doc.email="test@gmail.com"
	doc.mobile="9999999999"
	doc.invite_user=False
	doc.insert(doc)

def get_data_list(full_name):
	frappe.db.get_list("Member",{'full_name':full_name},['name'])

	
class TestMember(unittest.TestCase):
	def setUp(self) -> None:
		create_doc()
	def test_data_list(self) -> None:
		get_data_list("jeel viradiya")
		

class TestCommands(BaseTestCommands,unittest.TestCase):
	def test_execute(self):
		self.execute("bench --site gym_management.finbyz.com execute frappe_gym.frappe_gym.doctype.member.test_member.TestMember.setUp.create_doc")
		self.execute("bench --site gym_management.finbyz.com execute frappe_gym.frappe_gym.doctype.member.test_member.TestMember.test_data_list.get_data_list")