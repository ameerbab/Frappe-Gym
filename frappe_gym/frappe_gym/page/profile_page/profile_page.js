frappe.pages["profile-page"].on_page_load = function (wrapper) {
	frappe.require("profile_page_controller.bundle.js", () => {
		let user_profile = new frappe.ui.UserProfile(wrapper);
		user_profile.show();
	});
};
