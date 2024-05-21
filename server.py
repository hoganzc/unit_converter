from flask import Flask, request, render_template, jsonify
import convert

app = Flask(__name__)


@app.route("/api/convert", methods=['GET'])
def standard_imp_converter():

    data = request.get_json()
    unit = data['unit']
    amount = data['amount']

    return_unit = convert.get_unit(unit)
    return_amount = convert.convert(unit, amount)

    amount_2 = {return_amount: return_unit}
    return jsonify(amount_2)


if __name__ == "__main__":
    app.run()
