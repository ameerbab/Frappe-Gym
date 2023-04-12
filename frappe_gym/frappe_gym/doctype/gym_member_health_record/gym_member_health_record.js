// Copyright (c) 2023, Eng. Omar M. K. Shehada and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Member Health Record', {
	onload:function(frm){
		if (frm.doc.__islocal == 1)
			frm.doc.health_stats=[]
	},
	 click_button: function(frm) {
		let a = frm.add_child("health_stats");
		a.bmi=(frm.doc.weight/(frm.doc.height*frm.doc.height))
		a.member=(frm.doc.member)
		a.height=frm.doc.height
		a.weight=frm.doc.weight
		a.signs_date=frappe.datetime.get_today()
		if (a.bmi>16 && a.bmi<18.5 )
		 	a.bmi_type="UnderWeight"
		else if (a.bmi>18.5 && a.bmi<25)
		 	a.bmi_type="Normal"
		else if (a.bmi>25 && a.bmi<30) 
	 		a.bmi_type="Overweight"
		else
		 	a.bmi_type="Obesity"
			
		frm.refresh_fields("health_stats");


	 }
});
