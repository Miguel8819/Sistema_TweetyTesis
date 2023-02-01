-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-02-2023 a las 01:20:05
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `st`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cabecerafactura`
--

CREATE TABLE `cabecerafactura` (
  `nroFactura` int(100) NOT NULL,
  `fechaYhora` datetime(6) NOT NULL,
  `codCliente` int(100) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `motivoAnulacion` varchar(1000) NOT NULL,
  `codUsuario` int(11) NOT NULL,
  `anulo` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELACIONES PARA LA TABLA `cabecerafactura`:
--   `codUsuario`
--       `user` -> `codUsuario`
--   `codCliente`
--       `cliente` -> `codCliente`
--

--
-- Volcado de datos para la tabla `cabecerafactura`
--

INSERT INTO `cabecerafactura` (`nroFactura`, `fechaYhora`, `codCliente`, `activo`, `motivoAnulacion`, `codUsuario`, `anulo`) VALUES
(1, '2023-01-26 12:38:29.237042', 2, 1, 'aaaaqqq', 1, 0),
(2, '2023-01-26 14:58:46.714744', 3, 1, 'aaaaqqq', 1, 0),
(3, '2023-01-27 17:14:48.645793', 3, 1, 'aaaaqqq', 1, 0),
(4, '2023-01-31 17:41:41.655605', 5, 1, '', 1, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `codCliente` int(8) NOT NULL,
  `nroDni` varchar(10) NOT NULL,
  `nombreCliente` varchar(45) NOT NULL,
  `fechaAlta` varchar(45) NOT NULL,
  `calle` varchar(35) NOT NULL,
  `nroCalle` varchar(10) NOT NULL,
  `ciudad` varchar(45) NOT NULL,
  `codPostal` varchar(10) NOT NULL,
  `tel` varchar(20) NOT NULL,
  `email` varchar(45) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `fechaBaja` varchar(45) NOT NULL,
  `codUsuario` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELACIONES PARA LA TABLA `cliente`:
--   `codUsuario`
--       `user` -> `codUsuario`
--

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`codCliente`, `nroDni`, `nombreCliente`, `fechaAlta`, `calle`, `nroCalle`, `ciudad`, `codPostal`, `tel`, `email`, `activo`, `fechaBaja`, `codUsuario`) VALUES
(2, '11', 'Mario', '26/01/2023 16:02:00', 'Alem', '122', 'Alta Gracia', '1223', '3541', 'mm@gg', 0, '26/01/2023 16:16:45', 1),
(3, '22', 'Ramiro', '26/01/2023 16:03:13', 'Los Sauces', '765', 'Villa Carlos Paz', '5152', '3541676543', 'ramiro@gmail.com', 1, '26/01/2023 16:02:47', 2),
(5, '1', 'Mario', '31/01/2023 16:44:53', 'A', '1', 'Alta Gracia', '1', '1', '1', 1, '', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturacompra`
--

