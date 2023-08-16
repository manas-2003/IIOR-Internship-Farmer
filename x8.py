from flask import *
import mysql.connector
app = Flask(__name__)
mydb = mysql.connector.connect(host="localhost",user="root", password="pass123", database="fpo")
cursor=mydb.cursor()
app.secret_key='manas'
@app.route("/",methods=['GET','POST'])
def save_location():
    if(request.method=="POST"):
        village=request.form.get("village")
        Mandal=request.form.get("mandal")
        panchayath=request.form.get("panchayat")
        district=request.form.get("district")
        session['v1']=village
        session['v2']=Mandal
        cursor.execute("insert  into fpo.full_final(village,mandal,panchayat,district) values(%s, %s,%s,%s)", (village,Mandal,panchayath,district))
        session['id'] = cursor.lastrowid
        mydb.commit()
        return redirect("/information")
    return render_template('location.html')
@app.route("/team",methods=['GET','POST'])
def team_move():
    # if (request.method == "POST"):
    #     return redirect("/")
    return render_template('team.html')
@app.route("/back",methods=['GET','POST'])
def back_move():
    return redirect(url_for('save_location'))
@app.route("/information",methods=['GET','POST'])
def save_information():
    if (request.method == "POST"):
        Name = request.form.get("Name_of_FPO_member")
        Adhar = request.form.get("Aadhar_Number")
        Age= request.form.get("Age")
        Mobile= request.form.get("Mobile_NUmber")
        Familyma = request.form.get("Familymale")
        familfem = request.form.get("Familyfemale")
        familchil = request.form.get("Familychil")
        social = request.form.get("Group")
        engma = request.form.get("engaged")
        engfem = request.form.get("engagedfem")
        education = request.form.get("Education_level")
        religion = request.form.get("Religion")
        v1 = session.get('v1',str)
        v2 = session.get('v2',str)
        session['v3']=Name
        v3 = session.get('v3',str)
        id = session.get('id',int)
        # cursor.execute("insert  into fpo.general_information values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
        # id,v1,v2,Name, Adhar, Age, Mobile, Familyma, familfem, familchil, social, engma, engfem, education, religion))
        cursor.execute(
            "update full_final set name=%s,aadhar = %s,age=%s,mobile=%s,familymale=%s,familyfemale=%s,familychild=%s,social=%s,engamale=%s,engafemale=%s,education=%s,religion=%s where farmer_id=%s",
            (Name,Adhar, Age, Mobile, Familyma, familfem, familchil, social, engma, engfem, education, religion,id))
        mydb.commit()
        return redirect("/farmerholdings")
    return render_template('general.html')
@app.route("/farmerholdings",methods=['GET','POST'])
def save_holdings():
    if (request.method == "POST"):
        ownedrain = request.form.get("ownedrain")
        leasedrain = request.form.get("leasedrain")
        soilrain= request.form.get("rainsoil")
        totalrain= request.form.get("totalrain")
        ownedirrigated = request.form.get("ownedirrigated")
        leasedirrigated = request.form.get("leasedirrigated")
        soilirrigated = request.form.get("irrigatedsoil")
        totalirrigated = request.form.get("totalirrgated")
        totalowned = request.form.get("ownedtotal")
        totalleased= request.form.get("leasedtotal")
        totalarea = request.form.get("Total")
        v1 = session.get('v1', str)
        v2 = session.get('v2', str)
        v3 = session.get('v3', str)
        id = session.get('id', int)
        # cursor.execute("insert  into fpo.holdings values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,v1,v2,v3,ownedrain,leasedrain,soilrain,totalrain,ownedirrigated,
        # leasedirrigated,soilirrigated,totalirrigated,totalowned,totalleased,totalarea))
        cursor.execute(
            "update full_final set ownedrain=%s, leasedrain=%s, soilrain=%s, totalrain=%s, irriowned=%s, leasedirri=%s, soilirri=%s, totalirri=%s, totalowned=%s, totalleased=%s, totaltotal=%s where farmer_id=%s",
            (ownedrain, leasedrain, soilrain, totalrain,ownedirrigated, leasedirrigated, soilirrigated, totalirrigated, totalowned, totalleased, totalarea,id))
        mydb.commit()
        return redirect("/livestock")
    return render_template('Farmerholdings.html')
