# for pytest we need to set default test runner is pytest from file->setting->python integrated tools
# without that setting pytest not run.

import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")  # this is for run without opening browser.


# class Test_py:
#     def test_sum01(self):
#         a = 5
#         b = 3
#         sum = a + b
#
#         if sum == 8:
#             print("test_sum_01 is passed")
#
#         else:
#             print("test_sum_01 is failed")
#
#     def test_mul_02(self):
#         a = 5
#         b = 3
#         mul = a * b
#
#         if mul == 17:
#             print("test_mul_02 is passed")
#
#         else:
#             print("test_mul_02 is failed")

# test_file1.py::Test_py::test_mul_02 PASSED.
# case is failed, but it displays PASSED.
# but when we use assert, it will display failed case fail and passed test case Passed.
# assert result and print statement are different it will display result in PASSED and FAILED depend upon condition.
# it will give AssertionError.that means the code is correct but given condition is false.
# if we do not use assert failed case also shows as passed because code is correct,
# so we use assert to determine your test case condition is passed or fail.
# assert is not depend upon a case is passed or not, if you give assert True for failed test case,
# then that failed case shows passed in assert.
# when assert condition satisfies in method (True or False) the code after that assert in method not run.


# in pytest your function/method called test case, and its name always starts with test_ prefix,
# so call method to testcases.
# otherwise, it will not be considered as a part of pytest.
# class name is starts with "Test" T is always capital, otherwise it shows Empty suite.
# you can also run a pytest framework at terminal.open terminal and type 'pytest' then enter.
# if you type--> pytest -v in cmd/terminal, it will show additional info about your test cases in the terminal.
# for run in command prompt open project folder, type cmd on a folder path, it will redirect on cmd.

# comment above code rewrite code using assert

class Test_py:

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

    def test_mul_02(self):
        a = 5
        b = 3
        mul = a * b

        if mul == 15:
            print("test_mul_02 is passed")
            assert True
        else:
            print("test_mul_02 is failed")
            assert False

    # now take a new test case for Google logo find or not

    def test_googlelogo_03(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        logo = driver.find_element(By.XPATH, "//img[@alt='Google']").is_displayed()
        # is.displayed() check logo is dispay or not
        print(logo)

        if logo == True:
            assert True
        else:
            assert False

    # after that, refer test_file2 for condition when testcase(method) name is same.

    # we can also run test cases without opening a browser.
    # comment above testcase of google, we run that testcase in headless mode
    # import below library for that
    # from selenium.webdriver.common.by import By
    # from selenium.webdriver.chrome import webdriver
    # from selenium import webdriver

    # use the following method
    # chrome_options= webdriver.ChromeOptions()
    # chrome_options.add_argument("headless")
    def test_googlelogo_04(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com/")
        logo = driver.find_element(By.XPATH, "//img[@alt='Google']").is_displayed()
        # is.displayed() check logo is display or not
        print(logo)

        if logo == True:
            assert True
        else:
            assert False

# to create html report--> we can create report for our test run by using--> pytest -v --html=Reports/reports.html
# (Reports is folder name where we save report) before that you need to install pytest-html library.

# page title--> a driver can identify page title, it will confirm you go to that page or not.
# type 'cls' in terminal to clear terminal.

# we are importing a library--> 'pytestdist' for run test cases parallely, using this time for test case execution is
# reduced.
# to run parallely type in terminal= 'pytest -v -n=3 (-v is optional)
# no.3 represents how many worker processors you used to run this test.
# worker processor means how many memory of your RAM is consumed.
