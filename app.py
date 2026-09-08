import streamlit as st
# Import the Profile class from your local module
from plan import FinancialProfile

# -----------------------------------------------------------------------------
# 1. Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Personal Financial Planning Dashboard",
    page_icon="💰",
    layout="wide"
)

st.markdown("""
    <style>
    /* ลดขนาด st.title */
    .main h1 {
        font-size: 3.1rem !important;
        font-weight: 700 !important;
        padding-bottom: 0.2rem !important;
    }
    /* ขยายขนาด st.caption */
    [data-testid="stCaptionContainer"] {
        font-size: 1.5rem !important;
        line-height: 1.5 !important;
    }
    
    /* ปรับขนาดตัวอักษรในกล่อง st.info / st.warning / st.error / st.success */
    div[data-testid="stAlert"] p {
        font-size: 1.4rem !important;
        font-weight: 500 !important;
        line-height: 1.6 !important;
    }
    /* ปรับขนาดตัวอักษรของ Bullet List ใน Alert Box */
    div[data-testid="stAlert"] ul li {
        font-size: 1.4rem !important;
        line-height: 1.7 !important;
    }
    
    /* ปรับขนาดหัวข้อ Calculation Parameters */
    div[data-testid="stAlert"] h4, 
    div[data-testid="stAlert"] p strong {
        font-size: 1.45rem !important;
    }
    
    div[data-testid="stTabs"] button {
        padding: 0.8rem 1 rem !important;
    }

    /* ปรับขนาดตัวอักษรของชื่อ Tab โดยเฉพาะ */
    div[data-testid="stTabs"] button div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stTabs"] button p {
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        line-height: 1.5 !important;
    }
/* 1. ดันแถบ Tabs ขึ้นไปชิดเส้น divider ด้านบน */
    div[data-testid="stTabs"] {
        margin-top: -1 rem !important;
    }

    /* 2. ดึงเนื้อหาภายใน Tab ขึ้นมาชิดปุ่ม Tab Header */
    div[data-testid="stTabPanel"] {
        padding-top: 0rem !important;
        margin-top: -0.5 rem !important;
    }

    /* 3. ลบ Margin บนสุดของหัวข้อภายใน Tab */
    div[data-testid="stTabPanel"] h1,
    div[data-testid="stTabPanel"] h2,
    div[data-testid="stTabPanel"] h3 {
        margin-top: 0.2rem !important;
        padding-top: 0rem !important;
    }

    /* 4. ลดขนาดระยะห่างของ st.divider() */
    hr {
        margin-top: 0.8rem !important;
        margin-bottom: 0.8rem !important;
    }
    /* 1. เจาะจง st.metric label ทุกชั้น */
    div[data-testid="stMetricLabel"],
    div[data-testid="stMetricLabel"] *,
    div[data-testid="stMetricLabel"] p {
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        color: #ffffff !important;
    }

    /* 2. ดักจับกรณีเขียนเป็น Markdown หรือ Caption ซ้อนอยู่เหนือตัวเลข */
    div[data-testid="stMetric"] label,
    div[data-testid="stMetric"] label * {
        font-size: 1.3rem !important;
        font-weight: 700 !important;
    }
    /* 1. ขยายขนาดข้อความ Saving Ratio / Debt Ratio */
    div[data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem !important;
        line-height: 1.6 !important;
    }

    /* 2. ขยายขนาดตัวเลขในกล่องโค้ดไฮไลต์ (`36.65%`) */
    div[data-testid="stMarkdownContainer"] code {
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        padding: 0.2rem 0.5rem !important;
    }

    </style>
""", unsafe_allow_html=True)

st.title("💰 Personal Financial Planning Dashboard")
st.caption("Calculate tax liabilities, assess liquidity health, estimate retirement funds, and project investment growth.")

# -----------------------------------------------------------------------------
# 2. Sidebar Input Section
# -----------------------------------------------------------------------------
st.sidebar.header("👤 1. Personal Information")
name = st.sidebar.text_input("First Name", "Somchai")
surname = st.sidebar.text_input("Last Name", "Prosperous")
age = st.sidebar.number_input("Current Age", min_value=18, max_value=80, value=28)