CREATE TABLE `facturacompra` (
  `codFactCompra` int(10) NOT NULL,
  `tipoDoc` varchar(40) NOT NULL,
  `nombreProv` varchar(40) NOT NULL,
  `nroFacturaCompra` varchar(20) NOT NULL,
  `nroCuil` int(12) NOT NULL,
  `fechaEmision` varchar(10) NOT NULL,
  `fechaIngreso` varchar(10) NOT NULL,
  `tipoCompra` varchar(20) NOT NULL,
  `subtotal` varchar(20) NOT NULL,
  `descuento` varchar(20) NOT NULL,
  `iva` varchar(20) NOT NULL,
  `importeTotal` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELACIONES PARA LA TABLA `facturacompra`:
--

--
-- Volcado de datos para la tabla `facturacompra`
--

INSERT INTO `facturacompra` (`codFactCompra`, `tipoDoc`, `nombreProv`, `nroFacturaCompra`, `nroCuil`, `fechaEmision`, `fechaIngreso`, `tipoCompra`, `subtotal`, `descuento`, `iva`, `importeTotal`) VALUES
(1, 'Factura de Compra', 'Ortellado Lucas', '1', 20, '1/1/2000', '27/01/2023', 'Cuenta Corriente', '400.0', '100', '84.0', '484.0'),
(2, 'Factura de Compra', 'Ortellado Lucas', '2', 20, '1/1/2000', '27/01/2023', 'Cuenta Corriente', '1000.', '20', '210.0', '1210.'),
(3, 'Factura de Compra', 'Ortellado Lucas', '4', 20, '1/1/2000', '27/01/2023', 'Cuenta Corriente', '300.0', '30.0', '63.0', '333.0'),
(5, 'Factura de Compra', 'Ortellado Lucas', '5', 20, '1/1/2000', '29/01/2023', 'Cuenta Corriente', '200.0', '0.0', '42.0', '242.0'),
(6, 'Factura de Compra', 'Ortellado Lucas', '6', 20, '1/1/2000', '29/01/2023', 'Cuenta Corriente', '200.0', '0.0', '42.0', '242.0'),
(7, 'Factura de Compra', 'Ortellado Lucas', '8', 20, '1/1/2000', '29/01/2023', 'Cuenta Corriente', '200.0', '0.0', '42.0', '242.0'),
(10, 'Factura de Compra', 'Ortellado Lucas', '3', 20, '1/1/2010', '29/01/2023', 'Cuenta Corriente', '2300.0', '0.0', '483.0', '2783.0'),
(11, 'Factura de Compra', 'Ortellado Lucas', '9', 20, '1/1/2000', '29/01/2023', 'Cuenta Corriente', '90.0', '0.0', '18.9', '108.9'),
(12, 'Factura de Compra', 'Ortellado Lucas', '10', 20, '1/1/2000', '29/01/2023', 'Contado', '180.0', '0.0', '37.8', '217.8'),
(13, 'Factura de Compra', 'Ortellado Lucas', '11', 20, '1/1/2000', '29/01/2023', 'Cuenta Corriente', '100.0', '0.0', '21.0', '121.0'),
(14, 'Factura de Compra', 'Ortellado Lucas', '12', 20, '1/1/2000', '29/01/2023', 'Cuenta Corriente', '1.0', '0.0', '0.21', '1.21'),
(15, 'Factura de Compra', 'Ortellado Lucas', '15', 20, '1/2/2023', '29/01/2023', 'Cuenta Corriente', '100.0', '0.0', '21.0', '121.0');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `product`
--

CREATE TABLE `product` (
  `codProducto` int(8) NOT NULL,
  `CodigoDeBarras` varchar(45) NOT NULL,
  `producto` varchar(45) NOT NULL,
  `categoria` varchar(45) NOT NULL,
  `subCategoria` varchar(45) NOT NULL,
  `marca` varchar(45) NOT NULL,
  `tipoUnidad` varchar(45) NOT NULL,
  `unidadDeMedida` varchar(45) NOT NULL,
  `stock` int(45) NOT NULL,
  `cant_min_stock` int(45) NOT NULL,
  `PuntoDePedido` int(45) NOT NULL,
  `CostoDeCompra` varchar(45) NOT NULL,
  `PrecioDeVenta` varchar(45) NOT NULL,
  `activo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELACIONES PARA LA TABLA `product`:
--

--
-- Volcado de datos para la tabla `product`
--

INSERT INTO `product` (`codProducto`, `CodigoDeBarras`, `producto`, `categoria`, `subCategoria`, `marca`, `tipoUnidad`, `unidadDeMedida`, `stock`, `cant_min_stock`, `PuntoDePedido`, `CostoDeCompra`, `PrecioDeVenta`, `activo`) VALUES
(1, '1', 'lapiz', 'Utiles', 'Lapices', 'Bic', 'Unidad', 'Unidad', 125, 20, 30, '100', '70', 1),
(2, '2', 'lapicera', 'Utiles', 'Lapiceras', 'Bic', 'Unidad', 'Unidad', 98, 20, 30, '100', '150', 1),
(3, '3', 'cuaderno A4', 'Utiles', 'Cuadernos', 'Laprida', 'Unidad', 'Unidad', 100, 10, 20, '300', '500', 1),
(4, '4', 'cartulina', 'Papeleria', 'Otro', 'Otro', 'Unidad', 'Unidad', 100, 50, 70, '70', '110', 1),
(5, '6', 'Cartuchera', 'Utiles', 'Otro', 'Otro', 'Unidad', 'Unidad', 0, 10, 15, '200', '500', 0),
(6, '7', 'pincel n°8', 'Utiles', 'Pinceles', 'Otro', 'Unidad', 'Unidad', 0, 10, 15, '300', '500', 1),
(7, '8', 'Voligoma 70mg', 'Utiles', 'Plasticola', 'Otro', 'Volumen', 'Miligramo', 0, 20, 30, '200', '250', 1),
(8, '9', 'cinta adhesiva ', 'Utiles', 'Cinta adhesiva', 'Trabi', 'Volumen', 'Miligramo', 0, 20, 30, '100', '150', 1),
(9, '10', 'Tempera 10mg', 'Utiles', 'Temperas', 'Otro', 'Volumen', 'Miligramo', 0, 50, 80, '30', '50', 1),
(10, '11', 'Repuesto hojas', 'Utiles', 'Repuestos hojas', 'Rivadavia', 'Unidad', 'Unidad', 0, 10, 20, '300', '450', 1),
(11, '12', 'Cuaderno A4 Inspira', 'Utiles', 'Cuadernos', 'Otro', 'Unidad', 'Unidad', 0, 10, 15, '600', '1100', 1),
(12, '13', 'Lapiz ', 'Utiles', 'Lapices', 'Faber Castell', 'Unidad', 'Unidad', 0, 30, 40, '50', '80', 1),
(13, '14', 'Fibras x 12', 'Utiles', 'Fibras', 'Faber Castell', 'Unidad', 'Unidad', 0, 10, 15, '300', '450', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productoxproveedor`
--

CREATE TABLE `productoxproveedor` (
  `codProducto` int(10) NOT NULL,
  `codProveedor` int(10) NOT NULL,
  `precio` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELACIONES PARA LA TABLA `productoxproveedor`:
--   `codProveedor`
--       `proveedor` -> `codProveedor`
--   `codProducto`
--       `product` -> `codProducto`
--

--
-- Volcado de datos para la tabla `productoxproveedor`
--

INSERT INTO `productoxproveedor` (`codProducto`, `codProveedor`, `precio`) VALUES
(1, 3, 300),
(2, 3, 600),
(3, 3, 1200),
(2, 2, 100),
(1, 2, 200),
(10, 2, 300),
(11, 2, 600),
(13, 2, 300);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE `proveedor` (
  `codProveedor` int(8) NOT NULL,
  `nroCuilCuit` varchar(12) NOT NULL,
  `nombreProveedor` varchar(45) NOT NULL,
  `nombreFactura` varchar(45) NOT NULL,
  `fechaAlta` varchar(20) NOT NULL,
  `calle` varchar(45) NOT NULL,
  `numeroCalle` varchar(45) NOT NULL,
  `ciudad` varchar(45) NOT NULL,
  `codPostal` varchar(45) NOT NULL,
  `celular` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `pagWeb` varchar(45) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `fechaBaja` varchar(20) NOT NULL,
  `codUsuario` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELACIONES PARA LA TABLA `proveedor`:
--   `codUsuario`
--       `user` -> `codUsuario`
--

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`codProveedor`, `nroCuilCuit`, `nombreProveedor`, `nombreFactura`, `fechaAlta`, `calle`, `numeroCalle`, `ciudad`, `codPostal`, `celular`, `email`, `pagWeb`, `activo`, `fechaBaja`, `codUsuario`) VALUES
(2, '20', 'Ortellado Lucas', 'Bicho', '27/01/2023 12:03:23', 'San Martin', '234', 'Villa Carlos Paz', '5152', '3541345788', 'lucas', 'www', 1, '27/01/2023 12:01:39', 3),
(3, '30', 'Dario Montoya', 'lukaku SRL', '27/01/2023 17:06:53', 'La Ferrere', '785', 'Capilla del Monte', '5198', '3517891001', 'mahag@gmail.co', 'www.kjagaf.com', 1, '', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tablafacturacompra`
--

CREATE TABLE `tablafacturacompra` (
  `nroFacturaCompra` varchar(20) NOT NULL,
  `codCuilProv` int(12) NOT NULL,
  `fechaIngreso` varchar(10) NOT NULL,
  `codProducto` int(8) NOT NULL,
  `codBarra` varchar(45) NOT NULL,
  `producto` varchar(45) NOT NULL,
  `cantidad` int(45) NOT NULL,
  `precioUnitario` varchar(45) NOT NULL,
  `subtotal` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELACIONES PARA LA TABLA `tablafacturacompra`:
--

--
-- Volcado de datos para la tabla `tablafacturacompra`
--

INSERT INTO `tablafacturacompra` (`nroFacturaCompra`, `codCuilProv`, `fechaIngreso`, `codProducto`, `codBarra`, `producto`, `cantidad`, `precioUnitario`, `subtotal`) VALUES
('1', 20, '27/01/2023', 1, '1', 'lapiz', 1, '200', '200.0'),
('1', 20, '27/01/2023', 2, '2', 'lapicera', 2, '100', '200.0'),
('2', 20, '27/01/2023', 1, '1', 'lapiz', 10, '100', '1000.0'),
('4', 20, '27/01/2023', 1, '1', 'lapiz', 1, '100', '100.0'),
('4', 20, '27/01/2023', 2, '2', 'lapicera', 2, '100', '200.0'),
('2', 20, '27/01/2023', 1, '1', 'lapiz', 1, '100', '100.0'),
('2', 20, '27/01/2023', 2, '2', 'lapicera', 10, '200', '2000.0'),
('2', 20, '27/01/2023', 4, '4', 'cartulina', 2, '300', '600.0'),
('5', 20, '29/01/2023', 1, '1', 'lapiz', 2, '100', '200.0'),
('6', 20, '29/01/2023', 1, '1', 'lapiz', 2, '100', '200.0'),
('8', 20, '29/01/2023', 1, '1', 'lapiz', 2, '100', '200.0'),
('3', 20, '29/01/2023', 1, '1', 'lapiz', 1, '200', '200.0'),
('3', 20, '29/01/2023', 1, '1', 'lapiz', 9, '80', '720.0'),
('3', 20, '29/01/2023', 1, '1', 'lapiz', 10, '230', '2300.0'),
('9', 20, '29/01/2023', 1, '1', 'lapiz', 1, '90', '90.0'),
('10', 20, '29/01/2023', 1, '1', 'lapiz', 2, '90', '180.0'),
('11', 20, '29/01/2023', 1, '1', 'lapiz', 1, '100', '100.0'),
('12', 20, '29/01/2023', 1, '1', 'lapiz', 1, '1', '1.0'),
('15', 20, '29/01/2023', 1, '1', 'lapiz', 1, '100', '100.0');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `codUsuario` int(8) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `rol` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELACIONES PARA LA TABLA `user`:
--

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`codUsuario`, `user_name`, `password`, `rol`) VALUES
(1, 'm', 'm', 'Administrador'),
(2, 'v', 'v', 'Encargado de ventas'),
(3, 'c', 'c', 'Encargado de compras'),
(4, 'd', 'd', 'Encargado de deposito');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `codVenta` int(10) NOT NULL,
  `codCabecera` int(10) NOT NULL,
  `codProducto` int(10) NOT NULL,
  `cantidad` varchar(100) NOT NULL,
  `precioUnitario` varchar(100) NOT NULL,
  `condPago` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELACIONES PARA LA TABLA `venta`:
--   `codCabecera`
--       `cabecerafactura` -> `nroFactura`
--   `codProducto`
--       `product` -> `codProducto`
--

--
-- Volcado de datos para la tabla `venta`
--

INSERT INTO `venta` (`codVenta`, `codCabecera`, `codProducto`, `cantidad`, `precioUnitario`, `condPago`) VALUES
(1, 1, 1, '1', '70', 'Efectivo'),
(2, 1, 2, '1', '150', 'Efectivo'),
(3, 1, 3, '1', '500', 'Efectivo'),
(4, 2, 3, '1', '500', 'Efectivo'),
(5, 2, 1, '2', '70', 'Efectivo'),
(6, 2, 2, '1', '150', 'Efectivo'),
(7, 3, 1, '2', '70', 'Efectivo'),
(8, 3, 2, '1', '150', 'Efectivo'),
(9, 4, 1, '1', '70', 'Efectivo'),
(10, 4, 2, '1', '150', 'Efectivo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cabecerafactura`
--
ALTER TABLE `cabecerafactura`
  ADD PRIMARY KEY (`nroFactura`),
  ADD KEY `codCliente` (`codCliente`,`codUsuario`),
  ADD KEY `codUsuario` (`codUsuario`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`codCliente`),
  ADD KEY `codUsuario` (`codUsuario`);

--
-- Indices de la tabla `facturacompra`
--
ALTER TABLE `facturacompra`
  ADD PRIMARY KEY (`codFactCompra`);

--
-- Indices de la tabla `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`codProducto`);

--
-- Indices de la tabla `productoxproveedor`
--
ALTER TABLE `productoxproveedor`
  ADD KEY `codProducto` (`codProducto`,`codProveedor`),
  ADD KEY `codProveedor` (`codProveedor`);

--
-- Indices de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`codProveedor`),
  ADD KEY `codUsuario` (`codUsuario`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`codUsuario`);

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`codVenta`),
  ADD KEY `codCabecera` (`codCabecera`,`codProducto`),
  ADD KEY `codProducto` (`codProducto`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cabecerafactura`
--
ALTER TABLE `cabecerafactura`
  MODIFY `nroFactura` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `codCliente` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `facturacompra`
--
ALTER TABLE `facturacompra`
  MODIFY `codFactCompra` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `product`
--
ALTER TABLE `product`
  MODIFY `codProducto` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  MODIFY `codProveedor` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `codUsuario` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `venta`
--
ALTER TABLE `venta`
  MODIFY `codVenta` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cabecerafactura`
--
ALTER TABLE `cabecerafactura`
  ADD CONSTRAINT `cabecerafactura_ibfk_1` FOREIGN KEY (`codUsuario`) REFERENCES `user` (`codUsuario`) ON UPDATE CASCADE,
  ADD CONSTRAINT `cabecerafactura_ibfk_2` FOREIGN KEY (`codCliente`) REFERENCES `cliente` (`codCliente`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `cliente_ibfk_1` FOREIGN KEY (`codUsuario`) REFERENCES `user` (`codUsuario`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `productoxproveedor`
--
ALTER TABLE `productoxproveedor`
  ADD CONSTRAINT `productoxproveedor_ibfk_3` FOREIGN KEY (`codProveedor`) REFERENCES `proveedor` (`codProveedor`),
  ADD CONSTRAINT `productoxproveedor_ibfk_4` FOREIGN KEY (`codProducto`) REFERENCES `product` (`codProducto`);

--
-- Filtros para la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD CONSTRAINT `proveedor_ibfk_1` FOREIGN KEY (`codUsuario`) REFERENCES `user` (`codUsuario`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `venta`
--
ALTER TABLE `venta`
  ADD CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`codCabecera`) REFERENCES `cabecerafactura` (`nroFactura`) ON UPDATE CASCADE,
  ADD CONSTRAINT `venta_ibfk_2` FOREIGN KEY (`codProducto`) REFERENCES `product` (`codProducto`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
