# Expense Tracker — UI Redesign Report

**Date:** June 9, 2026  
**Project:** Personal Expense Tracker  
**Tech Stack:** Python, Streamlit, Text File Storage  
**File Modified:** `app.py`

---

## 1. Overview

The Expense Tracker application was redesigned with a modern, professional dashboard UI. All existing functionality (Add, View, Edit, Delete, Total, Category Totals) was preserved. The changes are purely visual and organizational — no changes were made to the data storage format (`expenses.txt`) or the core logic.

---

## 2. What Was Changed

### 2.1 Page Configuration

**Before:** No page config was set. The app used Streamlit's default narrow layout with a generic browser tab title.

**After:** Added `st.set_page_config()` as the first command:
- Browser tab title: "Expense Tracker"
- Browser tab icon: 💰
- Layout: `wide` (uses full browser width)

**Why:** A descriptive title and icon make the app feel polished. Wide layout gives more room for side-by-side columns and cards.

---

### 2.2 Custom CSS Injection

A large block of custom CSS was injected into the page using `st.markdown()` with `unsafe_allow_html=True`. This is the core of the visual redesign.

#### 2.2.1 Dark Theme Background

```css
.stApp {
    background-color: #0e1117;
}
```

- `.stApp` is the root container Streamlit uses for the entire page.
- `#0e1117` is a very dark blue-gray color.
- **Why:** Dark themes reduce eye strain, look modern, and make colored elements (like gradient accents) pop visually.

#### 2.2.2 Google Font (Inter)

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Inter', sans-serif;
}
```

- `@import url(...)` loads the "Inter" font from Google's free font service.
- `*` is a universal selector — it applies to every element on the page.
- **Why:** Browser default fonts (like Times New Roman or Arial) look dated. Inter is a clean, modern sans-serif font widely used in dashboards and tech products.

#### 2.2.3 Metric Cards

```css
.metric-card {
    background: #161b22;
    border-radius: 16px;
    padding: 1.5rem;
    border: 1px solid #21262d;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #7c3aed, #3b82f6);
}

.metric-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 30px rgba(124, 58, 237, 0.2);
}
```

**CSS concepts explained:**

| Property | What It Does |
|---|---|
| `background: #161b22` | Sets a dark card background color |
| `border-radius: 16px` | Rounds the corners of the card (higher = rounder) |
| `padding: 1.5rem` | Adds space inside the card between edge and content |
| `border: 1px solid #21262d` | Adds a thin, subtle border around the card |
| `box-shadow: 0 4px 20px rgba(0,0,0,0.3)` | Creates a shadow under the card to make it look elevated. The values are: x-offset, y-offset, blur-radius, color. `rgba` allows transparency. |
| `transition: transform 0.3s ease` | Makes property changes animate smoothly over 0.3 seconds instead of being instant |
| `::before` | A pseudo-element that creates a decorative element before the card's content. Used here for the gradient bar at the top. |
| `content: ''` | Required for pseudo-elements to render (even if empty) |
| `linear-gradient(90deg, #7c3aed, #3b82f6)` | Creates a smooth color transition from purple to blue at a 90-degree angle |
| `transform: translateY(-4px)` | Moves the card up by 4 pixels on hover, creating a "lift" effect |

**Why:** Card-based layouts are a standard pattern in modern dashboards. They group related information visually and make the interface scannable.

#### 2.2.4 Section Cards

```css
.section-card {
    background: #161b22;
    border-radius: 16px;
    padding: 1.8rem;
    border: 1px solid #21262d;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
}
```

**Why:** Used for the Edit and Delete sections to visually group them as distinct panels.

#### 2.2.5 Category Badges

```css
.category-badge {
    display: inline-block;
    background: linear-gradient(135deg, #7c3aed22, #3b82f622);
    color: #c9d1d9;
    padding: 0.5rem 1rem;
    border-radius: 10px;
    border: 1px solid #30363d;
    transition: transform 0.2s ease;
}

.category-badge:hover {
    transform: scale(1.05);
}
```

