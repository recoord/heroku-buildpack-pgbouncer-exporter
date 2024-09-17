# Heroku buildpack: pgbouncer exporter

This buildpack sets up the [PgBouncer exporter](https://github.com/prometheus-community/pgbouncer_exporter) to expose Metrics of PgBouncer running in the Heroku Dyno alongside application code.

## Usage

In your Procfile, start pgbouncer_exporter with a configuration then your application.

```console
bin/start-pgbouncer-exporter YOUR_PROC_CMD
```
