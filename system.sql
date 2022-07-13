-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 13, 2022 at 06:32 PM
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
(1, 'dhruvikaneriya52@gmail.com', '953f09c44c61118452dfdc131a3a0f78'),
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
  `profile_updated_dt` date NOT NULL,
  `profile_photo` varchar(1000) COLLATE utf8mb4_unicode_ci NOT NULL,
  `certificate_of_dob` varchar(1000) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Update_Profile`
--

INSERT INTO `Update_Profile` (`id`, `user_id`, `first_name`, `last_name`, `mobile_number`, `date_of_birth`, `gender`, `address`, `city`, `state`, `zipcode`, `profile_updated_dt`, `profile_photo`, `certificate_of_dob`) VALUES
(4, 1, 'Dhruvi', 'Kaneriya', '9512738266', '2000-01-12', 'Female', '102,shrenath,manavadar', 'Manavadar', 'Gujarat', 362630, '2022-07-13', 'dhruvi_123.png', 'dhruvi_123.pdf'),
(5, 2, 'Kruti', 'Kaneriya', '9512738266', '2000-06-01', 'Female', '102,shrenath,manavadar', 'Manavadar', 'Gujarat', 362630, '2022-07-13', 'Krutii_98.png', 'Krutii_98.pdf'),
(6, 14, 'Charlotte Rivers', 'Tad Nelson', '7897968354', '1992-02-05', 'Female', 'Ea aut corrupti ear', 'Adipisicing voluptat', 'Gujarat', 369165, '2022-07-13', 'mupomuli.png', 'mupomuli.pdf'),
(7, 18, 'Zia Parker', 'Rahim Santana', '9576387895', '1985-08-19', 'Male', 'Ex aliqua Officia q', 'Eos est nisi a digni', 'Assam', 429384, '2022-07-13', 'raxofimapy.png', 'raxofimapy.pdf'),
(8, 23, 'Aidan Stanton', 'Sean Casey', '7896325411', '1995-01-16', 'Male', 'Voluptas autem sit ', 'Sunt consectetur in ', 'Chhattisgarh', 315498, '2022-07-13', 'nefatujov.png', 'nefatujov.pdf'),
(9, 24, 'Len Romero', 'Alma Rhodes', '7896325411', '1980-10-24', 'Female', 'Aliquam qui quia dui', 'Enim iusto id odio ', 'Andhra Pradesh', 70946, '2022-07-13', 'jaticepyta.png', 'jaticepyta.pdf'),
(10, 26, 'Angela Bass', 'Anne Gonzales', '8556598525', '1972-03-07', 'Male', 'Quis nostrud sapient', 'Veniam dolorum numq', 'Jharkhand', 72544, '2022-07-13', 'wyzygary.png', 'wyzygary.pdf');

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
(1, 'dhruvipatel.9212@gmail.com', 'dhruvi_123', '9e90db7e1a516eb7e4c83670a137bfcf'),
(2, 'Krutikanertiya9821@gmail.com', 'Krutii_98', '2db358b7fe6da88bcc038436563cd5e5'),
(4, '21bph051@niramauni.ca.in', 'krutikaneriya', '91ea373bdd7fb351017ec92f4f494dad'),
(6, 'brijjagani2828@gmail.com', 'Brij_jagani', 'ea5e9f9f58605906f6f7f715f2731747'),
(7, 'thankianjali49@gmail.com', 'Anjali1234', '346bb22cca1984ab73da02a0b8798f7c'),
(8, 'fadaducharmi@gmail.com', 'Charmi_Fadadu', '5a41329f4d6e919d40792cf5076b60a5'),
(9, 'savaniniraj@gmail.com', 'Neeraj204', 'cfffcb27b571a181a1ff30f23037d7c5'),
(11, 'shruti18102@gamil.com', 'shruti18102', '4e4e8c9a1ddacebabc131fdd77ced37d'),
(12, 'hspithiya9818@gmail.com', 'hardik12', '534760c59ad3704f36ffff3557927bce'),
(13, 'darshpatelvadadoriya@gmail.com', 'darshit_patel12', '00fa027f1ff4fdbbbec2239425ad0016'),
(14, 'gobu@mailinator.com', 'mupomuli', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(15, 'mycoza@mailinator.com', 'pylogeve', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(16, 'puduhig@mailinator.com', 'kufuqofajy', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(17, 'rysiw@mailinator.com', 'raxofimapy', '7096442c7647dc391199968facc99e4f'),
(18, 'tujagipiso@mailinator.com', 'raxofimapy', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(19, 'moro@mailinator.com', 'wudivusove', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(20, 'jazod@mailinator.com', 'kosicoqyw', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(21, 'fejoq@mailinator.com', 'vugidiny', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(22, 'cezonexeti@mailinator.com', 'wexuwuno', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(23, 'sozi@mailinator.com', 'nefatujov', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(24, 'zuzo@mailinator.com', 'jaticepyta', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(25, 'tigoqum@mailinator.com', 'xapofgkl', '832a2509f23176a49883753fe80ae885'),
(26, 'barapatoh@mailinator.com', 'wyzygary', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(27, 'sisagixumu@mailinator.com', 'zycogevu', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(28, 'sexy@mailinator.com', 'wibokadike', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(29, 'syritoj@mailinator.com', 'jodyfatyl', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(30, 'mibekec@mailinator.com', 'xadohesywu', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(31, 'tatebuzaj@mailinator.com', 'byvuboqi', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(32, 'piluraseve@mailinator.com', 'wawypyput', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(33, 'quqeci@mailinator.com', 'vewyqalot', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(34, 'myhatomume@mailinator.com', 'samudohak', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(35, 'zuxeporu@mailinator.com', 'domexugyhy', '8a03e9df7de5780b14d1dbb837b75957'),
(36, 'qyvu@mailinator.com', 'riqopypy', '5b63281e43af9878084b3d5766db852f'),
(37, 'cyxigoti@mailinator.com', 'wicezohe', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(38, 'qazybenak@mailinator.com', 'mutebugym', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(39, 'beqagel@mailinator.com', 'viwysiwu', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(40, 'palakpadalia19@gmail.com', 'wexuwuno', '6821fed87540c2e27a4c8a361deaf76f'),
(41, 'qymokemywa@mailinator.com', 'xofosahus', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(42, 'quwejeke@mailinator.com', 'qoxisole', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(43, 'coxazoxahi@mailinator.com', 'zadyzoxoju', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(44, 'kubaxucuk@mailinator.com', 'rataweji', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(45, 'lijosel@mailinator.com', 'gefixoze', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(46, 'koro@mailinator.com', 'wogukigede', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(47, 'gido@mailinator.com', 'qefowano', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(48, 'bykepewuw@mailinator.com', 'dexahiman', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(49, 'soderik@mailinator.com', 'tojonuva', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(50, 'xyrype@mailinator.com', 'byzisahum', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(51, 'wybebidiru@mailinator.com', 'sygyjohyd', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(54, 'godytux@mailinator.com', 'tizybibal', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(55, 'ragygyxej@mailinator.com', 'sumaxavih', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(56, 'byxuc@mailinator.com', 'nydycymuh', 'f3ed11bbdb94fd9ebdefbaf646ab94d3');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `User_login`
--
ALTER TABLE `User_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

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
