-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 07, 2022 at 08:27 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vehicle_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `vehicle`
--

CREATE TABLE `vehicle` (
  `id` int(11) NOT NULL,
  `type` varchar(15) NOT NULL,
  `number_of_passengers` int(11) DEFAULT NULL,
  `ac` tinyint(1) DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  `in_job` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle`
--

INSERT INTO `vehicle` (`id`, `type`, `number_of_passengers`, `ac`, `size`, `in_job`) VALUES
(1, 'car', 3, 1, NULL, 0),
(2, 'car', 4, 1, NULL, 0),
(3, 'car', 3, 0, NULL, 0),
(4, 'car', 3, 0, NULL, 0),
(5, 'van', 6, 1, NULL, 0),
(6, 'van', 8, 0, NULL, 0),
(7, 'van', 8, 1, NULL, 0),
(8, '3weel', 3, 0, NULL, 1),
(9, '3weel', 3, 0, NULL, 0),
(10, '3weel', 3, 0, NULL, 0),
(11, 'truck', NULL, NULL, 7, 1),
(12, 'truck', NULL, NULL, 12, 0),
(13, 'truck', NULL, NULL, 7, 0),
(14, 'lorry', NULL, NULL, 3500, 1),
(15, 'car', 3, 1, NULL, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `vehicle`
--
ALTER TABLE `vehicle`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
