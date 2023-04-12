import frappe

@frappe.whitelist()
def get_details(doctype,user):
    
    data=frappe.db.get_list(doctype,{'email':user},['plan','start_date','end_date','status','day_lefts'])
    return data