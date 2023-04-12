frappe.query_reports["Fitness Journey"] = {
	"filters": [
		
		{
            fieldname:"member",
			label:__("Member"),
			fieldtype:"Link",
			options:"Member",
		},
		
		
		
	],
	after_datatable_render: function(datatable_obj) {
		$(datatable_obj.wrapper).find(".dt-row-0").find('input[type=checkbox]').click();
	},
	get_datatable_options(options) {
		return Object.assign(options, {
			checkboxColumn: true,
			events: {
				onCheckRow: function (data) {

					console.log(data)
					
					
					const data_doctype = "doctype"
					
					row_name = data[3].content;
					console.log(row_name)
					length = data.length-1;

				
					row_values = data
						.slice(5, length )
						.map(function (column) {
							return column.content;
						});
						
				    console.log(row_values)

					entry = {
						name: row_name,
						values: row_values,
					};
					console.log(entry)

					let raw_data = frappe.query_report.chart.data;
					console.log(raw_data)
					let new_datasets = raw_data.datasets;
                    console.log(new_datasets)
					let element_found = new_datasets.some((element, index, array)=>{
						if(element.name == row_name){
							array.splice(index, 1)
							return true
						}
						return false
					})

					if (!element_found) {
						new_datasets.push(entry);
					}

					let new_data = {
						labels: raw_data.labels,
						datasets: new_datasets,
					};
					console.log(new_data)
					chart_options = {
						data: new_data,
						type: "line",
					};
					frappe.query_report.render_chart(chart_options);

					frappe.query_report.raw_chart_data = new_data;
				},
			},
		});
	},
}