import streamlit as st
import streamlit.components.v1 as stc
import pdfplumber
from PIL import Image
from text_to_audio import get_audio_file_from_uuid,get_uuid_from_api,download_audio_file_from_url
import io
from utils import load_image
from ocr import detect_text


from google.cloud import vision
import io

import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='/home/revanth/Documents/GitHub/Read-to-me/google.json'
from google.cloud import vision
import re
from PIL import Image
from io import BytesIO


st.set_page_config(page_title='OCR',page_icon=':smiley:',initial_sidebar_state='collapsed')


def main():

    HTML = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">OCR App </h1>
    </div>
    """

    audio_output=[]
    detected_text_in_ocr=None
    side_bar_list=['Home','Image','Pdf']
    menu_bar=st.sidebar.selectbox('Menu',side_bar_list)

    if menu_bar=='Home':
        st.subheader('Home Page')
        stc.html(HTML)

        

    elif menu_bar=='Image':
        st.subheader('Upload Image')

        uploaded_image=st.file_uploader('Upload your Images',type=['png','jpeg','jpg'],accept_multiple_files=True)
        voices_list=['principal-bump', 'piniet-toh', 'candace-owens', 'philip-wittebane', 'rideshare', 'fci-dublin', 'odalia-blight', 'morton-toh', 'scorpion-armageddon', 'spamton-a-spamton', 'pump', 'incineroar', 'skid', 'dj-candy-supergroove', 'peyton-roi-list', 'superhorrorbro', 'smurfette-80s', 'jamfm', 'daffinee-toilette', 'mr-guinea-pig', 'georgecarlincomedy', 'tyler-dinky-doo', 'shawn-flynn', 'stephen-hillenburg', 'mattholomule', 'tfaprowl', 'cykill', 'brainy-smurf-80s', 'peach-movie', 'toad-movie', 'bowser-jack-black', 'bowser-jr', 'bowser', 'coral', 'brucelee', 'papa-smurf-80s', 'freddy-egb', 'marlin', 'professor-oak', 'meowth', 'sonic-frontiers', 'barack-obama-erb', 'thespoonyone', 'smurfs-opening-narrator', 'adrian-woop', 'erobb', 'el-chavo', 'allison-angel', 'james-hetfield-mop', 'charlie-brown', 'alan-partridge', 'stripe-heeler', 'lilith-clawthorne', 'sonic-ova', 'kikimora', 'cosmos', 'stan-lee', 'harold-squarepants', 'margaret-squarepants', 'golden-freddy-egb', 'jasmine-masters-ex', 'sam-jn', 'katya-toh', 'jerbo-toh', 'jacob-hopkins', 'hunter-owl-house', 'hooty', 'dory', 'gwendolyn-clawthorne', 'gus-porter-s1', 'earthworm-jim', 'cjetfire', 'gus-porter', 'lucky', 'flora-dsplora', 'ft-freddy-egb', 'emperor-belos', 'edric-blight', 'odessa-cubbage', 'eda-clawthorne-teen', 'chuck-tamzarian', 'replacement-sister', 'foundation', 'psabr-announcer', 'snotty-boy', 'cliffjumper', '50-cent', 'soto', 'lenny-ia', 'oscar-ia', 'zeke', 'dell-clawthorne', 'darius-deamonne', 'mugman', 'counselor-toh', 'pinstripe-potoroo', 'camila-noceda', 'bria', 'ronald-mcdonald', 'boscha', 'wilt', 'bill-toh', 'angmar', 'mori-calliope', 'pepper-ann-pearson', 'uncle-grandpa', 'gmm-link', 'hotwheels-tr', 'king-goobot-vg', 'ooblar-vg', 'cyclonus', 'geico', 'bat-queen', 'adegast-toh', 'adrian-graye', 'mort', 'bubbles-ppg', 'mayor-toadstool', 'marnie-amph', 'marcy-wu', 'spongebob-clean', 'silverboltg1', 'melman-ss', 'robot-krabs', 'doctor-claw', 'tiny-tiger', 'alador-blight', 'amity-blight', 'private-public', 'block-man', 'sonia-masters-ex', 'ghetsis-masters-ex', 'pico-recd', 'annie-brainpop', 'powerglide', 'winston', 'dan-hibiki', 'arne-magnusson', 'metal-sonic', 'batdog', 'chilli-heeler', 'sephiroth']
        selected_voice=st.selectbox('Choose voice',voices_list)

        selected_pace=st.slider('Choose Your Audio Pace',min_value=1,max_value=10)
        if st.button('Process Images'):
            for index,i in enumerate(uploaded_image):
                print('index',index)
                img=Image.open(i)
                st.image(image=img,use_column_width=True,width=50)
                
                
                content=img.save(f'image_files/{index}.jpeg')
                path=f'image_files/{index}.jpeg'

                detected_text_in_ocr=detect_text(path)
                # print('OUTPUT from ocr ',detected_text_in_ocr)
                
            

                # audio_output.append(detected_text_in_ocr)


        
        
                text=detected_text_in_ocr
                print('Checking output of the ocr text ',text)

                st.text_area('Text that has been found in the image',text,max_chars=10000,height=200)

        

        # if st.button('Submit'):
        #     st.write(selected_voice)
        #     st.write(selected_pace)

            

                st.write('Processing audio file')

                uuid=get_uuid_from_api(data=text[0],voice=str(selected_voice),pace=selected_pace)
                print(uuid)

                # audio_file_url=get_audio_file_from_uuid(uuid)
                # print(audio_file_url)


                audio_file=download_audio_file_from_url(uuid)
                print(audio_file)

                if audio_file:
                    st.audio(open('audio_files/audio_output.mp3','rb').read(),format='audio/mp3')


    elif menu_bar=='Pdf':
        st.subheader('Upload Pdf')

        uploaded_pdf=st.file_uploader('Upload your Pdf file',type='pdf',accept_multiple_files=False)

        if st.button('Process'):
            st.write('Processing')

         # Processing ocr model to retreive text


        # Processing text to get the audio file

            


        

        # st.write(uploaded_pdf)

if __name__=='__main__':
    main()