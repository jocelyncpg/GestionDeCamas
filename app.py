from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "clave_super_segura"

# Credenciales administrador
ADMIN_EMAIL = "admin@gestiondecamas.cl"
ADMIN_PASS = "1234"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        # Aquí después puedes enviar correo real
        return "Mensaje enviado correctamente"
    return render_template("contacto.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == ADMIN_EMAIL and password == ADMIN_PASS:
            session["admin"] = True
            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if not session.get("admin"):
        return redirect("/login")

    # Datos simulados (mockup)
    pacientes = [
        {
            "nombre": "Juan Pérez",
            "edad": 65,
            "sexo": "Masculino",
            "estado": "Activo",
            "email": "juan.perez@email.com"
        },
        {
            "nombre": "María González",
            "edad": 42,
            "sexo": "Femenino",
            "estado": "En tránsito",
            "email": "maria.g@email.com"
        },
        {
            "nombre": "Carlos Soto",
            "edad": 58,
            "sexo": "Masculino",
            "estado": "Concluido",
            "email": "carlos.s@email.com"
        }
    ]

    return render_template("dashboard.html", pacientes=pacientes)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
