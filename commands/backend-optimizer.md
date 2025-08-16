# Backend Performance Optimizer

Analyze the provided backend code and identify optimization opportunities across these core areas:

## 🗄️ Database Optimization
- **Query Performance**: Optimize N+1 queries, add proper indexing, use query analyzers
- **Connection Management**: Implement connection pooling, optimize timeout settings
- **Schema Design**: Normalize/denormalize appropriately, partition large tables
- **ORM Efficiency**: Review eager/lazy loading, optimize relation fetching

## ⚡ Code & Processing
- **Async Operations**: Convert blocking I/O to async/await patterns
- **Background Jobs**: Move heavy tasks to queues (Redis, Celery, Bull)
- **Memory Management**: Fix memory leaks, optimize data structures
- **Algorithm Efficiency**: Replace inefficient algorithms, reduce complexity

## 🔄 Caching Strategy
- **Application Cache**: Redis/Memcached for frequently accessed data
- **Database Cache**: Query result caching, prepared statement optimization
- **CDN Integration**: Cache static assets and API responses
- **Cache Invalidation**: Implement smart cache expiration policies

## 📡 API & Network
- **Pagination**: Implement cursor/offset pagination for large datasets
- **Rate Limiting**: Protect against abuse, implement backoff strategies
- **Response Optimization**: Compress responses, minimize payload size
- **Middleware**: Optimize request/response pipeline, remove unnecessary layers

## 🔧 Infrastructure & Monitoring
- **Load Balancing**: Distribute traffic effectively across instances
- **Auto-scaling**: Configure horizontal/vertical scaling triggers
- **Performance Metrics**: Add APM tools, database monitoring, custom metrics
- **Error Handling**: Implement circuit breakers, graceful degradation