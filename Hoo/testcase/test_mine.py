import time
import pytest
from config import config_file
from utils.excel_util import excel_date, analysis, expected_analysis
from utils.uiauto_util import ExecuteU2
from comman.excel_config import ExcelConfig


ex_file = config_file.get_excel_path()
run_ed = excel_date(ex_file, 0)


class TestMine:
    """参数化执行各个模块"""
    @pytest.mark.parametrize("case", run_ed)
    def test_mine(self, case):
        # case_id = case[ExcelConfig.case_id]
        # print(case_id)
        # case_catalog = case[ExcelConfig.case_catalog]
        # case_name = case[ExcelConfig.case_name]
        # case_priority = case[ExcelConfig.case_priority]
        # case_is_run = case[ExcelConfig.case_is_run]
        # case_preconditions = case[ExcelConfig.case_preconditions]
        # case_step = case[ExcelConfig.case_step]
        case_step_node = case[ExcelConfig.case_step_node]
        date1 = analysis(case_step_node)
        # print(date1)
        # case_expected_outcome = case[ExcelConfig.case_expected_outcome]
        case_expected_node = case[ExcelConfig.case_expected_node]
        data2 = expected_analysis(case_expected_node)
        print(data2)
        d = ExecuteU2("851QFDSG22CDZ", "com.tencent.hobby")
        for step_node, expected_node in zip(date1, data2):
            d.run_app(step_node)
            time.sleep(0.5)
            # for expected_node in data2:
            if type(expected_node) == str:
                d.app_assert(expected_node)
            if type(expected_node) == list:
                for e in expected_node:
                    d.app_assert(e)


if __name__ == "__main__":
    pytest.main(['-s', 'test_mine.py'])