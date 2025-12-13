import os
import yaml
import json
from logger import log_event

metadata_list = []
yaml_folder = 'yaml_files'

for filename in os.listdir(yaml_folder):
    if filename.endswith('.yaml') or filename.endswith('.yml'):
        file_path = os.path.join(yaml_folder, filename)
        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
            log_event("INFO", f"YAML file loaded successfully: {filename}")
        except Exception as e:
            log_event("ERROR", f"Failed to load YAML: {filename} - {e}", exception_code="YAML_LOAD_FAIL")
            continue

        try:
            api_metadata = {
                "title": data.get("info", {}).get("title"),
                "version": data.get("info", {}).get("version"),
                "description": data.get("info", {}).get("description"),
                "servers": data.get("servers", []),
                "tags": data.get("tags", []),
                "endpoints": []
            }
            paths = data.get("paths", {})
            for path, methods in paths.items():
                for method, details in methods.items():
                    endpoint_info = {
                        "path": path,
                        "method": method.upper(),
                        "request_schema": details.get("requestBody"),
                        "responses": details.get("responses"),
                        "authentication": data.get("components", {}).get("securitySchemes")
                    }
                    api_metadata["endpoints"].append(endpoint_info)
            metadata_list.append(api_metadata)
        except Exception as e:
            log_event("ERROR", f"Parsing failure for YAML: {filename} - {e}", exception_code="YAML_PARSE_FAIL")

with open("metadata.json", "w") as f:
    json.dump(metadata_list, f, indent=4)
log_event("INFO", "Metadata extraction completed")
summary = {
    "total_endpoints": 0,
    "http_methods": {},
    "auth_methods": set(),
    "endpoints_with_responses": 0,
    "endpoints_missing_responses": 0,
    "response_codes": set()
}

for api in metadata_list:
    summary["total_endpoints"] += len(api["endpoints"])
    for ep in api["endpoints"]:
        summary["http_methods"][ep["method"]] = summary["http_methods"].get(ep["method"],0)+1
        if ep["authentication"]:
            summary["auth_methods"].update(ep["authentication"].keys())
        if ep["responses"]:
            summary["endpoints_with_responses"] += 1
            summary["response_codes"].update(ep["responses"].keys())
        else:
            summary["endpoints_missing_responses"] += 1

summary["coverage_percent"] = round(
    (summary["endpoints_with_responses"]/summary["total_endpoints"])*100, 2
)
summary["auth_methods"] = list(summary["auth_methods"])
summary["response_codes"] = list(summary["response_codes"])

with open("summary.json","w") as f:
    json.dump(summary, f, indent=4)
log_event("INFO", "Aggregated summary generated")