# AI Coding Instructions for Web-Dev Labs

## Project Overview
This is a web development learning lab repository containing HTML, CSS, and JavaScript exercises organized into labs. Each lab focuses on progressively building web development skills with real-world UI/UX patterns.

## Project Structure

```
web-dev/
├── lab 2/          # Frontend UI recreation exercises
│   ├── task1.html  # Facebook login page clone
│   ├── task2.html  # [CSS/layout exercise]
│   └── task3.html  # [Interactive component]
└── Lab3/           # JavaScript fundamentals & interactive apps
    └── task1/
        ├── 1.html-7.html  # JavaScript basics (alerts, variables, DOM)
        └── task2/
            └── 1.html     # To-Do List app (DOM manipulation, events)
```

## Key Patterns & Conventions

### File Organization
- **Lab structure**: `Lab{N}/task{N}/` pattern reflects learning progression
- **Numbered files** (1.html-7.html) indicate sequential exercises within a topic
- **task2/** subdirectories are standalone mini-projects requiring complete features

### HTML Templates
All files follow standard HTML5 boilerplate:
- `<!DOCTYPE html>` declaration
- `<meta charset="UTF-8">` for encoding
- Inline `<style>` tags in `<head>` (single-file exercises)
- JavaScript in `<script>` tags (typically before closing `</body>`)

### Styling Conventions (from task1.html)
- **Utility-first approach**: `display: flex`, `box-sizing: border-box` globally
- **Gradient backgrounds**: Used for visual appeal (e.g., `background: linear-gradient(135deg, #667eea, #764ba2)`)
- **Box shadow effects**: `box-shadow: 0 15px 30px rgba(0,0,0,0.2)` for depth
- **Transitions/animations**: `@keyframes` for fade-in effects, smooth interactions
- **Responsive**: Focus on flexbox layouts and viewport centering
- **Modern fonts**: `"Segoe UI"`, `Arial` sans-serif stack

### JavaScript Patterns (from task2/1.html - To-Do App)
- **DOM manipulation**: `document.querySelector()`, `addEventListener()`
- **Event handling**: Click handlers for buttons (add/delete tasks)
- **Data storage**: Likely using localStorage for persistence (common pattern)
- **Simple state management**: Update UI by modifying DOM directly, no frameworks
- **Vanilla JS only**: No jQuery or frameworks; prioritize native DOM APIs

## Development Workflow

### How to Work with These Files
1. **Open in browser**: All files are standalone HTML - just open in any browser
2. **Testing**: Use browser DevTools for debugging (F12)
3. **No build process**: These are vanilla HTML/CSS/JS exercises - edit and refresh
4. **Live Server recommended**: VS Code Live Server extension for auto-refresh during editing

### Common Tasks
- **Update styling**: Edit inline `<style>` tags
- **Add interactivity**: Add `<script>` with event listeners
- **Debug JavaScript**: Use `console.log()` and browser DevTools
- **Reference patterns**: Check similar numbered files (1.html) for basic patterns before advanced ones

## Important Conventions

### CSS
- **Box-sizing**: Always set `* { box-sizing: border-box; }` globally
- **Flex centering**: Use `display: flex; justify-content: center; align-items: center;`
- **Color scheme**: Professional gradients and subtle shadows (not flat colors)
- **Spacing**: Consistent use of `gap`, `padding`, `margin` for alignment

### JavaScript
- **No external dependencies**: Avoid suggesting npm packages or build tools
- **Accessible selectors**: Use class names over element selectors where possible
- **Event delegation**: Use `addEventListener` on container elements for lists
- **Error handling**: Simple validation before DOM updates (alert user if needed)

## When Creating or Modifying Files

- Maintain the existing HTML5 structure with inline styles/scripts
- Keep single-file constraint (no external CSS/JS files in these exercises)
- Use descriptive HTML structure (semantic elements where applicable)
- Add comments explaining complex JavaScript logic
- Test in browser before considering complete

## Context for AI Agents

This is a **learning-focused project**, not production code. The goal is educational clarity, not performance optimization. When suggesting improvements:
- Prioritize readability and pedagogical value
- Prefer explicit code over clever tricks
- Keep examples simple and focused on single concepts
- Reference how concepts are built progressively across files
