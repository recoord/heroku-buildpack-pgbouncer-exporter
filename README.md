# Heroku buildpack: pgbouncer exporter

This buildpack sets up the [PgBouncer exporter](https://github.com/prometheus-community/pgbouncer_exporter) to expose Metrics of PgBouncer running in the Heroku Dyno alongside application code.

## Usage

In your Procfile, start pgbouncer_exporter with a configuration then your application.

```console
bin/start-pgbouncer-exporter YOUR_PROC_CMD
```

Add environment variable PGBOUNCER_EXPORTER_CONNECTION_STRING with connection string to PgBouncer:
```code
PGBOUNCER_EXPORTER_CONNECTION_STRING = postgresql://pgbouncer@:6000/pgbouncer?host=/tmp&sslmode=disable&connect_timeout=30
```

As it's [recommended](https://github.com/prometheus-community/pgbouncer_exporter?tab=readme-ov-file#pgbouncer-configuration) in the PGBouncer Exporter docs, a configuration change to pgbouncer to ignore a PostgreSQL driver connection parameter is needed. Add this variable to Config vars of your application:
```code
PGBOUNCER_IGNORE_STARTUP_PARAMETERS = extra_float_digits
```
