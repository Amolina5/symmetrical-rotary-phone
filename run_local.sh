
# this enviroment variavle tells flask hoe to find your app so it can run it

export FLASK_APP=app/routes.py
#this enivirtoment variable sets your enviroment to development which enjances debug mode
export FLASK_ENV=development
# this enables debug mode, which will also trigger auto relaod the sever restart when you save
export FLASK_DEBUG=1

flask run