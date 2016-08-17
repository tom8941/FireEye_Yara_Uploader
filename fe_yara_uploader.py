#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import argparse

parser = argparse.ArgumentParser(description="Upload yara file to FireEye CMS")
parser.add_argument("-f", "--file", help="yara file to upload", required=True)
parser.add_argument("-c", "--cms", help="cms ip or hostname", required=True)
parser.add_argument("-u", "--user", help="cms user account", required=True)
parser.add_argument("-p", "--password", help="cms password", required=True)

args = parser.parse_args()

YARA_FILE_PATH = args.file
YARA_FILE_NAME = YARA_FILE_PATH.split("/")[-1]
CMS = args.cms

oldname=""

try:
    #Authentication
    driver = webdriver.Firefox()
    driver.get("https://" + CMS + "/yara/yara")
    elem = driver.find_element_by_id("user_account")
    elem.send_keys(args.user)
    elem2 = driver.find_element_by_id("user_password")
    elem2.send_keys(args.password)
    elem3 = driver.find_element_by_id("logInButton")
    elem3.submit()
    time.sleep(2)

    #Go to the YARA menu
    elem3a = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/ul/li[2]/a")
    elem3a.click()
    time.sleep(2)
    elem4 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[10]/a")
    elem4.click()
    time.sleep(2)

except Exception:
    print 'Failed to load last MISP yara rules in ' + YARA_FILE_NAME + ' (Navigation problem on the admin portal)'
    driver.close()
    exit()

#Add new Yara file
try:
    elem3a = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/ul/li[2]/a")
    elem3a.click()
    time.sleep(2)
    elem4 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[10]/a")
    elem4.click()
    time.sleep(2)
    
    #upload the file
    elem6 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div/div/div/div[2]/div[5]/div/table/tbody/tr/td[2]/input")
    elem6.send_keys(YARA_FILE_PATH);
    time.sleep(2)
    elem7 = driver.find_element_by_id("yara_upload")
    elem7.click()
    time.sleep(30)

except Exception:
    print 'Failed to load last MISP yara rules in ' + YARA_FILE_NAME + ' (Impossible to click on upload button)'
    driver.close()
    exit()

try:
    elem8 = driver.find_element_by_class_name("alert-danger")

    print 'Failed to load last MISP yara rules in ' + YARA_FILE_NAME + ' (Some Yara rules contain errors)' # print only if alert-danger exists
    driver.close()
    exit()

except Exception:  # if error message is missing Exception is raised
    pass

print 'Auto Upload successfull of Yara rules : ' + YARA_FILE_NAME

exit()
