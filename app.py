import streamlit as st

  
def main():
    #print("hello world")    
    st.set_page_config(page_title="Chat with PDF", page_icon=":books:")
    st.header("Chat with PDF :books:")
    st.text_input("Ask a question about your documents")
    
    with st.sidebar:
        st.subheader("Your document")
        st.file_uploader("Upload you PDF here and click on 'Prodess'")
        st.button("Process")

if __name__ == '__main__':
    main()