import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import cint


class ClassBooking(WebsiteGenerator):
    def before_save(self):
        if not self.route:
            self.route = f"/{self.name}"


@frappe.whitelist()
def validate_booking(capacity, class_data):
    slot_available = cint(capacity) - 1
    
    if int(slot_available) <= 0:
        frappe.throw("slots is not available for this class")

    frappe.db.sql(
        f"""UPDATE `tabClass` SET available_capacity={slot_available} WHERE name='{class_data}';"""
    )
    return cint(slot_available)


@frappe.whitelist()
def get_trainer(class_data):
    trainer = frappe.db.get_value("Class", class_data, "trainer")
    trainer_name = frappe.db.get_value("Trainer", trainer, "full_name")
    return trainer_name
