# Bảng Task Team

Trang web một file để theo dõi task Jira và phân công người làm.

## Tính năng
- Bảng 4 cột: Cần làm · Đang làm · Chờ review · Xong (kéo thả hoặc bấm ‹ › để chuyển)
- Mỗi task có mã Jira (link sang Jira), tiêu đề, độ ưu tiên, hạn chót, người nhận, ghi chú
- Giao việc ngay trên thẻ bằng ô chọn người
- Thanh khối lượng việc theo từng người (số task mở, số task trễ), bấm để lọc
- Lọc theo độ ưu tiên, quá hạn, sắp đến hạn; tìm theo mã hoặc tiêu đề

## Chạy
Mở `index.html` bằng trình duyệt, hoặc bật GitHub Pages:
Settings → Pages → Source: *Deploy from a branch* → Branch `main` / `root`.

## Lưu ý về dữ liệu
Bản GitHub Pages lưu dữ liệu trong trình duyệt (localStorage) của từng người,
nên mỗi người thấy bảng riêng. Muốn cả team dùng chung một bảng thì cần thêm
backend (VD: Firebase/Supabase) hoặc gọi Jira API qua một proxy server.
