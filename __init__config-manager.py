# This Python file uses the following encoding: utf-8
from flask import Flask, render_template, g, redirect, url_for
from SqlServer import MSSQL
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

ms = MSSQL(host="localhost",user="sa",pwd="richeninfo",db="config_manager")

app = Flask(__name__)

@app.route('/index')
def index():
    rzDCProjects = ms.ExecQuery("select id as value,project_name as text from rz_dc_project order by id")
    for item in rzDCProjects:
        print item

    sqlForGatherIssues = '''
        select i.id, i.issue_project, i.issue_net_name
        from rz_dc_gather_issue i join rz_dc_project p
        on i.issue_project=p.id
        where i.issue_status!='ok'
        order by issue_add_date desc
    '''

    gatherIssues = ms.ExecQuery(sqlForGatherIssues)
    weekedAdd = []
    weekedAdd.append({
        'project_name' : u'永安',
        'net_name' : u'化工在线',
        'add_date' : '2013/6/4'
    })
    weekedAdd.append({
        'project_name' : u'永安',
        'net_name' : u'卓创资讯-塑料',
        'add_date' : '2013/6/4'
    })
    weekedAdd.append({
        'project_name' : u'永安',
        'net_name' : u'中国煤炭资源网',
        'add_date' : '2013/6/4'
    })
    weekedAdd.append({
        'project_name' : u'永安',
        'net_name' : u'中国化纤信息网',
        'add_date' : '2013/6/4'
    })
    weekedAdd.append({
        'project_name' : u'永安',
        'net_name' : u'广西糖网',
        'add_date' : '2013/6/4'
    })

    ret = {
        'weeked_untreated' : 5,
        'weeked_total' : 10,
        'history_total' : 4,
        'weekedAdd' : gatherIssues,
        "rzDCProjects" : rzDCProjects
    }
    g.untreated = 3
    return render_template('index.html', **ret)

@app.route('/addGatherIssue')
def addGatherIssue():
    return 'here'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
