# ADR Monitor API

## Health

GET /api/healthz

## Drugs

GET /api/drugs

GET /api/drugs/{id}

GET /api/drugs/{id}/risk-score

GET /api/drugs/{id}/interactions

## Reactions

GET /api/reactions

POST /api/reactions

PATCH /api/reactions/{id}

DELETE /api/reactions/{id}

## Alerts

GET /api/alerts

POST /api/alerts

PATCH /api/alerts/{id}

DELETE /api/alerts/{id}

## Reports

GET /api/reports

POST /api/reports

PATCH /api/reports/{id}

## Agent

POST /api/agent/query
