# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
import frappe

def has_permission(doc, ptype, user):
    # Allow access to everyone who is logged in
    if frappe.session.user == 'Guest':
        return False
        
    # Check if user is either a system user or has an LMS enrollment
    return (frappe.session.user == 'Administrator' 
            or frappe.db.exists('User', {'name': frappe.session.user, 'user_type': 'System User'})
            or frappe.db.exists('LMS Enrollment', {'user': frappe.session.user}))

def has_website_permission(doc, ptype, user):
    # Allow access to logged-in users with LMS enrollment
    if frappe.session.user == 'Guest':
        return False
    
    return frappe.db.exists('LMS Enrollment', {'user': frappe.session.user})

@frappe.whitelist()
def get_leaderboard_config():
	leaderboard_config = frappe._dict()
	leaderboard_hooks = frappe.get_hooks("leaderboards")
	for hook in leaderboard_hooks:
		leaderboard_config.update(frappe.get_attr(hook)())

	return leaderboard_config