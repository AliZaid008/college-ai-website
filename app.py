from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- ROUTE 1: HOME PAGE ---
@app.route('/')
def home():
    return render_template('index.html')

# --- ROUTE 2: ASK A QUESTION PAGE ---
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        # 1. Get data from the form
        user_email = request.form.get('email')
        user_question = request.form.get('question')

        # 2. SIMULATE EMAIL SENDING
        # In a real app, you would use an SMTP library here.
        # For now, we print to the console to prove it works.
        print(f"--------------------------------------------------")
        print(f"📩 NEW QUESTION RECEIVED!")
        print(f"From: {user_email}")
        print(f"Question: {user_question}")
        print(f"Action: Forwarding to Admin + 5 Collaborators...")
        print(f"--------------------------------------------------")

        # 3. Reload page with a "Success" message
        return render_template('ask.html', success=True)

    # If it's a GET request (user just opening the page)
    return render_template('ask.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)