from flask import render_template
from flask_appbuilder import ModelView
from flask_appbuilder.models.mongoengine.interface import MongoEngineInterface
from app import appbuilder
from .models import *

class TransactView(ModelView):
	datamodel = MongoEngineInterface(Transactions)
	list_columns = ['date','description','value','card','currency','category']


"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

appbuilder.add_view(TransactView,"TransactView",icon="fa-folder-open-o")