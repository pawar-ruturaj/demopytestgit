import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_002:
    def test_sum_04(self):
        a = 3
        b = 4
        sum = a + b
        if sum == 7:
            assert True
        else:
            assert False

    # there are two files test_file1 and test_file2, but when we run pytest command at command prompt, both files run.
    # don't run directly by run button, it will run only the current file so run in command prompt.

    # if we want to run only test_file2, then run like--> pytest -v test cases/test_file2.py( -v is optional)
    # ( copy this path from copy path from content root) we give a path of file at cmd.
    # -v is for more details about test run.

    # if file name not starts with test_ prefix, then also it will not execute in pytest.
    # in class name test_ prefix is not compulsory.
    # so we can say that file name and method name should be started with prefix test_ and
    # class name with this prefix is not compulsory.

# refer test_file1 for headless browser.





