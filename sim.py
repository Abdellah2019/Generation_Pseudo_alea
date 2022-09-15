import streamlit as st 
from PIL import Image
import pandas as pd 
import matplotlib.pyplot as plt 
import random

def gen_fibonacci(M):
	Xn_1=1
	Xn_2=0
	while True:
		Xn=(Xn_1+Xn_2)%M
		r=Xn
		Xn_2=Xn_1
		Xn_1=Xn
		print(Xn)
		yield r

	
def gen_pseudo_alea1(X0,m):
	a=16807
	c=0
	m=2**31-1

	Xn=X0
	while True:
		Xn_1=(a*Xn+c)%m
		r=Xn_1
		Xn=Xn_1
		yield r
		

methode_lehmer=gen_pseudo_alea1(100,100)
fibonacci=gen_fibonacci(100)


favicon = Image.open("favicon.ico")
PAGE_CONFIG = {"page_title":"🎲Simulation", 
               "page_icon":favicon, 
               "layout":"centered", 
               "initial_sidebar_state":"auto"}

st.set_page_config(**PAGE_CONFIG)






def plot(x1,y1,x2,y2,x3,y3,title1,title2,title3):
	fig,(ax1,ax2,ax3)=plt.subplots(3)

	ax1.scatter(x=x1,y=y1,color='r')
	ax1.set_xlabel('x')
	ax1.set_ylabel('y')
	ax1.set_title(title1)
	
	ax2.scatter(x=x2,y=y2)
	ax2.set_xlabel('x')
	ax2.set_ylabel('y')
	ax2.set_title(title2)

	ax3.scatter(x=x3,y=y3,color='y')
	ax3.set_xlabel('x')
	ax3.set_ylabel('y')
	ax3.set_title(title3)

	fig.tight_layout()

	st.pyplot(fig)



st.write("""# 🎲♣️Simulation du Gen PSA ♠️🎲""")



number=st.slider("Pick a number ",0,1000)

x1=[next(methode_lehmer)%100 for i in range(number)]
y1=[next(methode_lehmer)%100 for i in range(number)]

x2=[random.randint(0,100) for i in range(number)]
y2=[random.randint(0,100) for i in range(number)]

x3=[next(fibonacci)%100 for i in range(number)]
y3=[next(fibonacci)%100 for i in range(number)]



hide_streamlit_style = """<style>#MainMenu {visibility: hidden;}footer {visibility: hidden;}</style>"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
plot(x1,y1,x2,y2,x3,y3,"Random methode de Lehmer","Random python","Random Fibonacci")


