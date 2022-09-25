from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def count_telor(text):
  text = re.sub(r"[^\w\d\s]+", "", text).lower()
  text = text.split()
  sum = text.count('telor')
  return sum


@app.route("/post_text/v1", methods=['POST'])
def return_count():
    s = request.get_json()
    lenght = count_len(s['text'])
    count = count_telor(s['text'])
    return_text = {
        "total_char":lenght,
        "total_telor":count
    }
    return jsonify(return_text)

if __name__ == '__main__':
    app.run(port=1234, debug=True)