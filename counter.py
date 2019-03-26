#!/usr/bin/env python3
import time
import datetime
import sys
import argparse
from selenium import webdriver


def count_potatoes(config):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    try:
        print ('Run starting at ' + str(datetime.datetime.now()))
        driver.get('http://www.neopets.com/medieval/potatocounter.phtml')

        #Login
        print('Logging in...')
        login_form = driver.find_element_by_class_name('welcomeLoginContent')
        username_login = login_form.find_element_by_name('username')
        password_login = login_form.find_element_by_name('password')
        username_login.clear()
        username_login.send_keys(config.username)
        password_login.clear()
        password_login.send_keys(config.password)
        login_button = driver.find_element_by_class_name('welcomeLoginButton')
        login_button.click()
        print('Login successful')

        #Count those taters
        print('Counting Taters')
        counter = 0
        potatable = driver.find_element_by_xpath("//td[@class='content']/table[1]")
        for row in potatable.find_elements_by_xpath(".//tr"):
            for td in row.find_elements_by_xpath(".//img"):
                counter += 1
        print('Tater count complete - {} potatoes'.format(counter))

        guess_input = driver.find_element_by_name('guess')
        guess_input.clear()
        guess_input.send_keys(counter)

        submit_button = driver.find_element_by_xpath('//center/form[1]/input[3]')
        submit_button.click()
        print('Guessed successfully!')

        time.sleep(10)

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
    if config.username is None or config.password is None:
        print('Username and Password are required!')
        return 1
    
    count_potatoes(config)
    return 0


if __name__ == '__main__':
    sys.exit(main())