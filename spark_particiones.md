
Configurar el tamaño de partición
```
spark.sql.files.maxPartitioBytes
```

El tamaño predeterminado es minimo 128MB. Si lo disminutes podrías caer en el "small file problem". Demasiadas particiones más pequeñas introducen mayor actividad de I/O.


## Particiones shuffle

spark.sql.shuffle stage

defaul: 200
Created during the shuffle stage

Default

Falta min 22 
https://www.youtube.com/watch?v=R606AzrRYDY
