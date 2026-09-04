import streamlit as st
import base64
from pathlib import Path

# ============================================================
# CẤU HÌNH TRANG
# ============================================================
st.set_page_config(
    page_title="CV - Đặng Phú Hưng",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# HÀM ĐỌC ẢNH
# ============================================================
def get_image_base64(image_path):
    path = Path(image_path)

    if not path.exists():
        return ""

    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# ============================================================
# CSS - THIẾT KẾ GIAO DIỆN
# ============================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Arial:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}

.stApp {
    background: #eeeeee;
}

/* Ẩn menu Streamlit */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Container chính */
.cv-container {
    width: 900px;
    max-width: 95%;
    margin: 35px auto;
    background: white;
    padding: 35px 32px 45px 32px;
    box-shadow: 0px 2px 12px rgba(0,0,0,0.10);
    color: #111111;
}

/* Header */
.header {
    display: flex;
    align-items: flex-start;
    gap: 27px;
    margin-bottom: 42px;
}

.avatar-box {
    width: 135px;
    min-width: 135px;
    height: 180px;
    border: 1px solid #dddddd;
    padding: 7px;
    box-sizing: border-box;
}

.avatar {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.personal-info {
    flex: 1;
}

.name {
    font-size: 29px;
    font-weight: 700;
    margin: -5px 0 3px 0;
    line-height: 1.2;
}

.position {
    font-size: 17px;
    font-weight: 400;
    margin-bottom: 9px;
}

.info-row {
    font-size: 14px;
    line-height: 1.75;
}

.info-label {
    font-weight: 700;
    display: inline-block;
    width: 92px;
}

/* Section */
.section {
    margin-top: 25px;
}

.section-title {
    font-size: 18px;
    font-weight: 700;
    text-transform: uppercase;
    padding-bottom: 7px;
    border-bottom: 1.5px solid #222222;
    margin-bottom: 17px;
}

/* Text */
.text {
    font-size: 14px;
    line-height: 1.55;
    text-align: left;
}

/* Học vấn / hoạt động */
.timeline {
    display: grid;
    grid-template-columns: 160px 1fr;
    column-gap: 5px;
}

.date {
    font-size: 14px;
    line-height: 1.5;
}

.content {
    font-size: 14px;
    line-height: 1.55;
}

.content-title {
    font-weight: 700;
    text-transform: uppercase;
}

.school {
    font-weight: 700;
    font-size: 14px;
}

.degree {
    margin-top: 2px;
}

.bullet {
    margin-left: 12px;
}

/* Bảng */
.info-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
}

.info-table td {
    padding: 8px 0;
    border-bottom: 1px solid #e5e5e5;
    vertical-align: top;
}

.info-table td:first-child {
    width: 160px;
}

/* Kỹ năng */
.skill-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
}

.skill-table td {
    padding: 7px 0;
    border-bottom: 1px solid #e5e5e5;
    vertical-align: top;
    line-height: 1.45;
}

.skill-name {
    width: 160px;
    font-weight: 400;
}

.skill-description {
    padding-left: 2px;
}

/* Sở thích */
.hobby {
    font-size: 14px;
    line-height: 1.7;
}

/* Hoạt động */
.activity {
    display: grid;
    grid-template-columns: 160px 1fr;
    column-gap: 5px;
    font-size: 14px;
}

.activity-date {
    line-height: 1.5;
}

.activity-content {
    line-height: 1.6;
}

.activity-title {
    font-weight: 700;
    text-transform: uppercase;
}

.activity-item {
    margin-top: 2px;
}

/* Footer */
.cv-footer {
    text-align: right;
    color: #777777;
    font-size: 12px;
    margin-top: 15px;
}

