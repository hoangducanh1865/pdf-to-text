import fitz  # PyMuPDF
import re

def pdf_to_text(pdf_path, output_txt):
    doc = fitz.open(pdf_path)  
    final_text = ""
    found_count = 0

    for page_num, page in enumerate(doc):  
        text = page.get_text("text")
        if not text:
            continue  
        
        sentences = text.split("\n")  
        sentences = [s.strip() for s in sentences if not re.search(r"[∑∫√≈≤≥≠π∞αβγδθλμνξρσφψω×ϕ{}|τ]+", s)]

        fixed_sentences = []
        i = 0

        while i < len(sentences):
            line = sentences[i]

            # Kiểm tra nếu dòng chỉ chứa số (có thể là số trang)
            if re.match(r"^\d+\s*$", line):
                if i > 0 and not re.search(r"[.?:]$", sentences[i - 1]):  # Nếu dòng trước đó chưa kết thúc câu
                    fixed_sentences[-1] += " " + sentences[i + 1]  # Gộp với dòng sau
                    i += 1  # Bỏ qua dòng tiếp theo
                # Nếu là số trang thực sự, bỏ qua không thêm vào fixed_sentences
            else:
                fixed_sentences.append(line)
            i += 1

        for sentence in fixed_sentences:
            if re.search(r'CHƯƠNG\s*1.*GIỚI THIỆU', sentence, re.IGNORECASE) or "CHAPTER 1. LITERATURE REVIEW" in sentence:
                found_count += 1

        if found_count >= 2:
            final_text += "\n".join(fixed_sentences[1:])  

    if not final_text.strip():
        print("❌ Không có nội dung nào được trích xuất. Kiểm tra lại PDF hoặc điều kiện tìm kiếm.")

    # ✅ Xử lý nối các dòng kết thúc bằng "-"
    fixed_lines = []
    buffer = ""
    
    for line in final_text.split("\n"):
        if line.endswith("-"):  # Nếu dòng kết thúc bằng "-", nối với dòng sau
            buffer += line[:-1]  # Bỏ dấu "-" và lưu vào bộ đệm
        else:
            buffer += " " + line  # Nối phần còn lại
            if buffer.endswith(".") or buffer.endswith(":"):  # Dừng khi gặp dấu "." hoặc ":"
                fixed_lines.append(buffer.strip())
                buffer = ""

    if buffer:  # Nếu còn dữ liệu, thêm vào danh sách
        fixed_lines.append(buffer.strip())

    final_text = "\n".join(fixed_lines)  # Ghép lại thành văn bản hoàn chỉnh

    # Ghi vào file text
    with open(output_txt, "w", encoding="utf-8") as txt_file:
        txt_file.write(final_text.strip())

    print("✅ PDF converted to text successfully!")

if __name__ == "__main__":
    pdf_path = "/Users/trannguyenmyanh/Documents/pdf_to_text/test_input/input4.pdf"
    output_txt = "/Users/trannguyenmyanh/Documents/pdf_to_text/test_output/output4.txt"
    pdf_to_text(pdf_path, output_txt)
