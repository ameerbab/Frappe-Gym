import frappe
from frappe.tests.utils import FrappeTestCase
class TestGymSettings(FrappeTestCase):
	def check_gym_configuration_has_been_set(self):
		settings = frappe.get_doc("Gym Settings")
		self.assertIsNotNone(settings.email)