/* Responsive */
@media (max-width: 700px) {

    .cv-container {
        width: 100%;
        max-width: 100%;
        padding: 25px 18px;
        margin: 0;
        box-shadow: none;
    }

    .header {
        gap: 15px;
    }

    .avatar-box {
        width: 105px;
        min-width: 105px;
        height: 145px;
    }

    .name {
        font-size: 23px;
    }

    .position {
        font-size: 14px;
    }

    .info-row {
        font-size: 12px;
    }

    .info-label {
        width: 70px;
    }

    .timeline,
    .activity {
        grid-template-columns: 115px 1fr;
    }

    .info-table td:first-child,
    .skill-name {
        width: 115px;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# ẢNH CÁ NHÂN
# ============================================================
# Đặt ảnh cá nhân cùng thư mục với app.py
# Đổi tên ảnh thành: avatar.jpg
avatar_path = "avatar.jpg"
avatar_base64 = get_image_base64(avatar_path)

if avatar_base64:
    avatar_html = f"""
    <div class="avatar-box">
        <img class="avatar"
             src="data:image/jpeg;base64,{avatar_base64}">
    </div>
    """
else:
    avatar_html = """
    <div class="avatar-box"
         style="display:flex;align-items:center;justify-content:center;">
        <span style="font-size:13px;color:#777;text-align:center;">
            Thêm ảnh<br>avatar.jpg
        </span>
    </div>
    """


# ============================================================
# CV
# ============================================================
st.markdown(f"""

<div class="cv-container">

    <!-- ================= HEADER ================= -->
    <div class="header">

        {avatar_html}

        <div class="personal-info">

            <div class="name">
                Đặng Phú Hưng
            </div>

            <div class="position">
                SINH VIÊN NĂM 3 NGÀNH TÀI CHÍNH NGÂN HÀNG
            </div>

            <div class="info-row">
                <span class="info-label">Ngày sinh:</span>
                05/07/2005
            </div>

            <div class="info-row">
                <span class="info-label">Giới tính:</span>
                Nam
            </div>

            <div class="info-row">
                <span class="info-label">Số điện thoại:</span>
                0909116235
            </div>

            <div class="info-row">
                <span class="info-label">Email:</span>
                phuhung5705@gmail.com
            </div>

            <div class="info-row">
                <span class="info-label">Website:</span>
                https://www.facebook.com/profile_status/
            </div>

            <div class="info-row">
                <span class="info-label">Địa chỉ:</span>
                80/21 Tô Vĩnh Diện, Khu phố Tân Hòa,
                Phường Đông Hòa, Thành phố Hồ Chí Minh
            </div>

        </div>

    </div>


    <!-- ================= MỤC TIÊU ================= -->
    <div class="section">

        <div class="section-title">
            MỤC TIÊU NGHỀ NGHIỆP
        </div>

        <div class="text">
            Áp dụng kiến thức chuyên ngành Tài chính – Ngân hàng cùng
            kỹ năng Word, Excel và phân tích dữ liệu để hỗ trợ hiệu quả
            các nghiệp vụ ngân hàng. Không ngừng học hỏi quy trình
            nghiệp vụ, nâng cao kỹ năng chuyên môn và hướng tới trở
            thành nhân sự ngân hàng chuyên nghiệp, có giá trị lâu dài
            cho tổ chức.
        </div>

    </div>


    <!-- ================= HỌC VẤN ================= -->
    <div class="section">

        <div class="section-title">
            HỌC VẤN
        </div>

        <div class="timeline">

            <div class="date">
                19/2023 - nay
            </div>

            <div class="content">

                <div class="school">
                    Trường Đại học Nguyễn Tất Thành
                </div>

                <div class="degree">
                    Chuyên ngành Tài chính ngân hàng
                </div>

                <div class="bullet">
                    • Xếp loại: Khá
                </div>

                <div class="bullet">
                    • Chứng chỉ: Kỹ năng Hành chính văn phòng,
                    Kỹ năng làm chủ công việc
                </div>

            </div>

        </div>

    </div>


    <!-- ================= CHỨNG CHỈ ================= -->
    <div class="section">

        <div class="section-title">
            CHỨNG CHỈ
        </div>

        <table class="info-table">

            <tr>
                <td>2025</td>
                <td>KỸ NĂNG HÀNH CHÍNH VĂN PHÒNG</td>
            </tr>

            <tr>
                <td>2025</td>
                <td>KỸ NĂNG LÀM CHỦ CÔNG VIỆC</td>
            </tr>

        </table>

    </div>


    <!-- ================= KỸ NĂNG ================= -->
    <div class="section">

        <div class="section-title">
            KỸ NĂNG
        </div>

        <table class="skill-table">

            <tr>
                <td class="skill-name">
                    SOẠN THẢO VĂN BẢN
                </td>

                <td class="skill-description">
                    Kỹ năng soạn thảo văn bản hành chính và học thuật<br>
                    Thành thạo Microsoft Word, trình bày văn bản chuyên nghiệp<br>
                    Kỹ năng viết và chỉnh sửa báo cáo
                </td>
            </tr>

            <tr>
                <td class="skill-name">
                    KỸ NĂNG BÀN PHÍM
                </td>

                <td class="skill-description">
                    Kỹ năng bàn phím tốt, gõ nhanh và chính xác,
                    sử dụng thành thạo phím tắt trong Word và Excel
                </td>
            </tr>

            <tr>
                <td class="skill-name">
                    GIẢI QUYẾT VẤN ĐỀ
                </td>

                <td class="skill-description">
                    Phân tích tình huống, xác định nguyên nhân,
                    đề xuất và lựa chọn giải pháp phù hợp.
                </td>
            </tr>

            <tr>
                <td class="skill-name">
                    QUẢN LÍ THỜI GIAN
                </td>

                <td class="skill-description">
                    Sắp xếp công việc theo mức độ ưu tiên,
                    đảm bảo hoàn thành đúng hạn, cân bằng học tập
                    và công việc.
                </td>
            </tr>

        </table>

    </div>


    <!-- ================= SỞ THÍCH ================= -->
    <div class="section">

        <div class="section-title">
            SỞ THÍCH
        </div>

        <div class="hobby">
            Đọc sách<br>
            Nghe podcast học tập<br>
            Tham gia hoạt động học thuật<br>
            Tự học kỹ năng mềm
        </div>

    </div>


    <!-- ================= HOẠT ĐỘNG ================= -->
    <div class="section">

        <div class="section-title">
            HOẠT ĐỘNG
        </div>


        <div class="activity">

            <div class="activity-date">
                11/5/2024 -<br>
                23/12/2024
            </div>

            <div class="activity-content">

                <div class="activity-title">
                    TRƯỜNG ĐẠI HỌC NGUYỄN TẤT THÀNH
                </div>

                <div class="activity-title">
                    SINH VIÊN THAM GIA
                </div>

                <div class="activity-item">
                    Tham gia UNITOUR nhà lãnh đạo tương lai
                    và giới thiệu cuộc thi ASEAN - CHINA - INDIA 2024
                </div>

                <div class="activity-item">
                    Tham gia Ngày hội tuyển dụng tháng 5 năm 2024
                </div>

                <div class="activity-item">
                    Tham gia Workshop Đầu tư chứng khoán
                    Bản lĩnh đầu tư & tự tin chiến thắng
                </div>

                <div class="activity-item">
                    Tham gia Chương trình Tìm hiểu tài nguyên
                    giáo dục mở cho Tân SV khoá 2024
                </div>

            </div>

        </div>


        <div class="activity" style="margin-top:18px;">

            <div class="activity-date">
                9/8/2025 -<br>
                5/10/2025
            </div>

            <div class="activity-content">

                <div class="activity-title">
                    TRƯỜNG ĐẠI HỌC NGUYỄN TẤT THÀNH
                </div>

                <div class="activity-title">
                    SINH VIÊN THAM GIA
                </div>

                <div class="activity-item">
                    Tham gia Hội thảo khoa học Quốc tế
                    Toán học và Ứng dụng năm 2025
                </div>

                <div class="activity-item">
                    Tham gia Hoạt động phục vụ cộng đồng cấp Khoa 2025 -
                    Hành trình tuổi trẻ vì cộng đồng 2025 -
                    Trung thu nghĩa tình 2025
                </div>

            </div>

        </div>

    </div>


    <!-- ================= FOOTER ================= -->
    <div class="cv-footer">
        © CV Đặng Phú Hưng
    </div>

</div>

""", unsafe_allow_html=True)
