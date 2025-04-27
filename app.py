
# ─── Page config & Peace Meter ──────────────────────────────────────────────────
st.set_page_config(page_title="Say What? SupportOps", layout="wide")
if 'peace' not in st.session_state:
    st.session_state.peace = 100

# ─── Sidebar: Peace Meter & Intervention ─────────────────────────────────────────
st.sidebar.metric("🕊️ Peace Meter", f"{st.session_state.peace} / 100")
if st.sidebar.button("Auto-Approve Routine Filings ✔️"):
    st.session_state.peace = min(100, st.session_state.peace + 20)
    st.sidebar.success("Routine filings fast-tracked—peace restored!")

# ─── Helper functions ───────────────────────────────────────────────────────────
def simulate_support_action(action, department):
    return {
        "Employees Affected": random.randint(10, 100),
        "Penalty Risk ($)": round(random.uniform(0, 20000), 2),
        "Revenue at Risk ($)": round(random.uniform(10000, 100000), 2),
        "Compliance Cliff": random.choice(["🟢 GREEN","🟠 ORANGE","🔴 RED"])
    }

def generate_ipo_impact(action, dept):
    if action in ["File 1099s", "Process Census Forms"]:
        penalty = round(random.uniform(100000, 500000),2)
        reason = "VP/Director failed to review executive filings"
    else:
        penalty, reason = 0, "No executive-level misfiling"
    return penalty, reason

def get_narrative_scene(key):
    scenes = {
        "missing_1099s": {"ceo":"We’ll breeze through the IPO—I trust marketing to spin any story.","uncle_sam":"I don’t care about late receipts; I care about missing executive filings."},
        "late_expense_reports":{"ceo":"Expense reports? Meh, let them file when they can.","uncle_sam":"Late expenses don’t scare me—misclassified executive expenses do."},
        "unfiled_property_tax":{"ceo":"Property tax is for peasants. We’ve got bigger things to worry about.","uncle_sam":"Unfiled property tax by your directors? Now that’s a problem."}
    }
    return scenes.get(key, {"ceo":"All is calm… too calm.","uncle_sam":"Waiting for real trouble."})

# ─── Main Title ──────────────────────────────────────────────────────────────────
st.title("Say What? — SupportOps Simulation")

# ─── Tabs: Reality Check vs. Chaos Theater vs. Epilogue ───────────────────────────
tabs = st.tabs(["Reality Check 🛠️","Chaos Theater 🎭","Bonus Epilogue 🔒"])

with tabs[0]:
    st.subheader("Reality Check Panel")
    action = st.selectbox("Support Action", ["Run Payroll","File 1099s","Process Expense Reimbursements","Vendor Payment","Process Census Forms"], key="action1")
    dept = st.selectbox("Department", ["Payroll","Accounting","HR","Vendor Ops"], key="dept1")
    if st.button("Simulate Reality 🔄", key="real_btn"):
        metrics = simulate_support_action(action, dept)
        for k,v in metrics.items():
            st.metric(label=k,value=v)
        drop = random.randint(5,20)
        st.session_state.peace = max(0, st.session_state.peace - drop)
        st.write(f"🕊️ Peace dropped by {drop} points.")

    st.markdown("---")
    st.subheader("IPO-Level Audit Risk")
    penalty, reason = generate_ipo_impact(action, dept)
    if penalty:
        st.error(f"🚨 IRS Penalty: ${penalty:,} due to {reason}")
    else:
        st.success("✅ No executive-level penalties detected.")

with tabs[1]:
    st.subheader("Chaos Theater")
    chaos = st.selectbox("Choose Chaos Scenario", ["Missing 1099s","Late Expense Reports","Unfiled Property Tax"], key="chaos1")
    if st.button("Unleash Chaos 🎲", key="chaos_btn"):
        key_id = chaos.lower().replace(" ","_")
        scene = get_narrative_scene(key_id)
        col1,col2 = st.columns(2)
        with col1:
            st.markdown(f"<div style='padding:10px;border-radius:8px;background:#ff7043;color:#fff'><strong>CEO:</strong> {scene['ceo']}</div>",unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div style='padding:10px;border-radius:8px;background:#42a5f5;color:#fff'><strong>Uncle Sam:</strong> {scene['uncle_sam']}</div>",unsafe_allow_html=True)

with tabs[2]:
    unlock = st.checkbox("I seek the hidden path", key="unlock_easter")
    if unlock:
        st.markdown("**The office grows dark.**  The hero stands at the threshold of a lonely road...")
        st.image("https://via.placeholder.com/600x200?text=Sketch+Road", caption="A dark, rural path")
        st.markdown("🔒 The plain book appears once more in his hand.")
        st.markdown("> The hero bows in gratitude, then steps onto the path.")
        st.image("https://via.placeholder.com/100x200?text=Footprints", width=100)
        st.markdown("> As he walks, flute notes and footprints illuminate the way until he fades into the distance.")
        st.markdown("---")
        st.markdown("📖 The CEO greedily opens the book. The pages are blank—until a final line appears:")
        st.markdown("> *“This divine knowledge reveals itself only to the chosen ones. Turn inward.”*")

# ─── Flute & Footprints & Feather Visuals ───────────────────────────────────────
if st.session_state.peace < 30:
    st.markdown("🎶 A flute appears... soft notes guide you forward.")
    st.markdown("👣 Footprints appear, leading the way...")
if st.session_state.peace > 90:
    st.markdown("🦚 A peacock feather drifts down in celebration.")

# ─── Footer Placeholders ───────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "**Placeholders:**<br>"
    "- TODO: Compliance Cliff Counter logic<br>"
    "- TODO: Multi-scene branching outcomes<br>"
    "- TODO: Replace placeholder images with final art",
    unsafe_allow_html=True
)
```


