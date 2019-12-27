from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField, FloatField

class Transactions(Document):
	date = DateTimeField()
	description = StringField()
	value = FloatField()
	card = StringField()
	currency = StringField()
	category = StringField()

	def __unicode__(self):
		return '{}: {}'.format(self.card, self.description, self.value)
