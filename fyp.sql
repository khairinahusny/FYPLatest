-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2019 at 03:56 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fyp`
--

-- --------------------------------------------------------

--
-- Table structure for table `attempt`
--

CREATE TABLE `attempt` (
  `id` int(11) NOT NULL,
  `attempt` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attempt`
--

INSERT INTO `attempt` (`id`, `attempt`) VALUES
(1, 1),
(2, 2),
(3, 3);

-- --------------------------------------------------------

--
-- Table structure for table `defuz_req`
--

CREATE TABLE `defuz_req` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `mode_id` int(11) NOT NULL,
  `avg_duration` int(11) NOT NULL,
  `avg_score` int(11) NOT NULL,
  `defuzz_value` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `digit_span`
--

CREATE TABLE `digit_span` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `mode_id` int(11) NOT NULL,
  `duration` float NOT NULL,
  `score` float NOT NULL,
  `digit_category` int(11) NOT NULL,
  `attempt` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `digit_span`
--

INSERT INTO `digit_span` (`id`, `username`, `mode_id`, `duration`, `score`, `digit_category`, `attempt`) VALUES
(1, 'player1', 1, 10, 100, 4, 1),
(2, 'player1', 1, 13, 100, 5, 1),
(3, 'player1', 1, 20, 100, 6, 1),
(4, 'player1', 1, 34, 60, 7, 1),
(5, 'player1', 1, 27, 90, 6, 2),
(6, 'player1', 1, 18, 100, 5, 3),
(7, 'player1', 1, 25, 85, 6, 3),
(8, 'player2', 1, 20, 100, 4, 1),
(9, 'player2', 1, 26, 85, 5, 1),
(10, 'player2', 1, 18, 100, 4, 2),
(11, 'player2', 1, 19, 100, 5, 2),
(12, 'player2', 1, 21, 80, 6, 2),
(13, 'player2', 1, 17, 100, 5, 3),
(14, 'player2', 1, 19, 78, 6, 3),
(15, 'player3', 1, 15, 100, 4, 1),
(16, 'player3', 1, 16, 100, 5, 1),
(17, 'player3', 1, 18, 85, 6, 1),
(18, 'player3', 1, 17, 100, 5, 2),
(19, 'player3', 1, 19, 80, 6, 2),
(20, 'player4', 1, 18, 100, 4, 1),
(21, 'player4', 1, 15, 100, 5, 1),
(22, 'player4', 1, 15, 100, 6, 1),
(23, 'player4', 1, 16, 100, 7, 1),
(24, 'player4', 1, 18, 50, 8, 1),
(25, 'player4', 1, 20, 85, 7, 2),
(26, 'player4', 1, 19, 100, 6, 3),
(27, 'player4', 1, 18, 88, 7, 3),
(28, 'player5', 1, 8, 100, 4, 1),
(29, 'player5', 1, 9, 80, 5, 1),
(30, 'player5', 1, 9, 100, 4, 2),
(31, 'player5', 1, 10, 100, 5, 2),
(32, 'player5', 1, 10, 90, 6, 2),
(33, 'player5', 1, 11, 97, 5, 3),
(34, 'player6', 1, 11, 100, 4, 1),
(35, 'player6', 1, 10, 100, 5, 1),
(36, 'player6', 1, 13, 73, 6, 1),
(37, 'player6', 1, 12, 100, 5, 2),
(38, 'player6', 1, 14, 80, 6, 2),
(39, 'player6', 1, 10, 90, 5, 3),
(40, 'player7', 1, 8, 100, 4, 1),
(41, 'player7', 1, 9, 100, 5, 1),
(42, 'player7', 1, 8, 100, 6, 1),
(43, 'player7', 1, 10, 95, 7, 1),
(44, 'player7', 1, 8, 100, 6, 2),
(45, 'player7', 1, 10, 85, 7, 2),
(46, 'player7', 1, 10, 85, 6, 3),
(47, 'player8', 1, 13, 100, 4, 1),
(48, 'player8', 1, 14, 70, 5, 1),
(49, 'player8', 1, 14, 100, 4, 2),
(50, 'player8', 1, 12, 75, 5, 2),
(51, 'player8', 1, 13, 100, 4, 3),
(52, 'player8', 1, 12, 80, 5, 3),
(53, 'player9', 1, 20, 100, 4, 1),
(54, 'player9', 1, 19, 80, 5, 1),
(55, 'player10', 1, 17, 100, 4, 1),
(56, 'player10', 1, 18, 100, 5, 1),
(57, 'player10', 1, 19, 100, 6, 1),
(58, 'player10', 1, 20, 100, 7, 1),
(59, 'player10', 1, 21, 90, 8, 1),
(60, 'player10', 1, 20, 90, 7, 2),
(62, 'player1', 2, 19, 100, 4, 1),
(63, 'player1', 2, 23, 100, 0, 1),
(64, 'player1', 2, 24, 90, 5, 2),
(65, 'player1', 2, 24, 90, 5, 2),
(66, 'player1', 2, 22, 100, 4, 3),
(67, 'player1', 2, 21, 95, 5, 3),
(68, 'player2', 2, 18, 90, 4, 1),
(69, 'player2', 2, 20, 100, 4, 2),
(70, 'player2', 2, 20, 97, 5, 2),
(71, 'player2', 2, 19, 100, 4, 3),
(72, 'player2', 2, 20, 90, 5, 3),
(73, 'player3', 2, 17, 100, 4, 1),
(74, 'player3', 2, 18, 100, 5, 1),
(75, 'player3', 2, 19, 90, 6, 1),
(76, 'player3', 2, 17, 100, 5, 2),
(77, 'player3', 2, 19, 85, 6, 2),
(78, 'player4', 2, 20, 100, 4, 1),
(79, 'player4', 2, 18, 100, 5, 1),
(80, 'player4', 2, 19, 100, 6, 1),
(81, 'player4', 2, 17, 87, 7, 1),
(82, 'player4', 2, 21, 90, 6, 2),
(83, 'player4', 2, 18, 80, 5, 3),
(84, 'player5', 2, 11, 100, 4, 1),
(85, 'player5', 2, 10, 70, 5, 1),
(86, 'player5', 2, 9, 100, 4, 2),
(87, 'player5', 2, 10, 95, 5, 2),
(88, 'player5', 2, 11, 100, 4, 3),
(89, 'player5', 2, 13, 100, 5, 3),
(90, 'player5', 2, 13, 90, 6, 3),
(91, 'player6', 2, 11, 95, 4, 1),
(92, 'player6', 2, 12, 100, 4, 2),
(93, 'player6', 2, 14, 97, 5, 2),
(94, 'player6', 2, 14, 100, 4, 3),
(95, 'player6', 2, 15, 90, 5, 3),
(96, 'player7', 2, 7, 100, 4, 1),
(97, 'player7', 2, 9, 100, 5, 1),
(98, 'player7', 2, 10, 100, 6, 1),
(99, 'player7', 2, 8, 95, 7, 1),
(100, 'player7', 2, 9, 75, 6, 2),
(101, 'player7', 2, 9, 85, 5, 3),
(102, 'player8', 2, 15, 100, 4, 1),
(103, 'player8', 2, 14, 89, 5, 1),
(104, 'player8', 2, 13, 100, 4, 2),
(105, 'player8', 2, 14, 60, 4, 2),
(106, 'player8', 2, 13, 78, 4, 3),
(107, 'player9', 2, 30, 100, 4, 1),
(108, 'player9', 2, 35, 74, 5, 1),
(109, 'player9', 2, 36, 87, 4, 2),
(110, 'player10', 2, 30, 100, 4, 1),
(111, 'player10', 2, 33, 100, 5, 1),
(112, 'player10', 2, 40, 100, 6, 1),
(113, 'player10', 2, 46, 100, 7, 1),
(114, 'player10', 2, 50, 80, 8, 1),
(115, 'player10', 2, 54, 90, 7, 2),
(116, 'player10', 2, 51, 87, 6, 3),
(121, 'player11', 1, 10, 10, 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `mode_game`
--

CREATE TABLE `mode_game` (
  `id` int(11) NOT NULL,
  `mode_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mode_game`
--

INSERT INTO `mode_game` (`id`, `mode_name`) VALUES
(1, 'Visual'),
(2, 'Auditory');

-- --------------------------------------------------------

--
-- Table structure for table `nback`
--

CREATE TABLE `nback` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `mode_id` int(11) NOT NULL,
  `wmi_id` int(11) NOT NULL,
  `speed_nb` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `nback_score`
--

CREATE TABLE `nback_score` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `mode_id` int(11) NOT NULL,
  `score_nb` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`) VALUES
(1, 'player1'),
(10, 'player10'),
(11, 'player11'),
(2, 'player2'),
(3, 'player3'),
(4, 'player4'),
(5, 'player5'),
(6, 'player6'),
(7, 'player7'),
(8, 'player8'),
(9, 'player9');

-- --------------------------------------------------------

--
-- Table structure for table `wmi`
--
-- Error reading structure for table fyp.wmi: #1932 - Table 'fyp.wmi' doesn't exist in engine
-- Error reading data for table fyp.wmi: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `fyp`.`wmi`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `wm_index`
--

CREATE TABLE `wm_index` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `visual_score` varchar(255) NOT NULL,
  `visual_duration` varchar(255) NOT NULL,
  `auditory_score` varchar(255) NOT NULL,
  `auditory_duration` varchar(255) NOT NULL,
  `visual_result` varchar(255) NOT NULL,
  `auditory_result` varchar(255) NOT NULL,
  `wmi_result` varchar(255) NOT NULL,
  `date_created` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `wm_index`
--

INSERT INTO `wm_index` (`id`, `username`, `visual_score`, `visual_duration`, `auditory_score`, `auditory_duration`, `visual_result`, `auditory_result`, `wmi_result`, `date_created`) VALUES
(0, 'player1', '40', '30', '20', '20', '13.155844155844155', '9.964285714285715', '13.155844155844155', '2019-12-01 08:18:16');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attempt`
--
ALTER TABLE `attempt`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `defuz_req`
--
ALTER TABLE `defuz_req`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mode_id` (`mode_id`);

--
-- Indexes for table `digit_span`
--
ALTER TABLE `digit_span`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mode_id` (`mode_id`),
  ADD KEY `username` (`username`),
  ADD KEY `attempt` (`attempt`);

--
-- Indexes for table `mode_game`
--
ALTER TABLE `mode_game`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nback`
--
ALTER TABLE `nback`
  ADD PRIMARY KEY (`id`),
  ADD KEY `username` (`username`),
  ADD KEY `mode_id` (`mode_id`);

--
-- Indexes for table `nback_score`
--
ALTER TABLE `nback_score`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mode_id` (`mode_id`),
  ADD KEY `username` (`username`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `wm_index`
--
ALTER TABLE `wm_index`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attempt`
--
ALTER TABLE `attempt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `defuz_req`
--
ALTER TABLE `defuz_req`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `digit_span`
--
ALTER TABLE `digit_span`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=123;

--
-- AUTO_INCREMENT for table `mode_game`
--
ALTER TABLE `mode_game`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `nback`
--
ALTER TABLE `nback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `nback_score`
--
ALTER TABLE `nback_score`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `defuz_req`
--
ALTER TABLE `defuz_req`
  ADD CONSTRAINT `defuz_req_ibfk_1` FOREIGN KEY (`mode_id`) REFERENCES `mode_game` (`id`);

--
-- Constraints for table `digit_span`
--
ALTER TABLE `digit_span`
  ADD CONSTRAINT `digit_span_ibfk_1` FOREIGN KEY (`mode_id`) REFERENCES `mode_game` (`id`),
  ADD CONSTRAINT `digit_span_ibfk_2` FOREIGN KEY (`username`) REFERENCES `user` (`username`),
  ADD CONSTRAINT `digit_span_ibfk_3` FOREIGN KEY (`attempt`) REFERENCES `attempt` (`id`);

--
-- Constraints for table `nback`
--
ALTER TABLE `nback`
  ADD CONSTRAINT `nback_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`),
  ADD CONSTRAINT `nback_ibfk_2` FOREIGN KEY (`mode_id`) REFERENCES `mode_game` (`id`);

--
-- Constraints for table `nback_score`
--
ALTER TABLE `nback_score`
  ADD CONSTRAINT `nback_score_ibfk_1` FOREIGN KEY (`mode_id`) REFERENCES `mode_game` (`id`),
  ADD CONSTRAINT `nback_score_ibfk_2` FOREIGN KEY (`username`) REFERENCES `user` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
