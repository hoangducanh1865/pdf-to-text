import PyPDF2
import os

def pdf_to_text(pdf_path, output_txt):
    
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        
        for page_num in range(1, len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            text += page_text
                
        with open(output_txt, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

if __name__ == "__main__":
    input_dir = '/Users/hoangducanh/Library/Mobile Documents/com~apple~CloudDocs/Hoc o HUST <3/Nhóm anh Minh/pdf to text/test input/'
    output_dir = '/Users/hoangducanh/Library/Mobile Documents/com~apple~CloudDocs/Hoc o HUST <3/Nhóm anh Minh/pdf to text/test output/'

    # Process multiple input files
    for i in range(1, 5):  # Adjust the range as needed
        pdf_path = os.path.join(input_dir, f'input{i}.pdf')
        output_txt = os.path.join(output_dir, f'output{i}.txt')
        pdf_to_text(pdf_path, output_txt)
        print(f"PDF {i} converted to text successfully!")
        