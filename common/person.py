class Person(object):
	def __init__(self, uid="", name="", email="", job_title="", colleagues=None):
		self.set_attribute(uid, name, email, job_title, colleagues)

	def __str__(self):
		if self.colleagues:
			colleagues = []
			for colleague in self.colleagues:
				colleagues.append(str(colleague))
			return "Person {0} ({1}) (E-mail:{2}) has colleagues:{3}".format(self.name, self.job_title, self.email, colleagues)
		else:
			return "Person {0} ({1}) (E-mail:{2})".format(self.name, self.job_title, self.email)

	def set_attribute(self, uid="", name="", email="", job_title="", colleagues=None):
		self.uid = uid
		self.name = name
		self.email = email
		self.job_title = job_title
		self.colleagues = colleagues
