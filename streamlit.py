import streamlit as st


# st.title('Welcome to the show')

# st.header('Magical Show')

# st.subheader('hosted by deepika')

# st.text(''' Try to watch without sleeping
#         because it may get bored''')


# st.markdown('**Hello**')

# st.markdown('# Hello!')

# st.markdown('---')

# st.caption("'I'm a caption")

# st.write('hello')

# st.write('## H2')

# st.metric(label='windspeed',value='120ms-1',delta='1.4m-1')

# import camelcase

# c = camelcase.CamelCase()

# txt = "hello world"

# print(c.hump(txt))


import pandas as pd


# table = pd.DataFrame({'column1':[1,2,3,4,5],'column2':[6,7,8,9,10]})

# st.table(table)
# st.dataframe(table) #sorting

# code = '''
# Welcome
# '''
# st.code(code)

import json

# json = {'a':'1,2,3','b':'4,5,6'}

# st.json(json) #dictionary type

# st.metric(label = 'Wind Speed',value="120ms-1",delta='1.4ms-1')

# #Media widgets:

# st.image('download.jpg',caption='Flower',width=380)
# st.audio('')
# st.video('')

# #Uploading a file:

# uploaded_file = st.file_uploader('Choose a File',type=['jpg','png','pdf','csv'])

# if uploaded_file is not None:

#  st.image(uploaded_file) 

# if uploaded_file is not None:
#     st.write("PDF uploaded successfully!")
#     st.download_button(
#         label="Download PDF",
#         data=uploaded_file,
#         file_name=uploaded_file.name,
#         mime="application/pdf"
    # )


import numpy as np
# select = st.selectbox('what is your car',options=('Audi','BMW','Suzuki'))
# print(select)

# multiselect = st.multiselect('what is your car',options=('Audi','BMW','Suzuki'))
# print(select)

# age = st.slider('Select your age:',0,100)
# print(age)

# chart = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
# st.line_chart(chart)

#text input

# val = st.text_input('Enter your course!',max_chars=100)
# val2 = st.text_area('course Description',max_chars=500)
# val3 = st.date_input('Enter the date')
# val4 = st.time_input('Set timer')

# forms:

# st.markdown('<h1>User Registration</h1>',unsafe_allow_html=True)
# form = st.form('Form 1')
# form.text_input('First name')
# form.form_submit_button('Submit')

#Second method:

# with st.form('Form2'):
#     col1,col2 = st.columns(2)
#     col1.text_input('Second Name:')
#     col2.text_input('Last Name')

#     st.text_input('Enter your mail id: ')
#     st.text_input('password')
#     st.text_input('Confirm password')
#     st.form_submit_button('Submit')

# from streamlit_option_menu import option_menu
# selected = option_menu("main",['Home','upload','Tasks','Settings'],
#                        icons=['House','Cloud-upoad','List-task','gear'],
#                        menu_icon='cast',default_index=0,orientation='horizantal')


# opt = option_menu("Title",
#                   ["Data", "Prediction","EDA"],
#                   menu_icon="cast",
#                   styles={
#                       "container": {"padding":"4!important", "background-color":"pink"},
#                       "icon":{"color":"#01A982","font-size":"20px"},
#                       "nav-link": {"font-size": "20px", "text-align":"left"},
#                       "nav-link-selected": {"background-color": "blue"}})