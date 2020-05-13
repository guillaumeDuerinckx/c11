from flask import Flask, request, url_for,redirect
from flask import render_template
from test_data_base import *


app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template ('accueil.html')


@app.route('/résultatLSINF1101')
def résultatLSINF1101():
    line=get_result_course("LSINF1101-PYTHON")
    data = [d[0] for d in line]
    labels = [str(d[1]) for d in line]
    line2=get_succeeded_users("LSINF1101-PYTHON")
    data2= [d[0] for d in line2]
    label2 = [str(d[1]) for d in line2]
    line2bis=get_succeeded_users_all("LSINF1101-PYTHON")
    data2bis= [d[0] for d in line2bis]
    label2bis = [str(d[1]) for d in line2bis]

    return render_template('résultatLSINF1101.html',data=data, labels=labels, label2=label2, data2= data2, line2bis= line2bis, data2bis=data2bis,label2bis=label2bis )


@app.route('/soumissionparjourLSINF1101')
def soumissionparjourLSINF1101():
    return render_template('soumissionparjourLSINF1101.html')

@app.route('/batônnetsLSINF1101')
def batônnetsLSINF1101():
    return render_template('batônnetsLSINF1101.html')

@app.route('/résultatLSINF1252')
def résultatLSINF1252():
    line=get_result_course("LSINF1252")
    data = [d[0] for d in line]
    labels = [str(d[1]) for d in line]
    line2=get_succeeded_users("LSINF1252")
    data2= [d[0] for d in line2]
    label2 = [str(d[1]) for d in line2]
    line2bis=get_succeeded_users_all("LSINF1252")
    data2bis= [d[0] for d in line2bis]
    label2bis = [str(d[1]) for d in line2bis]
    return render_template('résultatLSINF1252.html',data=data, labels=labels, label2=label2, data2= data2, line2bis= line2bis, data2bis=data2bis,label2bis=label2bis)

@app.route('/soumissionparjourLSINF1252')
def soumissionparjourLSINF1252():
    return render_template('soumissionparjourLSINF1252.html')

@app.route('/batônnetsLSINF1252')
def batônnetsLSINF1252():
    return render_template('batônnetsLSINF1252.html')

@app.route('/résultatLEPL1402')
def résultatLEPL1402():
    line=get_result_course("LEPL1402")
    data = [d[0] for d in line]
    labels = [str(d[1]) for d in line]
    line2=get_succeeded_users("LEPL1402")
    data2= [d[0] for d in line2]
    label2 = [str(d[1]) for d in line2]
    line2bis=get_succeeded_users_all("LEPL1402")
    data2bis= [d[0] for d in line2bis]
    label2bis = [str(d[1]) for d in line2bis]
    return render_template('résultatLEPL1402.html',data=data, labels=labels, label2=label2, data2= data2, line2bis= line2bis, data2bis=data2bis,label2bis=label2bis)

@app.route('/soumissionparjourLEPL1402')
def soumissionparjourLEPL1402():
    return render_template('soumissionparjourLEPL1402.html')

@app.route('/batônnetsLEPL1402')
def batônnetsLEPL1402():
    return render_template('batônnetsLEPL1402.html')

@app.route('/page_contact')
def page_contact():
    return render_template('page_contact.html')
