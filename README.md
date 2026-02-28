# i智慧 社區大樓 PDF 爬蟲工具 (Community-Scraper)

這是一套半自動化的極速版工具，專門用來從 `is.ycut.com.tw` 下載「社區大樓二維透視」的藍色小人資料，並精準擷取 PDF 中的「純門牌地址」。

## 🚀 系統需求與環境安裝
請確保準備執行爬蟲的電腦已經安裝了 **Python 3.9 或以上版本**。

1. **下載專案**
   將這個資料夾 (`Community-Scraper`) 整個複製到準備使用的電腦上。

2. **開啟終端機 (PowerShell 或命令提示字元)**
   進入到 `Community-Scraper` 資料夾，例如：
   ```bash
   cd C:\路徑\Community-Scraper
   ```

3. **安裝相依套件**
   在此資料夾下執行以下指令，安裝處理 PDF 需要的核心模組 (`PyMuPDF`) 與資料整理模組：
   ```bash
   pip install pymupdf pandas
   ```

## 🛠️ 使用方式

整個流程分為兩段：**「蒐集網址」** 與 **「極速下載與萃取」**。

### 第一階段：取得 PDF 網址名單 (蒐集)
在此階段，我們需要先透過人工點擊或自動化瀏覽器外掛 (例如 Agent)，將所有藍色小人的公有雲 PDF 連結記錄下來，並整理成一個 JSON 檔案。

1. 請建立一個名為 `[社區名稱]_data.json` 的檔案，例如 `PARK188_data.json`。
2. 內容格式必須如下 (包含下拉選單地址、所有權人、PDF 原網址)：
   ```json
   [
       [
           "北新路 182巷32號 16樓之11", 
           "新ＯＯＯＯＯ (2025/05/31)", 
           "https://docs.evertrust.com.tw/ycut/pdf/xxx/.pdf/"
       ],
       [
           "北新路 182巷16號 15樓之4", 
           "林ＯＯ (2025/10/17)", 
           "https://docs.evertrust.com.tw/ycut/pdf/yyy/.pdf/"
       ]
   ]
   ```

### 第二階段：極速多執行緒下載與文字擷取
備妥 JSON 檔案後，我們就能讓 Python 一次五檔全開並行下載，且百分百精確地把地址抽取出來。

在終端機輸入：
```bash
python download_and_ocr.py [社區名稱]
```
> **範例**：若檔案叫 `PARK188_data.json`，請執行 `python download_and_ocr.py PARK188`

### 🎉 完成
程式會動態在畫面回報下載與地址擷取進度。
結束後，資料夾內會自動生成一份 `[社區名稱].csv`，裡面包含了乾淨的門牌與所有人姓名，可直接用 Excel 開啟過濾！