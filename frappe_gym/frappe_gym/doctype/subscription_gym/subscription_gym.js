frappe.ui.form.on('Subscription Gym', {
	end_date:function(frm){
	frappe.call({
		method:"frappe_gym.frappe_gym.doctype.subscription_gym.subscription_gym.get_daysleft_in_plan",
		args:{'start_date':frm.doc.start_date,'end_date':frm.doc.end_date},
		callback:function(r){
			cur_frm.set_value("days_left",r.message)
		}
	
	})
	frappe.call({
		method:"frappe_gym.frappe_gym.doctype.subscription_gym.subscription_gym.get_total_plan_day",
		args:{'start_date':frm.doc.start_date,'end_date':frm.doc.end_date},
		callback:function(r){
			cur_frm.set_value("plan_days",r.message)
		}
	
	})
},
   day_fee:function(frm){
	cur_frm.set_value("total_plan_days_fees",cur_frm.get_doc().plan_days*cur_frm.get_doc().day_fee)
   }
	

});
