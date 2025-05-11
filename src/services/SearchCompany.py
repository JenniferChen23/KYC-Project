from src.utils.selenium_utils import fetch_sg_company_info
from src.utils.selenium_utils import fetch_Thi_company_info
from src.utils.gemini_utils import find_company_info_FreeGemini
from src.utils.data_utils import map_company_info, shuffle_out, shuffle_in, show
import json

data_template = {
    "Company Registered Name": "",
    "Company Website": "",
    "Company Type": "",
    "Competitive": "",
    "Location of Company Registration": "",
    "Company Address": "",
    "Industry": "",
    "Main Products/Services": "",
    "Company Segment(B2B,B2C or..)": "",
    "Company Size": "",
    "Key Contact (C-Level)-Position": "",
    "Listed or not": "",
    "Emerge or not": "",
    "Responsible Persons": "",
    "Length of Business Operations": "",
    "Capital": "",
    "Registered Number": "",
    "Financial Report": ""
}

def get_company_info(company_name: str, location: str) -> dict:
    data = data_template.copy()
    reliable_platform_support = {"TH":fetch_Thi_company_info, "SG":fetch_sg_company_info}  # 可擴展其他國家

    # 設置基本資訊
    data["Company Registered Name"] = company_name

    # 可信平台搜尋
    location = location.upper()
    if location in reliable_platform_support:
        print(f"支援 {location} 政府平台搜尋")
        rough_result = reliable_platform_support[location](company_name)
        map_company_info(rough_result, data, location)
    else:
        print(f"⚠️ 不支援 {location} 的政府平台搜尋")

    # 中間結果
    print("經轉換成伊雲谷KYC欄位後的資訊")
    intermediate_result = show(data)

    # Gemini 補充剩餘欄位
    print("==========\n開始 Gemini search\n")
    rest = shuffle_out(data)
    gimini_result = find_company_info_FreeGemini(f"{location}-{company_name}", rest)
    final_data = shuffle_in(data, gimini_result)

    # 最終結果
    print("經轉換成伊雲谷KYC欄位後的資訊")
    print(final_data)
    final_result = json.dumps(final_data)


    return final_result 