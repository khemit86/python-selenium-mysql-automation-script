def clickautoemitrafunding(portno):
    #from importlib.resources import path
    from selenium import webdriver
    from weakref import WeakValueDictionary
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import TimeoutException
    from selenium.common.exceptions import ElementClickInterceptedException
    from selenium.common.exceptions import ElementNotInteractableException
    from selenium.common.exceptions import UnexpectedAlertPresentException
    from selenium.webdriver.chrome.options import Options
    from anticaptchaofficial.imagecaptcha import imagecaptcha
    import re
    import os
    import time
    from datetime import datetime
    import pymysql
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning) 
    #from file_path import path
    portno = portno

    print("1 Step Working")

    connection = pymysql.connect(host="xxxxxxxx", user="xxxxxx", passwd="xxxx", database="xxxxx")
    cursor = connection.cursor()


    retrivelspid = "Select * from ports_lsp_details where port_no=%s";
    cursor.execute(retrivelspid, portno)
    rows = cursor.fetchall()
    updateSql = "UPDATE  ports_lsp_details SET login_status = '2' WHERE port_no = %s ";
    cursor.execute(updateSql, portno)
    connection.commit()


    data = len(rows)
    # print(data)

    if data !=0:
        a=1
        # print("success")

    else:
        print("No Port Found in DB")
        exit()

    for row1 in rows:
        a=1
        # print(row1)

    Serial_no_port_lsp = row1[0]
    ssoid = row1[4]
    password = row1[5]
    Id_start_status = row1[6]
    partner_code = row1[1]
    capture_api_key = row1[8]

    # print("Sso Id    - " + ssoid)
    # print("Password  - " + password)

    if Id_start_status ==1:
        print("Sso Id    - " + ssoid)
        print("Password  - " + password)
        print("Partner_code  - " + partner_code)
        print(capture_api_key)
        # print("success")

    else:
        print("Sso-Id is Deactivated")
        exit()


    retrivelspid = "Select capture_api_key from Kiosk_Details where partner_code = %s";
    cursor.execute(retrivelspid,partner_code)
    rows = cursor.fetchall()


    data = len(rows)
    # print(data)

    if data !=0:
        a=1
        # print("success")

    else:
        print("No KCode Found in DB of "+ partner_code +" Partner Code")
        exit()

    capture_api_key = rows[0][0]
    print(capture_api_key)
    print("2 Step Working")

    path="E:\\chromedriver_win32\chromedriver.exe"
    driver=webdriver.Chrome(path)
    driver.maximize_window()
    
    login(driver,portno,cursor,connection,ssoid,password,capture_api_key)

    i = 1
    while i < 10000000:

        try:

            try:
                driver.find_element("xpath", '//*[@id="cpBody_txt_Data1"]')
                login(driver,portno,cursor,connection,ssoid,password,capture_api_key)

            except:
                print("emitra id is login")
                a=a

            retrivelspid = "Select * from Kiosk_Details where partner_code = %s";
            cursor.execute(retrivelspid,partner_code)
            rows = cursor.fetchall()


            data = len(rows)
            # print(data)

            if data !=0:
                a=1
                # print("success")

            else:
                print("No KCode Found in DB of "+ partner_code +" Partner Code")
                idlogout(driver,portno,cursor,connection)
                exit()

            for row1 in rows:
                a=1
                # print(row1)

            kcode = row1[3]
            print("Kcode     - " + kcode)
            kcode_active_status = row1[6]
            db_table_name = row1[2]
            print(db_table_name)

            if kcode_active_status ==1:
                a=1
                # print("success")

            else:
                print("No Active KCode Found in DB of "+ partner_code +" Partner Code")
                idlogout(driver,portno,cursor,connection)
                exit()

                    
            login_remark = "Id Is Login"
            now = datetime.now()
            updateSql = "UPDATE  ports_lsp_details SET login_status = '1',last_ping = %s,Remark = %s WHERE port_no = %s ";
            inputdata = (now, login_remark,portno)
            cursor.execute(updateSql, inputdata)
            connection.commit()

            retrive = 'Select Serial_no_cards from {}'.format(db_table_name)+' where status_no_cards="0" ORDER BY status_no_cards ASC LIMIT 1';

            cursor.execute(retrive)
            rows = cursor.fetchall()
            data = len(rows)
            print(data)

            if data !=0:
                print("success")
            else:
                print("No Card Found")
                idlogout(driver,portno,cursor,connection)
                exit()

            for row2 in rows:
                print(row2)




            Card_serail_no = row2[0]
            print(Card_serail_no)

            updateSql = "UPDATE  {}".format(db_table_name)+" SET status_no_cards = '3' WHERE Serial_no_cards = %s ";
            cursor.execute(updateSql, Card_serail_no)
            connection.commit()

            Card_details = "select * from {}".format(db_table_name)+" where Serial_no_cards = %s";
            cursor.execute(Card_details, Card_serail_no)
            rows = cursor.fetchall()
            for row2 in rows:
                print(row2)


            update_serial_no = row2[0]
            card_number = row2[1]
            exp_month = row2[2]
            exp_year = row2[3]
            cvv = row2[4]
            ipin = row2[5]
            amount_payable = row2[6]
            trying_cards = row2[9]+1
            print(card_number, "|", exp_month,"-", exp_year,"|",cvv,"|",ipin,"|",amount_payable,"|",trying_cards)

            updateid = "UPDATE  {}".format(db_table_name)+" SET port_no_cards = %s , k_code_cards = %s,trying_cards = %s WHERE Serial_no_cards = %s ";
            inputdata = (portno, kcode,trying_cards,update_serial_no)
            cursor.execute(updateid, inputdata)
            connection.commit()

            element=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="getVendorData"]')))

            driver.find_element("xpath", '//*[@id="vendorCode"]').send_keys(kcode)


            element=WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="getVendorData"]')))

            driver.find_element("xpath", '//*[@id="getVendorData"]').click()


            element=WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="paymentModeTypeNetBId"]')))

            current_balance=driver.find_element("xpath", '//*[@id="fileData2"]/tr/td[8]').text  #//*[@id="fileData2"]/tr/td[8]
            print(current_balance)
            now = datetime.now() 
            updateid = "UPDATE  Kiosk_Details SET balance = %s , last_updated_balance = %s WHERE k_code = %s ";
            inputdata = (current_balance, now, kcode)
            cursor.execute(updateid, inputdata)
            connection.commit()


            print("1")

        
            try: 
                driver.find_element("xpath", '//*[@id="refillPayout"]/div/div[3]/div/div/div/div/div[1]/div/div/div[3]/div[1]/div/div/div[1]/div/a[4]')
                xyz = driver.find_element("xpath", '//*[@id="refillPayout"]/div/div[3]/div/div/div/div/div[1]/div/div/div[3]/div[1]/div/div/div[1]/div/a[4]').text

                if xyz == "Aggregator":
                    print("Aggregator Found on First Place")
                    aggri='//*[@id="refillPayout"]/div/div[3]/div/div/div/div/div[1]/div/div/div[3]/div[1]/div/div/div[1]/div/a[4]' 
                else:
                    print("Aggregator Not Found")
                    
            except NoSuchElementException:
                print("first Valve not Found")
                aggri='//*[@id="refillPayout"]/div/div[4]/div/div/div/div/div[1]/div/div/div[3]/div[1]/div/div/div[1]/div/a[4]'
            


            #print(aggri)

            driver.find_element("xpath", aggri).click()

            print("2")
            driver.find_element("xpath", '//*[@id="bankTypeAggr"]').click()
            print("3")
            
            driver.find_element("xpath", '//*[@id="bankTypeAggr"]/option[9]').click()
            driver.find_element("xpath", '//*[@id="pay-text"]').send_keys(amount_payable)
            driver.find_element("xpath", '//*[@id="paymentModeTypeAggrId"]').click()

            element=WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/table/tbody/tr[22]/td/table/tbody/tr/td[1]/button')))

            driver.find_element("xpath", '/html/body/form/table/tbody/tr[22]/td/table/tbody/tr/td[1]/button').click()

            element=WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="proceedForm"]')))

            driver.find_element("xpath", '//*[@id="cnumber"]').send_keys(card_number)
            driver.find_element("xpath", '//*[@id="expmon"]').send_keys(exp_month)
            driver.find_element("xpath", '//*[@id="expyr"]').send_keys(exp_year)
            driver.find_element("xpath", '//*[@id="cvv2"]').send_keys(cvv)
            driver.find_element("xpath", '//*[@id="cname2"]').send_keys("sksdfjldf")
            print("Cards Details Entered Successfully")
            driver.find_element("xpath", '//*[@id="proceedForm"]').click()

            element=WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="confirmTrxn"]')))
            total_amount = driver.find_element("xpath", '//*[@id="chargesModal"]/div/div[1]/div/ul/li/span').text
            print(total_amount)
            driver.find_element("xpath", '//*[@id="confirmTrxn"]').click()
            print("Card Button Press Successfully")

            try:

                element=WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="btnSubmitId"]')))
                driver.find_element("xpath", '//*[@id="pwd"]').send_keys(ipin)
                print("Ipin Successful Entered")

                driver.find_element("xpath", '//*[@id="btnSubmitId"]').click()
                print("Ipin Button Successful Pressed")

                element=WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="getVendorData"]')))
                print("WebPage Successfully Come To Meitra")

                
                try:
                    driver.find_element("xpath", '//*[@id="refillPayout"]/div/div[3]')   # //*[@id="refillPayout"]/div/div[3]
                    transaction_id=driver.find_element("xpath", '//*[@id="refillPayout"]/div/div[3]').text  # //*[@id="refillPayout"]/div/div[3]
                    print(transaction_id)
                    track_status = "Successful"
                    track_status_1 = "Failed"
                    if track_status in transaction_id:
                        remark = ""
                        now = datetime.now()
                        updateSstatus = "UPDATE  {}".format(db_table_name)+" SET emitra_status = 'Successful',reference_no_of_status=%s, status_no_cards = '1',previous_balance = %s , date_time_cards = %s , Remark = %s WHERE Serial_no_cards = %s ";
                        inputdata = (transaction_id,current_balance,now,remark, update_serial_no)
                        cursor.execute(updateSstatus, inputdata)
                        connection.commit()
                    elif track_status_1 in transaction_id:
                        transaction_id = "Transaction Failed. After Ipin Entered"
                        print(transaction_id)

                        now = datetime.now()
                        updateSstatus = "UPDATE  {}".format(db_table_name)+" SET status_no_cards = '2',Remark = %s,date_time_cards = %s WHERE Serial_no_cards = %s ";
                        inputdata = (transaction_id,now, update_serial_no)
                        cursor.execute(updateSstatus, inputdata)
                        connection.commit()
                    else:
                        transaction_id = "Transaction Failed. No reason found. After Ipin Entered"
                        print(transaction_id)

                        now = datetime.now()
                        updateSstatus = "UPDATE  {}".format(db_table_name)+" SET status_no_cards = '4',Remark = %s,date_time_cards = %s WHERE Serial_no_cards = %s ";
                        inputdata = (transaction_id,now, update_serial_no)
                        cursor.execute(updateSstatus, inputdata)
                        connection.commit()


                except NoSuchElementException:
                    driver.find_element("xpath", '//*[@id="command"]/div/div/div')
                    transaction_id=driver.find_element("xpath", '//*[@id="command"]/div/div/div').text
                    print(transaction_id)

                    print("Transaction Failed.")
                    transaction_id = "Transaction Failed. After Ipin Entered(Found Failed on E-Mitra)"
                    print(transaction_id)

                    now = datetime.now()
                    updateSstatus = "UPDATE  {}".format(db_table_name)+" SET status_no_cards = '2',Remark = %s,date_time_cards = %s WHERE Serial_no_cards = %s ";
                    inputdata = (transaction_id,now, update_serial_no)
                    cursor.execute(updateSstatus, inputdata)
                    connection.commit()

                except TimeoutException:
                    print("Transaction Failed.")
                    transaction_id = "Transaction Failed. After Ipin Entered(Page not found)"

                    now = datetime.now()
                    updateSstatus = "UPDATE  {}".format(db_table_name)+" SET status_no_cards = '2',Remark = %s,date_time_cards = %s WHERE Serial_no_cards = %s ";
                    inputdata = (transaction_id,now, update_serial_no)
                    cursor.execute(updateSstatus, inputdata)
                    connection.commit()

            except TimeoutException:
                    print("Transaction Failed.")
                    transaction_id = "Transaction Failed. without Ipin Entered"

                    now = datetime.now()
                    updateSstatus = "UPDATE  {}".format(db_table_name)+" SET status_no_cards = '6',Remark = %s,date_time_cards = %s WHERE Serial_no_cards = %s ";
                    inputdata = (transaction_id,now, update_serial_no)
                    cursor.execute(updateSstatus, inputdata)
                    connection.commit()


            print("================================================================================================================")
            print(i)

        except (TimeoutException,ElementClickInterceptedException,ElementNotInteractableException,UnexpectedAlertPresentException,NoSuchElementException):
            print("Transaction Failed. Some page not Response")
            transaction_id = "Transaction Failed. Some page not Response"
            driver.get("https://emitraapp.rajasthan.gov.in/emitraApps/refillByLsp")


            now = datetime.now()
            updateSstatus = "UPDATE  {}".format(db_table_name)+" SET status_no_cards = '5',Remark = %s,date_time_cards = %s WHERE Serial_no_cards = %s ";
            inputdata = (transaction_id,now, update_serial_no)
            cursor.execute(updateSstatus, inputdata)
            connection.commit()



        i = i+1

    print("=================done===========================")

    idlogout(driver,portno,cursor,connection)
    exit()

