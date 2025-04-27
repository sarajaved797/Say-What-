import streamlit as st
import random

# Streamlit App starts here
st.set_page_config(page_title="Say What? SupportOps", layout="wide")
# 1) Peace Meter init
if 'peace' not in st.session_state:
    st.session_state.peace = 100

# Sidebar: Peace Meter display
st.sidebar.metric("🕊️ Peace Meter", f"{st.session_state.peace} / 100")

# Sidebar: interventions
if st.sidebar.button("All-Hands Meditation 🧘"):
    st.session_state.peace = min(100, st.session_state.peace + 30)
if st.sidebar.button("Auto-Approve Filings ✔️"):
    st.session_state.peace = min(100, st.session_state.peace + 20)
    st.sidebar.success("Routine filings fast-tracked—peace restored!")

# Main title
st.title("Say What? — SupportOps Simulation")

# Simulate Action
action = st.sidebar.selectbox("Action", ["Run Payroll", "File 1099s"])
simulate_button = st.sidebar.button("Simulate Action 🔄")

if simulate_button:
    # … your existing simulate_support_action logic
    drop = random.randint(10, 25)
    st.session_state.peace = max(0, st.session_state.peace - drop)
    st.subheader(f"After {action}, Peace dropped by {drop} points.")

# 5) Gita Moment if peace is low
if st.session_state.peace < 30:
    st.balloons()
    st.success(
      "🧘 Gita Moment: “When your mind is unstirred by sorrow and fear, you dwell in perfect peace.”")





st.title("Say What? — The App 🚀 - SupportOps Simulation")

# Placeholder functions for simulation logic and narrative scenes
def simulate_support_action(action, department):
    # TODO: Replace with real calculation logic
    return {
        "Employees Affected": 42,
        "Penalty Risk ($)": 12500,
        "Revenue at Risk ($)": 50000,
        "Compliance Cliff": "🟠 ORANGE"
    }

def get_narrative_scene(scene_id):
    scenes = {
        "missing_1099s": {
            "ceo": "What in the world just happened... We've got missing 1099s!",
            "uncle_sam": "You forgot your 1099s? I didn’t. 🧾"
        },
        "late_expense_reports": {
            "ceo": "Did you seriously let the expense reports slip?!",
            "uncle_sam": "Expenses are late? I'm going to need an explanation."
        },
        "unfiled_property_tax": {
            "ceo": "Unfiled property tax?! We're in trouble!",
            "uncle_sam": "The IRS is gonna have a field day. 😬"
        }
    }
    return scenes.get(scene_id, {"ceo": "No chaos here yet...", "uncle_sam": "Waiting for chaos!"})

# Available chaos choices
chaos_options = ["Missing 1099s", "Late Expense Reports", "Unfiled Property Tax"]

# Sidebar input for chaos choice
chaos_choice = st.sidebar.selectbox("Choose a Chaos Scenario", chaos_options)

# Get the narrative based on the selected scenario
scene_key = chaos_choice.lower().replace(" ", "_")
story = get_narrative_scene(scene_key)

# Display the chaos narrative
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    <div style="border-radius: 10px; background-color: #ff7043; padding: 10px; box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.2);">
        <h4 style="color: #fff;">🧑‍💼 CEO says:</h4>
        <p style="color: #fff;">{story["ceo"]}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="border-radius: 10px; background-color: #42a5f5; padding: 10px; box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.2);">
        <h4 style="color: #fff;">🦅 Uncle Sam says:</h4>
        <p style="color: #fff;">{story["uncle_sam"]}</p>
    </div>
    """, unsafe_allow_html=True)

# Button to trigger a CEO rant
if st.sidebar.button("CEO Meltdown 🚨"):
    ceo_rant = random.choice([
        "This is the worst thing that's ever happened!",
        "Can we please get some organized chaos around here?!",
        "I'm about to lose it over these 1099s!"
    ])
    st.sidebar.error(f"💥 CEO Rant: “{ceo_rant}”")

# Sidebar: Input Module for Simulated Action
st.sidebar.header("Reality Check Inputs 🛠️")
action = st.sidebar.selectbox(
    "Select Support Action",
    ["Run Payroll", "File 1099s", "Process Expense Reimbursements", "Vendor Payment", "File Census Forms"]
)
department = st.sidebar.selectbox("Select Department", ["Payroll", "Accounting", "HR", "Vendor Ops"])
simulate_button = st.sidebar.button("Simulate Action 🔄")

# Main layout: two columns for Reality Check and Chaos Theater
left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader("Reality Check Panel 📉")
    if simulate_button:
        metrics = simulate_support_action(action, department)
        for k, v in metrics.items():
            st.metric(label=k, value=v)
    else:
        st.markdown("_Select an action and click **Simulate Action** to see the impact._")

with right_col:
    st.subheader("Chaos Theater 🎭")
    if simulate_button:
        st.markdown(f"**CEO:** {story['ceo']}")
        st.markdown(f"**Uncle Sam:** {story['uncle_sam']}")
    else:
        st.markdown("_The story unfolds here once you simulate a scenario._")

# Footer / placeholders
st.markdown("---")
st.markdown(
    "**Placeholders:**<br>"
    "`# TODO:` Add Compliance Cliff Counter logic<br>"
    "`# TODO:` Add multi-scene support and dynamic thresholds<br>"
    "`# TODO:` Hook into real penalty calculation functions",
    unsafe_allow_html=True
)

# CEO Soundboard
CEO_LINES = [
    "Wait—why are we bleeding money?!",
    "Did someone forget to tell me we needed paperwork?",
    "I thought “file taxes” meant “throw forms in a file drawer.”",
    "Why is there a dark cloud over my IPO?!",
    "Can we just pay with Bitcoin and call it a day?"
]
