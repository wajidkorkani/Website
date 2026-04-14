from flask import Flask, render_template, redirect, request
app = Flask(__name__)

students = []
@app.route('/')
def index():
    names = ["John", "Jimmy", "Jey", "Jo"]
    return render_template('index.html', names=names)

@app.route('/about')
def About():
    data = {
        "name": "Classic academy of computer science larkana",
        "about": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus voluptatum cum est! Nulla nemo magni ipsum odit? Qui consequuntur harum doloremque natus illo atque asperiores quia, eligendi dolorum. Rerum eum ratione magnam maxime! Nesciunt, voluptatem soluta? Neque, reprehenderit inventore. Rem sequi quidem voluptas vel velit fugit a totam eum rerum, corrupti ducimus excepturi itaque nesciunt. Soluta officiis dignissimos nulla dolor atque, suscipit doloribus, aliquam beatae ab repellendus iusto id rerum recusandae veniam minus amet maxime accusantium tempore aperiam eveniet! Iste ratione perspiciatis odio ex at. Blanditiis dolore quis accusamus! Et tempora deserunt quaerat. Vel porro illum impedit culpa, libero ipsum similique aut dignissimos voluptatibus, minus eligendi error in. Quidem optio eius, deleniti ducimus consequatur aliquam asperiores quaerat assumenda fugiat dignissimos debitis. Nam repellendus, iste corrupti possimus sapiente quisquam nisi deserunt officiis blanditiis iusto ex voluptatum voluptatibus quasi modi eveniet commodi ullam dicta itaque soluta? Officia animi nemo deleniti deserunt, perferendis repudiandae, earum et, accusamus vero recusandae distinctio neque in voluptatum fugiat! Corporis neque ea temporibus expedita sed sapiente saepe perferendis aliquid magnam aspernatur. Aperiam incidunt, modi tenetur dolor eveniet doloribus a itaque laboriosam earum cupiditate architecto corrupti quod dicta. Fugiat illum adipisci minima itaque obcaecati ipsum ad dolor vero, voluptates blanditiis consectetur voluptatibus corporis similique dignissimos? Recusandae cumque fugiat sit pariatur delectus est, atque quod necessitatibus iusto vel facere? Officia quam est, neque perferendis vitae ipsa rerum laboriosam accusamus, molestiae adipisci eos mollitia eum harum molestias tempore ea dolores! Accusantium ipsam animi suscipit vel amet quia modi in quod dolores!"
    }

    return render_template("about.html", data=data, students=students)


@app.route("/add-data", methods=["POST"])
def add_data():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form['age']
        student = {
            "name": name,
            "age": int(age)
        }

        students.append(student)
        return redirect("/about")
    return redirect("/about", error="Something went wrong")
        

app.run(debug=True)