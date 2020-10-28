from flask import Flask, render_template #imports flask into program
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)


# @app.route('/') #main page of the HTML - dashboard
# def index():
#     return render_template('dashboard.html') #renders template


# @app.route('/data') #route to data page of the HTML
# def data():
#     return render_template('data.html') #renders template


# @app.route('/plot.png') #route to graph page of the HTMl
# def plot_png():
#     fig = create_figure()
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype='image/png')


# def create_figure():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     xs = range(100)
#     ys = [random.randint(1, 50) for x in xs]
#     axis.plot(xs, ys)
#     return fig