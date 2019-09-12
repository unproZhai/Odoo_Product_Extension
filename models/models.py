# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductCategory(models.Model):
    _inherit = "product.category"   

    image = fields.Binary(
    "Image", attachment=True,
    help="This field holds the image used as image for the product, limited to 1024x1024px.")

class ProductProduct(models.Model):
	_inherit = "product.product"

	item_number = fields.Char(index=True, help="Item Number", copy=False)
	model_number = fields.Char(index=True, help="Model Number", copy=False)

class ProductTemplate(models.Model):
    _inherit = "product.template"

    item_number = fields.Char(store=True, index=True,
                               related='product_variant_ids.item_number',
                               readonly=False, help='Item Number')
    model_number = fields.Char(store=True, index=True,
                               related='product_variant_ids.model_number',
                               readonly=False, help='Model Number')

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    item_number = fields.Char('Item Number', related='product_id.item_number')
    model_number = fields.Char('Model Number', related='product_id.model_number')

    image_small = fields.Binary(
        'Product Image', related='product_id.image_small')


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    item_number = fields.Char('Item Number', related='product_id.item_number')
    model_number = fields.Char('Model Number', related='product_id.model_number')