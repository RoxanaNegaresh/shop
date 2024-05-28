-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 24, 2024 at 09:18 AM
-- Server version: 8.3.0
-- PHP Version: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shop`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
CREATE TABLE IF NOT EXISTS `customers` (
  `user_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_persian_ci NOT NULL,
  `firstname` varchar(255) COLLATE utf8mb3_persian_ci DEFAULT NULL,
  `lastname` varchar(255) COLLATE utf8mb3_persian_ci DEFAULT NULL,
  `user_id` varchar(255) COLLATE utf8mb3_persian_ci DEFAULT NULL,
  `user_phonenumber` varchar(11) COLLATE utf8mb3_persian_ci DEFAULT NULL,
  `totalprice` float DEFAULT NULL,
  `discount` float DEFAULT NULL,
  `debt` float DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb3_persian_ci DEFAULT NULL,
  PRIMARY KEY (`user_name`),
  KEY `user_name` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`user_name`, `firstname`, `lastname`, `user_id`, `user_phonenumber`, `totalprice`, `discount`, `debt`, `password`) VALUES
('Its_Roxanax', 'Roxana', 'Negaresh', '0110960000', '09353157563', 3500000, 500000, 100000, 'Roxanax'),
('user', 'name', 'last', '0659', '8767', 7657.3, 3.4, 343.5, 'password');

-- --------------------------------------------------------

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
CREATE TABLE IF NOT EXISTS `goods` (
  `good_code` int NOT NULL,
  `good_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_persian_ci DEFAULT NULL,
  `good_company` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_persian_ci DEFAULT NULL,
  `good_production_date` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_persian_ci DEFAULT NULL,
  `good_expiration_date` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_persian_ci DEFAULT NULL,
  `good_Purchases` int DEFAULT NULL,
  `good_inventory` int DEFAULT NULL,
  `good_price` float DEFAULT NULL,
  PRIMARY KEY (`good_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;

--
-- Dumping data for table `goods`
--

INSERT INTO `goods` (`good_code`, `good_name`, `good_company`, `good_production_date`, `good_expiration_date`, `good_Purchases`, `good_inventory`, `good_price`) VALUES
(101, 'Milk', 'Kale', '5/22/2024', '6/22/2024', 100, 90, 100000);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
CREATE TABLE IF NOT EXISTS `orders` (
  `order_code` int NOT NULL,
  `user_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_persian_ci NOT NULL,
  `shop_code` int NOT NULL,
  `good_code` int NOT NULL,
  `order_date` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_persian_ci NOT NULL,
  `delivery_date` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_persian_ci NOT NULL,
  PRIMARY KEY (`order_code`),
  KEY `shop_code` (`shop_code`),
  KEY `good_code` (`good_code`),
  KEY `user_name` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_code`, `user_name`, `shop_code`, `good_code`, `order_date`, `delivery_date`) VALUES
(1001, 'Its_Roxanax', 10, 101, '5/22/2024', '5/22/2024');

-- --------------------------------------------------------

--
-- Table structure for table `shops`
--

DROP TABLE IF EXISTS `shops`;
CREATE TABLE IF NOT EXISTS `shops` (
  `shop_code` int NOT NULL,
  `shop_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_persian_ci NOT NULL,
  `undelivered` int NOT NULL,
  `price` float NOT NULL,
  PRIMARY KEY (`shop_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_persian_ci;

--
-- Dumping data for table `shops`
--

INSERT INTO `shops` (`shop_code`, `shop_name`, `undelivered`, `price`) VALUES
(10, 'Refah', 20, 30000000);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `good_code` FOREIGN KEY (`good_code`) REFERENCES `goods` (`good_code`),
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `customers` (`user_name`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `shop_code` FOREIGN KEY (`shop_code`) REFERENCES `shops` (`shop_code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
