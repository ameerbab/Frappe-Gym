frappe.ui.form.on("Gym Membership", {
    start_date: function (frm) {
        if(frm.doc.plan=='Monthly'){
        frm.set_value(
            "end_date",
            frappe.datetime.add_days(frm.doc.start_date,30)
        );
        frm.set_value("price",600)
        }
        if(frm.doc.plan=='Six-month'){
            frm.set_value(
                "end_date",
                frappe.datetime.add_days(frm.doc.start_date,180)
            );
            frm.set_value("price",1200)
            }
            if(frm.doc.plan=='Annually'){
                frm.set_value(
                    "end_date",
                    frappe.datetime.add_days(frm.doc.start_date,365)
                );
                frm.set_value("price",1800)
                }
            frappe.call({
                method:"frappe_gym.frappe_gym.doctype.gym_membership.gym_membership.get_daysleft_in_plan",
                args:{'start_date':frm.doc.start_date,'end_date':frm.doc.end_date},
                callback:function(r){
                    cur_frm.set_value("days_left",r.message)
                }
            })
                
    },
    plan:function(frm){
        if(frm.doc.plan=='Monthly'){
            
            frm.set_value("price",600)
            }
            if(frm.doc.plan=='Six-month'){
              frm.set_value("price",1200)
                }
                if(frm.doc.plan=='Annually'){
                  
                    frm.set_value("price",1800)
                    }
    },
    refresh: function (frm) {
        frm.set_query("plan", function () {
            return {
                filters: {
                    active: 1,
                },
            }
        })
        frm.set_query("trainer", function () {
            return {
                filters: {
                    active: 1,
                },
            }
        })
    },
   

});
