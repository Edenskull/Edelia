import json


class Config:

	_envar = ".env"

	@staticmethod
	def get_config():
		with open(Config._envar, 'r', encoding="UTF-8") as config_file:
			current_conf = json.load(config_file)
		return current_conf

	@staticmethod
	def update_config(new_config):
		with open(Config._envar, 'w', encoding="UTF-8") as config_file:
			json.dump(new_config, config_file, indent=4)

	@staticmethod
	def get_option(option):
		with open(Config._envar, 'r', encoding="UTF-8") as config_file:
			current_conf = json.load(config_file)
		if option not in current_conf:
			return None
		else:
			return current_conf[option]
