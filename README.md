# Logging with the python standard library

## Using the basic config
* logging.BasicConfig

## The structure
* link to the documentation

### The logger
* Instantiate from logging.getLogger
* Use logging.getLogger(__name__) to retain module structure
* For example: log records from main/util/date.py will be *logged as __main__.util.date*
* Logging levels

### The handler
* Use close before removing the handler (need to clean up)
* attach handlers 
* if handler level is lower than logger level it will not emit
### The filter
* Can use anonymous functions
### the formatter
* Add rich.Handler
#
## My notebook logging setup for debuggintg

