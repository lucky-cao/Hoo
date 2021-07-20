import os
import pytest
from config import config_file
from utils import report_uril
report_path = config_file.get_report_path() + os.sep + 'result'


if __name__ == '__main__':
    pytest.main(['-s', '--alluredir', report_path])
    report_uril.allure_report()