@app.route("/livestock",methods=['GET','POST'])
def save_stock():
    if (request.method == "POST"):
        livecow = request.form.get("lcow")
        livebuffalo = request.form.get("lbuffalo")
        livebullock = request.form.get("lbullock")
        livesheep = request.form.get("lsheep")
        livepoultry = request.form.get("lpoultry")
        liveother = request.form.get("lother")
        sourcow = request.form.get("scows")
        sourbuffalo = request.form.get("sbuffalos")
        sourbullock = request.form.get("sbullocks")
        soursheep = request.form.get("ssheeps")
        sourpoultry = request.form.get("spoultrys")
        sourother= request.form.get("sothers")
        v1 = session.get('v1', str)
        v2 = session.get('v2', str)
        v3 = session.get('v3', str)
        id = session.get('id', int)
        # cursor.execute("insert into fpo.livestock values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        # (id,v1,v2,v3,livecow, livebuffalo, livebullock,livesheep, livepoultry, liveother,sourcow,sourbuffalo,sourbullock, soursheep,sourpoultry,sourother))
        cursor.execute(
            "update full_final set livecow=%s,livebuffalo=%s,livebullock=%s,livesheep=%s,livepoultry=%s,liveother=%s,sourcecow=%s,sourcebuffalo=%s,sourcebullock=%s,sourcesheep=%s,sourcepoultry=%s,sourceother=%s where farmer_id=%s",
            (livecow, livebuffalo, livebullock, livesheep, livepoultry, liveother, sourcow, sourbuffalo, sourbullock,
             soursheep, sourpoultry, sourother, id))
        mydb.commit()
        return redirect('/farm')
    return render_template("livestock.html")
@app.route("/farm",methods=['GET','POST'])
def save_farm():
    if(request.method == "POST"):
        x = request.form.getlist('mytext1[]')
        y = request.form.getlist('mytext2[]')
        v1 = session.get('v1', str)
        v2 = session.get('v2', str)
        v3 = session.get('v3', str)
        id = session.get('id', int)
        for i in range(len(x)):
            a = "asset"+str(i+1)
            b = "source"+str(i+1)
            cursor.execute("update full_final set {m} = %s,{n} = %s where farmer_id = %s".format(m = a, n = b),(x[i],y[i],id))
        mydb.commit()
        return redirect("/labour")
    return render_template('farm.html')
@app.route("/labour",methods=['GET','POST'])
def save_labour():
    if (request.method == "POST"):
        wagemale= request.form.get("male")
        wagefemale = request.form.get("female")
        Hirincattle = request.form.get("cattle")
        Hirintractor = request.form.get("tractor")
        Hirinimplements = request.form.get("implements")
        Hirinspray = request.form.get("spray")
        v1 = session.get('v1', str)
        v2 = session.get('v2', str)
        v3 = session.get('v3', str)
        id = session.get('id', int)
        #cursor.execute("insert  into fpo.labour values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (id,v1,v2,v3,wagemale, wagefemale, Hirincattle, Hirintractor,Hirinimplements,Hirinspray))
        cursor.execute(
            "update full_final set wagemale=%s, wagefemale=%s, hiringcattle=%s, hiringtractor=%s, hiringimplement=%s, hiringspray=%s where farmer_id=%s",
            (wagemale, wagefemale, Hirincattle, Hirintractor, Hirinimplements, Hirinspray,id))
        mydb.commit()
        return redirect("/crop")
    return render_template('wages.html')
