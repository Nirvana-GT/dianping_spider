# -*- coding:utf-8 -*-

"""
      ┏┛ ┻━━━━━┛ ┻┓
      ┃　　　　　　 ┃
      ┃　　　━　　　┃
      ┃　┳┛　  ┗┳　┃
      ┃　　　　　　 ┃
      ┃　　　┻　　　┃
      ┃　　　　　　 ┃
      ┗━┓　　　┏━━━┛
        ┃　　　┃   神兽保佑
        ┃　　　┃   代码无BUG！
        ┃　　　┗━━━━━━━━━┓
        ┃CREATE BY SNIPER┣┓
        ┃　　　　         ┏┛
        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
          ┃ ┫ ┫   ┃ ┫ ┫
          ┗━┻━┛   ┗━┻━┛

"""
from utils.spider_config import spider_config


class Saver():
    """
    存储器
    """

    def __init__(self):
        # save_mode = global_config.get('config', 'save_mode')
        save_mode = spider_config.SAVE_MODE
        self.saver_list = []
        # 构造每个存储方法的存储器
        if 'csv' in save_mode:
            from utils.saver.csv_saver import CSV
            print('暂时不支持csv，如果您只选择了csv将不会进行存储（原因详见README）')
            # csv_saver = CSV()
            # self.saver_list.append(csv_saver)
            pass
        if 'mongo' in save_mode:
            from utils.saver.mongo_saver import MongoSaver
            mongo_saver = MongoSaver()
            self.saver_list.append(mongo_saver)
        if 'mongodb' in save_mode:
            from utils.saver.mongo_saver import MongoSaver
            mongo_saver = MongoSaver()
            self.saver_list.append(mongo_saver)

    def save_data(self, data, data_type, start_page, end_page):
        """
        保存数据
        :param data:
        :param data_type:
        :return:
        """
        assert data_type in ['search', 'detail', 'review']
        for each in self.saver_list:
            each.save_data(data, data_type, start_page, end_page)

    def get_data(self, shop_id):
        """
        获取数据
        :param shop_id:
        :return:
        """

        for each in self.saver_list:
            return each.get_info_data(shop_id)

    def get_infos(self):
        """
        获取数据
        :return:
        """

        for each in self.saver_list:
            return each.get_infos()

    def update_info_status(self, shop_id, status):
        """
        获取数据
        :param shop_id:
        :param status:
        :return:
        """

        for each in self.saver_list:
            each.update_info_status(shop_id, status)


saver = Saver()
