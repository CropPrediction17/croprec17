from flask import Flask,render_template,request
import mysql.connector
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

conn=mysql.connector.connect(host="localhost",user="root",password="",database="registration")
cursor=conn.cursor()

@app.route('/login')
def login(methods=['POST']):
    return render_template('login.html')

@app.route('/register')
def regs():
    return render_template('registration.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/crops')
def crops():
    return render_template("crops.html")

@app.route('/appled')
def appled():
    return render_template("appled.html")

@app.route('/bananad')
def bananad():
    return render_template("bananad.html")

@app.route('/blackgramd')
def blackgramd():
    return render_template("blackgramd.html")

@app.route('/chickpead')
def chickpead():
    return render_template("chickpead.html")

@app.route('/coconutd')
def coconutd():
    return render_template("coconutd.html")

@app.route('/coffeed')
def coffeed():
    return render_template("coffeed.html")

@app.route('/cottond')
def cottond():
    return render_template("cottond.html")

@app.route('/grapesd')
def grapesd():
    return render_template("grapesd.html")

@app.route('/juted')
def juted():
    return render_template("juted.html")

@app.route('/kidneybeansd')
def kidneybeansd():
    return render_template("kidneybeansd.html")

@app.route('/lentild')
def lentild():
    return render_template("lentild.html")

@app.route('/maized')
def maized():
    return render_template("maized.html")

@app.route('/mangod')
def mangod():
    return render_template("mangod.html")

@app.route('/mothbeansd')
def mothbeansd():
    return render_template("mothbeansd.html")

@app.route('/mungbeand')
def mungbeand():
    return render_template("mungbeand.html")

@app.route('/muskmelond')
def muskmelond():
    return render_template("muskmelond.html")

@app.route('/oranged')
def oranged():
    return render_template("oranged.html")

@app.route('/papayad')
def papayad():
    return render_template("papayad.html")

@app.route('/pigeonpeasd')
def pigeonpeasd():
    return render_template("pigeonpeasd.html")

@app.route('/pomegranated')
def pomegranated():
    return render_template("pomegranated.html")


@app.route('/riced')
def riced():
    return render_template("riced.html")

@app.route('/watermelond')
def watermelond():
    return render_template("watermelond.html")



@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=='POST':
        N=float(request.form['nitrogen'])
        P=float(request.form['potassium'])
        K=float(request.form['phosporous'])
        temperature=float(request.form['temperature'])
        humidity=float(request.form['humidity'])
        ph=float(request.form['ph'])
        rainfall=float(request.form['rainfall'])
        prediction=model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
        apple='apple'
        banana='banana'
        blackgram='blackgram'
        chickpea='chickpea'
        coconut='coconut'
        coffee='coffee'
        cotton='cotton'
        grapes='grapes'
        jute='jute'
        kidneybeans='kidneybeans'
        lentil='lentil'
        maize='maize'
        mango='mango'
        mothbeans='mothbeans'
        mungbean='mungbean'
        muskmelon='muskmelon'
        orange='orange'
        papaya='papaya'
        pigeonpeas='pigeonpeas'
        pomegranate='pomegranate'
        rice='rice'
        watermelon='watermelon'
        
        if prediction==0:
           return render_template("applep.html",apple=apple)
        if prediction==1:
            return render_template("bananap.html",banana=banana)
        if prediction==2:
           return render_template("blackgramp.html",blackgram=blackgram)
        if prediction==3:
            return render_template("chickpeap.html",chickpea=chickpea)
        if prediction==4:
            return render_template("coconutp.html",coconut=coconut)
        if prediction==5:
            return render_template("coffeep.html",coffee=coffee)
        if prediction==6:
            return render_template("cottonp.html",cotton=cotton)
        if prediction==7:
            return render_template("grapesp.html",grapes=grapes)
        if prediction==8:
            return render_template("jutep.html",jute=jute)
        if prediction==9:
            return render_template("kidneybeansp.html",kidneybeans=kidneybeans)
        if prediction==10:
            return render_template("lentilp.html",lentil=lentil)
        if prediction==11:
            return render_template("maizep.html",maize=maize)
        if prediction==12:
            return render_template("mangop.html",mango=mango)
        if prediction==13:
            return render_template("mothbeansp.html",mothbeans=mothbeans)
        if prediction==14:
            return render_template("mungbeanp.html",mungbean=mungbean)
        if prediction==15:
            return render_template("muskmelonp.html",muskmelon=muskmelon)
        if prediction==16:
           return render_template("orangep.html",orange=orange)
        if prediction==17:
            return render_template("papayap.html",papaya=papaya)
        if prediction==18:
            return render_template("pigeonpeasp.html",pigeonpeas=pigeonpeas)
        if prediction==19:
            return render_template("pomegranatep.html",pomegranate=pomegranate)
        if prediction==20:
            return render_template("ricep.html",rice=rice)
        if prediction==21:
            return render_template("watermelonp.html",watermelon=watermelon)

    return render_template("predict.html")


@app.route('/login_validation',methods=['POST'])
def login_validaton():
    email=request.form.get('email')
    password=request.form.get('password')
    cursor.execute(""" SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    user=cursor.fetchall()

    if len(user)>0:
        return render_template("index.html")
    else:
        return render_template("home.html")

@app.route('/add_user',methods=['POST'])
def add_user():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')


    cursor.execute("INSERT INTO `users` (`User_id`,`Name`,`Email`,`Password`) VALUES (NULL,'{}','{}','{}')".format(name,email,password))
    conn.commit()

    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)
