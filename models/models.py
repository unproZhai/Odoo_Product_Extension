# -*- coding: utf-8 -*-

from odoo import models, fields, api

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

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    item_number = fields.Char('Item Number', related='product_id.item_number')
    model_number = fields.Char('Model Number', related='product_id.model_number')