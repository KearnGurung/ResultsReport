#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import random
import os

import plotly.express as px
import plotly.graph_objects as gp   
from dash.exceptions import PreventUpdate
from dash import Dash, dash_table
from dash import Input, Output, State, html
from dash import Dash, dcc, html, Input, Output
from jupyter_dash import JupyterDash
import dash_bootstrap_components as dbc


# In[2]:


df=pd.read_csv('Grade10.csv')
df1=pd.read_csv('Grade12.csv')
df.astype(str)
df1.astype(str)


# In[3]:


def avg(Grade):
    
    if (Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        k=df2[df2['Name']=='Kiran']
        k.sort_values('Score', ascending=False,inplace=True)
        kk=k.head(5)
        kavg=kk.mean()
       
    
    else:
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        k=df2[df2['Name']=='Kiran']
        k.sort_values('Score', ascending=False,inplace=True)
        kk=k.head(5)
        kavg=kk.mean()

    return kavg


# In[4]:


def avg1(Grade):
    
    if (Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        n=df2[df2['Name']=='Namgay']
        n.sort_values('Score', ascending=False,inplace=True)
        nn=n.head(5)
        kavg1=nn.mean()
       
    
    else:
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        n=df2[df2['Name']=='Namgay']
        n.sort_values('Score', ascending=False,inplace=True)
        nn=n.head(5)
        kavg1=nn.mean()

    return kavg1


# In[5]:


def mapdata(Grade):
    if(Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Lat','Long','Dzongkhag']].copy()
        kmap10=gg1[gg1['Name']=='Kiran']
        
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Lat','Long','Dzongkhag']].copy()
        kmap12=gg1[gg1['Name']=='Kiran']
        
    else:
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Lat','Long','Dzongkhag']].copy()
        kmap10=gg1[gg1['Name']=='Kiran']
        
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Lat','Long','Dzongkhag']].copy()
        kmap12=gg1[gg1['Name']=='Kiran']
        
    return[kmap10,kmap12]


# In[6]:


def mapdata1(Grade):
    if(Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Lat','Long','Dzongkhag']].copy()
        nmap10=gg1[gg1['Name']=='Namgay']
        
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Lat','Long','Dzongkhag']].copy()
        nmap12=gg1[gg1['Name']=='Namgay']
        
    else:
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Lat','Long','Dzongkhag']].copy()
        nmap10=gg1[gg1['Name']=='Namgay']
        
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Lat','Long','Dzongkhag']].copy()
        nmap12=gg1[gg1['Name']=='Namgay']
        
    return[nmap10,nmap12]


# In[7]:


def getkiran():
    df10 = df[df['Name']=="Kiran"]
    df10 = df[df['Name']=="Kiran"]
    df12 = df1[df1['Name']=="Kiran"]
    dfk = pd.concat([df10, df12])
    return dfk


# In[8]:


def getnamgay():
    df10 = df[df['Name']=="Namgay"]
    df10 = df[df['Name']=="Namgay"]
    df12 = df1[df1['Name']=="Namgay"]
    dfn = pd.concat([df10, df12])
    return dfn


# In[9]:


def scoreinfo(Grade):
    
    if (Grade=='10th grade'):
        pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        k=df2[df2['Name']=='Kiran']
        highestscore = k.max()[2]
        highestscore
        
        grpscore = k.groupby(['Name','Subject']).sum()['Score']
        sub_nam = grpscore.idxmax()[1]
       
    
    else:
        pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        k=df2[df2['Name']=='Kiran']
        highestscore = k.max()[2]
        highestscore
        
        grpscore = k.groupby(['Name','Subject']).sum()['Score']
        sub_nam = grpscore.idxmax()[1]

    return [sub_nam,highestscore]


# In[10]:


def scoreinfo1(Grade):
    
    if (Grade=='10th grade'):
        pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        n=df2[df2['Name']=='Namgay']
        highestscore1 = n.max()[2]
        highestscore1
        
        grpscore = n.groupby(['Name','Subject']).sum()['Score']
        sub_nam1 = grpscore.idxmax()[1]
       
    
    else:
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        n=df2[df2['Name']=='Namgay']
        highestscore1 = n.max()[2]
        highestscore1
        
        grpscore = n.groupby(['Name','Subject']).sum()['Score']
        sub_nam1 = grpscore.idxmax()[1]
        
    return [sub_nam1,highestscore1]


# In[11]:


def gradedata(Grade):
    if(Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        k=df2[df2['Name']=='Kiran']
        
        df1=pd.read_csv('Grade12.csv')
        gg3 = df1[['Name','Subject','Score']].copy()
        df4 = gg3.groupby(['Name','Subject']).sum()[['Score']]
        df4.reset_index(inplace=True)
        k12=df4[df4['Name']=='Kiran']
        
    else:
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        k=df2[df2['Name']=='Kiran']
        
        df1=pd.read_csv('Grade12.csv')
        gg3 = df1[['Name','Subject','Score']].copy()
        df4 = gg3.groupby(['Name','Subject']).sum()[['Score']]
        df4.reset_index(inplace=True)
        k12=df4[df4['Name']=='Kiran']
        
    return[k,k12]


# In[12]:


def gradedata1(Grade):
    if(Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg2 = df[['Name','Subject','Score']].copy()
        df3 = gg2.groupby(['Name','Subject']).sum()[['Score']]
        df3.reset_index(inplace=True)
        n=df3[df3['Name']=='Namgay']
        
        df1=pd.read_csv('Grade12.csv')
        gg4 = df1[['Name','Subject','Score']].copy()
        df5 = gg4.groupby(['Name','Subject']).sum()[['Score']]
        df5.reset_index(inplace=True)
        n12=df5[df5['Name']=='Namgay']
    else:
        df=pd.read_csv('Grade10.csv')
        gg2 = df[['Name','Subject','Score']].copy()
        df3 = gg2.groupby(['Name','Subject']).sum()[['Score']]
        df3.reset_index(inplace=True)
        n=df3[df3['Name']=='Namgay']
        
        df1=pd.read_csv('Grade12.csv')
        gg4 = df1[['Name','Subject','Score']].copy()
        df5 = gg4.groupby(['Name','Subject']).sum()[['Score']]
        df5.reset_index(inplace=True)
        n12=df5[df5['Name']=='Namgay']

        
    return[n,n12]


# In[13]:


def drawfig(Grade):
    [kmap10,kmap12]=mapdata(Grade)
    [k,k12]=gradedata(Grade)
    if(Grade=='10th grade'):
        fig1 = px.bar(k, x='Subject', y='Score',color='Subject',title='Grade 10 Score(100)',text='Score',width=700,height=500)
        fig1.update_yaxes(range=[0,100])
        fig2 = px.scatter_mapbox(kmap10, lat="Lat", lon="Long", color="Dzongkhag")
        fig2.update_layout(mapbox_style="open-street-map")
    else:
        fig1 = px.bar(k12, x='Subject', y='Score',color='Subject',title='Grade 12 Score(100)',text='Score',width=700,height=500)
        fig1.update_yaxes(range=[0,100])
        fig2 = px.scatter_mapbox(kmap12, lat="Lat", lon="Long", color="Dzongkhag")
        fig2.update_layout(mapbox_style="open-street-map")
    return [fig1,fig2]       


# In[14]:


def drawfig1(Grade):
    [nmap10,nmap12]=mapdata1(Grade)
    [n,n12]=gradedata1(Grade)
    if(Grade=='10th grade'):
        fig1 = px.bar(n, x='Subject', y='Score',color='Subject',title='Grade 10 Score(100)',text='Score',width=700,height=500)
        fig1.update_yaxes(range=[0,100])
        fig2 = px.scatter_mapbox(nmap10, lat="Lat", lon="Long", color="Dzongkhag")
        fig2.update_layout(mapbox_style="open-street-map")
    else:
        fig1 = px.bar(n12, x='Subject', y='Score',color='Subject',title='Grade 12 Score(100)',text='Score',width=700,height=500)
        fig1.update_yaxes(range=[0,100])
        fig2 = px.scatter_mapbox(nmap12, lat="Lat", lon="Long", color="Dzongkhag")
        fig2.update_layout(mapbox_style="open-street-map")
    return [fig1,fig2]


# In[15]:


app = JupyterDash(external_stylesheets=[dbc.themes.LUMEN, dbc.icons.FONT_AWESOME])
app.title = "Dashbord for results"
server = app.server


# In[16]:


Grade= ['10th grade','12th grade']
#1st div
app.layout = dbc.Container(
    [
        html.H1('Welcome to Grade Report',style={'textAlign':'center','color':'#3498db','fontsize':50}),
        
       dbc.Card(
            [
                dbc.CardImg(src="https://lh3.google.com/pw/AM-JKLX1MmVwzMvUUs96Xjjj-18hh_C80ThearL9D8XJEaWXluHkSVoDRioACxmeU2US9mdUQe2GqyNCjlgdykK-nDW-DFKUH9I=w1179-h884-no?authuser=0", top=True),
                dbc.CardBody(
                    [
                        html.H4("Namgay and Kiran", className="card-title"),
                        html.P(
                            "Middle one is our madam Dr. Myo Thida, "
                            "left side one is Namgay and right side one is Kiran.",
                            className="card-text",
                        ),
                        dbc.Button("Namgay Tshering",
                                   href="https://www.facebook.com/tshering.foa",
                                   color="#32a852",
                                   id="collapse-button",
                                   n_clicks=0,
                                   className="mb-3",),
                        dbc.Collapse(
                        dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
                        id="collapse",
                        is_open=False,
                    ),
                        dbc.Button("Kiran Gurung",
                                   href="https://www.facebook.com/profile.php?id=100008197900713", 
                                   color="#3246a8",
                                   ),
                        
                    ]
                ),
            ],
            style={"width": "23rem"},
        ), 
        
        html.Br() ,
    
    #1st division
        html.Div(
            [
                dbc.Button(
                    dbc.Spinner(size="sm"),
                    color="primary",
                    disabled=True,
                    className="me-1",
                ),
                dbc.Button(
                    [dbc.Spinner(size="sm"), " Loading..."],
                    color="primary",
                    disabled=True,
                ),
            ]
        ),
        
        html.Span(
            [
                dbc.Badge(
                    "BCSE",
                    href="https://www.bcsea.bt/",
                    color="primary",
                    className="me-1 text-decoration-none",
                ),
                dbc.Badge(
                    "BHSCE",
                    href="https://www.bcsea.bt/",
                    color="secondary",
                    className="me-1 text-decoration-none",
                ),
            ]
        ),
        
        html.Div(
            [
                dbc.Row(dbc.Col(html.Div("***"), align="start")),
                dbc.Row(
                    [
                        dbc.Col(html.Div("Marks for:"), align="start"),
                        dbc.Col(html.Div("Class: X"), align="center"),
                        dbc.Col(html.Div("Class: XII"), align="end"),
                        
                    ]
                ),
            ],
            className="pad-row",
        ),  

        html.Br() ,
        
        dbc.Tabs([
            dbc.Tab(label="Namgay Tshering", tab_id="namgay"),
            dbc.Tab(label="Kiran Gurung", tab_id="kiran"),
            ], id="tabs", active_tab="namgay",
        ),
        
        #2nd div
        html.Div(
            [
                dbc.Alert("Hello!", color="primary"),
                dbc.Alert("Those are the figure for results of individual:", color="secondary"),
            ]
        ),
        
        html.Div([
            html.H2('Grade',style={'textAlign':'left','color':'#3498db','fontsize':40}),
            # create drop down
                dcc.Dropdown(id='grade_id',clearable=False,
                        options=[{'label':i,'value':i} for i in Grade],
                        placeholder='' ,
                         style={'width':'40%','padding':'3px','fontsize':40}),

            html.Div([
                html.H2('Highest Score Subject',style={'textAlign':'center','color':'#3498db','fontsize':20}),
                html.Div(id='numOf_id', style={'height': 30, 'textAlign':'center', 'fontsize':20,
                            'border-color': 'red','background-color': '#fcba03','margin-left': '20px'}), 
            ], id = 'num_box', style = {"width": "30%", 'padding': 10}),


            html.Div([
                html.H2('Highest Mark',style={'textAlign':'center','color':'#3498db','fontsize':20}),
                html.Div(id='major_id', style={'height': 30, 'textAlign':'center', 'fontsize':20,
                               'border-color': 'red','background-color': '#fcba03','margin-left': '20px'}), 
            ], id = 'offence_box', style = {"width": "30%", 'padding': 10}),

            html.Div([
                html.H2('Avarage Score(Top 5)',style={'textAlign':'center','color':'#3498db','fontsize':20}),
                html.Div(id='score_id', style={'height': 30, 'textAlign':'center', 'fontsize':20,
                               'border-color': 'red','background-color': '#32a852','margin-left': '20px'}), 
            ], id = 'score_box', style = {"width": "30%", 'padding': 10}),

        ], style = {'display': 'flex'}),

        html.Br() ,
        
        html.Div([
            dcc.Graph(id='plot1'),
            dcc.Graph(id='plot2'),

            ], style = {'display': 'flex'}),
        
        html.Div([
            dbc.Tabs([
                dbc.Tab(label="Kiran", tab_id="kiran"),
                dbc.Tab(label="Namgay", tab_id="namgay"),
                dbc.Tab(label="Grade 10", tab_id="G10"),
                dbc.Tab(label="Grade 12", tab_id="G12"),

            ],id="tabz",active_tab="Kiran"),
        ]),

        html.Div(id="table"),
    ]                
)
    


# In[17]:


@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)

def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# In[18]:


@app.callback(
    Output("table", "children"),
    Input('tabz','active_tab'),
)

def make_table(atab):
    if (atab =='kiran'):
        df = getkiran()
        
    elif(atab == 'namgay'):
        df = getnamgay()
        
    elif(atab == 'G10'):
        df = pd.read_csv('Grade10.csv')
        
    elif(atab == 'G12'):
        df = pd.read_csv('Grade12.csv')
        
    else:
        df = pd.read_csv('Grade10.csv')
        
    return dbc.Table.from_dataframe(df, striped=True, bordered=True, color = "primary", hover=True)


# In[19]:


@app.callback(
    [
    Output('numOf_id','children'),
    Output('major_id','children'),
    Output('score_id','children'),
    Output('plot1','figure'),
    Output('plot2','figure'),
    ],
    
    [Input('grade_id','value'),
    Input('tabs','active_tab')],   
           
)

def draw_graph(Grade,tabs):     
        
    if Grade is None or tabs is None:
        raise PreventUpdate
        
    elif(tabs=='namgay'):       
        [op1,op2]=scoreinfo1(Grade)
        [op3]=avg1(Grade)
        [fig1,fig2] =drawfig1(Grade)        
        
    elif(tabs=='kiran'):
        [op1,op2]=scoreinfo(Grade)
        [op3]=avg(Grade)
        [fig1,fig2] =drawfig(Grade)
        
    else:
        op1 = "Econonmics IT"
        op2 = 76
        [fig1,fig2] =drawfig(Grade)        
              
    return [op1,op2,op3,fig1,fig2]


# In[20]:


if __name__ == '__main__':
    port = 5000 + random.randint(0, 999)    
    url = "http://127.0.0.1:{0}".format(port)    
    app.run_server(use_reloader=False, debug=True, port=port)


# In[ ]:




