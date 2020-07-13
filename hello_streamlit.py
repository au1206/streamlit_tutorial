import streamlit as st

# Title
st.title("Streamlit Tutorial")
# Heading
st.header('Heading')
# sub-heading
st.subheader('Sub-heading')
# Text
st.text("Hello World")

# Markdown
st.markdown("#### Markdown")

# Error and colorful text
st.subheader('Some coloured tags')
st.success("Success")
st.info("Information")
st.warning("Warning!")
st.error("Error!")
st.exception("A dummy Exception")

# immediate printing help for any python fucntion etc.
st.help(range)

# writing text with the function
st.write("Some text with the function")
st.write(range(10))

# Images
from PIL import Image
st.subheader('Displaying Images')
img = Image.open('example_image.png')
st.image(img, width=700, caption="Simple Image")

# Videos
st.subheader('Embedding a video file')
vidfile = open('example_vid.mp4','rb')
vid_byte = vidfile.read()
st.video(vidfile)
vidfile.close()

# Audio
st.subheader('Embedding an audio file')
audfile = open('example_aud.mp3','rb')
aud_byte = audfile.read()
st.audio(aud_byte, format='audio/mp3')
audfile.close()

# WIDGETS
st.subheader('Some Cool Widgets')
# Checkbox
st.markdown("#### Checkbox")
if st.checkbox("Checkbox1 : Show/Hide"):    
    st.text("showing text")

# Radio Button
st.markdown("#### Radio Button")
status = st.radio("What is your status",("Active", "Inactive"))
if status=='Active':
    st.success("You are Active!")
else:
    st.error("You are Inactive")

# Select Box
st.markdown("#### Select Box")
occupation = st.selectbox("Your Occupation: ", ["Machine Learning Engineer", "Python Programmer", "Researcher", "Data Engineer"])
st.write("Your Selected Occupation is: ", occupation)

# Multi-Selection Box
st.markdown("#### MultiSelect")
skills = st.multiselect("Skill List", ["Python", "Machine Learning", "Deep Learning", "Computer Vision", "NLP"])
st.write(f"You selected {len(skills)} skills")

# Slider
st.markdown("#### Slider")
experience = st.slider("What is your years of experience",0,15)

# Buttons
st.markdown("#### Buttons")
st.button('Simple Button')
if st.button("About"):
    st.text("A basic streamlit tutorial")

# TEXT INPUTS
st.subheader('Text Inputs')
# TextField Input
st.markdown("#### Text Input")
first_name = st.text_input("First Name: ", "Type Here ...")
last_name = st.text_input("Last Name: ", "Type Here...")
name = first_name + " " + last_name
if st.button("Submit", key="name"):
    st.success(name) 

# Text Area
st.markdown("#### Text Area")
message = st.text_input("Your Message: ", "Type Here ...")
if st.button("Submit", key="message"):
    st.success(message) 

# Date and Time Input
st.subheader('Date and Time Inputs')
import datetime
date = st.date_input("today is: ", datetime.datetime.now())
time = st.time_input("time right now", datetime.time())

# Displaying JSON
st.subheader('Displaying JSON')
json_1 = {'Name': "Akshay Uppal", 'Gender': "Male", 'Age': 26}
st.json(json_1)

# Displaying Code
st.subheader('Displaying Code')
st.code("import numpy as np")
with st.echo():
    # this is a code block
    # Import Statements
    import numpy as np
    import pandas as pd
    import tensorflow as tf

# Progress Bar
st.markdown("#### Progress Bar")
import time
my_bar = st.progress(0)
for p in range(100):
    my_bar.progress(p+1)

# Spinner
st.markdown("#### Spinner")
with st.spinner("Waiting ..."):
    time.sleep(2)
st.success("Completed")

# Sidebar
epochs = st.sidebar.slider('Choose the number of epochs', 1, 50)
lr = st.sidebar.slider('Choose the learning rate (x10^-4)', 1, 100)
lr = lr*0.0001
st.sidebar.text(f"the learning rate chosen is {lr}")

# Cache
@st.cache
def func():
    return range(1000)
st.write(func())

# Dataframes and plots
st.subheader('Dataframe')
import pandas as pd
df = pd.read_csv('mnist_test.csv')[:500]
st.dataframe(df)

