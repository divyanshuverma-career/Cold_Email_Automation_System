import pandas as pd
import smtplib
import os

from datetime import datetime
from dotenv import load_dotenv

from email.message import EmailMessage

from email_templates import (
    first_email,
    followup1,
    followup2
)


load_dotenv()



EMAIL = os.getenv("EMAIL_ID")
PASSWORD = os.getenv("EMAIL_PASSWORD")

print("EMAIL:", EMAIL)
print("PASSWORD LOADED:", PASSWORD is not None)


EMAIL = os.getenv("Email_ID")
PASSWORD = os.getenv("Email_PASSWORD")


df = pd.read_csv(
    "contacts.csv",
    dtype={
        "Status": "object",
        "Followup_1_Status": "object",
        "Followup_2_Status": "object",
        "Reply_Status": "object"
    }
)

df.columns = df.columns.str.strip()

df["Sent_Date"] = pd.to_datetime(
    df["Sent_Date"],
    errors="coerce"
)

df["Followup_1_Date"] = pd.to_datetime(
    df["Followup_1_Date"],
    errors="coerce"
)


def send_mail(receiver, subject, body):

    msg = EmailMessage()

    msg["From"] = EMAIL
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)


    with open("Resume_.pdf","rb") as f:

        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename="Divyanshu_Resume.pdf"
        )


    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            EMAIL,
            PASSWORD
        )

        smtp.send_message(msg)



today = pd.Timestamp.today().normalize()


count = 0


for index,row in df.iterrows():

    if count == 50:
        break


    if pd.isna(row["Status"]):


        body = first_email(
            row["First Name"],
            row["Title"],
            row["Company"]
        )


        send_mail(
            row["Email"],
            "Data Analyst Internship Opportunity",
            body
        )


        df.loc[index,"Status"]="Sent"

        df.loc[index,"Sent_Date"]=today


        count+=1

# ==========================
# FOLLOW-UP 1
# ==========================

followup_count = 0

for index, row in df.iterrows():

    if followup_count == 50:
        break

    if (
        row["Status"] == "Sent"
        and pd.isna(row["Followup_1_Status"])
        and pd.isna(row["Reply_Status"])
        and pd.notna(row["Sent_Date"])
    ):

        days_passed = (today - row["Sent_Date"]).days

        if days_passed >= 3:

            body = followup1(
                row["First Name"]
            )

            send_mail(
                row["Email"],
                "Following up regarding Data Analyst Internship",
                body
            )

            df.loc[index, "Followup_1_Status"] = "Sent"

            df.loc[index, "Followup_1_Date"] = today

            followup_count += 1


# ==========================
# FOLLOW-UP 2
# ==========================

followup2_count = 0

for index, row in df.iterrows():

    if followup2_count == 50:
        break

    if (
        row["Followup_1_Status"] == "Sent"
        and pd.isna(row["Followup_2_Status"])
        and pd.isna(row["Reply_Status"])
        and pd.notna(row["Followup_1_Date"])
    ):

        days_passed = (today - row["Followup_1_Date"]).days

        if days_passed >= 7:

            body = followup2(
                row["First Name"]
            )

            send_mail(
                row["Email"],
                "Final Follow-up | Data Analyst Internship",
                body
            )

            df.loc[index, "Followup_2_Status"] = "Sent"

            df.loc[index, "Followup_2_Date"] = today

            followup2_count += 1

df.to_csv(
    "contacts.csv",
    index=False
)


print("Completed")
