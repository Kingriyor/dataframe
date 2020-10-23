-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Oct 23, 2020 at 10:18 AM
-- Server version: 5.7.26
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dataframe`
--

-- --------------------------------------------------------

--
-- Table structure for table `theatre_movies`
--

CREATE TABLE `theatre_movies` (
  `id` int(11) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `genres` varchar(100) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `theatre` varchar(100) DEFAULT NULL,
  `release_year` int(11) DEFAULT NULL,
  `showtimes` varchar(1000) DEFAULT NULL,
  `tmsId` varchar(100) DEFAULT NULL,
  `rootId` varchar(100) DEFAULT NULL,
  `releaseDate` varchar(100) DEFAULT NULL,
  `titleLang` varchar(100) DEFAULT NULL,
  `longDescription` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `tv_movies`
--

CREATE TABLE `tv_movies` (
  `id` int(11) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `genres` varchar(100) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `channel` varchar(100) DEFAULT NULL,
  `release_year` int(11) DEFAULT NULL,
  `startTime` varchar(100) DEFAULT NULL,
  `endTime` varchar(100) DEFAULT NULL,
  `duration` varchar(100) DEFAULT NULL,
  `tmsId` varchar(100) DEFAULT NULL,
  `rootId` varchar(100) DEFAULT NULL,
  `releaseDate` varchar(100) DEFAULT NULL,
  `titleLang` varchar(100) DEFAULT NULL,
  `longDescription` varchar(500) DEFAULT NULL,
  `stationId` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `theatre_movies`
--
ALTER TABLE `theatre_movies`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tv_movies`
--
ALTER TABLE `tv_movies`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `theatre_movies`
--
ALTER TABLE `theatre_movies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tv_movies`
--
ALTER TABLE `tv_movies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
