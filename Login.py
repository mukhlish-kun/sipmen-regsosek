from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://sipmen.bps.go.id/regsosek/login")
# variable login
usernameData = '211709670@stis.ac.id'
passwordData = '12345678'

username = driver.find_element(By.ID, "email")
username.send_keys(usernameData)

password = driver.find_element(By.ID, "password")
password.send_keys(passwordData)

submit = driver.find_element(By.XPATH, "//button[@type='submit']")
submit.click()
assert "Berhasil login"