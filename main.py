from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import time
import pickle
import logging

url = 'https://vk.com'

#logging
logging.basicConfig(filename="error_log.txt", level=logging.ERROR)

# useragent = UserAgent()

options = webdriver.ChromeOptions()
#user agent
options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0")

#headless mode
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

#disable webdriver mode
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
     "source": """
          const newProto = navigator.__proto__
          delete newProto.webdriver
          navigator.__proto__ = newProto
          """
    })

#vk links
with open('vk_links\\user_links.txt') as file:
    links = [item.strip() for item in file]
    
try:
    # driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(10)
    # time.sleep(5)

    # log in
    print("Passing authentication...")
    input_email = driver.find_element("xpath", "//input[@id='index_email']")
    input_email.clear()
    input_email.send_keys("89386933282")
    driver.implicitly_wait(10)
    # time.sleep(5)

    input_email.send_keys(Keys.ENTER)
    time.sleep(5)

    input_password = driver.find_element("xpath", "//input[@name='password']")
    input_password.clear()
    input_password.send_keys("thelast0")
    driver.implicitly_wait(10)
    # time.sleep(5)

    input_password.send_keys(Keys.ENTER)
    time.sleep(7)

    # go to page
    print("Starting parcing..")
    counter = 0

    print(f"Всего {len(links)} строк")
    print("===============================")
    for link in links:
        counter += 1

        driver.get(link)
        driver.implicitly_wait(5)

        #finding more button
        more_btn = driver.find_element("xpath", "//span[contains(@class, 'vkuiTypography')][text()='Подробнее']")
        driver.implicitly_wait(5)
        # time.sleep(3)

        more_btn.click()
        driver.implicitly_wait(1)

        #finding phonenumber
        phonenumber = driver.find_elements("xpath", "//div[@class='ProfileModalInfoRow__label'][text()='Моб. телефон:']/following::div[@class='ProfileModalInfoRow__in'][1]")

        additional_phonenumber = driver.find_elements("xpath", "//div[@class='ProfileModalInfoRow__label'][text()='Доп. телефон:']/following::div[@class='ProfileModalInfoRow__in'][1]")

        if len(phonenumber) == 0 and len(additional_phonenumber) == 0:
            print(f"Строка {counter} не найдено номеров!")
            continue
        else:
            print(f"Строка {counter} найден номер:")
            if len(phonenumber) != 0:
                print(f"Номер телефона: {phonenumber[0].text}")
                with open ("new_numbers.txt", "a") as f:
                    f.write(phonenumber[0].text + '\n')
            if len(additional_phonenumber) != 0:
                print(f"Дополнительный номер телефона: {additional_phonenumber[0].text}")
                with open ("new_numbers.txt", "a") as f:
                    f.write(additional_phonenumber[0].text + '\n')
    print("DONE!")

except Exception as ex:
    print(f"ERROR ON {counter} LINE")
    print(ex)

    logging.error(ex, exc_info=True)
    with open ("error_log.txt", "a") as f:
        f.write(f"ERROR ON {counter} LINE")

        
finally:
    driver.close()
    driver.quit()


########################################

# # save cookies
# with open("file_cookies", 'wb') as file:
#     pickle.dump(driver.get_cookies(), file)

#load cookies

# driver.get(url)
# time.sleep(5)

# for cookie in pickle.load(open('89386933282_cookies', 'rb')):
#     driver.add_cookie(cookie)

# time.sleep(5)
# driver.refresh()
# time.sleep(10)


#close modal
# link_news = driver.find_element('xpath', "(//a[@class='LeftMenuItem-module__item--XMcN9'])[2]").click()
# time.sleep(10)