import streamlit as st

st.set_page_config(
    page_title="Abhishek Singh",
    page_icon=":sunglasses:",
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

    ![]('https://raw.githubusercontent.com/Abhsin/TECHIN510_Lab_1_Hello_Streamlit/main/images/ProfilePic.jpg')
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.image('https://raw.githubusercontent.com/Abhsin/TECHIN510_Lab_1_Hello_Streamlit/main/images/ProfilePic.jpg')
with col2:
    st.markdown(
        """
    #    
    # Abhishek Singh

    - MS Student at University of Washington
    - Designer!
    
    """
    )


st.markdown(
    """
# Projects

"""
)


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

I am Alive!

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
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/Abhsin" target="_blank"> by Abhi!</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)