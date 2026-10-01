# my-ai-context

Bộ nhớ và cách làm việc của Thịnh dành cho AI: profile, rules, workflows và skills.

## Dùng thế nào?

Mở project đang làm và nói chuyện với AI bình thường. Không cần mở repo này mỗi lần.

Có thể yêu cầu trực tiếp:

- **Làm feature:** “Dùng my-feature-workflow, hỏi để rõ requirement trước khi code.”
- **Thêm skill:** “Project này dùng Python. Đề xuất skill phù hợp và quản lý qua my-ai-context.”
- **Update profile:** “Cập nhật cách làm việc này vào my-ai-context, cho mình xem trước khi áp dụng.”

Bạn duyệt nội dung → AI sửa repo này → áp dụng vào các công cụ trên máy.

## Hai lệnh cần dùng trên Mac này

Copy **cả dòng**, chạy trong Terminal ở thư mục nào cũng được.

**Xem trạng thái:**

```bash
python3 /Users/thinhnguyen/Desktop/Project/my-ai-context/bin/context status
```

**Áp dụng những thay đổi đã duyệt trong repo:**

```bash
python3 /Users/thinhnguyen/Desktop/Project/my-ai-context/bin/context update --apply
```

Bạn cũng có thể nhờ AI chạy giúp. Lệnh update không tự tải skill mới từ Internet.

## Đã dùng được ở đâu?

Codex đã nhận rules và thấy 8 skill cá nhân. Claude đã được cài file; Cursor/Copilot dùng kho skill chung, còn cần thiết lập rules và kiểm chứng. ChatGPT/Claude ở chế độ chat và plugin Figma cần kết nối riêng.

Trên máy mới, lấy repo vào workspace chính rồi nhờ AI cài cho các công cụ bạn dùng. Cùng account chưa tự đồng bộ toàn bộ file.

Chi tiết dành cho AI: [bảo trì](docs/maintenance.md) · [cài từng công cụ](adapters/README.md) · [trạng thái triển khai](docs/implementation-status.md).
