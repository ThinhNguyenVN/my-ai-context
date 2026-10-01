# Specification — DRAFT — 2026-10-01

## Mục tiêu

AI hiểu Thịnh và cộng tác nhất quán giữa máy cá nhân/công ty, giảm nhắc lại/làm sai/token lãng phí. Không hứa cùng account tự nạp repo. Cốt lõi độc lập công cụ; adapter theo từng surface.

## Phạm vi

Profile/rules/workflows/skill catalog, quản lý source/patch/version, installer cập nhật/gỡ/rollback, đồng bộ nội dung đã duyệt, kiểm chứng hành vi. Hỗ trợ Claude Code, Cursor, Codex desktop, Claude Desktop/Cowork, ChatGPT web/app, Copilot VS Code. Chat surface và code agent là adapter khác nhau; OpenCode có thể mở rộng sau, chưa bắt buộc bản đầu.

Không sao chép code/spec/dữ liệu nội bộ hay trạng thái milestone project. Cho phép mô tả khái quát repo công ty đã xác nhận. Không triển khai/cài ở giai đoạn draft, không commit/push tự động. Backend mục tiêu NestJS: catalog hỗ trợ API contract, data integrity, security và testing/debugging, nạp theo task. Không áp generic architecture/auth/ORM trái convention và spec dự án.

## Nạp context và token

Core ngắn + danh mục; profile/workflow/references đọc theo task. Không import toàn bộ tài liệu lúc startup. Ngân sách core tạm mục tiêu <=700 tokens theo tokenizer công cụ thực tế; danh mục ngắn tách biệt. Đo trước/sau, không dùng số dòng làm bằng chứng token. Đây là đề xuất kỹ thuật cần duyệt, không phải giới hạn Thịnh đã đặt.

Skill metadata trigger rõ, không luôn bật mọi skill. Một rule một nguồn canonical; adapter tránh chép lặp core và skill cùng lúc. Nạp lỗi phải báo, không im lặng coi đã tích hợp.

## Adapter

Mỗi adapter ghi tên surface/version, nơi cài, cấp áp dụng, load mode (tự động/thủ công), quyền filesystem, bước kiểm chứng và hạn chế. Ưu tiên mechanism chính thức. Không đồng nhất desktop app/chat với code CLI. Chat không đọc filesystem thì dùng instruction ngắn và tài liệu qua cơ chế hỗ trợ; đánh dấu manual nếu chưa tự đồng bộ được. Không cài MCP chỉ để có nhiều công cụ nếu không cần.

## Cài đặt và phiên bản

Đường dẫn workspace ánh xạ theo máy. Preview/dry-run trước đổi cấu hình; backup, manifest ownership/checksum, không đè phần người dùng quản lý. Rerun an toàn; phát hiện local edits/conflicts. Chỉ update file được quản lý, rollback/gỡ trả lại cấu hình cũ. Dependency/source pin commit + license + patch log; không tự nâng lên latest. Secret/OAuth state không nằm trong repo.

## Đồng bộ

Duyệt profile/rule mới cho phép lưu, chưa cho phép Git. Commit/push cần yêu cầu. Đồng bộ tự động chỉ bản đã push và đã duyệt; không auto-merge khi local có sửa. Đổi global config cần cho phép riêng. Dùng last-known-good khi offline/lỗi; báo khi actionable, không status spam. Cơ chế lịch/hook chọn sau khi kiểm chứng nhu cầu, chưa tạo automation.

## Acceptance

- Mỗi surface có trạng thái verified/manual/unavailable, không quảng cáo coverage chưa thử.
- Phiên mới nhận core đúng version và truy xuất đúng tài liệu cần; đo phần core thực nạp.
- Câu hỏi phân tích không tạo code; làm đi thực hiện scope chốt; không branch/commit/push/PR khi chưa rõ quyền.
- Feature theo workflow/convention; Figma đọc context trước và không giả vờ khi mất kết nối.
- Test chọn platform/rủi ro, không chạy rộng mặc định. Expo chỉ kích hoạt đúng stack.
- Đổi máy nhận cùng bản đã push; offline không mất last-known-good; local edit không bị ghi đè.
- Installer dry-run/idempotency/update/conflict/rollback/gỡ hoạt động với fixtures, không test trực tiếp gây phá cấu hình thật.

Đánh giá sau pilot: hỏi/phản biện đúng lúc, requirement/convention đúng hơn, ít token/vòng sửa, nhất quán giữa AI/máy. Đo task tương đương khi khả thi; không hứa token luôn giảm vì context chung cũng có chi phí.

## Bộ quản lý skill/plugin — bổ sung đã thống nhất

AI lựa chọn/audit, script triển khai; bản đầu không xây MCP hay GUI quản lý riêng. Repo là nguồn canonical cho skill được quản lý, gồm bộ cá nhân + core instruction; không chỉ một skill duy nhất kích hoạt tùy ý.

Entry `bin/context` tránh xung đột thư mục `context/`. Lệnh status chỉ đọc; install/update/uninstall/rollback preview mặc định, apply explicit. Update áp dụng bản đã ghim trong repo, không đồng nghĩa nâng source upstream hay đồng bộ Git. Dry-run không chạy lệnh có side effect, không download/execute source mới bất ngờ.

Manifest quản lý skill ID/source/version hoặc commit/checksum/license/patch và adapter/trigger; machine state/backup/đăng nhập để ngoài repo. Target path theo máy/công cụ. Chỉ tiếp nhận file ngoài quản lý khi có duyệt, không tự ghi đè. Plugin dùng vendor installer/CLI đã kiểm chứng; không ghim được version phải báo. Manual/OAuth là bước riêng, không giả completed.

README phải đủ cho AI khác thực hiện: quyền, checkout, audit, source pin, preview, apply, verification, Git/sync và rollback. Sau triển khai, command docs khớp script thực tế. Kiểm tra parser/help, dry-run không mutation, apply chỉ owned paths, drift/conflict, update không tự nâng upstream, rollback và idempotency qua fixtures.
