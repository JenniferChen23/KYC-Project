# KYC

> backend: Python, Selenium, FastAPI

## Project Overview
1. 爬取泰國及新加坡的公開數據平台來減省人工填表的時間 (不足之資訊輔以 Gemin 蒐集)
3. 運用文字探勘技術從公司self-description 中判斷風險


## To start the API

create venv

```
py -m venv venv   # for Windows
python3 -m venv venv   # for macOS
```

activate venv

```
.\venv\Scripts\activate.ps1   # for Windows
source venv/bin/activate   # for macOS
```
install requirements

```
pip install -r requirements.txt
```

run flask

```
uvicorn main:app --reload
```

and the swagger UI  would runs on port http://127.0.0.1:8000/docs#

## API Description
1. Seach Company Info
目前平台搜尋只支援泰國(th)及新加坡 (sg)
```
/api/company-info/{companyName}/{location}
```
![image](https://github.com/user-attachments/assets/af63c766-459a-4bab-a69a-10a2cbace0ec)
Selenium’s progress is displayed in the terminal during execution.
![image](https://github.com/user-attachments/assets/30c20250-4fa4-421e-b3f8-6983beb35f51)


