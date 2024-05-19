import great_expectations as ge
from great_expectations.profile.user_configurable_profiler import UserConfigurableProfiler
from great_expectations.core.batch import BatchRequest
from great_expectations.core.batch import RuntimeBatchRequest
from great_expectations.checkpoint import SimpleCheckpoint


server_url = "127.0.0.1"
database_name = "TRN"
table = "hr.employee"
user = "OlenaPavlyushchik"
password = "Oredko0808"

my_connection_string = (f"mssql+pyodbc://{user}:{password}@{server_url}/"
                        f"{database_name}?driver=ODBC+Driver+18+for+SQL+Server&charset=utf&autocommit=true&TrustServerCertificate=yes")

datasource_config = {
    "name": "my_datasource_36",
    "class_name": "Datasource",
    "execution_engine": {
        "class_name": "SqlAlchemyExecutionEngine",
        "connection_string": my_connection_string
    },
    "data_connectors": {
        "default_runtime_data_connector_name": {
            "class_name": "RuntimeDataConnector",
            "batch_identifiers": ["default_identifier_name"],
        }
    }
}
