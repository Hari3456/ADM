import streamlit as st
import al

def main():
    st.title("Android Malware Detection using ML")
    
    st.write(
        "Give an APK file in input below."
    )
    uploaded_file = st.file_uploader("Choose an APK file", type=["apk"])
    
    if uploaded_file is not None:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        
        # Optionally, save the file
        with open(f"uploaded_{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write("File saved successfully.")
    
if __name__ == "__main__":
    main()
