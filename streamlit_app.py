import streamlit as st

# ─── 세션 상태 초기화 (한 번만) ──────────────────────────
if "selected" not in st.session_state:
    st.session_state.selected = None

# ─── 페이지 설정 ──────────────────────────────────────────
st.set_page_config(page_title="Dose to Food", layout="centered")

# ─── 타이틀 ───────────────────────────────────────────────
st.markdown(
    "<h1 style='text-align:center; font-family: Pacifico, cursive;'>Dose to Food</h1>",
    unsafe_allow_html=True,
)
st.write("---")

# ─── 검색창 ───────────────────────────────────────────────
query = st.text_input("약물 검색...", "")

# ─── 약물 리스트 & 필터링 ─────────────────────────────────
drugs = ["변비약"]  # 예시: 변비약 한 가지
filtered = [d for d in drugs if query.lower() in d.lower()]

# ─── 버튼 그리드 (3열) ────────────────────────────────────
cols = st.columns(3)
for idx, drug in enumerate(filtered):
    with cols[idx % 3]:
        # 키를 유니크하게! 한 번만 st.button 호출
        if st.button(drug, key=f"btn_{drug}"):
            st.session_state.selected = drug

# ─── 상세 뷰 (선택된 약물이 있을 때) ───────────────────────
if st.session_state.selected:
    # 정보 매핑 (추후 다른 약들도 여기에 추가)
    info_map = {
        "변비약": {
            "side_effect": "과다 복용 시 설사, 복통이 발생할 수 있습니다.",
            "alternatives": ["Kiwi (100g)", "Xylobiose 5g"],
        }
    }
    info = info_map[st.session_state.selected]

    st.markdown(f"## {st.session_state.selected} 상세 정보")

    # 부작용 카드 (핑크)
    st.markdown(
        f"""
        <div style="
            background:#fde2e4;
            padding:16px;
            border-radius:8px;
            margin-bottom:12px;
        ">
            <strong>약의 부작용</strong><br>
            {info['side_effect']}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 대체 성분/음식 카드 (옐로우)
    for i, alt in enumerate(info["alternatives"], start=1):
        st.markdown(
            f"""
            <div style="
                background:#fff3bf;
                padding:16px;
                border-radius:8px;
                margin-bottom:12px;
            ">
                <strong>대체 성분/음식 {i}</strong><br>
                {alt}
            </div>
            """,
            unsafe_allow_html=True,
        )

# ─── CSS 스타일 (버튼 원형, 중앙 정렬, 볼드체) ────────────────
st.markdown(
    """
    <style>
    /* 버튼 그리드(컬럼) 전체를 가운데 정렬 */
    [data-testid="stColumns"] {
      justify-content: center !important;
    }
    /* 첫 번째 버튼(각 컬럼 내)만 원형으로, 글씨 볼드 */
    div.stButton > button:first-child {
      width: 100px;
      height: 100px;
      border-radius: 50%;
      background-color: #dce5ff;
      font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
