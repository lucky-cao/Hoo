import os

current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
# 获取各个文件的路径
print(BASE_DIR)


def get_excel_path():
    excel_path = BASE_DIR + os.sep + 'data' + os.sep + '嚯AND-我的.xls'
    if os.path.exists(excel_path):
        # print(excel_path)
        return excel_path
    else:
        raise Exception("文件不存在")


def get_report_path():
    report_path = BASE_DIR + os.sep + 'report' + os.sep
    if os.path.exists(report_path):
        return report_path
    else:
        os.makedirs(report_path)
        return report_path


if __name__ == "__main__":
    get_excel_path()