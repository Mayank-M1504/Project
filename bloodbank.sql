-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 13, 2024 at 07:41 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bloodbank`
--

-- --------------------------------------------------------

--
-- Table structure for table `blood`
--

CREATE TABLE `blood` (
  `id` int(11) NOT NULL,
  `type` varchar(15) NOT NULL,
  `qty` int(11) NOT NULL,
  `doctorid` int(11) NOT NULL,
  `disease` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `blood`
--

INSERT INTO `blood` (`id`, `type`, `qty`, `doctorid`, `disease`) VALUES
(14, 'A+', 0, 1234, 'Covid'),
(15, 'A', 1, 1111, 'Cancer'),
(16, 'B', 1, 2222, ''),
(17, 'AB', 2, 4444, 'Diabetes ');

-- --------------------------------------------------------

--
-- Table structure for table `custfeed`
--

CREATE TABLE `custfeed` (
  `id` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `feedback` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `custfeed`
--

INSERT INTO `custfeed` (`id`, `email`, `feedback`) VALUES
(0, 'mayankmjain16@gmail.com', 'bgdfgdfgfdgdgv');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `password`) VALUES
(777, 'sdr ', 'mayankmjain16@gmail.com', 'scrypt:32768:8:1$jFsH82tjLlhvF2Pk$d8c3105e34bbdf9bcefd4cea7b6ddc7ba7b846094d4258e0548b0a597ef0be5b0c51f54acdfe9c26e3c93c15b1a407175daa13700ed090c592e7d8709a4426b0'),
(1111, 'abcd', 'devimukesh2604@gmail.com', 'scrypt:32768:8:1$8yGN2xc9iy71oUov$6a7462648f903eaae0705a558513e80e080c5f3e22f64d74b0bcc51081500aaba1dbe7f366e35e6d73bbfedf6b4b158325f07e704cedf38e1fffc826eff025cb'),
(1234, 'sparsh', 'sparshjain189@gmail.com', 'scrypt:32768:8:1$fI3uZHzKkG36sTeB$8e26665ea7434af5a9ca08954603364138cc64b34f302d099234eab0341d0a45291ef0e5173ceb23626b094383b1637da7f648da66b103b6531b013d6c0fa209'),
(123456, 'adnan', 'adnan123@gmail.com', 'scrypt:32768:8:1$N3ThQEltz1OWVMbJ$d071f07a426b6d95e7a62b34898d0f68b7fa1ff8aaebcfffd7a5a1e39d1ba72ee5c2dbe8b99ad67480bc03cf4110dcd1a97bc57a4ad2656f6c0b40527c02ff52');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blood`
--
ALTER TABLE `blood`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `custfeed`
--
ALTER TABLE `custfeed`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blood`
--
ALTER TABLE `blood`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
