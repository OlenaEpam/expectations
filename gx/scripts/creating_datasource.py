server_url = "127.0.0.1"
database_name = "TRN"
user = "OlenaPavlyushchik"
password = "Oredko0808"

my_connection_string = (f"mssql+pyodbc://{user}:{password}@{server_url}/"
                        f"{database_name}?driver=ODBC+Driver+18+for+SQL+Server&charset=utf"
                        f"&autocommit=true&TrustServerCertificate=yes")

datasource_config = {
    "name": "my_datasource_38",
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
