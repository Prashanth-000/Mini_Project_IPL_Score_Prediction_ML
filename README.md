# Cricket Score Analyzer for Premier League

![Python](https://img.shields.io/badge/Python-3.9-blue) ![Flask](https://img.shields.io/badge/Flask-2.0.1-lightgrey) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-brightgreen)

## 📌 Project Overview
This project is a comprehensive Cricket Score Analyzer designed for premier league matches. It leverages machine learning techniques to predict match outcomes and project real-time scores based on various match statistics. The system is built using Flask and integrates a pre-trained Random Forest model for predictive analytics. Additionally, it employs a network-based model to dynamically assess ongoing match conditions and forecast potential results with greater accuracy.

## 📂 Folder Structure
```
FINAL MODEL/
│-- .ipynb_checkpoints/
│-- IPLScorePredictor-2024-main/
│   │-- .ipynb_checkpoints/
│   │-- static/
│   │   │-- .ipynb_checkpoints/
│   │   │-- css/
│   │   │-- files/
│   │   │-- images/
│   │   │-- deliveries.csv
│   │   │-- IPL_Ball_by_Ball_2008_2022.csv
│   │   │-- IPL_Matches_2008_2022.csv
│   │   │-- matches.csv
│   │-- templates/
│   │   │-- about.html
│   │   │-- contact.html
│   │   │-- index.html
│   │   │-- model.html
│   │   │-- predict.html
│   │   │-- result.html
│   │-- 2023data.ipynb
│   │-- app.py
│   │-- data.ipynb
│   │-- dataset.csv
│   │-- model.py
│   │-- pipe.pkl
│   │-- ra_pipe.pkl
│   │-- Requirement.txt
│   │-- testing.py
│   │-- Result/
│   │   │-- Screenshot 2024-12-27 212843.png
│   │   │-- Screenshot 2024-12-27 212927.png
│   │   │-- Screenshot 2024-12-27 213354.png
│   │   │-- Screenshot 2024-12-27 213418.png
│   │   │-- Screenshot 2024-12-27 213437.png
│   │   │-- Screenshot 2024-12-27 213506.png
│   │-- README.md
```

## 🚀 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Prashanth-000/Mini_Project_IPL_Score_Prediction_ML.git
   cd IPLScorePredictor-2024-main
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r Requirement.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open `http://127.0.0.1:5000/` in your browser.

## 🎯 Features
✅ Predict IPL match-winning probability
✅ User-friendly web interface
✅ Live match statistics input
✅ Trained ML model using Random Forest
✅ Interactive visualization of match outcomes

## 📸 Screenshots
### Inputs Page
![Input](/Result/Screenshot%202024-12-27%20213406.png)

### Results Page
![Results Page](/Result/Screenshot%202024-12-27%20212927.png)

## 🤝 Contribution
Feel free to fork, modify, and create pull requests. For major changes, please open an issue first to discuss.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

---
_Developed with ❤️ by [PFB-000]_

