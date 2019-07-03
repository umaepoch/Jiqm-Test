# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _, msgprint


def execute(filters=None):
	columns, data = [], []
	columns = get_columns_at()
	data.append(["hello"])
	return columns, data

def get_columns_at():
	return [
		_("Place Of Supply") + "::150"
	]
