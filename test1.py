import pymupdf  
import os

def pdf_to_text(pdf_path, output_txt):
    # Mở file PDF
    doc = pymupdf.open(pdf_path)
    text = ""

    # Duyệt qua từng trang trong PDF
    for page in doc:
        page_text = page.get_text("text")
        lines = page_text.split('\n')

        for line in lines:
                if any(keyword in line for keyword in ["REFERENCE", "TÀI LIỆU THAM KHẢO"]):
                    break
                if any(keyword in line for keyword in [". . . . ", "...............", "CHƯƠNG", "Biểu đồ", "Figure", "Table", "Ảnh", "Bảng", "Hình"]):
                    continue
                word_count = len(line.split())
                if word_count > 9:
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

    # Xử lý nhiều file PDF
    for i in range(1, 5):  # Điều chỉnh phạm vi nếu cần
        pdf_path = os.path.join(input_dir, f'input{i}.pdf')
        output_txt = os.path.join(output_dir, f'output{i}.txt')

        if os.path.exists(pdf_path):
            pdf_to_text(pdf_path, output_txt)
            print(f"PDF {i} converted to text successfully!")
        else:
            print(f"File {pdf_path} không tồn tại!")
