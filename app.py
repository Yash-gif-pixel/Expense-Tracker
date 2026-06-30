# =============================================================================
# EXPENSE TRACKER — Modern Dashboard UI
# =============================================================================
# Run this app with:
#   C:/Users/yashm/AppData/Local/Python/pythoncore-3.14-64/python.exe -m streamlit run app.py
# Or navigate to the folder and run:
#   cd C:\Python\expense_tracker
#   streamlit run app.py
# =============================================================================

import streamlit as st

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================
# st.set_page_config() must be the FIRST Streamlit command in the script.
# It sets the browser tab title, icon, and layout width.
# "wide" layout uses the full browser width instead of a narrow centered column.
st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)


# =============================================================================
# CUSTOM CSS STYLES
# =============================================================================
# We inject custom CSS into the page using st.markdown() with unsafe_allow_html=True.
# This lets us override Streamlit's default styling to create a modern dashboard look.
#
# HTML EXPLAINED:
#   <style> ... </style>  — The <style> tag tells the browser that everything inside
#                           it is CSS (styling rules), not regular text content.
#
# CSS CONCEPTS USED:
#   @import url(...)      — Loads the "Inter" font from Google Fonts so we can use
#                           a modern, clean typeface instead of the browser default.
#   .stApp                — Targets the main Streamlit app container to set the
#                           background color for the entire page.
#   .metric-card          — A custom class we created for the stat cards at the top.
#   border-radius         — Rounds the corners of an element (e.g., 16px = nicely rounded).
#   box-shadow            — Adds a shadow beneath an element to make it look "elevated"
#                           above the background, like a physical card on a table.
#   background: linear-gradient(...) — Creates a smooth color transition (gradient)
#                           from one color to another. Used for accent bars on cards.
#   padding               — The space INSIDE an element, between its border and content.
#   margin                — The space OUTSIDE an element, between it and other elements.
#   transition            — Makes property changes animate smoothly (e.g., hover effects
#                           take 0.3 seconds instead of being instant).
#   transform: translateY — Moves an element up or down. Used for a subtle "lift" on hover.
#   rgba(r, g, b, a)      — A color with transparency. The 'a' value (0 to 1) controls
#                           how see-through the color is. 0 = invisible, 1 = solid.
# =============================================================================

