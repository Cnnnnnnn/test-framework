from src.test.common.page import Page
from selenium.webdriver.common.by import By
import time


class WorkOrderListPage(Page):
    add_button = (By.XPATH, '//*[@id="afterService"]/div[1]/div[1]/button[1]')
    LIST = '//div[@id="table_order"]/table/tbody'
    # 第一条数据
    customer_loc = (By.XPATH, LIST + '/tr[1]/td[3]/span/div/a/span')
    product_loc = (By.XPATH, LIST + '/tr[1]/td[4]')
    detail_loc = (By.XPATH, LIST + '/tr[1]/td[5]/div/a/p')
    creator_loc = (By.XPATH, LIST + '/tr[1]/td[6]/span')
    sales_department_loc = (By.XPATH, LIST + '/tr[1]/td[9]/div/div/p[1]')
    it_department_loc = (By.XPATH, LIST + '/tr[1]/td[10]/div/div/p[1]')
    # 指派相关
    assign_input = (By.XPATH, '//*[@id="table_order"]/div[2]/div[1]/label/div/div/div[1]/input')
    assign_drop_box = (By.XPATH, '/html/body/div/div/div[1]/ul/li[1]')
    assign_confirm = (By.XPATH, '//*[@id="table_order"]/div[2]/div[2]/a[1]')
    
    def __init__(self, page):
        super().__init__(page)
        self.tr = None

    def get_order_id_loc(self, tr):
        return By.XPATH, self.LIST + '/tr[%s]/td[2]' % tr

    def get_detail_info_loc(self, tr):
        return By.XPATH, self.LIST + '/tr[%s]/td[5]/div/a/p' % tr

    def get_status_loc(self, tr):
        return By.XPATH, self.LIST + '/tr[%s]/td[7]/span' % tr

    def get_handler_info_loc(self, tr):
        return By.XPATH, self.LIST + '/tr[%s]/td[9]/div/div/p[1]' % tr

    def get_assign_button_loc(self, tr):
        return By.XPATH, self.LIST + '/tr[%s]/td[9]/div/div/p[1]/a' % tr

    def get_it_department_loc(self, tr):
        return By.XPATH, self.LIST + '/tr[%s]/td[10]/div/div/p[1]' % tr

    def get_complete_button_loc(self, tr):
        return By.XPATH, self.LIST + '/tr[%s]/td[11]/div/button[1]' % tr

    def get_tr(self):
        tr = 1
        while not self.is_element_exist(self.get_assign_button_loc(tr)):
            tr = tr + 1
        return tr

    def add_work_order(self):
        self.find_element(*self.add_button).click()

    def get_list_customer_info(self):
        return self.find_element(*self.customer_loc).text

    def get_list_product_info(self):
        return self.find_element(*self.product_loc).text

    def get_list_detail_info(self, tr=False):
        if tr:
            return self.find_element(*self.get_detail_info_loc(self.tr)).text
        else:
            return self.find_element(*self.detail_loc).text

    def get_list_creator_info(self):
        return self.find_element(*self.creator_loc).text

    def get_list_department_info(self, d_id, tr=False):
        if tr:
            if d_id == 2:
                return self.find_element(*self.get_it_department_loc(self.tr)).text
        else:
            if d_id == 1:
                return self.find_element(*self.sales_department_loc).text
            if d_id == 2:
                return self.find_element(*self.it_department_loc).text

    def assign(self, keys):
        self.find_element(*self.get_assign_button_loc(self.tr)).click()
        self.find_element(*self.assign_input).send_keys(keys)
        self.find_element(*self.assign_drop_box).click()
        self.find_element(*self.assign_confirm).click()
        time.sleep(1)

    def complete(self):
        self.find_element(*self.get_complete_button_loc(self.tr)).click()
        time.sleep(1)

    def get_handler_info(self):
        return self.find_element(*self.get_handler_info_loc(self.tr)).text

    def enter_into_order_detail(self):
        return self.find_element(*self.get_detail_info_loc(self.tr)).click()

    def get_status_info(self):
        return self.find_element(*self.get_status_loc(self.tr)).text

    def get_order_id(self):
        return self.find_element(*self.get_order_id_loc(self.tr)).text
