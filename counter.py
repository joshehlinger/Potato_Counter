import time
import argparse
from selenium import webdriver


def count_potatoes(config):
    driver = webdriver.Chrome()
    try:
        driver.get('http://www.neopets.com/medieval/potatocounter.phtml')

        #Login
        login_form = driver.find_element_by_class_name('welcomeLoginContent')
        username_login = login_form.find_element_by_name('username')
        password_login = login_form.find_element_by_name('password')
        username_login.clear()
        username_login.send_keys(config.username)
        password_login.clear()
        password_login.send_keys(config.password)
        login_button = driver.find_element_by_class_name('welcomeLoginButton')
        login_button.click()

        #Count those taters
        counter = 0
        potatable = driver.find_element_by_xpath("//td[@class='content']/table[1]")
        for row in potatable.find_elements_by_xpath(".//tr"):
            for td in row.find_elements_by_xpath(".//img"):
                counter += 1

        guess_input = driver.find_element_by_name('guess')
        guess_input.clear()
        guess_input.send_keys(counter)

        time.sleep(15)
        driver.quit()

    except Exception:
        driver.quit()


def arg_parser() -> argparse.ArgumentParser:
    desc = 'It counts potatoes guys'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--username',
                        dest='username',
                        metavar='',
                        help='Potato Name')
    parser.add_argument('--password',
                        dest='password',
                        metavar='',
                        help='Potato Pass')
    return parser


def main(args=None):
    parser = arg_parser()
    config = parser.parse_args(args=args)
    count_potatoes(config)


if __name__ == '__main__':
    main()