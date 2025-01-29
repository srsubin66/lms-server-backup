import frappe

def has_permission(doc=None, user=None, doctype=None):
    """
    Allow all users to access the leaderboard regardless of the doctype
    """
    return True

def has_website_permission(doc=None, user=None, doctype=None):
    """
    Allow all website users to access the leaderboard regardless of the doctype
    """
    return True


@frappe.whitelist()
def get_leaderboard_config():
    leaderboard_config = frappe._dict()
    leaderboard_hooks = frappe.get_hooks("leaderboards")
    for hook in leaderboard_hooks:
        leaderboard_config.update(frappe.get_attr(hook)())
        
    return leaderboard_config
