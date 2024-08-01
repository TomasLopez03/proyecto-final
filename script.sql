create database negocio;
use negocio;

CREATE TABLE `negocio`.`categorias` (
  `idcat` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idcat`));

CREATE TABLE `negocio`.`productos` (
  `idprod` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `tamaño` VARCHAR(10) NOT NULL,
  `idcat` INT NOT NULL,
  `stock` INT NOT NULL,
  `precio` FLOAT NOT NULL,
  PRIMARY KEY (`idprod`),
  INDEX `idcat_idx` (`idcat` ASC),
  CONSTRAINT `idcat`
    FOREIGN KEY (`idcat`)
    REFERENCES `negocio`.`categorias` (`idcat`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `negocio`.`ventas` (
  `idventas` INT NOT NULL AUTO_INCREMENT,
  `idprodu` INT NOT NULL,
  `cantidad` INT NOT NULL,
  `precio` FLOAT NOT NULL,
  `fecha` DATE NOT NULL,
  PRIMARY KEY (`idventas`),
  INDEX `idprod_idx` (`idprodu` ASC),
  CONSTRAINT `idprodu`
    FOREIGN KEY (`idprodu`)
    REFERENCES `negocio`.`productos` (`idprod`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

insert into categorias(nombre)values
("bebidas sin alcohol"),
("bebidas con alcohol"),
("productos de limpieza"),
("higiene personal"),
("congelados"),
("bebes y niños"),
("snacks"),
("alimentos");

insert into productos(nombre,tamaño,idcat,stock,precio)values
("gaseosa","1l",1,50,1000),
("gaseosa","2.25l",1,50,1400),
("gaseosa","2.50l",1,50,1600),
("gaseosa","3l",1,50,2000),
("agua","750ml",1,50,850),
("agua","1l",1,50,1000),
("agua","2l",1,50,1200),
("agua","2.25l",1,50,1400),
("soda","1l",1,50,1000),
("soda","1.50l",1,50,1150),
("vino","750ml",2,50,3000),
("vino","1l",2,50,3800),
("cerveza","1l",2,50,2000),
("fernet","450ml",2,50,5200),
("fernet","750ml",2,50,7200),
("fernet","1l",2,50,9200),
("vodka","750ml",2,50,8200),
("champu","750cm3",4,50,3200),
("acondicionador","750cm3",4,50,4200),
("crema de afeitar","500cm3",4,50,2500),
("helado","1/4kg",5,50,1500),
("helado","1/2kg",5,50,2500),
("helado","1kg",5,50,4500),
("mani","75g",7,50,1500),
("mani","100g",7,50,2200),
("nachos","129g",7,50,4000),
("nachos","200g",7,50,5200),
("papas fritas","65g",7,50,2500),
("papas fritas","100g",7,50,4500),
("papas fritas","200g",7,50,8500);

select * from ventas a inner join productos b on a.idprodu = b.idprod
where nombre = '' and fecha like '2024-07%';

select a.idventas, b.nombre as producto, b.tamaño, a.precio, fecha from ventas a 
inner join productos b on a.idprodu = b.idprod  where fecha like '2024-07-%' order by fecha desc;

select idprodu from ventas where fecha like '2024-07%';

select b.nombre as marca, c.nombre as producto, d.nombre as categoria,c.tamaño,c.stock,c.precio from prod_marca a 
inner join marcas b on a.idmarca = b.idmarca
inner join productos c on a.idprod = c.idprod
inner join categorias d on c.idcat= d.idcat;

select distinct nombre from productos;


set foreign_key_checks=1;
