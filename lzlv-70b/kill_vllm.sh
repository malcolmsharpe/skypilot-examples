set -xeuo pipefail

sky exec skypilot "ps aux | grep 'python3 -u -m vllm.entrypoints.openai.api_server' | grep -v grep | awk '{print \$2}' | xargs kill"
