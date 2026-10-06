import numpy as np
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time
import random
import os
from datetime import datetime

driver = webdriver.Chrome()

url = "https://www.topcv.vn/tim-viec-lam-cong-nghe-thong-tin-cr257?type_keyword=1&disable_auto_detect_type_keyword=1&"
pages ={"page": 1}

ids = []
titles = []
salaries = []
companies = []
locations = []
experiences = []
times = []

for page in range(1, 3):

    driver.get(url + f"page={page}")
    time.sleep(random.randint(2, 5))

    # Lấy từng tin tuyển dụng
    jobs = driver.find_elements(
        By.CSS_SELECTOR,
        ".job-item-search-result"
    )

    print(f"Trang {page}: {len(jobs)} tin")

    # Lấy thông tin bên trong từng tin
    for job in jobs:

        id_cv = job.get_attribute("data-job-id")
    
        title = job.find_element(
            By.CSS_SELECTOR, "h3.title"
        ).text

        company = job.find_element(
            By.CSS_SELECTOR, ".company"
        ).text

        salary = job.find_element(
            By.CSS_SELECTOR, ".salary"
        ).text

        location = job.find_element(
            By.CSS_SELECTOR, ".city-text"
        ).text

        experience = job.find_element(
            By.CSS_SELECTOR, ".exp"
        ).text

        posted_time = job.find_element(
            By.CSS_SELECTOR,
                "label.label-update"
        ).text.strip()

        ids.append(id_cv)
        titles.append(title)
        companies.append(company)
        salaries.append(salary)
        locations.append(location)
        times.append(posted_time)  
        experiences.append(experience)


df = pd.DataFrame({
    "id": ids,
    "title": titles,
    "salary": salaries,
    "company": companies,
    "location": locations,
    "experience": experiences,
    "time": times
})

output_folder = r"D:\Python code\crawl_data_topcv\data"

os.makedirs(output_folder, exist_ok=True)

today = datetime.now().strftime("%Y%m%d")

output_file = os.path.join(
    output_folder,
    f"topcv_{today}.csv"
)

df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

driver.quit()
