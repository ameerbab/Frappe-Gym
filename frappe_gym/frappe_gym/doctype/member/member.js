frappe.ui.form.on("Member", {
    full_name_concate:function(frm){
        frm.set_value("full_name", frm.doc.first_name +" "+frm.doc.last_name)
     },
    last_name:function(frm){
         frm.trigger('full_name_concate')
     },
    refresh: function (frm) {
        if(frm.doc.__islocal != 1){
         frm.add_custom_button(
                "Create Membership",
                () => {
                    let dialog = new frappe.ui.Dialog({
                        title: "Select Plan",
                        fields: [
                            {
                                fieldtype: "Select",
                                fieldname: "plan",
                                label: "Plan",
                                options: "Monthly\n Six-month\nAnnually",
                            },
                            
                        ],
                        primary_action_label: "Create Plan",
                        primary_action: (data) => {
                           frappe.new_doc("Gym Membership", {
                                member: frm.doc.name,
                                plan: data.plan,
                                
                            });
                        },
                    });
                    dialog.show();
                },
            );
         frm.add_custom_button(
                "Create Subscription Plan",
                () => {
                    let dialog = new frappe.ui.Dialog({
                        title: "Subscription Plan",
                        fields: [
                            {
                                fieldtype: "Link",
                                fieldname: "member",
                                label: "Member",
                                options: "Member",
                            } ],
                        primary_action_label: "Create Plan",
                        primary_action: (data) => {
                           frappe.new_doc("Subscription Gym", {
                                member: data.member,
                             });
                        },
                    });
                    dialog.show();
                },
            );
         frm.add_custom_button(
                "Professional Trainer Plan",
                () => {
                    let dialog = new frappe.ui.Dialog({
                        title: "Professional Trainer Plan",
                        fields: [
                            {
                                fieldtype: "Link",
                                fieldname: "member",
                                label: "Member",
                                options: "Member",
                            },
                            ],
                        primary_action_label: "Create Plan",
                        primary_action: (data) => {
                           frappe.new_doc("Professional Trainer Plan", {
                                member: data.member,
                                 });
                        },
                    });
                    dialog.show();
                },
            );
         }
    }
})
