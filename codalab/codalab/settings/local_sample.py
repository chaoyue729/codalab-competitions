"""
Provide a template to define local configuration settings. Make a copy of this
file named 'local.py' and set appropriate values for the settings.
"""

import subprocess

from base import DevBase


def naive_docker_service(service_name, port):
    """
    Simple command to retrieve the ip and port of the codalabcompetition docker containers.

    `docker-compose up` need to be running for the container to be discoverable.
    """
    cmd = """docker port codalabcompetitions_%s_1 %s""" % (service_name, port)
    out = subprocess.check_output(cmd, shell=True)
    host, port = out.decode('utf-8').strip().split(':')
    return host, port


# Uncomment this line if you're using the `docker-compose up` to run mysql:
# db_host, db_port = naive_docker_service('db', 3306)

class Dev(DevBase):
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # Azure Storage
    DEFAULT_FILE_STORAGE = 'codalab.azure_storage.AzureStorage'

    AZURE_ACCOUNT_NAME = 'your_account_name'
    AZURE_ACCOUNT_KEY = 'your_key_RE1uSw3y37MaRSUtUYkj+o2//AaoHv5YwcqGCUgRXoT2WPNt+iaaz/6KB2Oiyz8Y7FPA=='
    AZURE_CONTAINER = 'name_of_your_container_for_public_blobs'

    BUNDLE_AZURE_ACCOUNT_NAME = AZURE_ACCOUNT_NAME
    BUNDLE_AZURE_ACCOUNT_KEY = AZURE_ACCOUNT_KEY
    BUNDLE_AZURE_CONTAINER = 'name_of_your_private_container_for_bundles'

    # Service Bus
    SBS_NAMESPACE = '<service bus name>'
    SBS_ISSUER = 'owner'
    SBS_ACCOUNT_KEY = '<acs default key>'
    SBS_RESPONSE_QUEUE = 'response'  # incoming queue for site worker
    SBS_COMPUTE_QUEUE = 'compute'  # incoming queue for Windows compute worker

    # Database Setup
    DATABASES = {
        'default': {
            # Default: use sqlite3 (no setup, not scalable)
            'ENGINE': 'django.db.backends.sqlite3',  # Simple database
            'NAME': 'codalab.sqlite3',  # Path to database file

            ## Uncomment the following if you use MySQL (recommended):
            # 'ENGINE': 'django.db.backends.mysql',
            # 'NAME': 'codalab_website',            # Name of the database.
            # 'USER': 'root',
            # 'PASSWORD': 'mysql',
            ##  Use host '' (empty) for localhost through domain sockets or '127.0.0.1' for localhost through TCP:
            # 'HOST': db_host,
            ## Use port '' (empty) for the default value:
            # 'PORT': db_port,

            ## Uncomment the following if you use SQLServer:
            # 'ENGINE': 'sql_server.pyodbc',
            # 'NAME': 'somename',
            ## Leave user and password blank to use integrated security
            # 'USER': '',
            # 'PASSWORD': '',
            # 'HOST': '(localdb)\\v11.0',
            # 'PORT': '',
            # 'OPTIONS': {
            #     'driver': 'SQL Server Native Client 11.0',
            # }

            # Alternatives to 'mysql': 'postgresql_psycopg2', 'mysql', 'oracle'

        }
    }
