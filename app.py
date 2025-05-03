import streamlit as st
import numpy as np
import pandas as pd
import requests
import altair as alt
 
 # 1 Element Text di Streamlit
st.title("My First Streamlit App")
st.header("Muh.Kemal Pasha B")
st.header(240907501019)
st.subheader("Bisnis Digital")
st.text("Streamlit adalah framework Python yang digunakan untuk membangun aplikasi web dengan antarmuka pengguna interaktif untuk proyek-proyek data science dan machine learning. Ini memungkinkan pengembang untuk membuat aplikasi web khusus dan tampilan data dengan sedikit usaha dan keahlian dalam pengembangan, web Streamlit dibangun di atas pustaka ilmu data yang populer seperti NumPy, Pandas, dan Matplotlib, sehingga memudahkan untuk membuat visualisasi dan komponen interaktif dalam aplikasi. ")
st.caption('Lembar Kerja Streamlit.')
st.write("Ini adalah coding untuk menginstall Streamlit :")
st.code("pip install streamlit")
st.subheader("Rata-rata (Mean)")
st.latex(r"\text{Mean} = \frac{\sum X}{n}")
st.write("""
Rata-rata adalah jumlah seluruh nilai dibagi dengan jumlah elemen.
""")
st.divider()
 
 # 2 Menampilkan dataframe di streamlit
st.title("Dataframe")
data = {
     'Nama' : ['Kemal', 'Arun', 'Fatih', 'Wahbah', 'Fatihah'],
     'Umur' : [20, 30, 20, 18, 17],
     'Kota' : ['Jakarta', 'Bandung', 'Surabaya', 'Makassar', 'jepot'],
     'Jenis Kelamin' : ['Laki-laki', 'Laki-laki', 'Laki-laki', 'Laki-laki', 'Perempuan'],
     'Alamat' : ['Jl. A', 'Jl. B', 'Jl. C', 'Jl.D', 'Jl.E']
 }
 
df = pd.DataFrame(data)
st.write(df)
st.divider()
 
 # 3 Menampilkan data dari API
st.title("Data dari API")
url = "https://dummyjson.com/products"
response = requests.get(url)
 
if response.status_code == 200:
     data = response.json()
     df = pd.DataFrame(data)
     st.write(df)
     # print(data)
else:
     st.error(f"Failed to fetch data. Status code: {response.status_code}")
 
st.title("Data Upload File")
 # 4 Menampilkan EXCEL/upload file
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls","csv"])
if uploaded_file is not None:
     df = pd.read_csv(uploaded_file)
     st.write(df)
else:
     st.write("No file uploaded yet.")
 
 # 5 Menampilkan DataRandom
 # Menentukan jumlah baris dan kolom
st.title("Data Random")
n_rows = 10  # Jumlah baris
n_cols = 5   # Jumlah kolom
data = np.random.randint(0, 100, size=(n_rows, n_cols))  # Angka acak antara 0 dan 100
columns = [f"Kolom_{i+1}" for i in range(n_cols)]        # Nama kolom

df = pd.DataFrame(data, columns=columns)
 
st.dataframe(df)


 # 6 Metrix di Streamlit
# Judul aplikasi
st.title("Harga Jual dan Beli Emas")

# Membuat tiga kolom
col1, col2, col3 = st.columns(3)

# Menampilkan data harga jual, harga beli, dan perubahan
with col1: 
    st.metric(label="Harga Jual", value="Rp 1.050.000/gram", delta="Rp 5.000")
with col2: 
    st.metric(label="Harga Beli", value="Rp 1.000.000/gram", delta="-Rp 3.000")
with col3: 
    st.metric(label="Perubahan (%)", value="0.2%", delta="0.05%")

 
 # 7 Menampilkan Grafik
 # 7.1 Line Chart
 
data = pd.DataFrame({
    'Garis_1': np.random.randn(100).cumsum(),  # Garis pertama dengan data acak
    'Garis_2': np.random.randn(100).cumsum()   # Garis kedua dengan data acak
 })
st.line_chart(data)
 
 # 7.2 Bar Chart
st.bar_chart(data)
 
 # 7.3 Altair Chart
# Membuat data acak
data = pd.DataFrame({
    'Tanggal': pd.date_range('2023-01-01', periods=100, freq='D'),
    'Harga': np.random.randn(100).cumsum() + 100
})

# Membuat chart Altair
chart = alt.Chart(data).mark_line().encode(
    x='Tanggal:T',
    y='Harga:Q'
).properties(
    title='Grafik Harga Emas'
)

st.altair_chart(chart, use_container_width=True)
# Membuat data lokasi acak (latitude dan longitude)
data = pd.DataFrame({
    'lat': np.random.uniform(-90, 90, 100),  # Latitude antara -90 dan 90
    'lon': np.random.uniform(-180, 180, 100)  # Longitude antara -180 dan 180
})

# Menampilkan peta
st.map(data)
 # 7.4 Input Form
with st.form("form_input"):
     nama = st.text_input("Nama Lengkap", placeholder="Masukkan Nama Lengkap")
     alamat = st.text_area("Alamat", placeholder="Masukkan Alamat")
     usia = st.number_input("Usia", min_value=0, max_value=100, value=20)
     tanggal_lahir = st.date_input("Tanggal Lahir")
     jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
     hobi = st.multiselect("Hobi", ["Membaca", "Menulis", "Menggambar"])
     Motivasi = st.text_area("Motivasi", placeholder="Masukkan Motivasi")
     warna_favorit = st.color_picker("Warna Favorit")
     file = st.file_uploader("Upload Foto", type=["jpg", "jpeg", "png"])
     foto = st.camera_input("Ambil Foto")
     rating = st.slider("Rating", min_value=1, max_value=5, value=3)
 
     submitted = st.form_submit_button("Submit")
     if submitted:
         st.write("Nama:", nama)
         st.write("Alamat:", alamat)
         st.write("Usia:", usia)
         st.write("Tanggal Lahir:", tanggal_lahir)
         st.write("Jenis Kelamin:", jenis_kelamin)
         st.write("Hobi:", hobi)
         st.write("Motivasi", Motivasi)
         st.write("Warna Favorit:", warna_favorit)
         st.write("File:", file)
         st.write("Foto:", foto)
         st.write("Rating:", rating)

#Menampilkan vidio URL
st.title("Menampilkan Vidio URL")
st.video('https://youtu.be/gBg0qyuK1EQ?si=Mwv5TBN9s6x6JCOA')

#Menampilkan Musik Mp3
st.title("Menampilkan Musik Mp3")
# Ganti dengan lokasi file musik Anda
audio_file = open("C:/Musik/Sendiri.mp3", "rb")  # Lokasi file musik baru
audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/mp3")
