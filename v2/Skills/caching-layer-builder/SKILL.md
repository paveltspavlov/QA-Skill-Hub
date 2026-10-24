---
name: caching-layer-builder
description: "Add or review a cache using explicit freshness, invalidation, and capacity requirements. Use for read-heavy endpoints or repeated expensive computation."
---

# Caching Layer Builder

## Procedure
1. Confirm authoritative data, key identity, access scope, acceptable staleness, traffic, and invalidation events.
2. Reuse the repository's cache pattern; document key format, TTL, serialization, and versioning.
3. Handle misses, errors, invalidation, stampedes, partial writes, and sensitive-data boundaries.
4. Measure hit rate, latency, memory, and source load before/after; do not claim savings without measurements.
5. Add tests for stale data, invalidation, concurrent misses, and cache outage/fallback.

## Output
A cache design/change with a freshness contract, metrics, and tests.

## References
- [Redis cache-aside](https://redis.io/docs/latest/develop/use-cases/cache-aside/nodejs)
