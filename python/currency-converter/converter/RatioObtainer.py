import json, datetime, urllib.request


class RatioObtainer:
	base = None
	target = None

	API_KEY = "[INSERT API KEY HERE]"

	def __init__(self, base, target):
		self.base = base
		self.target = target

	def was_ratio_saved_today(self, return_ratio=False):
		# TODO
		# This function checks if given ratio was saved today and if the file with ratios is created at all
		# should return false when file doesn't exist or if there's no today's exchange rate for given values at all
		# should return true otherwise
		with open('ratios.json') as f:
			data = json.load(f)
			today = datetime.date.today().strftime("%Y-%m-%d")
			ratio = next(filter(lambda r:
				r["base_currency"] == self.base
				and r["target_currency"] == self.target
				and r["date_fetched"] == today, data), None)
		return ratio["ratio"] if return_ratio and ratio is not None else ratio is not None

	def fetch_ratio(self):
		# TODO
		# This function calls API for today's exchange ratio
		# Should ask API for today's exchange ratio with given base and target currency
		# and call save_ratio method to save it
		url = f"http://api.exchangerate.host/live?access_key={self.API_KEY}&source={self.base}&currencies={self.target}"
		with urllib.request.urlopen(url) as response:
			data = json.load(response)
			self.save_ratio(data["quotes"][f"{self.base}{self.target}"])

	def save_ratio(self, ratio):
		with open('ratios.json', 'r') as f:
			data = json.load(f)
			for saved_ratio in data:
				if saved_ratio["base_currency"] == self.base and saved_ratio["target_currency"] == self.target:
					saved_ratio["date_fetched"] = datetime.date.today().strftime("%Y-%m-%d")
					saved_ratio["ratio"] = ratio
					break
			else:
				data.append({
					"base_currency": self.base,
					"target_currency": self.target,
					"date_fetched": datetime.date.today().strftime("%Y-%m-%d"),
					"ratio": ratio,
				})

		with open('ratios.json', 'w') as f:
			json.dump(data, f)

	def get_matched_ratio_value(self):
		return self.was_ratio_saved_today(True)
