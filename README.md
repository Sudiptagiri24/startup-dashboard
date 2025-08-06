# 🚀 Startup Funding Dashboard

An interactive Streamlit dashboard that visualizes startup funding trends in India. Explore investments by year, funding rounds, sectors, and investor profiles.

🔴 **Live App:** [Startup Funding Dashboard](https://iswjcdzc4zzeabay4becrb.streamlit.app/)

---

## 📊 Features

- **Overall Analysis:**  
  View total, maximum, and average investments, along with funded startup count and a month-over-month funding trend graph.

- **Investor Analysis:**  
  Get detailed insights on any investor - their biggest investments, sectors of interest, cities, rounds, and year-wise trends.

- **StartUp Mode:** *(Coming soon or under development)*  
  Placeholder for startup-specific deep-dive.

---

## 📁 Dataset

- `startup_cleaned.csv`  
  A cleaned dataset containing columns like `startup`, `investors`, `amount`, `date`, `vertical`, `round`, `city`.

---

## 🛠 Tech Stack

- Python
- Pandas
- Matplotlib
- Streamlit

---

## 📦 Installation (For Local Use)

```bash
git clone https://github.com/your-username/startup-dashboard.git
cd startup-dashboard
pip install -r requirements.txt
streamlit run app.py
