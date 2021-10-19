from flask.globals import request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField

from flask import Flask, render_template, request

from flatmates1_bill.flat import Bill, Flatmate

app = Flask(__name__)


class HomePage(MethodView):
    """Creates a HomePage, rendering html file index2.html"""

    def get(self):
        return render_template('index2.html')


class BillFormPage(MethodView):
    """Creates a BillPage, rendering html file bill_form_page2.html"""

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page2.html', billform=bill_form)


class ResultPage(MethodView):
    """Creates a ResultPage, rendering html file results2.html"""

    def post(self):
        """Takes data from BillForm, Creates objects of Bill and Flatmate classes in accordance of number of flatmates,
        calculates the payment for each pearson and render a template 'results2.html'"""
        billOform = BillForm(request.form)

        amountpost = float(billOform.amount.data)
        periodpost = billOform.period.data
        flatmatespost = billOform.flatmates.data
        the_bill = Bill(amount=amountpost, period=periodpost,
                        flatmates=flatmatespost)

        name1 = billOform.name1.data
        days_in_house1 = int(billOform.days_in_house1.data)

        name2 = billOform.name2.data
        days_in_house2 = int(billOform.days_in_house2.data)

        name3 = billOform.name3.data
        days_in_house3 = int(billOform.days_in_house3.data)

        name4 = billOform.name4.data
        days_in_house4 = int(billOform.days_in_house4.data)

        name5 = billOform.name5.data
        days_in_house5 = int(billOform.days_in_house5.data)

        if flatmatespost == "2":
            flatmate1 = Flatmate(flatmate1=name1, dih1=days_in_house1,
                                 flatmate2=name2, dih2=days_in_house2)
            flatmate2 = Flatmate(flatmate1=name2, dih1=days_in_house2,
                                 flatmate2=name1, dih2=days_in_house1)
            return render_template("results2.html",
                                   name1=flatmate1.name, amount1=flatmate1.pays(
                                       the_bill),
                                   name2=flatmate2.name, amount2=flatmate2.pays(the_bill))

        elif flatmatespost == "3":
            flatmate1 = Flatmate(flatmate1=name1, dih1=days_in_house1,
                                 flatmate2=name2, dih2=days_in_house2,
                                 flatmate3=name3, dih3=days_in_house3)
            flatmate2 = Flatmate(flatmate1=name2, dih1=days_in_house2,
                                 flatmate2=name1, dih2=days_in_house1,
                                 flatmate3=name3, dih3=days_in_house3)
            flatmate3 = Flatmate(flatmate1=name3, dih1=days_in_house3,
                                 flatmate2=name2, dih2=days_in_house2,
                                 flatmate3=name1, dih3=days_in_house1)
            return render_template("results2.html",
                                   name1=flatmate1.name, amount1=flatmate1.pays(
                                       the_bill),
                                   name2=flatmate2.name, amount2=flatmate2.pays(
                                       the_bill),
                                   name3=flatmate3.name, amount3=flatmate3.pays(the_bill))

        elif flatmatespost == "4":
            flatmate1 = Flatmate(flatmate1=name1, dih1=days_in_house1,
                                 flatmate2=name2, dih2=days_in_house2,
                                 flatmate3=name3, dih3=days_in_house3,
                                 flatmate4=name4, dih4=days_in_house4)
            flatmate2 = Flatmate(flatmate1=name2, dih1=days_in_house2,
                                 flatmate2=name1, dih2=days_in_house1,
                                 flatmate3=name3, dih3=days_in_house3,
                                 flatmate4=name4, dih4=days_in_house4)
            flatmate3 = Flatmate(flatmate1=name3, dih1=days_in_house3,
                                 flatmate2=name2, dih2=days_in_house2,
                                 flatmate3=name1, dih3=days_in_house1,
                                 flatmate4=name4, dih4=days_in_house4)
            flatmate4 = Flatmate(flatmate1=name4, dih1=days_in_house4,
                                 flatmate2=name2, dih2=days_in_house2,
                                 flatmate3=name3, dih3=days_in_house3,
                                 flatmate4=name1, dih4=days_in_house1)
            return render_template("results2.html",
                                   name1=flatmate1.name, amount1=flatmate1.pays(
                                       the_bill),
                                   name2=flatmate2.name, amount2=flatmate2.pays(
                                       the_bill),
                                   name3=flatmate3.name, amount3=flatmate3.pays(
                                       the_bill),
                                   name4=flatmate4.name, amount4=flatmate4.pays(the_bill))

        elif flatmatespost == "5":
            flatmate1 = Flatmate(flatmate1=name1, dih1=days_in_house1,
                                 flatmate2=name2, dih2=days_in_house2, flatmate3=name3, dih3=days_in_house3, flatmate4=name4, dih4=days_in_house4, flatmate5=name5, dih5=days_in_house5)
            flatmate2 = Flatmate(flatmate1=name2, dih1=days_in_house2,
                                 flatmate2=name1, dih2=days_in_house1,  flatmate3=name3, dih3=days_in_house3, flatmate4=name4, dih4=days_in_house4, flatmate5=name5, dih5=days_in_house5)
            flatmate3 = Flatmate(flatmate1=name3, dih1=days_in_house3,
                                 flatmate2=name2, dih2=days_in_house2, flatmate3=name1, dih3=days_in_house1, flatmate4=name4, dih4=days_in_house4, flatmate5=name5, dih5=days_in_house5)
            flatmate4 = Flatmate(flatmate1=name4, dih1=days_in_house4,
                                 flatmate2=name2, dih2=days_in_house2, flatmate3=name3, dih3=days_in_house3, flatmate4=name1, dih4=days_in_house1, flatmate5=name5, dih5=days_in_house5)
            flatmate5 = Flatmate(flatmate1=name5, dih1=days_in_house5,
                                 flatmate2=name2, dih2=days_in_house2, flatmate3=name3, dih3=days_in_house3, flatmate4=name4, dih4=days_in_house4, flatmate5=name1, dih5=days_in_house1)
            return render_template("results2.html",
                                   name1=flatmate1.name, amount1=flatmate1.pays(
                                       the_bill),
                                   name2=flatmate2.name, amount2=flatmate2.pays(
                                       the_bill),
                                   name3=flatmate3.name, amount3=flatmate3.pays(
                                       the_bill),
                                   name4=flatmate4.name, amount4=flatmate4.pays(
                                       the_bill),
                                   name5=flatmate5.name, amount5=flatmate5.pays(the_bill))


class BillForm(Form):
    """Creates BillForm for getting data from user"""
    amount = StringField(label="Bill Amount: ", default="1000")
    period = StringField(label="Bill Period: ", default="March 2021")
    flatmates = StringField(
        label="Quantity of flatmates(up to 5): ", default="5")

    name1 = StringField(label="Name: ", default="None")
    days_in_house1 = StringField(label="Days in the house: ", default=0)

    name2 = StringField(label="Name: ", default="None")
    days_in_house2 = StringField(label="Days in the house: ", default=0)

    name3 = StringField(label="Name: ", default="None")
    days_in_house3 = StringField(label="Days in the house: ", default=0)

    name4 = StringField(label="Name: ", default="None")
    days_in_house4 = StringField(label="Days in the house: ", default=0)

    name5 = StringField(label="Name: ", default="None")
    days_in_house5 = StringField(label="Days in the house: ", default=0)
    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results2', view_func=ResultPage.as_view('results_page'))
app.run(debug=True)
