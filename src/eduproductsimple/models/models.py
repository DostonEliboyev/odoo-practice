# -*- coding: utf-8 -*-
from odoo import models, fields

class EduProductSimple(models.Model):
    _name = "edu.product.simple"
    _description = "Educational Product (Only Char, Text, Integer, Float)"

    # --- Char fields ---
    name = fields.Char(required=True)                 # Mahsulot nomi
    sku = fields.Char(string="SKU")                   # Mahsulot kodi
    barcode = fields.Char(string="Barcode")           # Shtrix-kod
    brand = fields.Char(string="Brand")               # Brendi
    category = fields.Char(string="Category")         # Toifasi
    color = fields.Char(string="Color")               # Rangi

    # --- Text fields ---
    description = fields.Text(string="Description")   # Tavsif
    notes = fields.Text(string="Internal Notes")      # Ichki eslatmalar

    # --- Integer fields ---
    qty_on_hand = fields.Integer(string="Qty On Hand", default=0)      # Ombordagi miqdor
    min_qty = fields.Integer(string="Min Qty", default=0)              # Minimal miqdor
    max_qty = fields.Integer(string="Max Qty", default=0)              # Maksimal miqdor
    reorder_step = fields.Integer(string="Reorder Step", default=1)    # Qayta buyurtma qadam
    sold_month = fields.Integer(string="Sold This Month", default=0)   # Ushbu oyda sotilgan miqdor

    # --- Float fields ---
    list_price = fields.Float(string="List Price", default=0.0)        # Sotuv narxi
    cost = fields.Float(string="Cost", default=0.0)                    # Tannarx
    discount_percent = fields.Float(string="Discount %", default=0.0)  # Chegirma foizi (%)
    weight = fields.Float(string="Weight (kg)", default=0.0)           # Og'irligi (kg)
    volume = fields.Float(string="Volume (m3)", default=0.0)           # Hajmi (m3)
    rating = fields.Float(string="Rating", default=0.0)                # Reyting
    tax_rate = fields.Float(string="Tax Rate %", default=0.0)          # Soliq stavkasi (%)
    length_cm = fields.Float(string="Length (cm)", default=0.0)        # Uzunligi (sm)
    width_cm  = fields.Float(string="Width (cm)", default=0.0)         # Kengligi (sm)
    height_cm = fields.Float(string="Height (cm)", default=0.0)        # Balandligi (sm)

    def test_method(self):
        # 1-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 2-vazifa
        self.env["edu.product.simple"].search([("brand", "=", "Apple"),('list_price','>',500)])
        # 3-vazifa
        self.env["edu.product.simple"].search(["|",("brand", "=", "Samsung"),('brand',"=","Xiaomi")])
        # 4-vazifa
        self.env["edu.product.simple"].search([ "|",("brand", "=", "Sony"),('brand',"=","LG"),('list_price',"<",300)])
        # 5-vazifa
        self.env["edu.product.simple"].search([("name", "like", "pro")])
        # 6-vazifa
        self.env["edu.product.simple"].search([("sku", "=like", "ABC%")])
        # 7-vazifa
        self.env["edu.product.simple"].search([("barcode", "=like", "%789")])
        # 8-vazifa
        self.env["edu.product.simple"].search([("description", "ilike", "waterproof")])
        # 9-vazifa
        self.env["edu.product.simple"].search([("qty_on_hand", ">",10),("qty_on_hand", "<",100)])
        # 10-vazifa
        self.env["edu.product.simple"].search([("weight", ">",0.5),("weight", "<",2)])
        # 11-vazifa -
        self.env["edu.product.simple"].search([("list_price", "=", "Electronics")],limit=5)
        # 12-vazifa -
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 13-vazifa -
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 14-vazifa -
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 15-vazifa
        self.env["edu.product.simple"].search([("discount_percent", "<=", 10),("discount_percent", ">", 0)])
        # 16-vazifa
        self.env["edu.product.simple"].search([("sold_month", "=", "Electronics")])
        # 17-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 18-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 19-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 20-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 21-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 22-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 23-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 24-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 25-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 26-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 27-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 28-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 29-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])
        # 30-vazifa
        self.env["edu.product.simple"].search([("category", "=", "Electronics")])


