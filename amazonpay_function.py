def test(portno):
    from datetime import time
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.chrome.options import Options
    options = Options()
    s = Service("E:\\chromedriver_win32\chromedriver.exe")
    localhost = "localhost:"+str(portno)
    options.add_experimental_option("debuggerAddress", localhost)
    driver = webdriver.Chrome(service=s, options=options)
    action = ActionChains(driver)
    time.sleep(1)
    driver.get("https://www.facebook.com/")

def amazon_pay(portno):
    from datetime import time
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.chrome.options import Options
    options = Options()
    s = Service("E:\\chromedriver_win32\chromedriver.exe")
    localhost = "localhost:"+str(portno)
    options.add_experimental_option("debuggerAddress", localhost)
    driver = webdriver.Chrome(service=s, options=options)
    action = ActionChains(driver)
    time.sleep(1)
    driver.get("https://www.amazon.in/")
    #time.sleep(3)
    firstLevelMenu = driver.find_element("xpath", '//*[@id="nav-link-accountList"]')
    action.move_to_element(firstLevelMenu).perform()

    secondLevelMenu = driver.find_element("xpath", '//*[@id="nav-flyout-ya-signin"]/a')
    secondLevelMenu.click()
    #time.sleep(3)

    signinelement = driver.find_element("xpath", '//*[@id="ap_email"]')
    signinelement.send_keys('xxxxxx')
    time.sleep(3)

    cont = driver.find_element("xpath",'//*[@id="continue"]')
    cont.click()
    time.sleep(1)

    passwordelement = driver.find_element("xpath",'//*[@id="ap_password"]')
    passwordelement.send_keys('xxxxxxx')
    time.sleep(1)

    login = driver.find_element("xpath",'//*[@id="signInSubmit"]')
    login.click()
    time.sleep(1)


    amazonPay = driver.find_element(By.LINK_TEXT,"Amazon Pay")
    amazonPay.click()
    time.sleep(3)

    amazonaddMoney = driver.find_element("xpath",'//*[@id="AddMoney"]/div[2]/span/a')
    amazonaddMoney.click()
    time.sleep(1)

    load_amount = driver.find_element("xpath",'//*[@id="adm-load-amount"]')
    load_amount.send_keys(Keys.CONTROL + "a")
    load_amount.send_keys("1")
    time.sleep(1)

    submit_amount = driver.find_element("xpath",'//*[@id="a-autoid-4"]/span/input')
    submit_amount.click()
    time.sleep(2)

    payment_method_type = driver.find_element("xpath", "//input[@value='SelectableAddCreditCard']")
    payment_method_type.click()
    time.sleep(1)


    plus_icon = driver.find_element("xpath", '//*[@id="apx-add-credit-card-action-test-id"]/div/img[1]')
    plus_icon.click()
    time.sleep(5)

    driver.switch_to.frame('ApxSecureIframe')

    credit_card_number_element = driver.find_element(By.NAME , "addCreditCardNumber")
    credit_card_number_element.send_keys(Keys.CONTROL + "a")
    credit_card_number_element.send_keys("4018066748021436")

    accountHolderName = driver.find_element(By.NAME , "ppw-accountHolderName")
    accountHolderName.send_keys(Keys.CONTROL + "a")
    accountHolderName.send_keys("manish sharma")

    Select(driver.find_element(By.NAME , "ppw-expirationDate_month")).select_by_value('10')
    Select(driver.find_element(By.NAME , "ppw-expirationDate_year")).select_by_value('2023')
    driver.find_element(By.NAME , "ppw-widgetEvent:AddCreditCardEvent").click()
    time.sleep(5)

    cvv_element = driver.find_element(By.NAME , "addCreditCardVerificationNumber0")
    cvv_element.send_keys("285")
    time.sleep(2)

    driver.find_element(By.NAME , "ppw-widgetEvent:SetPaymentPlanSelectContinueEvent").click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, "div#a-popover-3 .a-button-inner").click()
    time.sleep(5)

    driver.find_element(By.NAME , "placeYourOrder1").click()
    time.sleep(60)







