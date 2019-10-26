from flask import Flask, request, jsonify


from Shops.Athleta import search_athleta
from Shops.BananaRepublic import search_bananarepublic
from Shops.Bloomingdales import search_bloomingdales
from Shops.Forever21 import search_forever21
from Shops.Gap import search_gap
from Shops.Kohls import search_kohls
from Shops.Macys import search_macys
from Shops.Nordstrom import search_nordstrom
from Shops.OldNavy import search_oldnavy

app = Flask(__name__)

@app.route("/athleta")
def athleta_wrapper():
    keywords = request.args.getlist("q")
    return jsonify(search_athleta(*keywords))

@app.route("/bannanarepublic")
def bananarepublic_wrapper():
    keywords = request.args.getlist("q")
    return jsonify(search_bananarepublic(*keywords))

@app.route("/bloomingdales")
def bloomingdales_wrapper():
    keywords = request.args.getlist("q")
    return jsonify(search_bloomingdales(*keywords))

@app.route("/dillards")
def dillards_wrapper():
    keywords = request.args.getlist("q")
    pass

@app.route("/forever21")
def forever21_wrapper():
    keywords = request.args.getlist("q")
    return jsonify(search_forever21(*keywords))

@app.route("/gap")
def gap_wrapper():
    keywords = request.args.getlist("q")
    return jsonify(search_gap(*keywords))

@app.route("/kohls")
def kohls_wrapper():
    keywords = request.args.getlist("q")
    return jsonify(search_kohls(*keywords))

@app.route("/macys")
def macys_wrapper():
    keywords = request.args.getlist("q")
    return jsonify(search_macys(*keywords))

@app.route("/nordstrom")
def nordstrom_wrapper():
    keywords = request.args.getlist("q")
    return jsonify(search_nordstrom(*keywords))

@app.route("/oldnavy")
def oldnavy_wrapper():
    keywords = request.args.getlist("q")
    return jsonify(search_oldnavy(*keywords))

@app.route("/all")
def all_wrapper():
    keywords = request.args.getlist("q")
    largeArray = search_kohls(*keywords) \
    + search_nordstrom(*keywords) \
    + search_bloomingdales(*keywords) \
    + search_oldnavy(*keywords) \
    + search_forever21(*keywords) \
    + search_macys(*keywords) \
    + search_athleta(*keywords) \
    + search_bananarepublic(*keywords) \
    + search_gap(*keywords)
    return jsonify(largeArray)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)