import pandas as pd
from datetime import datetime

def map_company_info(company_info,mapped_company_info,location):
    
    if (location == 'TH'):
        # 計算 "Registered Date" 距離今天的年數
        def calculate_business_length(registered_date):
            registered_date = datetime.strptime(registered_date, '%d %b %Y')  # 解析日期
            current_date = datetime.now()
            delta = current_date - registered_date
            years = delta.days / 365.25  # 計算年數，使用 365.25 考慮閏年
            return round(years, 2)  # 保留兩位小數

        # 映射規則
        map_dict = {
            'Registered Type': 'Customer Type',
            'Status': "Emerge or not",
            'Registered Date': 'Length of Business Operations',
            'Registered Capital': 'Capital',
            'Fiscal Year (submitted financial statement)': 'Financial Report',
            'Business Size': 'Company Size',
            "Register Number":"Register Number"
        }

        # 轉換資料
        for old_key, new_key in map_dict.items():
            value = company_info.get(old_key)
            if old_key == 'Registered Date':  # 如果是 "Registered Date"，則需要計算天數
                mapped_company_info[new_key] = calculate_business_length(value)
            else:
                mapped_company_info[new_key] = value

        return mapped_company_info
    elif (location == "SG"):
        for key in company_info:
            mapped_company_info[key] = company_info[key]

def shuffle_out(data: dict) -> dict:
    return {key: value for key, value in data.items() if value == ""}

def shuffle_in(data: dict, missing_data: dict) -> dict:
    if missing_data:
        for key, value in missing_data.items():
            if key in data:
                data[key] = value
    return data

def show(company_info: dict) -> dict:
    df = pd.DataFrame([company_info])
    df_transposed = df.transpose()
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', 90)
    return df_transposed.rename(columns={0: 'Value'}).to_dict()