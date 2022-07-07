-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 30, 2022 at 06:43 PM
-- Server version: 10.6.7-MariaDB-2ubuntu1
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `system`
--

-- --------------------------------------------------------

--
-- Table structure for table `Admin_login`
--

CREATE TABLE `Admin_login` (
  `id` int(11) NOT NULL,
  `email` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Admin_login`
--

INSERT INTO `Admin_login` (`id`, `email`, `password`) VALUES
(1, 'dhruvikaneriya52@gmail.com', '21232f297a57a5a743894a0e4a801fc3'),
(2, 'palapadalia19@gmail.com', 'b17379c14cb29c6ce80dcf6b0621cb6b');

-- --------------------------------------------------------

--
-- Table structure for table `Update_Profile`
--

CREATE TABLE `Update_Profile` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `first_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mobile_number` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_of_birth` date NOT NULL,
  `gender` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `city` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `state` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `zipcode` int(7) NOT NULL,
  `profile_updated_dt` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Update_Profile`
--

INSERT INTO `Update_Profile` (`id`, `user_id`, `first_name`, `last_name`, `mobile_number`, `date_of_birth`, `gender`, `address`, `city`, `state`, `zipcode`, `profile_updated_dt`) VALUES
(1, 1, 'Darshit', 'Vadadoriya', '9904647022', '2001-03-03', 'Male', '102,shrenath,manavadar', 'manavadar', 'gujarat', 362630, '2022-06-30'),
(2, 3, 'Foram', 'patel', '09512738266', '2000-02-09', 'Female', '102,shrenath,manavadar', 'manavadar', 'gujarat', 362630, '2022-06-30');

-- --------------------------------------------------------

--
-- Table structure for table `User_login`
--

CREATE TABLE `User_login` (
  `id` int(11) NOT NULL,
  `email` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `User_login`
--

INSERT INTO `User_login` (`id`, `email`, `user_name`, `password`) VALUES
(1, 'darshitvadodariya12@gmail.com', 'darshit_12', '00fa027f1ff4fdbbbec2239425ad0016'),
(2, 'shrusti.shah@gmail.com', 'shrusti_shah123', '364893651056ea693060423e4b97d980'),
(3, 'foramshah27@gmail.com', 'foram_shah27', '41e7e7060351fb65a91562102c2b1b6b');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Admin_login`
--
ALTER TABLE `Admin_login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Update_Profile`
--
ALTER TABLE `Update_Profile`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `user_id_2` (`user_id`);

--
-- Indexes for table `User_login`
--
ALTER TABLE `User_login`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id` (`id`),
  ADD KEY `id_2` (`id`),
  ADD KEY `id_3` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Admin_login`
--
ALTER TABLE `Admin_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `Update_Profile`
--
ALTER TABLE `Update_Profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `User_login`
--
ALTER TABLE `User_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Update_Profile`
--
ALTER TABLE `Update_Profile`
  ADD CONSTRAINT `Update_Profile_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User_login` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
