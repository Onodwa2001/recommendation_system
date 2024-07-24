from flask import Flask, request, jsonify
from logic import compare_words

app = Flask(__name__)

@app.route('/rank-best-tutors', methods=['POST'])
def rankTutors():
    data = request.get_json()
    # Process the data as needed
    result= []
    student_data = data["student_data"]
    tutor_data = data["tutors"]

    scores = compare_words(student_data, tutor_data)

    i = 0
    for tutor in tutor_data:
        result.append({
            "id": tutor['id'],
            "score": scores[i] * 100
        })
        i += 1

    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)
