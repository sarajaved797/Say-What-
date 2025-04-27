import streamlit as st, random

# ─── Page config & Peace Meter ──────────────────────────────────────────────────
st.set_page_config(page_title="Say What? SupportOps", layout="wide")
if 'peace' not in st.session_state:
    st.session_state.peace = 100
if 'hero_state' not in st.session_state:
    st.session_state.hero_state = 'idle'

# ─── Choice Lists ─────────────────────────────────────────────────────────────
actions = ["Run Payroll", "File 1099s", "Process Expenses", "Vendor Payment", "Process Census Forms"]
CEO_LINES = [
    "We’ll breeze through the IPO—I trust marketing to spin any story.",
    "Expenses? Meh. Focus on the vision!",
    "I walked into a top-tier company. IPO is just a checkbox.",
    "Bonuses first, paperwork later!"
]
UNCLE_SAM_LINES = [
    "I don’t care about late receipts; I care about missing executive filings.",
    "You filed money, not forms—big difference.",
    "Paperwork or penalties—you choose.",
    "Forms late? Fines early."
]

# ─── Sidebar: Reality Check & Peace ─────────────────────────────────────────────
with st.sidebar:
    st.header("Reality Check 💰")
    action = st.selectbox("Support Action", actions, key="action_sim")
    if st.button("Simulate Reality 🔄", key="sim1"):
        # Hard-dollar metrics
        cod = random.randint(1000, 10000)            # Cost of Delay per day
        penalty = random.randint(0, 500000)         # Penalty Risk
        savings = random.randint(0, 50000)          # Savings Unlocked
        st.metric("Cost of Delay ($/day)", f"${cod}")
        st.metric("Penalty Risk ($)", f"${penalty}")
        st.metric("Savings Unlocked ($)", f"${savings}")
        # Update hero state and peace
        if penalty > 50000:
            st.session_state.hero_state = 'in_trouble'
            st.session_state.peace = max(0, st.session_state.peace - 30)
        else:
            st.session_state.hero_state = 'celebrate'
            st.session_state.peace = min(100, st.session_state.peace + 20)
    st.markdown("---")
    st.metric("🕊️ Peace Meter", f"{st.session_state.peace} / 100")

# ─── Main: Two Panels ──────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

# Act I: Chaos Theater (CEO & Uncle Sam)
with col1:
    st.subheader("Chaos Theater 🎭")
    st.write("**CEO:**", random.choice(CEO_LINES))
    st.write("**Uncle Sam:**", random.choice(UNCLE_SAM_LINES))

# Act II: Hero’s Path & Cliffhanger
with col2:
    st.subheader("Hero’s Path 🛤️")
    state = st.session_state.hero_state
    if state == 'in_trouble':
        st.markdown("🎶 A flute appears... soft notes guide you.")
        st.markdown("👣 Footprints light the way.")
        # Cliffhanger: CEO fires the hero
        st.error("💥 YOU ARE FIRED!!!!!!!!!!!! and ...")
        # Exit scene commented out for free version
        # st.session_state.hero_state = 'exit'
    elif state == 'celebrate':
        st.markdown("🦚 A peacock feather drifts down in celebration.")
    else:
        st.write("The hero stands ready...")
    if st.button("Resolve Action ✅", key="res1"):
        st.session_state.hero_state = 'celebrate'
        st.session_state.peace = min(100, st.session_state.peace + 40)

# ─── Footer Placeholders ───────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "**Placeholders:**<br>"
    "- TODO: Compliance Cliff Counter logic<br>"
    "- TODO: Multi-scene branching outcomes<br>"
    "- TODO: Replace placeholders with final art",
    unsafe_allow_html=True
)
```
