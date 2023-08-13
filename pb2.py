import turtle

gap = 30

calendar_width = 200
calendar_high = 150


box_len = 200 / 7
box_high = calendar_high/7

started_y_cord = 250
#set the turtle to be origin from the left side of the window instead of the center
turtle.screensize(900,550)
turtle.penup()
turtle.goto(-430, started_y_cord)
turtle.speed(0)

def set_turtle_to_row(row_num):
    y_cord = started_y_cord - ((calendar_high + gap) * row_num)
    turtle.penup()
    if( row_num == 1) :
        turtle.goto(-430, y_cord)
    if row_num == 2 :
        
        turtle.goto(-430, y_cord)
    if row_num == 3 :
        turtle.goto(-430,  y_cord)


def pre_turtle(row, col) :
    y_cord = started_y_cord - ((calendar_high + gap) * row)
    x = -430
    if col > 1 :
        x = -430 + ((calendar_width + gap) * (col -1))
    turtle.penup()

    turtle.goto( x ,y_cord )

def draw_cal_head(month):

    turtle.pendown()
    turtle.forward(calendar_width)
    turtle.right(90)
    turtle.forward(box_high)
    turtle.right(90)
    turtle.forward(calendar_width)
    turtle.right(90)
    turtle.forward(box_high)
    turtle.right(90)
    turtle.penup()
    t_x = turtle.xcor()
    t_y = turtle.ycor()
    turtle.goto(turtle.xcor()+20, turtle.ycor() -box_high )
    turtle.pendown()
    turtle.write(f"Month #{month}")
    turtle.penup()
    turtle.goto(t_x, turtle.ycor() + box_high)
    turtle.pendown()

def draw_cal_box(day, month):

    turtle.pendown()
    turtle.forward(box_len)
    turtle.right(90)
    turtle.forward(box_high)
    turtle.right(90)
    turtle.forward(box_len)
    turtle.right(90)
    turtle.forward(box_high)
    turtle.right(90)
    t_x = turtle.xcor()
    t_y = turtle.ycor()
    #write text to the box
    turtle.penup()
    turtle.goto(t_x + 5 , t_y - box_high )

    #need logic wheather to write or not
    wheather_to_write_day(day, month)
    #end of logic

    turtle.penup()
    turtle.goto(t_x, t_y)



def draw_cal_week_head() :

    weekdays = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor() - box_high)

    wkday = 0
    while wkday < len(weekdays) :
        draw_cal_box(weekdays[wkday], month="")
        turtle.penup()
        turtle.forward(box_len)
        wkday += 1
        

month_31 = [1,3,5,7,8,10,12]



def wheather_to_write_day(day, month) :
    if type(day) != int :
        turtle.write(day)
    else :
        if month in month_31 :
            if day <= 31 and day > 0 :
                turtle.write(day)
        else :
            if month == 2 and day > 0 :
                if day <= 28 :
                        turtle.write(day)
            else :
                if day <= 30 and day > 0 :
                    turtle.write(day)


def should_count_first_day(day, month) :

    if month in month_31 :
        if day <= 31 :
            return True
    else :
        if month == 2 :
            if day <= 28 :
                    return True
        else :
            if day <= 30 :
                return True
    return False

def draw_cal(cal_row, cal_col, month, first_day) :
    day = 0
    x = -430
    if cal_col > 1 :
        x = -430 + ((calendar_width + gap) * (cal_col -1))

    row = 1
    while row < 7 :

        turtle.goto(x, turtle.ycor() - box_high)
        turtle.pendown()

        # col = 1
        col = 1
        while col < 8 :
            #logic when to start count the day
            if day == 0 :
                if col == first_day :
                    day += 1
                    
            elif day > 0 and should_count_first_day(day, month):
                day += 1
            if day > 0 and should_count_first_day(day, month) :
                first_day +=1

            if (first_day > 7) :
                first_day = 1
            
            if row == 6 :
                if month == 4 or month == 7 or month == 12 :
                    draw_cal_box(day, month)
                    turtle.penup()
                    turtle.forward(box_len)
                else :
                    col += 1
            else :
                draw_cal_box(day, month)
                turtle.penup()
                turtle.forward(box_len)
            col += 1
        row += 1

    return first_day

month = 0
first_day_of_the_month = 1

#calendar grid row loop
row = 0
while row < 3 :
    set_turtle_to_row(row)

    #calendar grid column loop
    col = 1
    while col < 5:
        month += 1
        pre_turtle(row, col)
        draw_cal_head(month)
        draw_cal_week_head()

        first_day_of_the_month= draw_cal(row, col, month, first_day_of_the_month)
        col += 1
    row += 1
    
turtle.done()


    