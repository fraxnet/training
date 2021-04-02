# -*- coding: utf-8 -*-
 from odoo import http


 class Fraxmod4(http.Controller):
     @http.route('/fraxmod4/fraxmod4/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/fraxmod4/fraxmod4/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('fraxmod4.listing', {
             'root': '/fraxmod4/fraxmod4',
             'objects': http.request.env['fraxmod4.fraxmod4'].search([]),
         })

     @http.route('/fraxmod4/fraxmod4/objects/<model("fraxmod4.fraxmod4"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('fraxmod4.object', {
             'object': obj
         })
