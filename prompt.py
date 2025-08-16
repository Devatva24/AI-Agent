import streamlit as st
import requests
import json

# Groq API setup
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-70b-8192"  # Other options: "llama2-70b-4096", "gemma-7b-it"

# Function to generate chat response using Groq
def generate_with_groq(user_prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": user_prompt}],
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=body)

    try:
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        st.error(f"Error: {e}")
        st.text(response.text)
        return "❌ Failed to get response from Groq."

# Function to fetch Bitcoin prices (same as before)
def GetBitCoinPrices():
    url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"
    querystring = {
        "referenceCurrencyUuid": "yhjMzLPhuIDl",
        "timePeriod": "7d"
    }
    headers = {
        "X-RapidAPI-Key": "d8d30e9e63msh827b070cc7fc029p14bfc5jsn9fd8bdfc2bbb",
        "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    try:
        data = response.json()
        history = data["data"]["history"]
        prices = [entry["price"] for entry in history]
        return ','.join(prices)
    except Exception as e:
        st.error("❌ Failed to get Bitcoin prices.")
        st.text(response.text)
        return ""

# Function to generate analysis prompt
def AnalyzeBitCoinWithGroq(bitcoinPrices):
    prompt = f"""
    You are a professional crypto analyst. Here's the list of Bitcoin prices for the last 7 days:
    {bitcoinPrices}

    Please analyze this data and provide:
    - Price Overview
    - Moving Averages
    - RSI (Relative Strength Index)
    - MACD
    - Should I Buy or Sell?
    - Beginner-friendly explanation
    """
    return generate_with_groq(prompt)

# Streamlit UI
st.title("💹 Bitcoin Technical Analysis using Groq API")
st.subheader("🚀 Fast & Smart Analysis with Mixtral or LLaMA2")

if st.button("🔍 Analyze Bitcoin"):
    with st.spinner("Fetching Bitcoin prices..."):
        prices = GetBitCoinPrices()

    if prices:
        with st.spinner("Analyzing with Groq..."):
            result = AnalyzeBitCoinWithGroq(prices)
            st.text_area("📊 Technical Analysis", result, height=500)
            st.success("✅ Analysis Complete!")
