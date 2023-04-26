
import frappe
from frappe.utils import cint, cstr, getdate
import dateutil
from frappe import _
from frappe.model.document import Document

class Member(Document):
	def set_full_name(self):
		if self.last_name:
			self.full_name = " ".join(filter(None, [self.first_name, self.last_name]))
		else:
			self.full_name = self.first_name
	def create_website_user(self):
		users = frappe.db.get_all(
			"User",
			fields=["email", "mobile_no"],
			or_filters={"email": self.email, "mobile_no": self.mobile},
		)
		if users and users[0]:
			frappe.throw(
				_(
					"User exists with Email {}, Mobile {}<br>Please check email / mobile or disable 'Invite as User' to skip creating User"
				).format(frappe.bold(users[0].email), frappe.bold(users[0].mobile_no)),
				frappe.DuplicateEntryError,
			)

		user = frappe.get_doc(
			{
				"doctype": "User",
				"first_name": self.first_name,
				"last_name": self.last_name,
				"email": self.email,
				"user_type": "Website User",
				"gender": self.sex,
				"mobile_no": self.mobile,
				"birth_date": self.dob,
			}
		)
		user.flags.ignore_permissions = True
		user.enabled = True
		user.send_welcome_email = False
		user.add_roles("Gym Member")
		self.db_set("user_id", user.name)
	def validate(self):
		self.set_full_name()
	def on_update(self):
		if not self.user_id and self.email and self.invite_user:
			self.create_website_user()	
 