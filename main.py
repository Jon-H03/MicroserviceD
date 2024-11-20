import syllapy
from flask import Flask, request, jsonify

app = Flask(__name__)


def count_syllables(line):
    return sum(syllapy.count(word) for word in line.split())


def is_valid_haiku(haiku):
    lines = haiku.strip.split('\n')
    if len(lines) != 3:
        return False

    counts = [count_syllables(line) for line in lines]
    return counts == [5, 7, 5]


@app.route('/validate-haiku', methods=['POST'])
def validate_haiku():
    try:
        data = request.get_json()
        haiku = data.get('haiku', '').strip()

        valid = is_valid_haiku(haiku)

        if valid:
            return jsonify({"valid": True})
        else:
            return jsonify({"valid": False})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=5003)
