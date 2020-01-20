from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client
from dailyfresh import settings


class FDFSStorage(Storage):

    def __init__(self, client_conf=None, base_url=None):
        if client_conf is None:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf

        if base_url is None:
            base_url = settings.FDFS_URL
        self.base_url = base_url

    def _open(self, name, mode='rb'):
        '''打开文件时使用'''
        pass

    def _save(self, name, content):
        """

        :param name: 上传文件的名字
        :param content: 包含上传文件的内容的File对象
        :return:
        """
        client = Fdfs_client(self.client_conf)

        # 上传文件到fdfs系统
        res = client.upload_by_buffer(content.read())
        # ret = client.upload_by_filename('test.jpg')

        # dict
        # {
        #     'Group name': group_name,
        #     'Remote file_id': remote_file_id,
        #     'Status': 'Upload successed.',
        #     'Local file name': '',
        #     'Uploaded size': upload_size,
        #     'Storage IP': storage_ip
        # }
        if res.get('Status') != 'Upload successed.':
            # 上传失败
            raise Exception('上传文件到fast dfs失败')

        # 获取返回的文件ID
        filename = res.get('Remote file_id')
        return filename

    def exists(self, name):
        '''Django判断文件名是否可用'''
        return False

    def url(self, name):
        '''返回访问文件的url路径'''
        return self.base_url + name

