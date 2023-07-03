from cs1graphics import *
import math
import time

canvas = Canvas(400, 300)
canvas.setBackgroundColor("light blue")
canvas.setTitle("CS101 Drawing exercise")

def animate_sunrise(sun, morning_sun, noon_sun,
                    morning_sky, noon_sky):
  morning_color = color_value(morning_sun)
  noon_color    = color_value(noon_sun)
  dark_sky      = color_value(morning_sky)
  bright_sky    = color_value(noon_sky)
  w             = canvas.getWidth()
  h             = canvas.getHeight()
  r             = sun.getRadius()
  x0            = w / 2.0
  y0            = h + r
  xradius       = w / 2.0 - r
  yradius       = h
  for angle in range(181):
    rad = (angle/180.0) * math.pi
    t   = math.sin(rad)
    # morning_color : noon_color = 1-t : t 비율로 섞음
    col = interpolate_colors(t, morning_color, noon_color)
    sun.setFillColor(col)
    col = interpolate_colors(t, dark_sky, bright_sky)
    canvas.setBackgroundColor(col)
    x = x0 - xradius * math.cos(rad)
    y = y0 - yradius * math.sin(rad)
    sun.moveTo(x, y)
  
def interpolate_colors(t, color1, color2):
  """Interpolate between color1 (for t == 0.0)
  and color2 (for t == 1.0)."""
  r1, g1, b1 = color1
  r2, g2, b2 = color2
  return (int((1-t) * r1 + t * r2),
          int((1-t) * g1 + t * g2),
          int((1-t) * b1 + t * b2))

def color_value(color):
  """Convert a color name to an (r,g,b) tuple."""
  return Color(color).getColorValue()

ci = Circle(30)
canvas.add(ci)
animate_sunrise(ci, "red", "yellow", "dark blue", "light blue")
