# utils.py

from .models1 import GoogleForm, FormSubmission

def reset_google_form_links():
    submission = FormSubmission.objects.first()
    if submission.submission_count >= 10:
        # Reset the submission count
        submission.submission_count = 0
        submission.save()
        # Reset Google Form links
        google_form = GoogleForm.objects.first()
        google_form.pre_link = "new_pre_link"
        google_form.post_link = "new_post_link"
        google_form.mid_link = "new_mid_link"
        google_form.save()
