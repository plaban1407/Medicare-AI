from flask import Flask, render_template, request, url_for
from preprocess import word_extractor, symptoms
from predict import cardio_predict, diabetes_predict, thyroid_predict
import pandas as pd

from flask_ngrok import run_with_ngrok


app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/symp_check')
def sym():
    return render_template('symp_check.html')

@app.route('/cardio_check')
def cardio():
    return render_template('cardio_check.html')

@app.route('/diabetes_check')
def diabetes():
    return render_template('diabetes_check.html')

@app.route('/thyroid_check')
def thyroid():
    return render_template('thyroid_check.html')

@app.route('/kidney_check')
def kidney():
    return render_template('kidney_check.html')



input_text = ''


@app.route('/your-cardio',methods = ['POST'])
def cardio_post():
    if request.method == 'POST':
        features = []
        age = request.form.get('age')
        features.append(age)
        sex = request.form.get('sex')
        features.append(sex)
        cp = request.form.get('cp')
        features.append(cp)
        trestbps = request.form.get('trestbps')
        features.append(trestbps)
        chol = request.form.get('chol')
        features.append(chol)
        fbs = request.form.get('fbs')
        features.append(fbs)
        restecg = request.form.get('restecg')
        features.append(restecg)
        thalach = request.form.get('thalach')
        features.append(thalach)
        exang = request.form.get('exang')
        features.append(exang)
        oldpeak = request.form.get('oldpeak')
        features.append(oldpeak)
        slope = request.form.get('slope')
        features.append(slope)
        ca = request.form.get('ca')
        features.append(ca)
        thal = request.form.get('thal')
        features.append(thal)
        cardio = cardio_predict(features)
        print(cardio)
        if (cardio==[0]):
            cardio = '0'
        elif (cardio==[1]):
            cardio = '1'
        elif (cardio==[2]):
            cardio = '2'
        elif (cardio==[3]):
            cardio = '3'
        elif (cardio == [4]):
            cardio = '4'
        return render_template('cardio.html', cardio = cardio)

@app.route('/your-diabetes', methods=['POST'])
def diabetes_post():
    if request.method == 'POST':
        features = []
        age = request.form.get('age')
        features.append(age)
        gender = request.form.get('gender')
        features.append(gender)
        Polyuria = request.form.get('Polyuria')
        features.append(Polyuria)
        Polydipsia = request.form.get('Polydipsia')
        features.append(Polydipsia)
        sudden_weight_loss = request.form.get('sudden_weight_loss')
        features.append(sudden_weight_loss)
        weakness = request.form.get('weakness')
        features.append(weakness)
        Polyphagia = request.form.get('Polyphagia')
        features.append(Polyphagia)
        Genital_thrush = request.form.get('Genital_thrush')
        features.append(Genital_thrush)
        visual_blurring = request.form.get('visual_blurring')
        features.append(visual_blurring)
        Itching = request.form.get('Itching')
        features.append(Itching)
        Irritability = request.form.get('Irritability')
        features.append(Irritability)
        delayed_healing = request.form.get('delayed_healing')
        features.append(delayed_healing)
        partial_paresis = request.form.get('partial_paresis')
        features.append(partial_paresis)
        muscle_stiffness = request.form.get('muscle_stiffness')
        features.append(muscle_stiffness)
        Alopecia = request.form.get('Alopecia')
        features.append(Alopecia)
        Obesity = request.form.get('Obesity')
        features.append(Obesity)
        diabetes = diabetes_predict(features)
        print(diabetes)
        if (diabetes == [0]):
            diabetes = '0'
        else:
            diabetes = '1'
        return render_template('diabetes.html', diabetes=diabetes)


@app.route('/your-thyroid', methods=['POST'])
def thyroid_post():
    print("Inside thyroid")
    #Class attribute (1 = normal, 2 = hyper, 3 = hypo)
    if request.method == 'POST':
        features = []
        t3_resin = request.form.get('t3_resin')
        features.append(t3_resin)
        serum_thyroxin = request.form.get('serum_thyroxin')
        features.append(serum_thyroxin)
        serum_triiodothyronine = request.form.get('serum_triiodothyronine')
        features.append(serum_triiodothyronine)
        tsh = request.form.get('tsh')
        features.append(tsh)
        ad_tsh = request.form.get('ad_tsh')
        features.append(ad_tsh)

        thyroid = thyroid_predict(features)
        print(thyroid)
        if (thyroid == [1]):
            thyroid = '1'
        elif (thyroid == [2]):
            thyroid = '2'
        elif (thyroid == [3]):
            thyroid = '3'
        return render_template('thyroid.html', thyroid=thyroid)

# @app.route('/your-kidney',methods = ['POST'])
# def kidney_post():
#     if request.method == 'POST':
#         features = []
#         age = request.form.get('age')
#         features.append(age)
#         al = request.form.get('al')
#         features.append(al)
#         ane = request.form.get('ane')
#         features.append(ane)
#         appet = request.form.get('appet')
#         features.append(appet)
#         bact = request.form.get('bact')
#         features.append(bact)
#         bg = request.form.get('bg')
#         features.append(bg)
#         bp = request.form.get('bp')
#         features.append(bp)
#         bu = request.form.get('bu')
#         features.append(bu)
#         cad = request.form.get('cad')
#         features.append(cad)
#         dm = request.form.get('dm')
#         features.append(dm)
#         hemp = request.form.get('hemp')
#         features.append(hemp)
#         htn = request.form.get('htn')
#         features.append(htn)
#         pc = request.form.get('pc')
#         features.append(pc)
#         pcc = request.form.get('pcc')
#         features.append(pcc)
#         pcv = request.form.get('pcv')
#         features.append(pcv)
#         pe = request.form.get('pe')
#         features.append(pe)
#         pot = request.form.get('pot')
#         features.append(pot)
#         rbc = request.form.get('rbc')
#         features.append(rbc)
#         rc = request.form.get('rc')
#         features.append(rc)
#         sc = request.form.get('sc')
#         features.append(sc)
#         sg = request.form.get('sg')
#         features.append(sg)
#         sod = request.form.get('sod')
#         features.append(sod)
#         su = request.form.get('su')
#         features.append(su)
#         wc = request.form.get('wc')
#         features.append(wc)
#         print(len(features))
#         kid = kidney_predict(features)
#         if (kid==[0.]):
#             kid = '0'
#         else:
#             kid = '1'
#         return render_template('kidney.html', kid = kid)


# @app.route('/your-bert-diease', methods=['POST'])
# def bert_post():
#     text = request.form.get('bert_symptoms_input')
#     df = pd.read_csv('dataset/dis_symp_prcoseessd.csv')
#     text = pre_processing(text)
#     results = bert_disease_predict(text)
#     number_top_matches = 10
#     diseases = []
#     item = []
#     i = 0
#     score = []
#     info = []
#     for idx, distance in results[0:number_top_matches]:
#         diseases.append(df['diseases'][idx])
#         score.append(1-distance)
#         i = i+1
#         item.append(i)
#         info.append(df['Overview'][idx])
#
#     return render_template('bert.html',prediction = diseases,item = item,similarity = score,summary = score,overview = info)

if __name__ == '__main__':
    app.run()
