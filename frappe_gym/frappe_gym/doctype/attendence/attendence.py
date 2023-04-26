import frappe
from frappe.model.document import Document
from frappe.utils import add_to_date

class Attendence(Document):
    pass
@frappe.whitelist()
def send_weekly_data(full_name):
	row=frappe.db.get_list("Attendence",{'full_name':full_name},['class_name','email','class_type','full_name','select_day','present_or_absence','date'])
	message = """
				<table class="table table-bordered" style="margin: 0; font-size:100%;">
		<tr>
			<td>Class</td>
			<td>Class Type</td>
			<td>Member</td>
			<td>Day</td>
			<td>Status</td>
			<td>Date</td>
			
		</tr>"""
	for d in row:
		message +="""<tr>
			<td>{d.class_name}</td>
			<td>{d.class_type}</td>
			<td>{d.full_name}</td>
			<td>{d.select_day}</td>
			<td>{d.present_or_absence}</td>
			<td>{d.date}</td>
			</tr>
		""".format(d=d)
	message+="""</table>"""
	frappe.sendmail(recipients="jeelviradiya25@gmail.com",subject="weekly summary attendence",sender=frappe.session.user,message=message)
			   
				


			

		
