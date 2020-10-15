import time
import os

root = open(input("file "))

rootfour = ""

vars = [""]
lists = [[]]
opened = []

def compare(file):
    global rootfour

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
        # if rootfour.count("[input] ") == 1:
        #     move = rootfour.replace("\n", "")
        #     move = move.replace("[input] ", "")
        #     move = input(move)
        vars.append(move)

    if file.count("[run] ") == 1:
        move = rootfour.replace("\n", "")
        move = move.replace("[run] ", "")
        os.system(move)


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