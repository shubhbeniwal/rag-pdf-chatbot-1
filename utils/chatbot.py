from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def retrieve_context(vector_db, question):

    docs = vector_db.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context, docs


def generate_answer(context, question, chat_history):

    prompt = f"""
You are an AI assistant answering questions about a document.

Use the provided context and previous conversation history.

If the answer cannot be found in the context, say:

"I could not find that information in the document."

Conversation History:
{chat_history}

Context:
{context}

Current Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

def summarize_document(context):

    prompt = f"""
You are an expert document analyst.

Analyze the document and provide:

1. Executive Summary

2. Key Topics Covered

3. Important Insights

4. Key Takeaways

Document:

{context}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

def generate_suggested_questions(context):

    prompt = f"""
Based on this document, generate 5 useful questions a user might ask.

Return ONLY the questions.

Document:

{context}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content