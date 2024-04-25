"""
@File    : until.py
@Date    : 2023-02-18
@Author  : LiuTianSheng
@Software : flaskProject
"""
import base64


class Until:
    def img_base64(img_path):
        with open(img_path, "rb") as f:
            base64_str = base64.b64encode(f.read())
        return str(base64_str, 'utf-8')
