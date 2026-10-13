# Skill/plugin catalog — DRAFT

Được chấp thuận đưa vào plan, chưa cài/đổi cấu hình. Skills hướng dẫn quy trình; MCP/plugin cung cấp công cụ. Tồn tại trên đĩa không chứng minh đã được app nạp.

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
| NestJS best practices | Nhóm backend ưu tiên, tận dụng bản đã có; chỉ đọc rule phù hợp, spec/convention repo thắng |

Nguồn tham khảo: github.com/vercel-labs/agent-skills; github.com/expo/skills; github.com/Fission-AI/OpenSpec; developers.figma.com/docs/figma-mcp-server/remote-server-installation/; github.com/anthropics/claude-code/tree/main/plugins/frontend-design.

Trước vendoring: đọc toàn bộ file liên quan, kiểm tra script/network/chi phí, xác định commit và LICENSE; lưu checksum, patch địa phương và trigger. Không dùng ngày/commit trong PDF như xác nhận phiên bản thực tế đã cài. Không cài CLI tạo branch/PR hoặc tự động commit trái rules.

## Nhóm backend/NestJS bổ sung — DRAFT

Được yêu cầu bổ sung ngày 2026-10-01; chưa cài và chưa tạo SKILL.md. Skills chung tầng user, chỉ bật theo task backend. Các tên custom bên dưới là thiết kế đề xuất, không phải package đã tìm thấy.

| Skill | Nội dung và điều kiện |
| --- | --- |
| `nestjs-best-practices` (đã có) | Module/provider/DI, lỗi, validation, hiệu năng. Bản local metadata 1.2.0, MIT, author Kadajett. Cần audit references/source trước ghim; không áp cứng feature-module, repository pattern hay JWT nếu repo khác convention. |
| `backend-api-contract` (custom) | Làm rõ input/output, validation, lỗi, pagination, quyền truy cập và compatibility với FE trước code; theo transport/contract dự án, không tự thêm REST/versioning. |
| `backend-data-integrity` (custom) | Schema/query, transaction, migration, idempotency/concurrency và phân tách dữ liệu khi liên quan; đọc ORM/DB hiện có, không chọn công nghệ thay Thịnh. |
| `backend-security-review` (custom) | Review auth/authz, kiểm tra quyền theo tài nguyên, input, secret/log nhạy cảm và dependency bên ngoài theo scope; không tự chọn JWT hoặc thêm thư viện auth. |
| `backend-testing-and-debugging` (custom) | Trace request → controller/service → DB/tool, chọn unit/integration/e2e tối thiểu theo rủi ro; kiểm tra contract, quyền và tính toàn vẹn khi đổi hành vi. Không baseline/bộ test rộng mặc định. |
| Prisma official skills (có điều kiện) | Chỉ chọn skill Prisma Client/CLI phù hợp nếu dự án xác nhận dùng Prisma; chưa chọn managed Prisma service, không cài toàn bộ registry. |

Học backend: áp dụng cách giải thích trong profile, không tạo một skill dài lặp profile. Có thể gộp các custom skill khi audit thấy trigger trùng; không nạp cả nhóm mỗi task.

Nguồn NestJS/Prisma: https://github.com/Kadajett/agent-nestjs-skills ; https://docs.nestjs.com/fundamentals/testing ; https://docs.nestjs.com/security/authentication ; https://www.prisma.io/docs/ai/tools/skills . Dùng để xây/audit, không giả là các package custom đã tồn tại.

## Nhóm Python/FastAPI — 2026-10-01

Duyệt hướng custom only (không vendor pack FastAPI/DDD). Skill user-level, bật khi repo là Python; không thay `my-backend-review` (NestJS).

| Skill | Nội dung và điều kiện |
| --- | --- |
| `my-python-backend` (custom, đã thêm nguồn) | FastAPI router mỏng, service độc lập HTTP, client `httpx`, SQLAlchemy 2 async, Alembic, pytest mock HTTP, `uv`/`ruff`. Đọc convention/OpenSpec repo trước. Không áp DDD, repository hierarchy, JWT, queue hay đổi package manager. |
