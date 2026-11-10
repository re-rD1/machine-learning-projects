
import streamlit as st
import pandas as pd
import joblib

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Bank Marketing Prediction",
    page_icon="🏦",
    layout="wide"
)

# ==========================================
# 2. LOAD MODEL
# ==========================================

@st.cache_resource
def load_model():
    artifact = joblib.load("bank_marketing_model.joblib")
    return artifact

loaded_artifact = load_model()

model = loaded_artifact["model"]
threshold = loaded_artifact["threshold"]
features = loaded_artifact["features"]

# ==========================================
# 3. HEADER
# ==========================================

st.title("🏦 Bank Marketing Campaign Prediction")

st.markdown(
    """
    Predict the likelihood of a customer subscribing
    to a term deposit using Machine Learning.
    """
)

st.divider()

# ==========================================
# 4. MAIN LAYOUT
# ==========================================

col_form, col_info = st.columns([1.7, 1])

# ==========================================
# 5. CUSTOMER INPUT FORM
# ==========================================

with col_form:

    st.subheader("👤 Customer Information")

    st.caption(
        "Enter the customer's profile to generate a prediction."
    )

    with st.form("customer_form"):

        st.markdown("### Customer Profile")

        # Age
        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=30,
            help="Customer's age in years."
        )

        st.caption("Enter the customer's age in years.")

        # Job
        job = st.selectbox(
            "Job",
            [
                "admin.",
                "blue-collar",
                "entrepreneur",
                "housemaid",
                "management",
                "retired",
                "self-employed",
                "services",
                "student",
                "technician",
                "unemployed",
                "unknown"
            ],
            help="Select the customer's occupation."
        )

        # Balance
        balance = st.number_input(
            "Account Balance",
            value=1000,
            help="Average yearly balance in the customer's account."
        )

        # Housing
        housing = st.selectbox(
            "Housing Loan",
            ["yes", "no"],
            help="Does the customer have a housing loan?"
        )

        # Personal Loan
        loan = st.selectbox(
            "Personal Loan",
            ["yes", "no"],
            help="Does the customer have a personal loan?"
        )

        st.divider()

        st.markdown("### Previous Campaign Information")

        # Pdays
        pdays = st.number_input(
            "Days Since Previous Contact",
            min_value=-1,
            value=-1,
            help=(
                "Number of days since the customer was contacted "
                "in a previous campaign. Enter -1 if never contacted."
            )
        )

        st.caption(
            "💡 Use -1 if the customer has never been contacted "
            "in a previous campaign."
        )

        # Previous campaign outcome
        poutcome = st.selectbox(
            "Previous Campaign Outcome",
            ["unknown", "failure", "other", "success"],
            help="Outcome of the previous marketing campaign."
        )

        st.divider()

        # ==========================================
        # 6. AUTOMATIC FEATURE ENGINEERING
        # ==========================================

        # Age Group - Same binning as notebook
        if age <= 25:
            age_group = "Young Adult"
        elif age <= 35:
            age_group = "Adult"
        elif age <= 45:
            age_group = "Middle Adult"
        elif age <= 55:
            age_group = "Mature Adult"
        elif age <= 65:
            age_group = "Senior"
        else:
            age_group = "Elderly"

        # Previously Contacted
        previously_contacted = "no" if pdays == -1 else "yes"

        st.markdown("### Automatically Generated Features")

        st.info(
            f"""
            **Age Group:** {age_group}

            **Previously Contacted:** {previously_contacted}
            """
        )

        # Submit button
        submitted = st.form_submit_button(
            "🔍 Predict Subscription",
            use_container_width=True
        )

# ==========================================
# 7. MODEL INFORMATION
# ==========================================

with col_info:

    st.subheader("🤖 About This Model")

    st.info(
        """
        **Gradient Boosting Classifier**

        This model predicts whether a customer
        is likely to subscribe to a term deposit.
        """
    )

    st.metric(
        label="Decision Threshold",
        value=f"{threshold:.2f}"
    )

    st.metric(
        label="Number of Input Features",
        value=len(features)
    )

    st.divider()

    st.markdown("### How It Works")

    st.markdown(
        """
        1. Enter customer information.
        2. The model processes customer data.
        3. View the subscription prediction.
        """
    )

    st.divider()

    st.markdown("### Business Objective")

    st.write(
        """
        Help marketing teams prioritize potential
        customers before launching a marketing campaign.
        """
    )

    st.caption(
        "Machine Learning powered customer prediction."
    )


# ==========================================
# 8. PREDICTION PROCESS
# ==========================================

if submitted:

    # Create input DataFrame
    input_data = pd.DataFrame([{
        "age": age,
        "job": job,
        "balance": balance,
        "housing": housing,
        "loan": loan,
        "pdays": pdays,
        "poutcome": poutcome,
        "age_group": age_group,
        "previously_contacted": previously_contacted
    }])

    # Ensure feature order matches training
    input_data = input_data[features]

    # Predict probability
    probability = model.predict_proba(input_data)[0][1]

    # Apply decision threshold
    prediction = "yes" if probability >= threshold else "no"

    # Display result
    st.divider()
    st.header("Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Subscription Probability",
            f"{probability:.2%}"
        )

    with col2:
        st.metric(
            "Decision Threshold",
            f"{threshold:.2f}"
        )

    if prediction == "yes":
        st.success(
            "Prediction: YES - Customer is likely to subscribe."
        )
    else:
        st.warning(
            "Prediction: NO - Customer is less likely to subscribe."
        )