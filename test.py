'''
Descripttion: 
version: 
Author: wy
Date: 2020年07月28日 20:43:05
LastEditors: wy
LastEditTime: 2020年12月20日 23:07:40
'''
from selenium import webdriver
import time


# 拉动侧边滑动条，使页面数据加载完全
def dropScroll(start=1,end=10,step=1):
    for x in range(start, end, step):
        # 停一下，慢慢拉，拉快了会出问题哦
        time.sleep(0.5)
        # 代表滑动条位置
        j = x/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        # 运行上面的js代码
        driver.execute_script(js)
def getGooods(serach):
    tmp=serach
    # 序号
    number = 0
    # 分析淘宝页面后，获取商品div里面的数据
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    # 遍历每个divs，获取商品详细信息       //*[@id="mainsrp-itemlist"]/div/div/div[1]/div[2]
    for div in divs:
        print('hello, word! {}{}'.format(tmp, number)) 
        # initHandle=driver.getWindowHandle()
        a= div.click()
        
        time.sleep(3)
        #切换窗口
        n = driver.window_handles  # 获取当前页所有窗口句柄
        driver.switch_to.window(n[1])
        # 标题
        title = driver.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1').text

        dropScroll(1,20,1)
        # js = 'document.documentElement.scrollTop = 800;window.navigator.webdriver=false;' 
        # 运行上面的js代码
        # driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="J_TabBar"]/li[2]/a').click()
        # 获取评论
        title = driver.find_element_by_xpath('').text
        time.sleep(2)
        print(title)
        comments = dirver.find_elements_by_class_name('tm-col-master')
        for comment in comments:
            text = comment.find_element_by_class_name('tm-rate-fulltxt')
            print(text.text)
        
        driver.close()
        driver.switch_to.window(n[0])
        number += 1
# 根据自己的关键词开始遍历每个关键词
def toSearchs(serachs):
    for serach in serachs:
        print('第一次：',serach)
        # 获取文本框
        serachInput = driver.find_element_by_xpath('//*[@id="q"]')
        # 清空文本框
        serachInput.clear()
        # 输入查询内容
        serachInput.send_keys(serach)
        # 点击搜索按钮
        driver.find_element_by_xpath('//*[@id="J_SearchForm"]/button').click()
        # 拉动侧边滑动条，使页面数据加载完全
        dropScroll()
        # 获取商品信息
        getGooods(serach)
        
chromedriver_path = "C:\Python38/chromedriver.exe"
options = webdriver.ChromeOptions()
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# driver = webdriver.Chrome()  # 创建driver对象
driver.get('https://www.taobao.com')  # 请求淘宝
# 获取到搜索按钮后，点击
driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
# 最大化
driver.maximize_window()  
#输入账号密码
driver.find_element_by_id("fm-login-id").send_keys("")
password = driver.find_element_by_id("fm-login-password").send_keys("")
# 点击登录按钮
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
searchs = {'衣服男','丝袜','卫衣','jk制服','鞋子'}
time.sleep(2)
toSearchs(searchs)
dirver.close()


