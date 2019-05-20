from flask import Flask, render_template, request, url_for, redirect, send_file
import titanic

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Index'
    
@app.route('/titanicmenu',methods=['GET','POST'])
def titanicmenu():
    
    outputType = request.form.get('outputtype')
    
    sourcePath = 'train.csv'
    
    if request.method == 'POST':
        
        if  outputType == 'Reverse':
            
            outputPath = 'output/reversed.csv'
            
            rawDat = titanic.openAndParse(sourcePath)
            revList = titanic.reverseList(rawDat[0])
            reversedCols = titanic.rearrangeList(rawDat,revList)
            titanic.writeFile(reversedCols,outputPath)
            
            
            return send_file(outputPath, as_attachment=True)
        
        elif outputType == 'Every Other':
            
            outputPath = 'output/everyother.csv'
            
            rawDat = titanic.openAndParse(sourcePath)
            alternateList = titanic.everyOther(rawDat[0])
            everyOtherCol = titanic.rearrangeList(rawDat, alternateList)
            titanic.writeFile(everyOtherCol,outputPath)
            
            return send_file(outputPath, as_attachment=True)
        
    else:
        
        return render_template('titanic.html')

@app.route('/yahoomenu')
def yahoo():
    return 'Yahoo API not available'



if __name__ == '__main__':
    app.run(host='0.0.0.0',port='80')