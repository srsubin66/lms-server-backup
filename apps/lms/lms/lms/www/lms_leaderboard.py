import frappe
from frappe import _

def get_context(context):
    context.no_cache = 1
    context.show_sidebar = True
    
    # Add navigation context similar to statistics
    context.navigation_links = [
        {"name": _("Courses"), "route": "/lms/courses"},
        {"name": _("Batches"), "route": "/lms/batches"},
        {"name": _("Certified Participants"), "route": "/lms/certified-participants"},
        {"name": _("Jobs"), "route": "/lms/jobs"},
        {"name": _("Statistics"), "route": "/lms/statistics"},
        {"name": _("Leaderboard"), "route": "/lms/leaderboard", "active": True},
    ]
    
    # Add statistics data
    context.stats = {
        "courses": frappe.db.count("LMS Course"),
        "signups": frappe.db.count("User", {"enabled": 1}),
        "enrollments": frappe.db.count("LMS Enrollment"),
        "completions": frappe.db.count("LMS Enrollment", {"progress": 100}),
        "milestones": frappe.db.count("LMS Course Progress")
    }
    
    return context 