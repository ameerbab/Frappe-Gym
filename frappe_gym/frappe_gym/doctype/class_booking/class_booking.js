cur_frm.add_fetch("class_data", "class_time", "class_time")
frappe.ui.form.on("Class Booking", {
	validate: function (frm) {
		frappe.call({
			method: "frappe_gym.frappe_gym.doctype.class_booking.class_booking.validate_booking",
			args: {
				'capacity': frm.doc.slot_capacity,
				"class_data": frm.doc.class_data
			},
			callback: function (r) {
				frm.set_value('available_slots', r.message)
			}
		})
	},
	class_data: function (frm) {
		frappe.call({
			method: "frappe_gym.frappe_gym.doctype.class_booking.class_booking.get_trainer",
			args: { 'class_data': frm.doc.class_data },
			callback: function (r) {
				frm.set_value("trainer", r.message)
			}
		})

	},
	select_day: function (frm) {
		frappe.call({
			method: "frappe_gym.frappe_gym.doctype.gym_workout_plan.gym_workout_plan.get_workout_data",
			args: { 'select_day': frm.doc.select_day, 'plan_name': frm.doc.plan_name },
			callback: function (r) {
				console.log(r)
			}
		})
	},
})