st.markdown("""
<style>
    /* --- FONT --- */
    /* Load the "Inter" font from Google Fonts. It's a clean, modern sans-serif font
       commonly used in dashboards and tech interfaces. */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Apply the Inter font to ALL elements on the page.
       The * selector means "every element". */
    * {
        font-family: 'Inter', sans-serif;
    }

    /* --- MAIN BACKGROUND --- */
    /* .stApp is the root container Streamlit uses for the entire app.
       We set a very dark blue-gray background for the dashboard look. */
    .stApp {
        background-color: #0e1117;
    }

    /* --- DASHBOARD HEADER --- */
    /* A custom HTML block we'll create for the app title area. */
    .dashboard-header {
        text-align: center;           /* Center all text inside this div */
        padding: 2rem 0 1rem 0;      /* top right bottom left spacing */
        margin-bottom: 1rem;
    }
    .dashboard-header h1 {
        color: #ffffff;
        font-size: 2.4rem;
        font-weight: 700;            /* Bold weight */
        margin-bottom: 0.3rem;
    }
    .dashboard-header p {
        color: #8b949e;              /* Muted gray for subtitle */
        font-size: 1.05rem;
        font-weight: 300;            /* Light weight */
    }
    /* The gradient accent line below the header.
       It uses a linear-gradient that transitions through purple, blue, and teal. */
    .header-accent {
        height: 3px;
        background: linear-gradient(90deg, #7c3aed, #3b82f6, #06b6d4);
        border-radius: 2px;
        margin: 0.5rem auto;
        width: 60%;                  /* Only spans 60% of the page width */
    }

    /* --- METRIC CARDS --- */
    /* These are the stat boxes at the top showing Total Expense and Expense Count.
       They have a dark background, rounded corners, and a gradient top border. */
    .metric-card {
        background: #161b22;         /* Dark card background */
        border-radius: 16px;         /* Rounded corners */
        padding: 1.5rem;
        text-align: center;
        border: 1px solid #21262d;   /* Subtle border */
        /* box-shadow creates the "floating card" effect.
           Format: x-offset  y-offset  blur-radius  spread  color */
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        /* transition makes the hover animation smooth over 0.3 seconds */
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;          /* Needed so the ::before pseudo-element positions correctly */
        overflow: hidden;            /* Hides the gradient bar if it extends beyond the card */
    }
    /* ::before is a "pseudo-element" — it creates a decorative element BEFORE the
       card's content. We use it for the gradient accent bar at the top of each card. */
    .metric-card::before {
        content: '';                  /* Required for pseudo-elements (even if empty) */
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;                 /* Thin gradient bar */
        background: linear-gradient(90deg, #7c3aed, #3b82f6);
    }
    /* :hover triggers when the user moves their mouse over the card. */
    .metric-card:hover {
        transform: translateY(-4px); /* Moves the card up 4px for a "lift" effect */
        box-shadow: 0 8px 30px rgba(124, 58, 237, 0.2);  /* Purple-tinted shadow */
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0.5rem 0;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #8b949e;              /* Muted gray */
        font-weight: 500;
        text-transform: uppercase;   /* Makes text ALL CAPS */
        letter-spacing: 1px;         /* Adds space between letters for readability */
    }

    /* --- SECTION CARDS --- */
    /* Reusable card style for each dashboard section (Add, Edit, Delete, etc.) */
    .section-card {
        background: #161b22;
        border-radius: 16px;
        padding: 1.8rem;
        border: 1px solid #21262d;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
        margin-bottom: 1.5rem;
    }
    .section-title {
        color: #ffffff;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;               /* Flexbox lays out children in a row */
        align-items: center;         /* Vertically centers the icon and text */
        gap: 0.5rem;                 /* Space between the icon and the text */
    }

    /* --- CATEGORY BADGE --- */
    /* Small colored pills used in the Category Totals section. */
    .category-badge {
        display: inline-block;
        background: linear-gradient(135deg, #7c3aed22, #3b82f622);
        color: #c9d1d9;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        margin: 0.3rem;
        font-size: 0.9rem;
        border: 1px solid #30363d;
        transition: transform 0.2s ease;
    }
    .category-badge:hover {
        transform: scale(1.05);      /* Slightly enlarges on hover */
    }
    .category-amount {
        font-weight: 700;
        color: #7c3aed;             /* Purple highlight for the amount */
    }

    /* --- STREAMLIT WIDGET OVERRIDES --- */
    /* Override Streamlit's default input field styling to match our dark theme. */

    /* Target ALL input elements on the page so the dark theme applies
       regardless of Streamlit's internal class names (which can change
       between versions). */
    input[type="text"],
    input[type="number"] {
        background-color: #0d1117 !important;
        color: #c9d1d9 !important;
        border: 1px solid #30363d !important;
        border-radius: 10px !important;
        padding: 0.6rem 1rem !important;
    }
    /* Focus state — when the user clicks into an input field */
    input[type="text"]:focus,
    input[type="number"]:focus {
        border-color: #7c3aed !important;    /* Purple border when focused */
        box-shadow: 0 0 0 2px rgba(124, 58, 237, 0.2) !important;
    }

    /* Labels above input fields */
    label {
        color: #8b949e !important;
        font-weight: 500 !important;
    }

    /* --- BUTTON STYLING --- */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #3b82f6) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
        letter-spacing: 0.5px !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(124, 58, 237, 0.4) !important;
    }
    /* Active/clicked state */
    .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* --- DATAFRAME / TABLE STYLING --- */
    /* Make the Streamlit dataframe blend with our dark theme */
    .stDataFrame {
        border-radius: 12px !important;
        overflow: hidden !important;
    }

    /* --- DIVIDER --- */
    /* Streamlit's st.divider() creates an <hr> element. We style it to be subtle. */
    hr {
        border-color: #21262d !important;
        margin: 1.5rem 0 !important;
    }

    /* --- SUCCESS / ERROR MESSAGES --- */
    /* Streamlit shows these when you call st.success() or st.error().
       We round the corners and adjust the style. */
    .stAlert {
        border-radius: 10px !important;
    }

    /* --- HIDE DEFAULT STREAMLIT ELEMENTS --- */
    /* Hide the hamburger menu and "Made with Streamlit" footer for a cleaner look. */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* --- EXPENSE TABLE ROW --- */
    /* Custom styled rows for displaying expenses in a custom HTML table. */
    .expense-row {
        display: flex;
        justify-content: space-between;   /* Pushes items to opposite ends */
        align-items: center;
        padding: 0.8rem 1rem;
        background: #0d1117;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        border: 1px solid #21262d;
        transition: border-color 0.2s ease;
    }
    .expense-row:hover {
        border-color: #7c3aed;           /* Purple border on hover */
    }
    .expense-index {
        color: #484f58;
        font-size: 0.8rem;
        font-weight: 600;
        min-width: 30px;
    }
    .expense-category {
        color: #c9d1d9;
        font-weight: 500;
        flex: 1;                          /* Takes up remaining space */
        margin-left: 1rem;
    }
    .expense-amount {
        color: #7c3aed;
        font-weight: 700;
        font-size: 1.05rem;
    }
</style>
""", unsafe_allow_html=True)
# HTML EXPLAINED:
#   unsafe_allow_html=True — By default, Streamlit strips HTML tags for security.
#   This flag tells Streamlit "I know what I'm doing, allow my HTML/CSS."
#   We need this because we're injecting custom <style> and <div> elements.


