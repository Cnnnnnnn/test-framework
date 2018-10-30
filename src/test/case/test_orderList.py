# -*- coding: utf-8 -*-
import unittest, time
from src.utils.config import Config
from src.test.page import login_page, workorderAdd_page, workorderDetail_page


class ListTest(unittest.TestCase):
    ORDER_PATH = Config().get('PATH') + 'order'

    def setUp(self):
        self.page = login_page.LoginPage(browser_type='chrome').get(self.ORDER_PATH, maximize_window=True)
        self.page.login(1)

    def test_orderList(self):
        dr = workorderAdd_page.WorkOrderAddPage(self.page)
        dr.tr = dr.get_tr()
        dr2 = workorderDetail_page.WorkOrderDetailPage(self.page)

        # 指派处理人
        dr.assign(u"测试售后")
        self.assertEqual(dr.get_handler_info(), u'已指派(测试售后管理员)   指派', u"指派处理人fail")

        # 编辑工单
        dr.enter_into_order_detail()
        dr.switch_windows()
        dr2.click_edit_button()
        dr.department_select(2)
        dr.handler_select(u"测试售后")
        dr.title_edit(u"编辑工单标题")
        dr.problem_type_select(6)
        dr.input_edit(u"编辑测试内容")
        dr.submit()
        dr.switch_windows(new=False, old=True)
        time.sleep(1)
        dr.refresh()
        self.assertEqual(dr.get_list_detail_info(tr=True), u'【软件安装】 【编辑工单标题】 编辑测试内容', u'编辑工单内容fail')
        self.assertEqual(dr.get_list_department_info(2), u'已指派(测试售后管理员)    指派', u'编辑工单部门fail')

        # 完成工单
        dr.complete()
        self.assertEqual(dr.get_status_info(), '已完成', u'完成工单fail')

        # 删除工单
        order_id = dr.get_order_id()
        dr.enter_into_order_detail()
        dr.switch_windows()
        dr2.click_more_button()
        dr2.click_delete_button()
        dr2.click_confirm_button()
        dr.switch_windows(new=False, old=True)
        dr.refresh()
        self.assertNotEqual(order_id, dr.get_order_id(), u"删除工单fail")
