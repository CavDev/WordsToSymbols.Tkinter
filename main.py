from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import sv_ttk
import random as rd
import re

isCheck = True # 用布尔类型检测是否开启完整字符集

class NameList:
    
    # Normal
    listA = ("ẠạÅåÄäẢảḀḁẤấẦầẨẩȂȃẪẫẬậẮắẰằẲẳẴẵẶặĀāĄąȀȁǺǻȦȧÁáǞǟǍǎÀàÃãǠǡÂâȺⱥÆæǢǣǼǽⱭ℀⅍℁ª")
    listB = ("ḂḃḄḅḆḇƁɃƀ")
    listC = ("çḈḉĆćĈĉĊċČčÇçƇƈȻȼℂ℃Ɔℭ")
    listD = ("ḊḋḌḍḎḏḐḑḒḓĎďƊƋƌƉđȡǱǲǳǄǅǆȸ")
    listE = ("ḔḕḖḗḘḙḚḛḜḝẸẹẺẻẾếẼẽỀềỂểỄễỆệĒēĔĕĖėĘęĚěÈèÉéÊêËëȄȅȨȩȆȇƎɆɇƏǝℰℯ℮ℇ")
    listF = ("ḞḟƑƒℲⅎℱ")
    listG = ("ƓḠḡĜĝĞğĠġǤǥǦǧǴℊǵĢģ")
    listH = ("ḢḣḤḥḦḧḨḩḪḫĤĥȞȟĦħⱧⱨℍǶẖℏℎℋℌ")
    listI = ("ḬḭḮḯĲĳÍíÌìÎîÏïĨĩĪīĬĭĮįǏǐıƚℑℐ")
    listJ = ("ĴĵɈɉȷǰ")
    listK = ("ḰḱḲḳḴḵĶķƘƙǨǩⱩⱪĸ")
    listL = ("ḶḷḸḹḺḻḼḽĹĺĻļĽľĿŀŁłỈỉⱠⱡȽⱢǇǈǉỊİịȈȉȊȋℓℒ")
    listM = ("ḾḿṀṁṂṃƜℳ")
    listN = ("ṄṅṆṇṈṉṊṋŃńŅņŇňǸǹÑñȠƞŊŋƝŉǊǋǌȵℕ№")
    listO = ("ÖöṎṏṌṍṐṑṒṓȪȫȬȭȮȯȰȱǪǫǬǭỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợƠơŌōŎŏŐőÒòÓóÔôÕõǑǒȌȍȎȏŒœØøǾǿ⍥⍤ℴ")
    listP = ("ṔṕṖṗƤƥⱣℙǷ℘")
    listQ = ("Ɋɋℚȹ")
    listR = ("ŔŕŖŗŘřṘṙṚṛṜṝṞṟȐȑȒȓɌɍƦⱤ℞ℜℛ℟ℝ")
    listS = ("ṠṡṢṣṤṥṦṧṨṩŚśŜŝŞşŠšȘșȿƧƨϨϩẞßẛ℠")
    listT = ("ṪṫṬṭṮṯṰṱŢţŤťŦŧȚțȾⱦƬƮƫƭẗȶ™")
    listU = ("ṲṳṴṵṶṷṸṹṺṻỦủỤụỨứỪừỬửỮữỰựŨũŪūŬŭŮůŰűǙǚǗǘǛǜŲųǓǔȔȕÛûȖȗÙùÚúÜüƯưɄƲƱ")
    listV = ("ṼṽṾṿɅ℣ⱱⱴ")
    listW = ("ẀẁẂẃẄẅẆẇẈẉŴŵⱲⱳϢϣẘ")
    listX = ("ẊẋẌẍℵ×")
    listY = ("ẎẏỲỳỴỵỶỷỸỹŶŷƳƴŸÿÝýɎɏȲȳƔẙ")
    listZ = ("ẐẑẒẓẔẕŹźŻżŽžȤȥⱫⱬƵƶɀℨℤ")
    
    # Less
    lessListA = ("ǠǡÂâȺⱥ")
    lessListB = ("ḂḃḄḅḆḇƁɃƀ")
    lessListC = ("ÇçƇƈȻȼℂ℃ℭ")
    lessListD = ("ƊƉđȡ")
    lessListE = ("ȨȩȆȇɆɇℯ℮")
    lessListF = ("ḞḟƑƒℱ")
    lessListG = ("ǧǴℊǵĢģ")
    lessListH = ("ℍℏℎℋ")
    lessListI = ("ḬḭǏǐıƚ")
    lessListJ = ("ĴĵɈɉȷǰ")
    lessListK = ("ḲḳḴḵĶƘƙⱩⱪĸ")
    lessListL = ("ỊİịȈȉȊȋℓℒ")
    lessListM = ("ḾḿṀṁṂṃℳ")
    lessListN = ("ȠƞŊŋƝŉȵℕ№")
    lessListO = ("ȌȍȎȏØøǾǿ⍥⍤")
    lessListP = ("ṗƤƥⱣℙǷ℘")
    lessListQ = ("Ɋɋℚȹ")
    lessListR = ("ŖŗɌɍƦⱤ℞ℜℛ℟ℝ")
    lessListS = ("ŜŝŞşŠšȘșȿ")
    lessListT = ("ŦŧȚțȾⱦƬƮƫƭẗȶ")
    lessListU = ("ṳƯưɄƲƱ")
    lessListV = ("ṾṿɅ℣ⱱⱴ")
    lessListW = ("ŴŵⱲⱳϢϣẘ")
    lessListX = ("Ẋℵ×✗✘ㄨ✕")
    lessListY = ("ɎɏȲȳƔẙ")
    lessListZ = ("ȤȥⱫⱬƵƶɀℤ")

