# for pytest we need to set default test runner is pytest from file->setting->python integrated tools
# without that setting pytest not run.

import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")  # this is for run without opening browser.


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

    # test_file1.py::Test_py::test_mul_02 PASSED.

    # case is failed, but it displays passed
    # but when we use assert, it will display filed case fail.
    # assert result and print statement are different it will display result in PASSED and FAILED depend upon condition.
    # it will give AssertionError. that means code is not incorrect but given condition is false.
    # if we not use assert failed case also shows as passed because code is correct,
    # so we use assert to determine your test case condition is passed or fail.
    # assert is not depend upon case is passed or not, if you give assert True for failed test case,
    # then that failed case shows passed in assert.
    # in pytest your function/method called test case, and it's name always starts with test_ prefix
    # otherwise it will not consider as a part of pytest

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

    # you can also run pytest framework at terminal/command prompt.

    # now we are testing the google logo is present or not when we open it.

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
