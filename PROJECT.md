# プゥル・ヴー在庫管理（pourvous-inventory）

| 項目 | 内容 |
|------|------|
| **ID** | `pourvous-inventory` |
| **フォルダ** | `c:\dev\pourvous` |
| **一覧** | [c:\dev\PROJECTS.md](c:\dev\PROJECTS.md) |

## 概要

プゥル・ヴー向けの在庫管理 PWA。単体 HTML が正本。Supabase で注文コーナーを複数端末共有。

## 技術スタック

- 単体 HTML（`在庫管理.html` が正本）
- Supabase（注文データ: プロジェクト `jsowadohckantjtljdlb`）
- Firebase Hosting（任意・バックアップ用）
- Chrome インストール済み PWA

## 主要ファイル

| パス | 内容 |
|------|------|
| `在庫管理.html` | **正本**（編集はここ） |
| `manifest.webmanifest` | PWA 設定 |
| `supabase-orders-table.sql` | Supabase テーブル定義 |
| `install-desktop-shortcut.ps1` | デスクトップショートカット更新 |

## 起動

- デスクトップ `PourVous在庫管理.lnk` → Chrome PWA
- 開発: `在庫管理.html` をブラウザで直接開く

## 他アプリとの関係

**共有コードなし。** しゃぼん玉在庫管理（shabon-inventory）とは別アプリ・別データ。

## 変更履歴メモ

| 日付 | 内容 |
|------|------|
| 2026-06-11 | `c:\Users\e--yo\pourvous` から `c:\dev\pourvous` へ移動 |
