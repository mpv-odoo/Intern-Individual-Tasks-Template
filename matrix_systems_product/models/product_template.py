from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_group = fields.Selection([
        ('123456', '123456'),
        ('654321', '654321'),('172924', '172924')
        ], string='Product Group', default='123456', required=True)
    
    reference_no = fields.Char(string='Order Reference', required=True,
                          readonly=True, default='')
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('reference_no', ('New')) == ('New'):
                vals['reference_no'] = self.env['ir.sequence'].next_by_code('barcode.sequence.matrix')
        return super().create(vals_list)

    @api.depends('product_variant_ids.barcode','product_group')
    def _compute_barcode(self):
        for record in self:            
            barcode=str(record.product_group)[0:2]+"."+record.reference_no

            record.barcode = f"{str(record.product_group)[0:2]}.{record.reference_no}"
