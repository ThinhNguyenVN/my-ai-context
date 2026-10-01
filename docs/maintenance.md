# Hướng dẫn cho AI bảo trì my-ai-context

Dùng primary checkout trên máy hiện tại, không tạo branch/worktree/clone phụ. Từ project khác vẫn có thể cập nhật repo này khi có quyền. Luôn đọc core và phần workflow liên quan, không nạp hết profile.

## Thêm/update

1. Làm rõ yêu cầu: sửa context, thêm skill, nâng upstream hay áp dụng cấu hình. Kiểm tra Git và trạng thái cài hiện tại.
2. Đối chiếu skill đã có; đề xuất nguồn/version, lợi ích, compatibility, chi phí/dữ liệu bên ngoài nếu có. Chờ duyệt phần chưa có quyền.
3. Sửa nguồn canonical. Local skills dùng ID my-*, SKILL.md name/description và manifest entry. Technical bundles ngoài manifest hiện chưa được installer quản lý; cần audit/import phù hợp trước, không giả là update đã hỗ trợ.
4. Nguồn bên thứ ba cần LICENSE, version/commit, checksum và patch log. Giữ chỉnh sửa Expo bỏ feedback. Không tự update latest hàng loạt.
5. Preview bằng python3 bin/context update --dry-run. Review file/path/conflict; không force/reset/stash hay sửa riêng bản cài.
6. Khi được phép, apply và kiểm tra status; xác minh nạp trong phiên mới. Chỉ test cần thiết.
7. Git commit/push/PR cần yêu cầu rõ, không suy ra từ duyệt nội dung. Không hỏi lại hành động đã được cho phép.

## Giới hạn và phục hồi

Installer quản lý local skills và core cho Claude/Codex; shared skills cho Cursor/Copilot. User core của Cursor/Copilot, chat apps, plugin/OAuth theo adapters/README.md. Không suy từ file tồn tại thành runtime verified.

Update không nâng upstream hay chạy Git. State/backups ở ~/.local/state/my-ai-context/state.json. Uninstall/rollback áp dụng toàn bộ managed state; rollback một transaction. Drift/unmanaged/symlink làm dừng, không force. Restore khi write lỗi đã được fixture test.

Sau chuyển repo chính, preview/update để refresh đường dẫn. Máy mới có path riêng. Đồng bộ source và áp dụng config là hai bước; không có auto-sync nền ở v0.1.0.

Khi sửa installer: python3 -m unittest discover -s tests -v. Fixture ở work/, không đụng global config. Khi chỉ sửa docs, không chạy bộ test theo nghi thức.

Entrypoint portable: context.sh ở gốc repo, tự tìm đường dẫn của chính script; có thể gọi từ cwd khác. README dùng lệnh tương đối trong checkout. Sau chuyển primary repo, preview/update để refresh đường dẫn đã render; không cần sửa path trong script.
