import streamlit as st

st.set_page_config(
    page_title="Abhishek's Website",
    page_icon=":sunglasses:",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
        border-radius: 25%;
        border: 3px solid white;
    }
    </style>

    <div class="profile-img">

    ![](https://raw.githubusercontent.com/Abhsin/TECHIN510_Lab_1_Hello_Streamlit/main/images/ProfilePic.jpg)
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
    # Abhishek (He/Him)
                
    - Designer
    - Innovator
    - MS Student at University of Washington

    """
    )

st.markdown(
    """
# What I have been upto?
In the intricate tapestry of my existence, every pursuit and endeavor becomes a unique thread in the narrative of my life. What I've been up to is not just a series of actions; it's an exploration of the profound depths of my own consciousness. Navigating the complexities of life, each choice and endeavor is like a brushstroke on the canvas of my personal journey. Whether I'm immersed in intellectual pursuits, expressing my creativity, or seeking self-discovery, the essence lies in my continual quest for meaning and understanding. It's within these pursuits that I discover the rich tapestry of my own existence, where each thread contributes to the unfolding masterpiece of a life well-lived.

"""
)

st.markdown(
    """
# My Projects - 
""")
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
<style>
.container {
  position: relative;
  width: 100%;
}

.image {
  display: block;
  width: 100%;
  border-radius: 10%;


}

.overlay1 {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100%;
  width: 100%;
  opacity: 0;
  transition: .5s ease;
  background-color: #451030;
  border-radius: 10%;
}

.container:hover .overlay1 {
  opacity: 1;
}

.text {
  color: white;
  font-size: 20px;
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  text-align: center;
}
</style>

<div class="container">
  <img src="https://raw.githubusercontent.com/Abhsin/TECHIN510_Lab_1_Hello_Streamlit/main/images/AP.png" alt="Avatar" class="image">
  <a href = "https://drive.google.com/file/d/1eciKHR7cMEy8mxDYhHs37HHtbjGI6Gh7/view">
  <div class="overlay1">
    <div class="text" >Annapurna</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)    
    
with col2:
    st.markdown(
        """
<style>
.container {
  position: relative;
  width: 100%;
}

.image {
  display: block;
  width: 100%;
  border-radius: 10%;

}

.overlay {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100%;
  width: 100%;
  opacity: 0;
  transition: .5s ease;
  background-color: #17B254;
  border-radius: 10%;
}

.container:hover .overlay {
  opacity: 1;
}

.text {
  color: white;
  font-size: 20px;
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  text-align: center;
}
</style>

<div class="container">
  <img src="https://raw.githubusercontent.com/Abhsin/TECHIN510_Lab_1_Hello_Streamlit/main/images/latis.png" alt="Avatar" class="image">
  <a href = "https://drive.google.com/file/d/1SKhe__KB364oGXmt_6VHf5aSD2CWtDYt/view">
  <div class="overlay">
    <div class="text" >LATIS: A Biomimicry Project</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)


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
    visibility: hidden;
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
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/Abhsin" target="_blank"> by Abhishek</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)