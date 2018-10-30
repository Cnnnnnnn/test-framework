from src.test.page.workorderList_page import WorkOrderListPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class WorkOrderAddPage(WorkOrderListPage):
    submit_button = (By.XPATH, '//*[@id="add"]/div[1]/div/section[2]/section/div[5]/button')
    close_button = (By.XPATH, '//div[@class="swal-modal"]/div[@class="swal-footer"]/div/button')
    message = (By.XPATH, '//div[@class="swal-modal"]/div[@class="swal-text"]')
    hiddenTable = (By.CLASS_NAME, "hiddenTable")
    # 左侧页面元素
    customer_input_loc = (By.CSS_SELECTOR, "input.el-input__inner")

    @staticmethod
    def get_department_loc(d_id):
        return By.XPATH, '//ul[@class="leftInputArea container"]/li[4]/div[1]/label[%d]' % d_id

    department_loc = (By.XPATH, '//ul[@class="leftInputArea container"]/li[4]/div/label[1]')
    product = (By.XPATH, '//ul[@class="leftInputArea container"]/li[3]/div')
    handler_input_loc = (By.XPATH, '//ul[@class="leftInputArea container"]/li[5]/div/div[1]/input')
    phone_loc = (By.XPATH, '//ul[@class="leftInputArea container"]/li[6]/div/input')
    plan_time = (By.XPATH, '//ul[@class="leftInputArea container"]/li[9]/div')
    need_time = (By.XPATH, '//ul[@class="leftInputArea container"]/li[10]/div')
    reminder_loc = (By.CSS_SELECTOR, 'input.el-select__input.is-undefined')
    # 右侧页面元素
    input_frame = (By.XPATH, '//div[@class="iframe_b"]/div/div/div/div/div/div/div[@class="edui-editor-iframeholder edui-default"]')
    frame_name = (By.TAG_NAME, "iframe")
    input = (By.XPATH, '//body')
    title = (By.XPATH, '//*[@id="add"]/div[1]/div/section[2]/section/div[2]/input')
    other_problem_type = (By.XPATH, '//*[@id="add"]/div[1]/div/section[2]/section/div[3]/div/div[2]/div[1]')

    @staticmethod
    def get_problem_type(type_id):
        return By.XPATH, '//*[@id="add"]/div[1]/div/section[2]/section/div[3]/div/div[1]/label[% d]/span[1]/span' % type_id

    @staticmethod
    def get_other_problem_type(type_id):
        return By.XPATH, '/html/body/div[3]/div/div[1]/ul/li[%d]/span' % (type_id-4)

    # 下拉框元素
    customer_drop_box = (By.CSS_SELECTOR, "body > div.el-select-dropdown > div > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li")
    product_drop_box = (By.XPATH, '//div[@x-placement="bottom-start"]/div/div[1]/ul/li[1]')
    handler_drop_box = (By.XPATH, '//div[@x-placement="bottom-start"]/div/div[@class="el-select-dropdown__wrap el-scrollbar__wrap"]/ul/li[1]')
    reminder_drop_box = (By.XPATH, '//div[@x-placement="bottom-start"]/div/div[1]/ul/li')

    def submit(self):
        time.sleep(1)
        self.find_element(*self.submit_button).click()

    def close_popup(self):
        self.find_element(*self.close_button).click()

    def get_message(self):
        return self.find_element(*self.message).text

    def customer_select(self, keys):
        self.find_element(*self.customer_input_loc).send_keys(keys)
        self.find_element(*self.customer_drop_box).click()
        self.find_element(*self.hiddenTable).click()

    def department_select(self, d_id):
        self.find_element(*self.get_department_loc(d_id)).click()

    def product_select(self):
        self.find_element(*self.product).click()
        self.find_element(*self.product_drop_box).click()
        time.sleep(1)

    def input_edit(self, contains):
        frame = self.find_element(*self.input_frame).find_element(*self.frame_name)
        self.switch_frame(frame)
        self.find_element(*self.input).clear()
        self.find_element(*self.input).send_keys(contains)
        self.switch_default_content()

    def clear_default_phone(self):
        self.find_element(*self.phone_loc).clear()
        self.find_element(*self.phone_loc).send_keys("1")
        self.find_element(*self.phone_loc).send_keys(Keys.BACKSPACE)

    def phone_edit(self, phone):
        self.find_element(*self.phone_loc).send_keys(phone)

    def handler_select(self, keys):
        self.find_element(*self.handler_input_loc).send_keys(keys)
        self.find_element(*self.handler_drop_box).click()

    def plan_time_select(self):
        self.find_element(*self.plan_time).click()
        self.get_time(bottom=True)

    def need_time_select(self):
        self.find_element(*self.need_time).click()
        self.get_time(bottom=False)

    def reminder_select(self, keys):
        self.find_element(*self.reminder_loc).send_keys(keys)
        self.find_element(*self.reminder_drop_box).click()

    def title_edit(self, contains):
        self.find_element(*self.title).click()
        self.find_element(*self.title).clear()
        self.find_element(*self.title).send_keys(contains)

    # type_id:1：软件Bug  2:报表制作  3：软件升级  4：报表修改  5：功能需求  6：软件安装  7：其他问题
    def problem_type_select(self, type_id):
        if type_id < 5:
            self.find_element(*self.get_problem_type(type_id)).click()
        elif type_id < 8:
            self.find_element(*self.other_problem_type).click()
            self.find_element(*self.get_other_problem_type(type_id)).click()
        else:
            print(u'请传入正确的type id')

