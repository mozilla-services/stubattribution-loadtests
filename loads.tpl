#!/bin/bash
source loadtest.env && \
echo "Building loads.json" && \
cat > loads.json <<EOF
{
  "name": "Stub Attribution Server Testing",
  "plans": [

    {
      "name": "4 Servers",
      "description": "4 boxes",
      "steps": [
        {
          "name": "Stub Attribution: Test Cluster",
          "instance_count": 4,
          "instance_region": "us-east-1",
          "instance_type": "m3.medium",
          "run_max_time": 600,
          "container_name": "firefoxtesteng/stubattribution-loadtests:latest",
          "environment_data": [
            "URL_STUBATTRIBUTION_SERVER=https://stubattribution-default.stage.mozaws.net",
            "CONNECTIONS=100",
            "TEST_DURATION=600"
          ],
          "volume_mapping": "/var/log:/var/log/$RUN_ID:rw",
          "docker_series": "stubattribution-loadtests"
        }
      ]
    }
  ]
}
EOF
