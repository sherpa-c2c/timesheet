# Copyright 2016 Tecnativa - Antonio Espinosa
# Copyright 2016 Tecnativa - Sergio Teruel
# Copyright 2016-2018 Tecnativa - Pedro M. Baeza
# Copyright 2019 Brainbean Apps (https://brainbeanapps.com)
# Copyright 2024 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

from odoo.addons.project.models.project_task import CLOSED_STATES


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    task_id = fields.Many2one(
        "project.task",
        "Task",
        index="btree_not_null",
        compute="_compute_task_id",
        store=True,
        readonly=False,
        domain="project_id and [('allow_timesheets', '=', True), "
        "('has_template_ancestor', '=', False), "
        "('state', 'not in', " + str(list(CLOSED_STATES.keys())) + "), "
        "('project_id', '=', project_id)] "
        "or [('allow_timesheets', '=', True), "
        "('has_template_ancestor', '=', False), "
        "('project_id', '=?', project_id)]",
    )
