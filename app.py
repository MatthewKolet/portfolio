from flask import Flask, redirect, request, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', pageTitle= "Home")

@app.route('/about')
def about():
    return render_template('mike.html', pageTitle="About")

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = form['radius']
        height = form['height']
        radius = float(radius)
        height = float(height)
        top_area = 3.14 * radius**2
        sides_area = 2*3.14*radius*height
        total_area = top_area + sides_area
        total_sqft = total_area / 144
        material_cost = 25 
        total_material_cost = total_sqft * material_cost
        labor_cost = 15
        total_labor_cost = labor_cost * total_sqft
        total_cost_estimate = total_material_cost + total_labor_cost
        total_cost_estimate = round(total_cost_estimate, 2)
        total_cost_estimate = str(total_cost_estimate)
        return(render_template('estimate.html', quote=total_cost_estimate))
    return(render_template('estimate.html', pageTitle="Estimate")) 

if __name__ == '__main__':
    app.run(debug=True)