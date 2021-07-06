class FieldElement:
	def __init__(self, num: int, prime: int):
		if num>=prime or num<0:
			error = f"Num {num} not in the field range 0 to {prime}"
			raise ValueError(error)
		self.num = num
		self.prime = prime
	
	def __repr__(self):
		return f'FieldElement_{self.prime}({self.num})'
	
	def __eq__(self, other):
		if other == None:
			return False
		return self.num == other.num and self.prime == other.prime
	
	def __ne__(self, other):
		if other == None:
			raise ValueError(f"Cannot compare {other} with FiniteField")
		return self.num != other.num or self.prime != other.prime