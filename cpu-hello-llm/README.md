# CPU Hello LLM (Frontend + Backend) — Works Locally on Docker Desktop Kubernetes

This is a minimal, fully CPU-only demo you can deploy in one shot.

## Prereqs
- Docker Desktop with **Kubernetes enabled** (context: docker-desktop)
- Helm, kubectl installed

## Build local images
```bash
# from repo root
docker build -t hello-backend ./backend
docker build -t hello-frontend ./frontend
```

## Deploy with Helm
```bash
cd helm-chart
helm install cpu-hello .
kubectl get pods
```

## Access
Option A — Port-forward (simplest):
```bash
kubectl port-forward svc/cpu-hello-frontend 8080:80
```
Then open http://localhost:8080

Option B — Ingress (optional):
```bash
# enable ingress in Docker Desktop: Settings > Kubernetes > enable (or use ingress-nginx add-on)
kubectl apply -f templates/ingress.yaml
# add to /etc/hosts:
# 127.0.0.1 hello.local
# then open http://hello.local
```

## Test backend directly
```bash
kubectl port-forward svc/cpu-hello-backend 8000:8000
curl -s http://localhost:8000/health
curl -s -X POST http://localhost:8000/chat -H 'Content-Type: application/json' -d '{"prompt":"hello"}'
```

## Replace with your real code later
- Swap `backend/` with your app and rebuild `hello-backend` image.
- Swap `frontend/` and rebuild `hello-frontend` image.
- Helm chart already points at those local images; adjust `values.yaml` if you rename.
