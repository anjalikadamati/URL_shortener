# URL Shortener - Recent Links Fix TODO

## Approved Plan Steps:
- [x] 1. Update vite.config.js: Add proxy for /api → backend (localhost:5000)
- [x] 2. Update App.jsx: Error state, refetch on new link, /api/recent
- [x] 3. Update RecentLinks.jsx: Better truncation, accessibility (tooltip, aria-labels)
- [x] 4. Test: Backend run.py, frontend npm run dev
- [x] 5. Verify: Shorten URL → recent shows, clicks update (production-ready)

## Delete Feature + UI Fix TODO

- [x] 1. Backend: Add DELETE /delete/<short_code> endpoint
- [x] 2. Frontend RecentLinks: Delete button + API call + optimistic
- [ ] 3. App.css: Fix .recent-card spacing, .clicks badge
- [x] 4. Test delete + UI

Progress: Starting delete feature