| Property | What It Does |
|---|---|
| `display: inline-block` | Makes badges sit side by side instead of stacking vertically |
| `#7c3aed22` | The `22` at the end is hex transparency (very see-through purple) |
| `transform: scale(1.05)` | Enlarges the badge slightly (5%) on hover |

**Why:** Badges/pills are a compact way to show category totals without a full table. The subtle gradient background ties them to the app's purple-blue color scheme.

#### 2.2.6 Expense Rows

```css
.expense-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.8rem 1rem;
    background: #0d1117;
    border-radius: 10px;
    border: 1px solid #21262d;
    transition: border-color 0.2s ease;
}

.expense-row:hover {
    border-color: #7c3aed;
}
```

| Property | What It Does |
|---|---|
| `display: flex` | Uses Flexbox layout — children are arranged in a row |
| `justify-content: space-between` | Pushes items to opposite ends (index on left, amount on right) |
| `align-items: center` | Vertically centers all items in the row |

**Why:** Custom HTML rows give full control over styling. Streamlit's built-in `st.table()` cannot be easily styled with custom colors, hover effects, or spacing.

#### 2.2.7 Button Styling

```css
.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #3b82f6) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.6rem 2rem !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(124, 58, 237, 0.4) !important;
}
```

- `!important` is needed to override Streamlit's built-in button styles.
- **Why:** Default Streamlit buttons are plain white/gray. Gradient buttons with hover lift effects feel premium and interactive.

#### 2.2.8 Input Field Overrides

```css
input[type="text"],
input[type="number"] {
    background-color: #0d1117 !important;
    color: #c9d1d9 !important;
    border: 1px solid #30363d !important;
    border-radius: 10px !important;
}

input:focus {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 2px rgba(124, 58, 237, 0.2) !important;
}
```

- `input[type="text"]` targets all text inputs on the page by their HTML type attribute.
- `:focus` triggers when the user clicks into the field.
- **Why:** Default white input fields clash with the dark theme. Dark inputs with a purple focus glow maintain visual consistency.

#### 2.2.9 Hidden Default Elements

```css
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
```

- **Why:** Hides Streamlit's hamburger menu and "Made with Streamlit" footer for a cleaner, more app-like appearance.

---

### 2.3 Layout Reorganization

**Before (top to bottom):**
1. Title
2. Amount + Category inputs (2 columns)
3. "Add Expense" button
4. "View All Expenses" toggle button → table
5. "View Total" toggle button → metric
6. "View Category Totals" toggle button
7. Edit (left) + Delete (right) columns
8. "Edit Expense" button
9. Category totals table (at bottom)

**After (top to bottom):**
1. Header with title, subtitle, and gradient accent line
2. Metric cards row (Total Expenses ₹ + Number of Expenses)
3. Add New Expense section (Amount + Category + button)
4. Divider
5. All Expenses section (always visible, custom styled rows)
6. Divider
7. Category Breakdown section (always visible, styled badge pills)
8. Divider
9. Manage Expenses section (Edit left + Delete right)
10. Footer

**Why:** The original layout scattered related data across toggle buttons. A dashboard should show all key information at a glance — users shouldn't have to click to see their own data. The new top-to-bottom flow follows a logical hierarchy: summary → input → details → management.

---

### 2.4 Removed Toggle Buttons

Three `session_state` variables and their toggle buttons were removed:

| Removed | What It Did |
|---|---|
| `st.session_state.show_expenses` | Toggled expense table visibility |
| `st.session_state.show_total` | Toggled total metric visibility |
| `st.session_state.show_category_totals` | Toggled category totals visibility |

**Why:** In a dashboard, all data should be always visible. Toggle buttons add unnecessary clicks and hide information from the user. The metric cards, expense rows, and category badges are now always displayed.

---

### 2.5 HTML Elements Used