# =============================================================================
# DATA FUNCTIONS (unchanged from original)
# =============================================================================
# These three functions handle reading and writing expenses to the text file.
# The data format in expenses.txt is: Category-Amount (one per line).

# This function APPENDS a single new expense to the end of the file.
def save_expense(category, amount):
    file = open("expenses.txt", "a")          # "a" = append mode (adds to end)
    file.write(category + "-" + str(amount) + "\n")
    file.close()


# This function READS all expenses from the file and returns them as a list
# of dictionaries, plus the total amount.
def load_expenses():
    total = 0
    expenses = []

    try:
        file = open("expenses.txt", "r")      # "r" = read mode
    except FileNotFoundError:
        # If the file doesn't exist yet, return empty data
        return expenses, total

    for line in file:
        line = line.strip()                    # Remove whitespace/newlines

        if line == "":
            continue                           # Skip empty lines
        if "-" not in line:
            continue                           # Skip malformed lines

        category, amount = line.rsplit("-", 1) # Split from the RIGHT side once

        category = category.strip().title()    # Capitalize each word
        amount = amount.strip()

        try:
            amount = int(amount)               # Convert string to integer
        except ValueError:
            continue                           # Skip if amount isn't a number

        expense = {
            "category": category,
            "amount": amount
        }
        expenses.append(expense)
        total = total + amount

    file.close()
    return expenses, total


# This function OVERWRITES the entire file with the current list of expenses.
# Used after editing or deleting an expense.
def save_all_expenses(expenses):
    file = open("expenses.txt", "w")           # "w" = write mode (replaces everything)

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        file.write(category + "-" + str(amount) + "\n")

    file.close()


# =============================================================================
# LOAD DATA
# =============================================================================
# Load expenses FIRST, before building any UI, so we can display metrics.
expenses, total = load_expenses()


# =============================================================================
# HEADER
# =============================================================================
# HTML EXPLAINED:
#   <div class="dashboard-header"> — A <div> is a container element. The class
#   attribute links it to our CSS rules above so it gets styled.
#   <h1> is the largest heading tag. <p> is a paragraph of text.
st.markdown("""
<div class="dashboard-header">
    <h1>💰 Expense Tracker</h1>
    <p>Track, manage, and analyze your spending</p>
    <div class="header-accent"></div>
</div>
""", unsafe_allow_html=True)


# =============================================================================
# METRIC CARDS (Total Expense + Expense Count)
# =============================================================================
# We use st.columns(2) to create two equal-width columns side by side.
# Inside each column, we place a custom HTML metric card.

metric_col1, metric_col2 = st.columns(2)

with metric_col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Expenses</div>
        <div class="metric-value">₹{total:,}</div>
    </div>
    """, unsafe_allow_html=True)
    # f-string: The f before the string lets us embed Python variables inside {}.
    # {:,} adds comma separators to large numbers (e.g., 1,200 instead of 1200).

with metric_col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Number of Expenses</div>
        <div class="metric-value">{len(expenses)}</div>
    </div>
    """, unsafe_allow_html=True)
    # len(expenses) returns how many items are in the expenses list.

st.markdown("<br>", unsafe_allow_html=True)   # Adds vertical spacing


# =============================================================================
# ADD EXPENSE SECTION
# =============================================================================
st.markdown("""
<div class="section-title">➕ Add New Expense</div>
""", unsafe_allow_html=True)

# Create a card-like container using st.container()
with st.container():
    add_col1, add_col2 = st.columns(2)

    with add_col1:
        amount = st.number_input(
            "Amount (₹)",
            min_value=0,
            key="add_amount"
        )

    with add_col2:
        category = st.text_input(
            "Category",
            placeholder="e.g., Food, Travel, Shopping",
            key="add_category"
        ).title()       # .title() capitalizes the first letter of each word

    if st.button("💾  Add Expense", key="add_btn", use_container_width=True):
        # Validation: check that category is not empty and amount is positive
        if category == "":
            st.error("⚠️ Category cannot be empty")
        elif amount <= 0:
            st.error("⚠️ Amount must be greater than 0")
        else:
            save_expense(category, amount)
            st.success("✅ Expense added successfully!")
            st.rerun()   # Refresh the page to show updated data

st.divider()  # Horizontal line separator


# =============================================================================
# EXPENSES TABLE (always visible)
# =============================================================================
st.markdown("""
<div class="section-title">📋 All Expenses</div>
""", unsafe_allow_html=True)

