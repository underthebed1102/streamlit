from PIL import Image
import streamlit as st
import requests
st.set_page_config(page_title="Our Journey", page_icon=":tada:", layout="wide")


#Load Asset
img_2 = Image.open("steamlit/images/2.png")
img_3 = Image.open("streamlit/images/3.jpg")
img_contact_form = Image.open("streamlit/images/1.jpg")
#img_lottie_annimation = Image.open
#HEADER
with st.container():
    st.subheader("Halo, ini aku bubuw mu tersayang yang masih sering bikin kamu marah:wave:")
    st.title("The Journey To Go Beyond")
    st.write("Perjalanan yang dimulai dari gimik dan selera humor yang agak random")
with st.container():  
    st.write("---")
    left_column = st.columns(2)
with left_column:
    st.header("Permulaan")
    st.write("##")
    st.write("""
    Percaya gk sih ada hubungan yang dimulai dari sama-sama punya selera gimik yang sama.
    Ada, kita contohnya semua dari yang awalnya cuma teman biasa yang bahkan asing.
    Dan aku bersyukur karena tugas waktu itu aku dipertemukan sama kamu.
    """
            )

with st.container():
    st.write("---")
    st.header("Jalan jalan")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    
    with text_column:
        st.subheader("Gajah")
        st.write("""
        Masih inget gk yang ini pertama kali kita jalan keluar seharian bareng. pertama kali cuma kamu sama aku ngabisin waktu bareng.
        Mungkin agak aneh tapi aku seneng banget bisa abisin waktu di kebun binatang bareng kamu dan kalau boleh jujur aku udah suka tau sama kamu disana
        """
                )
with st.container():
    st.write("---")
    st.header("Anak Kabupaten")
    st.write("##")
    image_column1, text_column1 = st.columns((3,4))
    with image_column1:
        st.image(img_2)
    
    with text_column1:
        st.subheader("Sakit")
        st.write("""
        Disini awal kita makin deket manis ya bub, aku yang terlalu maksa badan aku sampe akhirnya drop sendiri. Alhamdulillah ada kamu yg ngerawat aku, jagain aku walaupun dengan kondisi kamar aku yg panas dan berantakan. kalau ditanya apa yg aku rasa setelah itu, aku cuma ngerasa beruntung dan kamu bener aku jatuh semakin dalam untuk cinta sama kamu. Bisa dibilang aku gk ada alasan buat gk sayang sama cinta sama kamu
        """
                )
with st.container():
    st.write("---")
    st.header("Sorry")
    st.write("##")
    image_column2, text_column2 = st.columns((5,6))
    with image_column2:
        st.image(img_3)
    
    with text_column2:
        st.subheader("Always")
        st.write("""
        Saat itu aku juga abis buat kamu marah sama seperti sekarang, aku juga janji buat berusaha nggk buat kamu marah. Tapi, maafin aku ya yang sampai saat ini aku masih aja buat kamu marah, aku selalu cinta sama kamu sampai kapan pun itu aku sayang sama kamu cinta sama kamu gk pernah sedetikpun aku gk mikirin kamu. Maafin aku ya yang belakangan ini nyuekin kamu padahal jelas-jelas ada kamu yg selalu disamping aku malah aku yg sibuk dengan mikirin hal yg seharusnya bukan tanggung jawab aku. kurasa sampai sini dulu nanti aku lanjut ya cinta batre aku udah muncul notif disini mati lampu pagi kalo udah nyala aku buat lebih baik lagi. See you tomorrow and can't wait for our next adventure
        """
                )
