'''
CHO TIẾNG VIỆT
'''


import PyPDF2
import os

so_la_ma_co_hai_chu = ['ii', 'iv', 'vi', 'ix']
so_la_ma_co_ba_chu = ['iii', 'vii']
so_la_ma_co_bon_chu = ['viii']

LIMIT = 4

bang_chu_cai = [
    'a', 'ă', 'â', 'b', 'c', 'd', 'đ', 'e', 'ê', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 
    'o', 'ô', 'ơ', 'p', 'q', 'r', 's', 't', 'u', 'ư', 'v', 'x', 'y'
]


def pdf_to_text(pdf_path, output_txt):
    
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        
        ### Process the first 20 pages
        for page_num in range(1, 20):
            page = pdf_reader.pages[page_num]
            pre_page_text = page.extract_text()
            
            # Nếu gặp bảng thì skip cả trang
            if any(keyword in pre_page_text for keyword in [". . . . ", "...............", "DANH MỤC THUẬT NGỮ VÀ TỪ VIẾT TẮT", "Bảng"]):
                continue
            lines = pre_page_text.split('\n')
            page_text = ''
            text += '\n'
            
            # Kiểm tra trong lines[i] có chứa công thức hay không
            for i in range(len(lines)):
                if len(lines[i]) > 2:
                    if lines[i][-1] == ')' and lines[i][-2] >= '0' and lines[i][-2] <= '9' and lines[i][-3] == '.' and lines[i][-4] >= '0' and lines[i][-4] <= '9' and lines[i][-5] == '(':
                        j = i
                        while (j - 1 >= 0 and len(lines[j - 1]) > 0) and ((lines[j - 1][-1] != ':') or (lines[j - 1][-1] in bang_chu_cai and lines[j - 1][-2] in bang_chu_cai)):
                            lines[j] = ''
                            j -= 1
                        lines[j] = ''
            
            for i in range(len(lines)):
                if len(lines[i]) > 2:
                    word_count = len(lines[i].split())
                    if word_count <= LIMIT:
                        continue
                    if ((lines[i][0] >= '0' and lines[i][0] <= '9') and (lines[i][1] == '.') and (lines[i][2] >= '0' and lines[i][2] <= '9')) or (lines[i][: 6] == 'CHƯƠNG') or (lines[i][: 4] == 'Hình'):
                        continue
                    elif (lines[i][0] >= '0' and lines[i][0] <= '9') and (lines[i][1] == '.') and (lines[i][2] == ' ') and len(lines[i]) < 50:
                        continue
                    else:
                        page_text += lines[i] + '\n'
                
                
            
            if len(page_text) > 1:
                if page_text[-2:] in so_la_ma_co_hai_chu:
                    text += page_text[:-2]
                elif page_text[-3:] in so_la_ma_co_ba_chu:
                    text += page_text[:-3]
                elif page_text[-4:] in so_la_ma_co_bon_chu:
                    text += page_text[:-4]
                else:
                    if page_text[-2] >= '0' and page_text[-2] <= '9':
                        text += page_text[:-2]
                    else:
                        text += page_text[:-1]
        
        
        ### Process the rest of the pages
        for page_num in range(21, len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pre_page_text = page.extract_text()
            
            # Nếu gặp bảng thì skip cả trang
            if any(keyword in pre_page_text for keyword in ["Bảng"]):
                continue
            
            if any(keyword in pre_page_text for keyword in ["TÀI LIỆU THAM KHẢO"]):
                break
            
            # Kiểm tra trong lines[i] có chứa công thức hay không
            for i in range(len(lines)):
                if len(lines[i]) > 2:
                    if lines[i][-1] == ')' and lines[i][-2] >= '0' and lines[i][-2] <= '9' and lines[i][-3] == '.' and lines[i][-4] >= '0' and lines[i][-4] <= '9' and lines[i][-5] == '(':
                        j = i
                        while (j - 1 >= 0 and len(lines[j - 1]) > 0) and ((lines[j - 1][-1] != ':') or (lines[j - 1][-1] >= 'a' and lines[j - 1][-1] <= 'z' and lines[j - 1][-2] >= 'a' and lines[j - 1][-2] <= 'z')):
                            lines[j] = ''
                            j -= 1
                        lines[j] = ''
            
            lines = pre_page_text.split('\n')
            page_text = ''
            text += '\n'
            
            for i in range(len(lines)):
                if len(lines[i]) > 2:
                    word_count = len(lines[i].split())
                    if word_count <= LIMIT:
                        continue
                    if ((lines[i][0] >= '0' and lines[i][0] <= '9') and (lines[i][1] == '.') and (lines[i][2] >= '0' and lines[i][2] <= '9')) or (lines[i][: 6] == 'CHƯƠNG') or (lines[i][: 4] == 'Hình'):
                        continue
                    elif (lines[i][0] >= '0' and lines[i][0] <= '9') and (lines[i][1] == '.') and (lines[i][2] == ' ') and len(lines[i]) < 50:
                        continue
                    else:
                        if lines[i][-1] == '-' and lines[i][-2] >= 'a' and lines[i][-2] <= 'z':
                            page_text += lines[i][:-1]
                        else:
                            page_text += lines[i] + '\n'
                    
            if len(page_text) > 1:
                if page_text[-2] >= '0' and page_text[-2] <= '9':
                    text += page_text[:-2]
                else:
                    text += page_text[:-1]
        
        with open(output_txt, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

if __name__ == "__main__":
    input_dir = '/Users/hoangducanh/Documents/Hoc o HUST/pdf_to_text/test_input/'
    output_dir = '/Users/hoangducanh/Documents/Hoc o HUST/pdf_to_text/test_output/'
    
    for i in range(1, 6):
        pdf_path = os.path.join(input_dir, f'input{i}.pdf')
        output_txt = os.path.join(output_dir, f'output{i}.txt')
        pdf_to_text(pdf_path, output_txt)
        print(f"PDF {i} converted to text successfully!")
            
            