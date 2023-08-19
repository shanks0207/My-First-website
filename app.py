from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
   'id' : 1,
   'title' : 'Data Analyst',
   'location' : 'Bangloro, India',
   'salary' : 'Rs. 15,00,000'    
  },
  {
   'id' : 2,
   'title' : 'Data Scientist',
   'location' : 'Sydney, Austrilia',
   
  },
  {
   'id' : 3,
   'title' : 'Frontend Engineer',
   'location' : 'London, United Kingdom',
   'salary' : 'Rs. 11,00,000'    
  },
  {
   'id' : 4,
   'title' : 'Backend Engineer',
   'location' : 'Bhaktapur, Nepal',
   'salary' : '$12,00,000'    
  },
  {
   'id' : 5,
   'title' : 'MERN Stack',
   'location' : 'New York, United States',
   'salary' : '$18,00,000'    
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs = JOBS,
                         company_name = "Jovian" #passing name to HTML templates
                        )
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)