from flask import Blueprint, render_template,request,flash,Response                                                # Là thiết kế cho ứng dụng: từng trang web (URL)
from flask_login import login_required, current_user
from . import db
from .models import Note
# from . import source_test
from . import source_2_test_2

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

views2 = Blueprint('views2',__name__)                                                          # Đặt cùng tên cho đơn giản

@views2.route('/mentor2', methods = ['GET','POST'])
# @login_required
def home2():
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


    if request.method == 'POST':
        note = request.form.get('note')
        Umin = request.form.get('umin')
        Alpha = request.form.get('alpha')
        Nodes = []
        for i in range(len(source_2_test_2.Node)):
            node_name = 'node-'+str(i+1)
            temp = request.form.get(node_name)
            Nodes.append(int(temp))
         
        flash(Nodes)
        source_2_test_2.Node = Nodes
        source_2_test_2.alpha = Alpha
        source_2_test_2.umin = Umin
        if(len(Umin)>1):
            flash(Umin)
            # flash(source.Node)



    #     if len(note)<1:
    #         flash('Note qua ngan!',category = 'error')
    #     else:
    #         new_note = Note(data = note, user_id=current_user.id)
    #         db.session.add(new_note)
    #         db.session.commit()
    #         flash('Note da duoc tao!', category = 'success')
    return render_template("home2.html", user=current_user, Node_all= source_2_test_2.Node,Umin = source_2_test_2.umin,Alpha=source_2_test_2.alpha)


@views2.route("/Mentor2-<float:Umin>-<float:Alpha>-<Node_all>.png")
def plot_png(Node_all=source_2_test_2.Node,Umin=source_2_test_2.umin,Alpha=source_2_test_2.alpha):
    """ renders the plot on the fly.
    """
    Node_all = json.loads(Node_all)
    fig1 = Figure()

    #         print(i)
    # axis = fig.add_subplot(1, 1, 1)
    # x_points = range(num_x_points)
    # axis.plot(x_points, [random.randint(1, 30) for x in x_points])

    fig1,axis = source_2_test_2.source_func(Node=Node_all,Umin=Umin,Alpha=Alpha,fig=fig1)
    output = io.BytesIO()
    FigureCanvasAgg(fig1).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")

