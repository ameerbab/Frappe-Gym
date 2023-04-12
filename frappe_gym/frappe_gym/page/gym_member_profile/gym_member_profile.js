frappe.pages["gym-member-profile"].on_page_load = function (wrapper) {
	
		gym_member_profile = new GymMember(wrapper);
		gym_member_profile.show();
	};
;
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

    make_user_profile() {
	this.user = frappe.user_info(this.user_id);
	this.page.set_title(this.user.fullname);
	
	frappe.xcall("frappe_gym.frappe_gym.page.gym_member_profile.gym_member_profile.get_details", {
		"doctype":"Gym Membership",
		"user":frappe.session.user,
	})
	.then((r) => {
	    
		this.main_section.empty().append(
			frappe.render_template("gym_member", {
				message:r,
				
			})
		);
		
	})
	
	}
	
// 	on_page_load(){
// 	   frappe.call({
// 	   method:"frappe_gym.frappe_gym.page.gym_member_profile.gym_member_profile.get_details",
// 	   args:{'doctype':"Gym Membership","user":frappe.session.user},
// 	   callback:function(r){
		
// 		frappe.render_template("gym_member", {
// 			plan: r.message.plan,
// 			start_date: r.message.start_date
// 		});
		
// 	    console.log(r.message)
		
		
		
	   
	
// 	}
// })	
	

// }

	
		}