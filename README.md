# api-worker

## sample 

```
curl -X POST "http://localhost:8000/tasks?seconds=50
{"task_id":"26067a03-2f9c-49bf-b01a-2a6c5db3a951","status":"queued"}

curl http://localhost:8000/tasks/26067a03-2f9c-49bf-b01a-2a6c5db3a951
{"task_id":"26067a03-2f9c-49bf-b01a-2a6c5db3a951","state":"PROGRESS","progress":{"current":11,"total":50}}

```
