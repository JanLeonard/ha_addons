from flask import Flask, render_template,request,redirect
import sqlite3




app = Flask(__name__)

@app.route('/orari', methods = ('GET','POST'))
def index():
    connection = sqlite3.connect('/share/flask-orari-lavoro/database.db')
    connection.row_factory = sqlite3.Row
    righe = connection.execute(
    'select * from PRESENZE order by giorno desc').fetchmany(5)
    totali = connection.execute('SELECT  STRFTIME("%m-%Y", giorno) AS Mese,  round(sum(case when pausa="Y" then (((cast(substr(orausci, 1, 2) as FLOAT)*60 + CAST(substr(orausci, 4, 4) as FLOAT))-(cast(substr(oranetr, 1, 2) as INT)*60 + CAST(substr(oranetr, 4, 4) as INT)))/60 -0.25) else (((cast(substr(orausci, 1, 2) as FLOAT)*60 + CAST(substr(orausci, 4, 4) as FLOAT))-(cast(substr(oranetr, 1, 2) as INT)*60 + CAST(substr(oranetr, 4, 4) as INT)))/60)   END),2) as Totore FROM PRESENZE GROUP BY STRFTIME("%m-%Y", giorno)').fetchall()
    connection.commit()
    connection.close()
    if request.method == 'POST':
       day = request.form['day']
       entr1 = request.form['entr1']
       usci1 = request.form['usci1']
       pausa = "N"
       if request.form.get('CheckB'):
              pausa = "Y"         
       #pausa = request.form['Check']
       #pausa = "N"
       #minusci = request.form['minusci']
       #giorno = request.form['giorno']
       #mese = request.form['mese']
       print(day)
       print(entr1)
       print(usci1)
       print(pausa)
       #print(minusci)
       #print(giorno)
       #print(mese)
       connection = sqlite3.connect('/share/flask-orari-lavoro/database.db')
       connection.row_factory = sqlite3.Row
       connection.execute(
       'INSERT INTO PRESENZE(oranetr,orausci,giorno,pausa) VALUES (?,?,?,?)', (entr1,usci1,day,pausa))
       connection.commit()
       connection.close()
       return redirect('/orari')
    return render_template('index.html', righe=righe , totali=totali)

	
@app.route('/orari/<int:idx>/delete', methods = ('GET','POST'))
def delete(idx):
    if request.method == 'POST':
       connection = sqlite3.connect('/share/flask-orari-lavoro/database.db')
       connection.row_factory = sqlite3.Row
       connection.execute('DELETE FROM PRESENZE where ID=?', (idx,))
       connection.commit()
       connection.close()
       return redirect('/orari')
    connection = sqlite3.connect('/share/flask-orari-lavoro/database.db')
    connection.row_factory = sqlite3.Row
    totali = connection.execute('SELECT * FROM PRESENZE where STRFTIME("%m-%Y", giorno)=?', (idx1,)).fetchall()
    connection.commit()
    connection.close()
    return render_template('remove.html', totali=totali)

@app.route('/orari/<string:idx1>/mesi', methods = ('GET','POST'))
def mesi(idx1):
    connection = sqlite3.connect('/share/flask-orari-lavoro/database.db')
    connection.row_factory = sqlite3.Row
    totali = connection.execute('SELECT * FROM PRESENZE where STRFTIME("%m-%Y", giorno)=?', (idx1,)).fetchall()
    connection.commit()
    connection.close()
    return render_template('months.html', totali=totali)

@app.route('/orari/inserisci', methods = ('GET','POST'))
def inserisci():
    if request.method == 'POST':
       day = request.form['day']
       entr1 = request.form['entr1']
       usci1 = request.form['usci1']
       pausa = "N"
       if request.form.get('CheckB'):
              pausa = "Y"         
       #pausa = request.form['Check']
       #pausa = "N"
       #minusci = request.form['minusci']
       #giorno = request.form['giorno']
       #mese = request.form['mese']
       print(day)
       print(entr1)
       print(usci1)
       print(pausa)
       #print(minusci)
       #print(giorno)
       #print(mese)
       connection = sqlite3.connect('/share/flask-orari-lavoro/database.db')
       connection.row_factory = sqlite3.Row
       connection.execute(
       'INSERT INTO PRESENZE(oranetr,orausci,giorno,pausa) VALUES (?,?,?,?)', (entr1,usci1,day,pausa))
       connection.commit()
       connection.close()
       return redirect('/orari')
    return render_template('insert.html')

@app.route('/orari/rimuovi', methods = ('GET','POST'))
def rimuovi():
    connection = sqlite3.connect('/share/flask-orari-lavoro/database.db')
    connection.row_factory = sqlite3.Row
    totali = connection.execute('select * from PRESENZE order by id desc').fetchmany(45)
    connection.commit()
    connection.close()
    return render_template('remove.html', totali=totali)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8139, debug=True)