set -xeuo pipefail

sky launch -d -c skypilot serve.yaml
ssh -N -f -L 8940:localhost:8000 skypilot
sky logs skypilot
