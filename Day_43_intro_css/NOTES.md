# Day 43: Intro to CSS -- Selectors & Styling

## What You Learned
CSS (Cascading Style Sheets) is how you make websites look good. You learned three types of selectors (element, class, ID), how to style properties, and how pseudo-classes add interactivity.

---

## Key Concepts

### 1. CSS Syntax & Selectors
CSS follows the pattern: `selector { property: value; }`

```css
/* Element selector: targets all tags of a type */
h1 { color: red; }

/* Class selector: targets elements with class attribute (can apply to many elements) */
.highlight { background-color: yellow; }

/* ID selector: targets one specific element (unique identifier) */
#special { font-size: 24px; }
```

**Three Selector Types:**
- **Element selectors**: `h1`, `p`, `img` — broad, affects all instances
- **Class selectors**: `.classname` — medium specificity, reusable on many elements
- **ID selectors**: `#idname` — high specificity, targets one unique element

**Why:** Selectors control WHAT you style. Understanding specificity (ID > class > element) is crucial.

### 2. Specificity & Cascade
CSS stands for "Cascading" because styles cascade down with specificity rules:
```
ID selectors (highest specificity)
  ↓
Class selectors
  ↓
Element selectors (lowest specificity)
```

If an ID and class style the same element differently, the ID wins. This is why IDs should be used sparingly.

**Why:** Specificity prevents style conflicts. Lower specificity = more reusable, flexible CSS.

### 3. Common CSS Properties
```css
/* Colors & Text */
color: red;                    /* Text color */
background-color: blue;        /* Background color */
font-size: 16px;              /* Text size */
font-family: Arial, sans-serif; /* Font choice */

/* Spacing */
margin: 10px;                 /* Space OUTSIDE element */
padding: 10px;                /* Space INSIDE element */
border: 2px solid black;      /* Border styling */

/* Positioning & Size */
width: 100%;                  /* Width (px, %, em, etc.) */
height: 50px;                 /* Height */
position: relative;           /* Positioning context */
left: 20px;                   /* Move left from normal position (with position: relative) */
```

**Why:** These are the most-used properties. Mastering them enables 80% of styling needs.

### 4. Pseudo-Classes
Pseudo-classes style elements in special states:
```css
a:hover { color: orange; }        /* When user hovers */
button:active { transform: scale(0.95); } /* When clicked */
input:focus { border-color: blue; } /* When focused */
```

**Why:** Pseudo-classes provide interactivity without JavaScript. Hover effects improve UX.

### 5. Multiple Classes
An element can have multiple classes for flexible styling:
```html
<img class="bacon circular" src="...">
```

```css
.bacon { background-color: green; }
.circular { border-radius: 100%; }
```

**Why:** Multiple classes enable composition—reuse small, single-purpose classes rather than creating mega-classes.

### 6. External Stylesheets
Always link CSS externally, not inline:
```html
<link rel="stylesheet" href="css/styles.css">
```

**Why:** External stylesheets separate content (HTML) from presentation (CSS), making code maintainable. Inline styles are considered bad practice.

### 7. Comments in CSS
```css
/* This is a comment */
/* Multi-line
   comments work too */
```

**Why:** Comments explain WHY, not WHAT. Future you will appreciate your explanations.

---

## Common Pitfalls
- **Over-relying on ID selectors**: IDs are hard to override. Classes are more flexible.
- **Using inline styles**: Defeats the purpose of CSS. Always use external stylesheets.
- **Not understanding specificity**: Styles mysteriously not working? Check specificity conflicts.
- **Forgetting units**: `width: 100;` doesn't work. Must be `width: 100px;` or `width: 100%;`
- **Using `position: relative` incorrectly**: Only shifts the element visually; other elements don't account for the shift.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 41-42** | CSS styles the HTML structure; CSS is meaningless without proper HTML |
| **Day 44** | Advanced layouts using position, flexbox, grid |
| **Day 27** | tkinter (Python GUI) uses similar concept: styling separate from widgets |
| **Day 45-48** | Web scraping/automation: understanding selectors helps target elements |

---

## Before You Move On

Make sure you can:
- [ ] Write CSS with proper syntax: `selector { property: value; }`
- [ ] Use element, class, and ID selectors correctly
- [ ] Understand specificity and cascade order
- [ ] Apply common properties: color, background, font-size, margin, padding
- [ ] Use pseudo-classes like :hover for interactivity
- [ ] Assign multiple classes to elements
- [ ] Link external stylesheets properly

---

## Practice Prompt
**Style your Day 41-42 HTML pages:**
1. Create a `style.css` file and link it to your HTML
2. Style headings with a custom color and font-size
3. Add background colors to sections using classes
4. Style links with `:hover` pseudo-class to change color on hover
5. Add margins and padding to create spacing
6. Use at least one ID selector for a unique element
7. Apply multiple classes to an image or button

**Challenge:** Create a color-coded form where inputs have different background colors based on input type (use class selectors).
