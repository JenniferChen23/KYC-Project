import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time

def fetch_sg_company_info(company_name: str) -> dict:

    # 初始化變數
    company_basic_info = {}


    attempt = 0
    max_attempts = 4

    while attempt < max_attempts:
    # 設定 Chrome options
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

        # 啟動瀏覽器
        driver = webdriver.Chrome(service=Service(), options=options)

        try:
            # 開啟網站
            url = 'https://www.bizfile.gov.sg/'
            driver.get(url)
            time.sleep(random.uniform(2, 3))
            print("🚀 程式啟動")

            # 模擬滑動頁面
            print("📜 開始模擬滑動頁面")
            driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(2)
            
            # 搜尋公司名稱
            print("1. 查詢公司")
            wait = WebDriverWait(driver, 10)  # 增加等待時間
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "input-search-bar")))

            # 輸入公司名稱並搜尋
            search_box.send_keys(company_name)
            time.sleep(2)

            driver.execute_script("window.scrollBy(0, 600);")

            # 點擊搜尋按鈕
            print("2. 模擬點擊搜尋按鈕")
            search_btn = wait.until(EC.element_to_be_clickable((By.ID, "federated-search-dropdown-bottom-search-btn")))
            driver.execute_script("arguments[0].click();", search_btn)
            time.sleep(random.uniform(2, 4))

            # 擷取基本資料
            print("3. 擷取基本資料")
            try:
                # 等待 id 為 industry-search-result 的 div 出現
                industry_container = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.ID, "industry-search-result"))
                )
                print("✅ 成功找到物件。")

            except Exception as e:
                print("⚠️ 超過等待時間，未找到 'industry-search-result' 元素。")
            
            elems = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cmp-information-snippet-value-horizontal-container")))
            if len(elems) >= 4:  # 確保有足夠的資料
                company_basic_info["Registered Number"] = elems[0].text.strip()
                company_basic_info["Emerge or not"] = elems[1].text.strip()
                company_basic_info["Industry"] = elems[2].text.strip()
                company_basic_info["Company Address"] = elems[3].text.strip().replace("View Map", "").strip()
                #company_basic_info["Entity status"] = driver.find_element(By.CSS_SELECTOR, "div.cmp-status-badge-base").text.strip()

                # 印出結果
                print("\n── 擷取結果 ──")
                for k, v in company_basic_info.items():
                    print(f"{k}: {v}")

                # 返回結果
                return company_basic_info
            else:
                print("⚠️ 沒有找到足夠的資料")
                attempt += 1
                print(f"⏳ 等待 4 秒後重試，已嘗試 {attempt}/{max_attempts} 次...")
                time.sleep(4)

        except Exception as e:
            print("⚠️ 發生錯誤：", str(e))
            attempt += 1
            if attempt < max_attempts:
                print(f"⏳ 等待 4 秒後重試，已嘗試 {attempt}/{max_attempts} 次...")
                time.sleep(4)
            else:
                print("❌ 重試次數達到最大限制，請檢查錯誤。")
        finally:
            driver.quit()
            attempt += 1
            if attempt < max_attempts and company_basic_info!=None :
                print("── End ──")

            elif attempt < max_attempts:
                print(f"⏳ 等待 4 秒後重試，已嘗試 {attempt}/{max_attempts} 次...")
                time.sleep(4)
            else:
                print("❌ 重試次數達到最大限制，請檢查錯誤。")
    return {}



def fetch_Thi_company_info(company_name):
    
    url = 'https://datawarehouse.dbd.go.th/index'
    print("🚀 程式啟動")
    options = Options()
    # options.add_argument("--headless")  # 無頭模式（不顯示瀏覽器介面）
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

    prefs = {
    "profile.default_content_settings.popups": 0,
    "download.prompt_for_download": False,  # 不跳出下載詢問視窗
    "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,  # 允許多檔案下載
    }

    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(), options=options)

    try:
        driver.get(url)
        time.sleep(random.uniform(3, 5))  # 初始隨機等待

        # 頁面隨機滑動
        try:
            print("📜 開始模擬滑動頁面")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(2, 4))
            actions = ActionChains(driver)
            actions.move_by_offset(random.randint(50, 150), random.randint(50, 150)).perform()
            time.sleep(random.uniform(1, 3))
        except Exception as e:
            print("⚠️ 滑動頁面失敗:", e)

        # 嘗試關閉提醒框
        try:
            print("🔍 嘗試關閉提醒框（如果有）")
            close_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "btnWarning"))
            )
            close_button.click()
            print("✅ 已成功關閉提醒框")
            time.sleep(random.uniform(1, 2))
        except Exception as e:
            print("ℹ️ 沒有提醒框需要關閉或無法點擊:", e)

        # 語言切換成英文
        try:
            print("🌐 嘗試切換語言成英文")
            lang_label = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "label.switch-item.lang"))
            )
            lang_label.click()
            print("✅ 語言切換成功")
            time.sleep(random.uniform(1, 2))
        except Exception as e:
            print("⚠️ 語言切換失敗:", e)

        # 查詢公司
        print("1️⃣ 查詢公司資訊")
        try:
            time.sleep(5)  # 多給點時間確保元件載入
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "key-word"))
            )
            search_box.clear()
            search_box.send_keys(company_name)
            search_box.submit()
            print(f"✅ 搜尋 {company_name}")
            time.sleep(5)  # 等搜尋結果出現
        except Exception as e:
            print("❌ 搜尋公司時出錯:", e)
            return {}

        # 抓取公司基本資料
        print("2️⃣ 抓取公司基本資料")
        company_basic_info = {}
        try:
            WebDriverWait(driver, 20).until(
                lambda d: d.find_element(By.CSS_SELECTOR, "div.col-6.bold.green").text.strip() != ""
            )
            items = driver.find_elements(By.CSS_SELECTOR, "div.row.g-2 > div")
            for i in range(0, len(items), 2):
                key = items[i].text.strip()
                value = items[i+1].text.strip()
                company_basic_info[key] = value
            register_no_text = driver.find_element(By.CSS_SELECTOR, 'div.cols h4').text
            company_basic_info["Register Number"] = register_no_text.split(":")[1].strip()
            print("✅ 成功抓取公司基本資料")
            print(company_basic_info)
        except Exception as e:
            print("⚠️ 抓取基本資料失敗:", e)

        # 財務資訊下載
        print("3️⃣ 下載財務資訊")
#         try:
#             tabs = WebDriverWait(driver, 20).until(
#                 EC.presence_of_all_elements_located((By.CLASS_NAME, "tabinfo"))
#             )
#             for tab in tabs[1:4]:  # 略過第一個 tab
#                 try:
#                     print(f"👉 點擊標籤頁: {tab.text}")
#                     driver.execute_script("arguments[0].click();", tab)
#                     time.sleep(5)
#                     pdf_button = WebDriverWait(driver, 20).until(
#                         EC.element_to_be_clickable((By.ID, "create_pdf"))
#                     )
#                     driver.execute_script("arguments[0].click();", pdf_button)
#                     print(f"📄 成功點擊下載 PDF")
#                     time.sleep(5)
#                 except Exception as e:
#                     print(f"⚠️ 無法下載 {tab.text} 的 PDF:", e)
#         except Exception as e:
#             print("⚠️ 找不到財務資料標籤:", e)

        return company_basic_info

    except Exception as e:
        print("❌ 主流程錯誤:", e)
        return {}

    finally:
        print("🛑 結束程式")
        time.sleep(2)
        driver.quit()
