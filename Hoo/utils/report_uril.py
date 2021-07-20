import subprocess
from config import config_file
_report_path = config_file.get_report_path()    # 报告路径
report_re_path = _report_path + 'result'
_report_html = _report_path + 'html'


def allure_report(report_path=report_re_path, report_html=_report_html):
    # 执行命令 allure generate
    allure_cmd = "allure generate %s -o %s --clean" % (report_path, report_html)
    # 生成报告路径，这个命令父进程等待子进程结束在执行
    # anywhere_cmd = 'anywhere -p 9000'
    try:
        subprocess.call(allure_cmd, shell=True)
        # subprocess.call(anywhere_cmd, shell=True)
    except:
        pass