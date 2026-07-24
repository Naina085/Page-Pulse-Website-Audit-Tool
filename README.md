
# 🚀 Page Pulse – Website Audit Tool

A lightweight web application built with **Flask**, **Python**, and **BeautifulSoup** that analyzes any website and provides a basic SEO & website health report.

This project was developed as part of a **Software Development Engineering Internship Assignment** to demonstrate backend development, web scraping, API integration, and frontend-backend communication.

---

## 📌 Features

✅ Analyze any website by entering its URL

✅ Check Website Status Code

✅ Measure Response Time

✅ Extract Page Title

✅ Extract Meta Description

✅ Count H1 Tags

✅ Count Images Missing ALT Attributes

✅ Calculate Approximate Word Count

✅ Responsive User Interface

✅ Flask REST API

✅ BeautifulSoup HTML Parsing

---

## 📸 Preview

### Homepage

- Simple and clean user interface
- Enter any website URL
- Click **Analyze**

### Website Report

The application displays:

- HTTP Status Code
- Response Time
- Page Title
- Meta Description
- H1 Tag Count
- Images Missing ALT Attributes
- Approximate Word Count

---

# 🛠️ Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- Python
- Flask

## Libraries

- Requests
- BeautifulSoup4

---

# 📂 Project Structure

```
Page-Pulse-Website-Audit-Tool/
│
├── app.py
├── analyzer.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── tests/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Page-Pulse-Website-Audit-Tool.git
```

Move into the project folder

```bash
cd Page-Pulse-Website-Audit-Tool
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 📖 How It Works

1. User enters a website URL.
2. JavaScript sends the URL to the Flask backend.
3. Flask receives the request through the `/analyze` API.
4. The backend fetches the webpage using the Requests library.
5. BeautifulSoup parses the HTML content.
6. Important SEO information is extracted.
7. The analysis is returned as JSON.
8. JavaScript updates the UI with the website report.

---

# 📊 Example Output

| Metric | Example |
|---------|---------|
| Status | 200 |
| Response Time | 235 ms |
| Page Title | Example Domain |
| Meta Description | Not Found |
| H1 Count | 1 |
| Missing ALT Images | 0 |
| Word Count | 21 |

---

# 💡 Current Capabilities

✔ Website Reachability Check

✔ HTML Parsing

✔ SEO Information Extraction

✔ Response Time Calculation

✔ REST API Integration

✔ Responsive Frontend

---

# 🚧 Future Improvements

- SEO Health Score
- Download Report as PDF
- Export Report as JSON
- Dark Mode
- Loading Animation
- Keyword Density Analysis
- Broken Link Detection
- Open Graph Tag Detection
- Mobile Friendliness Check
- Lighthouse API Integration

---

# 🧪 Testing

The application has been tested with websites such as:

- https://example.com
- https://python.org
- https://flask.palletsprojects.com

Some websites (such as Amazon and Wikipedia) may return HTTP 403 or 503 responses due to anti-bot protection, which is expected behavior when using standard HTTP requests.

---

# 📦 Dependencies

```
Flask
requests
beautifulsoup4
```

---

# 👨‍💻 Author

**Naina Kharayat**

Developed as part of a **Software Development Engineering Internship Assignment** using Flask, Python, Requests, BeautifulSoup, HTML, CSS, and JavaScript.

---

# 📄 License

This project is developed for educational and internship assessment purposes.
