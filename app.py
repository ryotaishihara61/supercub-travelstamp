
import streamlit as st
from data import destinations

st.set_page_config(page_title="スーパーカブ旅すごろく", layout="centered")

st.markdown("## 🏍 スーパーカブ旅すごろく")
st.markdown("現在のスーパーカブの総走行距離を入力してください。")

# 中古時点のメーター値
base_odometer = 39670
odometer = st.number_input("現在のメーター走行距離（km）", min_value=base_odometer)
distance = max(0, odometer - base_odometer)

st.markdown(f"**🛣 旅の走行距離**：{distance} km")

# 現在地点を取得
current = destinations[0]
for d in destinations:
    if distance >= d["distance"]:
        current = d
    else:
        break

# カラムレイアウト（左広め、画像縮小）
col1, col2 = st.columns([2.5, 2])

with col1:
    st.markdown("### 🎯 スタンプ進行状況")
    lines = []
    for d in destinations:
        label = f"{d['name']}（{d['country']}）"
        if distance >= d["distance"]:
            if distance < d["distance"] + 50:
                lines.append(f"🔵 {label}")
            else:
                lines.append(f"✅ {label}")
        else:
            lines.append(f"⬜ {label}")
    st.text("\n".join(lines))

with col2:
    st.markdown(f"### 🗺 現在地：{current['name']}（{current['country']}）")
    st.markdown(f"📝 {current['message']}")
    try:
        st.image(f"images/{current['image']}", width=250)  # 約70%サイズ
    except Exception as e:
        st.warning(f"画像の読み込みに失敗しました: {e}")
