# Agent Check: Ambari

## Overview

This check monitors [Ambari][1] through the Datadog Agent.

## Setup

Follow the instructions below to install and configure this check for an Agent running on a host. For containerized environments, see the [Autodiscovery Integration Templates][9] for guidance on applying these instructions.

### Installation

The Ambari check is included in the [Datadog Agent][2] package.
No additional installation is needed on your server.

### Configuration

1. Edit the `ambari.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to start collecting your Ambari performance data. See the [sample ambari.d/conf.yaml][3] for all available configuration options.

2. [Restart the Agent][4].

#### Log collection

 **Available for Agent >6.0**

 1. Collecting logs is disabled by default in the Datadog Agent, enable it in your `datadog.yaml` file:

     ```yaml
      logs_enabled: true
    ```

 2. Edit your `ambari.d/conf.yaml` by uncommenting the `logs` lines at the bottom. Update the logs `path` with the correct path to your Ambari log files.

    ```yaml
      logs:
        - type: file
          path: /var/log/ambari-server/ambari-alerts.log
          source: ambari
          service: ambari
          log_processing_rules:
              - type: multi_line
                name: new_log_start_with_date
                pattern: \d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])  # 2019-04-22 15:47:00,999
      ...
    ```

 3. [Restart the Agent][4].

### Validation

[Run the Agent's status subcommand][5] and look for `ambari` under the Checks section.


## Data Collected

This integration collects for every host in every cluster the following system metrics:

* boottime
* cpu
* disk
* memory
* load
* network
* process

If service metrics collection is enabled with `collect_service_metrics` this integration collects for each whitelisted service component the metrics with headers in the white list.

### Metrics

See [metadata.csv][7] for a list of all metrics provided by this integration.

### Service Checks

**ambari.can_connect**:<br>
Returns `OK` if the cluster is reachable, otherwise returns `CRITICAL`.

**ambari.state**:<br>
Returns `OK` if the service is installed or running, `WARNING` if the service is stopping or uninstalling,
or `CRITICAL` if the service is uninstalled or stopped.

### Events

Ambari does not include any events.

## Troubleshooting

Need help? Contact [Datadog support][8].

[1]: https://ambari.apache.org
[2]: https://docs.datadoghq.com/agent
[3]: https://github.com/DataDog/integrations-core/blob/master/ambari/datadog_checks/ambari/data/conf.yaml.example
[4]: https://docs.datadoghq.com/agent/guide/agent-commands/?tab=agentv6#start-stop-and-restart-the-agent
[5]: https://docs.datadoghq.com/agent/guide/agent-commands/?tab=agentv6#agent-status-and-information
[6]: https://github.com/DataDog/integrations-core/blob/master/ambari/datadog_checks/ambari/data/conf.yaml.example
[7]: https://github.com/DataDog/integrations-core/blob/master/ambari/metadata.csv
[8]: https://docs.datadoghq.com/help
[9]: https://docs.datadoghq.com/agent/autodiscovery/integrations
