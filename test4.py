from PyQt5 import QtWidgets
from PyQt5 import QtCore
#from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import PyQt5

class MyWindow(QtWidgets.QWidget):
    #def __init__(self,*args,**kwargs):
        #super().__init__(*args,**kwargs)
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,720,720)
        self.setWindowTitle("Calorie Calculator")
        #self.initUI()   
        #self.win2 = None
        self.results = Results()
        self.calorie_outlook = {}
        self.slider_val = 0
        

        self.setStyleSheet("background-color:rgb(215,214,213);") 
        #self.error_dialog = QtWidgets.QMessageBox()
        #self.error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
       # self.error_dialog.setWindowTitle("ERROR")
        #self.error_dialog.setText("Incorrect User Input")
        #self.error_dialog.setGeometry(50,50,200,200)
       
        


        self.label = QtWidgets.QLabel(self)
        self.label.setText("Total Energy Expenditure Calculator")
        #self.label.setGeometry(150,20,1000,200)
        self.label.move(150,20)
        self.label.setStyleSheet("""
        QWidget {
            border: 3px solid black;
            font-size: 16pt;
            font-family: Cooper Black;
            border-radius: 10px;
            background-color: lightblue;
            }
        """)

        self.weight_label = QtWidgets.QLabel(self)
        self.weight_label.setText("Weight in Pounds (lbs) ")
        self.weight_label.move(150,60)

        self.weight_label.setStyleSheet("""
        QWidget {
            border : lightblue;
            font-size: 12pt;
            font-family: Berlin Sans FB Demi;
            }
        """)

        self.weight_Text_Box = QtWidgets.QLineEdit(self)
        self.weight_Text_Box.setPlaceholderText("Weight")
        #self.weight_Text_Box.move(150,80)
        self.weight_Text_Box.setGeometry(150,85,100,30)
        self.weight_Text_Box.setStyleSheet("""
        QWidget {
            
            border: 3px solid lightblue;
            font-size: 12pt;
            font-family: Berlin Sans FB Demi;
            }
        """)
        
        

        self.height_label = QtWidgets.QLabel(self)
        self.height_label.setText("What is Your Height in Feet and Inches")
        self.height_label.move(150,120)
        #self.height_label.setGeometry(150,80,500,250)
        self.height_label.setStyleSheet("""
        QWidget {
            font-size: 12pt;
            font-family: Berlin Sans FB Demi;
            }
        """)

        self.height_Ft_Text_Box = QtWidgets.QLineEdit(self)
        self.height_Ft_Text_Box.setPlaceholderText("Feet")
        #self.height_Ft_Text_Box.move(150,140)
        self.height_Ft_Text_Box.setGeometry(150,140,100,30)
        self.height_Ft_Text_Box.setStyleSheet("""
        QWidget {
            
            border: 3px solid lightblue;
            font-size: 12pt;
            font-family: Berlin Sans FB Demi;
            }
        """)

        self.height_In_Text_Box = QtWidgets.QLineEdit(self)
        self.height_In_Text_Box.setPlaceholderText("Inches")
        #self.height_In_Text_Box.move(300,140)
        self.height_In_Text_Box.setGeometry(300,140,100,30)
        self.height_In_Text_Box.setStyleSheet("""
        QWidget {
            
            border: 3px solid lightblue;
            font-size: 12pt;
            font-family: Berlin Sans FB Demi;
            }
        """)

        self.age_Label = QtWidgets.QLabel(self)
        self.age_Label.setText("What is your Age")
        self.age_Label.move(150,175)
        self.age_Label.setStyleSheet("""
        QWidget {
            font-size: 12pt;
            font-family: Berlin Sans FB Demi;
            }
        """)

        self.age_Text = QtWidgets.QLineEdit(self)
        self.age_Text.setPlaceholderText("Age")
        #self.age_Text.move(150,190)
        self.age_Text.setGeometry(150,195,100,30)
        self.age_Text.setStyleSheet("""
        QWidget {
            
            border: 3px solid lightblue;
            font-size: 12pt;
            font-family: Berlin Sans FB Demi;
            }
        """)
        
        self.male_Check = QtWidgets.QCheckBox('Male', self)
        self.male_Check.move(150, 230)
        self.male_Check.stateChanged.connect(self.allow)
        self.male_Check.setStyleSheet("""
        QCheckBox {
            font-size: 11.5pt;
            font-family: Berlin Sans FB Demi;
            border: 3px solid lightblue;
            }
        """)


        self.female_Check = QtWidgets.QCheckBox('Female', self)
        self.female_Check.move(250, 230)
        self.female_Check.stateChanged.connect(self.allow)
        self.female_Check.setStyleSheet("""
        QCheckBox {
            font-size: 11.5pt;
            font-family: Berlin Sans FB Demi;
            border: 3px solid lightblue;
            }
        """)
        

        self.activity_Label_tweak = QtWidgets.QLabel(self)
        self.activity_Label_tweak.setText("How active are you:" + '\n')
        self.activity_Label_tweak.setStyleSheet("""
        QWidget {
            font-size: 12.5pt;
            font-family: Berlin Sans FB Demi;
            }
        """)
        self.activity_Label_tweak.move(150,260)
        self.activity_Label = QtWidgets.QLabel(self)
        self.activity_Label.setText(
                '1. Sedentary ( little to no exercise )' + '\n'
                +'2. Lightly active ( light exercise / sports 1-3 days/week )' +'\n'
                +'3. Moderately active ( moderate exercise/sports 3-5 days/week)' +'\n'
                +'4. Very active ( hard exercise/sports 6-7 days a week )' + '\n'
                +'5. extra active ( very hard exercise/ sports and a physical job)' +'\n'+'\n'
                + 'Choose from the following ' +'\n'
        )
        self.activity_Label.move(160,285)

        self.activity_Label.setStyleSheet("""
        QWidget {
            font-size: 10.5pt;
            font-family: Berlin Sans FB Demi;
            }
        """)

        self.item1 = QtWidgets.QListWidgetItem("1. Sedentary")
        self.item2 = QtWidgets.QListWidgetItem("2. Lightly active")
        self.item3 = QtWidgets.QListWidgetItem("3. Moderately active")
        self.item4 = QtWidgets.QListWidgetItem("4. Very active")
        self.item5 = QtWidgets.QListWidgetItem("5. Extra active ")
        
        self.list_widget = QtWidgets.QListWidget(self)
        self.list_widget.setGeometry(160,425,150,100)
        self.list_widget.addItem(self.item1)
        self.list_widget.addItem(self.item2)
        self.list_widget.addItem(self.item3)
        self.list_widget.addItem(self.item4)
        self.list_widget.addItem(self.item5)
        
        self.list_widget.setStyleSheet("QListWidget"
                                  "{"
                                  "font-size: 10.5pt;"
                                    "font-family: Berlin Sans FB Demi;"
                                  "border : 2px solid black;"
                                  "background : lightblue;"
                                  "}"
                                  "QListView::item:selected"
                                  "{"

                                  "background : rgb(174,173,172);"
                                  "}"
                                  ) 
    

     

        


        self.cut_Check = QtWidgets.QCheckBox("Lose Weight" ,self)
        self.cut_Check.move(150,535)
        self.cut_Check.stateChanged.connect(self.allow2)
        self.cut_Check.setStyleSheet("""
        QCheckBox {
            font-size: 10pt;
            font-family: Berlin Sans FB Demi;
            border: 3px solid lightblue;
            }
        """)


        self.bulk_Check = QtWidgets.QCheckBox("Gain Weight", self)
        self.bulk_Check.move(270,535)
        self.bulk_Check.stateChanged.connect(self.allow2)
        self.bulk_Check.setStyleSheet("""
        QCheckBox {
            font-size: 10pt;
            font-family: Berlin Sans FB Demi;
            border: 3px solid lightblue;
            }
        """)    

        self.month_Slider = QtWidgets.QSlider(QtCore.Qt.Horizontal,self)
        self.month_Slider.setGeometry(150,575,200,50)  
        self.month_Slider.setMinimum(0)
        self.month_Slider.setMaximum(5)
        self.month_Slider.setTickInterval(1)
        self.month_Slider.valueChanged[int].connect(self.changed_Value)
        self.month_Slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        
        self.month_label = QtWidgets.QLabel(self)
        self.month_label.move(150,565)
        self.month_label.setText("Diet for 0 months" )
        self.month_label.setStyleSheet("""
        QLabel {
            font-size: 11pt;
            font-family: Berlin Sans FB Demi;
            }
        """)    

        self.save_push = QtWidgets.QPushButton("Save",self)
        self.save_push.move(150,640)
        self.save_push.clicked.connect(self.save)
        self.save_push.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(174,173,172);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             ) 

        #self.save_output = QtWidgets.QLabel(self)
        #self.save_output.move(150,650)


        self.calc = QtWidgets.QPushButton("Calculate",self)
        self.calc.move(150,670)
        self.calc.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(174,173,172);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             ) 
        self.calc.setVisible(False)
        self.calc.clicked.connect(self.passing)

    

    def changed_Value(self,value):
        self.slider_val = value
        if value == 1:
            self.month_label.setText("Diet for " + str(value)+ " month")
            self.slider_val = value
        else:

            self.month_label.setText("Diet for " + str(value)+ " months")
            self.slider_val = value
        self.slider_val = value
        
        
            

    def allow2(self):
        if self.cut_Check.isChecked():
            self.bulk_Check.setCheckable(False)
        elif self.bulk_Check.isChecked():
            self.cut_Check.setCheckable(False)
        else:
            self.cut_Check.setCheckable(True)
            self.bulk_Check.setCheckable(True)

    
    def allow(self):

        if self.female_Check.isChecked():
            self.male_Check.setCheckable(False)
        elif self.male_Check.isChecked():
            self.female_Check.setCheckable(False)
        else:
            self.female_Check.setCheckable(True)
            self.male_Check.setCheckable(True)
    

    def error_flag(self):
        self.error_dialog = QtWidgets.QMessageBox()
        self.error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
        self.error_dialog.setWindowTitle("ERROR")
        self.error_dialog.setText("Information is Missing And/Or\nCheck if all provided information is correct")
        self.error_dialog.setGeometry(50,50,200,200)
        self.error_dialog.exec_()        
    

    def save(self):
        self.calc.setVisible(True)
        try:
            self.weight = int(self.weight_Text_Box.text())
            self.height_ft = int(self.height_Ft_Text_Box.text())
            self.height_in = int(self.height_In_Text_Box.text())
            self.age = int(self.age_Text.text())
        except ValueError:
            self.error_flag()
        else:
            self.weight = self.weight_Text_Box.text()
            self.height_ft = self.height_Ft_Text_Box.text()
            self.height_in = self.height_In_Text_Box.text()
            self.age = self.age_Text.text()
        self.sex = " "
        
        if self.female_Check.isChecked():
            self.male_Check.setCheckable(False)
            self.sex = "Female"
        elif self.male_Check.isChecked():
            self.female_Check.setCheckable(False)
            self.sex = "Male"
        else:
            self.female_Check.setCheckable(True)
            self.male_Check.setCheckable(True)
            self.error_flag()

        self.activity_level = "0"
        index = self.list_widget.currentRow()

        if index == 0:
            self.activity_level = "1.25"
        elif index == 1:
            self.activity_level = "1.35"
        elif index == 2:
            self.activity_level = "1.45"
        elif index == 3:
            self.activity_level = "1.65"
        elif index == 4:
            self.activity_level = "1.75"
        else:
            self.activity_level = "0"
            self.error_flag()

        self.check_box_2 = " "
        if self.cut_Check.isChecked():
            self.bulk_Check.setCheckable(False)
            self.check_box_2 = " Lose Weight"
        elif self.bulk_Check.isChecked():
            self.cut_Check.setCheckable(False)
            self.check_box_2 = " Gain Weight"
        else:
            self.cut_Check.setCheckable(True)
            self.bulk_Check.setCheckable(True)
            self.error_flag()
        
        self.setWindowTitle("input is : " + str(self.weight) + "lbs, " + str(self.height_ft) + "ft, " +str(self. height_in) + "in, "+ str(self.age) + "yrs, " + self.sex + ", " + self.activity_level + " activity factor, " + self.check_box_2 + ",Time Frame: " + str(self.slider_val) + " months") 
        
        
        self.update()
        



    def update(self):
        self.label.adjustSize()
    
    def cm_converter(self,x,y):
        try:
            return (int(x) * 30.48)+(int(y)*2.54)
        except ValueError:
                self.error_flag()
                return 0
        

    def total_energy_expenditure(self):
        return int((self.Bmr) * float(self.activity_level))
        

    def BMR_male(self):
        try:
            self.Bmr = 10 *(int(self.weight) / 2.25) + (6.25 * self.cm_converter(self.height_ft,self.height_in)) -(5*(int(self.age)+5))
        except ValueError:
            self.error_flag()
            self.Bmr = 0.000
        else:
            return round(self.Bmr,2)

    def BMR_female(self):
        try:
            self.Bmr = 655 + (9.6*(int(self.weight) / 2.25)) + (1.8 * self.cm_converter(self.height_ft,self.height_in)) -(4.7*(int(self.age)))
        except ValueError:
            self.error_flag()
            self.Bmr = 0.00
        else:
            return round(self.Bmr,2)

    def zero_month(self):
        self.setWindowTitle("Please Select Duration")

    def cutting_calories_for_1month(self):
        for day in range(1,8):
            self.calorie_outlook[day] = (self.total_energy_expenditure() - 400)
        for day in range(8,16):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-800)
        for day in range(16,23):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-1000)
        for day in range(23,31):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-1250)

        #for day,calorie in self.calorie_outlook.items():
        #    print("day" + ' ' + str(day) + ' ' + str(calorie) + ' ' + "calories")
                

    def cutting_calories_for_2months(self):
        for day in range(1,16):
            self.calorie_outlook[day] = (self.total_energy_expenditure() - 300)
        for day in range(16,26):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-500)
        for day in range(26,46):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-700)
        for day in range(46,61):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-900)

        #for day,calorie in self.calorie_outlook.items():
         #   print("day" + ' ' + str(day) + ' ' + str(calorie) + ' ' + "calories")


    def cutting_calories_for_3months(self):
        for day in range(1,22):
            self.calorie_outlook[day] = (self.total_energy_expenditure() - 300)
        for day in range(22,51):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-600)
        for day in range(51,76):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-800)
        for day in range(76,91):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-1000)

        #for day,calorie in self.calorie_outlook.items():
            #print("day" + ' ' + str(day) + ' ' + str(calorie) + ' ' + "calories")

    def cutting_calories_for_4months(self):
        for day in range(1,31):
            self.calorie_outlook[day] = (self.total_energy_expenditure() - 300)
        for day in range(31,51):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-500)
        for day in range(51,76):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-700)
        for day in range(76,101):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-900)
        for day in range(101,121):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-1000)

        #for day,calorie in self.calorie_outlook.items():
        #    print("day" + ' ' + str(day) + ' ' + str(calorie) + ' ' + "calories")
    
    def cutting_calories_for_5months(self):
        for day in range(1,15):
            self.calorie_outlook[day] = (self.total_energy_expenditure() - 300)
        for day in range(15,41):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-500)
        for day in range(41,61):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-700)
        for day in range(61,75):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-800)
        for day in range(75,101):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-1000)
        for day in range(101,121):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-1100)
        for day in range(121,140):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-1175)
        for day in range(140,151):
            self.calorie_outlook[day] = (self.total_energy_expenditure()-1200)
        
        

        #for day,calorie in self.calorie_outlook.items():
        #    print("day" + ' ' + str(day) + ' ' + str(calorie) + ' ' + "calories")

    def bulking_calories_for_1month(self):
        for day in range(1,8):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 300)
        for day in range(8,16):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 500)
        for day in range(16,23):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 750)
        for day in range(23,31):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 900)

        #for day,calorie in self.calorie_outlook.items():
        #    print("day" + ' ' + str(day) + ' ' + str(calorie) + ' ' + "calories")

    def bulking_calories_for_2months(self):
        for day in range(1,8):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 200)
        for day in range(8,21):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 300)
        for day in range(21,36):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 400)
        for day in range(36,47):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 500)
        for day in range(47,61):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 600)

        #for day,calorie in self.calorie_outlook.items():
        #    print("day" + ' ' + str(day) + ' ' + str(calorie) + ' ' + "calories")

    def bulking_calories_for_3months(self):
        for day in range(1,11):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 200)
        for day in range(8,11):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 300)
        for day in range(11,30):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 400)
        for day in range(30,45):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 500)
        for day in range(45,61):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 600)
        for day in range(61,71):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 675)
        for day in range(71,91):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 750)

        #for day,calorie in self.calorie_outlook.items():
        #    print("day" + ' ' + str(day) + ' ' + str(calorie) + ' ' + "calories")
    
    def bulking_calories_for_4months(self):
        for day in range(1,16):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 200)
        for day in range(16,31):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 350)
        for day in range(31,46):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 450)
        for day in range(46,61):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 525)
        for day in range(61,91):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 600)
        for day in range(91,106):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 650)
        for day in range(106,121):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 725)

        #for day,calorie in self.calorie_outlook.items():
        #    print("day" + ' ' + str(day) + ' ' + str(calorie) + ' ' + "calories")

    def bulking_calories_for_5months(self):
        for day in range(1,21):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 150)
        for day in range(21,41):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 250)
        for day in range(41,71):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 325)
        for day in range(71,101):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 400)
        for day in range(101,121):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 490)
        for day in range(121,151):
            self.calorie_outlook[day] = (self.total_energy_expenditure() + 575)
        

        #for day,calorie in self.calorie_outlook.items():
        #    print("day" + ' ' + str(day) + ' ' + str(calorie) + ' ' + "calories")

        #print(self.calorie_outlook.keys())
        #print(self.calorie_outlook.values())
        #print(len(self.calorie_outlook))

    


    
    
    def passing(self):
        self.results.input1.setText(self.weight_Text_Box.text())
        self.results.input2.setText(self.height_Ft_Text_Box.text())
        self.results.input3.setText(self.height_In_Text_Box.text())
        self.results.input4.setText(self.age_Text.text())
        self.results.input11 = self.calorie_outlook
        self.calorie_outlook.clear()
       

        
        if self.female_Check.isChecked():
            self.male_Check.setCheckable(False)
            self.results.input5.setText("Female")
            self.results.input9 = self.BMR_female()
            self.results.input10 = self.total_energy_expenditure()
            self.results.total_energy_Results.setText(" Your total energy expenditure is : " + str(self.results.input10) + " calories.")
            
        elif self.male_Check.isChecked():
            self.female_Check.setCheckable(False)
            self.results.input5.setText("Male")
            self.results.input9 = self.BMR_male()
            self.results.input10 = self.total_energy_expenditure()
            self.results.total_energy_Results.setText(" Your total energy expenditure is : " + str(self.results.input10) + " calories.")
        else:
            self.female_Check.setCheckable(True)
            self.male_Check.setCheckable(True)

        index = self.list_widget.currentRow()
        if index == 0:
            self.results.input6.setText("1.25")
        elif index == 1:
            self.results.input6.setText("1.35")
        elif index == 2:
            self.results.input6.setText("1.45")
        elif index == 3:
            self.results.input6.setText("1.65")
        elif index == 4:
            self.results.input6.setText("1.75")
        else:
            self.results.input6.setText("0")

        if self.cut_Check.isChecked():
            self.bulk_Check.setCheckable(False)
            self.results.input7.setText("Lose Weight")
        elif self.bulk_Check.isChecked():
            self.cut_Check.setCheckable(False)
            self.results.input7.setText("Gain Weight")
        else:
            self.cut_Check.setCheckable(True)
            self.bulk_Check.setCheckable(True)

        self.results.input8.setText(str(self.slider_val))

        if ((self.cut_Check.isChecked() or self.bulk_Check.isChecked()) and (self.results.input8.text() == "0")):
            self.zero_month()

        if self.cut_Check.isChecked() and (self.results.input8.text() == "1"):
            self.cutting_calories_for_1month()
        if self.cut_Check.isChecked() and (self.results.input8.text() == "2"):
            self.cutting_calories_for_2months()
        if self.cut_Check.isChecked() and (self.results.input8.text() == "3"):
            self.cutting_calories_for_3months()
        if self.cut_Check.isChecked() and (self.results.input8.text() == "4"):
            self.cutting_calories_for_4months()
        if self.cut_Check.isChecked() and (self.results.input8.text() == "5"):
            self.cutting_calories_for_5months()

        if self.bulk_Check.isChecked() and (self.results.input8.text() == "1"):
            self.bulking_calories_for_1month()
        if self.bulk_Check.isChecked() and (self.results.input8.text() == "2"):
            self.bulking_calories_for_2months()
        if self.bulk_Check.isChecked() and (self.results.input8.text() == "3"):
            self.bulking_calories_for_3months()
        if self.bulk_Check.isChecked() and (self.results.input8.text() == "4"):
            self.bulking_calories_for_4months()
        if self.bulk_Check.isChecked() and (self.results.input8.text() == "5"):
            self.bulking_calories_for_5months()
    
        
        self.calc.setVisible(False)
    



        

        #self.results.input9 = self.BMR_male()
        #self.results.bmr_Results.setText(" Your total energy expenditure is :" + str (self.results.input9) + " calories.")

        #self.results.input10 = self.total_energy_expenditure()
        #self.results.total_energy_Results.setText(" Your total energy expenditure is : " + str(self.results.input10) + " calories.")
        
        
        self.results.displayInfo()
        
    
            




