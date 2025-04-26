

import streamlit as st
import random

# Say What? - SupportOps MVP Skeleton
# ==================================
# This is the basic Streamlit layout for the Reality Check engine (left) and Chaos Theater (right).

# Placeholder functions for simulation logic and narrative scenes
def simulate_support_action(action, department):
    # TODO: Replace with real calculation logic
    # Return a dict of simulated metrics
    return {
        "Employees Affected": 42,
        "Penalty Risk ($)": 12500,
        "Revenue at Risk ($)": 50000,
        "Compliance Cliff": "🟠 ORANGE"
    }

def get_narrative_scene(scene_id):
    # TODO: Replace with dynamic dialogue based on scene_id
    scenes = {
        1: {
            "ceo": "What in the world just happened...",
            "uncle_sam": "You forgot your 1099s? I didn’t."
        }
    }
    return scenes.get(scene_id, {"ceo": "...", "uncle_sam": "..."})

# Streamlit App
st.set_page_config(page_title="Say What? SupportOps", layout="wide")
st.title("Say What? — SupportOps Simulation")


#Add the Sidebar Dropdown
st.sidebar.title("Disaster Controls 💥")

chaos_choice = st.sidebar.selectbox(
    "Choose Your Chaos:",
    [
        "Let Chaos Decide",
        "Missing 1099s",
        "Late Expense Reports",
        "Unfiled Property Tax",
        "Unleash Total Mayhem"
    ]
)

# Control the Scenes

if chaos_choice == "Let Chaos Decide":
    scene = random.choice(["missing_1099s", "late_expense_reports", "unfiled_property_tax"])
    st.subheader("🎲 Random Disaster Incoming!")
    st.write(get_narrative_scene(scene))

elif chaos_choice == "Unleash Total Mayhem":
    st.subheader("☄️ TOTAL MAYHEM MODE ACTIVATED!")
    for scene in ["missing_1099s", "late_expense_reports", "unfiled_property_tax"]:
        st.write(get_narrative_scene(scene))

else:
    scene_key = chaos_choice.lower().replace(" ", "_")
    st.subheader(f"⚡ Disaster: {chaos_choice}")
    st.write(get_narrative_scene(scene_key))




# Sidebar: Input Module
st.sidebar.header("Reality Check Inputs 🛠️")
action = st.sidebar.selectbox(
    "Select Support Action",
    [
        "Run Payroll",
        "File 1099s",
        "Process Expense Reimbursements",
        "Vendor Payment",
        "File Census Forms"
    ]
)
department = st.sidebar.selectbox(
    "Select Department",
    ["Payroll", "Accounting", "HR", "Vendor Ops"]
)
simulate_button = st.sidebar.button("Simulate Action 🔄")

# Main layout: two columns
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
        # For now, always show scene 1
        scene = get_narrative_scene(1)
        st.markdown(f"**CEO:** {scene['ceo']}")
        st.markdown(f"**Uncle Sam:** {scene['uncle_sam']}")
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
# Randomized “CEO Take” on Each Simulation

CEO_LINES = [
    "Wait—why are we bleeding money?!",
    "Did someone forget to tell me we needed paperwork?",
    "I thought “file taxes” meant “throw forms in a file drawer.”",
    "Why is there a dark cloud over my IPO?!",
    "Can we just pay with Bitcoin and call it a day?"
]

def get_narrative_scene(scene_id):
    return {
        "ceo": random.choice(CEO_LINES),
        "uncle_sam": "You forgot your 1099s? I didn’t."
    }

# “CEO Soundboard” Button"
if st.sidebar.button("CEO Meltdown 🚨"):
    ceo_rant = random.choice(CEO_LINES)
    st.sidebar.error(f"💥 CEO Rant: “{ceo_rant}”")

# Clueless CEO Profile Card
with right_col.expander("👔 Meet the CEO", expanded=False):
    st.markdown("""
    **Name:** Chad “Paperclip” McBoardroom  
    **Title:** Chief Every-Thing Officer  
    **Superpower:** Turning invoices into paper airplanes  
    **Weakness:** Actual paperwork, taxes, adulting  
    **Favorite Phrase:** “Show me the margin… or margaritas!”  
    """)
