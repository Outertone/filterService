import time
import pyperclip
from string import Template
from pywinauto import Application,findwindows,mouse
from pywinauto.keyboard import send_keys
app = Application(backend='uia').start("D:/v2rayN-With-Core/v2rayN.exe")
app = app.connect(path=r"D:/v2rayN-With-Core/v2rayN.exe")
window =  app.window()

def clickElement (element,event) :
    rectangle = element.element_info.rectangle
    x = int((rectangle.left + rectangle.right) / 2)
    y = int((rectangle.top + rectangle.bottom) / 2)
    mouse.click(event, (x, y))
    return



def clearAllNode():
    clickElement(window.child_window(auto_id="PART_ColumnHeadersPresenter", control_type="Header"),'right')
    clickElement(window.child_window(title="全选 (Ctrl+A)", auto_id="menuSelectAll", control_type="MenuItem"),'left')
    clickElement(window.child_window(auto_id="PART_ColumnHeadersPresenter", control_type="Header"),'right')
    clickElement(window.child_window(title="移除所选服务器(多选) (Delete)", auto_id="menuRemoveServer", control_type="MenuItem"),'left')
    send_keys('{Y}')
    clickElement(window.child_window(auto_id="btnClear", control_type="Button"),'left')

def batchImportNodes():
    clickElement(window.child_window(auto_id="btnClear", control_type="Button"),'left')
    # ^代表ctrl
    send_keys('^v')
    # 把上一次的五条也加进来
    with open("result.txt","r") as file:
        pyperclip.copy(file.read())
        send_keys('^v')


def batchTestSpeed():
    clickElement(window.child_window(auto_id="PART_ColumnHeadersPresenter", control_type="Header"),'right')
    clickElement(window.child_window(title="全选 (Ctrl+A)", auto_id="menuSelectAll", control_type="MenuItem"),'left')
    clickElement(window.child_window(auto_id="PART_ColumnHeadersPresenter", control_type="Header"),'right')
    clickElement(window.child_window(title="测试服务器速度(多选) (Ctrl+T)", auto_id="menuSpeedServer", control_type="MenuItem"),'left')


def cloneFirstFiveNodes() :
    with open('result.txt', 'w'):
        pass
    for i in range(5):
        clickElement(window.child_window(title="ServiceLib.Models.ProfileItemModel", control_type="DataItem",found_index = i),'right')
        clickElement(window.child_window(title="分享服务器 (Ctrl+F)", auto_id="menuShareServer", control_type="MenuItem"),'left')
        currentEdit =  window.child_window(auto_id="txtContent", control_type="Edit").wait("visible", timeout=20)
        # 获取当前剪切板内容
        with open("result.txt","a") as file:
            file.write(currentEdit.window_text())
            file.write('\n')
            clickElement(window.child_window(title="关闭", control_type="Button",found_index=1),'left')
    clickElement(window.child_window(title="最小化", control_type="Button"),'left')
    
def testSpeedResultSort() :
    clickElement(window.child_window(title="速度(M/s)", control_type="HeaderItem"),'left')
    # 再点击一次按最快排
    clickElement(window.child_window(title="速度(M/s)", control_type="HeaderItem"),'left')
    return

def checkDone() :
    logsEdit =  window.child_window(auto_id="txtMsg", control_type="Edit")
    time.sleep(5) 
    logText =  logsEdit.window_text()
    if "测试完成" in logText:
        testSpeedResultSort()
        cloneFirstFiveNodes()
    else :
        checkDone()
    return


def startTest() :
    clearAllNode()
    batchImportNodes()
    batchTestSpeed()
    checkDone()




# window.print_control_identifiers(depth=None, filename='output.txt')

