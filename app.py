import streamlit as st

st.set_page_config(
    page_title="Aayush Kumar - Engineer, Roboticist, Maker",
    page_icon="👨🏻‍💻",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.5, 0.5], gap="large")
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
        border-radius: 100%;
    }
    </style>

    <div class="profile-img">

    ![]('PXL_20240102_000607702-EDIT.jpg')
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.image('PXL_20240102_000607702-EDIT.jpg')
with col2:
    st.markdown(
        """
    #    
    # Aayush Kumar 

    - MS Student at University of Washington
    - Technical Asssistant at Prototyping LAB, GIX
    - Electrical Engineer
    - Roboticist
    
    """
    )


st.markdown(
    """
# Projects

"""
)
col3, col4 = st.columns([0.5, 0.5], gap="large")


with col3:
    st.markdown(
        '''
        [Smart Wearable](https://www.youtube.com/watch?v=UTy-pAyOvbw&t=29s)

    '''
    )
    st.video("https://www.youtube.com/watch?v=UTy-pAyOvbw&t=29s")

with col4:
    st.markdown(
        '''
        [6 DOF Robotic Arm](https://www.youtube.com/watch?v=X7lOsNUw-w0)

    '''
    )
    st.video("https://www.youtube.com/watch?v=X7lOsNUw-w0")

      


st.markdown(
    """
# Hobbies

- Playing table tennis
- Making embedded Projects
- Reverse engineering cool gadgets
- Swimming

""")
st.markdown(
    """
# About

I'am a Graduate Student at University of Washington majoring in Techhnology and Innovation - Robotics, and I have Bachelor's in Electronics and Electrical Engineer from Manipal University Jaipur with proficient technical skills in the field Embedded System Development, Robotics, 3D Printing, and Intellectual Property, Patent Prosecutions. 
Moreover, I'am an Embedded Hardware and Robotics enthusiast. I like to explore new gadgets and 3D print my own designs. 
I'am a fast learner who is always curious about new innovations in technology so that i can keep on upgrading my skill level to work on the latest technology.

""")


ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/zaayush" target="_blank"> by zaayush</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)
