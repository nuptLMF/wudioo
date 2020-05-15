from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
distance = 258
options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-automation']) 
dd = webdriver.Chrome(options=options)

dd.set_window_position(20, 40)
dd.set_window_size(1100,700)

dd.get('http://www.taobao.com')
time.sleep(3)

dd.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
time.sleep(3)
dd.find_element_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]').click()
dd.find_element_by_xpath('//*[@id="TPL_username_1"]').send_keys('lvmingfu007')
time.sleep(3)
dd.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys('lmf1990')
time.sleep(3)
dd.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()
time.sleep(3)
hk = dd.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(dd).click_and_hold(hk).perform()
def get_track(distance):
    """
    根据偏移量获取移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0
    
    while current < distance:
        if current < mid:
            # 加速度为正2
            a = 2
        else:
            # 加速度为负3
            a = -3
        # 初速度v0
        v0 = v
        # 当前速度v = v0 + at
        v = v0 + a * t
        # 移动距离x = v0t + 1/2 * a * t^2
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track
tracks = get_track(distance)
print(tracks)
for x in tracks:
	ActionChains(dd).move_by_offset(xoffset=x,yoffset=0).perform()
time.sleep(0.5)
ActionChains(dd).release().perform()
time.sleep(3)
dd.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys('lmf1990')
time.sleep(3)
dd.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()