from . import __version__ as app_version
from frappe import __version__ as frappe_version

app_name = "clefincode_erp"
app_title = "ClefinCode ERP"
app_publisher = "ClefinCode L.L.C-FZ"
app_description = """Boost ERPNext with efficient tools & mobile apps"""
app_email = "info@clefincode.com"
app_license = "GNU General Public License (v3)"
guest_title = app_title
is_frappe_above_v13 = int(frappe_version.split('.')[0]) > 13

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/clefincode_erp/css/clefincode_erp.css"
# app_include_js = "/assets/clefincode_erp/js/clefincode_erp.js"

# include js, css files in header of web template
web_include_css = ['clefincode_erp.bundle.css'] if is_frappe_above_v13 else [
    '/assets/css/clefincode_erp.css']

web_include_js = ['clefincode_erp.bundle.js'] if is_frappe_above_v13 else [
    '/assets/js/clefincode_erp.js']

# include js, css files in header of desk.html
app_include_css = ['clefincode_erp.bundle.css'] if is_frappe_above_v13 else [
    '/assets/css/clefincode_erp.css']

app_include_js = ['clefincode_erp.bundle.js' , 'override.bundle.js'] if is_frappe_above_v13 else [
    '/assets/js/clefincode_erp.js' ,  '/assets/js/override.js']

# web_include_css = "/assets/clefincode_erp/css/clefincode_erp.css"
# web_include_js = "/assets/clefincode_erp/js/clefincode_erp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "clefincode_erp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}
page_js ={"chat-portal" : "public/js/chat_portal/chat_portal.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "clefincode_erp.utils.jinja_methods",
#	"filters": "clefincode_erp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "clefincode_erp.install.before_install"
after_install = "clefincode_erp.setup.install.after_install"
after_migrate  = "clefincode_erp.setup.after_migrate.after_migrate"
# Uninstallation
# ------------

# before_uninstall = "clefincode_erp.uninstall.before_uninstall"
# after_uninstall = "clefincode_erp.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "clefincode_erp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
doc_events = {
	"Contact": {
		"after_insert": "clefincode_erp.api.api_1_0_1.api.sync_with_chat_profile",
        "on_update" : "clefincode_erp.api.api_1_0_1.api.sync_with_chat_profile"
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"clefincode_erp.tasks.all"
#	],
#	"daily": [
#		"clefincode_erp.tasks.daily"
#	],
#	"hourly": [
#		"clefincode_erp.tasks.hourly"
#	],
#	"weekly": [
#		"clefincode_erp.tasks.weekly"
#	],
#	"monthly": [
#		"clefincode_erp.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "clefincode_erp.install.before_tests"

# Overriding Methods
# ------------------------------
override_whitelisted_methods = {
    "frappe.desk.form.load.getdoc": "clefincode_erp.desk.custom_load.getdoc",}
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "clefincode_erp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "clefincode_erp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"clefincode_erp.auth.validate"
# ]

sounds = [
    {'name': 'chat-notification', 'src': '/assets/clefincode_erp/sounds/chat-notification.mp3', 'volume': 0.2},
    {'name': 'chat-message-send', 'src': '/assets/clefincode_erp/sounds/chat-message-send.mp3', 'volume': 0.2},
    {'name': 'chat-message-receive', 'src': '/assets/clefincode_erp/sounds/chat-message-receive.mp3', 'volume': 0.5}
]