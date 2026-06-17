# Configuración de Replicación MySQL

## Paso 1 (Principal)

Obtener el estado actual del servidor principal:

```sql
SHOW MASTER STATUS;
```

**Resultado:**

| File | Position |
|--------|----------|
| mysql-bin.000003 | 946 |

---

## Paso 2 (Secundario)

Detener la replicación:

```sql
STOP SLAVE;
```

Configurar el servidor principal como origen de replicación:

```sql
CHANGE MASTER TO
    MASTER_HOST='mysql_principal',
    MASTER_USER='root',
    MASTER_PASSWORD='root',
    MASTER_LOG_FILE='mysql-bin.000003',
    MASTER_LOG_POS=946;
```

Iniciar la replicación:

```sql
START SLAVE;
```

Verificar el estado:

```sql
SHOW SLAVE STATUS;
```

**Respuesta:**

```text
Queueing source event to the relay log
mysql_principal
root
3306
60
mysql-bin.000003
```

---

## Paso 3 (Secundario)

Obtener el estado actual del servidor secundario:

```sql
SHOW MASTER STATUS;
```

**Resultado:**

| File | Position |
|--------|----------|
| mysql-bin.000003 | 946 |

---

## Paso 4 (Principal)

Detener la replicación:

```sql
STOP SLAVE;
```

Configurar el servidor secundario como origen de replicación:

```sql
CHANGE MASTER TO
    MASTER_HOST='mysql_secundario',
    MASTER_USER='root',
    MASTER_PASSWORD='root',
    MASTER_LOG_FILE='mysql-bin.000003',
    MASTER_LOG_POS=946;
```

Iniciar la replicación:

```sql
START SLAVE;
```

Verificar el estado:

```sql
SHOW SLAVE STATUS;
```

**Respuesta:**

```text
Queueing source event to the relay log
mysql_principal
root
3306
60
mysql-bin.000003
```