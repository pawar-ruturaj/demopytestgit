# if a developer mark one of the test case as differed means there is no solution for that case now, but it will solve
# in upcoming build, so when we run all test cases, that differed test case always show Failed.so such test cases we
# need to skip while executing pytest. provision for that is decorators.
# we use --> @pytest.mark.skip
# here we skip test_mul_02.

# in result, it will show your skipped test cases and no. of test cases you skipped.

# if you know that your one of the test case failed, then you can use mark.xfail, in a result it will show XFAIL means
# you mark this case as fail and move forward.
# if you apply xfail on a passed test case, then it will show XPASS in a result.

# you can also execute test cases in sets/groups. e.g. we need to test 100 test cases and there are 10 cases for sanity
# testing or 10 for log in, 15 for orderamount and so on, so we can use decorators(markers) by grouping test cases by
# specific name in mark.groupname/setname.
# we can give multiple markers for the same test case
# here we create group for sum operations test cases and give name sum for that. then we execute that case in terminal
# like--> pytest -v -m sum

# we can apply marker using 'or' and 'and' conditions. e.g. -m group1 or group2.    -m group1 and group2
# collected 5 items / 3 deselected / 2 selected

# by using this technique, we can group our test cases like sanity, regression, login etc.
# -m for you can run the specific test case under marker.


import time

import pytest  # importing this for marker
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
class Test_py:
    @pytest.mark.sum
    def test_sum01(self):
        a = 5
        b = 3
        sum = a + b

        if sum == 8:
            print("test_sum_01 is passed")
            assert True
        else:
            print("test_sum_01 is failed")
            assert False

    @pytest.mark.skip
    def test_mul_02(self):
        a = 5
        b = 3
        mul = a * b

        if mul == 17:
            print("test_mul_02 is passed")
            assert True
        else:
            print("test_mul_02 is failed")
            assert False

    def sum_03(self):
        a = 5
        b = 3
        sum = a + b

        if sum == 8:
            print("test_sum_01 is passed")
            assert True
        else:
            print("test_sum_01 is failed")
            assert False

    # it will collect only 2 items(test cases), sum_03 is not taken into consideration as test case.

    # now we are testing the Google logo is present or not when we open it.

    @pytest.mark.group1
    def test_googlelogo_03(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com/")
        logo = driver.find_element(By.XPATH, "//img[@alt='Google']").is_displayed()
        print(logo)

        if logo == True:
            assert True
        else:
            assert False

    @pytest.mark.skip
    @pytest.mark.xfail
    def test_irctclogo_04(self):
        driver1 = webdriver.Firefox()
        driver1.get("https://www.irctc.co.in/nget/train-search")
        time.sleep(5)
        logo1 = driver1.find_element(By.CLASS_NAME, "pull-right h_logo_right_div").is_displayed()
        print(logo1)

        if logo1 == True:
            assert True
        else:
            assert False


    @pytest.mark.credence
    def test_credence(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        offer = driver.find_element(By.XPATH, "//span[@class='text-white b label']").text
        print(offer)

        if driver.title == "Credence":  # we get "credence" page title from html file of web
            assert True
        else:
            assert False

    # find specific contact number from contact of credence.in
    # we find CSS path in selectorshub find-->//div[5]/div/p/a[6]
    @pytest.mark.credence
    def test_credence2(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
        time.sleep(2)
        l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a"))
        list=[]

        for r in range(1,l+1):
            contact=driver.find_element(By.XPATH, "//div[@class ='quickfinder-description gem-text-output']//p//a["+str(r)+"]").text
            # print(contact)
            list.append(contact)

        if "+91 9091929355" in list:
            print(list.index("+91 9091929355"))
            assert True
        else:
            assert False