| HTML Element | Where Used | What It Does |
|---|---|---|
| `<div>` | Cards, rows, badges | A block-level container that groups content. Starts on a new line. |
| `<span>` | Index, category, amount in expense rows | An inline container. Does NOT start a new line. |
| `<h1>` | Dashboard header title | The largest heading element |
| `<p>` | Dashboard subtitle | A paragraph of text |
| `<style>` | CSS injection block | Tells the browser that its contents are CSS rules |
| `<br>` | Spacing between sections | A line break (adds vertical space) |
| `class="..."` | All custom elements | Links an HTML element to CSS styling rules |

---

### 2.6 Error Handling Improvement

**Before:**
```python
file = open("expenses.txt", "r")
```
This would crash if the file didn't exist yet.

**After:**
```python
try:
    file = open("expenses.txt", "r")
except FileNotFoundError:
    return expenses, total
```
Now the app handles the case where `expenses.txt` doesn't exist (e.g., first run) gracefully.

---

### 2.7 Color Palette

| Color | Hex Code | Usage |
|---|---|---|
| Page background | `#0e1117` | Main dark background |
| Card background | `#161b22` | Elevated card panels |
| Card border | `#21262d` | Subtle card outlines |
| Input background | `#0d1117` | Dark input fields |
| Primary text | `#ffffff` | Headings, metric values |
| Secondary text | `#c9d1d9` | Body text, category names |
| Muted text | `#8b949e` | Labels, subtitles |
| Dim text | `#484f58` | Index numbers, footer |
| Accent purple | `#7c3aed` | Gradients, focus states, amounts |
| Accent blue | `#3b82f6` | Gradient endpoints |
| Accent teal | `#06b6d4` | Header gradient endpoint |

---

## 3. Features Preserved

All original functionality is intact:

| Feature | Status |
|---|---|
| Add expense (category + amount) | ✅ Working |
| Category validation (not empty) | ✅ Working |
| Amount validation (greater than 0) | ✅ Working |
| View all expenses | ✅ Always visible |
| View total expense | ✅ Always visible (metric card) |
| View category totals | ✅ Always visible (badges) |
| Edit expense by index | ✅ Working |
| Delete expense by index | ✅ Working |
| File-based storage (expenses.txt) | ✅ Unchanged |
| Data format (Category-Amount) | ✅ Unchanged |

---

## 4. Data Functions (Unchanged)

The three core functions were not modified:

| Function | Purpose |
|---|---|
| `save_expense(category, amount)` | Appends a single expense to `expenses.txt` |
| `load_expenses()` | Reads all expenses from the file, returns list + total |
| `save_all_expenses(expenses)` | Overwrites the file with the current expense list |

---

## 5. Learning Summary

### CSS Concepts Covered
1. **Selectors:** `*`, `.class`, `#id`, `::before`, `:hover`, `:focus`, `input[type="..."]`
2. **Box Model:** `padding`, `margin`, `border`, `border-radius`
3. **Colors:** Hex (`#7c3aed`), `rgba()` with transparency, `linear-gradient()`
4. **Layout:** `display: flex`, `justify-content`, `align-items`, `flex-wrap`, `gap`
5. **Effects:** `box-shadow`, `transform`, `transition`, `scale()`
6. **Typography:** `@import`, `font-family`, `font-weight`, `text-transform`, `letter-spacing`
7. **Specificity:** `!important` for overriding framework styles

### HTML Concepts Covered
1. **Container elements:** `<div>` (block), `<span>` (inline)
2. **Text elements:** `<h1>`, `<p>`
3. **Styling:** `<style>`, `class` attribute
4. **Pseudo-elements:** `::before` for decorative content

### Streamlit Concepts Covered
1. `st.set_page_config()` for page metadata
2. `st.markdown()` with `unsafe_allow_html=True` for custom HTML/CSS
3. `st.columns()` for side-by-side layouts
4. `st.container()` for grouping widgets
5. `st.divider()` for visual section breaks
6. `st.rerun()` for refreshing after data changes
7. `use_container_width=True` for full-width buttons

---

*End of Report*
