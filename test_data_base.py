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
    conn.close()
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
    conn.close()
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
    conn.close()
    return d
def get_date_results(a):
    d=list()
    new_d=list()
    conn= sqlite3.connect('inginious.sqlite')
    cur = conn.cursor()
    if a == "":
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
    new_1=list()
    new_2=list()
    for i in l:
        if i[1]=='success':
            new_1.append(i)
        else:
            new_2.append(i)
    return new_1,new_2

def transform_to_data(l):
    new =list()
    for i in l:
        new.append(i[2])
    return new

def transform_to_label(l):
    new =list()
    for i in l:
        new.append(i[0])
    return new
l=get_date_results("LEPL1402")
l=separateur(l)
f=transform_to_label(l[0])
g = transform_to_data(l[0])
h = transform_to_data(l[1])
