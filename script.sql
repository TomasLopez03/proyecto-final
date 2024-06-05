create database negocio;

use negocio;

CREATE TABLE `negocio`.`productos` (
  `id_productos` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `stock` INT NOT NULL,
  `precio` FLOAT NOT NULL,
  PRIMARY KEY (`id_productos`),
  UNIQUE INDEX `id_productos_UNIQUE` (`id_productos` ASC));

CREATE TABLE `negocio`.`ventas` (
  `id_ventas` INT NOT NULL AUTO_INCREMENT,
  `id_productos` INT NOT NULL,
  `cantidad` INT NOT NULL,
  `precio` FLOAT NOT NULL,
  PRIMARY KEY (`id_ventas`),
  UNIQUE INDEX `id_ventas_UNIQUE` (`id_ventas` ASC),
  INDEX `id_productos_idx` (`id_productos` ASC),
  CONSTRAINT `id_productos`
    FOREIGN KEY (`id_productos`)
    REFERENCES `negocio`.`productos` (`id_productos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);























