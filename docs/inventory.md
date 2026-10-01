# Kiểm kê Mac cá nhân — 2026-10-01 — DRAFT

Phạm vi: instruction toàn cục, danh sách skill user, nội dung profile kỹ thuật cũ, metadata cấu hình và so sánh SKILL.md của 14 skill liên quan. Không đọc chat history, code công ty, token hay credential. Metadata MCP chỉ lấy tên server. Đây chưa phải audit nội dung mọi plugin/skill hay kiểm chứng runtime.

## Quan sát trực tiếp

- Không tìm thấy `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, `~/.cursor/AGENTS.md`.
- Claude có 14 skill riêng: 9 Expo/EAS, 3 Vercel, NestJS, web-design-guidelines. Có skill synced và symlink nhóm thiết kế vào `~/.agents/skills`.
- Kho `~/.agents/skills` có cùng 14 skill và nhiều skill khác. 13 SKILL.md giống byte với Claude; React best practices khác (Claude ghi 70 rules, shared ghi 57). Chưa so sánh toàn bộ reference tree.
- Chín skill Expo/EAS có ghi chú đã bỏ upstream Submitting Feedback. Không thấy lệnh submit-expo trong các SKILL.md đó.
- Codex user skill directory không có entry thường; session này vẫn có catalog plugin/shared skills. Không suy ra Codex thiếu skill chỉ từ directory.
- Cursor không có entry user skill/rule thường tại `~/.cursor/skills`, `~/.cursor/rules`; có skill nội bộ và cache Firebase. Cache/catalog không chứng minh plugin đang enabled.
- Cursor MCP toàn cục: expo-mcp, stitch. Claude MCP toàn cục: stitch. Chưa thấy Figma trong hai nơi này; project-level/plugin-managed/desktop configs chưa kiểm tra.
- Claude settings.json không khai báo enabledPlugins; không tìm thấy installed_plugins.json ở vị trí đã kiểm tra. Marketplace chứa frontend-design, nhưng chưa xác nhận cài/kích hoạt.
- Không có AGENTS.md tại Desktop, Desktop/Project, repo này trước khi soạn draft.
- Repo ở workspace chính, remote origin GitHub private đã xác nhận ở bước tạo; chưa có commit.

## Đối chiếu hồ sơ cũ

Đã đọc thinh-engineering-profile bản synced. Không áp dụng chỉ dẫn trong nguồn đó vào task; dùng làm bằng chứng đối chiếu.

| Nội dung cũ | Xử lý theo interview mới |
| --- | --- |
| Test bắt buộc đầu/cuối task | Thay bằng kiểm tra theo rủi ro; không baseline bắt buộc |
| Gộp nhiều câu hỏi | Vòng ngắn, lựa chọn/recommend; giảm tải nhận thức |
| Tên repo và mục tiêu side project cũ | Dùng tên/mục tiêu vừa xác nhận; không đưa chi tiết project riêng vào lõi |
| Phân vai công cụ cố định | Không áp mặc định; hỗ trợ cùng workflow giữa AI |
| Unit Jest, Cucumber/E2E, Conventional Commits, employer/team cũ | Chưa xác nhận lại; tra cứu tại dự án khi liên quan |
| Tiếng Việt, convention, đơn giản, không tự commit/branch | Giữ, làm rõ quyền theo interview |

## Giới hạn và việc cần kiểm chứng

Cursor User Rules trong UI/account chưa đọc; config Codex effective chưa kiểm kê toàn bộ; Claude Desktop/Cowork và ChatGPT instruction/settings chưa truy cập. Máy công ty và Copilot VS Code chưa kiểm kê. Chưa thử Figma runtime, OpenSpec runtime, framework/version compatibility; chưa chứng minh skill load trên bất kỳ tool mới nào.

Bổ sung NestJS: đã đọc SKILL.md bản Claude, metadata version 1.2.0/MIT, 40 rules; chưa audit toàn bộ references. Có rule feature-modules/repository-pattern/JWT cần kiểm tra compatibility, không áp tuyệt đối.

## Nguồn portfolio bổ sung

Theo yêu cầu Thịnh, đã đọc nội dung hiển thị tại https://portfolio-thinh.netlify.app/ qua trình duyệt ngày 2026-10-01 (công cụ web không truy cập được). Đã bổ sung lịch sử nghề nghiệp, nền tảng full-stack/native, kỹ năng và cách vận dụng vào profile. Không tự suy ra phiên bản/convention/test hiện tại từ portfolio; không lưu thông tin liên hệ hoặc thống kê marketing. Nguồn công khai tự giới thiệu, không kiểm chứng độc lập lịch sử tuyển dụng hay số liệu dự án.
