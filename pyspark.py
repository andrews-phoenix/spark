


spark.dynamicAllocation.enable                          True
spark.dynamicAllocation.minExecutors                    2
# Executor minimos que se levantan al iniciar
spark.dynamicAllocation.schedulerBacklogTimeout         1m
# Periodicamente checa backlog. Si no se ha terminado crea un nuevo executor
spark.dynamicAllocation.maxExecutors                    20
# Máximo número de executors
spark.dynamicAllocation.executorIdleTimeout             2min
# Si un executor termina una tarea y queda en espera: Se elimina el executor