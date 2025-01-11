import streamlit as st


st.set_page_config(page_title="Web-Based Text Editor", layout="wide")


st.title("📝 Web-Based Text Editor")


st.sidebar.header("Formatting Options")


formatting_options = [
    {"name": "Bold", "style": "font-weight: bold;"},
    {"name": "Italic", "style": "font-style: italic;"},
    {"name": "Underline", "style": "text-decoration: underline;"},
]
selected_options = [opt["style"] for opt in formatting_options if st.sidebar.checkbox(opt["name"])]


font_size = st.sidebar.slider("Font Size", min_value=12, max_value=48, value=16)
text_color = st.sidebar.color_picker("Text Color", value="#000000")
background_color = st.sidebar.color_picker("Background Color", value="#ffffff")


alignments = ("Left", "Center", "Right")
alignment = st.sidebar.radio("Text Alignment", alignments)

alignment_styles = {
    "Left": "text-align: left;",
    "Center": "text-align: center;",
    "Right": "text-align: right;",
}
selected_options.append(alignment_styles[alignment])


transformations = [
    ("Normal", "none"),
    ("Uppercase", "uppercase"),
    ("Lowercase", "lowercase"),
    ("Capitalize", "capitalize"),
]
transformation = st.sidebar.radio("Text Transformation", [t[0] for t in transformations])


for name, css_value in transformations:
    if transformation == name:
        selected_options.append(f"text-transform: {css_value};")


selected_options.extend([
    f"font-size: {font_size}px;",
    f"color: {text_color};",
    f"background-color: {background_color};",
])


st.markdown("### Text Editor")
user_text = st.text_area("Write your text below:", height=300, placeholder="Start typing here...")


if user_text:
    styles = " ".join(selected_options)
    styled_text = f"<div style='{styles}'>{user_text}</div>"

    st.markdown("### Preview")
    st.markdown(styled_text, unsafe_allow_html=True)


    st.download_button(
        label="📥 Download as HTML",
        data=f"<html><body>{styled_text}</body></html>",
        file_name="styled_text.html",
        mime="text/html",
    )
else:
    st.info("Start typing to see the preview!")


st.markdown(
    """
    <style>
        textarea {
            font-family: Arial, sans-serif !important;
        }
        .stButton > button {
            background-color: orange !important;
            color: white !important;
        }
        .stRadio > div {
            flex-direction: row !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
