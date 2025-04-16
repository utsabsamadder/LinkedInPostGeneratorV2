import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Main app layout
def main():
    st.subheader("LinkedIn Post Generator: Codebasics")

    # Sidebar for input options
    st.sidebar.header("Input Options")

    fs = FewShotPosts()
    tags = fs.get_tags()

    # Dropdown for Topic (Tags)
    selected_tag = st.sidebar.selectbox("Topic", options=tags)

    # Dropdown for Length
    selected_length = st.sidebar.selectbox("Length", options=length_options)

    # Dropdown for Language
    selected_language = st.sidebar.selectbox("Language", options=language_options)

    # Main area for custom input
    st.write("### Custom Input")
    custom_input = st.text_area("Enter any additional information or context here...", "")

    # Generate Button
    if st.button("Generate"):
        # Pass the custom input to the generate_post function
        post = generate_post(selected_length, selected_language, selected_tag, custom_input)
        st.write(post)

# Run the app
if __name__ == "__main__":
    main()