# Implementation plan — DRAFT

Không ước lượng thời gian. Phụ thuộc theo thứ tự. Thịnh duyệt spec/plan trước triển khai; từng hành động Git/global config có quyền riêng.

## P0 — Chốt bản nháp (hiện tại)

Profile/core/workflows/catalog/inventory/spec/plan được soạn. Thịnh xem hiểu đúng chưa. Không bắt duyệt lại từng câu interview. Chỉ hỏi khi mâu thuẫn ảnh hưởng thiết kế.

## P1 — Xác minh adapter và source

Đối chiếu tài liệu chính thức từng surface, phiên bản đang chạy và cơ chế load thực tế; đọc Cursor User Rules với quyền phù hợp, metadata Codex effective, Claude Desktop/ChatGPT. Kiểm chứng nơi Figma được đăng ký. Audit selected skills + LICENSE/references/patches, quyết định React version. Bổ sung audit NestJS đã có và thiết kế các skill API contract, data integrity, security review, testing/debugging; chỉ chọn Prisma khi stack được xác nhận. Output: compatibility matrix và SOURCES/manifest có dữ liệu xác minh, không invent commit.

## P2 — Hoàn thiện nội dung canonical

Chốt core và routing index, chia workflow/skill entry đúng trigger; tách references để nạp theo nhu cầu. Source user confirmed vs source legacy rõ. Đo core/token và rà trùng/mâu thuẫn. Không copy toàn bộ installed skills/plugins vào repo.

## P3 — Installer/adapter trên Mac cá nhân

Triển khai `bin/context` với status/install/update/uninstall/rollback, preview mặc định và explicit apply; manifest source ghim + machine state riêng. Làm dry-run/backup/ownership/update/conflict/rollback/uninstall và test fixtures cần thiết. Plugin/MCP dùng cơ chế chính thức, manual/OAuth khi cần; không xây tool/MCP quản lý riêng ở bản đầu. Cập nhật README với lệnh thực tế và walkthrough đã kiểm chứng. Trình thay đổi config cụ thể cho Thịnh duyệt. Kết nối từng surface tuần tự: Claude Code → Cursor → Codex → chat/desktop khác. Không giả định adapter CLI hoạt động ở app.

## P4 — Pilot hành vi

Task nhỏ đại diện: research chưa implement, feature convention, Figma + design system, Expo + platform check, yêu cầu Git thiếu/đủ. Kiểm chứng skill load/context version bằng evidence app và hành vi; không chỉ hỏi AI có hiểu không. Báo giới hạn và core thực nạp; sửa lệch rồi chốt release nội dung.

## P5 — Đồng bộ và máy công ty

Commit/push khi được yêu cầu. Chọn cơ chế sync nhẹ sau pilot. Kiểm kê máy công ty chỉ khi truy cập được; không remote đoán. Thiết lập path riêng, giữ cấu hình công ty, kết nối Claude và Copilot VS Code, thử cùng acceptance. Chat surfaces manual nếu không có hỗ trợ sync phù hợp.

## P6 — Bảo trì

Đề xuất bộ nhớ có giá trị; duyệt → lưu → commit/push có yêu cầu → đồng bộ. Khi project mới: kiểm tra stack/skill, đề xuất thiếu trước khi bắt đầu. Update dependency/plugin qua repo canonical: AI đề xuất/audit, Thịnh duyệt nguồn/version/patch, script preview rồi apply có quyền. Không sửa độc lập bản cài mỗi máy, không dùng update script để tự nâng upstream hoặc commit/push. Update có source pin, diff và Thịnh duyệt. Không nhắc bài học hay upgrade mỗi phiên.

## Các quyết định kỹ thuật còn mở (để P1 giải quyết bằng chứng)

- Adapter khả dụng và mức tự động cho từng chat surface.
- Nơi cài skills được từng tool thực đọc; dùng shared path/symlink/copy tùy compatibility và rollback.
- React version sau audit toàn bộ reference tree.
- Cơ chế sync, tokenizer và metric pilot.