class Event:
    # def __init__(self, e):
    #     self.e = StringVar

    def clickButton(event):
        global isCheck
        textList = ""
        resultTextList = ""
        overText = ""

        if e.get() == "":
            # messagebox.showwarning("错误","文本框为空！")
            pass
        else:
            for index in range(len(e.get())):
                x = e.get()[index]
                result = re.match("[A-Za-z]*", x) # 用正则表达式匹配26个英文字母
                textList += str(result.group())
               
        resultTextList = textList
        
        if isCheck == False: # 当“完整字符集”未被勾选
             for index in range(len(resultTextList)):
                 indexZ = len(eval("NameList.list" + resultTextList[index].upper()))
                 indexDown = rd.randint(0, indexZ)
                 # messagebox.showinfo("title", indexDown)   
                 overText += eval("NameList.list" + resultTextList[index].upper())[indexDown - 1]
        elif isCheck == True:
            for index in range(len(resultTextList)):
                 indexZ = len(eval("NameList.lessList" + resultTextList[index].upper()))
                 indexDown = rd.randint(0, indexZ)
                 overText += eval("NameList.lessList" + resultTextList[index].upper())[indexDown - 1]
          
        e.set(overText)

    def changeTheme(event):
        global e
        sv_ttk.toggle_theme()

    def aboutThis(event):
        messagebox.showinfo("说明", "又是一个牛马工具\n它可以为你将你原来输入的英语字母使用形近的特殊符号代替\n输入的其它字符会被忽略，所以你可以把你想要替换的内容直接Copy进来\n你可以将它用作名字或是任何途径\n如果想要使用更多字符来进行匹配替换请勾选 “完整字符集” 选项'\n(PS:请手动 Ctrl + C 复制文本框中内容)\n\nBy NSX7\n最后更改于 2022.8.12")

    def changeCharsType():
        global isCheck
        
        if isCheck == 0:
            isCheck = True
        else:
            isCheck = False
    
class Win:
    def __init__(self):
        self.root = self.__win()
        self.tk_label_titleText = self.__tk_label_titleText()
        self.tk_button_goButton = self.__tk_button_goButton()
        self.tk_input_nameBox = self.__tk_input_nameBox()
        self.tk_button_changeTheme = self.__tk_button_changeTheme()
        self.tk_button_aboutThis = self.__tk_button_aboutThis()
        self.tk_Checkbutton_fullChars = self.__tk_Checkbutton_fullChars()

    def __win(self):
        root = Tk()
        root.title("")
        # 设置大小 居中展示
        width = 610
        height = 400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(geometry)
        root.iconbitmap('ico.ico')
        root.resizable(width=False, height=False)
        return root

    def show(self):
        self.root.mainloop()

    def __tk_label_titleText(self):
        label = Label(self.root,text="字词 ➪ 符号", foreground='gray')
        label.configure(font=("Microsoft YaHei", 25, 'bold'))
        label.place(x=205, y=70, width=220, height=40)
        return label

    def __tk_button_goButton(self):
        btn = Button(self.root, text="生成", style="Accent.TButton")
        btn.place(x=110, y=220, width=115, height=36)
        btn.bind('<Button-1>', Event.clickButton)
        return btn

    def __tk_button_changeTheme(self):
        btn = Button(self.root, text="改变主题")
        btn.place(x=250, y=220, width=115, height=36)
        btn.bind('<Button-1>', Event.changeTheme)
        return btn

    def __tk_button_aboutThis(self):
        btn = Button(self.root, text="说明")
        btn.place(x=430, y=220, width=85, height=36)
        btn.bind('<Button-1>', Event.aboutThis)
        return btn
    
    def __tk_Checkbutton_fullChars(self):
        swt = Checkbutton(self.root, style="Switch.TCheckbutton", text='完整字符集', command=Event.changeCharsType)
        swt.place(x=410, y=82, width=180, height=36)
        return swt

    def __tk_input_nameBox(self):
        global e
        e = StringVar()
        ipt = Entry(self.root, textvariable=e)
        ipt.place(x=80, y=150, width=459, height=37)
        ipt.bind('<Return>', Event.clickButton) # 绑定到回车
        return ipt

if __name__ == "__main__":
    win = Win()
    sv_ttk.set_theme("light")
    sv_ttk.use_light_theme()

    # TODO 绑定点击事件或其他逻辑处理
    

    win.show()
