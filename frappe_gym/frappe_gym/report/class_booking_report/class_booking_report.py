import frappe
from frappe import _, scrub
from frappe.utils import add_days, add_to_date, flt, getdate
from six import iteritems

from erpnext.accounts.utils import get_fiscal_year


def execute(filters=None):
	return Analytics(filters).run()

class Analytics(object):
	def __init__(self, filters=None):
		self.filters = frappe._dict(filters or {})
		
	def run(self):
		self.get_columns()
		self.get_data()
		self.get_chart_data()

		
		skip_total_row = 1

	   
		return self.columns, self.data, None, self.chart

	def get_columns(self):
		self.columns = [
			
			{
				"label": _("Class"),
				"fieldname": "class_data",
				"fieldtype": "Data",
				"options":"Class",
				"width": 140,
			},
			{
				"label": _("Status"),
				"fieldname": "status",
				"fieldtype":"Select",
				"options":"Confirmed\nCancelled\nWaitlisted",
				"width": 140,
			},
			{
				"label":_("Class Name"),
				"fieldname":"class_name",
				"fieldtype":"Data",
				"width":140,
			},
			{
				"label":_("Class Type"),
				"fieldname":"class_type",
				"fieldtype":"Select",
				"width":140,
			},
			{
				"label":_("Member"),
				"fieldname":"member",
				"fieldtype":"Link",
				"options":"Member",
				"width":140,
			}
			
		]
		

	def get_data(self):
		self.get_gym_members()
		self.get_rows()

	def get_gym_members(self):

		self.entries = frappe.db.sql(
			"""
			SELECT 
			   c.class_name,c.class_type,cb.status,cb.class_data,cb.member,m.full_name
			FROM
				`tabClass` as c,`tabClass Booking` as cb,`tabMember` as m
			WHERE
			   cb.class_name=c.class_name and cb.full_name=m.full_name
			""",
			as_dict=1,
		)
		
		
	def get_rows(self):
		self.data = []
		count=0
		
		for d in self.entries:
			
			member = self.filters.get('member')
			member_name = frappe.db.get_value("Member", member, "full_name")
			class_name = self.filters.get('class')
			
			if class_name==d['class_data']:
				row={
					"class_name":d.class_name,
					"class_type":d.class_type,
					"class_data":d.class_data,
					"status":d.status,
					"member":d.full_name,
				}
				
				count=count+1
				# frappe.msgprint(str(count))
				row.update({'count':count})
				self.data.append(row)
		
			# else:
			# 	row={
			# 		"class_name":d.class_name,
			# 		"class_type":d.class_type,
			# 		"class_data":d.class_data,
			# 		"status":d.status,
			# 		"member":d.full_name,
			# 	}
			
				# self.data.append(row)
				
				

   
	def get_chart_data(self):
		# length = len(self.columns)
		# rows=[d for d in self.data]
		labels = []
		total_members=[]
		total_mem = {}
		for row in self.entries:
			if row.class_name not in labels:
				labels.append(row.class_name)
				total_mem.update({row.class_name:1})
			if total_mem.get(row.class_name):
				total_mem[row.class_name] += 1
				
				
	
		datasets = []
		for row in total_mem:
			total_members.append(total_mem[row]-1)
		datasets.append(
		{
			"name": "Total Members",
			"values": total_members,
		}
	)
		# frappe.msgprint(str(datasets))
		# frappe.msgprint(str(total_mem))
		self.chart = {"data": {"labels": labels, "datasets": datasets},"type": "donut"}
		
		