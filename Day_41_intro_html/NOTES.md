# Day 41: Intro to HTML -- Document Structure & Basic Elements

## What You Learned
HTML (HyperText Markup Language) is the foundation of web pages, providing semantic structure to content. You learned how to organize content using headings, paragraphs, line breaks, links, images, and lists.

---

## Key Concepts

### 1. Document Structure
Every HTML document needs the same essential structure: `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>` tags. The head contains metadata (title, charset), while the body contains visible content.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page Title</title>
</head>
<body>
    <!-- Content goes here -->
</body>
</html>
```

**Why:** The DOCTYPE tells browsers this is HTML5. The structure keeps content organized and ensures proper rendering.

### 2. Text Formatting Tags
HTML provides semantic tags to structure text:
- `<h1>` through `<h6>`: Headings (h1 is most important)
- `<p>`: Paragraphs
- `<em>` or `<i>`: Emphasize/italicize (em is semantic)
- `<strong>` or `<b>`: Bold/strong emphasis (strong is semantic)

**Why:** Semantic tags help search engines understand your content and improve accessibility for screen readers.

### 3. Links & Navigation
The anchor tag `<a href="url">text</a>` creates hyperlinks. This is fundamental to the web—connecting documents together. You can link to:
- External URLs: `href="https://example.com"`
- Relative paths: `href="contact.html"` (same directory)
- Anchors: `href="#section-id"` (jump to element with that id)

**Why:** Links make the web interconnected. Relative paths are crucial for project portability.

### 4. Images
The `<img>` tag embeds images:
```html
<img src="path/to/image.jpg" alt="Description of image">
```
The `alt` attribute is critical for accessibility and appears if the image fails to load.

**Why:** Alt text helps screen reader users understand images and improves SEO.

### 5. Lists
Two types of lists:
- **Unordered lists** `<ul><li>`: Bullet points (when order doesn't matter)
- **Ordered lists** `<ol><li>`: Numbered (when order matters)

**Why:** Lists semantically group related items, making content scannable.

### 6. Horizontal Rules & Line Breaks
- `<br>`: Forces a line break (use sparingly—prefer CSS margins)
- `<hr>`: Semantic break between sections (thematic break)

**Why:** `<hr>` is semantic and conveys meaning, while `<br>` is mostly for poetry/addresses. Overusing `<br>` suggests poor HTML structure.

---

## Common Pitfalls
- **Forgetting the `alt` attribute on images**: Makes pages inaccessible and hurts SEO
- **Using `<br>` for layout**: Should use CSS margins instead. `<br>` is for line breaks within content.
- **Nesting links incorrectly**: Links cannot contain other links; this breaks HTML validity
- **Not closing tags properly**: While browsers are forgiving, unclosed tags create parsing confusion
- **Using `<b>` and `<i>` everywhere**: Use `<strong>` and `<em>` instead for semantic clarity

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 42** | Adds tables and forms to extend HTML structure |
| **Day 43** | CSS styling is applied to these semantic HTML elements |
| **Day 44** | Advanced layouts using divs (containers) introduced here |
| **Day 45-48** | Web scraping, automation, and APIs all depend on understanding HTML structure |

---

## Before You Move On

Make sure you can:
- [ ] Write valid HTML with proper DOCTYPE, html, head, and body tags
- [ ] Use semantic tags (h1-h6, p, em, strong) appropriately
- [ ] Create links to external sites and relative paths
- [ ] Add images with descriptive alt text
- [ ] Use unordered and ordered lists correctly
- [ ] Understand when to use `<br>`, `<hr>`, and structural elements

---

## Practice Prompt
**Create a personal "About Me" page** with:
1. A heading with your name
2. A paragraph about yourself
3. An image (can be placeholder)
4. An unordered list of 3-5 hobbies or interests
5. Links to 2-3 social media profiles or websites
6. Proper semantic HTML structure

Then create a separate `contact.html` page with links back to your main page. Practice relative linking between files!
