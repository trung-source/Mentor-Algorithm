from bokeh.plotting import figure, output_file, show,ColumnDataSource
from bokeh.models import  ColumnDataSource,Range1d, LabelSet, Label

from pandas.core.frame import DataFrame
source = DataFrame(
    dict(
        off_rating=[66, 71, 72, 68, 58, 62],
        def_rating=[165, 189, 220, 141, 260, 174],
        names=['Mark', 'Amir', 'Matt', 'Greg', 'Owen', 'Juan']
    )
)
p = figure(plot_width=600, plot_height=450, title = "'Offensive vs. Defensive Eff'")
p.circle('off_rating','def_rating',source=source,fill_alpha=0.6,size=10, )
p.xaxis.axis_label = 'off_rating'
p.yaxis.axis_label = 'def_rating'
labels = LabelSet(x='off_rating', y='def_rating', text='names',text_font_size='9pt',
              x_offset=5, y_offset=5, source=ColumnDataSource(source), render_mode='canvas')
p.add_layout(labels)
show(p)