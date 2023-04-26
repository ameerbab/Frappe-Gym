var locker_start_time=cur_frm.add_fetch('locker_name','start_time','l_start_time')
var locker_end_time=cur_frm.add_fetch('locker_name','end_time','l_end_time')
frappe.ui.form.on('Locker Booking',{
    validate:function(frm){
      frappe.call({
        method: "frappe_gym.frappe_gym.doctype.locker_booking.locker_booking.validate_locker_availability",
        args:{
           'locker_start_time':frm.doc.l_start_time,
           'locker_end_time':frm.doc.l_end_time,
           'start_time':frm.doc.start_time,
           'end_time':frm.doc.end_time,
           'date_of_booking':frm.doc.date_of_booking,
           },
        callback:function(r){
                 console.log(r.message)
        }
      })
       
    },
    date_of_booking:function(frm){
      frappe.call({
        method:"frappe_gym.frappe_gym.doctype.locker_booking.locker_booking.validate_no_of_lockers",
        args:{'no_of_lockers':frm.doc.no_of_lockers,'locker_name':frm.doc.locker_name},
        callback:function(r){
         cur_frm.set_value("no_of_lockers",r.message)
         
        }
      })
    }
})