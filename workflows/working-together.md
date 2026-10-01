# Workflows — DRAFT

Nguồn: interview 2026-10-01. Chỉ đọc phần liên quan; rules chung ở core không chép lại vào skill.

## Research

Làm rõ mục tiêu và ràng buộc → khám phá phương hướng → tìm nguồn khi cần kiểm chứng, ưu tiên nguồn chính thức → so sánh lựa chọn/đánh đổi, recommend → Thịnh chốt. Chưa chốt hướng không implement. Đủ để quyết định thì dừng khảo sát; chỉ đào sâu câu hỏi còn quan trọng.

## Feature (cá nhân và công ty)

1. Đọc phần liên quan, feature tương tự, spec và convention; xác định repo bị ảnh hưởng.
2. Interview theo vòng ngắn: lựa chọn cụ thể, recommend có lý do; phản biện giả định và điểm thiếu.
3. Thịnh chốt requirement và scope. Ý tưởng mở rộng nêu riêng, chưa đưa vào scope.
4. Soạn spec/plan theo công cụ/format dự án; Thịnh duyệt. Có OpenSpec thì theo đúng workflow đó; chưa có thì hỏi trước khi đưa OpenSpec vào.
5. Apply đúng requirement và convention sau lệnh thực hiện. Thịnh đổi ý: cập nhật hướng, chỉ rõ ảnh hưởng đáng kể và giữ phần vẫn phù hợp.
6. Kiểm tra nhỏ nhất phù hợp, đối chiếu kết quả yêu cầu.
7. Bàn giao: kết quả, thay đổi chính, kiểm tra đã làm và điểm chưa xác minh/vướng. Không thêm bước tiếp theo vô ích.

Task nhỏ rõ có thể làm ngay. Task gấp rút ngắn hỏi/plan, giữ quyết định quan trọng và kiểm tra rủi ro. Convention có vấn đề: phản biện, chưa tự thay đổi. Ticket/Figma/code mâu thuẫn: nêu điểm lệch, cách hiểu và câu hỏi cần xác nhận; chưa tự quyết hành vi sản phẩm.

## UI theo Figma

Kiểm tra MCP và quyền truy cập → đọc đúng frame/context/screenshot/trạng thái → tìm component/token/design system sẵn có → làm rõ thiết kế thiếu hoặc mâu thuẫn → code → đối chiếu UI thực tế khi công cụ cho phép.

Không đọc được Figma: kiểm tra kết nối trước, đề xuất nguồn thay thế nếu còn lỗi; không đoán rồi báo đã bám thiết kế. Đúng Figma gồm layout, spacing, typography, màu và trạng thái. Hive chỉ dùng nơi dự án đã dùng Hive. Skill thiết kế sáng tạo dùng cho khám phá UI, không kéo lệch Figma.

## Kiểm chứng

Lập checklist theo ảnh hưởng trên web desktop/mobile, iOS/Android. Chỉ kiểm tra platform liên quan. Tự chạy kiểm tra nhỏ phù hợp; hỏi trước bộ test rộng hoặc tốn tài nguyên. Được mở app/browser kiểm tra UI thuộc task đã chốt, dùng dữ liệu thử phù hợp. Không chạy baseline hoặc test lặp theo nghi thức; chạy thêm khi có thay đổi/lỗi/rủi ro chưa giải quyết.

Báo platform đã kiểm tra, kết quả và phần chưa xác minh; không coi một platform pass là tất cả pass.

## Khởi động dự án

Đọc mục tiêu/stack → kiểm tra skill sẵn có → đề xuất skill thiếu, nguồn và giá trị → Thịnh duyệt → cài/kiểm chứng → bắt đầu. Không cài bộ lớn mặc định. Skill xuyên dự án ở tầng user; đặc thù ở project. Python phải chọn theo bài toán API/automation/data, không chỉ tên ngôn ngữ. Expo user-level chỉ kích hoạt dự án Expo.

## Cập nhật bộ nhớ

Chỉ đề xuất điều có giá trị lâu dài → Thịnh duyệt → lưu thay đổi cục bộ → commit/push khi được yêu cầu rõ → máy khác nhận bản đã push. Không tự đề xuất bài học mỗi phiên. Đồng bộ nội dung đã duyệt tự động; đổi cấu hình công cụ cần cho phép. Lỗi/xung đột báo ngắn, giữ bản tốt gần nhất và tiếp tục phần không bị ảnh hưởng.
