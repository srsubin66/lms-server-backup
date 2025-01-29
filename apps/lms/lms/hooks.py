from . import __version__ as app_version

app_name = "frappe_lms"
app_title = "Frappe LMS"
app_publisher = "Frappe"
app_description = "Frappe LMS App"
app_icon_url = "/assets/lms/images/lms-logo.png"
app_icon_title = "Learning"
app_icon_route = "/lms"
app_color = "grey"
app_email = "hello@subin.in"
app_license = "AGPL"

# Includes in <head>
# ------------------

app_include_js = [
    # ... other js files ...
    "/assets/lms/js/lms_leaderboard.js"
]

app_include_css = [
    # ... other css files ...
    "/assets/lms/css/lms_leaderboard.css"
]

web_include_css = "lms.bundle.css"
web_include_js = ["website.bundle.js"]


website_route_rules = [
    {"from_route": "/lms/<path:app_path>", "to_route": "lms"},
    {
        "from_route": "/courses/<course_name>/<certificate_id>",
        "to_route": "certificate",
    },
    {"from_route": "/app/lms_leaderboard/<doctype>", "to_route": "lms_leaderboard"},
    {"from_route": "/lms_leaderboard", "to_route": "lms_leaderboard"},
]

after_install = "lms.install.after_install"
after_sync = "lms.install.after_sync"
before_uninstall = "lms.install.before_uninstall"
setup_wizard_requires = "assets/lms/js/setup_wizard.js"


has_permission = {
    "Page": "lms.lms.page.lms_leaderboard.leaderboard.has_permission",
    "DocType": "lms.lms.page.lms_leaderboard.leaderboard.has_permission"
}


has_website_permission = {
    "Page": "lms.lms.page.lms_leaderboard.leaderboard.has_website_permission",
    "LMS Certificate Evaluation": "lms.lms.doctype.lms_certificate_evaluation.lms_certificate_evaluation.has_website_permission",
    "LMS Certificate": "lms.lms.doctype.lms_certificate.lms_certificate.has_website_permission",
}

override_doctype_class = {
    "User": "lms.overrides.user.CustomUser",
    "Web Template": "lms.overrides.web_template.CustomWebTemplate",
}

doc_events = {
    "*": {
        "on_change": [
            "lms.lms.doctype.lms_badge.lms_badge.process_badges",
        ]
    },
    "Discussion Reply": {"after_insert": "lms.lms.utils.handle_notifications"},
    "Notification Log": {"on_change": "lms.lms.utils.publish_notifications"},
}

scheduler_events = {
    "hourly": [
        "lms.lms.doctype.lms_certificate_request.lms_certificate_request.schedule_evals",
        "lms.lms.api.update_course_statistics",
    ],
    "daily": ["lms.job.doctype.job_opportunity.job_opportunity.update_job_openings"],
}

fixtures = ["Custom Field", "Function", "Industry", "LMS Category"]

website_redirects = [
    {"source": "/update-profile", "target": "/edit-profile"},
    {"source": "/courses", "target": "/lms/courses"},
    {
        "source": r"^/courses/.*$",
        "target": "/lms/courses",
    },
    {"source": "/batches", "target": "/lms/batches"},
    {
        "source": r"/batches/(.*)",
        "target": "/lms/batches",
        "match_with_query_string": True,
    },
    {"source": "/job-openings", "target": "/lms/job-openings"},
    {
        "source": r"/job-openings/(.*)",
        "target": "/lms/job-openings",
        "match_with_query_string": True,
    },
    {"source": "/statistics", "target": "/lms/statistics"},
    {"source": "/app/lms_leaderboard", "target": "/lms/lms_leaderboard"},
    {
        "source": r"/app/lms_leaderboard/(.*)",
        "target": "/lms/lms_leaderboard",
        "match_with_query_string": True,
    },
    {"source": "/lms_leaderboard", "target": "/lms/lms_leaderboard"},
    {
        "source": r"/lms_leaderboard/(.*)",
        "target": "/lms/lms_leaderboard",
        "match_with_query_string": True,
    },

]

update_website_context = [
    "lms.widgets.update_website_context",
]

jinja = {
    "methods": [
        "lms.lms.utils.get_signup_optin_checks",
        "lms.lms.utils.get_tags",
        "lms.lms.utils.get_lesson_count",
        "lms.lms.utils.get_instructors",
        "lms.lms.utils.get_lesson_index",
        "lms.lms.utils.get_lesson_url",
        "lms.page_renderers.get_profile_url",
        "lms.overrides.user.get_palette",
        "lms.lms.utils.is_instructor",
    ],
    "filters": [],
}

lms_markdown_macro_renderers = {
    "Exercise": "lms.plugins.exercise_renderer",
    "Quiz": "lms.plugins.quiz_renderer",
    "YouTubeVideo": "lms.plugins.youtube_video_renderer",
    "Video": "lms.plugins.video_renderer",
    "Assignment": "lms.plugins.assignment_renderer",
    "Embed": "lms.plugins.embed_renderer",
    "Audio": "lms.plugins.audio_renderer",
    "PDF": "lms.plugins.pdf_renderer",
}

page_renderer = [
    "lms.page_renderers.ProfileRedirectPage",
    "lms.page_renderers.ProfilePage",
    "lms.page_renderers.CoursePage",
    "lms.page_renderers.SCORMRenderer",
]

profile_url_prefix = "/users/"

signup_form_template = "lms.plugins.show_custom_signup"

on_session_creation = "lms.overrides.user.on_session_creation"

add_to_apps_screen = [
    {
        "name": "lms",
        "logo": "/assets/lms/images/lms-logo.png",
        "title": "Learning",
        "route": "/lms",
        "has_permission": "lms.lms.api.check_app_permission",
    }
]