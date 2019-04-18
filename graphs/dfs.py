
class Node:
	def __init__(self, val):
		self.val = val
		self.visited = False
		self.adj_list = []
	
	def visit(curr_node):
		curr_node.visited = True
		
	def dfs(self, root):
		if self.root == None:
			return
		self.visit(self.root)
		for adj_node in self.adj_list:
			if adj_node.visited == False:
				search(adj_node)

	def dfs_visit(self, curr_graph, curr_node):
		time += 1
		
				
	def bfs(self, root):
		q = Queue()
		self.visit(root)
		q.put(root)

		while not q.empty():
			curr_node = q.get()
			for adj_node in curr_node.adj_list:
				if adj_node.visited == False:
					self.visit(adj_node)
					q.put(adj_node)
