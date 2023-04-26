frappe.ui.form.on('Attendence', {
    send_email:function(frm){
    frappe.call({
            method:"frappe_gym.frappe_gym.doctype.attendence.attendence.send_weekly_data",
            args:{'full_name':frm.doc.full_name},
            callback:function(r){
                console.log(r)
            }
            
        })

    } 
});
