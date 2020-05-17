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

def take_second(elem):
    return str.lower(elem[1])

def get_date_results(a):
    """
        pre: un nom de cours
        post: unelist arrangée sous cet ordre (date, success/fail, soumissions count)
    """
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
    """fonction utilisée pour ranger les donnée sous forme de liste utilisable pour les graphiques ,
        ici on extrait les soumissions.
        pre:une liste contenant les données sous forme (date, fail/success, quantité(int))
        post:une liste de toutes les soumissions int()"""
    new =list()
    for i in l:
        new.append(i[2])
    return new

def transform_to_label(l):
    """fonction utilisée pour ranger les donnée sous forme de liste utilisable pour les graphiques ,
        ici on extrait les dates.
        pre:une liste contenant les données sous forme (date, fail/success, quantité(int))
        post:une liste de toutes les dates"""
    new =list()
    for i in l:
        new.append(i[0])
    return new

def get_3rd_graph_info1(a,b):
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
    if b==0:
        return 0
    result=(a/b)*100
    return result
def final(a):
    succ=get_3rd_graph_info1(a,'true')
    fail=get_3rd_graph_info1(a,'false')
    succ,fail = equalizing(succ,fail)
    fail,succ = equalizing(fail,succ)
    succ=sorted(succ, key=take_second)
    fail=sorted(fail, key=take_second)
    return succ,fail

def final2(a):
    succ=get_3rd_graph_info2(a,'true')
    fail=get_3rd_graph_info2(a,'false')
    succ,fail = equalizing(succ,fail)
    fail,succ = equalizing(fail,succ)
    succ=sorted(succ, key=take_second)
    fail=sorted(fail, key=take_second)
    return succ,fail

def get_percent1(a):
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

a = [(331, 'ASCIIDecoder'), (328, 'AbstractClass'), (373, 'AccessModifiers'), (346, 'Array2D'), (294, 'BlackBox'), (213, 'BoundedBuffer'), (324, 'BubbleSortInvariant'), (393, 'Casting'), (294, 'CircularLL'), (3, 'CodeAccuracy'), (3, 'CodeAccuracy2'), (427, 'CommonErrors'), (352, 'ComparatorAndCollections'), (273, 'ComparatorvsComparable'), (381, 'ComplexityArraySearch'), (376, 'ComplexityMCQ1'), (403, 'ComplexitySpaceMCQ'), (246, 'Coverage'), (161, 'CyclicBarrier'), (237, 'FList'), (166, 'FListMergeSort'), (238, 'FTree'), (280, 'Factory'), (383, 'Fibonacci'), (284, 'Future'), (324, 'Generics'), (312, 'Generics2'), (284, 'Generics3'), (346, 'HanoiTower'), (2, 'InfiniteStreams'), (329, 'Inheritance'), (378, 'Introduction'), (339, 'LambdaExpressioninJava'), (424, 'LearnException'), (397, 'MakeMistakeToUnderstandThem'), (255, 'MaximumSumSubarray'), (235, 'MergeSortImplementation'), (241, 'MidTermQuiz'), (147, 'MidTermQuizMCQ'), (167, 'MidTermQuizMCQ2'), (269, 'MyArrayList'), (298, 'Observer'), (174, 'Optional'), (137, 'ParallelelMergeSort'), (4, 'PostScript'), (200, 'ProducerConsumer'), (332, 'QueueWithStacks'), (265, 'SharedCounter'), (306, 'SieveOfEratosthenesImplementation'), (387, 'SieveOfEratosthenesMCQ'), (372, 'StackWithQueue'), (219, 'Streams'), (209, 'Streams2'), (360, 'StringUtils'), (290, 'ThreadsIntroduction'), (300, 'TreeCombineWith'), (324, 'TreeInorder'), (321, 'TreeSame'), (451, 'ValueOrReference'), (262, 'Visitor'), (264, 'VisitorBasic'), (339, 'complexityMCQ2'), (273, 'valley')]
b= [(23, 'ASCIIDecoder'), (9, 'AbstractClass'), (25, 'AccessModifiers'), (64, 'Array2D'), (48, 'BlackBox'), (6, 'BoundedBuffer'), (68, 'BubbleSortInvariant'), (38, 'Casting'), (57, 'CircularLL'), (15, 'CommonErrors'), (18, 'ComparatorAndCollections'), (45, 'ComparatorvsComparable'), (33, 'ComplexityArraySearch'), (42, 'ComplexityMCQ1'), (2, 'ComplexitySpaceMCQ'), (44, 'Coverage'), (20, 'CyclicBarrier'), (39, 'FList'), (27, 'FListMergeSort'), (16, 'FTree'), (41, 'Factory'), (18, 'Fibonacci'), (5, 'Future'), (9, 'Generics'), (6, 'Generics2'), (9, 'Generics3'), (23, 'HanoiTower'), (9, 'Inheritance'), (107, 'Introduction'), (6, 'LambdaExpressioninJava'), (22, 'LearnException'), (36, 'MakeMistakeToUnderstandThem'), (104, 'MaximumSumSubarray'), (99, 'MergeSortImplementation'), (134, 'MidTermQuiz'), (279, 'MidTermQuizMCQ'), (253, 'MidTermQuizMCQ2'), (46, 'MyArrayList'), (12, 'Observer'), (24, 'Optional'), (20, 'ParallelelMergeSort'), (31, 'ProducerConsumer'), (9, 'QueueWithStacks'), (5, 'SharedCounter'), (50, 'SieveOfEratosthenesImplementation'), (1, 'SieveOfEratosthenesMCQ'), (5, 'StackWithQueue'), (47, 'Streams'), (25, 'Streams2'), (52, 'StringUtils'), (3, 'ThreadsIntroduction'), (18, 'TreeCombineWith'), (24, 'TreeInorder'), (27, 'TreeSame'), (1, 'ValueOrReference'), (6, 'Visitor'), (18, 'VisitorBasic'), (17, 'complexityMCQ2'), (2, 'fail'), (63, 'valley')]
    

