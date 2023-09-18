from flask import Flask,redirect,url_for,render_template,request
import numpy as np
from sklearn import *
import pickle


model = pickle.load(open('model.plk','rb'))

app=Flask(__name__,template_folder='templetes')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():
    cap_shape = float(request.form.get('cap-shape'))
    cap_surface = float(request.form.get('cap-surface'))
    cap_color = float(request.form.get('cap-color'))
    bruises   = float(request.form.get('bruises'))
    odor = float(request.form.get('odor'))
    gill_attachment = float(request.form.get('gill-attachment'))
    gill_spacing = float(request.form.get('gill-spacing'))
    gill_size = float(request.form.get('gill-size'))
    gill_color = float(request.form.get('gill-color'))
    stalk_shape = float(request.form.get('stalk-shape'))
    stalk_root = float(request.form.get('stalk-root'))
    stalk_surface_above_ring = float(request.form.get('stalk-surface-above-ring'))
    stalk_surface_below_ring = float(request.form.get('stalk-surface-below-ring'))  
    stalk_color_above_ring = float(request.form.get('stalk-color-above-ring'))  
    stalk_color_below_ring = float(request.form.get('stalk-color-below-ring'))  
    veil_color = float(request.form.get('veil-color'))
    ring_number = float(request.form.get('ring-number'))
    ring_type = float(request.form.get('ring-type'))
    spore_print_color = float(request.form.get('spore-print-color'))
    population = float(request.form.get('population'))
    habitat = float(request.form.get('habitat'))
    r = np.array([cap_shape,cap_surface,cap_color,bruises,
                                     odor,gill_attachment,gill_spacing,
                                     gill_size,
                                     gill_color,stalk_shape,stalk_root, 
                                     stalk_surface_below_ring,
                                     stalk_surface_above_ring,stalk_color_above_ring,stalk_color_below_ring,
                                     veil_color,ring_number,
                                     ring_type,spore_print_color,population,habitat]).reshape(-1, 1).transpose()
    re = model.predict(r)
    result = round(re[0],2)
    
    if result == 0:
        result= 'ediable'
    elif result == 1:
        result = 'posion'
    else:
        result = 'error'

    
    return render_template('index.html',result="Your mushroom is {res}!".format(res=result))

if __name__ == '__main__':
    app.run(host = "127.0.0.1",port=8080 ,debug=True)