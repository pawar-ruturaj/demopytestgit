import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_002:
    @pytest.mark.sum
    def test_sum_04(self):
        a = 3
        b = 4
        sum = a + b
        if sum == 7:
            assert True
        else:
            assert False

    # there are two files test_file1 and 2 but when we run pytest at command prompt, both files run. don't run directly by
    # run, it will run only current file so run in command prompt.

    # if we want to run only test_file2, then run like- pytest -v test cases/test_file2.py( -v is optional)
    # ( copy this path from copy path from content root)
    # -v is for more details about test run.

    # if file name not starts with test_ prefix then also  it will not execute in pytest.
    # in class name test_ prefix is not compulsory.
    # so we can say that file name and method name should be starts with prefix test_ and
    # class name with this prefix is not compulsory.

    # we can also run test cases without opening browser. import below library for that
    # from selenium.webdriver.common.by import By
    # from selenium.webdriver.chrome import webdriver
    # from selenium import webdriver

    # use following method
    # chrome_options= webdriver.ChromeOptions()
    # chrome_options.add_argument("headless")

    # if developer mark one of the test case as differed means there is no solution for that case now, but it will solve
    # in upcoming build, so when we run all test cases, that differed test case always show Failed.so such test cases we
    # need to skip while executing pytest. provision for that is decorators.
    # we use --> @pytest.mark.skip
    # here we skip test_mul_02.

    # testcases/test_file1.py::Test_py::test_mul_02 SKIPPED (unconditional skip)
    # 3 passed, 1 skipped

    # in result, it will show your skipped test cases and no. of test cases you skipped

    # if you know that your one of the test case failed, then you can use mark.xfail, in result it will show XFAIL means
    # you mark this case as fail and move forward.
    # if you apply xfail on passed test case then it will show XPASS in result

    # you can also test cases in sets/groups. e.g. we need to test 100 teat cases and there are 10 cases for sanity
    # testing or 10 for log in, 15 for orderamount and so on, so we can use decorators(markers) by grouping test cases by
    # specific name in mark.groupname/setname.
    # we can give multiple markers for same test case
    # here we create group for sum operations test cases and give name sum for that. then we execute that case in terminal
    # like--> pytest -v -m sum
    # we can apply marker using 'or'  and 'and' conditions. e.g. -m group1 or group2.    -m group1 and group2
    # collected 5 items / 3 deselected / 2 selected

    # by using this technique we can group our test cases like sanity,regression,login etc.
    # -m for you can run the specific test case under marker

    # we can create report for our test run by using--> pytest -v --html=Reports/reports.html (Reports is folder name)
    # before that you need to install pytest-html library.

    # page title--> driver can identify page title, it will confirm you go to that page or not.

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
    # we find CSS path in selectorhub find-->//div[5]/div/p/a[6]
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

# type 'cls' in terminal to clear terminal.

# we are importing library--> 'pytestdist' for run test cases parallely, using this time for test case execution is
# reduced. to run parallely type in terminal= 'pytest -v -n=3'(-v is optional) no.3 represent how many worker
# processors you used to run this test.worker processor means how many memory of your RAM is consumed.
