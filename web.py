import streamlit as st
import al

def main():
    st.title("Web Information & APK Uploader")
    
    st.header("What is the Web?")
    st.write(
        "The web, also known as the World Wide Web (WWW), is a system of interlinked hypertext documents accessed via the Internet. "
        "Users can view web pages using a web browser and navigate between them using hyperlinks. The web enables communication, commerce, entertainment, and information sharing globally."
    )
    
    st.header(al)
    uploaded_file = st.file_uploader("Choose an APK file", type=["apk"])
    
    if uploaded_file is not None:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        
        # Optionally, save the file
        with open(f"uploaded_{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write("File saved successfully.")
    
if __name__ == "__main__":
    main()
