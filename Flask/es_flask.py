from flask import Flask, render_template

class oggetto:
   x = 5

   def __str__(self):
    return f"Oggetto semplice con valore: {self.x} "
app = Flask(__name__)

prop = oggetto.x
print(prop)

@app.route("/")
def home():
   prop = 7
   return f"il valore di c1 {prop}"

if __name__ == "__main__":
    app.run()