def idlogout(driver,portno,cursor,connection):
    # driver.get("https://emitraapp.rajasthan.gov.in/emitraApps/refillByLsp")
    driver.find_element("xpath", '/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]').click()
    driver.find_element("xpath", '/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div/ul/li[2]/a').click()
    remark_logout = "E-Mitra Id Logout"
    updateSql = "UPDATE  ports_lsp_details SET login_status = '0',Remark=%s WHERE port_no = %s";
    inputdata = (remark_logout,portno)
    cursor.execute(updateSql, inputdata)
    connection.commit()
    connection.close()
    print("E-Mitra Id Logout Successfully")
    print("working")
    driver.close()



def login(driver,portno,cursor,connection,ssoid,password,capture_api_key):
    from selenium import webdriver
    from anticaptchaofficial.imagecaptcha import imagecaptcha
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from datetime import datetime
    #from file_path import filename_capture

    driver.get("https://sso.rajasthan.gov.in/signin")


    element=WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cpBody_btn_LDAPLogin"]')))

    driver.find_element("xpath", '//*[@id="cpBody_txt_Data1"]').send_keys(ssoid)
    driver.find_element("xpath", '//*[@id="cpBody_txt_Data2"]').send_keys(password)
    
    """
    driver.find_element("xpath", '//*[@id="cpBody_ssoCaptcha_txtCaptcha"]').send_keys("")

    now = datetime.now()
    updateSql = "UPDATE  ports_lsp_details SET login_status = '2',last_ping = %s,Remark = 'Waiting For Capture' WHERE port_no = %s ";
    inputdata = (now,portno)
    cursor.execute(updateSql, inputdata)
    connection.commit()

    # capture process start #

    img = driver.find_element_by_xpath('//*[@id="cpBody_ssoCaptcha_imgCaptcha"]')
    src = img.get_attribute('src')

    filename = filename_capture +str(portno)+".png"

    with open(filename, 'wb') as file:
        file.write(driver.find_element_by_xpath('//*[@id="cpBody_ssoCaptcha_imgCaptcha"]').screenshot_as_png)

    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key(capture_api_key)

    solver.set_soft_id(0)

    captcha_text = solver.solve_and_return_solution(filename)
    if captcha_text != 0:
        print("captcha text "+captcha_text)
    else:
        print("task finished with error "+solver.error_code)

    driver.find_element_by_xpath('//*[@id="cpBody_ssoCaptcha_txtCaptcha"]').send_keys(captcha_text)
    """
    
    #driver.find_element_by_xpath('//*[@id="cpBody_btn_LDAPLogin"]').click()


    # capture process end #
    # time.sleep(10)
    try:
        driver.find_element("xpath", '//*[@id="cpBody_txt_Data2"]')
        driver.find_element_by_xpath('//*[@id="cpBody_txt_Data2"]').send_keys(password)
        driver.find_element_by_xpath('//*[@id="cpBody_cbx_newsession"]').click()
        driver.find_element_by_xpath('//*[@id="cpBody_btn_LDAPLogin"]').click()


    except:
        #driver.find_element("xpath", '//*[@id="cpBody_dlApplications_LinkButton2_0"]/div')
        print("1")
    
    element=WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cpBody_dlApplications_LinkButton2_0"]')))
    
    now = datetime.now()
    updateSql = "UPDATE  ports_lsp_details SET login_status = '2',last_ping = %s,Remark = 'Login In Process...' WHERE port_no = %s ";
    inputdata = (now,portno)
    cursor.execute(updateSql, inputdata)
    connection.commit()

    #driver.find_element("xpath", '//*[@id="cpBody_dlApplications_LinkButton2_0"]/div').click()
    driver.find_element("xpath", '//*[@id="cpBody_dlApplications_LinkButton2_0"]').click()

    element=WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="iAccept"]')))

    driver.find_element("xpath", '//*[@id="iAccept"]').click()
    driver.find_element("xpath", '/html/body/div/div[3]/div/div[7]/div[2]/input[2]').click()
    driver.get("https://emitraapp.rajasthan.gov.in/emitraApps/refillByLsp")

    login_remark = "Successful Login"
    print(login_remark)

    now = datetime.now()
    updateSql = "UPDATE  ports_lsp_details SET login_status = '1',login_date_time = %s,last_ping = %s,Remark = %s WHERE port_no = %s ";
    inputdata = (now,now, login_remark,portno)
    cursor.execute(updateSql, inputdata)
    connection.commit()

#from multiprocessing import Pool
#if __name__ == '__main__':
#   with Pool(processes=4) as p:
#       print(p.map(clickautoemitrafunding, [9001,9002,9003,9004]))

#clickautoemitrafunding(9001)

import threading
if __name__=='__main__':
    p1 = threading.Thread(target=clickautoemitrafunding, args=[9001])
    p2 = threading.Thread(target=clickautoemitrafunding, args=[9002])
    p1.start();
    p2.start()