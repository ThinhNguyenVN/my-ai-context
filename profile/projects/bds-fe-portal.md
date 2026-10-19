# BDS FE Portal

Ghi chú kiến trúc để hỗ trợ các phiên làm việc về repository `bds-fe-portal`.
Tóm tắt từ `AGENTS.md`, `README.md`, `docs/architecture.md` và Nx project
graph ngày 2026-10-02, kiểm chứng lại 2026-10-19. Đây là context định hướng, không thay thế tài liệu và
source of truth trong checkout dự án; luôn kiểm tra convention hiện hành khi
thực hiện task. Không lưu source code, credentials, API secret hay dữ liệu nội
bộ vào file này.

## Vai trò và stack

Monorepo frontend cho Batdongsan.com.vn, tổ chức bằng Nx và pnpm. Stack chính
là TypeScript/React, Expo/React Native cho mobile, Next.js cho web. Hive là
design system: các package UI dùng Hive React Native packages và
`@bds/design-tokens` cung cấp tokens cho native/web.

Đây là snapshot của workspace tại ngày trên, không phải cam kết version lâu
dài. Khi cần version chính xác, đọc `package.json` và lockfile.

## Ứng dụng

| Nx project | Vai trò | Render/runtime |
| --- | --- | --- |
| `@bds/mobile-app` | Một Expo app có consumer và seller modes | React Native trên iOS/Android |
| `@bds/seller-web` | Seller web | Next.js static export; page chạy ở browser |
| `@bds/consumer-web` | Consumer website, cần SEO | Next.js server rendering cho content và metadata |
| `@bds/relay-server` | Relay hỗ trợ local development | Chỉ chạy local, không deploy |

## Quan hệ với legacy repos

bds-fe-portal đang thay thế dần các repo legacy (`bds-mobile`,
`bds-seller-experience-sellernet-rtk`, `bds-seller-experience-sellernet-utils`).
Tới khi mọi team chuyển sang, legacy vẫn được cập nhật và bds-fe nhận thay đổi
qua các đợt sync định kỳ (`tools/legacy-sync/`, mỗi đợt là một OpenSpec
change). Xung đột được giải theo hướng giữ cải tiến của bds-fe và port behavior
legacy vào code đã chuyển sang `@bds/ui`/`@bds/pages`. Legacy seller web
(`bds-seller-sellernet`) là tham chiếu behavior/layout cho seller-web, không
copy stack.

## Package layers

- `@bds/design-tokens`: Hive tokens và CSS tokens cho web.
- `@bds/ui`: UI primitives/components dùng chung. Nhiều component dùng React
  Native primitives; có web implementation/entry khi khác biệt nền tảng.
- `@bds/ui-connected`: UI components đọc shared state theo id; không dùng
  Next.js trực tiếp.
- `@bds/ui-seo`: web-only helpers cho metadata, crawlable links, pagination và
  structured data. Bổ sung cho UI, không thay thế `@bds/ui`.
- `@bds/pages`: nội dung page dùng chung, nhận data/actions/slots từ app host.
- `@bds/state`: Redux slices, selectors, thunks và API DTO mappers; data
  sources được inject vào store/thunks.
- `@bds/rtk-sellernet`: Sellernet API client.
- `@bds/sellernet-utils`: helper/type cho seller domain.
- `@bds/utils`: helper cross-app nhỏ.

Dependency nền chính: `ui -> design-tokens`; `ui-connected -> ui, state`;
`ui-seo -> ui`; `state -> rtk-sellernet, sellernet-utils`;
`rtk-sellernet -> sellernet-utils`. `pages` dùng UI, tokens, state và các
helper web cần thiết. Các app import package theo nhu cầu; xem `pnpm nx graph`
để lấy graph hiện hành, vì direct dependencies có thể đổi.

Direct app dependencies theo Nx graph tại ngày kiểm chứng:

| App | Shared packages |
| --- | --- |
| `@bds/mobile-app` | pages, rtk-sellernet, state, ui, utils |
| `@bds/seller-web` | pages, ui-connected, rtk-sellernet, sellernet-utils, state, ui, design-tokens |
| `@bds/consumer-web` | pages, rtk-sellernet, state, ui, ui-seo, design-tokens, utils |
| `@bds/relay-server` | Không phụ thuộc package workspace nào trong Nx graph |

