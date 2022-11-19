
import streamlit as st
import time
from whatthelang import WhatTheLang


def in_progress_fnc():
    

    # Add a placeholder
    latest_iteration = st.empty()
    'Starting a long computation...'
    bar = st.progress(0)

    for i in range(100):
    # Update the progress bar with each iteration.
        latest_iteration.text(f'In-progress {i+1} %')
        bar.progress(i + 1)
        time.sleep(0.01)

    '...and now we\'re done!'


def text_input_fnc():
    st.text_input("Text or statement", key="name")

    # You can access the value at any point with:
    return st.session_state.name



def predict_lang_fnc(text: None):
    if text is None: 
        return 'Text is available'
    else:
        return wtl.predict_lang(text)

def button_acction(text):

    if st.button('Predict Language'):
        in_progress_fnc()
        result = predict_lang_fnc(text)
        # st.write(f'Prediction: {result}')
        output = f'Prediction: {result}'.format(result)
        st.subheader(output)
    else: 
        st.write(f'Click the button to predict') 




if __name__=='__main__':
    wtl = WhatTheLang()

    st.title('What The Lang on Streamlit')

    text = text_input_fnc()
    button_acction(text)


    

