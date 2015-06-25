# -*- encoding: utf-8 -*-
##############################################################################
#    
#    Odoo, Open Source Management Solution
#
#    Author: Andrius Laukavičius. Copyright: JSC NOD Baltic
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from openerp import models, fields

class res_partner(models.Model):
    _inherit = 'res.partner'
    

    x_tw_marfilacc = fields.Char(string='Cuenta Marfil', size=128,  
            help="Ponga aquí la cta.cliente en Marfil. Ejemplo 43002234")
    x_tw_marfilaccp = fields.Char(string='Cuenta Marfil', size=128, 
            help="Ponga aquí la cta.proveedor en Marfil. Ejemplo 40002234")

class res_account_invoice(models.Model):
    _inherit = 'account.invoice'

    x_tw_traspaso = fields.Boolean(string='Traspasado')
	
	
	

	
