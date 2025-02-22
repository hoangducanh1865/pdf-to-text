'''
CHO TIẾNG VIỆT
'''


import PyPDF2
import os

so_la_ma_co_hai_chu = ['ii', 'iv', 'vi', 'ix']
so_la_ma_co_ba_chu = ['iii', 'vii']
so_la_ma_co_bon_chu = ['viii']

LIMIT = 4

ho_viet_nam = [
    "Nguyễn", "Nguyen", "NGUYỄN", "NGUYEN",
    "Trần", "Tran", "TRẦN", "TRAN",
    "Lê", "Le", "LÊ", "LE",
    "Phạm", "Pham", "PHẠM", "PHAM",
    "Hoàng", "Hoang", "HOÀNG", "HOANG",
    "Huỳnh", "Huynh", "HUỲNH", "HUYNH",
    "Phan", "Phan", "PHAN", "PHAN",
    "Vũ", "Vu", "VŨ", "VU",
    "Võ", "Vo", "VÕ", "VO",
    "Đặng", "Dang", "ĐẶNG", "DANG",
    "Bùi", "Bui", "BÙI", "BUI",
    "Đỗ", "Do", "ĐỖ", "DO",
    "Hồ", "Ho", "HỒ", "HO",
    "Ngô", "Ngo", "NGÔ", "NGO",
    "Dương", "Duong", "DƯƠNG", "DUONG",
    "Lý", "Ly", "LÝ", "LY",
    "Đinh", "Dinh", "ĐINH", "DINH",
    "Đoàn", "Doan", "ĐOÀN", "DOAN",
    "Trương", "Truong", "TRƯƠNG", "TRUONG",
    "Văn", "Van", "VĂN", "VAN",
    "Tô", "To", "TÔ", "TO",
    "Tạ", "Ta", "TẠ", "TA",
    "Tăng", "Tang", "TĂNG", "TANG",
    "Tống", "Tong", "TỐNG", "TONG",
    "Quách", "Quach", "QUÁCH", "QUACH",
    "Lâm", "Lam", "LÂM", "LAM",
    "Cao", "Cao", "CAO", "CAO",
    "Mai", "Mai", "MAI", "MAI",
    "Khương", "Khuong", "KHƯƠNG", "KHUONG",
    "Hà", "Ha", "HÀ", "HA",
    "Đào", "Dao", "ĐÀO", "DAO",
    "Hồng", "Hong", "HỒNG", "HONG",
    "Chu", "Chu", "CHU", "CHU",
    "Hứa", "Hua", "HỨA", "HUA",
    "Từ", "Tu", "TỪ", "TU",
    "Thái", "Thai", "THÁI", "THAI",
    "Ôn", "On", "ÔN", "ON",
    "Thạch", "Thach", "THẠCH", "THACH",
    "Châu", "Chau", "CHÂU", "CHAU",
    "Mạc", "Mac", "MẠC", "MAC",
    "Đàm", "Dam", "ĐÀM", "DAM",
    "La", "La", "LA", "LA",
    "Giang", "Giang", "GIANG", "GIANG",
    "Vi", "Vi", "VI", "VI",
    "Lương", "Luong", "LƯƠNG", "LUONG",
    "Khuất", "Khuat", "KHUẤT", "KHUAT",
    "Chử", "Chu", "CHỬ", "CHU",
    "Lục", "Luc", "LỤC", "LUC",
    "Bành", "Banh", "BÀNH", "BANH",
    "Lưu", "Luu", "LƯU", "LUU",
    "Tường", "Tuong", "TƯỜNG", "TUONG",
    "Nhâm", "Nhan", "NHÂM", "NHAN",
    "Ân", "An", "ÂN", "AN",
    "An", "An", "AN", "AN",
    "Triệu", "Trieu", "TRIỆU", "TRIEU",
    "Kiều", "Kieu", "KIỀU", "KIEU",
    "Cổ", "Co", "CỔ", "CO",
    "Nghiêm", "Nghiem", "NGHIÊM", "NGHIEM",
    "Bạch", "Bach", "BẠCH", "BACH",
    "Ninh", "Ninh", "NINH", "NINH",
    "Đường", "Duong", "ĐƯỜNG", "DUONG",
    "Thân", "Than", "THÂN", "THAN",
    "Phùng", "Phung", "PHÙNG", "PHUNG",
    "Thịnh", "Thinh", "THỊNH", "THINH",
    "Trịnh", "Trinh", "TRỊNH", "TRINH",
    "Quang", "Quang", "QUANG", "QUANG",
    "Cấn", "Can", "CẤN", "CAN",
    "Lai", "Lai", "LAI", "LAI",
    "Thi", "Thi", "THI", "THI",
    "Yên", "Yen", "YÊN", "YEN",
    "Tôn", "Ton", "TÔN", "TON",
    "Sử", "Su", "SỬ", "SU",
    "Việt", "Viet", "VIỆT", "VIET",
    "Ngọc", "Ngoc", "NGỌC", "NGOC",
    "Hàn", "Han", "HÀN", "HAN",
    "Kim", "Kim", "KIM", "KIM",
    "Vĩnh", "Vinh", "VĨNH", "VINH",
    "Đắc", "Dac", "ĐẮC", "DAC",
    "Thiều", "Thieu", "THIỀU", "THIEU",
    "Bảo", "Bao", "BẢO", "BAO",
    "Diệp", "Diep", "DIỆP", "DIEP",
    "Xà", "Xa", "XÀ", "XA",
    "Lư", "Lu", "LƯ", "LU",
    "Cung", "Cung", "CUNG", "CUNG",
    "Nông", "Nong", "NÔNG", "NONG",
    "Giáp", "Giap", "GIÁP", "GIAP",
    "Kha", "Kha", "KHA", "KHA",
    "Chung", "Chung", "CHUNG", "CHUNG",
    "Tào", "Tao", "TÀO", "TAO",
    "Ái", "Ai", "ÁI", "AI",
    "Hùng", "Hung", "HÙNG", "HUNG",
    "Ngũ", "Ngu", "NGŨ", "NGU",
    "Tịch", "Tich", "TỊCH", "TICH",
    "Sơn", "Son", "SƠN", "SON",
    "Cù", "Cu", "CÙ", "CU",
    "Phương", "Phuong", "PHƯƠNG", "PHUONG",
    "Quyền", "Quyen", "QUYỀN", "QUYEN",
    "Tiêu", "Tieu", "TIÊU", "TIEU",
    "Bế", "Be", "BẾ", "BE",
    "Trác", "Trac", "TRÁC", "TRAC",
    "Hán", "Han", "HÁN", "HAN",
    "Hầu", "Hau", "HẦU", "HAU",
    "Vương", "Vuong", "VƯƠNG", "VUONG"
]