st.sidebar.divider()

st.sidebar.header("💵 2. Monthly Financial Data")
salary = st.sidebar.number_input("Monthly Salary (THB)", min_value=0, value=50000, step=1000)
fix_expense = st.sidebar.number_input("Fixed Expenses (THB/month)", min_value=0, value=15000, step=500)
vary_expense = st.sidebar.number_input("Variable Expenses (THB/month)", min_value=0, value=10000, step=500)
debt_pay = st.sidebar.number_input("Debt Payments (THB/month)", min_value=0, value=5000, step=500)

st.sidebar.divider()

st.sidebar.header("🏖️ 3. Retirement Goals")
retire_age = st.sidebar.number_input("Target Retirement Age", min_value=age+1, max_value=90, value=60)
life_age = st.sidebar.number_input("Expected Life Expectancy", min_value=retire_age+1, max_value=120, value=85)
monthly_cost = st.sidebar.number_input("Post-Retirement Expenses (THB/month)", min_value=0, value=20000, step=1000)
st.sidebar.header("📈 4. Investment Strategy")
customize_allocation = st.sidebar.checkbox("Custom Asset Allocation", value=False)

if customize_allocation:
    low_risk_ratio = st.sidebar.number_input(
        "Low Risk Asset Ratio (%) (1.5% Expected Annual Return)", 
        min_value=0.0, max_value=100.0, value=20.0, step=5.0
    )

    mid_risk_ratio = st.sidebar.number_input(
        "Medium Risk Asset Ratio (%) (5% Expected Annual Return)", 
        min_value=0.0, max_value=100.0, value=30.0, step=5.0
    )

    high_risk_ratio = st.sidebar.number_input(
        "High Risk Asset Ratio (%) (10% Expected Annual Return)", 
        min_value=0.0, max_value=100.0, value=40.0, step=5.0
    )

    veryhigh_risk_ratio = st.sidebar.number_input(
        "Alternative Asset Ratio (%) (25% Expected Annual Return)", 
        min_value=0.0, max_value=100.0, value=10.0, step=5.0
    )
        
    total_alloc = low_risk_ratio + mid_risk_ratio + high_risk_ratio + veryhigh_risk_ratio
    
    total_alloc = low_risk_ratio + mid_risk_ratio + high_risk_ratio
    if total_alloc != 100.0:
        st.sidebar.warning(f"⚠️ Total Allocation: **{total_alloc:.1f}%** (Must sum to 100%)")

st.sidebar.divider()

btn_calculate = st.sidebar.button("🚀 Process Financial Plan", type="primary", use_container_width=True)

@st.dialog("⚠️ Input Error")
def show_error_dialog(error_message):
    st.error(error_message)
    st.write("Please check your input values in the sidebar and try again.")
    if st.button("Close"):
        st.rerun()

