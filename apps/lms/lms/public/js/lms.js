window.updateProgress = function() {
    frappe.call({
        method: "frappe.client.get",
        args: {
            doctype: "LMS Enrollment",
            filters: {
                course: frappe.course_name,
                member: frappe.session.user,
                member_type: "Student"
            }
        },
        callback: function(r) {
            if(r.message) {
                let progress = r.message.progress || 0;
                // Update progress display
                $('.course-progress').text(Math.round(progress) + '%');
                $('.progress-bar').css('width', progress + '%');
            }
        }
    });
}; 