from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import json
import os
import time


def get_review(element):
    review = element.find_element(By.CLASS_NAME, 'apphub_CardTextContent').text
    text_list = review.split('\n')
    text_list.pop(0)
    review = ' '.join(text_list)
    return review

def get_reviews_steam(types_of_reviews, language='english', number_of_revisions = 100, filename_save = 'review_data'):

    url = f'https://steamcommunity.com/app/1091500/{types_of_reviews}/?browsefilter=toprated&snr=1_5_100010_&filterLanguage={language}'

    driver = None

    try:
        driver = webdriver.Chrome(service=ChromeService('webdrivers\chromedriver.exe'))
        driver.set_page_load_timeout(30)  
        driver.get(url)
        driver.maximize_window()
        driver.find_element(By.XPATH,'//*[@id="responsive_page_template_content"]/div/div/div[2]/button[1]').click()
        iframe = driver.find_element(By.XPATH, '//*[@id="GetMoreContentBtn"]')
        list_of_reviews = []
        current_maximum_index = 0
        previous_maximum_index = 0

        while len(list_of_reviews) < number_of_revisions:
            print(f'previous_maximum_index: {previous_maximum_index}')

            elements = driver.find_elements(By.CLASS_NAME, 'apphub_Card')

            current_maximum_index = len(elements)

            if previous_maximum_index > 0:
                elements = elements[previous_maximum_index:]

            for element in elements:

                id = int(element.find_element(By.CLASS_NAME, 'apphub_friend_block').get_attribute('data-miniprofile'))
                review_text = get_review(element)
                rating = element.find_element(By.CLASS_NAME, 'title').text.lower()

                review = {
                    'id': id,
                    'review': review_text,
                    'rating':rating
                }

                if not any(l['id'] == review['id'] for l in list_of_reviews):
                    list_of_reviews.append(review)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5) 

            previous_maximum_index = current_maximum_index

            print(f'list_of_reviews: {len(list_of_reviews)}')

        review_data = []

        if os.path.exists(filename_save):
            with open(filename_save, encoding='utf-8') as f:
                review_data = json.load(f)

        for review in list_of_reviews:
            if not any(review['id'] == l['id'] for l in review_data):
                review_data.append(review)

        with open(filename_save, 'w', encoding='utf-8') as f:
            json.dump(review_data, f, sort_keys=True, indent=4, ensure_ascii=False)
    except Exception as e:
        print("Erro:", e)
    finally:
        driver.quit()