# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "jiqm_test"
app_title = "JIQM_Test"
app_publisher = "frappe"
app_description = "Articles"
app_icon = "octicon octicon-book"
app_color = "#589494"
app_email = "mohammad@meritsystems.com"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jiqm_test/css/jiqm_test.css"
# app_include_js = "/assets/jiqm_test/js/jiqm_test.js"

# include js, css files in header of web template
# web_include_css = "/assets/jiqm_test/css/jiqm_test.css"
# web_include_js = "/assets/jiqm_test/js/jiqm_test.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

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

# Website user home page (by function)
# get_website_user_home_page = "jiqm_test.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "jiqm_test.install.before_install"
# after_install = "jiqm_test.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jiqm_test.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"jiqm_test.tasks.all"
# 	],
# 	"daily": [
# 		"jiqm_test.tasks.daily"
# 	],
# 	"hourly": [
# 		"jiqm_test.tasks.hourly"
# 	],
# 	"weekly": [
# 		"jiqm_test.tasks.weekly"
# 	]
# 	"monthly": [
# 		"jiqm_test.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "jiqm_test.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "jiqm_test.event.get_events"
# }

