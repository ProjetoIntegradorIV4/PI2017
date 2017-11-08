from flask import Flask, render_template
 
app = Flask(__name__)  

@app.route("/teste")
def index():
	return render_template('C:\Users\milen\Documents\GitHub\PI2017\index.html')

if __name__ == '__main__':
  app.run(debug=True)