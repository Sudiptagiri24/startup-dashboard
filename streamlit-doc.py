import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('I am learnign Strramlit')
st.subheader('Amd i am loving it')
st.write('This is a mormal text')

st.markdown("""
### My favorite movies
- Race 3
- Humshakal
- Housefull
""")

st.code("""
def foo(input):
    return input**2

x = foo(2)
""")

st.latex('x^2 + y^3 + 2 = 9')

df = pd.DataFrame({'Name': ['Ankit', 'Ashwin', 'shubham'],
                   'marks': [70, 80, 90],
                   'package': [10, 20, 30]
                   })
st.dataframe(df)

st.metric('Revenue', 'Rs 3L', '3%')
st.metric('Revenue', 'Rs 3L', '-3%')

st.json({'Name': ['Ankit', 'Ashwin', 'shubham'],
         'marks': [70, 80, 90],
         'package': [10, 20, 30]
         })

st.image('image.png')

st.video('Timeline.mov')

st.sidebar.title('Sidebar ka title')

col1, col2, col3 = st.columns(3)

with col1:
    st.image('image.png')

with col2:
    st.image('image.png')

with col3:
    st.video('Timeline.mov')

st.error('Login Failed')
st.success('Login Failed')

st.info('Pillasauras')

st.warning('heheheh')

bar = st.progress(0)

for i in range(1, 101):
    time.sleep(0)
    bar.progress(i)

email = st.text_input("Enter Email")
num = st.number_input("Enter your phone number")
da = st.date_input("Enter the date")



email = st.text_input("Enter Email")
passw = st.text_input("Enter Password")
gender = st.selectbox('Select Gender',['Male','Female', 'Gay', 'Others'])

btn = st.button("Login karona")
#if the button is clicked

if btn:
    if email == "sudiptagiri4@gmail.com" and passw == "papu1":
        st.success("Login Successful")
        st.balloons()
        st.write(gender)
    else:
        st.error("Login Failed")

import streamlit as st
import pandas as pd

file = st.file_uploader("Upload a CSV file")
if file is not None:
   df = pd.read_csv(file)
   st.dataframe(df.describe())
