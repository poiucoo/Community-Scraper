import urllib.request
import os
import subprocess
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
import subprocess

pdf_data = [
    ("北新路 182巷32號 16樓之11", "新ＯＯＯＯＯ (2025/05/31)", "https://docs.evertrust.com.tw/ycut/pdf/25151062qQjoO7rOB5RyN4QpCt5xw/.pdf/"),
    ("北新路 182巷16號 15樓之4", "新ＯＯＯＯＯ (2025/10/17)", "https://docs.evertrust.com.tw/ycut/pdf/25290063h2OimbcVpwF9WHwtWMQNV/.pdf/"),
    ("北新路 182巷32號 14樓之4", "新ＯＯＯＯＯ (2025/08/21)", "https://docs.evertrust.com.tw/ycut/pdf/25233063N0rUEWxs7F9ZiGsIUVtD1/.pdf/"),
    ("北新路 182巷16號 6樓之5", "新ＯＯＯＯＯ (2025/10/17)", "https://docs.evertrust.com.tw/ycut/pdf/25290061MW6mseHeS2u7ZceJmbxjH/.pdf/"),
    ("北新路 182巷32號 5樓之5", "新ＯＯＯＯＯ (2025/10/17)", "https://docs.evertrust.com.tw/ycut/pdf/25290060QoTOgNGtz7bSzIeVHJd0r/.pdf/"),
    ("北新路 182巷16號 4樓之5", "新ＯＯＯＯＯ (2025/08/05)", "https://docs.evertrust.com.tw/ycut/pdf/25217067cDlRMK58GLaxideT1Ztu3/.pdf/"),
    ("北新路 182巷32號 3樓之1", "新ＯＯＯＯＯ (2025/10/17)", "https://docs.evertrust.com.tw/ycut/pdf/25290062DUPoIQES2GXj4fCFhJzWd/.pdf/"),
    ("北新路 182巷16號 1樓", "新ＯＯＯＯＯ (2024/10/22)", "https://docs.evertrust.com.tw/ycut/pdf/24296062nwWi4h3LHLjJ63YzP7k7j/.pdf/"),
    ("北新路 182巷18號 1樓", "新ＯＯＯＯＯ (2024/05/13)", "https://docs.evertrust.com.tw/ycut/pdf/24135066u0r2cU6UgB12Z7i3bfhuc/.pdf/")
]

download_dir = "pdfs"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

for i, (addr, owner, url) in enumerate(pdf_data):
    pdf_path = os.path.join(download_dir, f"file_{i}.pdf")
    try:
        print(f"Downloading {url} to {pdf_path}")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(pdf_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
            
        print(f"Downloaded, running OCR for {addr}...")
        subprocess.run([r"c:\Antigravity\Hi-City-Scraper\venv\Scripts\python.exe", "process_pdf.py", pdf_path, addr, owner])
    except Exception as e:
        print(f"Failed to process {addr}: {e}")
