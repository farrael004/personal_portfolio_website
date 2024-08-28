import streamlit as st

st.title("Rafael Moraes", anchor=False)
st.subheader("AI Developer", anchor=False)

col1, col2 = st.columns([2, 1])

with col1:
    st.write(
        """
    Welcome to my portfolio! I'm an experienced AI developer with goverment experience. 
    I'm passionate about creating innovative AI solutions and have a track record of developing groundbreaking tools.
    
    ### Highlights:
    - 🚀 Full-time AI Developer at Agriculture and Agri-Food Canada
    - 🏆 [Winner of Canada's Public Service Data Challenge](https://www.linkedin.com/feed/update/urn:li:activity:7232449240822665218/)
    - 💡 Creator of [AgPal Chat](https://agpal.ca/en/home) and AI-assisted [deduplication tool](https://www.fwd50.com/speaker/2116/raphael-moraes)
    - 🌟 Recipient of [multiple performance awards](https://www.linkedin.com/in/rafael-moraes-49407b1ba/details/honors/)

    Feel free to explore my projects and experiences using the sidebar navigation!
    """
    )

with col2:
    st.image(
        "assets/photo.jpg",
        caption="Rafael Moraes",
    )

st.markdown("---")
st.subheader("Contact Information", anchor=False)
st.write("📞 +1 (613) 880 8507")
st.write("✉️ farrael004@Gmail.com")
st.write("🔗 [GitHub](https://github.com/farrael004)")
