import requests
from django.conf import settings
import json

def get_ai_summary(content):
    """
    Generate AI summary using Groq API with Llama 3.3 70B
    """
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {settings.GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that creates concise, informative summaries of blog posts. Create a summary that is 2-3 sentences long and captures the main points of the content."
                },
                {
                    "role": "user",
                    "content": f"Please summarize this blog post:\n\n{content}"
                }
            ],
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        summary = result['choices'][0]['message']['content'].strip()
        return summary
        
    except Exception as e:
        print(f"Error generating AI summary: {e}")
        return "Unable to generate summary at this time. Please try again later."

def get_ai_comment_suggestion(post_content):
    """
    Generate AI comment suggestion using Groq API with Llama 3.3 70B
    """
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {settings.GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that suggests thoughtful, engaging comments for blog posts. Generate a single, concise comment suggestion that is relevant to the content and encourages discussion."
                },
                {
                    "role": "user",
                    "content": f"Suggest a thoughtful comment for this blog post:\n\n{post_content}"
                }
            ],
            "max_tokens": 100,
            "temperature": 0.8
        }
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        suggestion = result['choices'][0]['message']['content'].strip()
        return suggestion
        
    except Exception as e:
        print(f"Error generating AI comment suggestion: {e}")
        return "This is an interesting perspective! I'd love to hear more about your thoughts on this topic."

def generate_ai_blog_post(topic, tone="informative", length="medium"):
    """
    Generate a complete blog post using AI based on a topic
    """
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {settings.GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        # Configure length and style based on parameters
        length_instructions = {
            "short": "300-400 words",
            "medium": "500-700 words", 
            "long": "800-1000 words"
        }
        
        tone_instructions = {
            "informative": "educational and factual",
            "casual": "conversational and friendly",
            "professional": "formal and business-oriented",
            "creative": "imaginative and engaging"
        }
        
        word_count = length_instructions.get(length, "500-700 words")
        style = tone_instructions.get(tone, "educational and factual")
        
        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "system",
                    "content": f"You are a skilled blog writer. Write engaging, well-structured blog posts that are {style}. Your posts should be approximately {word_count} and include a clear introduction, body paragraphs, and conclusion. Use proper formatting and transitions."
                },
                {
                    "role": "user",
                    "content": f"Write a complete blog post about: {topic}\n\nPlease include:\n1. An engaging title\n2. A compelling introduction\n3. Well-structured body content\n4. A concluding paragraph\n\nFormat your response as:\n\nTITLE: [Your title here]\n\nCONTENT: [Your blog post content here]"
                }
            ],
            "max_tokens": 1500,
            "temperature": 0.8
        }
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        generated_content = result['choices'][0]['message']['content'].strip()
        
        # Parse the response to extract title and content
        if "TITLE:" in generated_content and "CONTENT:" in generated_content:
            parts = generated_content.split("CONTENT:")
            title = parts[0].replace("TITLE:", "").strip()
            content = parts[1].strip()
        else:
            # Fallback if format is different
            lines = generated_content.split('\n')
            title = lines[0].strip() if lines else "AI Generated Post"
            content = '\n'.join(lines[1:]).strip() if len(lines) > 1 else generated_content
        
        return {
            'title': title,
            'content': content
        }
        
    except Exception as e:
        print(f"Error generating AI blog post: {e}")
        return {
            'title': "Error Generating Post",
            'content': "Unable to generate blog post at this time. Please try again later or write the post manually."
        }
