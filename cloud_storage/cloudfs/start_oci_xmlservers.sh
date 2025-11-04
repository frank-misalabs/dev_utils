#!/bin/bash
taskset -c 0 python load_test_oci_server.py 8881 &
taskset -c 1 python load_test_oci_server.py 8882 &
taskset -c 2 python load_test_oci_server.py 8883 &
taskset -c 3 python load_test_oci_server.py 8884 &
taskset -c 4 python load_test_oci_server.py 8885 &
taskset -c 5 python load_test_oci_server.py 8886 &
taskset -c 6 python load_test_oci_server.py 8887 &
taskset -c 7 python load_test_oci_server.py 8888 &
taskset -c 8 python load_test_oci_server.py 8889 &
taskset -c 9 python load_test_oci_server.py 8890 &
taskset -c 10 python load_test_oci_server.py 8891 &
taskset -c 11 python load_test_oci_server.py 8892 &
taskset -c 12 python load_test_oci_server.py 8893 &
taskset -c 13 python load_test_oci_server.py 8894 &
taskset -c 14 python load_test_oci_server.py 8895 &
taskset -c 15 python load_test_oci_server.py 8896 &
