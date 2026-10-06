# Thu thập dữ liệu tuyển dụng TopCV tự động

Dự án tự động thu thập dữ liệu tin tuyển dụng CNTT từ TopCV bằng Python và Selenium, kết hợp Windows Task Scheduler để thiết lập lịch chạy tự động. Dữ liệu sau khi thu thập được xử lý và lưu thành các file CSV theo từng ngày, phục vụ cho việc theo dõi và phân tích dữ liệu tuyển dụng.

## Mục tiêu

- Thực hành thu thập dữ liệu từ website bằng Selenium.
- Tự động hóa quá trình thu thập dữ liệu theo lịch.
- Xử lý và lưu trữ dữ liệu bằng Pandas.
- Xây dựng quy trình thu thập dữ liệu có thể chạy định kỳ mà không cần thực hiện thủ công.

## Dữ liệu thu thập

Các thông tin được thu thập từ tin tuyển dụng gồm:

- ID công việc
- Tên công việc
- Tên công ty
- Mức lương
- Địa điểm
- Kinh nghiệm yêu cầu
- Thời gian đăng tuyển

## Công nghệ sử dụng

- **Python** – xây dựng chương trình thu thập dữ liệu
- **Selenium** – tự động truy cập và trích xuất dữ liệu từ TopCV
- **Pandas** – xử lý và lưu trữ dữ liệu
- **NumPy** – hỗ trợ xử lý dữ liệu
- **Windows Task Scheduler** – thiết lập lịch chạy tự động
- **CSV** – lưu trữ dữ liệu sau khi thu thập

## Quy trình hoạt động

```text
Windows Task Scheduler
        ↓
   run_crawl.bat
        ↓
   crawl_data.py
        ↓
      Selenium
        ↓
       TopCV
        ↓
  Thu thập dữ liệu
        ↓
      Pandas
        ↓
   Lưu file CSV