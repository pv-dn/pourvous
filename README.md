# プゥル・ヴー在庫管理

正本: `在庫管理.html`（Supabase `jsowadohckantjtljdlb`・注文コーナー付き）

## 日常の起動方法（これが在庫管理アプリ）

- デスクトップ `PourVous在庫管理.lnk` → Chrome インストール版 PWA（`app-id=fjdfpjippadiknpllhijkfnbcajpnbbo`）
- 元ファイル: `Downloads\プゥル・ヴー在庫管理_19.html`（`c:\dev\pourvous\在庫管理.html` と同期）

## 使わない URL（別デプロイ）

- **https://pourvous-inventory.web.app/** — Firebase 用の別サイト。ユーザーは利用しない。

## 注文コーナー（Supabase）

複数端末で注文を共有するには、Supabase で `supabase-orders-table.sql` を実行してください。

1. [Supabase ダッシュボード](https://supabase.com/dashboard) → プロジェクト `jsowadohckantjtljdlb`
2. SQL Editor → `supabase-orders-table.sql` の内容を貼り付けて Run

## デスクトップショートカット

```powershell
.\install-desktop-shortcut.ps1
```

（Chrome PWA 向け。`pourvous-inventory.web.app` には向けない。）

## Firebase（任意・バックアップ用のみ）

ユーザー向けの公開先ではない。必要なときだけ:

```powershell
firebase deploy --only hosting --project zaikokanri-5708f
```
