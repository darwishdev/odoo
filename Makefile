run: 
	python3 odoo-bin --addons-path=addons -c debian/odoo.conf --without-demo=all -d=retail_odoo

new: 
	python3 odoo-bin scaffold $(name) custom


dropdb:
	docker exec -it postgres  dropdb --username=dev   $(name)