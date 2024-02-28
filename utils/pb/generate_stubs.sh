#!/bin/bash

proto_dir=$(dirname "$0")

for dir in "$proto_dir"/*; do
  if [ -d "$dir" ]; then
    python -m grpc_tools.protoc -I"$dir" --python_out="$dir" --pyi_out="$dir" --grpc_python_out="$dir" "$dir"/*.proto
  fi
done

