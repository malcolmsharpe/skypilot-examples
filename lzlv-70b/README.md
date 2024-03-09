# Serve lizpreciatior/lzlv_70b_fp16_hf using SkyPilot

This example launches a single instance serving lizpreciatior/lzlv_70b_fp16_hf using vLLM. For security, the endpoint is exposed by SSH tunneling. Run `./launch.sh` to launch and `./down.sh` to tear down.

To test that it worked:
```
curl http://localhost:8940/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
      "model": "lizpreciatior/lzlv_70b_fp16_hf",
      "prompt": "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user'\''s questions.\n\nUSER: What is the capital of France?\nASSISTANT:"
  }'
```

## SillyTavern configuration

Text Completion endpoint settings:

- API: "Text Completion"
- API Type: "Aphrodite"
- API URL: "http://localhost:8940/"

## Notes

To avoid persisting input data remotely, vLLM is invoked with `--disable-log-requests`. For easier debugging, remove this argument.

A chat completions endpoint is not provided because the model doesn't include a chat template. The format recommended by the model card is Vicuna 1.1. For a Vicuna 1.1 template, see https://github.com/chujiezheng/chat_templates/blob/main/chat_templates/vicuna.jinja. Note that it includes bos_token, which should be removed since vLLM adds the bos_token itself.

These scripts were tested on MacOS with RunPod cloud.
