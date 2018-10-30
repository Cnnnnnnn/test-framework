# -*- coding: utf-8 -*-
import unittest, time

from src.utils.config import Config
from src.test.page.login_page import LoginPage
from src.test.page.workorderAdd_page import WorkOrderAddPage


class AddTest(unittest.TestCase):
    ORDER_PATH = Config().get('PATH')+'order'

    @classmethod
    def setUpClass(cls):
        cls.page = LoginPage(browser_type='chrome').get(cls.ORDER_PATH, maximize_window=True)
        cls.page.login(1)

    @classmethod
    def tearDownClass(cls):
        cls.page.quit()

    def test_orderAdd_empty(self):
        dr = WorkOrderAddPage(self.page)
        dr.add_work_order()  # 点击添加工单

        dr.submit()
        self.assertEqual(dr.get_message(), u'填写有效的客户', "客户信息为空fail")
        dr.close_popup()

        dr.customer_select(u"测试")  # 选择客户
        dr.submit()
        self.assertEqual(dr.get_message(), u'选择有效的部门', "部门信息为空fail")
        dr.close_popup()

        dr.department_select(1)  # 选择部门
        dr.submit()
        self.assertEqual(dr.get_message(), u'选择产品类型', "产品分类为空fail")
        dr.close_popup()

        dr.product_select()  # 选择产品
        dr.submit()
        self.assertEqual(dr.get_message(), u'请填写内容', "填写内容为空fail")
        dr.close_popup()

        dr.input_edit(u"测试")  # 输入内容
        dr.clear_default_phone()
        dr.submit()
        self.assertEqual(dr.get_message(), u'请填写联系方式', "联系方式为空fail")
        dr.close_popup()

        dr.phone_edit("13812345678")
        dr.submit()
        self.assertTrue(dr.get_list_customer_info() == u"测试客户" and dr.get_list_product_info() == u"门窗CC 定制版" and dr.get_list_detail_info() == u"测试" and dr.get_list_creator_info() == u"测试售后", u'提交工单fail')

    def test_orderAdd_full(self):  # 填写全部条件
        time.sleep(2)
        dr = WorkOrderAddPage(self.page)
        dr.add_work_order()
        dr.customer_select(u"测试")
        dr.product_select()
        dr.department_select(1)
        dr.handler_select(u"测试售后")
        dr.plan_time_select()
        dr.need_time_select()
        dr.reminder_select(u"测试售后管理员")
        dr.title_edit(u"工单标题")
        dr.problem_type_select(1)
        dr.input_edit(u"测试")
        dr.submit()
        self.assertEqual(dr.get_list_detail_info(), u'【软件BUG】 【工单标题】 测试', u"提交工单fail")
