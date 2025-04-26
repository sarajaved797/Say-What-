import streamlit as st
import random

# Say What? - SupportOps MVP Skeleton
# ==================================
# Streamlined version of the app code for better readability and structure

# Placeholder functions for simulation logic and narrative scenes
def simulate_support_action(action, department):
    # Simulated metrics for support actions (to be Replaced with real calculation logic)
    return {
        "Employees Affected": 42,
        "Penalty Risk ($)": 12500,
        "Revenue at Risk ($)": 50000,
        "Compliance Cliff": "🟠 ORANGE"
    }

def get_narrative_scene(scene_id):
    scenes = {
        1: {
            "ceo": "What in the world just happened...",
            "uncle_sam": "You forgot your 1099s? I didn’t."
        }
    }
    return scenes.get(scene_id, {"ceo": "...", "uncle_sam": "..."})

# Streamlit App Configuration
st.set_page_config(page_title="Say What? SupportOps", layout="wide")
st.title("Say What? — The App 🚀- SupportOps Simulation")

# Scene and Reactions
scene_key = 1  # Static for now; can later make it dynamic
story = get_narrative_scene(scene_key)
reactions = {
    1: {"ceo": "😵‍💫", "uncle_sam": "🧐"}
}.get(scene_key, {"ceo": "🤔", "uncle_sam": "🦅"})

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div style="border-radius: 10px; background-color: #f4e1d2; padding: 10px; box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.2);">
        <h4 style="color: #d94e45;">🧑‍💼 CEO says {reactions['ceo']}</h4>
        <p>{story["ceo"]}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="border-radius: 10px; background-color: #c8e6e8; padding: 10px; box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.2);">
        <h4 style="color: #3f91b5;">🦅 Uncle Sam says {reactions['uncle_sam']}</h4>
        <p>{story["uncle_sam"]}</p>
    </div>
    """, unsafe_allow_html=True)

# Sidebar Dropdown for Chaos Controls
st.sidebar.title("Disaster Controls 💥")
chaos_choice = st.sidebar.selectbox(
    "Choose Your Chaos:",
    ["Let Chaos Decide", "Missing 1099s", "Late Expense Reports", "Unfiled Property Tax", "Unleash Total Mayhem"]
)

# Handle Chaos Scenarios
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

# Sidebar: Input Module for Reality Check
st.sidebar.header("Reality Check Inputs 🛠️")
action = st.sidebar.selectbox(
    "Select Support Action",
    ["Run Payroll", "File 1099s", "Process Expense Reimbursements", "Vendor Payment", "File Census Forms"]
)
department = st.sidebar.selectbox("Select Department", ["Payroll", "Accounting", "HR", "Vendor Ops"])
simulate_button = st.sidebar.button("Simulate Action 🔄")

# Reality Check and Chaos Theater in Columns
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
        scene = get_narrative_scene(1)
        st.markdown(f"**CEO:** {scene['ceo']}")
        st.markdown(f"**Uncle Sam:** {scene['uncle_sam']}")
    else:
        st.markdown("_The story unfolds here once you simulate a scenario._")

# Footer / placeholders for future improvements
st.markdown("---")
st.markdown(
    "**Placeholders:**<br>"
    "`# TODO:` Add Compliance Cliff Counter logic<br>"
    "`# TODO:` Add multi-scene support and dynamic thresholds<br>"
    "`# TODO:` Hook into real penalty calculation functions",
    unsafe_allow_html=True
)

# Random CEO meltdown with a button
CEO_LINES = [
    "Wait—why are we bleeding money?!",
    "Did someone forget to tell me we needed paperwork?",
    "I thought “file taxes” meant “throw forms in a file drawer.”",
    "Why is there a dark cloud over my IPO?!",
    "Can we just pay with Bitcoin and call it a day?"
]

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


