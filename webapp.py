from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/bigboy")
def render_page1():
    return render_template('Discovery of America.html')

@app.route("/p2")
def render_page2():
    return render_template('ww1.html')

@app.route("/p3")
def render_page3():
    return render_template('ww2.html')
  
  @app.route("/p4")
def render_page3():
    return render_template('coldwar.html')
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
