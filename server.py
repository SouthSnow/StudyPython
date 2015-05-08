import pymongo
from flask import Flask, request
import json
from bson import json_util
from bson.objectid import ObjectId



app = Flask(__name__)

mongoClient = pymongo.MongoClient('localhost', 27017)
db = mongoClient['dbmeizi']
def toJson(data):
    return json.dumps(data, default=json_util.default)

@app.route('/meizi/', methods=['GET'])

def findmeizi():
    if request.method == 'GET':
        lim = int(request.args.get('limit', 10))
        off = int(request.args.get('offset',0))
        results = db['meizi'].find().skip(off).limit(lim)
        json_results= []
        for result in results:
            json_results.append(result)
        return toJson(json_results)

if __name__ == '__main__':
    app.run(debug=True)
