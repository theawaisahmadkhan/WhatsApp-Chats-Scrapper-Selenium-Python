#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os


# In[ ]:


driver = webdriver.Chrome('D:\chromedriver_win32')


# In[ ]:


driver.get('https://web.whatsapp.com')


# In[ ]:


driver.maximize_window()


# In[ ]:


while True:
    try:
        chat_list = driver.find_element(By.XPATH, '//div[@class="_1Gy50"]')
        break
    except:
        time.sleep(5)


# In[ ]:


chats = driver.find_elements(By.XPATH, '//div[@class="_1vDUw"]')

# Create a folder to store the chat files
folder_name = "WhatsApp Chats"
os.makedirs(folder_name, exist_ok=True)

# Iterate over each chat and save the chat to a file
for chat in chats:
    # Check if it is a group chat
    if chat.get_attribute("data-testid") == "default":
        continue

    # Open the chat
    chat.click()

    # Get the user name
    user_name = driver.find_element(By.XPATH, '//div[@class="_2zCfw"]//span').text

    # Get the chat messages
    chat_messages = driver.find_elements(By.XPATH, '//div[contains(@class, "_1Gy50")]//span[contains(@class, "_3Whw5")]')

    # Create a file with the user name and save the chat messages
    file_name = f"{folder_name}/{user_name}.txt"
    with open(file_name, 'w', encoding='utf-8') as file:
        for message in chat_messages:
            file.write(message.text + '\n')

# Close the browser
driver.quit()


# In[ ]:




