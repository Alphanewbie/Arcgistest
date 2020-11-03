- docker build -t cwleecr.azurecr.io/arcgis_test:latest .

- docker push cwleecr.azurecr.io/arcgis_test:latest

- docker run -d -p 8000:8000 -p 8888:8888 --name arcgis_test cwleecr.azurecr.io/arcgis_test:latest
