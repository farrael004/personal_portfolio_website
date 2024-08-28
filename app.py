import streamlit as st


def main():
    st.set_page_config(page_title="Rafael Moraes - Portfolio", page_icon="✨")

    home_page = st.Page("pages/home.py", title="Home", icon=":material/home:")
    agpal_chat_page = st.Page(
        "pages/agpal_chat.py", title="AgPal Chat", icon=":material/chat:"
    )
    deduplication_tool_page = st.Page(
        "pages/deduplication_tool.py",
        title="Deduplication Tool",
        icon=":material/search:",
    )
    awards_page = st.Page("pages/awards.py", title="Awards", icon=":material/trophy:")
    generative_ai_page = st.Page(
        "pages/generative_ai.py", title="Generative AI", icon=":material/star:"
    )
    data_visualization_page = st.Page(
        "pages/data_visualization.py",
        title="Data Visualization",
        icon=":material/monitoring:",
    )
    experiences_page = st.Page(
        "pages/experiences.py", title="Experiences", icon=":material/work:"
    )
    education_page = st.Page(
        "pages/education.py", title="Education", icon=":material/school:"
    )
    skills_page = st.Page("pages/skills.py", title="Skills", icon=":material/bolt:")
    pg = st.navigation(
        {
            "Home": [home_page],
            "Interactive demos": [generative_ai_page, data_visualization_page],
            "Projects": [agpal_chat_page, deduplication_tool_page],
            "Resume": [experiences_page, awards_page, education_page, skills_page],
        }
    )

    pg.run()


if __name__ == "__main__":
    main()
