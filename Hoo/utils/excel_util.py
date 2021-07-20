import xlrd
from config import config_file

excel_file = config_file.get_excel_path()


class ExcelUtil:
    """读取解析excel"""
    def __init__(self, file_name, sheet):
        wb = xlrd.open_workbook(file_name)
        if type(sheet) == str:
            self.table = wb.sheet_by_name(sheet)
        if type(sheet) == int:
            self.table = wb.sheet_by_index(sheet)

    def get_all_data(self):
        """获取所有的用例"""
        max_rows = self.table.nrows
        title = self.table.row_values(0)
        data_list = []
        for i in range(1, max_rows):
            row_date = self.table.row_values(i)
            data_dict = dict(zip(title, row_date))
            data_list.append(data_dict)
        # print(data_list)
        return data_list

    def get_run_data(self):
        """读取需要执行的用例"""
        run_data_list = []
        for i in self.get_all_data():
            for k in i:
                if i[k].lower() == 'yes':
                    run_data_list.append(i)
        # print(run_data_list)
        return run_data_list


def excel_date(file_name, sheet):
    eu = ExcelUtil(file_name, sheet)
    ed = eu.get_run_data()
    return ed


def analysis(excel_str):
    # element_list = list()
    ex_str = excel_str.replace('\n', ', ')
    return [i for i in ex_str.split(', ')]


def expected_analysis(excel_str):
    if excel_str:
        if '\n' not in excel_str:
            return excel_str.split(', ')
        if '\n' in excel_str:
            el_list = []
            for i in excel_str.split('\n'):
                if ', ' not in i:
                    el_list.append(i)
                if ', ' in i:
                    el_list.append(i.split(', '))
            return el_list


if __name__ == "__main__":
    excel_date(excel_file, 0)