bang_chu_cai = [
    'a', 'ă', 'â', 'b', 'c', 'd', 'đ', 'e', 'ê', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 
    'o', 'ô', 'ơ', 'p', 'q', 'r', 's', 't', 'u', 'ư', 'v', 'x', 'y'
]


### Lấy ra tên file
def get_file_name(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        file_name = ''
        page = pdf_reader.pages[0]
        page_text = page.extract_text()
        lines = page_text.split('\n')
        
        for i in range(2, len(lines)):
            first_word = lines[i].split()[0]
            if first_word in ho_viet_nam:
                break
            file_name += lines[i] + ' '
        file_name = file_name[:-1].replace(' ', '_')
        return file_name + '.txt'


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
    input_dir = '/Users/hoangducanh/Library/Mobile Documents/com~apple~CloudDocs/Hoc o HUST <3/Nhóm anh Minh/pdf to text/test input/'
    output_dir = '/Users/hoangducanh/Library/Mobile Documents/com~apple~CloudDocs/Hoc o HUST <3/Nhóm anh Minh/pdf to text/test output/'
    
    for i in range(1, 5):
        pdf_path = os.path.join(input_dir, f'input{i}.pdf')
        output_txt = os.path.join(output_dir, get_file_name(pdf_path))
        pdf_to_text(pdf_path, output_txt)
        print(f"PDF {i} converted to text successfully!")
            
            