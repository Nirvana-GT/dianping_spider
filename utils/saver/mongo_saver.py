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
import sys

from utils.config import global_config
from utils.logger import logger
from utils.spider_config import spider_config


class MongoSaver():
    def __init__(self):
        mongo_url = spider_config.MONGO_PATH
        try:
            import pymongo
            client = pymongo.MongoClient(mongo_url)
            self.database = client['dianping']
        except:
            logger.warning(
                u'系统中可能没有安装或启动MongoDB数据库，请先根据系统环境安装或启动MongoDB，再运行程序')
            sys.exit()

    def save_data(self, data, data_type, start_page, end_page):
        """
        保存数据
        :param data:
        :param data_type:
        :return:
        """
        assert data_type in ['search', 'detail', 'review']
        if data_type == 'search':
            self.save_search_list(data)
        elif data_type == 'detail':
            self.save_detail_list(data)
        elif data_type == 'review':
            self.save_review_list(data, start_page, end_page)
        else:
            raise Exception

    def get_infos(self):
        """
        获取数据
        :return:
        """
        return self.get_infos_data()

    def update_info_status(self, shop_id, status):
        """
        获取数据
        :param shop_id:
        :param status:
        :return:
        """
        return self.update_status(shop_id, status)

    def save_search_list(self, data):
        """
        保存搜索结果
        :param data:
        :return:
        """
        col = self.database['info']
        col.delete_many({'店铺id': data['店铺id']})
        col.insert(data)


    def save_detail_list(self, data):
        """
        保存详细结果
        :param data:
        :return:
        """
        col = self.database['info_detail']
        col.delete_many({'店铺id': data['店铺id']})
        col.insert(data)


    def save_review_list(self, data, start_page, end_page):
        """
        保存评论数据
        :param data:
        :return:
        """
        col = self.database['review_' + data['店铺id'] + str(start_page) + '-' + str(end_page)]
        col.delete_many({'店铺id': data['店铺id']})
        col.insert(data)

    def get_info_data(self, shop_id):
        """
        获取商家数据
        :param shop_id:
        :return:
        """
        col = self.database['info']
        return col.find_one({'店铺id': shop_id})


    def get_infos_data(self):
        """
        获取商家数据
        :return:
        """
        col = self.database['info']
        return col.find({'status': {'$in': [1, 3, 4]}})

    def update_status(self, shop_id, status):
        """
        获取商家数据
        :param shop_id:
        :param status:
        :return:
        """
        col = self.database['info']
        return col.update_one({'店铺id': shop_id}, {'$set': {'status': status}})

