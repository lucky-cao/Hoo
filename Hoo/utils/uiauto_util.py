import time
import uiautomator2 as u2


class ExecuteU2:
    """uiautomator2操作手机"""
    def __init__(self, mobile_service, package):
        self.package = package
        if ':' in mobile_service:
            self.dv = u2.connect(mobile_service)
        if mobile_service.isalnum():
            # 判断是不是数字，字母组合
            self.dv = u2.connect_usb(mobile_service)
        else:
            raise Exception("手机连接异常")

        self.dv.app_stop_all()
        # 停止所有应用
        # if self.dv(resourceId="com.android.systemui:id/clearAnimView").exists(timeout=5):
        #     self.dv(resourceId="com.android.systemui:id/clearAnimView").click()
        #     time.sleep(1)
        self.dv.press("home")
        time.sleep(2)
        # self.dv.app_start(self.package)
        self.dv(text="嚯").click()
        time.sleep(1)
        self.dv(text="跳过").click()
        time.sleep(3)

    def run_app(self, element):

        if self.dv.session(self.package, attach=True):
            # 判断程序是否打开
            if self.dv(text=element).exists(timeout=5):
                # exists: 等待元素出现
                self.dv(text=element).click()
            if self.dv(resourceId=element).exists(timeout=5):
                self.dv(resourceId=element).click()
            if "(" in element:
                coordinate_one = eval(element)[0]
                coordinate_two = eval(element)[1]
                self.dv.click(coordinate_one, coordinate_two)
            # else:
            #     raise Exception("元素不存在")
        else:
            print("app打开异常")

    def app_assert(self, element):
        """页面断言"""
        time.sleep(0.7)
        if self.dv(text=element).exists(timeout=5):
            # exists: 等待元素出现
            print(f"{element}.success")
        elif self.dv(resourceId=element).exists(timeout=5):
            print(f"{element}.success")
        elif element == " ":
            pass
        else:
            raise Exception(f"{element}.元素不存在")


if __name__ == "__main__":
    str_1 = "1234:56"
    str_2 = "fc244f6d"
    str_3 = "123Abc"
    print(str_1.isalnum())
    print(str_2.isalnum())
    print(str_3.isalnum())
    # d = ExecuteU2("851QFDSG22CDZ", "com.tencent.hobby")