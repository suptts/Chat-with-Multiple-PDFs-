import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_pdf_text(pdf_doc):
    text = ""
    for pdf in pdf_doc:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text +=page.extract_text()
    return text
  
def main():
    #print("hello world")
    load_dotenv()    
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    st.header("Chat with multiple PDF :books:")
    st.text_input("Ask a question about your documents")
    
    with st.sidebar:
        st.subheader("Your documents")
        pdf_doc = st.file_uploader("Upload your PDFs here and click on 'Prodess'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_doc)
                st.write(raw_text)

                # get the text chunks

                # create vector store


if __name__ == '__main__':
    main()