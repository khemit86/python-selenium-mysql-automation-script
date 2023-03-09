def click(portno):
    from importlib.resources import path
    from weakref import WeakValueDictionary
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import TimeoutException
    import os
    import time
    import openpyxl
    from datetime import datetime
    import pymysql
    from selenium.webdriver.chrome.options import Options

    cardno = "xxxxx"
    exp = "xxx"
    cvv = "xxx"
    name = "xxx"


    voucher="xxxxxxx"

    pot = "localhost:"+str(portno)
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", pot)
    chrome_driver = "E:\chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

    #print("1 Step Working")
    driver.get('https://www.swiggy.com/checkout')

    # # time.sleep(3)
    # print("1+1 Step Working")
    # element=WebDriverWait(driver,3000).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[1]/div')))

    # # apply = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[6]/div[1]')

    # try: 
    #     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[6]/div[1]')
    #     xyz = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[6]/div[1]').text
    #     print(xyz)
    #     if xyz == "Apply Coupon":
    #         print("Apply Coupon Found on 6 posi")
    #         aggri='/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[6]/div[1]' 
    #     else:
    #         print("Apply Coupon not Found on 6 posi")
    #         aggri='/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[5]/div[1]'
        
    # except NoSuchElementException:
    #     print("first Valve not Found")
    #     aggri='/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[5]/div[1]'
        

    
    
    
    # print(aggri)
    
    
    
    


    # time.sleep(2)
    # driver.find_element_by_xpath(aggri).click()

    # element=WebDriverWait(driver,3000).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div[2]/form/div/input')))
    # driver.find_element_by_xpath('//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div[2]/form/div/input').send_keys(voucher)
    # element=WebDriverWait(driver,3000).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div[2]/form/a')))
    # driver.find_element_by_xpath('//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div[2]/form/a').click()
    # #element=WebDriverWait(driver,3000).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/button')))
    # time.sleep(1)

    # # try: 
    # #     driver.find_element_by_xpath('/html/body/div[4]/div/div/button')
    # #     xyz = driver.find_element_by_xpath('/html/body/div[4]/div/div/button').text
    # #     print(xyz)

    # #     if xyz == "YAY!":
    # #         print("Apply Coupon Found on 4 posi")
    # #         aggri1='/html/body/div[4]/div/div/button' 
    # #     else:
    # #         print("Apply Coupon not Found on 4 posi")
    # #         aggri1='/html/body/div[5]/div/div/button'
        
    # # except NoSuchElementException:
    # #     print("first Valve not Found")
    # #     aggri1='/html/body/div[5]/div/div/button'
      
      

    # # driver.find_element_by_xpath(aggri1).click()


    # driver.get("https://www.swiggy.com/checkout")

    element=WebDriverWait(driver,3000).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[2]/div[2]')))
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[2]/div[2]').click()





    element=WebDriverWait(driver,3000).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]')))
    print("2 Step Working")

    driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]').click()

    
    #time.sleep(2)
    print("3 Step Working")
    element=WebDriverWait(driver,3000).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="cardNumber"]')))
    print("4 Step Working")

    driver.find_element_by_xpath('//*[@id="cardNumber"]').send_keys(cardno)
    driver.find_element_by_xpath('//*[@id="expiry"]').send_keys(exp)
    driver.find_element_by_xpath('//*[@id="cvv"]').send_keys(cvv)
    driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
    driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div').click()

    print("Data Enter Successfully")

    connection = pymysql.connect(host="216.10.247.238", user="rdjm_live_1", passwd="hArsh@123", database="rdjm_text")
    cursor = connection.cursor()

    updateSql = "UPDATE  Server_status SET Status = '2' WHERE Serial_no = '1' ";
    cursor.execute(updateSql)
    connection.commit()


    i = 1
    while i < 500:
        time.sleep(5)
        connection = pymysql.connect(host="216.10.247.238", user="rdjm_live_1", passwd="hArsh@123", database="rdjm_text")
        cursor = connection.cursor()

        retrivelspid = "Select Status from Server_status where Serial_no='1' ";
        cursor.execute(retrivelspid)
        rows = cursor.fetchall()

        for row2 in rows:
            continue

        loginvalue = row2[0]


        print(loginvalue)

        if loginvalue == 1:
            print("Server Started")

            i = i + 1000


        else:
            print("Server Not Yet Start")


        i = i


    connection = pymysql.connect(host="216.10.247.238", user="rdjm_live_1", passwd="hArsh@123", database="rdjm_text")
    cursor = connection.cursor()

    retrivelspid = "Select Last_ping from Server_status where Serial_no='1' ";
    cursor.execute(retrivelspid)
    rows = cursor.fetchall()

    for row2 in rows:
        continue

    systemtime = row2[0]



    i=1

    while i < 500:
        nowtime = datetime.now()
        if nowtime < systemtime:
            print("timeleft in ordring")
        else:
            print("time to order")
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[4]').click()
            print("Ordered Placed")
            updateSql = "INSERT INTO `swiggy_time`(`id`, `time stamp`) VALUES ('',%s)";
            cursor.execute(updateSql, nowtime)
            connection.commit()
            i = i + 1000
        i = i


    time.sleep(3)

    #element=WebDriverWait(driver,3000).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="securePay"]')))
    #driver.find_element_by_xpath('//*[@id="securePay"]').click()
    exit()


#clickswiggy(9002);