@app.route('/crop', methods=["POST", "GET"])
def crop():
       if request.method == 'POST':
           field = request.form.getlist('mytext1[]')
           crop_names = request.form.getlist('mytext2[]')
           variety = request.form.getlist('mytext3[]')
           Area_sown = request.form.getlist('mytext4[]')
           Rainfed = request.form.getlist('mytext5[]')
           source = request.form.getlist('mytext6[]')
           Method = request.form.getlist('mytext7[]')
           production = request.form.getlist('mytext8[]')
           price = request.form.getlist('mytext9[]')
           mode = request.form.getlist('mytext10[]')
           sowmonth = request.form.getlist('mytext11[]')
           harvmonth = request.form.getlist('mytext12[]')
           v1 = session.get('v1', str)
           v2 = session.get('v2', str)
           v3 = session.get('v3', str)
           id = session.get('id', int)
           # cursor.execute("insert into crop(farmer_id,village,mandal,name) values(%s,%s,%s,%s)", (id,v1,v2,v3))
           # cursor.execute("insert into input_costs(farmer_id,village,mandal,name) values(%s,%s,%s,%s)", (id,v1, v2, v3))
           # cursor.execute("insert into marketing_costs(farmer_id,village,mandal,name) values(%s,%s,%s,%s)", (id,v1, v2, v3))
           for i in range(len(field)):
               cursor.execute(
                   "update full_final set  {x1}=%s,{x2}=%s,{x3}=%s,{x4}=%s,{x5}=%s,{x6}=%s,{x7}=%s,{x8}=%s,{x9}=%s,{x10}=%s,{x11}=%s,{x12}=%s where farmer_id = %s ".format(
                       x1="field" + str(i + 1), x2="crop_name" + str(i + 1), x3="variety" + str(i + 1),
                       x4="area_sown" + str(i + 1), x5="rainfed" + str(i + 1), x6="source" + str(i + 1),
                       x7="method" + str(i + 1), x8="production" + str(i + 1), x9="price" + str(i + 1),
                       x10="mode" + str(i + 1), x11="sowmonth" + str(i + 1), x12="harvestmonth" + str(i + 1)), (
                   field[i], crop_names[i], variety[i], Area_sown[i], Rainfed[i], source[i], Method[i], production[i],
                   price[i], mode[i], sowmonth[i], harvmonth[i], id))
           crop_names = request.form.getlist('mytext2[]')
           session['my_list'] = crop_names
           session['count'] = -1
           mydb.commit()
           return  redirect('/sample_input_costs')
       return render_template('crop_management.html')
