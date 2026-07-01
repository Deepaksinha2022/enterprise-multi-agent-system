import json

with open("audit.log", "r") as f:

    for line in f:

        log = json.loads(line)

        if log["trace_id"] == "bd5fb144-7b0a-40ea-8c7c-352eb1f7a42d":

            print(log)