import time
import yaml


def get_data(filename):
    """
    读取指定的文件信息
    :param filename: 需要读取的文件
    :return: 返回读取的文件
    """
    file_path = '../data/' + filename
    with open(file_path, 'rb') as file:
        data = file.read()
        result = yaml.safe_load(data)
    return result


def get_time():
    """
    获取当前时间，并格式化输出 \n
    :return: 当前时间
    """
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    return now


def get_picture_data(picture_path):
    """
    读取图片文件 \n
    :param picture_path: 要读取的文件路径
    :return: 读取的文件
    """
    with open(picture_path, 'rb') as file:
        picture_data = file.read()
    return picture_data



