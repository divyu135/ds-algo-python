version: 2

pre-hook:
  - query: |
      {% set schema_name = "my_dataset" %}
      {% set sql_query %}
      SELECT
        table_name
      FROM
        `{{ config.project }}.{{ schema_name }}.__TABLES__`
      {% endset %}
      {% set results = run_query(sql_query) %}
      {% set table_names = [] %}
      {% for row in results %}
        {% do table_names.append(row.table_name) %}
      {% endfor %}
      {% set my_variable = table_names %}
    vars:
      - var: my_variable
