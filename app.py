import streamlit as st
import random

st.set_page_config(page_title="Belated Valentine", page_icon="🤍", layout="centered")

# --- clean, minimal styling ---
st.markdown(
    """
    <style>
      .wrap {max-width: 760px; margin: 0 auto;}
      .card {
        border: 1px solid rgba(0,0,0,0.10);
        border-radius: 18px;
        padding: 18px;
        background: rgba(255,255,255,0.75);
        backdrop-filter: blur(8px);
      }
      .muted {opacity: 0.75;}
      .big {font-size: 1.05rem; line-height: 1.7;}
      .line {
        height: 1px; background: rgba(0,0,0,0.08); margin: 14px 0;
      }
      .pill {
        display: inline-block;
        padding: 6px 10px;
        border-radius: 999px;
        border: 1px solid rgba(0,0,0,0.10);
        margin-right: 6px;
        margin-bottom: 8px;
        font-size: 0.92rem;
        opacity: 0.9;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- message you provided (verbatim) ---
TITLE = "happy belated valentine sayang 🤍"
MSG = """telat dikit gapapa lah ya, yg penting niatnya sampe haha.

i really hope this year, and the next years after this, can be our year. bukan cuma soal happy moments, tapi juga soal kita makin dewasa, makin ngerti satu sama lain juga. semoga kita ga ribut ribut mulu karena hal kecil, semoga kalo ada masalah kita bisa ngobrol baik baik, ga saling ninggalin atau saling nyakitin.

aku pengen kita makin solid, makin langgeng, makin stabil. bukan yg heboh di awal doang tapi pelan pelan kuatnya di dalem. i want us to grow, bukan cuma bareng bareng tapi juga masing masing jadi versi yg lebih baik yayyy.

semoga kita bisa terus milih satu sama lain, even pas lagi capek, lagi kesel, lagi ga mood. semoga kita tetep jadi partner, bukan lawan haha. dan semoga semua doa baik buat hubungan ini dikabulin satu satu.

makasih ya udah ada. semoga ke depannya lebih banyak tenang, lebih banyak moment of joy, dan lebih sedikit drama. love you, always sayang🤍"""

# --- session state ---
if "stage" not in st.session_state:
    st.session_state.stage = 0  # 0 cover, 1 opened, 2 revealed
if "reveal" not in st.session_state:
    st.session_state.reveal = {"message": False, "promises": False, "mini": False}
if "promise_checks" not in st.session_state:
    st.session_state.promise_checks = {
        "ngobrol baik-baik": False,
        "ga kabur pas masalah": False,
        "lebih sedikit drama": False,
        "jaga hati & cara ngomong": False,
        "tetep pilih satu sama lain": False,
    }

# --- header ---
st.markdown("<div class='wrap'>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("### 🤍")
st.markdown("<p class='muted'>a tiny page, buat satu orang</p>", unsafe_allow_html=True)
st.markdown("<div class='line'></div>", unsafe_allow_html=True)

# --- stage-based UI ---
if st.session_state.stage == 0:
    st.markdown("#### Tap dulu ya")
    col1, col2 = st.columns([1, 1])
    with col1:
        name = st.text_input("Nama panggilan kamu", placeholder="isi bebas")
    with col2:
        vibe = st.selectbox("Mood buka ini:", ["pelan-pelan", "senyum dikit", "kangen tipis-tipis"])

    st.markdown(
        f"<span class='pill'>mode: {vibe}</span>"
        f"<span class='pill'>klik: di bawah</span>",
        unsafe_allow_html=True,
    )

    if st.button("Open 🤍", use_container_width=True):
        st.session_state.stage = 1
        st.balloons()

elif st.session_state.stage == 1:
    st.markdown(f"## {TITLE}")
    st.markdown("<p class='muted'>telat dikit, tapi niatnya beneran.</p>", unsafe_allow_html=True)

    st.markdown("<div class='line'></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Buka pesannya", use_container_width=True):
            st.session_state.reveal["message"] = True
            st.session_state.stage = 2
    with c2:
        if st.button("Janji kecil", use_container_width=True):
            st.session_state.reveal["promises"] = True
            st.session_state.stage = 2
    with c3:
        if st.button("Mini moment", use_container_width=True):
            st.session_state.reveal["mini"] = True
            st.session_state.stage = 2

    st.info("Pilih salah satu dulu. Nanti bisa balik-balik kok.")

else:
    # stage 2 — content revealed
    st.markdown(f"## {TITLE}")

    tabs = st.tabs(["Pesan", "Janji kecil", "Mini moment"])
    with tabs[0]:
        st.markdown("<div class='line'></div>", unsafe_allow_html=True)
        st.markdown(f"<p class='big'>{MSG.replace('\n', '<br><br>')}</p>", unsafe_allow_html=True)
        st.markdown("<div class='line'></div>", unsafe_allow_html=True)
        if st.button("Confetti dikit", use_container_width=True):
            st.balloons()

    with tabs[1]:
        st.markdown("<div class='line'></div>", unsafe_allow_html=True)
        st.caption("ceklist yang simpel aja, biar inget pelan-pelan.")
        for k in list(st.session_state.promise_checks.keys()):
            st.session_state.promise_checks[k] = st.checkbox(
                k, value=st.session_state.promise_checks[k]
            )

        total = sum(st.session_state.promise_checks.values())
        st.progress(total / len(st.session_state.promise_checks))
        st.write(f"{total}/{len(st.session_state.promise_checks)}")

        if total == len(st.session_state.promise_checks):
            st.success("nah ini. pelan-pelan tapi kompak 🤍")
            st.snow()

    with tabs[2]:
        st.markdown("<div class='line'></div>", unsafe_allow_html=True)
        st.caption("jawab santai ya.")
        q1 = st.radio("kalau kita lagi beda pendapat, yang kamu pilih:", [
            "ngobrol baik-baik",
            "minta waktu bentar terus balik ngobrol",
            "peluk dulu baru ngomong",
        ])
        q2 = st.slider("skala pengen makin solid:", 0, 10, 10)

        if st.button("Lihat hasil", use_container_width=True):
            responses = [
                "okeh. yang penting kita tetap satu tim.",
                "deal. kita belajar pelan-pelan, bareng.",
                "tenang. kita bisa kok ngelewatin hal kecil tanpa jadi besar.",
            ]
            st.success(random.choice(responses))
            st.write(f"pilihan kamu: **{q1}**")
            st.write(f"solid meter: **{q2}/10**")

        st.markdown("<div class='line'></div>", unsafe_allow_html=True)
        note = st.text_area("tulis 1 kalimat buat kita (optional)", placeholder="misal: kita kuat pelan-pelan.")
        if note and st.button("Simpan di halaman ini", use_container_width=True):
            st.session_state.saved_note = note.strip()

        if "saved_note" in st.session_state and st.session_state.saved_note:
            st.markdown("**catatan kamu:**")
            st.write(st.session_state.saved_note)

    st.markdown("<div class='line'></div>", unsafe_allow_html=True)
    if st.button("Balik ke menu awal", use_container_width=True):
        st.session_state.stage = 1

st.markdown("</div>", unsafe_allow_html=True)  # card
st.markdown("</div>", unsafe_allow_html=True)  # wrap
