from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    dr = webdriver.Chrome(options=options, executable_path='./chromedriver.exe')
    dr.get('https://docs.google.com/forms/d/e/1FAIpQLScurc0oOMpIxUfhWEcrcvPZYgc2EP_nwv684U4bEgz7VNhLqA/viewform')

    element_email = dr.find_element(By.CSS_SELECTOR, 'input.quantumWizTextinputPaperinputInput[autocomplete="email"]')
    element_email.send_keys("kuchriavy10@gmail.com")

    element_answer = dr.find_element(By.CSS_SELECTOR, 'input.quantumWizTextinputPaperinputInput[autocomplete="off"]')
    element_answer.send_keys('https://github.com/pavlokucheriavyi/learnpython/tree/main/HT_16')

    send_on_user_email_form_element = dr.find_element(By.CSS_SELECTOR, 'div.quantumWizTogglePapertoggleThumb')
    send_on_user_email_form_element.click()

    dr.save_screenshot('1.png')

    submit_element = dr.find_element(By.CSS_SELECTOR, 'div.freebirdFormviewerViewNavigationSubmitButton')
    submit_element.click()
    sleep(12)

    dr.save_screenshot('2.png')
    dr.quit()


if __name__ == "__main__":
    main()