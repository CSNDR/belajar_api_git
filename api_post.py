from flask import Flask, request, jsonify
import re 

app =  Flask(__name__)

def _remove_punct(s):
    return re.sub(r"[^\w\d\s]+", "",s)

@app.route("/hitung_text/v1", methods=['POST'])
def get_text():
    s = request.get_json()
    s = s['text']

    total_char = len(s)
    s = s.lower()
    s = _remove_punct(s)
    list_s = s.split()

    total_telor = list_s.count("telor")

    dict_result = {
        "total_char": total_char,
        "total_telor": total_telor

    }
    return jsonify(dict_result)
 

if __name__ == "__main__":
    app.run(port=1234, debug=True)