from flask import Flask, render_template 
app = Flask(__name__)    



@app.route('/')          
def checkerboard1():
    return render_template('8_by_8.html')  

@app.route('/4')          
def checkerboard2():
    return render_template('8_by_4.html')  

@app.route('/12/12')          
def checkerboard3():
    return render_template('12_by_12.html')  



if __name__=="__main__":       
    app.run(debug=True)    