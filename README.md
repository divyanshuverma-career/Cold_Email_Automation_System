# 📧 Cold Email Automation for Internship Outreach

This project automates sending personalized cold emails and follow-up emails to recruiters or hiring managers. It keeps track of sent emails, follow-ups, and replies using a CSV file.

---

## 💙 Built with Python by Divyanshu Verma

Thanks for checking out this project!

I created this tool to simplify my internship outreach process by automating personalized cold emails and follow-ups. If it saves you time or helps you in your job search, I'd love to hear about it.

If you found this project useful, consider giving it a ⭐ on GitHub. Feedback, suggestions, and contributions are always welcome!

**Connect with me:**
- GitHub: https://github.com/divyanshuverma-career
- LinkedIn: www.linkedin.com/in/divyanshuverma-career


---

# Features

- Send personalized cold emails
- Automatically attach your resume
- Store email credentials securely using `.env`
- Track sent emails in `contacts.csv`
- Send first follow-up after 3 days (if no reply)
- Prevent duplicate emails
- Easy to customize email templates

---

# Project Structure

```
project/
│
├── mail.py                 # Main script
├── email_templates.py      # Email templates
├── contacts.csv            # Recruiter database
├── resume.pdf              # Resume attachment
├── .env                    # Email credentials
├── requirements.txt
└── README.md
```

---

# Step 1: Clone the Repository

```bash
git clone <repository-url>

cd <repository-folder>
```

or simply download the project ZIP and extract it.

---

# Step 2: Install Python

Download Python (3.10 or above)

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

# Step 3: Install Dependencies

Install all required packages.

```bash
pip install -r requirements.txt
```

If you don't have a requirements file, install manually:

```bash
pip install pandas python-dotenv
```

---

# Step 4: Enable Gmail App Password

**Important**

Google no longer allows logging in using your normal Gmail password.

You must create an **App Password**.

### Enable Two-Factor Authentication

Go to:

https://myaccount.google.com/security

Enable

- 2-Step Verification

After that

Go to

https://myaccount.google.com/apppasswords

Generate a new App Password.

Copy the generated password.

---

# Step 5: Create a `.env` File

Create a file named

```
.env
```

inside the project folder.

Example:

```env
EMAIL_ID=your_email@gmail.com
EMAIL_PASSWORD=your_16_character_app_password
```

Example:

```env
EMAIL_ID=john@gmail.com
EMAIL_PASSWORD=abcd efgh ijkl mnop
```

Do **NOT** use your normal Gmail password.

---

# Step 6: Add Your Resume

Place your resume in the project folder.

Rename it exactly as:

```
resume.pdf
```

or update this line inside `mail.py`

```python
with open("resume.pdf","rb") as f:
```

to match your file name.

---

# Step 7: Prepare contacts.csv

Create a CSV file named

```
contacts.csv
```

Required columns:

| Column |
|----------|
| First Name |
| Last Name |
| Email |
| Title |
| Company |
| Status |
| Sent_Date |
| Followup_1_Status |
| Followup_1_Date |
| Followup_2_Status |
| Followup_2_Date |
| Reply_Status |

Example

| First Name | Last Name | Email | Title | Company | Status |
|------------|-----------|-------|--------|----------|--------|
| John | Doe | john@gmail.com | HR Manager | ABC Ltd | |

Leave the tracking columns empty initially.

---

# Step 8: Customize Email Templates

Open

```
email_templates.py
```

Modify

- first_email()
- followup1()
- followup2()

according to your outreach style.

These functions return the email body.

---

# Step 9: Run the Script

```bash
python mail.py
```

or

```bash
python3 mail.py
```

---

# What Happens After Running?

The script:

1. Reads all contacts
2. Finds contacts whose `Status` is empty
3. Sends personalized emails
4. Attaches your resume
5. Marks them as **Sent**
6. Saves today's date
7. Checks previous emails
8. Sends follow-up after 3 days (if no reply)

---

# Tracking Status

The script updates `contacts.csv` automatically.

Example:

| Name | Status | Sent_Date | Followup_1_Status |
|------|---------|-----------|-------------------|
| John | Sent | 2026-07-24 | Sent |

No manual editing is required.

---

# Sending Limit

To avoid Gmail spam restrictions, the script sends a maximum of **50 emails** per run.

You can change this inside `mail.py`.

```python
if count == 50:
    break
```

Similarly for follow-ups.

---

# Common Errors

## SMTP Authentication Error

**Reason**

Using your Gmail password instead of an App Password.

**Solution**

Generate an App Password.

---

## resume.pdf Not Found

Place your resume inside the project folder.

or

Update the filename inside

```python
with open(...)
```

---

## contacts.csv Not Found

Make sure the CSV file is inside the project directory.

---

## Missing Python Package

Install dependencies again.

```bash
pip install pandas python-dotenv
```

---

# Future Improvements

- SQLite/PostgreSQL database
- HTML email support
- Email open tracking
- Click tracking
- Automatic second follow-up
- Logging system
- Retry on failed emails
- Scheduler (Windows Task Scheduler / Cron)
- Dashboard for tracking outreach

---

# Disclaimer

Use this project responsibly.

Sending a large number of unsolicited emails may violate the policies of email providers or recipients. Always personalize your outreach, respect rate limits, and comply with applicable anti-spam laws and platform terms of service.

---

# License

This project is intended for educational and personal use. Feel free to modify and improve it according to your needs.

