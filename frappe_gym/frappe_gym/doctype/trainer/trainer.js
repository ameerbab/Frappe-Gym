frappe.ui.form.on("Trainer", {
    
    full_name_concate:function(frm){
       frm.set_value("full_name", frm.doc.first_name +" "+frm.doc.last_name)
    },
   
    last_name:function(frm){
        frm.trigger('full_name_concate')
    },
    validate:function(frm){
        if(frm.doc.docstatus=="Draft" || frm.doc.docstatus=="Submitted"){
            cur_frm.set_value("active",1)
        }
        else{
            cur_frm.set_value("active",0)
        }
       
    }
});
