
import streamlit as st

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

