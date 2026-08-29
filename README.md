Live Demo Link -------> https://chatbot-2ctb.onrender.com/


# 🤖 Sagebot – AI Chatbot (Django + Gemini API)

Sagebot is a simple, clean AI-powered chatbot web application built with **Django** and **Google's Gemini API**. Users can ask any question and get an instant AI-generated answer, with every question automatically saved to a searchable history and manageable via the Django Admin panel.

---

## ✨ Features

- **Ask Anything** – Type a question and get a real-time AI response powered by Google Gemini.
- **Search History** – Every question is stored in the database and can be viewed on a dedicated history page.
- **Admin Panel Access** – All submitted questions are safely stored and viewable/manageable through Django's built-in admin interface.
- **Clean, Themed UI** – Dark navy theme with a custom robot mascot and simple, responsive design.
- **Environment-based Configuration** – API keys and secrets are kept out of source control using a `.env` file.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.2 |
| AI Engine | Google Gemini API (`google-generativeai`) |
| Database | SQLite (default, dev-friendly) |
| Frontend | HTML, CSS |
| Config | python-dotenv |
| Deployment | Gunicorn + Whitenoise |

---

## 📁 Project Structure

```
ChatBot/
├── ChatBot/                # Project settings, URLs, WSGI/ASGI config
├── testapp/                # Core app: models, views, forms, admin
│   ├── models.py           # Chatbot model (stores questions)
│   ├── views.py            # Handles question submission + Gemini API call
│   ├── forms.py            # Question input form
│   └── admin.py            # Admin panel registration
├── templates/               # HTML templates (index, history)
├── static/                  # CSS and images
├── requirements.txt          # Python dependencies
├── manage.py
└── .env                      # API key & secrets (not committed to git)
```

---

## ⚙️ Setup & Installation

### 1. Clone the project
```bash
git clone <your-repo-url>
cd ChatBot
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root (same level as `manage.py`) and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```
> Get your API key from [Google AI Studio](https://aistudio.google.com/api-keys).

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Create an admin superuser
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your browser.

---

## 🔍 Usage

| Page | URL | Description |
|---|---|---|
| Home / Ask a Question | `/` | Main chatbot interface |
| Search History | `/history` | View all previously asked questions |
| Admin Panel | `/admin` | Manage stored questions (requires superuser login) |

---

## 🔐 Data & Security Notes

- All questions submitted through the chatbot are stored in the database and are safely accessible only via the **Django Admin panel** (login required).
- The `.env` file (containing the API key) is excluded from version control via `.gitignore` — never commit real API keys to a public repository.
- `DEBUG = True` is enabled for local development only. Set it to `False` and configure `ALLOWED_HOSTS` before deploying to production.

---

## 🚀 Future Improvements

- User authentication for personalized chat history
- Delete/edit options for saved questions
- Pagination on the history page
- Deployment guide for production (Gunicorn + Whitenoise setup included in requirements)

---

## 📄 License

This project is for personal/educational use. Feel free to modify and extend it.

