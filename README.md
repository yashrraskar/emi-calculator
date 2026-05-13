# EMI Calculator Web Application

## 📌 Project Description

This is a simple EMI (Equated Monthly Installment) Calculator web application developed using Python Flask and HTML.

The application allows users to:

- Enter Loan Amount
- Enter Loan Tenure
- Enter CIBIL Score
- Calculate EMI
- View monthly EMI breakdown table

The rate of interest is decided based on the user's CIBIL score.



---

## 📖 Features

- Simple and beginner-friendly interface
- EMI calculation using financial formula
- Interest rate based on CIBIL score
- Monthly payment schedule
- Displays:
  - EMI Amount
  - Interest Component
  - Principal Component
  - Remaining Balance

---

## 📊 Interest Rate Logic

- If CIBIL score > 800  
  Interest Rate = 7.5%

- If CIBIL score <= 800  
  Interest Rate = 8.3%

---

## 🧮 EMI Formula

EMI = [P × R × (1 + R)^N] / [(1 + R)^N – 1]

Where:

- P = Principal Loan Amount
- R = Monthly Interest Rate
- N = Loan Tenure in Months

---

## 📁 Project Structure

```text
emi-calculator/
│
├── app.py
├── requirements.txt
├── README.md
│
└── templates/
      └── index.html
```
## 🎯 Learning Outcomes

- Understanding EMI calculations
- Using conditional statements in Python
- Working with loops
- Creating web applications using Flask
- Displaying tabular output
```
link : https://emi-calculator-6dx3.onrender.com/
