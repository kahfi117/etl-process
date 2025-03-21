import requests
import pandas as pd
import os
from config.settings import API_URL
import re

def extract_json():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    
def normalize_column_names(columns):
    """Fungsi untuk menormalkan nama kolom (huruf kecil, spasi menjadi underscore, hapus karakter spesial)"""
    return [
        re.sub(r'[^a-zA-Z0-9_]', '', col.strip().lower().replace(" ", "_").replace('"', ''))
        for col in columns
    ]

def extract_csv(file_path="data/raw_data/01_05_2025_mini.csv"):
    """Mengambil data dari file CSV dengan penyesuaian format."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File CSV tidak ditemukan di {file_path}")

    try:
        df = pd.read_csv(
            file_path, 
            on_bad_lines="skip",  # Lewati baris yang bermasalah
            encoding="utf-8",  # Pastikan encoding benar
            delimiter=",",  # Pastikan pemisah adalah koma
            quotechar='"',  # Mengabaikan tanda kutip ekstra
            dtype=str  # Membaca semua kolom sebagai string terlebih dahulu
        )

        # Normalisasi nama kolom
        df.columns = normalize_column_names(df.columns)

        # Pastikan CSV tidak kosong
        if df.empty:
            raise ValueError("CSV kosong atau tidak dapat diparse dengan benar.")

        return df
    except pd.errors.ParserError as e:
        raise Exception(f"Terjadi kesalahan dalam parsing CSV: {e}")
