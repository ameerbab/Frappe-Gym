frappe.ui.form.on("Class Booking", {
	validate:function(frm) {
	   
	   
	   frappe.call({
		method:"frappe_gym.frappe_gym.doctype.class_booking.class_booking.validate_booking",
		args:{'capacity':frm.doc.slot_capacity,
	    "class_data":frm.doc.class_data},
		callback:function(r){
			console.log(r)
			frm.set_value('available_slots',r.message)
	
			

			
			
			

		}
	})
	}})



	