# -----------------------------------------------------------------------------
# 3. Main Display Panel
# -----------------------------------------------------------------------------
if btn_calculate:
    try:
        # Initialize and execute calculations via the Profile instance
        user = FinancialProfile(name, surname, age)
        user.get_finance_info(salary, fix_expense, vary_expense, debt_pay)
        user.get_retire_goal(retire_age, life_age, monthly_cost)
        
        if customize_allocation:
            invest_plan = [low_risk_ratio, mid_risk_ratio, high_risk_ratio, veryhigh_risk_ratio]
            user.get_invest_plan(invest_plan)
        else:
            user.get_invest_plan() # Automatically assigns asset allocation based on age
        user.create_plan()
        
        # Retrieve structured data via get_result()
        data = user.get_result()
        res = data["results"]
        prof = data["profile"]

        # Header summary
        st.subheader(f"📊 Financial Summary for {prof['full_name']} (Age {prof['age']})")
        st.markdown("---")

        # Organize outputs into 4 distinct tabs
        tab_tax, tab_liq, tab_ret, tab_inv = st.tabs([
            "🧾 Tax Planning", 
            "💧 Liquidity Health", 
            "🏖️ Retirement Fund", 
            "📈 Investment Strategy"
        ])

        # -------------------------------------------------------------------------
        # TAB 1: Tax Planning
        # -------------------------------------------------------------------------
        with tab_tax:
            tax_data = res.get("Tax Planning", {})
            st.header("🧾 Annual Personal Income Tax Estimation")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Annual Income", f"฿{tax_data['annual_income']:,.2f}")
            c2.metric("Total Tax Deductions", f"฿{tax_data['total_deduction']:,.2f}")
            c3.metric("Net Taxable Income", f"฿{tax_data['net_taxable_income']:,.2f}")
            
            st.divider()
            st.subheader("💰 Tax Payable")
            st.success(f"Estimated tax liability for this year: **฿{tax_data['tax_payable']:,.2f} THB**")

        # -------------------------------------------------------------------------
        # TAB 2: Liquidity Health
        # -------------------------------------------------------------------------
        with tab_liq:
            liq_data = res.get("Liquidity Health", {})
            st.header("💧 Financial Liquidity Assessment")
            
            c1, c2 = st.columns(2)
            c1.metric("Net Monthly Savings", f"฿{liq_data['saving']:,.2f}")
            c2.metric("Recommended Emergency Fund (6 Months)", f"฿{liq_data['reserve_fund']:,.2f}")

            st.divider()
            st.subheader("🎯 Ratio Analysis & Feedback")
            
            # Savings Ratio Assessment
            saving_info = liq_data["saving_analysis"]
            st.markdown(f"**Saving Ratio:** `{saving_info['ratio']:.2f}%`")
            
            if saving_info["status"] == "error":
                st.error(f"🔴 {saving_info['message']}")
            elif saving_info["status"] == "warning":
                st.warning(f"🟡 {saving_info['message']}")
            elif saving_info["status"] == "info":
                st.info(f"🔵 {saving_info['message']}")
            else:
                st.success(f"🟢 {saving_info['message']}")


            # Debt Ratio Assessment
            debt_info = liq_data["debt_analysis"]
            st.markdown(f"**Debt Ratio:** `{debt_info['ratio']:.2f}%`")
            if debt_info["status"] == "error":
                st.error(f"🔴 {debt_info['message']}")
            elif debt_info["status"] == "warning":
                st.warning(f"🟡 {debt_info['message']}")
            elif debt_info["status"] == "info":
                st.info(f"🔵 {debt_info['message']}")
            else:
                st.success(f"🟢 {debt_info['message']}")

        # -------------------------------------------------------------------------
        # TAB 3: Retirement Fund
        # -------------------------------------------------------------------------
        with tab_ret:
            ret_data = res.get("Retire Fund", {})
            st.header("🏖️ Retirement Capital Requirement")
            
            st.metric("Target Retirement Fund Needed", f"฿{ret_data['retire_fund']:,.2f}")
            
            st.info(
                f"📌 **Calculation Parameters:**\n"
                f"- Planned Retirement Age: **{ret_data['retire_age']} years old**\n"
                f"- Retirement Duration: **{ret_data['retire_duration']} years**\n"
                f"- Monthly Post-Retirement Budget: **{ret_data['monthly_cost']:,.2f} THB/month** (Adjusted for inflation)"
            )

        # -------------------------------------------------------------------------
        # TAB 4: Investment Strategy
        # -------------------------------------------------------------------------
        with tab_inv:
            inv_data = res.get("Investment", {})
            st.header("📈 Portfolio Growth Projection")
            
            c1, c2 = st.columns(2)
            c1.metric("Annual Investment Amount", f"฿{inv_data['annual_investment']:,.2f}")
            c2.metric("Projected Portfolio Value at Retirement", f"฿{inv_data['projected_total']:,.2f}")

            st.divider()
            st.subheader("🏁 Goal Feasibility Evaluation")
            
            if inv_data["is_sufficient"]:
                st.success(f"🎉 **On Track:** {inv_data['status_message']}")
            else:
                st.warning(f"⚠️ **Adjustment Needed:** {inv_data['status_message']}")
    except ValueError as e:
        # เมื่อเกิด ValueError ให้เรียกแสดง Pop-up Modal ทันที
        show_error_dialog(str(e))

else:
    # Initial prompt displayed before processing
    st.info("👈 Please enter your financial details in the sidebar menu and click **'Process Financial Plan'** to generate the report.")