frappe.pages["member-profile-page"].refresh= function (wrapper) {
	frappe.require("member_profile_details_controller.js", () => {
		let user_profile = new frappe.ui.UserProfile(wrapper);
		user_profile.show();
	});
};
