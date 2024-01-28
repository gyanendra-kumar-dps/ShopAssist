from flask import *
proj=Flask(__name__)
@proj.route('/')
def main():
    return render_template('main.html')
usrlist=[]
@proj.route('/call',methods=['GET','POST'])
def call():
    global usrlist
    if request.method == 'POST':
        usrlist.append(('user',request.form.get('user')))
        usrlist.append(('bot','This is a demo test'))
    return render_template('main.html',abc=usrlist)
proj.run(debug=True)
