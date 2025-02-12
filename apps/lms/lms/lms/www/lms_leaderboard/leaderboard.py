# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
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