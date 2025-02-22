import PyPDF2
import os

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

### Lấy ra tên file
def get_file_name(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        file_name = ''
        page = pdf_reader.pages[0]
        page_text = page.extract_text()
        lines = page_text.split('\n')
        
        for i in range(2, len(lines)):
            if len(lines[i]) == 0:
                continue
            words = lines[i].split()
            if not words:
                continue
            first_word = words[0]
            if first_word in ho_viet_nam:
                break
            file_name += lines[i] + ' '
        file_name = file_name[:-1].replace(' ', '_')
        return file_name + '.txt'

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
    input_dir = '/Users/hoangducanh/Library/Mobile Documents/com~apple~CloudDocs/Hoc o HUST/Nhom anh Minh/pdf to text/test input output/input/vietnamese/'
    output_dir = '/Users/hoangducanh/Library/Mobile Documents/com~apple~CloudDocs/Hoc o HUST/Nhom anh Minh/pdf to text/test input output/output/vietnamese/'

    for pdf_file in os.listdir(input_dir):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, pdf_file)
            try:
                output_txt = os.path.join(output_dir, get_file_name(pdf_path))
                pdf_to_text(pdf_path, output_txt)
                print(f"{pdf_file} converted to text successfully!")
            except Exception as e:
                print(f"Failed to convert {pdf_file}: {e}")
        