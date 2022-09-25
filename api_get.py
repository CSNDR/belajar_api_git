from flask import Flask, request, jsonify

app =  Flask(__name__)


@app.route("/get_text/v2", methods=['GET']) 
def return_text():
    name_input = request.args.get('name')
    if  name_input == 'jokowi':
        return_text = {
            "nama":f"ya ndak tahu kok tanya saya",
       
            }
    else: 
        return_text = {
            "nama":f"nama beliau adalah {name_input}"
            }
    return jsonify(return_text)


if __name__ == "__main__":
    app.run(port=1234, debug=True)