import frappe
from frappe import _
from frappe.model.document import Document
class Trainer(Document):
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
                ).format(frappe.bold(users[0].email), frappe.bold(users[0].mobile)),
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
        user.add_roles("Gym Trainer")
        self.db_set("user_id", user.name)

    def on_update(self):
        if not self.user_id and self.email and self.invite_user:
            self.create_website_user()	
    
    def activestatus(self):
        if self.docstatus==0 or self.docstatus==1:
            frappe.db.set_value("Trainer","active",1)
        else:
            frappe.db.set_value("Trainer","active",0)
        
    def on_save(self):
        self.activestatus()


