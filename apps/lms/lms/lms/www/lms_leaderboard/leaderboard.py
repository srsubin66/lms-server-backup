# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
import frappe
from frappe import _

def get_context(context):
    context.no_cache = 1
    context.show_sidebar = True
    
    # Add page title and breadcrumbs
    context.title = _("LMS Leaderboard")
    context.parents = [
        {"name": _("Home"), "route": "/"},
        {"name": _("LMS"), "route": "/lms"}
    ]
    
    # Add navigation context
    context.navigation_links = [
        {"name": _("Courses"), "route": "/lms/courses"},
        {"name": _("Batches"), "route": "/lms/batches"},
        {"name": _("Certified Participants"), "route": "/lms/certified-participants"},
        {"name": _("Jobs"), "route": "/lms/jobs"},
        {"name": _("Statistics"), "route": "/lms/statistics"},
        {"name": _("Leaderboard"), "route": "/lms/leaderboard", "active": True},
    ]
    
    try:
        # Add statistics data with error handling
        context.stats = {
            "courses": frappe.db.count("LMS Course") or 0,
            "signups": frappe.db.count("User", {"enabled": 1}) or 0,
            "enrollments": frappe.db.count("LMS Enrollment") or 0,
            "completions": frappe.db.count("LMS Enrollment", {"progress": 100}) or 0,
            "milestones": frappe.db.count("LMS Course Progress") or 0
        }
    except Exception as e:
        frappe.log_error(f"Error fetching leaderboard stats: {str(e)}")
        context.stats = {
            "courses": 0,
            "signups": 0,
            "enrollments": 0,
            "completions": 0,
            "milestones": 0
        }
    
    return context

def has_permission(doc, ptype, user):
    # Allow access to everyone, including guests
    return True

def has_website_permission(doc, ptype, user):
    # Allow access to everyone, including guests
    return True

@frappe.whitelist()
def get_leaderboard_config():
	leaderboard_config = frappe._dict()
	leaderboard_hooks = frappe.get_hooks("leaderboards")
	for hook in leaderboard_hooks:
		leaderboard_config.update(frappe.get_attr(hook)())

	return leaderboard_config