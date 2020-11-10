from flask import Flask, render_template
import csv

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/atlanticsim', methods=['GET'])
def atlanticsim():
    bosplayers = []
    with open('Boston.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Rk': row[0]}
            rowDict.update(d0)
            d1 = {'Name': row[1]}
            rowDict.update(d1)
            d6 = {'PTS': row[6]}
            rowDict.update(d6)
            d2 = {'TRB': row[2]}
            rowDict.update(d2)
            d3 = {'AST': row[3]}
            rowDict.update(d3)
            d4 = {'STL': row[4]}
            rowDict.update(d4)
            d5 = {'BLK': row[5]}
            rowDict.update(d5)
            bosplayers.append(rowDict)
        bosplayers.pop(0)
    bknplayers = []
    with open('Brooklyn.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Rk': row[0]}
            rowDict.update(d0)
            d1 = {'Name': row[1]}
            rowDict.update(d1)
            d6 = {'PTS': row[6]}
            rowDict.update(d6)
            d2 = {'TRB': row[2]}
            rowDict.update(d2)
            d3 = {'AST': row[3]}
            rowDict.update(d3)
            d4 = {'STL': row[4]}
            rowDict.update(d4)
            d5 = {'BLK': row[5]}
            rowDict.update(d5)
            bknplayers.append(rowDict)
        bknplayers.pop(0)
    nykplayers = []
    with open('NewYork.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Rk': row[0]}
            rowDict.update(d0)
            d1 = {'Name': row[1]}
            rowDict.update(d1)
            d6 = {'PTS': row[6]}
            rowDict.update(d6)
            d2 = {'TRB': row[2]}
            rowDict.update(d2)
            d3 = {'AST': row[3]}
            rowDict.update(d3)
            d4 = {'STL': row[4]}
            rowDict.update(d4)
            d5 = {'BLK': row[5]}
            rowDict.update(d5)
            nykplayers.append(rowDict)
        nykplayers.pop(0)
    phiplayers = []
    with open('Philadelphia.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Rk': row[0]}
            rowDict.update(d0)
            d1 = {'Name': row[1]}
            rowDict.update(d1)
            d6 = {'PTS': row[6]}
            rowDict.update(d6)
            d2 = {'TRB': row[2]}
            rowDict.update(d2)
            d3 = {'AST': row[3]}
            rowDict.update(d3)
            d4 = {'STL': row[4]}
            rowDict.update(d4)
            d5 = {'BLK': row[5]}
            rowDict.update(d5)
            phiplayers.append(rowDict)
        phiplayers.pop(0)
    torplayers = []
    with open('Toronto.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Rk': row[0]}
            rowDict.update(d0)
            d1 = {'Name': row[1]}
            rowDict.update(d1)
            d6 = {'PTS': row[6]}
            rowDict.update(d6)
            d2 = {'TRB': row[2]}
            rowDict.update(d2)
            d3 = {'AST': row[3]}
            rowDict.update(d3)
            d4 = {'STL': row[4]}
            rowDict.update(d4)
            d5 = {'BLK': row[5]}
            rowDict.update(d5)
            torplayers.append(rowDict)
        torplayers.pop(0)
    atlallplayers = []
    with open('AtlanticAll.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d1 = {'WS': row[1]}
            rowDict.update(d1)
            atlallplayers.append(rowDict)
        atlallplayers.pop(0)
    return render_template('atlanticsim.html', bosplayers=bosplayers, bknplayers=bknplayers, nykplayers=nykplayers,
                           phiplayers=phiplayers, torplayers=torplayers, atlallplayers=atlallplayers)


@app.route('/centralsim', methods=['GET'])
def centralsim():
    chiplayers = []
    with open('Chicago.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            chiplayers.append(rowDict)
        chiplayers.pop(0)
    cleplayers = []
    with open('Cleveland.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            cleplayers.append(rowDict)
        cleplayers.pop(0)
    detplayers = []
    with open('Detroit.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            detplayers.append(rowDict)
        detplayers.pop(0)
    indplayers = []
    with open('Indiana.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            indplayers.append(rowDict)
        indplayers.pop(0)
    milplayers = []
    with open('Milwaukee.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            milplayers.append(rowDict)
        milplayers.pop(0)
    cenallplayers = []
    with open('CentralAll.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d1 = {'WS': row[1]}
            rowDict.update(d1)
            cenallplayers.append(rowDict)
        cenallplayers.pop(0)
    return render_template('centralsim.html', chiplayers=chiplayers, cleplayers=cleplayers, detplayers=detplayers,
                           indplayers=indplayers, milplayers=milplayers, cenallplayers=cenallplayers)


@app.route('/southeastsim', methods=['GET'])
def southeastsim():
    atlplayers = []
    with open('Atlanta.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            atlplayers.append(rowDict)
        atlplayers.pop(0)
    chaplayers = []
    with open('Charlotte.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            chaplayers.append(rowDict)
        chaplayers.pop(0)
    miaplayers = []
    with open('Miami.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            miaplayers.append(rowDict)
        miaplayers.pop(0)
    orlplayers = []
    with open('Orlando.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            orlplayers.append(rowDict)
        orlplayers.pop(0)
    wasplayers = []
    with open('Washington.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            wasplayers.append(rowDict)
        wasplayers.pop(0)
    steallplayers = []
    with open('SoutheastAll.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d1 = {'WS': row[1]}
            rowDict.update(d1)
            steallplayers.append(rowDict)
        steallplayers.pop(0)
    return render_template('southeastsim.html', atlplayers=atlplayers, chaplayers=chaplayers, miaplayers=miaplayers,
                           orlplayers=orlplayers, wasplayers=wasplayers, steallplayers=steallplayers)


@app.route('/northwestsim', methods=['GET'])
def northwestsim():
    denplayers = []
    with open('Denver.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            denplayers.append(rowDict)
        denplayers.pop(0)
    minplayers = []
    with open('Minnesota.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            minplayers.append(rowDict)
        minplayers.pop(0)
    okcplayers = []
    with open('OklahomaCity.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            okcplayers.append(rowDict)
        okcplayers.pop(0)
    porplayers = []
    with open('Portland.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            porplayers.append(rowDict)
        porplayers.pop(0)
    utaplayers = []
    with open('Utah.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            utaplayers.append(rowDict)
        utaplayers.pop(0)
    norallplayers = []
    with open('NorthwestAll.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d1 = {'WS': row[1]}
            rowDict.update(d1)
            norallplayers.append(rowDict)
        norallplayers.pop(0)
    return render_template('northwestsim.html', denplayers=denplayers, minplayers=minplayers, okcplayers=okcplayers,
                           porplayers=porplayers, utaplayers=utaplayers, norallplayers=norallplayers)


@app.route('/pacificsim', methods=['GET'])
def pacificsim():
    gswplayers = []
    with open('GoldenState.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            gswplayers.append(rowDict)
        gswplayers.pop(0)
    lacplayers = []
    with open('LosAngelesClippers.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            lacplayers.append(rowDict)
        lacplayers.pop(0)
    lalplayers = []
    with open('LosAngelesLakers.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            lalplayers.append(rowDict)
        lalplayers.pop(0)
    phoplayers = []
    with open('Phoenix.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            phoplayers.append(rowDict)
        phoplayers.pop(0)
    sacplayers = []
    with open('Sacramento.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            sacplayers.append(rowDict)
        sacplayers.pop(0)
    pacallplayers = []
    with open('PacificAll.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d1 = {'WS': row[1]}
            rowDict.update(d1)
            pacallplayers.append(rowDict)
        pacallplayers.pop(0)
    return render_template('pacificsim.html', gswplayers=gswplayers, lacplayers=lacplayers, lalplayers=lalplayers,
                           phoplayers=phoplayers, sacplayers=sacplayers, pacallplayers=pacallplayers)


@app.route('/southwestsim', methods=['GET'])
def southwestsim():
    dalplayers = []
    with open('Dallas.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            dalplayers.append(rowDict)
        dalplayers.pop(0)
    houplayers = []
    with open('Houston.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            houplayers.append(rowDict)
        houplayers.pop(0)
    memplayers = []
    with open('Memphis.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            memplayers.append(rowDict)
        memplayers.pop(0)
    nolplayers = []
    with open('NewOrleans.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            nolplayers.append(rowDict)
        nolplayers.pop(0)
    sasplayers = []
    with open('SanAntonio.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d5 = {'PTS': row[5]}
            rowDict.update(d5)
            d1 = {'TRB': row[1]}
            rowDict.update(d1)
            d2 = {'AST': row[2]}
            rowDict.update(d2)
            d3 = {'STL': row[3]}
            rowDict.update(d3)
            d4 = {'BLK': row[4]}
            rowDict.update(d4)
            sasplayers.append(rowDict)
        sasplayers.pop(0)
    stwallplayers = []
    with open('SouthwestAll.csv') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rowDict = {}
            d0 = {'Name': row[0]}
            rowDict.update(d0)
            d1 = {'WS': row[1]}
            rowDict.update(d1)
            stwallplayers.append(rowDict)
        stwallplayers.pop(0)
    return render_template('southwestsim.html', dalplayers=dalplayers, houplayers=houplayers, memplayers=memplayers,
                           nolplayers=nolplayers, sasplayers=sasplayers, stwallplayers=stwallplayers)


if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True