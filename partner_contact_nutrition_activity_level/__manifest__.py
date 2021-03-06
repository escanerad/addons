# -*- coding: utf-8 -*-
# Copyright 2016 Ursa Information Systems <http://ursainfosystems.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner Contact Activity Level",
    "summary": "Set the activity level of your contacts",
    "version": "10.0.1.0.0",
    "category": "Health",
    "website": "http://ursainfosystems.com",
    "author": "Ursa Information Systems, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "partner_contact_nutrition",
    ],
    "data": [
        "views/res_partner_view.xml",
    ],
}
