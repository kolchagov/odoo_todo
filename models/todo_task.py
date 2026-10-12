from odoo import api, fields, models
from odoo.exceptions import UserError


class TodoTask(models.TransientModel):
    _name = "todo.task"
    _description = "Todo Task"

    name = fields.Char(string="Description", required=True)
    is_done = fields.Boolean(string='Done?')
    active = fields.Boolean(string='Active?', default=True)
