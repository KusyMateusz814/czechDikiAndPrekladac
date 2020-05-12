from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep 
import os
import sys
import argparse
import logging

sentence_var=''

def def_slovnicek_cz(args):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    url=''
    if args.czeskipolski:
        url="https://www.slovnicek.cz/cesko-polsky-prekladac"
    elif args.polskiczeski:
        url="https://www.slovnicek.cz/polsko-cesky-prekladac"
    elif args.polskirosyjski:
        url="https://www.slovnicek.cz/polsko-rusky-prekladac"
    elif args.rosyjskipolski:
        url="https://www.slovnicek.cz/rusko-polsky-prekladac"
    else:
        url='brak'
    if args.loghami:
        logging.debug("wygenerowany url")
    sentence_var=args.sentence    
    driver.get(url)
    #refresh uzylem, bo przy pierwszym odpaleniu
    #wczytuje czesko-angielski
    driver.refresh()
    textArea=driver.find_element_by_xpath('//*[@id="translate_textarea"]')
    textArea.click()
    textArea.send_keys(sentence_var)
    prelozitBtn=driver.find_element_by_xpath('//*[@id="translate_button"]')
    prelozitBtn.click()
    sleep(1)
    prekladtext=driver.find_element_by_xpath('/html/body/section[1]/div[2]/div[2]/div[1]/div/div[2]')
    slovniktext=driver.find_element_by_xpath('//*[@id="result_slovnik"]')
    logging.debug(prekladtext.text)
    logging.debug(slovniktext.text)
    print('překlad: '+ prekladtext.text +'\n' "slovnik: " + slovniktext.text)
    sleep(1)
    driver.quit()

def def_params():
    parser = argparse.ArgumentParser(
        description='A test script for http://stackoverflow.com/q/14097061/78845'
    )
    parser.add_argument("-l", "--loghami", action='store_true', help="increase output verbosity", required=False)
    parser.add_argument("-cz-pl", "--czeskipolski", action='store_true', help="z czeskiego na polski", required=False)
    parser.add_argument("-pl-cz", "--polskiczeski", action='store_true', help="z polskiego na czeski", required=False)
    parser.add_argument("-pl-rus", "--polskirosyjski", action='store_true', help="z polskiego na rosyjski", required=False)
    parser.add_argument("-rus-pl", "--rosyjskipolski", action='store_true', help="z rosyjskiego na polski", required=False)
    parser.add_argument("-sent", "--sentence", help="sentencja do przetlumaczenia", required=True)
    args = parser.parse_args() # parsujemy argumenty aby wyłuskać przekazane w nich wartosci i wyświetlamy je na ekranie
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG)
    return args

def def_environment():
    path_to_dir = os.path.dirname(os.path.realpath(__file__))
    #print("Scieszka do folder:" + path_to_dir
    os.environ["PATH"] += os.pathsep + path_to_dir

def main():
    args=def_params()
    def_environment()
    logging.debug('Only shown in debug mode')
    def_slovnicek_cz(args)

if __name__ == "__main__":
    main() 
