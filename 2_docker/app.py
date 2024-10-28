import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    numbers = list(range(1, 51))
    return render_template('index.html', numbers=numbers)


@app.route('/submit', methods=['POST'])
def submit():
    user_numbers = [int(request.form[f'number{i}']) for i in range(1, 6)]
    results = []
    total_attempts = 1

    for user_number in user_numbers:
        count = 0
        while True:
            count += 1
            random_number = random.randint(1, 50)
            if random_number == user_number:
                results.append({'user_number': user_number, 'count': count})
                break

        total_attempts *= count

    percentage = 1 / total_attempts * 100 if total_attempts != 0 else 0

    return render_template('results.html', results=results, total_attempts=total_attempts, percentage=percentage)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)