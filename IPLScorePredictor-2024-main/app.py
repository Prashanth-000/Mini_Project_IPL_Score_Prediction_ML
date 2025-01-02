from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
# Prediction Page Route
@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/models')
def models():
    return render_template('model.html')

# About Page Route
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        batting_team = request.form['batting_team']
        bowling_team = request.form['bowling_team']
        selected_city = request.form['selected_city']
        target = int(request.form['target'])
        score = int(request.form['score'])
        balls_left = int(request.form['balls_left']) 
        wickets = int(request.form['wickets'])

        runs_left = target - score
        wickets_remaining = 10 - wickets
        overs_completed = (120 - balls_left) / 6  # Calculate overs_completed from balls_left
        crr = score / overs_completed
        rrr = runs_left / (balls_left / 6)
        bowling_score=target;
        batting_score = round(crr*(balls_left/6));
        batting_score+=score;

        input_data = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets_remaining': [wickets_remaining],
            'total_run_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        pipe = pickle.load(open('IPLScorePredictor-2024-main/ra_pipe.pkl', 'rb'))
        result = pipe.predict_proba(input_data)

        win_probability = round(result[0][1] * 100)
        loss_probability = round(result[0][0] * 100)

        return render_template('result.html', batting_team=batting_team, bowling_team=bowling_team, win_probability=win_probability, loss_probability=loss_probability,batting_score=batting_score,bowling_score=bowling_score)


if __name__ == '__main__':
    app.run(debug=True)
