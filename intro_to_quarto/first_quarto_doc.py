

import plotly.express as px
from itables import show

tips = px.data.tips()
show(tips)


# Displaying Plots


px.violin(tips, x="tip", y="sex")


# Displaying Static PLots



tips_sex = px.violin(tips, x="tip", y="sex")
tips_sex.write_image('tips_by_sex.png')




