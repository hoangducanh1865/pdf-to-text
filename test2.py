import PyPDF2
import re
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

# def clean_text(text):
#     """Thực hiện bước làm sạch dữ liệu văn bản."""
#     # Loại bỏ nhiều dấu phẩy đầu dòng
#     text = re.sub(r'^[„",]+', '', text, flags=re.MULTILINE)

#     # Loại bỏ dấu đầu dòng (•, -, ●, ◦, →)
#     text = re.sub(r'^\s*[-•●◦→]\s*', '', text, flags=re.MULTILINE)

#     # Loại bỏ các tham chiếu dạng [1], [2]...
#     text = re.sub(r'\[\d+\]', '', text)

#     # Loại bỏ các URL
#     text = re.sub(r'http[s]?://\S+', '', text)

#     # Loại bỏ các newline dư thừa (> 2 lần xuống dòng)
#     text = re.sub(r'\n{3,}', '\n\n', text)

#     # Loại bỏ đoạn văn có độ dài < 50 ký tự
#     paragraphs = text.split("\n")
#     text = "\n".join([p.strip() for p in paragraphs if len(p.strip()) >= 50])

#     # Ghép dòng bị xuống hàng do lỗi chuyển đổi PDF
#     text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)

#     return text.strip()

def clean_line(line):

    line = re.sub(r'^[„",]+', '', line, flags=re.MULTILINE)

    line = re.sub(r'^\s*[-•●◦→]\s*', '', line, flags=re.MULTILINE)

    line = re.sub(r'\[\d+\]', '', line)

    line = re.sub(r'http[s]?://\S+', '', line)

    # Ghép dòng bị xuống hàng do lỗi chuyển đổi PDF
    line = re.sub(r'\n{3,}', '\n\n', line)
    return line

def pdf_to_text(pdf_path, output_txt):
    try:
        with open(pdf_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            final_text = ""
            found_count = 0

            for page_num in range(len(reader.pages)):
                text = reader.pages[page_num].extract_text()
                if not text:
                    continue  

                sentences = text.split("\n")  
                sentences = [s.strip() for s in sentences if not re.search(r"[∑∫√≈≤≥≠π∞αβγδθλμνξρσφψω×ϕ{}|τ]+", s)]

                fixed_sentences = []
                i = 0

                while i < len(sentences):
                    line = sentences[i]

                    # Kiểm tra nếu dòng chỉ chứa số (có thể là số trang)
                    if re.match(r"^\d+\s*$", line) and i + 1 < len(sentences):  
                        if i > 0 and not re.search(r"[.?:]$", sentences[i - 1]):  
                            fixed_sentences[-1] += " " + sentences[i + 1]  
                        i += 1  
                    else:
                        fixed_sentences.append(line)
                    i += 1

                for sentence in fixed_sentences:
                    if re.search(r'CHƯƠNG\s*1.*GIỚI THIỆU', sentence, re.IGNORECASE) or "CHAPTER 1." in sentence:
                        found_count += 1

                if found_count >= 2:
                    final_text += "\n".join(fixed_sentences[1:])  

        if not final_text.strip():
            print(f"❌ Không có nội dung nào được trích xuất từ {pdf_path}. Kiểm tra lại PDF hoặc điều kiện tìm kiếm.")
            return

        # ✅ Xử lý nối các dòng bị cắt bởi dấu "-"
        fixed_lines = []
        buffer = ""
        
        for line in final_text.split("\n"):
            line = clean_line(line)
            if line.endswith("-"):  
                buffer += line[:-1]  
            else:
                buffer += " " + line  
                if buffer.endswith(".") or buffer.endswith(":"):  
                    fixed_lines.append(buffer.strip())
                    buffer = ""

        if buffer:  
            fixed_lines.append(buffer.strip())

        final_text = "\n".join(fixed_lines)  

        # Ghi vào file text
        with open(output_txt, "w", encoding="utf-8") as txt_file:
            txt_file.write(final_text)

        print(f"✅ PDF '{pdf_path}' converted and cleaned successfully!")

    except Exception as e:
        print(f"❌ Failed to convert {pdf_path}: {e}")

if __name__ == "__main__":
    input_dir = '/Users/trannguyenmyanh/Documents/HUST/AUTH SCAN/pdf-to-text/input/english'
    output_dir = '/Users/trannguyenmyanh/Documents/HUST/AUTH SCAN/pdf-to-text/output/english'
    
    for pdf_file in os.listdir(input_dir):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, pdf_file)
            try:
                output_txt = os.path.join(output_dir, get_file_name(pdf_path))
                pdf_to_text(pdf_path, output_txt)
                print(f"{pdf_file} converted to text successfully!")
            except Exception as e:
                print(f"Failed to convert {pdf_file}: {e}")