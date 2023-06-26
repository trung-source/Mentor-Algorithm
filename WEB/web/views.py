from flask import Blueprint, render_template,request,flash,Response                                                # Là thiết kế cho ứng dụng: từng trang web (URL)
from flask_login import login_required, current_user
from . import db
from .models import Note
from . import source_test
# from . import source_2_test_2

import json

from io import BytesIO
import base64


import io
import random

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib import pyplot as plt

from matplotlib.figure import Figure

from bokeh.embed import components
from bokeh.plotting import figure



views = Blueprint('views',__name__)                                                          # Đặt cùng tên cho đơn giản

@views.route('/', methods = ['GET','POST'])
# @login_required
def home():
    # num_x_points = int(request.args.get("num_x_points", 50))
    # Generate the figure **without using pyplot**.
    # fig = Figure()
    # ax = fig.subplots()
    # ax.plot([1, 2])
    # # Save it to a temporary buffer.
    # buf = BytesIO()
    # fig.savefig(buf, format="png")
    # # Embed the result in the html output.
    # data = base64.b64encode(buf.getbuffer()).decode("ascii")
    # return f"<img src='data:image/png;base64,{data}'/>"

    from bokeh.plotting import figure
    p = figure(title="Mentor1",plot_width=800, plot_height=800)
    p2 = figure(title="Mentor2",plot_width=800, plot_height=800) 
    graph1=source_test.source_func(Node=source_test.Node,Umin=source_test.umin,Alpha=source_test.alpha,graph=p)
    graph2=source_test.source_func_2(Node=source_test.Node,Umin=source_test.umin,Alpha=source_test.alpha,graph=p2)

    script, div = components(graph1)
    script2, div2 = components(graph2)
    if request.method == 'POST':
        Rand = request.form.get('Randoom')
        Umin = float(request.form.get('umin'))
        Alpha = float(request.form.get('alpha'))
        Traff = request.form.get('Traffic')
        
         
        flash("SUCCESS")

        from random import randint, random
        if int(Rand) == 1:
            Nodes = []
            for i in range(180):
                Nodes.append(randint(1,1000))
        else:
            Nodes = []
            for i in range(len(source_test.Node)):
                node_name = 'node-'+str(i+1)
                temp = request.form.get(node_name)
                Nodes.append(int(temp))
        # flash(Rand)
        source_test.Node = Nodes
        source_test.alpha = Alpha
        source_test.umin = Umin
        # if(len(Umin)>1):
        #     flash(Umin)
            # flash(source.Node)

        p = figure(title="Mentor1",plot_width=800, plot_height=800)
        p2 = figure(title="Mentor2",plot_width=800, plot_height=800) 
        graph1=source_test.source_func(Node=Nodes,Umin=Umin,Alpha=Alpha,graph=p,New_trafic=int(Traff))
        graph2=source_test.source_func_2(Node=Nodes,Umin=Umin,Alpha=Alpha,graph=p2)

        script, div = components(graph1)
        script2, div2 = components(graph2)

    #     if len(note)<1:
    #         flash('Note qua ngan!',category = 'error')
    #     else:
    #         new_note = Note(data = note, user_id=current_user.id)
    #         db.session.add(new_note)
    #         db.session.commit()
    #         flash('Note da duoc tao!', category = 'success')
    return render_template("home.html", user=current_user, Node_all= source_test.Node,
    Umin = source_test.umin,Alpha=source_test.alpha,Rand0=0,Rand1=1,Add_traffic0=0,Add_traffic1=1,
    script = script,
    div = div, script2 = script2, div2 = div2)


# @views.route("/Mentor1-<float:Umin>-<float:Alpha>-<Node_all>.png")
# def plot_png(Node_all=source_test.Node,Umin=source_test.umin,Alpha=source_test.alpha):
#     """ renders the plot on the fly.
#     """
#     Node_all = json.loads(Node_all)
#     fig1 = Figure()

#     #         print(i)
#     # axis = fig.add_subplot(1, 1, 1)
#     # x_points = range(num_x_points)
#     # axis.plot(x_points, [random.randint(1, 30) for x in x_points])

#     fig1,axis1 = source_test.source_func(Node=Node_all,Umin=Umin,Alpha=Alpha,fig=fig1)
#     output1 = io.BytesIO()
#     FigureCanvasAgg(fig1).print_png(output1)
#     print("OUT1",fig1)
#     # canvas = FigureCanvasAgg(fig1)
#     # canvas.draw()
#     axis1.clear()

#     return Response(output1.getvalue(), mimetype="image/png")


# # from .source_2_test_2 import source_func as sf
    
# @views.route("/Mentor2-<float:Umin>-<float:Alpha>-<Node_all>.png")
# def plot_png_mentor2(Node_all=source_test.Node,Umin=source_test.umin,Alpha=source_test.alpha):
#     """ renders the plot on the fly.
#     """
#     # fig2 = plt.figure()
#     fig2 = Figure()
#     Node_all = json.loads(Node_all)
#     print(type(Node_all))

#     #         print(i)
    
    
#     fig2,axis=source_test.source_func_2(Node=Node_all,Umin=Umin,Alpha=Alpha,fig=fig2)
#     output = io.BytesIO()
#     FigureCanvasAgg(fig2).print_png(output)

#     print("OUT",fig2)

#     # canvas = FigureCanvasAgg(fig2)
#     # canvas.draw()
#     # axis.clear()
#     return Response(output.getvalue(), mimetype="image/png")