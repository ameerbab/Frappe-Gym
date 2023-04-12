// Copyright (c) 2023, Eng. Omar M. K. Shehada and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Class Booking Report"] = {
	"filters": [
          
			// {
			// 	fieldname:"member",
			// 	label:__("Member"),
			// 	fieldtype:"Link",
			// 	options:"Member",
			// },
		    {
				fieldname: "class",
				fieldtype: "Link",
				label: "Class",
				options: "Class",
			},

	]
};
