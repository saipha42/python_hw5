import turtle

gap = 20

calendar_width = 200
calendar_high = 150


box_len = 200 / 7
box_high = calendar_high/7
#set the turtle to be origin from the left side of the window instead of the center
turtle.screensize(900,550)
turtle.penup()
turtle.goto(-430, 225)
turtle.speed(0)

# y_cord = 230

def set_turtle_to_row(row_num):
    y_cord = 225 - ((calendar_high + gap) * row_num)
    turtle.penup()
    if( row_num == 1) :
        turtle.goto(-430, y_cord)
    if row_num == 2 :
        
        turtle.goto(-430, y_cord)
    if row_num == 3 :
        turtle.goto(-430,  y_cord)


def pre_turtle(row, col) :
    y_cord = 225 - ((calendar_high + gap) * row)
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

    for wkday in weekdays :
        draw_cal_box(wkday, month="")
        turtle.penup()
        turtle.forward(box_len)
        

month_31 = [1,3,5,7,8,10,12]


def wheather_to_write_day(day, month) :
    if type(day) != int :
        turtle.write(day)
    else :
        if day == 0 :
            print()
            
        if month in month_31 :
            if day <= 31 :
                
                turtle.write(day)
                

        else :
            if month == 2 :
                if day <= 28 :
                       
                        turtle.write(day)
                        
            else :
                if day <= 30 :
                    
                    turtle.write(day)
                    


def draw_cal(row, col, month) :
    day = 0
    x = -430
    if col > 1 :
        x = -430 + ((calendar_width + gap) * (col -1))

    for row in range(1, 6) :

        turtle.goto(x, turtle.ycor() - box_high)
        turtle.pendown()
        for col in range(1, 8) :
            #logic when to start count the day
            day += 1
            #end of logic
            draw_cal_box(day, month)
            turtle.penup()
            turtle.forward(box_len)
        

month = 0
#calendar grid row loop
for row in range(0, 3) :

    
    set_turtle_to_row(row)

    #calendar grid column loop
    for col in range(1, 5):
        month += 1
        pre_turtle(row, col)
        draw_cal_head(2)
        draw_cal_week_head()
        draw_cal(row, col, month)
    

turtle.done()


    