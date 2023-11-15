from flask import Flask, render_template, url_for

app = Flask(__name__)

head:list = ['idno', 'lastname', 'firstname', 'course', 'level']


with open('static/student.txt', 'r') as f:
    lines = f.readlines()

    g = [content.split(',') for content in lines]

# f = open('static/student.txt','r')
# g:list = f.readlines().split(,)


@app.route("/")
def main()->None:
    return render_template("index.html", title = "Student List" , content = g, header=head)

if __name__ == "__main__":
    app.run(debug = True)
