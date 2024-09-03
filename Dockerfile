
FROM python:3.9.17-slim-buster

# Set environment variables
ENV MySQLConnectionString=mysql+pymysql://taladmin:Nikifox2023!@prioriy-sandbox.mysql.database.azure.com/ \
    #local mysql server mysql+pymysql://root:Taltool87!@localhost:3306/
    MongoDBconnectionstring=mongodb+srv://talcohen0507:Taltool87!@erpdataplatform.t8ot6ep.mongodb.net/test \
    BlobConectionString=DefaultEndpointsProtocol=https;AccountName=priorityapiintegration;AccountKey=zp/xIg89+rpCtViB8EP5jakFAh66OxqD5dQ2goAgc7Rhi159FnmhqZYwLDwZPNo7/mJrXvXmFB92+AStqmvPew==;EndpointSuffix=core.windows.net

WORKDIR /app
COPY . /app


RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]

# RUN mkdir -p /app/output
# CMD ["sh", "-c", "ls -R > /app/output/files.txt"]

