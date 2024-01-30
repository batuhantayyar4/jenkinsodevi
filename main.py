from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Yolcu(Resource):
    def get(self):
        data = pd.read_csv('yolcular.csv')
        data = data.to_dict('records')
        return {'data': data}, 200

    def post(self):
        isim = request.args['isim']
        soyisim = request.args['soyisim']
        kalkisYeri = request.args['kalkisYeri']
        varisYeri = request.args['varisYeri']
        kalkisSaati = request.args['kalkisSaati']
        varisSaati = request.args['varisSaati']
        koltukNo = request.args['koltukNo']
        aracNo = request.args['aracNo']
        plaka = request.args['plaka']
        ucret = request.args['ucret']

        data = pd.read_csv('yolcular.csv')

        new_data = pd.DataFrame({
            'isim': [isim],
            'soyisim': [soyisim],
            'kalkisYeri': [kalkisYeri],
            'varisYeri': [varisYeri],
            'kalkisSaati': [kalkisSaati],
            'varisSaati': [varisSaati],
            'koltukNo': [koltukNo],
            'aracNo': [aracNo],
            'plaka': [plaka],
            'ucret': [ucret]
        })

        data = data.append(new_data, ignore_index=True)
        data.to_csv('yolcular.csv', index=False)
        return {'data': new_data.to_dict('records')}, 200

class Arac(Resource):
    def get(self):
        data = pd.read_csv('yolcular.csv', usecols=[7])
        data = data.to_dict('records')
        return {'data': data}, 200

class YolcuAra(Resource):
    def get(self, isim):
        data = pd.read_csv('yolcular.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['isim'] == isim:
                return {'data': entry}, 200
        return {'message': 'No entry found with this name !'}, 404

api.add_resource(Yolcu, '/yolcular', methods=['GET', 'POST'])
api.add_resource(Arac, '/araclar')
api.add_resource(YolcuAra, '/<string:isim>')

if __name__ == '__main__':
    app.run()