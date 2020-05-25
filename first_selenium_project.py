from selenium import webdriver
import time

browser = webdriver.Chrome("/home/neovo/Genel/chromedriver")

browser.get("https://www.forbes.com/powerful-brands/list/")

browser.fullscreen_window()

browser.get("https://www.forbes.com/companies/apple/?list=powerful-brands#1470ea125355")
time.sleep(2)

browser.set_window_size(1020,600)
time.sleep(2)

browser.save_screenshot("/home/neovo/Masaüstü/screen.png")
time.sleep(2)

browser.back()
time.sleep(2)

browser.quit()
