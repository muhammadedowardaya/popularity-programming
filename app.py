import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt
import time
# merepresentasikan data menjadi garis linear dalam grafik
# label berfungsi agar dapat dikenali legends

st.set_page_config(page_title='Popularitas Bahasa Pemrograman')
st.header('Popularitas Bahasa Pemrograman')
image = Image.open('./images/programming-language.jpg')
st.image(image, use_column_width=True)
# st.subheader('Melihat popularitas bahasa pemrograman dari tahun 2004 - 2022')
st.caption('Pilih bahasa pemrograman dibawah ini untuk melihat grafik popularitasnya dari tahun 2004 sampai tahun 2022')

### --- LOAD DATAFRAME
csv_file = 'Most_Popular_Programming_Languages_from_2004-2022.csv'

df = pd.read_csv(csv_file)
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])

bahasa_pemrograman = ['Python','JavaScript','Java','Dart','PHP','C/C++','C#','Go','Kotlin','R','Ruby','Rust','Swift','TypeScript','Visual Basic']

bahasa_pemrograman_selection = st.multiselect('Bahasa Pemrograman :',
                                    bahasa_pemrograman,
                                    default='Python'
                                )
def tampilkan_hasil(pilihanUser):
    plt.plot(df['Date'], df[pilihanUser], label=pilihanUser)
    
    plt.xlabel('Tahun') # informasi teks untuk axis horizontal
    plt.ylabel('Popularitas (%)') # informasi teks untuk axis vertikal
    plt.title('Perkembangan popularitas bahasa pemrograman') # judul
    plt.grid(True) # garis background untuk mempermudah pembacaan
    plt.legend() # informasi warna garis

fig = plt.figure() 
tampilkan_hasil(bahasa_pemrograman_selection)
with st.spinner('Dagoan heula sakedeung...'):
    time.sleep(3)
st.pyplot(fig)

body = '''

import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt

st.set_page_config(page_title='Popularitas Bahasa Pemrograman')
st.header('Popularitas Bahasa Pemrograman')
image = Image.open('./images/programming-language.jpg')
st.image(image, use_column_width=True)
st.caption('Pilih bahasa pemrograman dibawah ini untuk melihat grafik popularitasnya dari tahun 2004 sampai tahun 2022')

csv_file = 'Most_Popular_Programming_Languages_from_2004-2022.csv'

df = pd.read_csv(csv_file)
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])

bahasa_pemrograman = ['Python','JavaScript','Java','Dart','PHP','C/C++','C#','Go','Kotlin','R','Ruby','Rust','Swift','TypeScript','Visual Basic']

bahasa_pemrograman_selection = st.multiselect('Bahasa Pemrograman :',
                                    bahasa_pemrograman,
                                    default='Python'
                                )
def tampilkan_hasil(pilihanUser):
    plt.plot(df['Date'], df[pilihanUser], label=pilihanUser)
    
    plt.xlabel('Tahun') # informasi teks untuk axis horizontal
    plt.ylabel('Popularitas (%)') # informasi teks untuk axis vertikal
    plt.title('Perkembangan popularitas bahasa pemrograman') # judul
    plt.grid(True) # garis background untuk mempermudah pembacaan
    plt.legend() # informasi warna garis

fig = plt.figure() 
tampilkan_hasil(bahasa_pemrograman_selection)
st.pyplot(fig)

# By : Muhammad Edo Wardaya
'''

def show_code():
    st.code(body, language="python")

col1, col2 = st.columns(2)

with col1:
    lihat_kode = st.button('Lihat Kode')

if lihat_kode:
    with st.spinner('Dagoan heula sakedeung...'):
        time.sleep(3)
    with col2:
        tutup_kode = st.button('Tutup Kode')
    st.code(body, language="python")
    if tutup_kode:
        st.code('', language="python")
    

st.subheader('My Profile')

col1, col2, col3 = st.columns(3)

with col1:
    my_photo = Image.open('./images/my-photo.jpg')
    st.image(my_photo, use_column_width=True)

with col2:
    cacahan = """
    Nama saya Muhammad Edo Wardaya, 
    saya seorang Web Developer... (kayak yang bener aja ya wkwkwk)
    jangan lupa follow instagram saya @m_edo_wardaya >_<

    duhhh makin gajelas aja eh .......
    """
    st.caption(cacahan)