## Shared UI trên native và web

TypeScript/TSX mô tả React components; renderer và module resolution quyết
định giao diện nền tảng:

- Mobile/Metro chọn React Native export condition và implementation mặc định
  (`.tsx`); React Native render primitives thành native views.
- Next.js transpile workspace source (`transpilePackages`), ưu tiên
  `.web.tsx`, và alias `react-native` sang `react-native-web`. React Native Web
  chuyển API tương thích như `View`/`Image` thành DOM.
- `@bds/ui` có web entry riêng; `Text` web dùng semantic HTML. Một số server
  components import các entry server-safe như `@bds/ui/text`,
  `@bds/ui/layout`, `@bds/ui/condition-renderer`.
- Consumer pages có thể server-render qua web implementation. SSR vẫn cần
  content ổn định lúc render, semantic HTML và links có href; metadata,
  canonical và JSON-LD thuộc page/SEO layer. SSR không tự nó đảm bảo SEO.

## Pages và ownership

`@bds/pages` giữ page content, không giữ app shell. Page nhận data, callbacks
và slots qua props; app host giữ routing, store, navigation, platform hooks và
platform-only UI. Cùng page có thể được dùng bởi mobile và Next.js nếu phần
render dùng API phù hợp; dùng `.web.tsx` hoặc slot khi thực sự có khác biệt nền
tảng.

Page layout theo `PageContainer`: compact dưới Hive tablet breakpoint (750px),
wide từ breakpoint đó trở lên. Web đổi layout bằng CSS/style props, không đọc
viewport width trong render để chọn content. Mobile parent có thể cung cấp
native list/interactions; web list thường đi theo document flow và tải thêm
bằng action rõ ràng.

Ví dụ đã xác nhận: `SellerLeadsPage` được dùng ở mobile seller screen lẫn
seller-web `/leads`; page chung dựng nội dung/bố cục, còn app truyền lead rows,
search/filter handlers, offline state và list implementation.

## Data flow

- Mobile giữ platform store/API integration; shared pages nhận props và
  shared mappers/constants giúp thống nhất domain presentation.
- Seller-web chọn live hoặc demo data source; shared state không cần biết
  source cụ thể. Trong local live flow, relay có thể chuyển tiếp request và
  xử lý cookie/CORS.
- Consumer-web fetch consumer data trên server, không cần relay để tránh CORS;
  SEO metadata/JSON-LD được ghép tại route/page.
- Relay là local-only, không phải package dependency hay production service.

## Quy ước khi làm việc

- Đọc `AGENTS.md` trước khi đổi code; đây là convention chính của repo.
- Khi khám phá Nx workspace, nạp skill `nx-workspace`; chạy task qua `pnpm nx`
  theo package manager của repo.
- Share UI/page trước khi tạo component riêng trong app. Component mới trong
  shared `@bds/ui`/`@bds/ui-seo` cần Storybook story theo convention hiện hành.
- Thay đổi kiến trúc cần cập nhật `docs/architecture.md` và `README.md` cùng
  thay đổi. Repo dùng OpenSpec cho planning; theo workflow và spec tại repo.
- Với thay đổi callback/routing/business behavior có legacy Sellernet tương
  ứng, so sánh behavior legacy trước để tránh contract drift.
- Nâng dependency theo policy của repo (`pnpm deps:plan`); package Hive và
  sellernet đã publish chỉ đổi theo legacy sync.
- consumer-web dùng Next.js có breaking changes so với kiến thức phổ biến; đọc
  `apps/consumer-web/AGENTS.md` và docs đi kèm package `next` trước khi viết
  code Next.
- Chỉ kiểm tra platform bị ảnh hưởng; chọn test/check nhỏ theo rủi ro. Hỏi
  trước khi chạy bộ test rộng hoặc tốn tài nguyên.

## Tài liệu source of truth

- `AGENTS.md`: rules, package boundaries, shared UI/page conventions.
- `docs/architecture.md`: diagrams, render paths, data flow, SSR và relay.
- `README.md`: setup, commands, local environments.
- `openspec/specs/` và `openspec/changes/`: requirements/planning của repo.
- Nx graph và `package.json`: direct project/package dependencies hiện tại.
