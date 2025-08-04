# 2025 Tax Constants

# Federal tax brackets: (lower_bound, upper_bound, rate)
FEDERAL_BRACKETS = {
    'single': [
        (0, 11925, 0.10),
        (11925, 48475, 0.12),
        (48475, 103350, 0.22),
        (103350, 197300, 0.24),
        (197300, 250525, 0.32),
        (250525, 626350, 0.35),
        (626350, float('inf'), 0.37),
    ],
    'married': [  # Married Filing Jointly
        (0, 23850, 0.10),
        (23850, 96950, 0.12),
        (96950, 206700, 0.22),
        (206700, 394600, 0.24),
        (394600, 501050, 0.32),
        (501050, 751600, 0.35),
        (751600, float('inf'), 0.37),
    ],
    'hoh': [  # Head of Household
        (0, 17000, 0.10),
        (17000, 64850, 0.12),
        (64850, 103350, 0.22),
        (103350, 197300, 0.24),
        (197300, 250500, 0.32),
        (250500, 626350, 0.35),
        (626350, float('inf'), 0.37),
    ],
    'married_sep': [  # Married Filing Separately
        (0, 11925, 0.10),
        (11925, 48475, 0.12),
        (48475, 103350, 0.22),
        (103350, 197300, 0.24),
        (197300, 250525, 0.32),
        (250525, 375800, 0.35),
        (375800, float('inf'), 0.37),
    ],
    'surviving_spouse': [  # Optional for completeness, same as MFJ
        (0, 23850, 0.10),
        (23850, 96950, 0.12),
        (96950, 206700, 0.22),
        (206700, 394600, 0.24),
        (394600, 501050, 0.32),
        (501050, 751600, 0.35),
        (751600, float('inf'), 0.37),
    ]
}

STANDARD_DEDUCTION = {
    'single': 15750,
    'married': 31500,
    'hoh': 23625,
    'married_sep': 15750,
    'surviving_spouse': 31500,
}

# Additional standard deduction for age 65+ or blind (per qualifying person)
EXTRA_STANDARD_DEDUCTION = {
    'single': 2000,
    'hoh': 2000,
    'married': 1600,           # per qualifying person (MFJ)
    'married_sep': 1600,       # per qualifying person (MFS)
    'surviving_spouse': 1600,  # per qualifying person
}

# SALT cap from OBBB (2025)
SALT_CAP = 40000

# HSA & FSA limits (2025)
HSA_LIMIT = {
    'self': 4300,
    'family': 8550,
}
FSA_LIMIT = 3300  # Medical FSA (2025, OBBB)

# Retirement account deferral limits for 2025
RETIREMENT_LIMIT = 23500   # 401(k), 403(b), etc. employee deferral
CATCH_UP_LIMIT = 7500      # Age 50+ catch-up

# IRA Limit
IRA_LIMIT = 7000  # Traditional or Roth (under age 50)

# QBI deduction thresholds (Section 199A)
QBI_THRESHOLDS = {
    'single': 197300,
    'married': 394600,
}
}
