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
    'married': [
        (0, 23850, 0.10),
        (23850, 96950, 0.12),
        (96950, 206700, 0.22),
        (206700, 394600, 0.24),
        (394600, 501050, 0.32),
        (501050, 751600, 0.35),
        (751600, float('inf'), 0.37),
    ],
    'hoh': [
        (0, 17000, 0.10),
        (17000, 64850, 0.12),
        (64850, 103350, 0.22),
        (103350, 197300, 0.24),
        (197300, 250500, 0.32),
        (250500, 626350, 0.35),
        (626350, float('inf'), 0.37),
    ],
}

STANDARD_DEDUCTION = {
    'single': 15000,
    'married': 30000,
    'hoh': 22500,
}

# SALT cap from OBBB
SALT_CAP = 40000

# HSA & FSA limits
HSA_LIMIT = {
    'self': 4300,
    'family': 8550,
}
FSA_LIMIT = 3300  # Medical FSA

# Retirement account deferral limits for 2025
RETIREMENT_LIMIT = 23500
CATCH_UP_LIMIT = 7500  # Age 50+

# QBI deduction thresholds
QBI_THRESHOLDS = {
    'single': 197300,
    'married': 394600,
}
