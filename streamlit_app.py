import streamlit as st

# ─── 세션 상태 초기화 ───────────────────────────────────────────
if "selected" not in st.session_state:
    st.session_state.selected = None

# ─── 페이지 설정 ─────────────────────────────────────────────────
st.set_page_config(page_title="Dose to Food", layout="centered")

# ─── 타이틀 ───────────────────────────────────────────────────────
st.markdown(
    "<h1 style='text-align:center; font-family:Pacifico, cursive;'>Dose to Food</h1>",
    unsafe_allow_html=True
)
st.write("---")

# ─── 검색창 ───────────────────────────────────────────────────────
query = st.text_input("약물 검색...", "")

# ─── 약물 리스트 및 필터링 ───────────────────────────────────────
drugs = ["변비약"]
filtered = [d for d in drugs if query.lower() in d.lower()]

# ─── 버튼 그리드 (토글 기능 포함) ────────────────────────────────
cols = st.columns(3)
for idx, drug in enumerate(filtered):
    with cols[idx % 3]:
        clicked = st.button(drug, key=f"btn_{drug}")
        if clicked:
            if st.session_state.selected == drug:
                st.session_state.selected = None
            else:
                st.session_state.selected = drug

# ─── 상세 뷰 ────────────────────────────────────────────────────
if st.session_state.selected:
    info_map = {
        "변비약": {
            "side_effect": "과다 복용 시 설사, 복통 발생 가능",
            "alternatives": ["Kiwi (100g)", "Xylobiose 5g"],
        }
    }
    sel = st.session_state.selected
    info = info_map.get(sel, {})

  

    # 부작용 카드
    st.markdown(f"""
    <div style="
        background:#fde2e4;
        color:#000;
        padding:16px;
        border-radius:8px;
        margin-bottom:12px;
    ">
        <strong>약의 부작용</strong><br>{info.get('side_effect','')}
    </div>
    """, unsafe_allow_html=True)

    # 대체 성분/음식 카드
    for i, alt in enumerate(info.get("alternatives", []), start=1):
        st.markdown(f"""
        <div style="
            background:#fff3bf;
            color:#000;
            padding:16px;
            border-radius:8px;
            margin-bottom:12px;
        ">
            <strong>대체 성분/음식 {i}</strong><br>{alt}
        </div>
        """, unsafe_allow_html=True)

# ─── CSS 스타일 (원형 버튼 배경 흰색으로) ─────────────────────────
st.markdown(
    """
    <style>
      /* 버튼 원형, 배경을 흰색으로, 텍스트 검정 */
      div.stButton > button {
          width:100px;
          height:100px;
          border-radius:50%;
          background-color:#fff !important;
          color:#000 !important;
          font-weight:bold;
          border:1px solid #ccc;
      }
      /* 버튼 그리드 중앙 정렬 */
      [data-testid="stColumns"] {
          justify-content:center !important;
      }
      /* 카드 내부 텍스트 검정 */
      div[style*="background:#fde2e4"] *,
      div[style*="background:#fff3bf"] * {
          color:#000 !important;
      }
    </style>
    """,
    unsafe_allow_html=True
)
