# my-ai-context

Profile, rules, workflows và skills cá nhân của Thịnh dành cho AI.

## 1. Cài trên máy mới

Mở Terminal tại workspace chính rồi chạy:

```bash
git clone https://github.com/ThinhNguyenVN/my-ai-context.git
cd my-ai-context
./my-install
```

Cần Python 3.9+ và tài khoản GitHub có quyền truy cập repo private. Nếu đã có repo trên máy, dùng bản đó thay vì clone thêm. Sau khi cài, mở phiên AI mới.

Mặc định chọn Claude Code, Codex, Cursor và Copilot. Chọn riêng nếu cần:

```bash
./my-install --targets claude,copilot
```

Bộ cài thêm skills; rules tự cài cho Claude Code/Codex. Cursor/Copilot còn bước rules riêng; ChatGPT/Claude chat và plugin/MCP có cách kết nối riêng: [hướng dẫn](adapters/README.md).

## 2. Thêm hoặc cập nhật skill

Prompt ngay trong project đang làm, không cần chuyển chat:

> Thêm skill Python phù hợp cho project này vào my-ai-context. Kiểm tra phần đã có và đề xuất trước khi cài.

> Kiểm tra skill NestJS có cần cập nhật không, so sánh và recommend cho mình.

AI kiểm tra → đề xuất → bạn duyệt → AI thêm/sửa nguồn skill và đăng ký trong bộ quản lý của repo. Sau đó chạy trong my-ai-context:

```bash
./my-update
```

Bạn có thể nhờ AI áp dụng luôn khi duyệt, không cần tự chạy. Skill cài trực tiếp ngoài repo chưa được đồng bộ; skill bên ngoài cần rà soát và tích hợp vào bộ quản lý trước.

**my-update áp dụng nội dung trong repo lên máy, không tự tải skill mới hay lấy bản repo từ GitHub.** Nó cài skill mới đã đăng ký và cập nhật skill đang có cho các công cụ đã chọn.

## 3. Đồng bộ sang máy khác

Trên máy vừa thêm/sửa skill: yêu cầu AI **commit và push** bản đã duyệt lên GitHub.

Trên máy khác đã cài lần đầu, vào repo rồi chạy:

```bash
git pull --ff-only
./my-update
```

Skill mới được cài, skill đã có được cập nhật. Điều kiện: nguồn skill và đăng ký bộ quản lý đã được push lên repo. Máy chưa cài thì làm bước 1. Plugin/MCP có đăng nhập hoặc cấu hình riêng có thể cần thêm bước.

Nếu Git báo lỗi hoặc đang có thay đổi cục bộ, nhờ AI kiểm tra trước; không force/reset. Chưa có đồng bộ nền tự động.

## Lệnh nhanh

Chạy trong thư mục my-ai-context:

```bash
./my-status     # Xem trạng thái
./my-install    # Cài lần đầu trên máy
./my-update     # Cài/cập nhật theo nội dung repo hiện tại
```

Chuyển folder repo: chạy my-update tại vị trí mới để cập nhật đường dẫn đã cài.
