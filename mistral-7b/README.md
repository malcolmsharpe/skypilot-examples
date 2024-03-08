# Serve Mistral-7B-Instruct-v0.2 using SkyPilot

This example launches a single instance serving Mistral-7B-Instruct-v0.2 using vLLM. For security, the endpoint is exposed by SSH tunneling. Run `./launch.sh` to launch and `./down.sh` to tear down.

To test that it worked:
```
curl http://localhost:8940/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
            "model": "mistralai/Mistral-7B-Instruct-v0.2",
            "messages": [
                {
                    "role": "user",
                    "content": "What is the capital of France?"
                }
            ]
        }'
```

## SillyTavern configuration

To use as a backend for SillyTavern, there are two options.

Chat Completion endpoint settings:

- API: "Chat Completion"
- Chat Completion Source: "Custom (OpenAI-compatible)"
- Custom Endpoint (Base URL): "http://localhost:8940/v1"
- Enter a Model ID: "mistralai/Mistral-7B-Instruct-v0.2"

Text Completion endpoint settings:

- API: "Text Completion"
- API Type: "Aphrodite"
- API URL: "http://localhost:8940/"

For Text Completion, the included Instruct Mode preset "Mistral" is missing the EOS token `</s>`. Put it in the "Separator" text box.

## Notes

The official Mistral-7B-Instruct-v0.2 chat template does not accept a system message, so the workdir contains a generalized chat template that concatenates the system message with the first user message.

To avoid persisting input data remotely, vLLM is invoked with `--disable-log-requests`. For easier debugging, remove this argument.

These scripts were tested on MacOS with RunPod cloud.
