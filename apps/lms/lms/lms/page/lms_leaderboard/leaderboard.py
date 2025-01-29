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
def get_leaderboard_data():
    """
    Function to get leaderboard data - implement your logic here
    """
    return True