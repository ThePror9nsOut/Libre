import time
from tkinter import *
import random

root = open(input("file "))
rootfour = ""
rt = Tk()
vars = [""]
lists = [[]]
opened = []
funcs = [""]
do = [""]
ind = 0

plugiedinvisual = False

def compare(file):
    global rootfour, plugiedinvisual

    if file.count("[printf] ") == 1:
        rootfour = rootfour.replace("\n", "")
        print(rootfour.replace("[printf] ", ""))
    if file.count("[printfln] ") == 1:
        print(rootfour.replace("[printfln] ", ""))
        #
    if file.count("[num var]:") == 1:
        rootfour = root.readline()
        move = rootfour.replace("\n", "")
        move = move.replace("[ ", "")
        vars.append(int(move))
    if file.count("[str var]:") == 1:
        move = root.readline()
        move = move.replace("[ ", "")
        move = move.replace("\n", "")
        vars.append(move)

    if file.count("[input str var]:") == 1:
        move = root.readline()
        move = move.replace("[ ", "")
        move = move.replace("\n", "")
        move = str(input(move))
        vars.append(move)

    if file.count("[input int var]:") == 1:
        move = root.readline()
        move = move.replace("[ ", "")
        move = move.replace("\n", "")
        move = int(input(move))
        vars.append(move)

    # if file.count("[run] ") == 1:
    #     move = rootfour.replace("\n", "")
    #     move = move.replace("[run] ", "")
    #     move = open(move)
    #     while rootfour != "end":
    #         rootfour = move.readline()
    #
    #         compare(rootfour)


        # if rootfour.count("if is {") == 1:
            #     one = root.readline()
            #     one = one.replace("{ ", "")
            #     two = root.readline()
            #     two = two.replace("{ ", "")
            #
            #     if vars[int(one)] == vars[int(two)]:
            #         compare(rootfour)
            #     else:
            #         while rootfour != "}\n":
            #             rootfour = root.readline()
            # if rootfour.count("if is not {") == 1:
            #     one = root.readline()
            #     one = one.replace("{ ", "")
            #     two = root.readline()
            #     two = two.replace("{ ", "")
            #
            #     if vars[int(one)] != vars[int(two)]:
            #         compare(rootfour)
            #     else:
            #         while rootfour != "}\n":
            #             rootfour = root.readline()
            # if rootfour.count("if > {") == 1:
            #     one = root.readline()
            #     one = one.replace("{ ", "")
            #     two = root.readline()
            #     two = two.replace("{ ", "")
            #
            #     if vars[int(one)] >= vars[int(two)]:
            #         compare(rootfour)
            #     else:
            #         while rootfour != "}\n":
            #             rootfour = root.readline()
            # if rootfour.count("if < {") == 1:
            #     one = root.readline()
            #     one = one.replace("{ ", "")
            #     two = root.readline()
            #     two = two.replace("{ ", "")
            #
            #     if vars[int(one)] <= vars[int(two)]:
            #         compare(rootfour)
            #     else:
            #         while rootfour != "}\n":
            #             rootfour = root.readline()

    # if rootfour.count("[list var]:") == 1:
    #     move = root.readline()
    #     move = move.replace("[ ", "")
    #     move1 = root.readline()
    #     move1 = move1.replace("[ ", "")
    #     move2 = root.readline()
    #     move2 = move2.replace("[ ", "")
    #     lists[int(move)].append(move)
    #     lists.append(move1)
    #     lists.append(move2)

    if file.count("[plugin]:") == 1:
        move = root.readline()
        move = move.replace("[ ", "")
        move = move.replace("\n", "")
        if move == "visual":
            plugiedinvisual = True

    if plugiedinvisual == True:

        if file.count("[config]:") == 1:
            move = root.readline()
            title = move.replace("[ ", "")
            title = title.replace("\n", "")
            rt.title(title)
            move = root.readline()
            bg = move.replace("[ ", "")
            bg = bg.replace("\n", "")
            rt["bg"] = bg
            move = root.readline()
            geo = move.replace("[ ", "")
            geo = geo.replace("\n", "")
            rt.geometry(geo)
            move = root.readline()
            rz1 = move.replace("1[ ", "")
            rz1 = rz1.replace("\n", "")
            move = root.readline()
            rz2 = move.replace("2[ ", "")
            rz2 = rz2.replace("\n", "")
            rt.resizable(rz1, rz2)

        if file.count("[loop]") == 1:
            rt.mainloop()
            #

        if file.count("[label]:") == 1:
            move = root.readline()
            text = move.replace("[ ", "")
            text = text.replace("\n", "")
            move = root.readline()
            bg = move.replace("[ ", "")
            bg = bg.replace("\n", "")
            move = root.readline()
            fg = move.replace("[ ", "")
            fg = fg.replace("\n", "")
            move = root.readline()
            psx = move.replace("[ ", "")
            psx = psx.replace("\n", "")
            move = root.readline()
            psy = move.replace("[ ", "")
            psy = psy.replace("\n", "")
            move = root.readline()
            font = move.replace("[ ", "")
            font = font.replace("\n", "")
            newlbl = Label(text=vars[int(text)], bg=bg, fg=fg, font=font)
            newlbl.place(relx=psx, rely=psy)

        if file.count("[entry]:") == 1:
            move = root.readline()
            bg = move.replace("[ ", "")
            bg = bg.replace("\n", "")
            move = root.readline()
            fg = move.replace("[ ", "")
            fg = fg.replace("\n", "")
            move = root.readline()
            psx = move.replace("[ ", "")
            psx = psx.replace("\n", "")
            move = root.readline()
            psy = move.replace("[ ", "")
            psy = psy.replace("\n", "")
            move = root.readline()
            font = move.replace("[ ", "")
            font = font.replace("\n", "")
            newentry = Entry(bg=bg, fg=fg, font=font)
            newentry.place(relx=psx, rely=psy)

        if file.count("[image]:") == 1:
            move = root.readline()
            image = move.replace("[ ", "")
            image = image.replace("\n", "")
            image = PhotoImage(file=image)
            move = root.readline()
            psx = move.replace("[ ", "")
            psx = psx.replace("\n", "")
            move = root.readline()
            psy = move.replace("[ ", "")
            psy = psy.replace("\n", "")
            newlbl = Label(image=image)
            newlbl.place(relx=psx, rely=psy)

    if file.count("[set]:") == 1:
        index = rootfour.replace("\n", "")
        index = index.replace("[set]:", "")
        index = root.readline()
        index = index.replace("[ ", "")
        index = index.replace("\n", "")
        toset = root.readline()
        toset = toset.replace("\n", "")
        toset = toset.replace("[ ", "")
        vars[int(index)] = toset
    if file.count("[randomize]:") == 1:
        index = root.readline()
        index = index.replace("[ ", "")
        index = index.replace("\n", "")
        toset = root.readline()
        toset = toset.replace("\n", "")
        toset = toset.replace("[ ", "")
        toset1 = root.readline()
        toset1 = toset1.replace("\n", "")
        toset1 = toset1.replace("[ ", "")
        vars[int(index)] = random.randint(int(toset), int(toset1))
    if file.count("[printf var] ") == 1:
        move = rootfour.replace("\n", "")
        move = int(move.replace("[printf var] ", ""))
        print(vars[move])
    # if rootfour.count("[printf list]:") == 1:
    #     rootfour = root.readline()
    #     move = rootfour.replace("\n", "")
    #     move = int(move.replace("[ ", ""))
    #     rootfour = root.readline()
    #     move1 = rootfour.replace("\n", "")
    #     move1 = int(move1.replace("[ ", ""))
    #     print(lists[move])
    if file.count("[-]:") == 1:
        move = rootfour.replace("\n", "")
        move = move.replace("[-]:", "")
        one = root.readline()
        one = one.replace("[ ", "")
        one = one.replace("\n", "")
        two = root.readline()
        two = two.replace("[ ", "")
        two = two.replace("\n", "")
        one = int(one)
        two = int(two)
        vars[one] -= vars[two]
    if file.count("[+]:") == 1:
        one = root.readline()
        one = one.replace("[ ", "")
        one = one.replace("\n", "")
        two = root.readline()
        two = two.replace("[ ", "")
        two = two.replace("\n", "")
        one = int(one)
        two = int(two)
        vars[one] += vars[two]
    if file.count("[/]:") == 1:
        move = rootfour.replace("\n", "")
        move = move.replace("[/]:", "")
        one = root.readline()
        one = one.replace("[ ", "")
        one = one.replace("\n", "")
        two = root.readline()
        two = two.replace("[ ", "")
        two = two.replace("\n", "")
        one = int(one)
        two = int(two)
        vars[one] /= vars[two]
        one = int(one)
        two = int(two)
    if file.count("[*]:") == 1:
        move = rootfour.replace("\n", "")
        move = move.replace("[*]:", "")
        one = root.readline()
        one = one.replace("[ ", "")
        one = one.replace("\n", "")
        two = root.readline()
        two = two.replace("[ ", "")
        two = two.replace("\n", "")
        one = int(one)
        two = int(two)
        vars[one] *= vars[two]
    # if rootfour.count("[^]:") == 1:
    #     move = rootfour.replace("\n", "")
    #     move = move.replace("[^]:", "")
    #     one = root.readline()
    #     one = one.replace("[ ", "")
    #     one = one.replace("\n", "")
    #     two = root.readline()
    #     two = two.replace("[ ", "")
    #     two = two.replace("\n", "")
    #     one = int(one)
    #     two = int(two)
    #     vars[one] ^= vars[two]
    if file.count("[sleep] ") == 1:
        move = rootfour.replace("\n", "")
        move = move.replace("[sleep] ", "")
        time.sleep(int(move))
    if file.count("[sleep as var] ") == 1:
        move = rootfour.replace("\n", "")
        move = move.replace("[sleep as var] ", "")
        time.sleep(vars[int(move)])
    if file.count("[exit]") == 1:
        move = rootfour.replace("\n", "")
        move = move.replace("[exit] ", "")
        time.sleep(int(move))
    if file.count("[input] ") == 1:
        move = rootfour.replace("\n", "")
        move = move.replace("[input] ", "")
        input(move)

