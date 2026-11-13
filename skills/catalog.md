# Skill/plugin catalog — DRAFT

Skill my-* trong manifest được cài qua bin/context; skill bên thứ ba ghi cách cài riêng. Skills hướng dẫn quy trình; MCP/plugin cung cấp công cụ. Tồn tại trên đĩa không chứng minh đã được app nạp.

| Nhóm | Quyết định |
| --- | --- |
| Interview requirement, research, feature, kiểm chứng platform | Viết riêng từ workflow đã chốt; entry ngắn, chi tiết đọc theo nhu cầu |
| `my-code-review` (custom, đã thêm nguồn) | Chỉ khi được nhờ review diff/PR/implementation. Soi thay đổi, caller dùng chung, và feature/logic cũ bị ảnh hưởng; bug cũ không liên quan để ngoài scope. Mở đầu bằng tóm tắt PR, nêu điểm làm tốt có căn cứ, rồi Critical/High/Medium/Low kèm vị trí, tác động và fix; đánh giá PR feedback trước khi sửa code hoặc resolve và báo user trước; không sửa code nếu chỉ được yêu cầu review; không chạy unit/e2e hay test suite khi chưa được yêu cầu. Không bắt buộc plan/spec cho mọi review. |
| `my-code-conventions` (custom, đã thêm nguồn) | Khi đang viết hoặc sửa code, không phải workflow review hay cổng duyệt plan. Trước khi sửa logic/component/nhánh dùng chung, tìm caller và giữ behavior cũ nếu request không đổi. Convention theo repo; performance khi có tác động cụ thể; reuse trước khi tạo function/component; chỉ chuyển sang generic khi reuse vượt domain; unit test cho tính toán phức tạp, e2e khi cần. Hive UI/design tokens cho project PropertyGuru đã dùng Hive, cả web và mobile. |
| Figma plugin/MCP chính thức | Ưu tiên kiểm chứng kết nối, tích hợp Claude Code/Cursor và công cụ khác theo tài liệu |
| Vercel React/Next.js và React Native | Tận dụng bản đang có, chọn phiên bản ghim sau khi audit nguồn/compatibility |
| Composition patterns, web-design-guidelines | Gọi khi thiết kế component/review UI; giữ bản chỉnh sửa địa phương |
| Expo: native-ui, router, animation, data-fetching, upgrade, dev-client, module | User-level, chỉ Expo; giữ bỏ bước feedback gửi context ra ngoài |
| EAS update/app-stores | Có trong kho; chỉ dùng khi task yêu cầu, làm rõ chi phí và hành động phát hành |
| OpenSpec | Tích hợp dự án đã dùng; hỏi trước dự án chưa có |
| Frontend-design | Khám phá UI sản phẩm cá nhân; tránh trùng skill thiết kế hiện có và lệch Figma |
| Agent Reach (Panniantong, MIT) | Cho AI đọc/tìm web, YouTube, Reddit, Twitter... Chỉ đọc, không đăng. Cài trên Mac bằng prompt cho Claude Code: `Install Agent Reach: https://raw.githubusercontent.com/Panniantong/Agent-Reach/main/docs/install.md`. Skill do CLI tự cài/cập nhật (`agent-reach update`), không vendoring vào repo/plugin. Kênh cần login copy từ Chrome: dùng tài khoản phụ; key nhập trong terminal. Không cài gói PyPI `agent-reach`. |
| NestJS best practices | Nhóm backend ưu tiên, tận dụng bản đã có; chỉ đọc rule phù hợp, spec/convention repo thắng |
| UI/UX Pro Max (nextlevelbuilder/ui-ux-pro-max-skill) | Chọn visual direction (style, palette, font) khi kickoff project mới hoặc feature cần UI mới chưa có brand/kit; không dùng cho feature trong kit/design system có sẵn. Cài 2026-10-31 bằng `npx -y -p ui-ux-pro-max-cli uipro init --ai claude --global` (Thịnh tự chạy), không vendoring. Bộ 7 skill `ui-ux-pro-max`, `ui-styling`, `design`, `design-system`, `brand`, `banner-design`, `slides` đều khoá `disable-model-invocation: true`: AI không tự gọi, gặp điều kiện trên thì đề xuất Thịnh chạy `/ui-ux-pro-max`. Sau `uipro update --global` thêm lại dòng khoá. Cần Python 3. |

Nguồn tham khảo: github.com/vercel-labs/agent-skills; github.com/expo/skills; github.com/Fission-AI/OpenSpec; developers.figma.com/docs/figma-mcp-server/remote-server-installation/; github.com/anthropics/claude-code/tree/main/plugins/frontend-design.

Trước vendoring: đọc toàn bộ file liên quan, kiểm tra script/network/chi phí, xác định commit và LICENSE; lưu checksum, patch địa phương và trigger. Không dùng ngày/commit trong PDF như xác nhận phiên bản thực tế đã cài. Không cài CLI tự merge hoặc push thẳng nhánh mặc định trái rules.

## Nhóm backend/NestJS

Skill user-level, chỉ bật theo task backend NestJS.

| Skill | Nội dung và điều kiện |
| --- | --- |
| `nestjs-best-practices` (bên thứ ba) | Module/provider/DI, lỗi, validation, hiệu năng. Metadata 1.2.0, MIT, author Kadajett; chưa audit hết references. Không áp cứng feature-module, repository pattern hay JWT nếu repo khác convention. |
| `my-backend-review` (custom, đã thêm nguồn) | Gộp API contract, data integrity, security và testing/debugging (references api/data/security/testing). Theo convention repo, không tự chọn transport/ORM/auth. |
| Prisma official skills (có điều kiện) | Chỉ khi dự án dùng Prisma; không cài toàn bộ registry. |

Nguồn: https://github.com/Kadajett/agent-nestjs-skills ; https://docs.nestjs.com/fundamentals/testing ; https://docs.nestjs.com/security/authentication ; https://www.prisma.io/docs/ai/tools/skills .

## Nhóm Python/FastAPI — 2026-10-01

Duyệt hướng custom only (không vendor pack FastAPI/DDD). Skill user-level, bật khi repo là Python; không thay `my-backend-review` (NestJS).

| Skill | Nội dung và điều kiện |
| --- | --- |
| `my-python-backend` (custom, đã thêm nguồn) | FastAPI router mỏng, service độc lập HTTP, client `httpx`, SQLAlchemy 2 async, Alembic, pytest mock HTTP, `uv`/`ruff`. Đọc convention/OpenSpec repo trước. Không áp DDD, repository hierarchy, JWT, queue hay đổi package manager. |
