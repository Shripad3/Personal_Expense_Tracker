# Personal_Expense_Tracker

# 📊 Personal Expense Tracker

Automated tool to generate a professional **PDF expense report** from your Excel sheet — complete with category-wise summaries, charts, and optional email delivery. Built for freelancers, students, and professionals.


---

## ✨ Features

- 📥 Read data from `.xlsx` Excel files
- 📊 Generate **category-wise expense summary**
- 📈 Visualize data using **pie charts**
- 📝 Create a well-styled **PDF report**
- 📧 Optionally email the report as an attachment
- 🔐 Credentials stored securely via `.env`

---

## 🖼️ Sample Output

<p align="center">
  <img src="assets/sample_report.png" width="600"/>
</p>

---

## 📁 Sample Excel Format (`sample_data.xlsx`)

| Date       | Description      | Category     | Amount | Type    |
|------------|------------------|--------------|--------|---------|
| 2025-05-01 | Grocery Store     | Groceries    | 45.00  | Expense |
| 2025-05-02 | Freelance Project | Income       | 500.00 | Income  |
| 2025-05-03 | Bus Ticket        | Travel       | 10.00  | Expense |

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/Shripad3/Personal_Expense_Tracker.git
cd Personal_Expense_Tracker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up `.env`

Create a `.env` file in the root directory:

```
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_app_password
RECIPIENT_EMAIL=recipient@example.com
```

> 💡 Use an App Password if using Gmail (with 2FA enabled).

### 4. Add your data file

Replace or update `sample_data.xlsx` with your own data.

### 5. Run the script

```bash
python main.py
```

- Generates `monthly_report.pdf`
- Emails it if `.env` is correctly configured

---

## 📂 Project Structure

```
├── main.py                # Orchestrates everything
├── data_utils.py          # Parses and summarizes data
├── report_generator.py    # Builds styled PDF report
├── email_utils.py         # Sends email with attachment
├── sample_data.xlsx       # Sample input file
├── requirements.txt
├── .env                   # (Not committed) Credentials
```

---

## 🎯 Tech Stack

- Python 3.8+
- `pandas`, `matplotlib`
- `fpdf2`
- `smtplib`, `email.message`
- `python-dotenv`

---

## 📌 Future Improvements

- [ ] Add Streamlit interface for easy web usage
- [ ] Support `.csv` in addition to `.xlsx`
- [ ] Generate AI-based financial summaries
- [ ] Add CLI flags (e.g., `--email false`, `--file path.xlsx`)

---

## 🧑‍💻 Author

Built with ❤️ by [Shripad](https://github.com/Shripad3)

---

## 📄 License

[MIT License](LICENSE)
