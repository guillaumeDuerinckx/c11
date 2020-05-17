# -*- coding: utf-8 -*-
import sqlite3
calcul_b_reussite="select count(succeeded), succeeded from user_tasks where tried <> 0 group by succeeded"
null_count = "select count(tried), submission from user_tasks where tried = 0 "
all= "select count(succeeded), succeeded from user_tasks group by succeeded"
def requete_sql(a):
    """
    pre: une requete sql representee dans un string
    post: retour d'une liste des donnee demandee
    """
    d=list()
    conn= sqlite3.connect('inginious.sqlite')
    cur = conn.cursor()
    for line in cur.execute(a):
        d.append(line)
    conn.close()
    return d
def get_result_course(a):
    """
    pre: string contenantle nom d'un cours
    post: retour d'une liste des donnee comptant le chaque type de resultat reçu pou ce cours
    """
    d=list()
    conn= sqlite3.connect('inginious.sqlite')
    cur = conn.cursor()
    if a == "":  # Dans l'éventualité qu'un string vide soit placé en pre
        for line in cur.execute("select count(result), result  from submissions group by result "):
            d.append(line)
        return d
    a="\"{}\"".format(a)
    phrase = "select count(result), result  from submissions where course = {} group by result ".format(str(a))
    for line in cur.execute(phrase):
        d.append(line)
    conn.close()
    return d
def get_succeeded_users_all(a):
    """
    pre :string contenant le nom d'un cours
    post:retourne une liste de tuple comptant le nombre de reussite et d'échecs

    """
    d=list()
    conn= sqlite3.connect('inginious.sqlite')
    cur = conn.cursor()
    if a == "":   # Dans l'éventualité qu'un string vide soit placé en pre
        for line in cur.execute("select count(succeeded), succeeded from user_tasks group by succeeded"):
            d.append(line)
        return d
    a="\"{}\"".format(a)
    phrase = "select count(succeeded), succeeded from user_tasks where course = {} group by succeeded".format(str(a))
    for line in cur.execute(phrase):
        if 'false'in line:
            line=(line[0],'Failed Submissions')
        if 'true' in line :
            line=(line[0],'Success')
        d.append(line)
    conn.close()
    return d

def get_succeeded_users(a):
    d=list()
    conn= sqlite3.connect('inginious.sqlite')

    if a == "":   # Dans l'éventualité qu'un string vide soit placé en pre
        for line in cur.execute("select count(succeeded), succedeed  from user_tasks group by succeeded "):
            d.append(line)
        return d
    a="\"{}\"".format(a)
    cur = conn.cursor()
    calcul_b_reussite="select count(succeeded), succeeded from user_tasks where tried <> 0 and course = {} group by succeeded".format(str(a))
    null_count = "select count(tried), submission from user_tasks where tried = 0 and course = {} ".format(str(a))
    for line in cur.execute(calcul_b_reussite):
        if 'false'in line:
            line=(line[0],'Echec')
        if 'true' in line :
            line=(line[0],'Success')
        d.append(line)
    for line in cur.execute(null_count):
        line=(line[0],'None')
        d.append(line)
    d = sorted(d, key=lambda course: str.lower(course[1]) )
    conn.close()
    return d

def take_second(elem):
    return str.lower(elem[1])

def get_date_results(a):
    """
        pre: un nom de cours
        post: une liste de tuples arrangés sous cet ordre (date, success/fail, soumissions count)
    """
    d=list()
    new_d=list()
    conn= sqlite3.connect('inginious.sqlite')
    cur = conn.cursor()
    if a == "":  # Dans l'éventualité qu'un string vide soit placé en pre
        for line in cur.execute("select course, submitted_on, result from submissions order by submitted_on"):
            line = list(line)
            line[1]=line[1].split('T')
            line[1]=line[1][0]
            d.append(line)
            count_succ=0
            count_fail=0
        for i in range(0,len(d)-1):
            if d[i][1] == d[i+1][1]:
                if d[i][1] == 'success':
                    count_succ=count_succ+1
                if d[i][2] == 'failed':
                    count_fail=count_fail+1
            else:
                if d[i][2] == 'success':
                    count_succ=count_succ+1
                if d[i][2] == 'failed':
                    count_fail=count_fail+1
                succ=(d[i][1],'success',count_succ)
                new_d.append(succ)
                fail=(d[i][1],'fail',count_fail)
                new_d.append(fail)
                count_succ=0
                count_fail=0
        if d[i][2] == 'success':
            count_succ=count_succ+1
        if d[i][2] == 'failed':
            count_fail=count_fail+1
        succ=(d[i][2],'success',count_succ)
        new_d.append(succ)
        fail=(d[i][2],'fail',count_fail)
        new_d.append(fail)
        count_succ=0
        count_fail=0
        conn.close()
        return new_d

    a="\"{}\"".format(a)
    date_getter="select submitted_on, result from submissions where course = {} order by submitted_on ".format(str(a))
    for line in  cur.execute(date_getter):
        line = list(line)
        line[0]=line[0].split('T')
        line[0]=line[0][0]
        d.append(line)
        count_succ=0
        count_fail=0
    for i in range(0,len(d)-1):
        if d[i][0] == d[i+1][0]:
            if d[i][1] == 'success':
                count_succ=count_succ+1
            else:
                count_fail=count_fail+1
        else:
            if d[i][1] == 'success':
                count_succ=count_succ+1
            else:
                count_fail=count_fail+1
            succ=(d[i][0],'success',count_succ)
            new_d.append(succ)
            fail=(d[i][0],'fail',count_fail)
            new_d.append(fail)
            count_succ=0
            count_fail=0
    if d[i][1] == 'success':
        count_succ=count_succ+1
    else:
        count_fail=count_fail+1
    succ=(d[i][0],'success',count_succ)
    new_d.append(succ)
    fail=(d[i][0],'fail',count_fail)
    new_d.append(fail)
    count_succ=0
    count_fail=0
    conn.close()
    return new_d