while rootfour.count("end") < 1:
    rootfour = root.readline()

    compare(rootfour)

    if rootfour.count("if is {") == 1:
        one = root.readline()
        one = one.replace("{ ", "")
        two = root.readline()
        two = two.replace("{ ", "")

        if vars[int(one)] == vars[int(two)]:
            compare(rootfour)
        else:
            while rootfour != "}\n":
                rootfour = root.readline()
    if rootfour.count("if is not {") == 1:
        one = root.readline()
        one = one.replace("{ ", "")
        two = root.readline()
        two = two.replace("{ ", "")

        if vars[int(one)] != vars[int(two)]:
            compare(rootfour)
        else:
            while rootfour != "}\n":
                rootfour = root.readline()
    if rootfour.count("if > {") == 1:
        one = root.readline()
        one = one.replace("{ ", "")
        two = root.readline()
        two = two.replace("{ ", "")

        if vars[int(one)] >= vars[int(two)]:
            compare(rootfour)
        else:
            while rootfour != "}\n":
                rootfour = root.readline()
    if rootfour.count("if < {") == 1:
        one = root.readline()
        one = one.replace("{ ", "")
        two = root.readline()
        two = two.replace("{ ", "")

        if vars[int(one)] <= vars[int(two)]:
            compare(rootfour)
        else:
            while rootfour != "}\n":
                rootfour = root.readline()
    # if rootfour.count("while is {") == 1:
    #     one = root.readline()
    #     one = one.replace("{ ", "")
    #     two = root.readline()
    #     two = two.replace("{ ", "")
    #
    #     while vars[int(one)] == vars[int(two)]:
    #         compare()
    #     else:
    #         while rootfour != "}\n":
    #             rootfour = root.readline()