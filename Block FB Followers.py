from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import keyboard
fb_user = input("Enter your facebook username: ")
fb_pass = input("Enter your facebook password: ")
fb_id = input("Enter your facebook id: ")
options = Options()
options.add_argument("start-minimized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://m.facebook.com")
delay = 3
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'login')))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")
user_elm = driver.find_element(By.ID,'m_login_email')
pass_elm = driver.find_element(By.ID,'m_login_password')
login_btn_elm = driver.find_element(By.NAME,'login')
user_elm.send_keys(fb_user)
pass_elm.send_keys(fb_pass)
login_btn_elm.click()
time.sleep(3)
"""try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'fb_dtsg')))
except TimeoutException:
    print ("Loading took too much time!")
    """
while True:
    driver.get("https://m.facebook.com/" + fb_id + "?v=followers")
    #time.sleep(3)
    """try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'image')))
    except TimeoutException:
        print ("Loading took too much time!")"""
    time.sleep(3)
    ret = driver.execute_script('function getElementByXpath(e) { return document.evaluate(e, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; } function sleep(e) { return new Promise((o) => setTimeout(o, e)); } function get_url() { return window.location.href; } function check_fb_platform() { return get_url().indexOf("m.facebook.com") >= 0 ? 1 : 0; } function get_followers_quantity() { return getElementByXpath(`//*[@id="timelineBody"]/div/div/header/div/div/div/div/span`).innerHTML; } function block_user() { document.getElementsByClassName("touchable primary")[0].click(), sleep(3000).then(() => { document.getElementsByClassName("_8hq7 _8hp3 _56br")[1].click(); let e = get_url(), o = getElementByXpath(`//*[@id="root"]/div[2]/div/div/div[2]`).childNodes.length; (blck_btn_elm = getElementByXpath(2 == o ? `//*[@id="root"]/div[2]/div/div/div[2]/a[2]` : 3 == o ? `//*[@id="root"]/div[2]/div/div/div[2]/a[3]` : `//*[@id="root"]/div[2]/div/div/div[2]/a[4]`)).click(), sleep(1e3).then(() => { (cf_blck_elm = document.getElementsByName("confirmed")[0].click()), console.clear(), console.log("🚫 User blocked: " + e), sleep(1500).then(() => { window.close(); }); }); }); } var blck_btn_elm; console.clear(), 1 == check_fb_platform() ? (console.log("Số người follower là: " + get_followers_quantity()), block_user()) : console.log("Sai đường dẫn facebook platform. Vui lòng sử dụng `m.facebook.com`");')
    print(ret)
    """blocked_count = blocked_count + 1
    print(blocked_count)
    if blocked_count == 5:
        time.sleep(120)
        blocked_count = 0"""
    if keyboard.is_pressed("del"):
        print("delete key pressed, ending loop")
        break
