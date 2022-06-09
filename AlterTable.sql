ALTER TABLE `mydb`.`Product`
ADD `UnitPriceUSD` DECIMAL NOT NULL
AFTER `UnitPrice`,
ADD `UnitPriceEuro` DECIMAL NOT NULL
AFTER `UnitPrice`;