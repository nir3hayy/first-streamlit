# import time
#
# import streamlit as st
# st.image("sahand-babali-LbJ_EU8hELk-unsplash.jpg")
# st.title('welcome tho the steamlit library')
# st.header("machin lerning")
# st.subheader("linear reggretion")
# st.info(" hi my name is nirbhay and this is a forst day that i am going to use a streamlit library")
# st.warning(" helllo mc")
# st.error(" this is an a error function")
# st.success(" conrats is an succes")
#
# st.caption(" this functiion is use for tyhe caption")
# st.write(" this is write afunction")
#
# #markdown function
#
# st.markdown("#nirbhay")
# st.markdown("# nirbhay")
# st.markdown("## nirbhay")
# st.markdown("### nirbhay")
# st.markdown(":moon:")# this syntax is use for the crete a emoji
#
# st.latex('''a+b^2''')
# st.checkbox("push here")
# st.checkbox(" push kar ")
# st.selectbox("selet any one",["java" ,"python","nirbhay"])
# st.button(" chick here")
# st.multiselect(" chose ttw 2 elective",["data science","cloud","nirbhay"])
# st.select_slider("expiriance",["bad", "good","very good","excelecnt"])
# st.slider("chose a number",1,199)
# st.text_input(" entter  the number")
# st.number_input(" entter  the number")
# st.time_input("mjkfhjbehjb")
# st.text_area(" enter the description here")
# st.file_uploader(" upload a file")
# st.color_picker("red")
# st.progress(20)
# with st.spinner():
#      time.sleep(20)
import pandas as pd
import numpy as np
import streamlit as st
from altair import Column

st.title(" Thw bar chart")
data=pd.DataFrame(np.random.rand(40,2),columns = ["x" ,  "y"])
st.bar_chart(data)