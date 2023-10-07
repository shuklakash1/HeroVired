from flask import Flask, request

app = Flask(__name__)

student = [
    {
        "name":"Archer",
        "age":32
    },
    {
        "name":"Lana",
        "age":"31"
    },
    {
        "name":"Mallory",
        "age":"67"
    }
]

# @app.route('/', methods=['GET', 'POST', 'PUT'])
# def helloWorld():
#     num1 = int(request.args.get('num1'))
#     num2 = int(request.args.get('num2'))
#     num3 = int(request.args.get('num3'))


#     return str(num1+num2+num3)

@app.route("/string", methods=['GET', 'POST', 'PUT'])
def reverse():

    txt = "Akash" [::-1]

    return str(txt)

if __name__ == "__main__":
    app.run(debug=True)
