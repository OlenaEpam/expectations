import great_expectations as ge
from great_expectations.profile.user_configurable_profiler import UserConfigurableProfiler
from great_expectations.core.batch import RuntimeBatchRequest
from creating_datasource import datasource_config

context = ge.get_context()
context.add_datasource(**datasource_config)

batch_request = RuntimeBatchRequest(
    datasource_name="my_datasource_38",
    data_connector_name="default_runtime_data_connector_name",
    data_asset_name="default_data_asset_name",
    runtime_parameters={
        "query": f"SELECT * FROM hr.employees"
    },
    batch_identifiers={
        "default_identifier_name": "identifier_value",
    },
)

validator = context.get_validator(batch_request=batch_request)

ignored_columns = [
    "employee_id",
    "first_name",
    "email",
    "phone_number",
    "hire_date",
    "job_id",
    "manager_id",
    "department_id",
]

profiler = UserConfigurableProfiler(
    profile_dataset=validator,
    excluded_expectations=None,
    ignored_columns=ignored_columns,
    not_null_only=False,
    primary_or_compound_key=None,
    semantic_types_dict=None,
    table_expectations_only=False,
    value_set_threshold="MANY",
)
suite = profiler.build_suite()
validator.save_expectation_suite()
print(suite.expectations)
checkpoint = context.add_or_update_checkpoint(
    name="my_quickstart_checkpoint",
    validator=validator,
)
results = checkpoint.run()
context.build_data_docs()
context.open_data_docs()
