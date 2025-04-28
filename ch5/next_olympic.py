def show_next_olympic(year):
    i = 4 - year % 4
    year2 = year + i

    s = "{0}年の次のオリンピックは{1}年です。".format(year,year2)
    print(s)

show_next_olympic(2004)
show_next_olympic(2006)
show_next_olympic(2009)