@app.route("/sample_input_costs",methods=['GET','POST'])
def farm_accept():
    v1 = session.get('v1', str)
    v2 = session.get('v2', str)
    v3 = session.get('v3', str)
    items = session.get('my_list', [])
    ct = session.get('count', int)
    id = session.get('id', int)
    if request.method=="POST":
        sq = request.form.get("sq")
        su = request.form.get("su")
        ss = request.form.get("ss")
        sa = request.form.get("sa")
        #cursor.execute("insert into fpo.input_costs_seed values(%s,%s,%s,%s)",(sq,su,ss,sa))
        cursor.execute(
            "update full_final set {i1}=%s,{i2}=%s,{i3}=%s,{i4}=%s,{i5}=%s where farmer_id = %s".format(
                i1="crop"+str(ct + 1),i2="seed_quantity" + str(ct + 1), i3="seed_price" + str(ct + 1),
                i4="seed_source" + str(ct + 1), i5="seed_address" + str(ct + 1)), (items[ct], sq, su, ss, sa, id))
        fq = request.form.get("fq")
        fu = request.form.get("fu")
        fs = request.form.get("fs")
        fa = request.form.get("fa")
        #cursor.execute("insert into fpo.input_costs_fym values(%s,%s,%s,%s)", (fq, fu, fs, fa))
        cursor.execute(
            "update full_final set {i1}=%s,{i2}=%s,{i3}=%s,{i4}=%s where farmer_id = %s".format(
                i1="fym_quantity" + str(ct + 1), i2="fym_price" + str(ct + 1), i3="fym_source" + str(ct + 1),
                i4="fym_address" + str(ct + 1)), (fq, fu, fs, fa, id))
        mytext0=request.form.getlist("mytext0[]")
        mytext1=request.form.getlist("mytext1[]")
        mytext2 = request.form.getlist("mytext2[]")
        mytext3 = request.form.getlist("mytext3[]")
        mytext4 = request.form.getlist("mytext4[]")
        for i in range(len(mytext0)):
            #cursor.execute("insert into fpo.input_costs_fertilizers values(%s,%s,%s,%s,%s)",(mytext0[i],mytext1[i],mytext2[i],mytext3[i],mytext4[i]))
            cursor.execute(
                "update full_final set {i1}=%s,{i2}=%s,{i3}=%s,{i4}=%s,{i5}=%s where farmer_id = %s".format(
                    i1="ferti_name" + str(ct + 1) + "_" + str(ct + i + 1),
                    i2="ferti_quantity" + str(ct + 1) + "_" + str(ct + i + 1),
                    i3="ferti_price" + str(ct + 1) + "_" + str(ct + i + 1),
                    i4="ferti_source" + str(ct + 1) + "_" + str(ct + i + 1),
                    i5="ferti_address" + str(ct + 1) + "_" + str(ct + i + 1)),
                (mytext0[i], mytext1[i], mytext2[i], mytext3[i], mytext4[i], id))
        plantText0 = request.form.getlist("plantText0[]")
        plantText1 = request.form.getlist("plantText1[]")
        plantText2 = request.form.getlist("plantText2[]")
        plantText3 = request.form.getlist("plantText3[]")
        plantText4 = request.form.getlist("plantText4[]")
        for i in range(len(plantText0)):
            #cursor.execute("insert into fpo.input_costs_chemicals values(%s,%s,%s,%s,%s)",(plantText0[i],plantText1[i],plantText2[i],plantText3[i],plantText4[i]))
            cursor.execute(
                "update full_final set {i1}=%s,{i2}=%s,{i3}=%s,{i4}=%s,{i5}=%s where farmer_id = %s".format(
                    i1="chemi_name" + str(ct + 1) + "_" + str(ct + i + 1),
                    i2="chemi_quantity" + str(ct + 1) + "_" + str(ct + i + 1),
                    i3="chemi_price" + str(ct + 1) + "_" + str(ct + i + 1),
                    i4="chemi_source" + str(ct + 1) + "_" + str(ct + i + 1),
                    i5="chemi_address" + str(ct + 1) + "_" + str(ct + i + 1)),
                (plantText0[i],plantText1[i],plantText2[i],plantText3[i],plantText4[i], id))
        herbicidesText0 = request.form.getlist("herbicidesText0[]")
        herbicidesText1 = request.form.getlist("herbicidesText1[]")
        herbicidesText2 = request.form.getlist("herbicidesText2[]")
        herbicidesText3 = request.form.getlist("herbicidesText3[]")
        herbicidesText4 = request.form.getlist("herbicidesText4[]")
        for i in range(len(herbicidesText0)):
            cursor.execute(
                "update full_final set {i1}=%s,{i2}=%s,{i3}=%s,{i4}=%s,{i5}=%s where farmer_id = %s".format(
                    i1="herbi_name" + str(ct + 1) + "_" + str(ct + i + 1),
                    i2="herbi_quantity" + str(ct + 1) + "_" + str(ct + i + 1),
                    i3="herbi_price" + str(ct + 1) + "_" + str(ct + i + 1),
                    i4="herbi_source" + str(ct + 1) + "_" + str(ct + i + 1),
                    i5="herbi_address" + str(ct + 1) + "_" + str(ct + i + 1)),
                (herbicidesText0[i], herbicidesText1[i], herbicidesText2[i], herbicidesText3[i], herbicidesText4[i], id))
        oq = request.form.get("oq")
        ou = request.form.get("ou")
        os = request.form.get("os")
        oa = request.form.get("oa")
        #cursor.execute("insert into fpo.input_costs_others values(%s,%s,%s,%s)", (oq, ou, os, oa))
        cursor.execute(
            "update full_final set {i1}=%s,{i2}=%s,{i3}=%s,{i4}=%s where farmer_id = %s".format(
                i1="other_quantity" + str(ct + 1), i2="other_price" + str(ct + 1), i3="other_source" + str(ct + 1),
                i4="other_address" + str(ct + 1)), (oq, ou, os, oa, id))
        mydb.commit()
        return redirect('/marketing_costs')
    ct += 1
    session['count'] = ct
    return render_template('sample_input_costs.html',x1=items[ct])
