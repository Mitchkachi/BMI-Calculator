import streamlit as st
from PIL import Image
backgroundColor = "#F0F0F0"
exercise = Image.open("C:\\Users\\HP\\OneDrive\\Pictures\\My BMI picture.jpg")

st.title(':white[Mitchelle\'s BMI Calculator]')
st.image(exercise)
st.markdown('#### What is BMI ?')
st.text('BMI is a measurement of a person\'s leanness or corpulence based on their height and weight, and is intended to quantify tissue mass.\nIt is widely used as a general indicator of whether a person has a healthy body weight for their height. \
      \nSpecifically, the value obtained from the calculation of BMI is used to categorize whether a person is underweight, normal weight, overweight, or obese depending on what range the value falls between.'
        '\nThese ranges of BMI vary based on factors such as region and age,and are sometimes further divided into subcategories such as severely underweight or very severely obese.'
        '\nBeing overweight or underweight can have significant health effects, so while BMI is an imperfect measure of healthy body weight, it is a useful indicator of whether any additional testing or action is required.')

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")
status = st.radio('select your height format: ', ('cms', 'meters', 'feet'))

# #centimetres
if (status == 'cms'):
    height = st.number_input('cms')

    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter value of your height")

# meters
elif (status == 'meters'):
    height = st.number_input('meters')

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter value of your height")

#feet
else:
    height = st.number_input('Feet')
    # 1 meter = 3.28
    try:
        bmi = weight / ((height/3.28)**2)
    except:
        st.text("Enter some value of height")

if (st.button('Calculate BMI')):
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))
    if (bmi < 16):
        st.error('You Are Extremely Underweight😩')
    elif(bmi >= 16 and bmi < 18.5):
        st.warning('You Are Underweight😒')
    elif(bmi >=18.5 and bmi < 25):
        st.success('You Are Healthy🤗')
    elif (bmi >= 25 and bmi < 30):
        st.warning("You Are Overweight🥲")
    elif (bmi > 30):
        st.error("You Are Extremely Overweight🥺")