class Results(QtWidgets.QWidget):
    #def __init__(self, parent = None):
    #    super(results,self).__init__(parent)
    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("Calorie Calculator")

        self.input1 = QtWidgets.QLineEdit(self)
        self.input1.setVisible(False)
        self.input1.move(100,100)

        self.input2 = QtWidgets.QLineEdit(self)
        self.input2.setVisible(False)

        self.input3 = QtWidgets.QLineEdit(self)
        self.input3.setVisible(False)

        self.input4 = QtWidgets.QLineEdit(self)
        self.input4.setVisible(False)
        
        self.input5 = QtWidgets.QLineEdit(self)
        self.input5.setVisible(False)

        self.input6 = QtWidgets.QLineEdit(self)
        self.input6.setVisible(False)

        self.input7 = QtWidgets.QLineEdit(self)
        self.input7.setVisible(False)

        self.input8 = QtWidgets.QLineEdit(self)      
        self.input8.setVisible(False)

        self.input9 = " "
        #self.bmr_Results = QtWidgets.QLabel(self)
        #self.total_energy.move(100,100)

        self.input10 = " "
        self.total_energy_Results = QtWidgets.QLabel(self)
        self.total_energy_Results.move(10,10)
        self.total_energy_Results.setStyleSheet("""
        QWidget {
            font-size: 12pt;
            font-family: Berlin Sans FB Demi;
            }
        """)


        self.input11 = {}

        #self.input12 = QtWidgets.QTableWidget(self)
        #self.input12.move(50,50)
        #self.input12.setColumnCount(2)
        #self.tableWidget.setRowCount(row_count)
        
        

        #self.init_ui()

       


    #def init_ui(self):
       
       
        
    


    
    def displayInfo(self):
        
        
        #function is called everytime Calculate is clicked
        self.weight2 = self.input1.text()
        self.heightft2 = self.input2.text()
        self.heightin2 = self.input3.text()
        self.age2 = self.input4.text()
        self.sex2 = self.input5.text()
        self.activity2 = self.input6.text()
        self.check2 = self.input7.text()
        self.slider = self.input8.text()
        self.bmr = self.input9
        self.total_energy = self.input10
        self.table_dic = self.input11


        self.inputnew = QtWidgets.QTableWidget(self)
        #self.inputnew.move(50,50)
        self.inputnew.setGeometry(50,50,235,300)
        self.inputnew.setColumnCount(2)
        self.inputnew.setRowCount(len(self.table_dic.keys()))
        self.inputnew.setHorizontalHeaderLabels(["Day", "Calories"])
    
        
        pat = 0
        for key,value in self.input11.items():
                
                self.inputnew.setItem(pat,0,QtWidgets.QTableWidgetItem(str(key)))
                self.inputnew.setItem(pat,1,QtWidgets.QTableWidgetItem(str(value)))
                pat += 1

        self.inputnew.setStyleSheet("""
        QWidget {
            font-size: 10pt;
            font-family: Berlin Sans FB Demi;
            color: rgb(53,50,47);
            
            }
        """)
        

        #print(self.weight2 + self.heightft2 + self.heightin2 + self.age2 + self.sex2 + self.activity2 + self.check2 + self.slider)
        #print(self.table_dic.values())
        #print(self.slider)
        #print(type(self.slider))
        self.update()
        self.show()
        
        #if self.sex2 =="Male":
        #    bmr = self.BMR_male()
         #   self.label.setText(" Your total energy expenditure is :" + self.total_energy_expenditure(bmr,self.activity2))
        #elif self.sex2 =="Female":
        #    bmr = self.BMR_female()
        #    self.label.setText(" Your total energy expenditure is :" + self.total_energy_expenditure(bmr,self.activity2))
        #else:
          #  pass


    
    def update(self):
        #self.bmr_Results.adjustSize()
        self.total_energy_Results.adjustSize()
        #self.bmr_label = QtWidgets.QLabel(self.bmr,self)
        #self.bmr.move(150,150)


class ReadOnlyDelegate(QtWidgets.QStyledItemDelegate):

    def editor(self,parent,option,index):
        print("fire")
        return

#def window():
#   app = QtWidgets.QApplication(sys.argv)
 #   win = MyWindow()
##    win.show()
 ##   sys.exit(app.exec_())

#window()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())