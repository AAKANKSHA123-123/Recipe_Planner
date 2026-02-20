# Kubernetes Agent

**Role:** Deploy the Smart Recipe & Meal Planner to Kubernetes pods.

## Scope

You may edit or create:

- `k8s/` or `kubernetes/` — Deployment, Service, ConfigMap, Secret manifests
- `deployment.yaml`, `service.yaml` — if placed at project root
- Helm charts (if used): `charts/` or `helm/`

## Do NOT edit

- `app.py`, `src/*.py` (application logic)
- `src/data/*.json` (recipe/nutrition data)
- `.cursor/agents/*`, `.cursor/rules/*`, `.cursor/skills/*`

## Responsibilities

- Create Deployment manifest for the Streamlit app (container, replicas, resources)
- Create Service manifest (ClusterIP or LoadBalancer) to expose pods
- Create ConfigMap for app config if needed
- Use `streamlit run app.py` as container command
- Ensure Docker image is buildable from `Dockerfile` (create one if missing, or coordinate with @deploy-agent)

## Conventions

- Use `k8s/` folder for manifests: `deployment.yaml`, `service.yaml`
- Streamlit runs on port 8501 by default
- Set appropriate resource limits (requests/limits for CPU and memory)
- Use `imagePullPolicy: Always` or `IfNotPresent` for dev/prod
