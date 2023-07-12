## Executor

El monto de memoria de un executor
```
spark.executor.memory
```
Está dividida en 
- Ejecución         60%
- Almacenamiento    40%
- Reservada

```
spark.executor.memory
```

## Execution memory:
Join, sort and agregation.
```
spark.memory.fraction(0.6 by default)
```
## Storage memory:
Caching user data structures and partitions dereived from DataFrames. Heavy I/I activity..


```
```