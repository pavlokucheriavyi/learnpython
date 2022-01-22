from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    dr = webdriver.Chrome(options=options, executable_path='./chromedriver.exe')
    dr.get('https://docs.google.com/forms/d/e/1FAIpQLScurc0oOMpIxUfhWEcrcvPZYgc2EP_nwv684U4bEgz7VNhLqA/viewform')
    current = dr.current_url
    try:
        element_of_email = WebDriverWait(dr, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input.quantumWizTextinputPaperinputInput[autocomplete="email"]')))
        element_of_email.send_keys("kuchriavy10@gmail.com")

        element_answer = WebDriverWait(dr, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input.quantumWizTextinputPaperinputInput[autocomplete="off"]')))
        element_answer.send_keys('https://github.com/pavlokucheriavyi/learnpython/tree/main/HT_17')

        send_on_user_email_form_element = WebDriverWait(dr, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.quantumWizTogglePapertoggleThumb')))
        send_on_user_email_form_element.click()

        WebDriverWait(dr, 5).until(
            EC.url_to_be(current))
        dr.save_screenshot('1.png')

        submit_element = WebDriverWait(dr, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.freebirdFormviewerViewNavigationSubmitButton')))
        submit_element.click()

        WebDriverWait(dr, 17).until(
            EC.url_changes(current))
        dr.save_screenshot('2.png')

    finally:
        dr.quit()


if __name__ == "__main__":
    main()