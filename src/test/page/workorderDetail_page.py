from src.test.common.page import Page
from selenium.webdriver.common.by import By


class WorkOrderDetailPage(Page):
    more_button = (By.XPATH, '//*[@id="after_sale_detail"]/div[1]/div[1]/div[2]/div/span')
    edit_button = (By.XPATH, '//*[@id="after_sale_detail"]/div[1]/div[1]/div[2]/a/button')
    delete_button = (By.XPATH, '/html/body/ul[@class="el-dropdown-menu"]/li[3]')
    confirm_button = (By.XPATH, '/html/body/div[2]/div/div[4]/div[2]/button')

    def click_more_button(self):
        self.move_to_element(*self.more_button)

    def click_edit_button(self):
        self.find_element(*self.edit_button).click()

    def click_delete_button(self):
        self.find_element(*self.delete_button).click()

    def click_confirm_button(self):
        self.find_element(*self.confirm_button).click()
