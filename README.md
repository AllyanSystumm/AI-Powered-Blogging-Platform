# 🚀 Django AI-Powered Blogging Platform

AI-powered blogging platform built with **Django** + **Bootstrap**, integrating **Groq API** (**Llama 3.3 70B**) for summaries, comment suggestions, and AI-assisted writing.

## Stack
- **Backend**: Django 5.2, Python 3.10+
- **Frontend**: Bootstrap 5.3, Django templates, vanilla JS (Fetch/AJAX)
- **AI**: Groq Chat Completions API (`llama-3.3-70b-versatile`)
- **DB**: SQLite (dev)

## Features
- **Auth**: Register, login, logout
- **Posts**: View posts
- **Comments**: Add comments on posts
- **AI Summary**: Generate summary on post detail page
- **AI Comment Suggestion**: Suggest a comment for a post
- **AI Writer**: Generate full blog posts from a topic (styles + lengths)

## Permissions
- **Superuser**
  - Can create posts (`/post/create/`)
  - Can use AI Writer (`/ai-writer/`)
- **Regular users**
  - Can view posts, generate summaries, and comment

## Setup & Run

```bash
python -m venv venv
source venv/bin/activate
pip install django requests
python blogging_platform/manage.py makemigrations
python blogging_platform/manage.py migrate
python blogging_platform/manage.py runserver 8001
```

Open:
- http://127.0.0.1:8001/

### Create a superuser
```bash
python blogging_platform/manage.py createsuperuser
```

## Configure Groq API Key
Set environment variable `GROQ_API_KEY`.

Example:
```bash
export GROQ_API_KEY="your_groq_key"
```

## Key Files
- `blogging_platform/blog/ai_service.py` (Groq API calls)
- `blogging_platform/blog/views.py` (AI endpoints + permissions)
- `blogging_platform/blog/templates/blog/` (UI)

