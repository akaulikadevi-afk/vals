import streamlit as st
import random

st.set_page_config(page_title="Belated Valentine", page_icon="🤍", layout="centered")

st.markdown(
    """
    <style>
      .wrap {max-width: 760px; margin: 0 auto;}
      .card {
        border: 1px solid rgba(0,0,0,0.10);
        border-radius: 18px;
        padding: 20px;
        background: rgba(255,255,255,0.80);
        backdrop-filter: blur(8px);
      }
      .muted {opacity: 0.7;}
      .big {font-size: 1.05rem; line-height: 1.7;}
      .line {
        height: 1px; background: rgba(0,0,0,0.08); margin: 18px 0;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

TITLE = "happy belated valentine sayang 🤍"

MSG = """telat dikit gapapa lah ya, yg penting niatnya sampe haha.

i really hope this year, and the next years after this, can be our year. bukan cuma soal happy moments, tapi juga soal kita makin dewasa, makin ngerti satu sama lain juga. semoga kita ga ribut ribut mulu karena hal kecil, semoga kalo ada masalah kita bisa ngobrol baik baik, ga saling ninggalin atau saling nyakitin.

aku pengen kita makin solid, makin langgeng, makin stabil. bukan yg heboh di awal doang tapi pelan pelan kuatnya di dalem. i want us to grow, bukan cuma bareng bareng tapi juga masing masing jadi versi yg lebih baik yayyy.

semoga kita bisa terus milih satu sama lain, even pas lagi capek, lagi kesel, lagi ga mood. semoga kita tetep jadi partner, bukan lawan haha. dan semoga semua doa baik buat hubungan ini dikabulin satu satu.

makasih ya udah ada. semoga ke depannya lebih banyak tenang, lebih banyak moment of joy, dan lebih sedikit drama. love you, always sayang🤍"""

# ---- SESSION STATE ----
if "stage" not in st.session_state:
    st.session_state.stage = 0

if "promise_checks" not in st.session_state:
    st.session_state.promise_checks = {
        "ngobrol baik-baik (no ego)": False,
        "ga kabur pas lagi susah": False,
        "lebih sedikit drama": False,
        "jaga cara ngomong": False,
        "tetep milih satu sama lain": False,
    }

st.markdown("<div class='wrap'>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("### 🤍")
st.markdown("<p class='muted'>a tiny page, just for us</p>", unsafe_allow_html=True)
st.markdown("<div class='line'></div>", unsafe_allow_html=True)

# ---- COVER ----
if st.session_state.stage == 0:
    st.markdown("#### ready buka ini? 🤍")

    vibe = st.selectbox("mood kamu sekarang", ["soft", "kangen dikit", "calm tapi sayang"])
    st.caption(f"ok noted: {vibe}")

    if st.button("Open 🤍", use_container_width=True):
        st.session_state.stage = 1
        st.balloons()

# ---- MENU ----
elif st.session_state.stage == 1:
    st.markdown(f"## {TITLE}")
    st.markdown("<p class='muted'>late dikit tapi tetep full niat.</p>", unsafe_allow_html=True)
    st.markdown("<div class='line'></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Read the Note", use_container_width=True):
            st.session_state.stage = 2
            st.session_state.tab = "note"
    with c2:
        if st.button("Mini Promise", use_container_width=True):
            st.session_state.stage = 2
            st.session_state.tab = "promise"
    with c3:
        if st.button("Little Moment", use_container_width=True):
            st.session_state.stage = 2
            st.session_state.tab = "moment"

# ---- CONTENT ----
else:
    st.markdown(f"## {TITLE}")
    st.markdown("<div class='line'></div>", unsafe_allow_html=True)

    tab = st.session_state.get("tab", "note")

    # ---- NOTE ----
    if tab == "note":
        st.markdown(f"<p class='big'>{MSG.replace(chr(10), '<br><br>')}</p>", unsafe_allow_html=True)
        if st.button("confetti dikit 🤍"):
            st.balloons()

    # ---- MINI PROMISE ----
    elif tab == "promise":
        st.caption("ceklist kecil buat kita pelan-pelan ya.")
        for k in st.session_state.promise_checks:
            st.session_state.promise_checks[k] = st.checkbox(
                k, value=st.session_state.promise_checks[k]
            )

        total = sum(st.session_state.promise_checks.values())
        st.progress(total / len(st.session_state.promise_checks))

        if total == len(st.session_state.promise_checks):
            st.success("nah ini. pelan-pelan tapi kompak 🤍")
            st.snow()

    # ---- LITTLE MOMENT ----
    elif tab == "moment":
        q = st.radio("kalo lagi beda pendapat kamu pilih:", [
            "ngobrol baik-baik",
            "diam bentar terus balik ngobrol",
            "peluk dulu baru ngomong"
        ])

        st.markdown("### love meter 🤍")
        love = st.slider("seberapa sayang sih", 0, 100, 87)

        if love < 100:
            st.warning("naikin dong sialan, aku aja sayang km 1000000%%%%")
        else:
            st.success("100%??? ok… kamu resmi jadi tempat pulang aku 🤍")
            st.balloons()

        solid = st.slider("skala pengen makin solid", 0, 10, 10)

        if st.button("lihat hasil"):
            st.success("yang penting kita tetep satu tim 🤍")
            st.write(f"pilihan kamu: {q}")
            st.write(f"love meter: {love}%")
            st.write(f"solid meter: {solid}/10")

    st.markdown("<div class='line'></div>", unsafe_allow_html=True)
    if st.button("balik"):
        st.session_state.stage = 1

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
