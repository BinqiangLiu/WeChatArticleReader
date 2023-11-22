import streamlit as st
import requests
import timeit
import datetime

st.set_page_config(page_title="AI Chat Client", layout="wide")
st.title("AI Chat Client")

current_datetime_0= datetime.datetime.now()
print(f"Anything happens, this ST app will execute from top down. @ {current_datetime_0}")
print()

# FastAPI 服务器的 URL
fastapi_server_url = "https://binqiangliu-wechatarticleloaderfastapi.hf.space/get_ai_response"

# 用户输入
url = st.text_input("Enter the URL to chat with:")
print(f"URL Entered: "+url)
print()
question = st.text_input("Enter your question:")
print(f"Question Entered: "+question)
print()

# 当用户点击按钮时
if st.button('Get AI Response'):
    if url and question:
        print(f"URL & Question Entered & Button clicked.")
        print()
        with st.spinner('Fetching AI response...'):
            # 构造请求
            data = {"url": url, "question": question}
            # 发送请求到 FastAPI 服务器
            current_datetime_0 = datetime.datetime.now()
            print(f'API调用请求发送开始 @ {current_datetime_0}')   
            print()
            start_1 = timeit.default_timer() # Start timer               
            response = requests.post(fastapi_server_url, json=data)                       
            end_1 = timeit.default_timer() # Start timer   
            print(f'API调用请求发送结束，共耗时： @ {end_1 - start_1}')  
            print()
            
            if response.status_code == 200:
                # 显示 AI 的回答
                #ai_response = response.json().get("AI Response", "No response received.")
                current_datetime_1 = datetime.datetime.now()
                print(f'获取API调用结果开始 @ {current_datetime_1}')
                print()
                start_2 = timeit.default_timer() # Start timer   
                ai_response = response.json()
                ai_response_output=ai_response['AIResponse']
                end_2 = timeit.default_timer() # Start timer   
                print(f'获取API调用结果完毕，共耗时： @ {end_2 - start_2}') 
                print()
                print("AI Response:", ai_response)
                #print("AI Response:", ai_response_output)    
                print()
                #st.write("AI Response:", ai_response)
                st.write("AI Response:", ai_response_output)
            else:
                # 显示错误信息
                st.error("Error in fetching response from AI server.")
    else:
        st.warning("Please enter both URL and a question.")
