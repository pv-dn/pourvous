# プゥル・ヴー在庫管理

## 公開URL（メイン）

**https://pourvous-inventory.web.app/**

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
