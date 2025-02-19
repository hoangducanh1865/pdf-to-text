import PyPDF2
import os

def pdf_to_text(pdf_path, output_txt):
    
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            lines = page_text.split('\n')
            
            for line in lines:
                word_count = len(line.split())
                if "REFERENCE" in line:
                    break
                if "..............." in line or "CHƯƠNG" in line or "Biểu đồ" in line or "Figure" in line or "Table" in line or "Ảnh" in line or "Bảng" in line or "Hình" in line:
                    continue
                if word_count > 10:
                    text = text + line + " "

            if len(text) > 1:
                if text[-2] >= '0' and text[-2] <= '9':
                    text = text[:-2]
                else:
                    text = text[:-1]
                
        with open(output_txt, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

if __name__ == "__main__":
    input_dir = '/Users/hoangducanh/Library/Mobile Documents/com~apple~CloudDocs/Hoc o HUST <3/Nhóm anh Minh/pdf to text/test input/'
    output_dir = '/Users/hoangducanh/Library/Mobile Documents/com~apple~CloudDocs/Hoc o HUST <3/Nhóm anh Minh/pdf to text/test output/'

    # Process multiple input files
    for i in range(1, 4):  # Adjust the range as needed
        pdf_path = os.path.join(input_dir, f'input{i}.pdf')
        output_txt = os.path.join(output_dir, f'output{i}.txt')
        pdf_to_text(pdf_path, output_txt)
        print(f"PDF {i} converted to text successfully!")