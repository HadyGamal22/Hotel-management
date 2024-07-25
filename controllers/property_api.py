import json
import math
from urllib.parse import parse_qs

from odoo import http
from odoo.http import request


def valid_response(data,pagination_info,status_code):
    respose_body={
        'message':"successfully fetched api",
        'data':data
    }
    if pagination_info:
        respose_body['pagination_info']=pagination_info
    return request.make_json_response(respose_body, status=status_code)
class PropertyApi(http.Controller):
    @http.route("/v1/property",methods=["POST"],type="http",auth="none",csrf=False)
    def post_property(self):
        args=request.httprequest.data.decode()
        vals=json.loads(args)
        print("inside post test point",vals)
        res=request.env['model.a'].sudo().create(vals)
        print(res)
        if res:
            return valid_response({
                "message":"done post"
            },200)
    @http.route("/v1/property/json",methods=["POST"],type="json",auth="none",csrf=False)
    def post_property_json(self):
        args=request.httprequest.data.decode()
        vals=json.loads(args)
        if not vals.get('name'):
            return "not valid"
        else:
            print("inside post test point",vals['name'])
            try:
                res=request.env['model.a'].sudo().create(vals)
                # print(res)
                #i can easilt return with the li
                if res:
                    return {
                        "message":"done",
                        "id":res.id,
                        "name":res.name,
                        "status":201
                    }
            except Exception as error:
                return {
                    "message": error,
                }

    @http.route("/v1/property/json/<int:property_id>", methods=["PUT"], type="json", auth="none", csrf=False)
    def update_property_json(self,property_id):
        try:
            property_id=request.env['model.a'].sudo().search([
                ("id","=",property_id)
            ])
            if not property_id:
                return {
                    "message": "id not found",
                }
            print(property_id)
            args = request.httprequest.data.decode()
            vals = json.loads(args)
            print(vals)
            property_id.write(vals)
            return valid_response({
                "message": "updated successfully",
                "id":property_id.id,
            },201)

        except Exception as error:
            return {
                    "message": error,
                }

    @http.route("/v1/property/json/<int:property_id>", methods=["GET"], type="json", auth="none", csrf=False)
    def get_property_json(self, property_id):
        try:
            property_id = request.env['model.a'].sudo().search([
                ("id", "=", property_id)
            ])
            if not property_id:
                return {
                    "message": "id not found",
                }
            for rec in property_id:
                print(rec.name)
            # print(property_id)
            return {
                "message": "updated successfully",
                "id": property_id.id,
                "name": property_id.name,
                "status": 201
            }

        except Exception as error:
            return {
                "message": error,
            }

    @http.route("/v1/property/json/<int:property_id>", methods=["DELETE"], type="json", auth="none", csrf=False)
    def delete_property_json(self, property_id):
        try:
            property_id = request.env['model.a'].sudo().search([
                ("id", "=", property_id)
            ])
            if not property_id:
                return {
                    "message": "id not found",
                }
            property_id.unlink()
            return valid_response({
                "message": "deleted successfully",
                "id": property_id.id,
            },200)

        except Exception as error:
            return {
                "message": error,
            }

    @http.route("/v1/property_all", methods=["GET"], type="http", auth="none", csrf=False)
    def get_all_property_json(self):
        try:
            req = parse_qs(request.httprequest.query_string.decode('utf-8'))
            property_domain=[]
            page = offset = None
            limit=5
            if req:
                if req.get('limit'):
                    # print("limit",req.get('limit'))
                    limit=int(req.get('limit')[0])
                if req.get('page'):
                    page = int(req.get('page')[0])
            print(page)
            print(limit)
            if req.get("state"):
                property_domain+=[("state","=",req.get("state")[0])]
            property_ids = request.env['model.a'].sudo().search(property_domain,offset=page*limit-limit,limit=limit,order='id desc')
            property_count = request.env['model.a'].sudo().search_count(property_domain)

            print(property_ids)
            print(property_count)
            if not property_ids:
                return valid_response({
                    "message": "there are no records",
                },200)
            counter=0
            return valid_response( [{
                "message": "get data successfully",
                "id": property.id,
                "name": property.name,
                "state": property.state,
                "counter":len( property_ids),
            } for property in property_ids ],
                pagination_info ={
                'page':page if page else 1 ,
                'limit':limit,
                'pages':math.ceil(property_count/limit) if limit else 1,
                "count":property_count
                },
                status_code=200)

        except Exception as error:
            return {
                "message": error,
            }
