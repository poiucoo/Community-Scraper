import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import pandas as pd
import sys
import os
import re

# 如果系統環境沒有將 tesseract 加入 PATH，可能需要指定安裝路徑
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def process_pdf(pdf_path, address_dropdown, owner_name, community_name="output"):
    """
    處理單一 PDF，截取第二頁特定區塊進行 OCR。
    預計：擷取『建物所有權部』的地址欄位。
    """
    try:
        # 開啟 PDF
        doc = fitz.open(pdf_path)
        if len(doc) < 2:
            print(f"Error: {pdf_path} 頁數不足兩頁。")
            return
            
        # 取得第二頁 (index=1)
        page = doc[1]
        
        # 定義裁切區域 (x0, y0, x1, y1) - 這些座標需視實際 PDF 版面調整
        # 由於尚未有實際 PDF 測試，先假設一個抓取上半部偏左或特定表格位置的區域
        # 調整時，可以使用 page.rect 確認整體寬高
        rect = fitz.Rect(100, 200, 500, 400) # 假設區塊
        
        # 改用 PyMuPDF 的文字提取功能 (因為 PDF 是系統產生的，通常包含可選取的文字內容)
        text = page.get_text("text", clip=rect)
        
        # 清除所有空白與換行以方便正則比對
        clean_text = re.sub(r'\s+', '', text)
        
        # 尋找 "地址" 和 "權利範圍" 之間的字串
        match = re.search(r'地址(.*?)權利範圍', clean_text)
        if match:
            extracted_address = match.group(1)
        else:
            # 若無匹配或內容為空
            extracted_address = clean_text if clean_text else "[無文字或需使用OCR提取]"
        
        # 寫入 CSV
        csv_file = f"{community_name}.csv"
        file_exists = os.path.isfile(csv_file)
        
        new_row = pd.DataFrame([{
            "下拉選單地址": address_dropdown,
            "所有權人姓名": owner_name,
            "擷取到的地址文字": extracted_address
        }])
        
        # a=append mode
        new_row.to_csv(csv_file, mode='a', index=False, header=not file_exists, encoding='utf-8-sig')
        print(f"Success: {pdf_path} 處理完成 -> {extracted_address}")
        
    except Exception as e:
        print(f"發生錯誤 {pdf_path}: {e}")

if __name__ == "__main__":
    # 使用範例: python process_pdf.py "C:\path\to\file.pdf" "新北市淡水區XX路" "王大明" "Hi-City"
    if len(sys.argv) >= 4:
        pdf_file = sys.argv[1]
        addr = sys.argv[2]
        owner = sys.argv[3]
        community = sys.argv[4] if len(sys.argv) > 4 else "output"
        process_pdf(pdf_file, addr, owner, community)
    else:
        print("Usage: python process_pdf.py <pdf_path> <address_dropdown> <owner_name> [community_name]")
