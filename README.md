# 💰 Personal Expense Analyzer (Python CLI App)

A robust command-line application built using Python that analyzes personal expense data, generates meaningful insights, and provides interactive user queries with visualization support.

---

## 🚀 Features

* 📊 **Expense Analysis**

  * Total, average, and maximum expense calculation
* 📂 **Category-wise Aggregation**

  * Grouping expenses by category using Pandas
* 📈 **Percentage Contribution**

  * Understand how much each category contributes to total spending
* 🔍 **Interactive Search**

  * Query spending by category (case-insensitive)
* 📉 **Data Visualization**

  * Bar chart visualization using Matplotlib
* ⚠️ **Smart Insights**

  * Detects high spending categories automatically
* 🛡️ **Error Handling**

  * Handles missing files, empty datasets, and invalid inputs

---

## 🛠️ Tech Stack

* Python
* Pandas
* Matplotlib

---

## 📁 Project Structure

```
Personal_Expense_Analysis/
│
├── analysis.py
├── expenses.csv
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone <https://github.com/Achu-24/Personal_Expense_analysis.git>
cd Personal_Expense_Analysis
```

2. Install dependencies:

```bash
pip install pandas matplotlib
```

3. Run the application:

```bash
python analysis.py
```

---

## 🧠 Example Menu

```
====== EXPENSE ANALYZER ======
1. Show Analysis
2. Search Category
3. Show Chart
4. Exit
```

---

## 📊 Sample Output

* Total Expense: 4900
* Average Expense: 544.44
* Top Category: Shopping

---

## 💡 Key Learnings

* Data analysis using Pandas
* GroupBy operations and aggregations
* Building CLI-based applications
* Handling real-world edge cases and user inputs
* Data visualization using Matplotlib

---

## 📌 Future Improvements

* Add date-wise analysis
* Export reports to CSV/PDF
* Convert to web app using Streamlit
* Add database integration

---

