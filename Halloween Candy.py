#1 khune mesvak mide 2 khune dollar midan
#tedade kolle khune ha dade mishe, mizan % ehtemale inke chizi ke random az kifet dar miari dollar bashe cheqade?
# integer neshuneye kolle khune ha be onvane input
# khuruji ye % e ke be bala gerd shode

houses = int(input())
percent = 100 / houses
d = 2 * percent
if int(d) == float(d):
    print(int(d))
else:
    print(int(d) + 1)

