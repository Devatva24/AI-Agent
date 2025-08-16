import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

st.set_page_config(page_title="Autism Prediction App", layout="wide")
st.title("🧠 Autism Spectrum Disorder (ASD) Prediction")

# Load model assets
@st.cache_resource
def load_assets():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    target_encoder = joblib.load("target_encoder.pkl")
    encoders = joblib.load("feature_encoders.pkl")
    feature_columns = joblib.load("feature_columns.pkl")
    return model, scaler, target_encoder, encoders, feature_columns

model, scaler, target_encoder, encoders, feature_columns = load_assets()

# Encode input dataframe
def encode_input(df, encoders, feature_columns):
    df = df.copy()
    for col in df.columns:
        if col in encoders:
            df[col] = encoders[col].transform(df[col].astype(str))
    df = df[feature_columns]  # Ensure correct column order
    return df

uploaded_file = st.file_uploader("📁 Upload test CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        df_original = df.copy()
        df_encoded = encode_input(df, encoders, feature_columns)
        df_scaled = scaler.transform(df_encoded)

        preds = model.predict(df_scaled)
        preds_labels = target_encoder.inverse_transform(preds)

        df_original["Predicted_ASD"] = preds_labels
        st.success("✅ Prediction completed!")
        st.dataframe(df_original)

        csv = df_original.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Predictions", data=csv, file_name="predicted_asd.csv", mime="text/csv")
    except Exception as e:
        st.error(f"❌ Error: {e}")
