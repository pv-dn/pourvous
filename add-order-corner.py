"""Add order corner to user's restored inventory HTML (Downloads _19)."""
from pathlib import Path

DOWNLOADS = Path.home() / "Downloads"
TARGETS = [
    DOWNLOADS / "プゥル・ヴー在庫管理_19.html",
    DOWNLOADS / "プゥル・ヴー在庫管理.html",
]
DEV = Path(__file__).resolve().parent / "在庫管理.html"

ORDER_CSS = """
.order-corner{background:#fff;border-bottom:1px solid #e0ddd5;padding:0.6rem 0.75rem}
.order-corner-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px}
.order-corner-title{font-size:13px;font-weight:600;color:#1a1a1a}
.order-corner-count{font-size:11px;color:#888;margin-left:6px;font-weight:500}
.order-list{list-style:none;display:flex;flex-direction:column;gap:5px;max-height:140px;overflow-y:auto}
.order-empty{font-size:12px;color:#aaa;padding:4px 0}
.order-item{display:flex;align-items:center;justify-content:space-between;background:#f7f6f2;border:1px solid #e8e6e0;border-radius:9px;padding:7px 10px}
.order-item-name{font-size:13px;font-weight:600;color:#1a1a1a}
.order-del{background:none;border:none;color:#999;font-size:14px;cursor:pointer;padding:2px 6px;border-radius:5px;font-family:inherit;line-height:1}
.order-del:active{background:#ffeaea;color:#c0392b}
.icon-btn.order-btn{color:#7a4f00;border-color:#e8c87a;background:#fffaf0}
.icon-btn.order-btn:active{background:#fff3cd}
"""

ORDER_HTML = """
  <div class="order-corner" id="order-corner">
    <div class="order-corner-head">
      <div class="order-corner-title">📋 注文コーナー<span class="order-corner-count" id="order-count"></span></div>
      <button class="hbtn" id="clear-orders-btn" onclick="clearOrders()" style="display:none;font-size:11px;padding:4px 9px">すべて消す</button>
    </div>
    <ul class="order-list" id="order-list"></ul>
  </div>
"""

ORDER_JS = """
const ORDERS_LS_KEY='pourvous_orders';

function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');}

function loadOrdersLocal(){
  try{orders=JSON.parse(localStorage.getItem(ORDERS_LS_KEY)||'[]');}catch{orders=[];}
  ordersUseLocal=true;
  renderOrderCorner();
}
function saveOrdersLocal(){localStorage.setItem(ORDERS_LS_KEY,JSON.stringify(orders));}

async function loadOrders(){
  try{
    const rows=await api('orders?order=created_at.asc');
    orders=rows||[];
    ordersUseLocal=false;
    renderOrderCorner();
  }catch{loadOrdersLocal();}
}

function renderOrderCorner(){
  const el=document.getElementById('order-list');
  const cnt=document.getElementById('order-count');
  const clr=document.getElementById('clear-orders-btn');
  cnt.textContent=orders.length?'（'+orders.length+'件）':'';
  clr.style.display=orders.length?'inline-block':'none';
  if(!orders.length){el.innerHTML='<li class="order-empty">注文はありません</li>';return;}
  el.innerHTML=orders.map(o=>'<li class="order-item"><span class="order-item-name">'+esc(o.item_name)+'</span><button class="order-del" onclick="removeOrder('+o.id+')" title="消す">✕</button></li>').join('');
}

async function placeOrder(name){
  const itemName=String(name).trim();
  if(!itemName)return;
  try{
    if(ordersUseLocal)throw new Error('local');
    const rows=await api('orders','POST',{item_name:itemName});
    orders.push(rows[0]);
  }catch{
    ordersUseLocal=true;
    orders.push({id:Date.now(),item_name:itemName,created_at:new Date().toISOString()});
    saveOrdersLocal();
  }
  renderOrderCorner();
  showToast('注文しました：'+itemName);
}

async function removeOrder(id){
  if(!ordersUseLocal){try{await api('orders?id=eq.'+id,'DELETE');}catch(e){showToast('削除エラー');return;}}
  orders=orders.filter(o=>o.id!=id);
  if(ordersUseLocal)saveOrdersLocal();
  renderOrderCorner();
}

async function clearOrders(){
  if(!orders.length)return;
  if(!confirm('注文コーナーをすべて消しますか？'))return;
  try{
    if(!ordersUseLocal){for(const o of [...orders]){await api('orders?id=eq.'+o.id,'DELETE');}}
    orders=[];
    if(ordersUseLocal)saveOrdersLocal();
    renderOrderCorner();
    showToast('注文をすべて消しました');
  }catch(e){showToast('削除エラー');}
}
"""


def patch(html: str) -> str:
    if "注文コーナー" in html:
        return html

    html = html.replace("@keyframes spin{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}", "@keyframes spin{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}" + ORDER_CSS)

    html = html.replace(
        "  </div>\n  <div class=\"tab-bar\" id=\"tab-bar\"></div>",
        "  </div>" + ORDER_HTML + "\n  <div class=\"tab-bar\" id=\"tab-bar\"></div>",
        1,
    )

    import re
    html = re.sub(
        r'<div class="toast" id="toast">[^<]*</div>',
        '<div class="toast" id="toast"></div>',
        html,
        count=1,
    )

    html = html.replace(
        "let genres=['すべて'],items=[],currentGenre='すべて';",
        "let genres=['すべて'],items=[],orders=[],currentGenre='すべて',ordersUseLocal=false;",
    )

    html = html.replace(
        "function setSyncing(on){document.getElementById('sync-btn').classList.toggle('spinning',on);}",
        "function setSyncing(on){document.getElementById('sync-btn').classList.toggle('spinning',on);}" + ORDER_JS,
    )

    html = html.replace(
        "    renderTabs();renderItems();\n    showToast('データを更新しました');",
        "    renderTabs();renderItems();\n    await loadOrders();\n    showToast('データを更新しました');",
    )

    html = html.replace(
        "  }catch(e){showToast('通信エラー：'+e.message);}\n  setSyncing(false);",
        "  }catch(e){showToast('通信エラー：'+e.message);document.getElementById('items-list').innerHTML='<div class=\"empty\">データを読み込めませんでした。<br>↻ で再試行してください。</div>';}\n  setSyncing(false);",
    )

    html = html.replace(
        """        <div class="item-actions">
          <button class="icon-btn" onclick="toggleEdit(${item.id})">✎</button>""",
        """        <div class="item-actions">
          <button class="icon-btn order-btn" onclick="placeOrder(${JSON.stringify(item.name)})">注文</button>
          <button class="icon-btn" onclick="toggleEdit(${item.id})">✎</button>""",
    )

    html = html.replace("loadAll();", "loadOrdersLocal();loadAll();")

    return html


def main():
    src = next((p for p in TARGETS if p.exists()), None)
    if not src:
        raise SystemExit("User HTML not found in Downloads")
    content = patch(src.read_text(encoding="utf-8"))
    for path in TARGETS:
        if path.exists():
            path.write_text(content, encoding="utf-8")
            print(f"Patched: {path}")
    if DEV.parent.exists():
        DEV.write_text(content, encoding="utf-8", newline="\n")
        print(f"Patched: {DEV}")


if __name__ == "__main__":
    main()
