# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from six import iteritems

from datadog_checks.mapreduce import MapReduceCheck

from .common import (
    CUSTOM_TAGS,
    INIT_CONFIG,
    MAPREDUCE_JOB_COUNTER_METRIC_TAGS,
    MAPREDUCE_JOB_COUNTER_METRIC_VALUES_READ,
    MAPREDUCE_JOB_COUNTER_METRIC_VALUES_RECORDS,
    MAPREDUCE_JOB_COUNTER_METRIC_VALUES_WRITTEN,
    MAPREDUCE_JOB_METRIC_TAGS,
    MAPREDUCE_JOB_METRIC_VALUES,
    MAPREDUCE_MAP_TASK_METRIC_TAGS,
    MAPREDUCE_MAP_TASK_METRIC_VALUES,
    MAPREDUCE_REDUCE_TASK_METRIC_TAGS,
    MAPREDUCE_REDUCE_TASK_METRIC_VALUES,
    MR_AUTH_CONFIG,
    MR_CONFIG,
    RM_URI,
)


def test_check(aggregator, mocked_request):
    """
    Test that we get all the metrics we're supposed to get
    """
    instance = MR_CONFIG['instances'][0]

    # Instantiate the check
    mapreduce = MapReduceCheck('mapreduce', INIT_CONFIG, [instance])

    # Run the check once
    mapreduce.check(instance)

    # Check the MapReduce job metrics
    for metric, value in iteritems(MAPREDUCE_JOB_METRIC_VALUES):
        aggregator.assert_metric(metric, value=value, tags=MAPREDUCE_JOB_METRIC_TAGS + CUSTOM_TAGS, count=1)

    # Check the map task metrics
    for metric, value in iteritems(MAPREDUCE_MAP_TASK_METRIC_VALUES):
        aggregator.assert_metric(metric, value=value, tags=MAPREDUCE_MAP_TASK_METRIC_TAGS + CUSTOM_TAGS, count=1)

    # Check the reduce task metrics
    for metric, value in iteritems(MAPREDUCE_REDUCE_TASK_METRIC_VALUES):
        aggregator.assert_metric(metric, value=value, tags=MAPREDUCE_REDUCE_TASK_METRIC_TAGS + CUSTOM_TAGS, count=1)

    # Check the MapReduce job counter metrics
    for metric, attributes in iteritems(MAPREDUCE_JOB_COUNTER_METRIC_VALUES_READ):
        aggregator.assert_metric(
            metric,
            value=attributes["value"],
            tags=attributes["tags"] + MAPREDUCE_JOB_COUNTER_METRIC_TAGS + CUSTOM_TAGS,
            count=1,
        )

    # Check the MapReduce job counter metrics
    for metric, attributes in iteritems(MAPREDUCE_JOB_COUNTER_METRIC_VALUES_WRITTEN):
        aggregator.assert_metric(
            metric,
            value=attributes["value"],
            tags=attributes["tags"] + MAPREDUCE_JOB_COUNTER_METRIC_TAGS + CUSTOM_TAGS,
            count=1,
        )

    # Check the MapReduce job counter metrics
    for metric, attributes in iteritems(MAPREDUCE_JOB_COUNTER_METRIC_VALUES_RECORDS):
        aggregator.assert_metric(
            metric,
            value=attributes["value"],
            tags=attributes["tags"] + MAPREDUCE_JOB_COUNTER_METRIC_TAGS + CUSTOM_TAGS,
            count=1,
        )

    # Check the service tests
    service_check_tags = ["url:{}".format(RM_URI)] + CUSTOM_TAGS
    aggregator.assert_service_check(
        MapReduceCheck.YARN_SERVICE_CHECK, status=MapReduceCheck.OK, tags=service_check_tags, count=1
    )
    aggregator.assert_service_check(
        MapReduceCheck.MAPREDUCE_SERVICE_CHECK, status=MapReduceCheck.OK, tags=service_check_tags, count=1
    )

    aggregator.assert_all_metrics_covered()


def test_auth(aggregator, mocked_auth_request):
    """
    Test that we get all the metrics we're supposed to get
    """
    instance = MR_AUTH_CONFIG['instances'][0]

    # Instantiate the check
    mapreduce = MapReduceCheck('mapreduce', INIT_CONFIG, [instance])

    # Run the check once
    mapreduce.check(instance)

    # Check the service tests
    service_check_tags = ["url:{}".format(RM_URI)] + CUSTOM_TAGS
    aggregator.assert_service_check(
        MapReduceCheck.YARN_SERVICE_CHECK, status=MapReduceCheck.OK, tags=service_check_tags, count=1
    )
    aggregator.assert_service_check(
        MapReduceCheck.MAPREDUCE_SERVICE_CHECK, status=MapReduceCheck.OK, tags=service_check_tags, count=1
    )
