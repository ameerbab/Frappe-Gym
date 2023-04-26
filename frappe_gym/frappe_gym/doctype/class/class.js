frappe.ui.form.on("Class", {
    refresh(frm) {
        if(!frm.is_dirty()) {
        frm.add_custom_button(
            "Add Booking",
            () => {
                let dialog = new frappe.ui.Dialog({
                    title: "Select Member to Book",
                    fields: [
                        {
                            fieldtype: "Link",
                            fieldname: "member",
                            label: "Member",
                            options: "Member",
                        },
                    ],
                    primary_action_label: "Book Class",
                    primary_action: (data) => {
                        data.class_data=cur_frm.doc.name
                       frappe.new_doc("Class Booking", {
                            class: frm.doc.class,
                            member: data.member,
                            class_data:data.class_data,
                            status: "Confirmed"
                        });
                    },
                });

                dialog.show();
            },
        );
        }
    },
});
