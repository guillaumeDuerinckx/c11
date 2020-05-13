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
    return d
def get_result_course(a):
    d=list()
    conn= sqlite3.connect('inginious.sqlite')
    cur = conn.cursor()
    if a == "":
        for line in cur.execute("select count(result), result  from submissions group by result "):
            d.append(line)
        return d
    a="\"{}\"".format(a)
    phrase = "select count(result), result  from submissions where course = {} group by result ".format(str(a))
    for line in cur.execute(phrase):
        d.append(line)
    return d
def get_succeeded_users_all(a):
    d=list()
    conn= sqlite3.connect('inginious.sqlite')
    cur = conn.cursor()
    if a == "":
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
    return d
    
def get_succeeded_users(a):
    d=list()
    conn= sqlite3.connect('inginious.sqlite')
   
    if a == "":
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
    return d