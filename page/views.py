from django.shortcuts import render
from django.views.generic import TemplateView
import matplotlib.pyplot as plt
import numpy as np
from math import sin
from io import BytesIO
import base64
from numpy import sin
import re


class HomePage(TemplateView):
    template_name = 'base.html'

def programm(request):
    fig, ax = plt.subplots()
    ax.set_xlim((-5, 5))
    ax.set_ylim((-5, 5))
    ax.set_aspect("equal")
    ax.grid()
    ax.set_title("Заголовок")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    x = np.linspace(-5, 5, 100)
    formy = request.GET['y']
    g = re.findall('(\d+)', formy)
    g = ', '.join(g)
    y = request.GET['y']
    #y = eval('sin(x*' + g + ')')
    ax.plot(x, y)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'programm.html', {'graphic': graphic})
