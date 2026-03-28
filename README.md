# Dev Nautics CRM Dashboard 🎓

A professional, multi-page CRM dashboard for **Dev Nautics** — an education tuition business based in Surat, Gujarat. Built with Python, Streamlit, and Plotly.

🌐 **Website**: [devnautics.com](https://devnautics.com)  
📍 **Location**: U-33, Corner Point, Citylight, Surat – 395007  
📞 **Contact**: 8866713206

---

## 📸 Features

- **10 fully interactive pages** covering every aspect of the business
- **30+ charts and infographics** (bar, pie, area, scatter, funnel, heatmap, gauge, waterfall)
- **Global sidebar filters** — class, service, academic year
- **Editable sample data** in CSV format — swap with real data anytime
- **Branded teal-green theme** matching Dev Nautics identity
- **Mobile-responsive** layout via Streamlit's wide mode

## 📄 Pages

| Page | Description |
|------|-------------|
| 🏠 Executive Overview | KPI cards, revenue trend, business health gauge |
| 👦 Student Management | Roster, attendance heatmap, gender split, scatter plot |
| 📋 Services | All 8 service cards, enrollment & revenue charts |
| 📦 Products & Inventory | Books, worksheets, kits, PAN India shipping |
| 💰 Revenue & Finance | Monthly revenue, waterfall, fee collection |
| 📣 Leads & Enquiries | Pipeline funnel, source breakdown, conversion rates |
| ⭐ Testimonials & Feedback | Ratings, NPS gauge, sentiment, review cards |
| 📊 Academic Performance | Score improvement, Olympiad medals, leaderboard |
| 👩‍🏫 Staff & Operations | Staff directory, payroll, batch capacity |
| 📡 Social & Digital | Follower trends, website traffic, WhatsApp leads |

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/devnautics-dashboard.git
cd devnautics-dashboard
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run locally
```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501**

---

## ☁️ Deploy to Streamlit Cloud (Free)

1. Push this repo to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **"New app"**
4. Select your repo, branch `main`, and file `app.py`
5. Click **"Deploy"** — your dashboard will be live in ~2 minutes!

---

## 📂 Project Structure

```
devnautics-dashboard/
├── app.py                    # Main entry point (sidebar + routing)
├── requirements.txt          # Python dependencies
├── README.md
├── pages/
│   ├── __init__.py
│   ├── page_overview.py      # Executive Overview
│   ├── page_students.py      # Student Management
│   ├── page_services.py      # Services Dashboard
│   ├── page_products.py      # Products & Inventory
│   ├── page_finance.py       # Revenue & Finance
│   ├── page_leads.py         # Leads & Enquiries
│   ├── page_feedback.py      # Testimonials & Feedback
│   ├── page_performance.py   # Academic Performance
│   ├── page_staff.py         # Staff & Operations
│   └── page_social.py        # Social & Digital Presence
└── data/
    ├── students.csv          # Student roster & scores
    ├── revenue.csv           # Monthly revenue by service
    ├── leads.csv             # Enquiry and lead data
    ├── feedback.csv          # Parent/student feedback
    ├── staff.csv             # Staff directory
    ├── performance.csv       # Academic scores & Olympiad
    └── social.csv            # Social media metrics
```

---

## ✏️ Customising Your Data

All data lives in the `/data` folder as simple CSV files. To use real data:

1. Open any CSV in Excel or Google Sheets
2. Replace the sample rows with your actual data
3. Keep the column names exactly as they are
4. Save and re-run `streamlit run app.py`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11+ | Core language |
| Streamlit | Web app framework |
| Plotly Express | Interactive charts |
| Pandas | Data manipulation |

---

## 📞 Support

Built for Dev Nautics. For questions or customisations, contact the development team.

> *"The future of your child is in our classroom."* — Dev Nautics
