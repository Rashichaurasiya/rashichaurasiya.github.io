import pickle
import streamlit as st
model1=pickle.load(open("area.pkl","rb"))

def my1():
    area=st.number_input("enter a area....")
    pred=st.button("predict")

    if pred:
      op=model1.predict([[area]])
      st.write("The price of the area",op)
my1()        
        
    