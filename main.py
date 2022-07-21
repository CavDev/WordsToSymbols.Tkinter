from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import sv_ttk
import random as rd
import re

class NameList:
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

class Event:
    # def __init__(self, e):
    #     self.e = StringVar

    def clickButton(event):
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
                # messagebox.showinfo("1", result.group()) 
                textList += str(result.group())
               
        resultTextList = textList
        
        for index in range(len(resultTextList)):
            indexZ = len(eval("NameList.list" + resultTextList[index].upper()))
            indexDown = rd.randint(0, indexZ)
            # messagebox.showinfo("title", indexDown)   
            overText += eval("NameList.list" + resultTextList[index].upper())[indexDown - 1]

        # messagebox.showinfo("title", overText)   
        e.set(overText)

    def changeTheme(event):
        global e
        sv_ttk.toggle_theme()

    def aboutThis(event):
        messagebox.showinfo("说明", "这是一个写了两小时的小工具\n它可以为你将你原来输入的英文字母使用特殊符号代替\n你可以将它用作名字或是任何途径\n(PS:请手动 Ctrl + C 复制文本框中内容)\n\n\nBy NSX")

class Win:
    def __init__(self):
        self.root = self.__win()
        self.tk_label_titleText = self.__tk_label_titleText()
        self.tk_button_goButton = self.__tk_button_goButton()
        self.tk_input_nameBox = self.__tk_input_nameBox()
        self.tk_button_changeTheme = self.__tk_button_changeTheme()
        self.tk_button_aboutThis = self.__tk_button_aboutThis()

    def __win(self):
        root = Tk()
        root.title("随机特殊字母 By NSX")
        # 设置大小 居中展示
        width = 300
        height = 260
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(geometry)
        root.resizable(width=False, height=False)
        return root

    def show(self):
        self.root.mainloop()

    def __tk_label_titleText(self):
        label = Label(self.root,text="在下方输入字符")
        label.configure(font=("Microsoft YaHei", 12))
        label.place(x=20, y=50, width=160, height=24)
        return label

    def __tk_button_goButton(self):
        btn = Button(self.root, text="生成", style="Accent.TButton")
        btn.place(x=20, y=140, width=75, height=32)
        btn.bind('<Button-1>', Event.clickButton)
        return btn

    def __tk_button_changeTheme(self):
        btn = Button(self.root, text="改变主题")
        btn.place(x=105, y=140, width=75, height=32)
        btn.bind('<Button-1>', Event.changeTheme)
        return btn

    def __tk_button_aboutThis(self):
        btn = Button(self.root, text="说明")
        btn.place(x=190, y=140, width=75, height=32)
        btn.bind('<Button-1>', Event.aboutThis)
        return btn

    def __tk_input_nameBox(self):
        global e
        e = StringVar()
        ipt = Entry(self.root, textvariable=e)
        ipt.place(x=20, y=90, width=226, height=31)
        return ipt

if __name__ == "__main__":
    win = Win()
    sv_ttk.set_theme("light")
    sv_ttk.use_light_theme()

    # TODO 绑定点击事件或其他逻辑处理
    

    win.show()