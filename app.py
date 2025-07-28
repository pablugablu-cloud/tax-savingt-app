import streamlit as st
import pandas as pd
from tax_data import FEDERAL_BRACKETS, STANDARD_DEDUCTION, SALT_CAP, HSA_LIMIT, FSA_LIMIT, RETIREMENT_LIMIT, CATCH_UP_LIMIT, QBI_THRESHOLDS

st.set_page_config(page_title='2025 Tax Savings Calculator', layout='wide')

st.title('2025 Tax Savings Calculator')

# Side inputs
st.sidebar.header('Client Information')
filing = st.sidebar.selectbox('Filing Status', ['single', 'married', 'hoh'], format_func=lambda x: x.capitalize())
w2_income = st.sidebar.number_input('W-2 Income', min_value=0.0, step=1000.0, value=0.0)
business_income = st.sidebar.number_input('Self-Employment Profit', min_value=0.0, step=1000.0, value=0.0)
deferred_income = st.sidebar.number_input('Income Deferred (Deferment)', min_value=0.0, step=1000.0, value=0.0)

st.sidebar.header('Contributions & Deductions')
hsa_type = st.sidebar.selectbox('HSA Plan Type', ['self', 'family'])
hsa_amt = st.sidebar.number_input('HSA Contribution', min_value=0.0, step=100.0, value=0.0)
fsa_amt = st.sidebar.number_input('Medical FSA Contribution', min_value=0.0, step=100.0, value=0.0)
retirement_amt = st.sidebar.number_input('401(k) Contribution', min_value=0.0, step=500.0, value=0.0)
salt_paid = st.sidebar.number_input('State & Local Tax Paid', min_value=0.0, step=500.0, value=0.0)

# Cap SALT
salt_ded = min(salt_paid, SALT_CAP)

# Tax calculation function
def calc_tax(income, brackets):
    tax = 0.0
    for low, high, rate in brackets:
        if income > low:
            taxable = min(income, high) - low
            tax += taxable * rate
        else:
            break
    return tax

# Baseline taxable income
baseline_ti = w2_income + business_income - STANDARD_DEDUCTION[filing]
baseline_ti = max(baseline_ti, 0)
baseline_tax = calc_tax(baseline_ti, FEDERAL_BRACKETS[filing])

# Strategies
strategies = []

# HSA
hsa_ded = min(hsa_amt, HSA_LIMIT[hsa_type])
ti_hsa = max(w2_income + business_income - hsa_ded - STANDARD_DEDUCTION[filing], 0)
tax_hsa = calc_tax(ti_hsa, FEDERAL_BRACKETS[filing])
strategies.append({
    'Strategy': 'HSA Contribution',
    'Savings': baseline_tax - tax_hsa,
    'Details': f'Contribute up to ${HSA_LIMIT[hsa_type]:,} to HSA.',
})

# FSA
fsa_ded = min(fsa_amt, FSA_LIMIT)
ti_fsa = max(w2_income + business_income - fsa_ded - STANDARD_DEDUCTION[filing], 0)
tax_fsa = calc_tax(ti_fsa, FEDERAL_BRACKETS[filing])
strategies.append({
    'Strategy': 'Medical FSA Contribution',
    'Savings': baseline_tax - tax_fsa,
    'Details': f'Contribute up to ${FSA_LIMIT:,} to FSA.',
})

# 401(k)
ret_ded = min(retirement_amt, RETIREMENT_LIMIT + CATCH_UP_LIMIT)
ti_ret = max(w2_income + business_income - ret_ded - STANDARD_DEDUCTION[filing], 0)
tax_ret = calc_tax(ti_ret, FEDERAL_BRACKETS[filing])
strategies.append({
    'Strategy': '401(k) Contribution',
    'Savings': baseline_tax - tax_ret,
    'Details': f'Contribute up to ${RETIREMENT_LIMIT:,} (+${CATCH_UP_LIMIT:,} if age 50+).',
})

# Income Deferment
ti_def = max(w2_income + business_income - deferred_income - STANDARD_DEDUCTION[filing], 0)
tax_def = calc_tax(ti_def, FEDERAL_BRACKETS[filing])
strategies.append({
    'Strategy': 'Income Deferment',
    'Savings': baseline_tax - tax_def,
    'Details': 'Defer billing/invoicing to next year.',
})

# QBI Deduction
qbi_ded = 0.0
if business_income > 0 and (w2_income + business_income) <= QBI_THRESHOLDS[filing]:
    qbi_ded = 0.2 * business_income
ti_qbi = max(w2_income + business_income - qbi_ded - STANDARD_DEDUCTION[filing], 0)
tax_qbi = calc_tax(ti_qbi, FEDERAL_BRACKETS[filing])
strategies.append({
    'Strategy': 'Qualified Business Income',
    'Savings': baseline_tax - tax_qbi,
    'Details': '20% deduction on pass-through business income (subject to thresholds).',
})

# SALT cap
ti_salt = max(w2_income + business_income - salt_ded - STANDARD_DEDUCTION[filing], 0)
tax_salt = calc_tax(ti_salt, FEDERAL_BRACKETS[filing])
strategies.append({
    'Strategy': 'SALT Deduction',
    'Savings': baseline_tax - tax_salt,
    'Details': f'Deduct up to ${SALT_CAP:,} SALT paid.',
})

# Display results
df = pd.DataFrame(strategies)
df['Savings'] = df['Savings'].apply(lambda x: round(x, 2))
st.subheader('Tax Savings by Strategy')
st.dataframe(df.sort_values(by='Savings', ascending=False), use_container_width=True)

# Download button
csv = df.to_csv(index=False)
st.download_button('Download Savings CSV', csv, 'tax_savings.csv', 'text/csv')
