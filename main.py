#!/usr/bin/env python
# coding: utf-8

# In[193]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

#載入更多留言
def clickMoreComment():
    while True:
        try:
            commentBlock = driver.find_element_by_class_name("_333v._45kb")
            targetBtn    = commentBlock.find_element_by_css_selector("div[id^='see_next_']>a")
            driver.execute_script('arguments[0].click()', targetBtn)
            print('success')
            time.sleep(1)
        except Exception as e:
            #print(e)
            print('failed')
            break

#Sample Url: https://www.facebook.com/kh.inmap.tw/posts/5014346518617596
while True:
    postUrl = input('Please Input Facebook Post Url: ')
    if postUrl.find('www.facebook.com') >= -1:
        postUrl = postUrl.replace('www.facebook.com', 'm.facebook.com')
        print(postUrl)
        break
    else:
        print('URL FORMAT ERROR PLEASE TRY AGAIN...')

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get(postUrl)
driver.implicitly_wait(1)
clickMoreComment()
print('Processing...')
index  = 1
result = []
commentBlock    = driver.find_element_by_class_name("_333v._45kb")
allUserComments = commentBlock.find_elements_by_css_selector("div[data-uniqueid]")
for userComment in allUserComments:
    username  = userComment.find_element_by_class_name("_2b05").text
    comment   = userComment.find_element_by_css_selector('div[data-commentid]').text
    result.append({
        "user"    : username,
        "comment" : comment
    })

print(result)
#driver.get_screenshot_as_file('screenShot.png')


# In[192]:




