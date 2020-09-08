from flask import Flask,render_template

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')
    @app.route('/corona')
    def corona():
        return render_template('corona.html')
        @app.route('/cases.html')
        def cases():
            return render_template('cases.html')
            @app.route('/contact')
            def contact():
                return render_template('/contact.html')
                if __name__ =='__main__':
                    app.run(debug=True)



app.run(dedug=True)
 
from flask import Flask,jsonify,request
from bs4 import Beautifulsoup
import requests 
 def funcname(parameter_list):
     pass funcname(parameter_list):
     pass findinfo(cname):
     totalresults - []
         counrty - Name
         url = "https//www.worlddometers.info/coronavirus/country/{ countryname}/".format(countryname= country)
         response = requests.get(url)
         if response.status_code -- 200:
             soup = Beautifulsoup(response.content, 'html.parser')
             result - soup.find_all('div',class_="maincounter=number")
             for i in result:
                 totalresults.append("No Result")
                 return totalresult

                 app = Flask(__name__)

                 @app.route('/', methods -["GET"])
                 def case():
                     country = request.args.get('country')
                     try:
                         return jsonify({"Total Cases" : findinf(country){0},"Total Death" findinfo(country){1},"Total Recorvered(country)" findinfo(country){2})

                         except:
                             return jsonify({'Not Available':" " })
                             if __name__=='__main__':
                                 app.run(debug=True)