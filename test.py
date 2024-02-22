#!/usr/bin/python3

import argparse
import glob
import pathlib
import os
import shutil
import subprocess
import sys

tiny_tests = [
        "test10", 
        "test20", 
        "test21",
        "test22",
        "test23",
        "test24",
        "test25",
        "test26",
        "test27"
]
def nolog(working_directory):
    for path in ["test_result.log", "test.log", "messages", "starttime"]:
        try:
            os.remove(os.path.join(working_directory, path))
        except:
            pass

def report(working_directory):
    test_log = os.path.join(working_directory, "test.log")
    result_log = os.path.join(working_directory, "test_result.log")

    if os.path.exists(test_log):
        shutil.copyfile(test_log, result_log)
    else:
        with open(result_log, "a") as log:
            log.write("No failures reported\n")

    run_result = subprocess.run(
            [vim_name, "-u", "NONE", "--noplugin", "--not-a-term",
             "-S", "summarize.vim", "messages"], cwd=working_directory)

    try:
        os.remove(working_directory, "starttime")
    except:
        pass

    print("\nTest results:\n")
    with open(result_log, "r") as f:
        shutil.copyfileobj(f, sys.stdout)

    if os.path.exists(test_log):
        print("TEST FAILURE\n")
        exit(1)
    else:
        print("ALL DONE\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--vim-name", default="base/src/vim")
    parser.add_argument("--working-directory", default="base/src/testdir")

    args = parser.parse_args()

    vim_name = os.path.abspath(args.vim_name)
    working_directory = os.path.abspath(args.working_directory)
    print(f"Using vim: '{vim_name}'")
    print(f"Using working directory: '{working_directory}'")

    nolog(working_directory)

    for test in tiny_tests:
        run_result = subprocess.run(
                [vim_name, "-u", "unix.vim",
                 "-U", "NONE", "--noplugin",  "--not-a-term",
                 "-s", "dotest.in",
                 "{}.in".format(test)], cwd=working_directory)

        if run_result.returncode != 0:
            print(f"{test} exited with code: {run_result.returncode}")

        output_file = os.path.join(working_directory, "test.out")
        log_file = os.path.join(working_directory, "test.log")

        if os.path.exists(output_file):
            diff_result = subprocess.run(
                    ["diff", "test.out", f"{test}.ok"], cwd=working_directory)

            if diff_result.returncode > 0:
                with open(log_file, "a") as log:
                    log.write(f"{test} FAILED\n")
                os.rename(output_file, os.path.join(working_directory, f"{test}.failed"))
            else:
                os.rename(output_file, os.path.join(working_directory, f"{test}.ok"))

        else:
            with open(log_file, "a") as log:
                log.write(f"{test} NO OUTPUT\n")

        for path in glob.glob(os.path.join(working_directory, "X*")):
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)

        try:
            os.remove(os.path.join(working_directory, "viminfo"))
        except:
            pass

    report(working_directory)

