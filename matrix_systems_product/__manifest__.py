{
    "name": "LMatrix Systems : Sequential Number for Barcode",
    "website": "https://www.odoo.com",
    "author": "Odoo Inc.",
    "summary": "The client would like to have a sequence number for barcodes on product.template (and product.product).",
    "description": "The client would like to have a sequence number for barcodes on product.template (and product.product). He has a studio field on product.template called Product Group (x_studio_product_group, type selection), he would like the sequence of the bar code to be 'FirstTwoDigitsofProductGroup.sequece'. According to the review from the development team, we will create another field called Product Group that will work the same way as the studio field, since we do not use Studio field for developments.",
    "license": "OPL-1",
    "category": "Custom Development.",
    "depends": [
        "product",

    ],
    "data": [
        "data/barcode_sequence.xml",
        "views/product_template.xml"
    ],
    "application": False,
}