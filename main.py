from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)#WSGI

#decorator
@app.route('/')
def welcome():
    #return "RESULTS RELEASED"
    return render_template('index.html')

'''
#jinja2 techinique are of four types
#{%....%}for conditional, for loops #this is for statements
#{{   }}#for expression to print output
#{#....#}#for commenting 

'''

@app.route('/success/<int:score>')#flask variable rule
def success(score):
    #return "success with score of " + str(score) + " marks ...."
    #return render_template('result.html',res = score)
    res =""
    if score>=50:
        res ="PASS"
    else:
        res ="FAIL"
    final={'score':score,'res':res}
    return render_template('result.html',out=final)

@app.route('/fail/<int:score>')#flask variable rule
def fail(score):
    #return "fail with score of " + str(score) + " marks ...." 
    return '''<html><body><h1>DEVI</h1><h2>fail</h2></body></html>''' 

#result checker
@app.route('/results/<int:marks>')#flask variable rule
def results(marks):
    result = ""
    if(marks>50):
        result = "success"
    else:
        result = "fail"
    #return result +" with score of " + str(marks) + " marks ...."
    return redirect(url_for(result,score = marks))


@app.route('/submit',methods=['POST','GET'])
def submit():
    total=0.0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        total=(science+maths+c+datascience)/4
    if(total>=50):
        result = "success"
    else:
        result = "fail"
    return redirect(url_for(result,score=total))

if __name__== '__main__':
    app.run(debug=True)