if len(expenses) == 0:
    # Show a friendly message if there are no expenses yet
    st.info("No expenses recorded yet. Add your first expense above! 👆")
else:
    # Build custom HTML rows for each expense.
    # This gives us full control over the styling (unlike st.table).
    #
    # HTML EXPLAINED:
    #   We loop through the expenses list and create one <div class="expense-row">
    #   for each expense. Inside each row are three <span> elements for the index,
    #   category name, and amount. <span> is an inline container (doesn't start
    #   a new line, unlike <div>).
    row_items = []
    for index, expense in enumerate(expenses):
        formatted_amt = f"{expense['amount']:,}"
        row_items.append(
            '<div class="expense-row">'
            + '<span class="expense-index">#' + str(index) + '</span>'
            + '<span class="expense-category">' + expense['category'] + '</span>'
            + '<span class="expense-amount">₹' + formatted_amt + '</span>'
            + '</div>'
        )
    rows_html = ''.join(row_items)
    # enumerate(expenses) gives us both the index (0, 1, 2...) and the expense
    # dictionary on each loop iteration.

    st.markdown(rows_html, unsafe_allow_html=True)

st.divider()


# =============================================================================
# CATEGORY TOTALS (always visible)
# =============================================================================
st.markdown("""
<div class="section-title">📊 Category Breakdown</div>
""", unsafe_allow_html=True)

if len(expenses) == 0:
    st.info("No categories to display yet.")
else:
    # Calculate totals per category using a dictionary.
    # If the category already exists as a key, add to it; otherwise create it.
    category_totals = {}

    for expense in expenses:
        cat = expense["category"]
        amt = expense["amount"]

        if cat in category_totals:
            category_totals[cat] += amt    # Add to existing total
        else:
            category_totals[cat] = amt     # Create new entry

    # Build the category badges as HTML.
    # We build each badge as a single-line string to avoid Streamlit's HTML
    # sanitizer breaking multi-line nested HTML tags.
    badge_items = []
    for cat, amt in category_totals.items():
        formatted_amt = f"{amt:,}"
        badge_items.append(
            '<div class="category-badge">'
            + cat + ': <span class="category-amount">₹' + formatted_amt + '</span>'
            + '</div>'
        )
    badges_html = '<div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">' + ''.join(badge_items) + '</div>'
    # CSS EXPLAINED:
    #   display: flex    — Lays out children in a row (or wraps to next line)
    #   flex-wrap: wrap  — If badges don't fit in one row, they wrap to the next
    #   gap: 0.5rem     — Space between each badge

    st.markdown(badges_html, unsafe_allow_html=True)

st.divider()


# =============================================================================
# EDIT & DELETE SECTION (side by side)
# =============================================================================
st.markdown("""
<div class="section-title">⚙️ Manage Expenses</div>
""", unsafe_allow_html=True)

edit_col, delete_col = st.columns(2)

# --- EDIT EXPENSE ---
with edit_col:
    st.markdown("""
    <div class="section-card">
        <div class="section-title">✏️ Edit Expense</div>
    </div>
    """, unsafe_allow_html=True)

    edit_index = st.number_input(
        "Expense index to edit",
        min_value=0,
        step=1,
        key="edit_index"
    )

    new_category = st.text_input(
        "New category",
        placeholder="Enter new category name",
        key="edit_category"
    ).title()

    new_amount = st.number_input(
        "New amount (₹)",
        min_value=0,
        key="edit_amount"
    )

    if st.button("✏️  Save Changes", key="edit_btn", use_container_width=True):
        if edit_index < len(expenses):
            expenses[edit_index]["category"] = new_category
            expenses[edit_index]["amount"] = new_amount
            save_all_expenses(expenses)
            st.success("✅ Expense updated!")
            st.rerun()
        else:
            st.error("⚠️ Invalid index — no expense found at that position")

# --- DELETE EXPENSE ---
with delete_col:
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🗑️ Delete Expense</div>
    </div>
    """, unsafe_allow_html=True)

    delete_index = st.number_input(
        "Expense index to delete",
        min_value=0,
        step=1,
        key="delete_index"
    )

    # Add some vertical space so the Delete button aligns with the Edit button.
    # We use empty markdown lines as spacers.
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    if st.button("🗑️  Delete Expense", key="delete_btn", use_container_width=True):
        if delete_index < len(expenses):
            del expenses[delete_index]
            save_all_expenses(expenses)
            st.success("✅ Expense deleted!")
            st.rerun()
        else:
            st.error("⚠️ Invalid index — no expense found at that position")


# =============================================================================
# FOOTER
# =============================================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #484f58; font-size: 0.85rem; padding: 1rem 0;">
    Built with 💜 using Python & Streamlit
</div>
""", unsafe_allow_html=True)