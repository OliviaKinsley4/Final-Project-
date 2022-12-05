#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import time

scr = turtle.getscreen()
scr.title("Flag of America")
scr.bgcolor("white")
t = turtle.Turtle()
t.speed(20)
t.penup


# In[2]:


def draw_rectangle(x, y, height, width, color):
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.end_fill()
    t.penup()


# In[3]:


def draw_star(x, y, color, length):
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.color(color)
    for turn in range(0,5) :
        t.forward(length)
        t.right(144)
        t.forward(length)
        t.right(144)
    t.end_fill()
    t.penup()


# In[4]:


def draw_stripes(x, y, flag_ht):
    flag_wth = flag_ht*1.5
    stripe_ht = flag_ht/13
    stripe_wth = flag_wth
    for stripe in range(0,6):
        for color in ["Dark red", "white"]:
            draw_rectangle(x, y, stripe_ht, stripe_wth, color)
            y = y - stripe_ht
    draw_rectangle(x, y, stripe_ht, stripe_wth, 'Dark red')
    y = y - stripe_ht


# In[5]:


def draw_square(x, y, flag_ht):
    square_ht = (7/13) * flag_ht
    square_wth = (0.76) * flag_ht
    draw_rectangle(x, y, square_ht, square_wth, 'navy') 


# In[6]:


def Star1(x, y, flag_ht):
    stripe_ht = flag_ht/13
    dist_of_stars = 30
    dist_bet_lines = stripe_ht + 6
    y = 112
    for row in range(0,5) :
        x = -234
        for star in range (0,6) :
            star_size = 13
            draw_star(x, y, 'white', star_size)
            x = x + dist_of_stars
        y = y - dist_bet_lines 


# In[7]:


def stars_five(x, y, flag_ht):
    star_size = 13
    stripe_ht = flag_ht/13
    dist_of_stars = 30
    dist_bet_lines = stripe_ht + 6
    y = 100
    for row in range(0,4) :
        x = -217
        for star in range (0,5) :
            draw_star(x, y, 'white', star_size)
            x = x + dist_of_stars
        y = y - dist_bet_lines


# In[8]:


def draw_flag(x, y, flag_ht):
    draw_stripes(x, y, flag_ht)
    draw_square(x, y, flag_ht)
    Star1(x, y, flag_ht)
    stars_five(x, y, flag_ht)


# In[9]:


def main():
    flag_ht = 250
    x = -250
    y = 120
    time.sleep(5)
    draw_flag(x, y, flag_ht)
    t.hideturtle()


# In[10]:


main()

