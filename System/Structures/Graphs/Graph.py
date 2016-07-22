#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Vertex import Vertex

class Graph:
    
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        return self.vert_dict[n] if n in self.vert_dict else None

    def add_edge(self, frm, to):
        self.vert_dict[frm].add_neighbor(self.vert_dict[to])
        self.vert_dict[to].add_neighbor(self.vert_dict[frm])

    def get_vertices(self):
        return self.vert_dict.keys()
