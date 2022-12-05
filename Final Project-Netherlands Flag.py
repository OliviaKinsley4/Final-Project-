#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import time

scr = turtle.getscreen()
scr.title("Flag of The Netherlands")
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


def draw_stripes(x, y, flag_ht):
    flag_wth = flag_ht*1.5
    stripe_ht = flag_ht/3
    stripe_wth = flag_wth
    for stripe in range(0,1,2):
        for color in ["Dark red", "white", "Dark blue"]:
            draw_rectangle(x, y, stripe_ht, stripe_wth, color)
            y = y - stripe_ht


# In[4]:


def draw_flag(x, y, flag_ht):
    draw_stripes(x, y, flag_ht)


# In[5]:


def main():
    flag_ht = 250
    x = -250
    y = 120
    time.sleep(5)
    draw_flag(x, y, flag_ht)
    t.hideturtle()


# In[6]:


main()


# In[ ]:




