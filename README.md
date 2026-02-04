# 100 Days of Code -- Python

A progressive learning journey through Python and web development, from object-oriented fundamentals to API integrations, GUIs, and browser automation.

Each day folder contains working code plus a `NOTES.md` with key concepts, common pitfalls, cross-references to other days, and practice prompts.

---

## Learning Path Overview

### Part 1: Python Fundamentals (Days 1-13)
Core language features -- classes, file I/O, exceptions, control flow, testing, and debugging. Everything here is a building block for the rest of the curriculum.

### Part 2: Interactive Programs & Games (Days 14-24)
Apply fundamentals to build real programs: games with Turtle graphics, GUI apps with Tkinter, and file-based projects. Introduces event-driven programming and multi-class architecture.

### Part 3: Data & Visualization (Days 25-28)
Data analysis with Pandas, dictionary comprehensions, and GUI applications. The shift from "making things work" to "working with data."

### Part 4: APIs & Integrations (Days 33-40)
HTTP requests, JSON APIs, email/SMS notifications, and chaining multiple services together. Real-world automation with external data sources.

### Part 5: Web Development (Days 41-44)
HTML structure and CSS styling fundamentals. The foundation for understanding how web applications render content.

### Part 6: Web Scraping & Automation (Days 45-48)
BeautifulSoup for HTML parsing, Selenium for browser automation, and combining scraping with APIs (Spotify, Amazon).

---

## Day-by-Day Reference

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| 01 | OOP Basics | Classes, `__init__`, `self`, inheritance, composition, imports |
| 02 | File Handling & Exceptions | `pathlib.Path`, `read_text()`, `try/except/else`, JSON serialization |
| 03 | Django Setup | Project structure, `manage.py`, settings, URL routing |
| 04 | Control Flow & Lists | Nested if/elif, 2D lists, string indexing, `.index()` |
| 05 | Password Generator | `random` module, list building, `shuffle()`, string joining |
| 06 | Testing with pytest | Unit tests, assertions, test functions for classes |
| 07 | Hangman | Custom modules, game loops, ASCII art, word lists |
| 08 | Caesar Cipher | Modulo operator, string manipulation, encode/decode logic |
| 09 | Silent Auction | Dictionaries, nested data structures, finding max values |
| 10 | Functions with Outputs | Return values, parameters, docstrings, calculator project |
| 11 | Blackjack | Game algorithms, card logic, Ace handling, dealer AI |
| 12 | Scope | Local vs global, `global` keyword, constants |
| 13 | Debugging | Print debugging, error analysis, systematic bug fixing |
| 14 | Higher/Lower Game | Data comparison, game flow, dictionary-based records |
| 15 | Coffee Machine (Procedural) | Resource management, transaction logic, nested dicts |
| 16 | Coffee Machine (OOP) | Multiple classes, encapsulation, separation of concerns |
| 17 | Quiz Game | API data integration, class-based quiz engine |
| 18 | Turtle Graphics | Drawing, loops, color extraction from images |
| 19 | Turtle Race | Event listeners, keyboard input, screen events |
| 20 | Snake Game (Part 1) | Game architecture, `Snake` and `Food` classes, collision |
| 21 | Snake Game (Part 2) | Scoreboard class, score persistence, file I/O in games |
| 22 | Pong | Two-player logic, paddle physics, ball movement |
| 23 | Turtle Crossing | Progressive difficulty, random spawning, level system |
| 24 | Files & Directories | `pathlib` expanded, mail merge, template-based file generation |
| 25 | CSV & Pandas | DataFrames, `read_csv()`, filtering, statistical methods |
| 26 | NATO Alphabet | List/dict comprehensions, `iterrows()`, CSV to dict |
| 27 | Tkinter Basics | Windows, Labels, Buttons, Entry, grid layout, event handling |
| 28 | Pomodoro App | Canvas widget, timer logic, state management, UI design |
| 31 | Capstone Project | (Placeholder for personal project) |
| 33 | ISS Tracker | `requests.get()`, API calls, `smtplib` email, sunrise/sunset API |
| 34 | Quiz Brain GUI | OOP + Tkinter combined, API data in GUI, HTML decoding |
| 35 | Weather API | OpenWeatherMap, API parameters, weather condition codes |
| 36 | Stock Tracker | Alpha Vantage + NewsAPI + Twilio SMS, percentage calculations |
| 37 | Habit Tracker | HTTP POST/PUT/DELETE, API headers, Pixe.la integration |
| 38 | Workout Tracker | NLP input parsing, Nutritionix API, Google Sheets via Sheety |
| 39 | Flight Deal Finder | Multi-API orchestration, date handling, data classes |
| 40 | Flight Club | Extended flight search, improved notifications |
| 41 | Intro to HTML | Document structure, headings, text formatting, semantic tags |
| 42 | Intermediate HTML | Links, forms, navigation, multi-page sites |
| 43 | Intro to CSS | Selectors, box model, colors, fonts, external stylesheets |
| 44 | Intermediate CSS | Grid, Flexbox, positioning, media queries |
| 45 | BeautifulSoup | HTML parsing, `find_all()`, CSS selectors, web scraping |
| 46 | Spotify Playlist | Billboard scraping + Spotify API, OAuth authentication |
| 47 | Amazon Price Tracker | E-commerce scraping, price monitoring, alerts |
| 48 | Selenium WebDriver | Browser automation, element finding, driver management |

---

## Technologies Used

- **Python 3** -- Primary language throughout
- **Pandas** -- Data analysis (Day 25+)
- **Tkinter** -- Desktop GUIs (Days 27-28, 34)
- **Turtle** -- Graphics and games (Days 18-23)
- **Requests** -- HTTP/API calls (Days 33-40)
- **BeautifulSoup** -- Web scraping (Days 45-47)
- **Selenium** -- Browser automation (Day 48)
- **Django** -- Web framework intro (Day 3)
- **HTML/CSS** -- Web fundamentals (Days 41-44)

## Setup

Each day is self-contained. To run any day's code:

```bash
cd Day_XX_folder_name
python main.py
```

Some days require additional packages (listed in their respective `NOTES.md` files) or API keys stored in environment variables.