import streamlit as st
import PyPDF2
import groq

# Initialize Groq API
GROQ_API_KEY = "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"  # Replace with your actual key
groq_client = groq.Client(api_key=GROQ_API_KEY)

# Function to extract text from the uploaded PDF
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to summarize the document
def summarize_text(text):
    prompt = f"Summarize the following crime report concisely:\n{text}"
    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Function to answer queries based on document
def answer_query(text, query):
    prompt = f"Based on the following crime report:\n{text}\n\nAnswer this question: {query}"
    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("Crime Report Analyzer")
st.write("Upload a crime report PDF, get a summary, and ask case-related questions.")

# File upload section
uploaded_file = st.file_uploader("Crime Report AI Agent", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF uploaded successfully! Extracting text...")
    
    # Extract text
    crime_report_text = extract_text_from_pdf(uploaded_file)
    
    # Summarization
    st.subheader("Summary of Crime Report")
    summary = summarize_text(crime_report_text)
    st.write(summary)
    
    # Query Handling
    st.subheader("Ask a Question About the Case")
    user_query = st.text_input("Enter your question:")
    if user_query:
        response = answer_query(crime_report_text, user_query)
        st.write("### Answer:")
        st.write(response)