@app.route("/marketing_costs",methods=['GET','POST'])
def save_marketing():
    ct = session.get('count', int)
    items = session.get('my_list', [])
    if request.method=="POST":
        bc = request.form.get("bc")
        br = request.form.get("br")
        tc = request.form.get("tc")
        tr = request.form.get("tr")
        hc = request.form.get("hc")
        hr = request.form.get("hr")
        mc = request.form.get("mc")
        mr = request.form.get("mr")
        wc = request.form.get("wc")
        wr = request.form.get("wr")
        cc = request.form.get("cc")
        cr = request.form.get("cr")
        oc = request.form.get("oc")
        other_r = request.form.get("or")
        total = request.form.get("total")
        v1 = session.get('v1', str)
        v2 = session.get('v2', str)
        v3 = session.get('v3', str)
        id = session.get('id', str)
        cursor.execute(
            "update full_final set {c1}=%s,{m1}=%s,{m2}=%s,{m3}=%s,{m4}=%s,{m5}=%s,{m6}=%s,{m7}=%s,{m8}=%s,{m9}=%s,{m10}=%s,{m11}=%s,{m12}=%s,{m13}=%s,{m14}=%s,{m15}=%s where farmer_id = %s".format(
                c1="crop_"+str(ct+1),m1="bagging_cost" + str(ct + 1), m2="bagging_remarks" + str(ct + 1),
                m3="transportation_cost" + str(ct + 1), m4="transportation_remarks" + str(ct + 1),
                m5="hamali_cost" + str(ct + 1), m6="hamali_remarks" + str(ct + 1), m7="market_cost" + str(ct + 1),
                m8="market_remarks" + str(ct + 1), m9="weighing_cost" + str(ct + 1),
                m10="weighing_remarks" + str(ct + 1), m11="commission_cost" + str(ct + 1),
                m12="commission_remarks" + str(ct + 1), m13="others_cost" + str(ct + 1),
                m14="others_remarks" + str(ct + 1), m15="total_costs" + str(ct + 1)),(
            items[ct],bc, br, tc, tr, hc, hr, mc, mr, wc, wr, cc, cr, oc, other_r, total, id))
        mydb.commit()
        if(ct< len(items)-1):
            return redirect('/sample_input_costs')
        else:
            return redirect('/livelihood_sources')
    return render_template('marketing_costs.html',x1=items[ct])
@app.route("/livelihood_sources",methods=['GET','POST'])
def livelihood():
    if request.method=="POST":
        iagri = request.form.get("iagri")
        ianmi = request.form.get("ianmi")
        ifodd = request.form.get("ifodd")
        ipoul = request.form.get("ipoul")
        ivalue = request.form.get("ivalue")
        iother = request.form.get("iother")
        itotal = request.form.get("itotal")
        vagri = request.form.get("vagri")
        vanmi = request.form.get("vanmi")
        vfodd = request.form.get("vfodd")
        vpoul = request.form.get("vpoul")
        vvalue = request.form.get("vvalue")
        vother = request.form.get("vother")
        vtotal = request.form.get("vtotal")
        agritotal = request.form.get("agritotal")
        anmitotal = request.form.get("anmitotal")
        foddtotal = request.form.get("foddtotal")
        poultotal = request.form.get("poultotal")
        valuetotal = request.form.get("valuetotal")
        otherstotal = request.form.get("otherstotal")
        totaltotal = request.form.get("totaltotal")
        v1 = session.get('v1', str)
        v2 = session.get('v2', str)
        v3 = session.get('v3', str)
        id = session.get('id', str)
        #cursor.execute("insert into fpo.livelihood_sources values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(iagri,ianmi,ifodd,ipoul,ivalue,iother,itotal,vagri,vanmi,vfodd,vpoul,vvalue,vother,vtotal,agritotal,anmitotal,foddtotal,poultotal,valuetotal,otherstotal,totaltotal))
        cursor.execute(
            "update full_final set income_agri=%s,income_animal=%s,income_fodder=%s,income_poultry=%s,income_value=%s,income_others=%s,income_total=%s,value_agri=%s,value_animal=%s,value_fodder=%s,value_poultry=%s,value_value=%s,value_others=%s,value_total=%s,total_agri=%s,total_animal=%s,total_fodder=%s,total_poultry=%s, total_value=%s,total_others=%s,total_total=%s where farmer_id = %s",
            (iagri, ianmi, ifodd, ipoul, ivalue, iother, itotal, vagri, vanmi, vfodd, vpoul, vvalue, vother, vtotal,
             agritotal, anmitotal, foddtotal, poultotal, valuetotal, otherstotal, totaltotal, id))
        mydb.commit()
        return redirect('/fill_another')
    return render_template('livelihood_sources.html')
@app.route("/fill_another",methods=['GET','POST'])
def about():
    if request.method == "POST":
        return  redirect('/')
    return render_template('fill_another.html')

if __name__ == "__main__":
   app.run(debug=True)
