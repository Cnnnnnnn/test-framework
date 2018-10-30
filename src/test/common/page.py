import selenium.common.exceptions
from selenium.webdriver.support import expected_conditions
from src.test.common.browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


class Page(Browser):

    def __init__(self, page=None, browser_type='chrome'):
        self.accept_next_alert = True
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)

    def get_driver(self):
        return self.driver

    def refresh(self):
        self.driver.refresh()
        time.sleep(1)

    def find_element(self, *args):
        try:
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*args).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*args)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, args))

    def move_to_element(self, *args):
        ele = self.find_element(*args)
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(1)

    def switch_frame(self, name):
        return self.driver.switch_to_frame(name)

    def switch_default_content(self):
        return self.driver.switch_to_default_content()

    def switch_windows(self, new=True, old=False):
        windows = self.driver.window_handles
        if new:
            self.driver.switch_to_window(windows[1])
        if old:
            self.driver.switch_to_window(windows[0])

    def get_time(self, bottom=True):
        if bottom:
            place = '//div[@x-placement="bottom-start"]'
        else:
            place = '//div[@x-placement="top-start"]'

        # 设置为2017年12月30日
        time.sleep(1)
        self.driver.find_element_by_xpath(place+'/div[@class="el-picker-panel__body-wrapper"]/div/div[@class="el-date-picker__header"]/span[1]').click()
        self.driver.find_element_by_xpath(place+'/div[@class="el-picker-panel__body-wrapper"]/div/div[2]/table[@class="el-year-table"]/tbody/tr[3]/td[1]').click()
        self.driver.find_element_by_xpath(place+'/div[@class="el-picker-panel__body-wrapper"]/div/div[2]/table[@class="el-month-table"]/tbody/tr[3]/td[4]').click()
        self.driver.find_element_by_xpath(place+'/div[@class="el-picker-panel__body-wrapper"]/div/div[2]/table[@class="el-date-table"]/tbody/tr[5]/td[7]').click()
        time.sleep(1)

    def is_element_exist(self, *args):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(*args))
            return True
        except:
            return False

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except selenium.common.exceptions.NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            pass
