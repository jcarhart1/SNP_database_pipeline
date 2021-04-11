
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

# df = pd.read_sql()
df = pd.read_csv("C:/Users/jcarhart/Desktop/pharmgkb_long.csv")
df1 = df.fillna(0)


def generate_table(dataframe, max_rows=1000):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app = dash.Dash(
    __name__,
    external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div(children=[
    html.H4(children='Genetika+ PharmGKB Database'),
    dcc.Dropdown(id='dropdown1', options=[
        {'label': i, 'value': i} for i in df1.gene.unique()
    ], multi=False, placeholder='Filter by gene'),
    html.Div(id='table-container1')

    # dcc.Dropdown(id='dropdown2', options=[
    #     {'label': i, 'value': i} for i in df1.gene.unique()
    # ], multi=False, placeholder='Filter by variant'),
    # html.Div(id='table-container2')
])


@app.callback(
    dash.dependencies.Output('table-container1', 'children'),
    [dash.dependencies.Input('dropdown1', 'value')])
def display_table(dropdown_value):
    if dropdown_value is None:
        return generate_table(df1)

    dff = df1[df1.gene.str.contains(''.join(dropdown_value))]
    return generate_table(dff)

# @app.callback(
#     dash.dependencies.Output('table-container2', 'children'),
#     [dash.dependencies.Input('dropdown2', 'value')])
# def display_table(dropdown_value):
#     if dropdown_value is None:
#         return generate_table(df1)
#
#     dff = df1[df1.variant.str.contains(''.join(dropdown_value))]
#     return generate_table(dff)


# app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/JYBPQZ.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