def separateur(l):
    """
    pre: une liste rendue sous le même format du post de la fonction get_date_result(a)
    post: deux liste sous le même format que la pré, contenant dans l'une tous les tuples détenant la mention success et  dans l'autre la mention fail
    """
    new_1=list()
    new_2=list()
    for i in l:
        if i[1]=='success':
            new_1.append(i)
        else:
            new_2.append(i)
    return new_1,new_2

def transform_to_data(l):
    """
    fonction utilisée pour ranger les donnée sous forme de liste utilisable pour les graphiques ,
    ici on extrait les soumissions.
    pre:une liste contenant les données sous forme (date, fail/success, quantité(int))
    post:une liste de toutes les soumissions int()
    """
    new =list()
    for i in l:
        new.append(i[2])
    return new

def transform_to_label(l):
    """
    fonction utilisée pour ranger les donnée sous forme de liste utilisable pour les graphiques ,
    ici on extrait les dates.
    pre:une liste contenant les données sous forme (date, fail/success, quantité(int))
    post:une liste de toutes les dates
    """
    new =list()
    for i in l:
        new.append(i[0])
    return new

def get_3rd_graph_info1(a,b):
    """
    pre: deux strings contenant le nom d'un cours et la mention true/false
    post: retourne une liste de tuples rangés sous la forme (compte du nombre de mention true/false, exercice concerné)
    Cette fonctiion ne prend pas en compte les exercices non tentés
    """
    d=list()
    conn= sqlite3.connect('inginious.sqlite')
    cur = conn.cursor()
    a="\"{}\"".format(a)
    b="\"{}\"".format(b)
    phrase = "select count(succeeded), task  from user_tasks where course = {0} and succeeded = {1} and tried > 0 group by task ".format(str(a),str(b))
    for line in cur.execute(phrase):
        d.append(line)
    conn.close()
    return d

def get_3rd_graph_info2(a,b):
    """
    pre: deux strings contenant le nom d'un cours et la mention true/false
    post: retourne une liste de tuples rangés sous la forme (compte du nombre de mention true/false, exercice concerné)
    Cette fonctiion prend en compte les exercices non tentés
    """
    d=list()
    conn= sqlite3.connect('inginious.sqlite')
    cur = conn.cursor()
    a="\"{}\"".format(a)
    b="\"{}\"".format(b)
    phrase = "select count(succeeded), task  from user_tasks where course = {0} and succeeded = {1} group by task ".format(str(a),str(b))
    for line in cur.execute(phrase):
        d.append(line)
    conn.close()
    return d

def equalizing(a,b):
    """
    pre: deux listes de tuples sous la forme de get_3rd_graph_info1()
    post: les listes sont egalizées en faisant apparaître les exercises non présents de l'une dans l'autre
    """

    for i in a:
        found = False
        for j in b:
            if i[1]==j[1]:
                found= True
                break
            else:
                continue
        if found == False:
            b.append((0,i[1]))
    return a,b
def percentage(a,b):
    """
    pre: deux ints ou floats
    post: le resultat du pourcentage de a par rapport à b
    """
    if b==0:
        return 0
    result=(a/b)*100
    return result
def final(a):
    """
    pre: le nom d'un cours
    post: retourne deux listes sous le format get_3rd_graph_info1() triées et egalisées
    """
    succ=get_3rd_graph_info1(a,'true')
    fail=get_3rd_graph_info1(a,'false')
    succ,fail = equalizing(succ,fail)
    fail,succ = equalizing(fail,succ)
    succ=sorted(succ, key=take_second)
    fail=sorted(fail, key=take_second)
    return succ,fail

def final2(a):
        """
        pre: le nom d'un cours
        post: retourne deux listes sous le format get_3rd_graph_info2() triées et egalisées
        """

    succ=get_3rd_graph_info2(a,'true')
    fail=get_3rd_graph_info2(a,'false')
    succ,fail = equalizing(succ,fail)
    fail,succ = equalizing(fail,succ)
    succ=sorted(succ, key=take_second)
    fail=sorted(fail, key=take_second)
    return succ,fail

def get_percent1(a):
            """
            pre: le nom d'un cours
            post: retourne deux listes sous le format get_3rd_graph_info1() triées et egalisées en remplaçant les taux par des pourcentages
            """

    d=list()
    succ=get_3rd_graph_info1(a,'true')
    fail=get_3rd_graph_info1(a,'false')
    succ,fail = equalizing(succ,fail)
    fail,succ = equalizing(fail,succ)
    succ=sorted(succ, key=take_second)
    fail=sorted(fail, key=take_second)
    for i in range(len(succ)):
        d.append((percentage(fail[i][0],succ[i][0]),succ[i][1]))
    return d

def get_percent2(a):
    """
    pre: le nom d'un cours
    post: retourne deux listes sous le format get_3rd_graph_info2() triées et egalisées en remplaçant les taux par des pourcentages
    """
    d=list()
    succ=get_3rd_graph_info2(a,'true')
    fail=get_3rd_graph_info2(a,'false')
    succ,fail = equalizing(succ,fail)
    fail,succ = equalizing(fail,succ)
    succ=sorted(succ, key=take_second)
    fail=sorted(fail, key=take_second)
    for i in range(len(succ)):
        d.append((percentage(fail[i][0],succ[i][0]),succ[i][1]))
    return d
