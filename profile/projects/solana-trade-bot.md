# Solana Trade Bot

Ghi chú định hướng cho các phiên làm việc về `solana-trade-bot` (dự án cá nhân của Thịnh) và
scanner đi kèm. Tóm tắt ngày 2026-11-17 từ `openspec/MASTER_PLAN.md` của repo và các thread
paper test. Source of truth là repo; không lưu API key, private key, ví hay dữ liệu giao dịch
vào file này.

## Vai trò

- **`solana-token`** (scanner): dự án của một client, Thịnh làm. Python/FastAPI, quét token
  Solana qua Birdeye, phân tích ví qua Helius, gắn nhãn RED/CAUTION/GREEN. Dùng làm service
  cho bot; Thịnh được phép dùng key Helius/Birdeye của client cho việc này.
- **`solana-trade-bot`**: bot đầu tư memecoin cá nhân. Đọc nhãn từ DB scanner (chỉ đọc), cho
  Claude đánh giá tín hiệu, ghi lệnh vào các ví paper, báo qua Telegram. Python 3.13, uv,
  SQLAlchemy async, Alembic, httpx — cùng stack với scanner. Chạy trên Mac của Thịnh, sau
  chuyển VPS.

## Roadmap (chốt 2026-11-17)

1. Bot nháp + paper test đợt 2 (sau khi Helius reset ~26/11): các ví `RULE`, `RULE_PB`,
   `AI_FULL`, `AI_VETO`, mỗi ví $500, $100/lệnh, scan mỗi giờ.
2. Tổng kết đợt 2 → rule và playbook mới, Thịnh duyệt.
3. Tiền thật với vốn nhỏ: Thịnh xác nhận từng lệnh qua Telegram, AI chỉ đưa CHO QUA/CHẶN.
4. Tự động: AI chỉ lọc (CHO QUA/CHẶN), bot vào/thoát lệnh theo rule Thịnh đã duyệt.

## Ranh giới cố định

- Với tiền thật, Claude không quyết định mua bán và không kích hoạt lệnh; chỉ được chặn.
  Paper thì AI được quyết toàn bộ.
- AI tham gia qua `claude -p` chạy nền (gói Claude của Thịnh, không dùng Claude API key),
  không có công cụ, đọc bản tóm tắt gồm playbook đóng băng + snapshot token.
- Playbook đóng băng trong mỗi đợt test; bài học mới chỉ cập nhật giữa các đợt.

## Quy ước khi làm việc

- Đọc `AGENTS.md` và `openspec/MASTER_PLAN.md` của repo trước khi làm. Mỗi Task có OpenSpec
  change (tiếng Việt) được Thịnh duyệt trước khi code.
- Làm ở vị trí senior Python: thiết kế cấu trúc rõ lớp, hàm dùng chung tái sử dụng được,
  không duplicate code.
- Số liệu báo cáo (số dư, tỉ lệ thắng, lợi thế AI) phải tính lại từ DB/CSV bằng script, ghi
  nguồn, không cộng dồn từ tóm tắt cũ.
- Ưu tiên an toàn vốn: nguyên tắc "thà bỏ lỡ còn hơn dính lỗ".
