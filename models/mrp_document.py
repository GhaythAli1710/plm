from odoo import models, fields


class MrpDocument(models.Model):
    _inherit = 'mrp.document'

    origin_attachment_id = fields.Many2one(
        comodel_name='ir.attachment',
    )
