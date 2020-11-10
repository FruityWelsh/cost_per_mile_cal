AVERAGE_LIFE = 150000
CURRENT_MILES = 30000
MILES_PER_MAINT = 7000
YEARLY_MILES = 15000
MAINTIANCE_COST = 200
OWNERSHIP_COST = 5544
GAS = True
MPG = 35
COST_PER_GALLON = 4

## BASIC INFO
miles_life =  AVERAGE_LIFE - CURRENT_MILES

## MAINTIANCE
maint_cost_per_mile = MAINTIANCE_COST / MILES_PER_MAINT  

## USAGE
if GAS:
    usage_cost_per_mile = COST_PER_GALLON / MPG

## Ownership
owenership_cost_per_mile = OWNERSHIP_COST / miles_life

## TOTAL
total_cost_per_mile = owenership_cost_per_mile + maint_cost_per_mile + usage_cost_per_mile
