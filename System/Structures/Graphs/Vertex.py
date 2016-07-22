#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Vertex:
    
    def __init__(self, node):
        self.id = node
        self.adjacent = []

    def add_neighbor(self, neighbor): self.adjacent.append(neighbor)

    def get_adjacents(self): return self.adjacent  

    def get_id(self): return self.id
