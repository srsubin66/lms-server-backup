# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
import frappe
def has_permission(doc, ptype, user):
    # Allow access to everyone who is logged in
    return frappe.session.user != 'Guest'


def has_website_permission(doc, ptype, user):
    return True 

@frappe.whitelist()
def get_leaderboard_config():
	leaderboard_config = frappe._dict()
	leaderboard_hooks = frappe.get_hooks("leaderboards")
	for hook in leaderboard_hooks:
		leaderboard_config.update(frappe.get_attr(hook)())

	return leaderboard_config


def has_permission():
	"""Allow all users to access the leaderboard"""
	return True

def has_website_permission():
	"""Allow all website users to access the leaderboard"""
	return True