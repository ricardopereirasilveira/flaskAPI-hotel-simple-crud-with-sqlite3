from flask_restful import Resource, reqparse
from models.hotelmodel import HotelModels

class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModels.query.all()]}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModels.find_hotel(hotel_id)
        if hotel:
            return hotel.json(), 200
        return {'message': 'Hotel not found!'}, 404

    def post(self, hotel_id):
        if HotelModels.find_hotel(hotel_id):
            return {"message": f"Hotel ID {hotel_id} already exists!"}, 401

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModels(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json(), 201

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_encontrado = HotelModels.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200

        hotel = HotelModels(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json(), 201



    def delete(self, hotel_id):
        hotel = HotelModels.find_hotel(hotel_id)
        if hotel:
            hotel.delete_hotel()
            return {'message': 'hotel deleted'}
        return {'message': 'hotel not found'}, 404