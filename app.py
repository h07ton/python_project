from flask import Flask, render_template
import generate_course

app = Flask(__name__)

@app.route('/')
def index():
    prompt = "Write an e-course on Python programming for beginners"
    course = generate_course.generate_course(prompt)
    return render_template('index.html', course=course)

if __name__ == '__main__':
    app.run(debug=True)
