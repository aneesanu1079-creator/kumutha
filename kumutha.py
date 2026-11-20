import streamlit as st
st.title("Grade Evaluation")
name=st.text_input("student name")
a=st.number_input("Mark 1",min_value=0,max_value=100)
b=st.number_input("Mark 2",min_value=0,max_value=100)
c=st.number_input("Mark 3",min_value=0,max_value=100)  
total=a+b+c
avg=total/3
high=max(a,b,c)
if st.button("calculate"):
  st.success("Name:"+name)
  st.success(f"Total:{total}")
  st.success(f"Average:{avg:.2f}")
  st.success(f"Highest Mark:{high}")
if avg>=90:
    st.success("Grade A")
elif avg>=60:
    st.success("Grade B")
elif avg>=35:
    st.success("Grade c")
else:
    st.success("Fail")
    