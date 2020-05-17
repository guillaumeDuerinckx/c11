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
    line = separateur(get_date_results("LSINF1101-PYTHON"))
    labels = transform_to_label(line[0])
    datasuccess= transform_to_data(line[0])
    datafail = transform_to_data(line[1])

    return render_template('soumissionparjourLSINF1101.html', labels=labels, datasuccess=datasuccess,datafail=datafail)

@app.route('/batônnetsLSINF1101')
def batônnetsLSINF1101():
    true_e= final("LSINF1101-PYTHON")[0]
    trust= [d[0] for d in true_e]
    false_e=final("LSINF1101-PYTHON")[1]
    falsest= [d[0] for d in false_e]
    true_e2= final2("LSINF1101-PYTHON")[0]
    trust2= [d[0] for d in true_e2]
    false_e2=final2("LSINF1101-PYTHON")[1]
    falsest2= [d[0] for d in false_e2]
    percent_e=get_percent1('LSINF1101-PYTHON')
    percent=[d[0] for d in percent_e]
    percent2_e=get_percent2('LSINF1101-PYTHON')
    percent2=[d[0] for d in percent2_e]
    labels=[d[1] for d in true_e]

    return render_template('batônnetsLSINF1101.html',trust=trust, falsest=falsest,percent=percent,labels =labels, percent2= percent2, trust2= trust2, falsest2= falsest2)

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
    line = separateur(get_date_results("LSINF1252"))
    labels = transform_to_label(line[0])
    datasuccess= transform_to_data(line[0])
    datafail = transform_to_data(line[1])

    return render_template('soumissionparjourLSINF1252.html', labels=labels, datasuccess=datasuccess,datafail=datafail)

@app.route('/batônnetsLSINF1252')
def batônnetsLSINF1252():
    true_e= final("LSINF1252")[0]
    trust= [d[0] for d in true_e]
    false_e=final("LSINF1252")[1]
    falsest= [d[0] for d in false_e]
    true_e2= final2("LSINF1252")[0]
    trust2= [d[0] for d in true_e2]
    false_e2=final2("LSINF1252")[1]
    falsest2= [d[0] for d in false_e2]
    percent_e=get_percent1('LSINF1252')
    percent=[d[0] for d in percent_e]
    percent2_e=get_percent2('LSINF1252')
    percent2=[d[0] for d in percent2_e]
    labels=[d[1] for d in true_e]

    return render_template('batônnetsLSINF1252.html',trust=trust, falsest=falsest,percent=percent,labels =labels, percent2= percent2, trust2= trust2, falsest2= falsest2)

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
    line = separateur(get_date_results("LEPL1402"))
    labels = transform_to_label(line[0])
    datasuccess= transform_to_data(line[0])
    datafail = transform_to_data(line[1])

    return render_template('soumissionparjourLEPL1402.html', labels=labels, datasuccess=datasuccess,datafail=datafail)

@app.route('/batônnetsLEPL1402')
def batônnetsLEPL1402():
    true_e= final("LEPL1402")[0]
    trust= [d[0] for d in true_e]
    false_e=final("LEPL1402")[1]
    falsest= [d[0] for d in false_e]
    true_e2= final2("LEPL1402")[0]
    trust2= [d[0] for d in true_e2]
    false_e2=final2("LEPL1402")[1]
    falsest2= [d[0] for d in false_e2]
    percent_e=get_percent1('LEPL1402')
    percent=[d[0] for d in percent_e]
    percent2_e=get_percent2('LEPL1402')
    percent2=[d[0] for d in percent2_e]
    labels=[d[1] for d in true_e]

    return render_template('batônnetsLEPL1402.html',trust=trust, falsest=falsest,percent=percent,labels =labels, percent2= percent2, trust2= trust2, falsest2= falsest2)

@app.route('/page_contact')
def page_contact():
    return render_template('page_contact.html')
