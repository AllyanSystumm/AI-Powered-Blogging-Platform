# 🚀 Django AI-Powered Blogging Platform

![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-AI-orange?style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

A feature-rich, AI-integrated blogging platform built with **Django** and **Bootstrap**. It leverages the **Groq API** (using **Llama 3.3 70B**) to provide intelligent writing assistance, automated summaries, and smart comment suggestions.

---

## ✨ Key Features

### 👤 User Features
- **Modern UI**: Sleek, responsive design using Bootstrap 5.3.
- **Authentication**: Fully functional user registration, login, and logout.
- **Interactive Blogging**: Read posts, engage with comments, and join the community.

### 🤖 AI-Powered Capabilities (Powered by Groq)
- **AI Summary**: One-click generation of concise summaries for long blog posts.
- **AI Comment Suggestion**: Get intelligent suggestions for what to comment on a post.
- **AI Writer**: A dedicated tool for creators to generate full-length, styled blog posts from simple topics.

### 🛠 Administrative Tools
- **Secure Post Creation**: Post creation and AI Writing tools are restricted to authorized users (Superusers).
- **Admin Dashboard**: Manage users, posts, and comments effortlessly through the Django admin interface.

---

## 🛠 Tech Stack

- **Backend**: Django 5.2 (Python 3.10+)
- **Frontend**: Bootstrap 5.3, Django Templates, Vanilla JavaScript (AJAX)
- **Database**: SQLite (Development)
- **AI Integration**: Groq Cloud API (`llama-3.3-70b-versatile`)
- **Deployment**: Gunicorn + Nginx (Production-ready)
- **Static Files**: WhiteNoise for efficient static file serving

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10 or higher
- A Groq API Key (Get one at [console.groq.com](https://console.groq.com/))

### 2. Installation

```bash
# Clone the repository
git clone <repository-url>
cd Blogging_Platform

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file in the project root or set the environment variables directly:

```bash
export GROQ_API_KEY="your_groq_api_key_here"
export DJANGO_SECRET_KEY="your_secret_key"  # Optional: for production
export DJANGO_DEBUG="True"                  # Optional: True for dev, False for prod
```

### 4. Database Setup & Run

```bash
# Run migrations
python blogging_platform/manage.py makemigrations
python blogging_platform/manage.py migrate

# Create an administrator
python blogging_platform/manage.py createsuperuser

# Start the development server
python blogging_platform/manage.py runserver 8001
```

Access the application at: `http://127.0.0.1:8001/`

---

## 📂 Project Structure

```text
Blogging_Platform/
├── blogging_platform/        # Django project root
│   ├── blog/                 # Main application logic
│   │   ├── ai_service.py     # Groq API integration
│   │   ├── templates/        # HTML templates (AI Writer, Blog, Auth)
│   │   └── views.py          # AI endpoints & business logic
│   ├── blogproject/          # Project settings & configuration
│   └── manage.py             # Django CLI
├── deploy/                   # Deployment configurations (Nginx & Gunicorn)
├── scripts/                  # Automation scripts
│   └── deploy.sh             # Automated deployment script for production
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## 🛰 Deployment

The project includes pre-configured deployment files for an EC2/Linux environment:
- `deploy/gunicorn.service`: Systemd service configuration for Gunicorn.
- `deploy/nginx_config.conf`: Nginx server block configuration.
- `scripts/deploy.sh`: A one-click script to update the codebase, run migrations, collect static files, and restart services.

---

## 📄 License
This project is open-source. Feel free to contribute and improve!
