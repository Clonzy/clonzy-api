# Clonzy API

Clonzy API is a Flask-based application that fetches graduated token data from [https://clonzy.fun/api/graduated](https://clonzy.fun/api/graduated) every 10 seconds. The data is saved into a CSV file and dynamically displayed on a Tailwind-styled web page with a black-and-white theme.

## Features

- ⏱️ Real-time data fetching every 10 seconds
- 💾 Saves token data to `graduated.csv`
- 🌐 Dynamic HTML table with live updates via JavaScript
- 🎨 Clean black/white UI with Tailwind CSS + custom styling
- 📊 API data exposed as JSON for frontend rendering

## Live Demo

Coming soon...

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Clonzy/clonzy-api.git
cd clonzy-api
```

### 2. (Optional) Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python app.py
```

Then open your browser at:  
👉 `http://127.0.0.1:5000/`

## How It Works

- `app.py` starts a background thread that fetches data from Clonzy API and writes it to `graduated.csv`.
- The `/` route renders `index.html`, displaying token data using Jinja2.
- `/api/data` serves the latest token data as JSON.
- JavaScript polls this endpoint every 10 seconds to update the table without reloading the page.

## API Endpoint

You can access raw data via:

```
GET /api/data
```

Response: JSON array of token records.

## License

This project is open-sourced under the MIT License — feel free to use, fork, or contribute.

## Contributing

Pull requests are welcome! Feel free to open issues or submit improvements.

---

Made with ❤️ by the Clonzy team.
