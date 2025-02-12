window.updateProgress = function() {
    frappe.call({
        method: "frappe.client.get",
        args: {
            doctype: "LMS Enrollment",
            filters: {
                course: frappe.course_name,
                member: frappe.session.user
            }
        },
        callback: function(r) {
            if(r.message) {
                let progress = r.message.progress || 0;
                // Update progress bar
                $('.course-progress-bar').css('width', progress + '%');
                $('.progress-value').text(Math.round(progress) + '%');
            }
        }
    });
} 