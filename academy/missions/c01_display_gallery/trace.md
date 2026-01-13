# Trace a Small Example (C-01)

Use this example:

- `w=200`, `h=100`, `padding=10`, `gap=10`, `box_count=3`

1. What is the `(x1, y1, x2, y2)` for the first box?
   200 width - 20 padding = 180
   2 gaps for 3 boxes is 2 x 10 = 20
   180 - 20 = 160
   160 / 3 = 53.33 -> 53

x1 = 0 + 10 = 10
y1 = 0 + 10 = 10
x2 = x1 + 53 = 60
y2 = 100 - 10 = 90
(10, 10, 63, 90)

2.  What is the `(x1, y1, x2, y2)` for the second box?

x1 = 63 + 10 = 73
y1 = 0 + 10 = 10
x2 = x1 + 53 = 126
y2 = 100 - 10 = 90
(73, 10, 126, 90)
