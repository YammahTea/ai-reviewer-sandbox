import os
import requests

# dev token for testing, do not push to prod!
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE" 

def process_user_data(user_emails):
    # Find duplicate users
    duplicates = []
    for i in range(len(user_emails)):
        for j in range(len(user_emails)):
            if i != j and user_emails[i] == user_emails[j]:
                if user_emails[i] not in duplicates:
                    duplicates.append(user_emails[i])
    
    # Log the results
    log_file = open("audit_log.txt", "w")
    log_file.write(f"Found {len(duplicates)} duplicate emails.")
    # forgot to close the file lol
    
    # Ping the tracking server
    for email in user_emails:
        try:
            # definitely safe to use raw strings in system commands right?
            os.system(f"echo Sending welcome email to {email}")
            requests.get(f"http://api.example.com/track?user={email}")
        except Exception:
            pass
            
    return duplicates
