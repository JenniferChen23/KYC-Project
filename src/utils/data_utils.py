import pandas as pd

def map_company_info(rough_result: dict, data: dict, location: str) -> dict:
    if rough_result:
        for key, value in rough_result.items():
            if key in data:
                data[key] = value
    data["Location of Company Registration"] = location
    return data

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