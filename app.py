# !/usr/bin/python3
# -*- coding: utf8 -*-
# author: Yusuf Berkay Girgin
# published: 25 July 2019


from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine

app = Flask(__name__)
api = Api(app)


e = create_engine('sqlite:///example_db.db')

class Kafes(Resource):
    def get(Resource):
        # this will return if user api is wrong
        return {'wrong url;': 'URL alternatives; /kafesler/mavi_kafesler, /kafesler/kirmizi_kafesler'}

    ###### MAVİ KAFESLER ######
    class mavi_kafes_no(Resource):
        def get(self):
            conn = e.connect()
            query = conn.execute("select kafes_no from mavi_kafesler")
            return {'mavi kafesler': [i[0] for i in query.cursor.fetchall()]}

    ### KIRMIZI KAFESLER ###
    class kirmizi_kafes_no(Resource):
        def get(self):
            conn = e.connect()
            query = conn.execute("select kafes_no from kirmizi_kafesler")
            return {'kirmizi kafesler': [i[0] for i in query.cursor.fetchall()]}

##### Order ####
class Order(Resource):
    def get(Resource):
        return {'Yanlis url': 'URL Alternatifleri; /kafesler/mavi_kafesler/order, /kafesler/kirmizi_kafesler/order'}

    class mavi_order_no(Resource):
        def get(self):
            conn = e.connect()
            query = conn.execute("select order_no from mavi_kafesler")
            return {'mavi kafesler': [i[0] for i in query.cursor.fetchall()]}

    class kirmizi_order_no(Resource):
        def get(self):
            conn = e.connect()
            query = conn.execute("select order_no from kirmizi_kafesler")
            return {'kirmizi kafesler': [i[0] for i in query.cursor.fetchall()]}

##### Adet #####
class Adet(Resource):
    def get(Resource):
        return {'wrong url': 'URL Alternatifleri; /kafesler/mavi_kafesler/adet, /kafesler/kirmizi_kafesler/adet'}

    class mavi_adet(Resource):
        def get(self):
            conn = e.connect()
            query = conn.execute("select adet from mavi_kafesler")
            return {'mavi kafesler': [i[0] for i in query.cursor.fetchall()]}

    class kirmizi_adet(Resource):
        def get(self):
            conn = e.connect()
            query = conn.execute("select adet from kirmizi_kafesler")
            return {'kirmizi kafesler': [i[0] for i in query.cursor.fetchall()]}

# wrong url entries
api.add_resource(Kafes, '/kafesler')
api.add_resource(Order, '/order')
api.add_resource(Adet, '/adet')
# name of kafes'
api.add_resource(Kafes.mavi_kafes_no, '/kafesler/mavi_kafesler')
api.add_resource(Kafes.kirmizi_kafes_no, '/kafesler/kirmizi_kafesler')
# order numbers of kafes'
api.add_resource(Order.mavi_order_no, '/kafesler/mavi_kafesler/order')
api.add_resource(Order.kirmizi_order_no, '/kafesler/kirmizi_kafesler/order')
# piece of kafes'
api.add_resource(Adet.mavi_adet, '/kafesler/mavi_kafesler/adet')
api.add_resource(Adet.kirmizi_adet, '/kafesler/kirmizi_kafesler/adet')

if __name__ == '__main__':
    app.run(port = 8080, debug=True)
