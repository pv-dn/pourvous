# プゥル・ヴー在庫管理

正本: `在庫管理.html`（Supabase `jsowadohckantjtljdlb`・注文コーナー付き）

## 公開URL

**https://pourvous-inventory.web.app/**

デスクトップの `PourVous在庫管理.lnk`（Chrome PWA）を使う場合は `Downloads\プゥル・ヴー在庫管理_19.html` も同内容に同期済み。

## 注文コーナー（Supabase）

複数端末で注文を共有するには、Supabase で `supabase-orders-table.sql` を実行してください。

1. [Supabase ダッシュボード](https://supabase.com/dashboard) → プロジェクト `jsowadohckantjtljdlb`
2. SQL Editor → `supabase-orders-table.sql` の内容を貼り付けて Run

## デスクトップショートカット

```powershell
.\install-desktop-shortcut.ps1
```

## Firebase へ再デプロイ

```powershell
firebase deploy --only hosting --project zaikokanri-5708f
```
