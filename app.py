from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory storage for emails
registered_emails = set()

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    
    if not email or '@' not in email:
        flash('Please enter a valid email address')
        return redirect('/')
    
    if email in registered_emails:
        flash('This email is already registered')
        return redirect('/')
    
    registered_emails.add(email)
    flash('Registration successful!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
