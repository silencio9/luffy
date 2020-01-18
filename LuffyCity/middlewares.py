# -*- coding:utf-8 -*-
from django.utils.deprecation import MiddlewareMixin


class MyCors(MiddlewareMixin):

    def process_response(self,request,response):

        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET,POST,DELETE,PUT"
        response["Access-Control-Allow-Headers"] = "Content-Type,AUTHORIZATION"

        return response



