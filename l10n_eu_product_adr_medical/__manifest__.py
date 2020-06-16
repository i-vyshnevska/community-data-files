# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
{
    "name": "ADR Medial Products",
    "summary": "Extencion to better handling of medical products",
    "version": "13.0.1.0.0",
    "category": "Product",
    "website": "https://github.com/OCA/community-data-files",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["l10n_eu_product_adr"],
    "data": [
        "data/product_dangerous_type_data.xml",
        "data/product_dangerous_class_data.xml",
        "security/ir.model.access.csv",
        "views/product_template_view.xml",
        "views/product_dangerous.xml",
    ],
}
