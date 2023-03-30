def widgets_and_gixmos(widget,gizmos):
    total = 0
    return widget * 75 + gizmos * 112

a , b =  map(int, input('numbers of widgets and gizmos: ').split())
print(widgets_and_gixmos(a,b))