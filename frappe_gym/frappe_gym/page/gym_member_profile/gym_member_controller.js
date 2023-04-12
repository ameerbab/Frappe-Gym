class GymMember {
	constructor(wrapper) {
		this.wrapper = $(wrapper);
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
		});
		this.sidebar = this.wrapper.find(".layout-side-section");
		this.main_section = this.wrapper.find(".layout-main-section");
		this.wrapper.bind("show", () => {
			this.show();
		});
	}
    
    show() {
		let route = frappe.get_route();
		this.user_id = route[1] || frappe.session.user;
		frappe.dom.freeze(__("Loading user profile") + "...");
		frappe.db.exists("User", this.user_id).then((exists) => {
			frappe.dom.unfreeze();
			if (exists) {
				this.make_user_profile();
			} else {
				frappe.msgprint(__("User does not exist"));
			}
		});
	}
}