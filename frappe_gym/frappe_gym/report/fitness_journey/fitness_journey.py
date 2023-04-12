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
                "label": _("Membership No"),
                "options": "Member",
                "fieldname": "membership_no",
                "fieldtype": "Link",
                "width": 140,
            },
            {
                "label": _("Member Name"),
                "fieldname": "full_name",
                "fieldtype": "Data",
                "width": 140,
            },
             {
                "label": _("Date"),
                "fieldname": "signs_date",
                "fieldtype":"Date",
                "width": 140,
            },
            {
                "label": _("Weight"),
                "fieldname": "weight",
                "fieldtype": "Float",
                "width": 140,
            },
            {
                "label": _("Height"),
                "fieldname": "height",
                "fieldtype": "Float",
                "width": 140,
            },
          
            {
                "label": _("BMI"),
                "fieldname": "bmi",
                "fieldtype": "Float",
                "width": 140,
            },
            {
                "label": _("BMI Type"),
                "fieldname": "bmi_type",
                "fieldtype": "Data",
                "width": 140,
            },
            
        ]
        

    def get_data(self):
        self.get_gym_members()
        self.get_rows()

    def get_gym_members(self):

        self.entries = frappe.db.sql(
            """
            SELECT 
                gmhr.membership_no, 
                gmhs.signs_date,
                gmhs.weight, 
                gmhs.height,
                gmhs.bmi,
                gmhs.bmi_type,
                m.name, m.first_name, m.last_name,m.full_name
            FROM
                `tabGym Member Health Status` as gmhs,`tabGym Member Health Record` as gmhr ,`tabMember` as m
            WHERE
                gmhr.member = m.name and gmhs.parent=gmhr.name
            """,
            as_dict=1,
        )
        
    def get_rows(self):
        self.data = []
        
        for d in self.entries:
            
            member = self.filters.get('member')
            member_name = frappe.db.get_value("Member", member, "full_name")
            if member_name==d['full_name']:
                row={
                    "membership_no":d.membership_no,
                    "full_name":d.full_name,
                    "weight":d.weight,
                    "height":d.height,
                    "bmi":d.bmi,
                    "bmi_type":d.bmi_type,
                    "signs_date":d.signs_date
                }
                
            
                self.data.append(row)

   
    def get_chart_data(self):
        length = len(self.columns)
        labels = [d.get("label") for d in self.columns[3:length-1]]
        
        self.chart = {"data": {"labels": labels, "datasets": []}, "type": "line"}

      