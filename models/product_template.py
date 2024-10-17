from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    version = fields.Integer(
        string='Version',
        default=1,
        readonly=True,
        copy=False,
        help="The current version of the product.",
    )
    eco_count = fields.Integer(
        string='# ECOs',
        compute='_compute_eco_count',
    )
    eco_ids = fields.One2many(
        comodel_name='mrp.eco',
        inverse_name='product_tmpl_id',
        string='ECOs',
    )

    def _compute_eco_count(self):
        for p in self:
            p.eco_count = len(p.eco_ids)
