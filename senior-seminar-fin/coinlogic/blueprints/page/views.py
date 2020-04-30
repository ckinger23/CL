from flask import Flask, flash, Blueprint, render_template, request
import os
page = Blueprint('page', __name__, template_folder='templates')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')

def parse_txt():
    cikTable = {}
    companyNames = []
    with open(os.path.join(APP_STATIC, 'companies.txt')) as f:
        companies = f.readlines()
        for line in companies:
            splitUp = line.split(': ')
            companyNames.append(splitUp[0])
            compName = splitUp[0].rstrip()
            compCIK = splitUp[1].rstrip()
            cikTable[compName] = compCIK
    return companyNames, cikTable


@page.route('/')
def home():
    return render_template('page/home.html')


@page.route('/dashboard', methods =['GET', 'POST'])
def dashboard():
    companyNames, cikTable = parse_txt()
    if request.method == 'POST':
        company = request.form.get('company')
        flash(str(company))
    if request.method == 'GET':
        company = request.args.get('company')
        flash(str(company))
    return render_template('page/dashboard.html', companies=companyNames)


@page.route('/learn')
def learn():
    return render_template('page/learn.html')
