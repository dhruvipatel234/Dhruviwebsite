-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 19, 2022 at 04:58 PM
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
(1, 1, 'Michael Brooks', 'Inez Brock', '9632587410', '1955-03-15', 'female', 'Sed consequat Elige', 'At non ea sapiente u', 'Jharkhand', 850912, '2022-07-19', 'qidunibedg12.png', 'qidunibedg12.pdf'),
(2, 2, 'Zephr Bray', 'Fulton Meyers', '8963251047', '2001-03-13', 'Male', 'Et cupidatat rerum n', 'Id id dolor dolorum', 'Tamil Nadu', 246301, '2022-07-19', 'kazimynivfg.png', 'kazimynivfg.pdf'),
(3, 3, 'Palmer Henry', 'Bevis Henry', '7896325410', '1972-03-27', 'Female', 'In accusantium et hi', 'Libero do aperiam of', 'Jharkhand', 78817, '2022-07-19', 'vuberiqed12.png', 'vuberiqed12.pdf');

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
(1, 'vupanyvume@mailinator.com', 'fydejexoqy', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(2, 'bubu@mailinator.com', 'xylasaquso', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(3, 'mewex@mailinator.com', 'vuberiqed12', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(4, 'deqopo@mailinator.com', 'vepipoly', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(5, 'jolasep12@mailinator.com', 'cihokerei12', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(6, 'symaf@mailinator.com', 'moqohugum', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(7, 'cyzomuvyxi@mailinator.com', 'gubikyre', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(8, 'sepiqi@mailinator.com', 'pomisygip', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(9, 'kagiqa@mailinator.com', 'cyfyvugii', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(10, 'qabe@mailinator.com', 'wodihakos', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(11, 'cogapike@mailinator.com', 'pekigiwe', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(12, 'huvyta@mailinator.com', 'bowifofio', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(13, 'majyf@mailinator.com', 'pykanahe', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(14, 'rokowosoju12@mailinator.com', 'palak_patel19', '832a2509f23176a49883753fe80ae885'),
(15, 'tywybaf12@mailinator.com', 'gekydoba', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(16, 'fojipyd@mailinator.com', 'laqinutui', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(17, 'sohevaza@mailinator.com', 'viqijulah4', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(18, 'kifeta@mailinator.com', 'vehasunel', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(19, 'palijoca@mailinator.com', 'likyvocade4', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(20, 'ranuwy@mailinator.com', 'gemeqaper', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(21, 'sutyti@mailinator.com', 'hacelejojoi', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(22, 'gugexamy@mailinator.com', 'zetemapyu', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(23, 'delyfimape@mailinator.com', 'labicutacuo', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(24, 'fynyhi@mailinator.com', 'mocyzazin', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(25, 'papiraby@mailinator.com', 'fedukogui', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(26, 'mase@mailinator.com', 'sugiguku', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(27, 'cikawo@mailinator.com', 'tibiqujock', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(28, 'zyvimig@mailinator.com', 'puzehyvizi', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(29, 'jihow@mailinator.com', 'mihavowanl', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(30, 'fikoly@mailinator.com', 'nunyhubepil', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(31, 'gykeqi@mailinator.com', 'tarydetomo1', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(32, 'nupytohu@mailinator.com', 'tesilugew', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(33, 'kufojy@mailinator.com', 'gipybopie', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(34, 'dekom@mailinator.com', 'quwydykut', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(35, 'kohewo@mailinator.com', 'nukudaket', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(36, 'visafitaxa@mailinator.com', 'pujanyjig', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(37, 'gubapugoc@mailinator.com', 'bamujyzif', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(38, 'talelu@mailinator.com', 'tuvamidif', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(39, 'qipygaqevo@mailinator.com', 'wybutypomof', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(40, 'hyjahu@mailinator.com', 'muhopyrohd', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(41, 'disove@mailinator.com', 'jafuqimef', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(42, 'vivegagyh@mailinator.com', 'rykoxudif', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(43, 'bapix@mailinator.com', 'zisozemihy', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(44, 'zonine@mailinator.com', 'migaxykif', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(45, 'geqofumew@mailinator.com', 'huvanisog', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(46, 'xojy@mailinator.com', 'fawimarir', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(47, 'wezorywyw@mailinator.com', 'dunonara', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(48, 'kababer@mailinator.com', 'luqewerio', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(49, 'boxuj@mailinator.com', 'qyhokohi', 'f3ed11bbdb94fd9ebdefbaf646ab94d3'),
(50, 'bypevymuha@mailinator.com', 'ritukofas', 'f3ed11bbdb94fd9ebdefbaf646ab94d3');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `User_login`
--
ALTER TABLE `User_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

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
