NAMELIST = []
DATA = {}
RAWS = []
NAMEFILE = "names.txt"
NOTRANS = ''
MISSREQ = ''
MISSONE = ''
PASSONE = ''
BEYOND = ''
BASIC = ''
BASICNOTRANS = ''
STOREWPERC = "0.9"
STOREQPERC = "1.0"
TARGET = "2.5"

##Swipe rate 22.4%W 21.4%Q

def template_read(filename):
    file = open(filename)
    file = file.read()
    return file


def name_file(filename):
    file = open(filename)
    for line in file:
        NAMELIST.append(line.strip())


def data_dict(filename):
    file = open(filename)
    for line in file:
        line = line.strip().split(',')
        if line[0] != '':
            line[0] = int(line[0])
        if line[1] != '':
            line[1] = int(line[1])
        if line[2] != '#DIV/0!' and line[2] != '':
            line[2] = float(line[2].strip('%'))
        RAWS.append(line)


def name_add():
    for i in range(len(NAMELIST)):
        DATA[NAMELIST[i]] = RAWS[i]


def template_fill_sept():
    for name in DATA:
        sold = DATA[name][0]
        trans = DATA[name][1]
        perc = DATA[name][2]
        output = ''
        if trans == 0 or trans == '':
            output = NOTRANS.format(name)
        elif 0 <= perc < 3.2:
            output = MISSREQ.format(name, sold, trans, str(perc))
        elif 3.2 <= perc < 4.2:
            output = MISSONE.format(name, sold, trans, str(perc))
        elif 4.2 <= perc < 5.2:
            output = PASSONE.format(name, sold, trans, str(perc))
        elif perc >= 5.2:
            output = BEYOND.format(name, sold, trans, str(perc), str(perc))

        print(output)


def template_fill_basic():
    for name in DATA:
        sold = DATA[name][0]
        trans = DATA[name][1]
        perc = DATA[name][2]
        if trans == 0 or trans == '':
            output = BASICNOTRANS.format(name, TARGET, STOREWPERC, STOREQPERC)
        else:
            output = BASIC.format(name, sold, trans,
                                  str(perc), TARGET, STOREWPERC, STOREQPERC)
        print(output)


if __name__ == "__main__":
    name_file(NAMEFILE)
    data_dict("CSVs/9FEB22.csv")
    name_add()
    BASICNOTRANS = template_read("Templates/BasicMissed2022.txt")
    BASIC = template_read("Templates/BasicTemplate2022.txt")
    template_fill_basic()

    # NOTRANS = template_read("noTransOCT.txt")
    # PASSONE = template_read("passOneOCT.txt")
    # # print(NAMELIST)
    # print(DATA)
    # print(NOTRANS)

#     We also want to take this opportunity to try and work on storytelling Plum+
#     on the sales floor. When we're on the floor we have so much more time to
#     spend with each customer and inform them of all the potential benefits of
#     the membership and what would work best for them. Whether that be:
#
#         - grandparents that have begun to come in for holiday shopping about
#         free shipping to any address in Canada all year long.
#
#     - The super mom that could use that Birthday 20% coupon on themselves
#
#     - Cool Uncles that would take advantage of 4 day Early Access
#     to Black Friday this year
#
# and so much more!
