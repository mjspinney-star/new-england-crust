# COWORK SCHEDULED TASK — Weekly Newsletter Draft
## Paste this into the Cowork Scheduled section (left sidebar → Scheduled → New Task)

### Task name
New England Crust — Weekly Newsletter Draft

### Frequency
Weekly — set for Monday at 9:00 AM
(You'll review and send to ConvertKit same day or Tuesday morning)

### Task prompt — paste exactly as written below

---

First, run git pull in /Users/michaelspinney/Desktop/new-england-crust to sync the latest posts from GitHub.

Then do the following:

1. Read the most recently published post in src/content/blog/ — check the pubDate frontmatter field to find it.

2. Read the newsletter broadcast template at /Users/michaelspinney/Desktop/new-england-crust/email/newsletter-broadcast-template.md for formatting and voice guidance.

3. Draft a broadcast email for ConvertKit using the template structure:
   - Subject line (under 50 characters, one of the three formats in the template)
   - Preview text (one sentence extending the subject)
   - Opening paragraph (2-3 sentences — what we cooked or tried, specific and sensory)
   - The Thing (3-5 sentences — a genuine tip or lesson pulled from the post, useful on its own without clicking)
   - Post link line (post title, one-sentence description, full URL with trailing slash)
   - Optional affiliate mention (only if a product with a natural fit appears in the post — one sentence max, never forced)
   - Sign-off in the standard format

4. Save the draft as a new file: /Users/michaelspinney/Desktop/new-england-crust/email/drafts/newsletter-YYYY-MM-DD.md using today's date.

5. Print a summary: post used, subject line chosen, and one sentence on why you picked that tip as "the thing."

Voice notes: first-person plural throughout (we/our/us). Short sentences. Sounds like telling a friend what we cooked, not writing a newsletter. The tip should be useful on its own without clicking the link.

---

### Setup instructions

**Before activating this task:**

1. Create this folder structure inside your project:
   - /Users/michaelspinney/Desktop/new-england-crust/email/
   - /Users/michaelspinney/Desktop/new-england-crust/email/drafts/

2. Save the newsletter-broadcast-template.md file (from outputs) into:
   /Users/michaelspinney/Desktop/new-england-crust/email/newsletter-broadcast-template.md

3. In Cowork left sidebar → Scheduled → New Task → paste the task prompt above → set to Weekly, Monday 9:00 AM

4. Run it once manually to test before relying on the schedule

**Your Monday workflow after setup:**
- Open email/drafts/ folder
- Open the latest newsletter-YYYY-MM-DD.md file
- Copy into ConvertKit → Broadcasts → New Broadcast
- Paste, adjust anything that doesn't sound right, set send time
- Done in under 5 minutes
