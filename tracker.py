import csv
from datetime import datetime
import sys

FOLLOW_UP_DAYS = 7

if len(sys.argv) > 1 and sys.argv[1] == "add":
    company = input("Company: ")
    date_sent = input("Date sent [today - yyyy-mm-dd]: ")

    if date_sent == "":
        date_sent = datetime.now().strftime("%Y-%m-%d")
    
    contact_person = input("Contact person [optional]: ")
    email = input("Email [optional]: ")
    status = input("Status [waiting]: ")
    notes = input("Notes [optional]: ")

    if status == "":
        status = "waiting"
    
    new_application = {
            "company": company,
            "date_sent": date_sent,
            "contact_person": contact_person,
            "email": email,
            "status": status,
            "last_contact": date_sent,
            "follow_up_date": "",
            "notes": notes,
    }

    with open("applications.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=new_application.keys())
        writer.writerow(new_application)

    print("Application added:", company)
    sys.exit()



with open("applications.csv", "r") as file:
    reader = csv.DictReader(file)
    
    total = 0
    waiting = 0
    rejected = 0
    follow_up_needed = 0
    rejected_companies = []
    waiting_companies = []

    print("LIA APPLICATION TRACKER")
    print("-----------------------")

    for row in reader:
        total += 1

        if row["status"] == "waiting":
            waiting += 1
            waiting_companies.append(row)

        if row["status"] == "rejected":
            rejected += 1
            rejected_companies.append(row)
    
    print()
    print("Waiting for response:")
    
    today = datetime.now()

    for row in waiting_companies:
        sent_date = datetime.strptime(row["date_sent"], "%Y-%m-%d")
        days_waiting = (today - sent_date).days
        
        if days_waiting >= FOLLOW_UP_DAYS:
            follow_up_needed += 1
            print("-", row["company"], "-", days_waiting, "days waiting - FOLLOW UP!")
        else:
            print("-", row["company"], "-", days_waiting, "day/s waiting")


    print()
    print("Rejected applications:")

    for row in rejected_companies:
        print("-", row["company"], "-", row["notes"])

    print()
    print("Total applications:", total)
    print("Waiting for response:", waiting)
    print("Rejected:", rejected)
    print("Follow-up needed:", follow_up_needed)
