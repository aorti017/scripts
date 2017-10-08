from prettytable import PrettyTable
f = open('finances.csv')
lines = [line.split("\n") for line in f]
found_month = False
first = True
month = ""
beginning = True;
curr_month = ""

categories = {}
sub_categories = {}
total_in = 0.0
total_out = 0.0
begin_val = 0.0
end_val = 0.0
for i in lines:
    i = i[0].split(',')
    if i[0] == "Month" or i[0] == "Total":
        continue
    if not i[0] == "":
        if first:
            begin_val = i[5]
            beginning = False
            curr_month = i[0]
            first = False
            continue

        print((' ' + curr_month + ' ').center(80, '*'))
        t = PrettyTable(['Category', 'Value', 'Percentage'])
        for j in categories:
            if categories[j] == 0.0:
                continue
            temp = (categories[j] / total_out)*100
            if temp < 0:
                temp = temp * -1
            t.add_row([j, str(categories[j]), str(temp)[:6] + "%"])
        print t

        print ""

        t = PrettyTable(['Sub-category', 'Value', 'Percentage'])
        for j in sub_categories:
            if sub_categories[j] == 0.0:
                continue
            temp  = (sub_categories[j] / total_out)*100
            if temp < 0:
                temp = temp * -1
            t.add_row([j, str(sub_categories[j]), str(temp)[:6] + "%"])
        print t
        print ""

        t = PrettyTable(['Movement', 'Value'])
        t.add_row(["In", str(total_in)])
        t.add_row(["Out", str(total_out)])
        t.add_row(["Total", str(total_in-total_out)])
        print t


        t = PrettyTable(['Time', 'Value'])
        t.add_row(['Beginning', begin_val])
        t.add_row(['End',  end_val])
        print t

        curr_month = i[0]
        categories = {}
        sub_categories = {}
        total_in = 0.0
        total_out = 0.0
        begin_val = end_val
        end_val = 0.0
        begninning = True
        continue

    if True:
        if found_month or month == "":
            cat = i[3]
            sub_cat = i[4]
            try:
                x = categories[cat]
            except:
                categories[cat] = 0.0
            try:
                x = sub_categories[sub_cat]
            except:
                sub_categories[sub_cat] = 0.0
            if beginning:
                try:
                    begin_val = i[5]
                    beginning = False
                except:
                    pass
            try:
                end_val = i[5]
            except:
                pass
            if i[1] == "":
                categories[cat] -= float(i[2])
                sub_categories[sub_cat] -= float(i[2])
                total_out += float(i[2])
            else:
                categories[cat] += float(i[1])
                sub_categories[sub_cat] += float(i[1])
                total_in += float(i[1])


print((' ' + curr_month + ' ').center(80, '*'))
t = PrettyTable(['Category', 'Value', 'Percentage'])
for i in categories:
    if categories[i] == 0.0:
        continue
    if not i == "Misc.":
        t.add_row([i, str(categories[i]), str(-1*(categories[i] / total_out)*100)[:6] + "%"])
    else:
        t.add_row([i, "+" + str(categories[i]), str((categories[i] / total_in)*100)[:6] + "%"])
print t
print ""
t = PrettyTable(['Sub-category', 'Value', 'Percentage'])
for i in sub_categories:
    if sub_categories[i] == 0.0:
        continue
    if not i == "Reimbursement":
        t.add_row([i, str(sub_categories[i]), str(-1*(sub_categories[i] / total_out)*100)[:6] + "%"])
    else:
        t.add_row([i, "+" + str(sub_categories[i]), str((sub_categories[i] / total_in)*100)[:6] + "%"])
print t
print ""
t = PrettyTable(['Movement', 'Value'])
t.add_row(["In", str(total_in)])
t.add_row(["Out", str(total_out)])
t.add_row(["Total", str(total_in-total_out)])
print t
t = PrettyTable(['Time', 'Value'])
t.add_row(['Beginning', begin_val])
t.add_row(['End',  end_val])
print t
