# Day 47: Amazon Price Tracker -- Email Alerts & Data Monitoring

## What You Learned
You combined web scraping with email automation. You monitored product prices and sent email notifications when prices dropped below thresholds—a practical automation task.

---

## Key Concepts

### 1. Web Scraping with Headers
Websites block scrapers using User-Agent detection:
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept-Language': 'en-US,en;q=0.5'
}

response = requests.get(URL, headers=headers)
```

**Why:** Servers reject requests without browser-like headers. Spoofing headers with `User-Agent` makes your script appear as a normal browser.

### 2. HTML Parsing with lxml
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'lxml')  # Faster parser than 'html.parser'
```

**Why:** `lxml` is faster and more robust than built-in parser. Requires `pip install lxml`.

### 3. Extracting Price Data
```python
price = soup.find(name="span", class_="a-offscreen")
price_float = float(price.string.split("$")[1])  # "Price: $123.45" → 123.45
```

**Pattern:**
1. Find price element by tag and class
2. Get text content (`.string` or `.getText()`)
3. Split on "$" to remove currency symbol
4. Convert to float for comparison

**Why:** Amazon wraps prices in `<span class="a-offscreen">` for accessibility. Direct `.string` access gets the first text node.

### 4. Email via SMTP
SMTP (Simple Mail Transfer Protocol) sends emails:
```python
import smtplib

with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
    connection.starttls()  # Start secure connection
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=recipient,
        msg="Subject: Alert\n\nMessage body"
    )
```

**Why:** SMTP is the standard email protocol. `.starttls()` encrypts connection. Port 587 is standard.

### 5. Email Configuration for Different Providers
```python
# Gmail
smtp_address = "smtp.gmail.com"
port = 587

# Yahoo
smtp_address = "smtp.mail.yahoo.com"
port = 587

# Outlook
smtp_address = "smtp-mail.outlook.com"
port = 587
```

**Why:** Different providers have different SMTP servers. Gmail/Outlook may require app-specific passwords.

### 6. Email Message Format
```python
msg = f"Subject: Price Alert!!!\n\nThe price of the item you are monitoring is ${price}, below your purchase threshold"
```

**Format:** `"Subject: Title\n\nBody"` (blank line separates subject from body)

**Why:** SMTP expects this format. Many libraries (like `smtplib`) require manual formatting; higher-level libraries abstract this.

### 7. Conditional Execution
```python
if price <= 200:  # Only send alert if price below threshold
    with smtplib.SMTP(...) as connection:
        # Send email
```

**Why:** Don't spam! Only alert when condition is met.

### 8. Environment Variables for Credentials
```python
from dotenv import load_dotenv
import os

load_dotenv("../.env")
email = os.getenv("mistwire_yahoo_account")
password = os.getenv("mistwire_yahoo_password")
```

**.env file:**
```
mistwire_yahoo_account=your_email@yahoo.com
mistwire_yahoo_password=your_app_password
```

**Why:** Never hardcode credentials. Store in .env and add to .gitignore.

### 9. Real-World Considerations
- **Scraping restrictions:** Amazon may block aggressive scraping. Respectful delays are important.
- **Price changes:** HTML structure changes over time. Selectors break.
- **Email limits:** Services rate-limit emails. Amazon price tracker would need scheduling (see Day 27 Tkinter or cron jobs).
- **Legal/ethical:** Check site terms. Some prohibit scraping.

### 10. Scheduling (Beyond Day 47)
For production, schedule with:
- **Windows:** Task Scheduler
- **macOS/Linux:** cron jobs (`crontab -e`)
- **Cloud:** AWS Lambda, Google Cloud Functions

This project runs once; production needs scheduling.

---

## Common Pitfalls
- **Not using headers:** Requests without User-Agent get blocked
- **Hardcoding credentials:** Anyone viewing code sees passwords
- **Not handling network errors:** Website down? Script crashes. Use try/except.
- **Assuming price format never changes:** Amazon redesigns pages. Selectors break. Defensive code handles this.
- **Password as plaintext:** Store app-specific passwords, not main account password
- **Not `.starttls()`:** Unencrypted email is insecure
- **Sending too many emails:** Spam filters will mark you. Respect rate limits.
- **Not checking if price element exists:** `NoneType` errors if selector is wrong

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 45** | Web scraping fundamentals (BeautifulSoup, find, select) |
| **Day 46** | APIs (similar monitoring concept, but API-based) |
| **Day 25** | CSV/pandas for logging price history |
| **Day 27** | Tkinter GUI could display price tracker dashboard |
| **Day 28** | Pomodoro's timer could schedule price checks |
| **Days 33-40** | Similar monitoring tasks (habit tracker, stock tracker) |
| **Day 48** | Selenium could handle JavaScript-heavy product pages |

---

## Before You Move On

Make sure you can:
- [ ] Use headers in requests to bypass User-Agent blocking
- [ ] Extract and convert price data (string → float)
- [ ] Set up SMTP connections for different email providers
- [ ] Format email messages with subject and body
- [ ] Use .env files for credentials (never hardcode!)
- [ ] Implement conditional alerts (send only when threshold met)
- [ ] Handle network/parsing errors gracefully
- [ ] Understand basic email security (starttls, app passwords)

---

## Practice Prompt
**Build a price tracker for multiple products:**

1. **Track multiple URLs:** Create a list of product URLs to monitor
2. **Log prices:** Store price history in CSV (date, product, price)
3. **Email alerts:** Send notifications when:
   - Price drops below threshold
   - Price increases significantly
   - Item goes out of stock
4. **Scheduling:** Use a task scheduler to run daily
5. **Error handling:** Gracefully handle:
   - Network failures
   - Changed HTML structure
   - Email delivery failures
6. **Statistics:** Calculate average price, price trends, savings potential

**Challenge:** Track competitor prices across multiple retailers (Amazon, Walmart, Best Buy) and alert when cheaper alternative found.
