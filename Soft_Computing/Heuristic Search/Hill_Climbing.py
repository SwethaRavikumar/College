import pandas as pd
import numpy as np
import math
import networkx as nx
#from networkx.drawing.nx_agraph import graphviz_layout
#import matplotlib.pyplot as plt

def reversal_node(df_row, current_node):
    if df_row['to'] == current_node:
        df_row['from'], df_row['to'] = df_row['to'],df_row['from']
    return df_row

def get_all_edges(closed, parent, end_node, edges_list):
    edges = []
    for index, row in closed.iterrows():
        edge_ = edges_list.loc[((edges_list['from']==row['node'])&(edges_list['to']==parent[row['node']]))|((edges_list['from']==parent[row['node']])&(edges_list['to']==row['node']))]
        if not edge_.empty:
            edges.append((parent[row['node']], row['node'], edge_.iloc[0]['weights']))
    weight_goal = edges_list.loc[(edges_list['from']==parent[end_node])&(edges_list['to']==end_node)]
    edges.append((parent[end_node], end_node,weight_goal.iloc[0]['weights']))
    return edges
    
    
edges = pd.read_csv('edge_list.csv')
straight_dist = pd.read_csv('straight_line.csv', header=None, index_col=0, squeeze=True).to_dict()
start_node, end_node = 'A','R'
result = hillClimbing(edges, straight_dist, start_node, end_node)
print(" Success: {}".format(result['success']))
