import PyPDF2

def pdf_to_text(pdf_path, output_txt):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PdfReader object instead of PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store the text
        text = ''
        found_count = 0  # Counter to track occurrences of "CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI"
        
        # Loop through the pages starting from the first page
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()

            # Check if the page contains the target line
            if "CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI" in page_text:
                found_count += 1
            if "INTRODUCTION" in page_text:
                found_count += 1

            # Once the second occurrence is found, start adding text
            if found_count >= 2:
                lines = page_text.split('\n')
                first_line = lines[0]
                # print(first_line)
                # remaining_text = '\n'.join(lines[1:])
                
                if first_line[:7] == "CHAPTER": 
                    page_text = '\n'.join(lines[1:])
                    # print(page_text)
                if page_text[-2] >= '0' and page_text[-2] <= '9':
                    text = text + page_text[:-2]
                else:
                    text = text + page_text[:-1]
                

        # Write the extracted text to a text file
        with open(output_txt, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

if __name__ == "__main__":
    pdf_path = '/Users/hoangducanh/Library/Mobile Documents/com~apple~CloudDocs/Hoc o HUST <3/Nhóm anh Minh/pdf to text/test input/input4.pdf'
    output_txt = '/Users/hoangducanh/Library/Mobile Documents/com~apple~CloudDocs/Hoc o HUST <3/Nhóm anh Minh/pdf to text/test output/output4.txt'

    pdf_to_text(pdf_path, output_txt)

    print("PDF converted to text successfully!")