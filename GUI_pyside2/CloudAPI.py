# -*- codeing = utf-8 -*-
# @Time :2023/5/11 14:32
# @Author :yujunyu
# @Site :
# @File :CloudAPI.py
# @software: PyCharm

# 腾讯云
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_cos.cos_threadpool import SimpleThreadPool
# UniSMS
from unisdk.sms import UniSMS
from unisdk.exception import UniException
# Others
import pandas as pd
from io import BytesIO
import io
import random
import os
from PIL import Image
import cv2
import numpy as np


class COS:
    def __init__(self):
        """初始化COS"""
        self.secret_id = 'your_secret_id'
        self.secret_key = 'your_secret_key'
        self.region = 'your_region'
        self.bucket = 'your_bucket'
        self.config = CosConfig(Region=self.region, SecretId=self.secret_id, SecretKey=self.secret_key)
        self.client = CosS3Client(self.config)

    def reset_user_pwd(self,phonenumber,password):
        """
        intro:重置用户密码
        :param phonenumber: 用户手机号
        :param password: 用户密码
        :return:
        """
        try:
            response = self.client.get_object(
                Bucket=self.bucket,
                Key='user.xlsx'
            )
            data = response['Body'].get_raw_stream().read()
            df = pd.read_excel(data, sheet_name='Sheet1')
            df.loc[df['phoneNumber'] == phonenumber, 'password'] = password
            buf = BytesIO()
            df.to_excel(buf, index=False)
            self.client.put_object(
                Bucket=self.bucket,
                Key='user.xlsx',
                Body=buf.getvalue()
            )
        except Exception as e:
            print("Read COS error:", e)

    def read_user_from_dataset(self):
        """
        intro:从COS中读取Excel文件内容
        :return: df:pd.DataFrame
        """
        try:
            response = self.client.get_object(
                Bucket=self.bucket,
                Key='user.xlsx'
            )
            data = response['Body'].get_raw_stream().read()
            df = pd.read_excel(data, sheet_name='Sheet1')
            return df
        except Exception as e:
            print("Read COS error:", e)

    def write_user_to_dataset(self, new_data: pd.DataFrame):
        """
        intro:将新数据写入COS中的Excel文件
        :param new_data: 写入的新数据
        :return:
        """
        try:
            # 读取数据
            df = self.read_user_from_dataset()

            # 将新数据追加到原有数据中
            df = pd.concat([df, new_data])

            # 将修改后的数据写入 COS 中的 Excel 文件
            buf = BytesIO()
            df.to_excel(buf, index=False)
            self.client.put_object(
                Bucket=self.bucket,
                Key='user.xlsx',
                Body=buf.getvalue()
            )
            # print('Write COS success!')
        except Exception as e:
            print("Write COS error:", e)

    def create_db(self,username,db_name,db_description,db_version,db_remark):
        """
        intro:创建数据集
        :return:
        """
        try:
            self.client.put_object(
                Bucket=self.bucket,
                Key=f'{username}_database/{db_name}',
                Body=''
            )
            # print(f"Folder 'database' created in bucket '{self.bucket}'")
        except Exception as e:
            print(f"Error creating folder: {e}")

    def send_code(self, to_phone_number: str):
        """
        intro:向指定手机号码(to)发送短信验证码
        :param to_phone_number:str 指定手机号码
        :return:
        """
        # 初始化
        # client = UniSMS("your access key id", "your access key secret") # 若使用简易验签模式仅传入第一个参数即可
        client = UniSMS("m8mpM9rU2M4PbFbhy2HtB8fDgfdRgXGQMquodxBvDaAeu2QNV")  # 若使用简易验签模式仅传入第一个参数即可

        try:
            # 随机生成6为纯数字验证码
            code = random.randint(100000, 999999)
            # 发送短信
            res = client.send({
                "to": to_phone_number,
                "signature": "余俊瑜测试",
                "templateId": "pub_verif_register_ttl",
                "templateData": {
                    "code": code,
                    "ttl": 2
                }
            })
            # print(res.data)
            # print("Send SMS success!")
            return to_phone_number, code
        except UniException as e:
            print("Send SMS error:", e)

    def create_user_database(self, user_name: str):
        """
        intro:创建个人用户的数据库，用于后续存储数据集、模型等数据
        :return:
        """
        try:
            self.client.put_object(
                Bucket=self.bucket,
                Key=user_name + '_database/',
                Body=''
            )
            # print(f"Folder '{user_name}' created in bucket '{self.bucket}'")
        except Exception as e:
            print(f"Error creating folder: {e}")

    def judge_database_if_exist(self, user_name: str):
        """
        intro:判断该用户是否在COS已有数据库
        :return:True/False
        """
        # 列出指定前缀的对象
        folder_path = user_name + '_database/'
        response = self.client.list_objects(
            Bucket=self.bucket,
            Prefix=folder_path,
        )

        # 检查是否存在指定的文件夹
        for content in response.get('Contents', []):
            if content.get('Key') == folder_path:
                return True
        else:
            return False

    def batch_upload(self, folder_path: str, uploadDir: str):
        """
        intro:批量上传数据
        :return:
        """
        g = os.walk(uploadDir)
        # 创建上传的线程池
        pool = SimpleThreadPool()
        for path, dir_list, file_list in g:
            for file_name in file_list:
                srcKey = os.path.join(path, file_name)
                cosObjectKey = srcKey.strip('/')
                # 判断 COS 上文件是否存在
                exists = False
                try:
                    response = self.client.head_object(Bucket=self.bucket, Key=cosObjectKey)
                    exists = True
                except CosServiceError as e:
                    if e.get_status_code() == 404:
                        exists = False
                    else:
                        print("Error happened, reupload it.")
                if not exists:
                    print("File %s not exists in cos, upload it", srcKey)
                    pool.add_task(self.client.upload_file, self.bucket, os.path.join(folder_path, cosObjectKey), srcKey)

        pool.wait_completion()
        result = pool.get_result()
        if not result['success_all']:
            print("Not all files upload sucessed. you should retry")

    def upload_data(self, user_name: str, upload_dir: str, ):
        """
        intro:上传数据集
        :return:
        """
        try:
            # 1 判断是否在COS已存在[用户_database/]文件夹
            if self.judge_database_if_exist(user_name) == True:
                self.batch_upload(folder_path=user_name + f'_database/{upload_dir}/', uploadDir=upload_dir)
            else:
                self.create_user_database(user_name)
                self.batch_upload(folder_path=user_name + f'_database/{upload_dir}/', uploadDir=upload_dir)
        except Exception as e:
            print(e)

    def read_img_data(self, user_name: str, imgdataset: str):
        """
        intro:读取图片数据
        :return:
        """
        print('建设中...')

    def upload_model(self, user_name: str, model_dir: str):
        """
        intro:上传模型
        :return:
        """
        print('建设中...')

    def read_model(self, user_name: str, model_dir: str):
        """
        intro:读取模型
        :return:
        """
        print('建设中...')


if __name__ == '__main__':
    # 【初始化COS】
    MyCOS = COS()

    # 【读取数据】
    MyCOS.reset_user_pwd(10086, '123456788')
    data = MyCOS.read_user_from_dataset()

    print(data)

    # 【添加新数据】
    # new_phone_number = '18888888888'
    # new_password = '123456'
    # new_data = pd.DataFrame({
    #     'phoneNumber': [new_phone_number],
    #     'password': [new_password]
    # })
    # MyCOS.write_user_to_dataset(new_data)

    # 【短信验证】
    # phone_number, code = MyCOS.send_code(to_phone_number='17788595485')
    # print(phone_number, code)

    # 【上传数据集】
    # MyCOS.upload_data(user_name='17788595485', upload_dir='img')

    # 【读取数据集】
    MyCOS.read_img_data(user_name='17788595485', imgdataset='img')
