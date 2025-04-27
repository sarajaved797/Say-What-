import streamlit as st, random

import streamlit as st
import random

# ─── Define all  choice-lists up front ────────────────────────
actions = [
    "Run Payroll",
    "File 1099s",
    "Process Expense Reimbursements",
    "Vendor Payment",
    "Process Census Forms"
]

CEO_LINES = [
    "Let's be honest, we're going public because of ME.",
    "My vision has carried this company to the brink of IPO!",
    "I walked into a top-tier business—IPO is just a checkbox.",
    "We're worth billions—tax filings are trivial.",
    "Bonuses first, paperwork later!"
]

UNCLE_SAM_LINES = [
    "I don’t care about late receipts; I care about missing executive filings.",
    "You filed the money but not the form—big difference.",
    "Paperwork or penalties—your choice.",
    "I audit what I see, not what you pay.",
    "Forms late? Fines early."
]

# Now call:
# action = st.sidebar.selectbox("Action", actions)
# st.write("CEO:", random.choice(CEO_LINES))
# st.write("Uncle Sam:", random.choice(UNCLE_SAM_LINES))



# --- Reality Check (left) ---
st.sidebar.header("Reality Check 💰")
actions = [
    "Run Payroll",
    "File 1099s",
    "Process Expense Reimbursements",
    "Vendor Payment",
    "Process Census Forms"
]
action = st.sidebar.selectbox("Action", actions)
if st.sidebar.button("Simulate"):
    penalty = random.randint(0,100000)
    st.sidebar.metric("Penalty Risk", f"${penalty:,}")
    hero_state = "in_trouble" if penalty>50000 else "celebrate"
    st.session_state.hero_state = hero_state

# --- Main panels ---
col1, col2 = st.columns([1,1])

# Act I: Chaos Theater
with col1:
    st.header("Chaos Theater")
    st.write("**CEO:**", random.choice(CEO_LINES))
    st.write("**Uncle Sam:**", random.choice(UNCLE_SAM_LINES))

# Act II: Hero’s Journey
with col2:
    st.header("Hero’s Journey")
    hs = st.session_state.get("hero_state","idle")
    if hs=="in_trouble":
        st.markdown("🎶 A flute appears… 👣 footprints guide you.")
    elif hs=="celebrate":
        st.markdown("🦚 A peacock feather drifts down.")
    elif hs=="exit":
        st.markdown("The hero bows and walks the illuminated path…")
        st.write("*This divine knowledge reveals itself only to the chosen ones.*")
    else:
        st.write("The hero stands ready…")



