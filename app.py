import time
from subscriptionURL import setSubscriptionURL,getSubscriptionURL,getBeforeURL,getServicesByURL
from testSpeed import startTest


def run():
    currentURL = getSubscriptionURL()
    beforeURL = getBeforeURL()
    if currentURL != beforeURL :
        setSubscriptionURL(currentURL)
        getServicesByURL(currentURL)
        startTest()
    else :
        with open("los.txt","a") as file:
            file.write("\n订阅未更新\n")
            file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) )


while True:
    with open("los.txt","a") as file:
        file.write("\n开始执行\n")
        file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) )
    run()
    with open("los.txt","a") as file:
        file.write("\n执行完毕\n")
        file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) )
    time.sleep(60 * 10)  # 暂停 10 分钟
