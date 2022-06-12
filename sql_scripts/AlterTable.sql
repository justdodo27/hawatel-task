ALTER TABLE `mydb`.`Product`
ADD `UnitPriceUSD` DECIMAL(12,2) NOT NULL
AFTER `UnitPrice`,
ADD `UnitPriceEuro` DECIMAL(12,2) NOT NULL
AFTER `UnitPrice`;