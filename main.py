class Cash:
	amount=0
	def top_up(self,money):
		self.amount+=money
	def count_1000(self):
		return int(self.amount/1000)
	def take_away(self,quantity):
		if self.amount>=quantity:
			self.amount-=quantity
			print(f'выдано {quantity}')
		else:
			raise ValueError('недостаточно денег в кассе')
