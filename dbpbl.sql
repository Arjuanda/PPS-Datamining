-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 28, 2024 at 12:24 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbpbl`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id_admin` int NOT NULL,
  `nama` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `nip` int NOT NULL,
  `alamat` varchar(100) NOT NULL,
  `kontak` varchar(20) NOT NULL,
  `gambar` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id_admin`, `nama`, `email`, `password`, `nip`, `alamat`, `kontak`, `gambar`) VALUES
(3, 'Admin2', 'admin@pps.local', 'Password$2', 345566, 'Bengkong Sulawesi', '467766', 'static/uploads/logo.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE `log` (
  `id_log` int NOT NULL,
  `id_admin` int NOT NULL,
  `action` varchar(255) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`id_log`, `id_admin`, `action`, `timestamp`) VALUES
(4, 3, 'Editted Nilai: ARJU', '2024-06-16 05:58:56'),
(5, 3, 'Editted: ARJU', '2024-06-16 05:59:22'),
(6, 3, 'Editted: ARJU', '2024-06-17 06:19:37'),
(7, 3, 'Added: percobaan2', '2024-06-22 09:42:28'),
(8, 3, 'Added: percobaan3', '2024-06-22 09:42:46'),
(9, 3, 'Added: percobaan4', '2024-06-22 09:42:57'),
(10, 3, 'Editted: Alfarizi Ibrahim', '2024-06-22 11:48:40'),
(11, 3, 'Editted: percobaan1', '2024-06-22 11:49:13'),
(12, 3, 'Editted: Teknik Informatika', '2024-06-22 12:31:47'),
(13, 3, 'Editted: Teknik Informatika', '2024-06-22 12:32:03'),
(14, 3, 'Editted: ARJU', '2024-06-22 12:33:20'),
(15, 3, 'Editted: ARJU', '2024-06-22 12:33:38'),
(16, 3, 'Editted: Admin2', '2024-06-22 12:34:17'),
(17, 3, 'Editted: Admin2', '2024-06-22 12:41:38'),
(18, 3, 'Added: Admin3', '2024-06-22 12:43:39'),
(19, 3, 'Editted: Admin2', '2024-06-22 12:47:23'),
(20, 3, 'Editted: ARJU', '2024-06-22 12:48:18'),
(21, 3, 'Editted: Teknik Informatika', '2024-06-22 12:49:25'),
(22, 3, 'Editted: Animasi', '2024-06-22 12:54:38'),
(23, 3, 'Editted: Tekni Multimedia & Jaringan', '2024-06-22 12:55:50'),
(24, 3, 'Editted: Animasi', '2024-06-22 12:57:00'),
(25, 3, 'Deleted: Alfarizi Ibrahim', '2024-06-22 13:01:44'),
(26, 3, 'Deleted: percobaan2', '2024-06-22 13:04:07'),
(27, 3, 'Editted: Animasi', '2024-06-22 13:04:19'),
(28, 3, 'Added: Tekni Rekayasa Keamanan Siber', '2024-06-22 13:04:45'),
(29, 3, 'Editted: Teknik Rekayasa Keamanan Siber', '2024-06-22 13:05:21'),
(30, 3, 'Editted: Teknik Animasi', '2024-06-22 13:05:29'),
(31, 3, 'Added: Teknik Geomatika', '2024-06-22 13:09:45'),
(32, 3, 'Editted: Teknik Rekayasa Keamanan Siber', '2024-06-22 13:11:27'),
(33, 3, 'Editted: Teknik Informatika', '2024-06-22 13:13:00'),
(34, 3, 'Editted: Teknik Geomatika', '2024-06-22 13:13:38'),
(35, 3, 'Editted: Teknik Animasi', '2024-06-22 13:16:20'),
(36, 3, 'Editted: Teknologi Rekayasa Multimedia', '2024-06-22 13:17:31'),
(37, 3, 'Editted: Animasi', '2024-06-22 13:18:11'),
(38, 3, 'Editted: Rekayasa Keamanan Siber', '2024-06-22 13:19:54'),
(39, 3, 'Added: Teknologi Rekayasa Perangkat Lunak', '2024-06-22 13:36:45'),
(40, 3, 'Editted: Teknik Geomatika', '2024-06-22 14:45:30'),
(41, 3, 'Editted: Admin2', '2024-06-28 06:05:45'),
(42, 3, 'Deleted: Admin3', '2024-06-28 06:05:49'),
(43, 3, 'Added: Percobaan 2', '2024-06-28 08:22:52'),
(44, 3, 'Added: Percobaan 2', '2024-06-28 08:26:24'),
(45, 3, 'Added: Percobaan 2', '2024-06-28 08:33:38'),
(46, 3, 'Deleted: Percobaan 2', '2024-06-28 08:36:38'),
(47, 3, 'Deleted: Percobaan 2', '2024-06-28 08:36:40'),
(48, 3, 'Deleted: Percobaan 2', '2024-06-28 08:36:43'),
(49, 3, 'Added: Percobaan 2', '2024-06-28 08:41:45'),
(50, 3, 'Added: Percobaan 2', '2024-06-28 08:49:19'),
(51, 3, 'Deleted: Percobaan 2', '2024-06-28 08:54:48'),
(52, 3, 'Deleted: Percobaan 2', '2024-06-28 08:54:51'),
(53, 3, 'Added: Percobaan 2', '2024-06-28 08:55:43'),
(54, 3, 'Added: Percobaan 2', '2024-06-28 09:06:36'),
(55, 3, 'Deleted: Percobaan 2', '2024-06-28 09:07:38'),
(56, 3, 'Deleted: Percobaan 2', '2024-06-28 09:07:40'),
(57, 3, 'Added: Percobaan 2', '2024-06-28 09:12:46'),
(58, 3, 'Added: Percobaan 2', '2024-06-28 09:20:06'),
(59, 3, 'Added: Percobaan 2', '2024-06-28 09:29:42'),
(60, 3, 'Added: Percobaan 2', '2024-06-28 09:38:06'),
(61, 3, 'Deleted: Percobaan 2', '2024-06-28 09:39:28'),
(62, 3, 'Deleted: Percobaan 2', '2024-06-28 09:39:29'),
(63, 3, 'Deleted: Percobaan 2', '2024-06-28 09:39:31'),
(64, 3, 'Deleted: Percobaan 2', '2024-06-28 09:39:33'),
(65, 3, 'Deleted: Teknologi Rekayasa Perangkat Lunak', '2024-06-28 09:39:34'),
(66, 3, 'Added: fwewe', '2024-06-28 09:41:21'),
(67, 3, 'Deleted: fwewe', '2024-06-28 09:41:29'),
(68, 3, 'Added: Percobaan 2', '2024-06-28 10:00:52'),
(69, 3, 'Deleted: Percobaan 2', '2024-06-28 10:02:56'),
(70, 3, 'Added: Percobaan 2', '2024-06-28 10:09:04'),
(71, 3, 'Added: Pengguna Baru', '2024-06-28 10:14:38'),
(72, 3, 'Added: Percobaan 2', '2024-06-28 10:16:14'),
(73, 3, 'Deleted: Percobaan 2', '2024-06-28 10:20:06'),
(74, 3, 'Deleted: Percobaan 2', '2024-06-28 10:20:08'),
(75, 3, 'Deleted: Pengguna Baru', '2024-06-28 10:27:43'),
(76, 3, 'Added: Percobaan 2', '2024-06-28 10:29:39'),
(77, 3, 'Added: fwewe', '2024-06-28 10:33:10'),
(78, 3, 'Deleted: fwewe', '2024-06-28 10:33:16'),
(79, 3, 'Deleted: Percobaan 2', '2024-06-28 10:33:20'),
(80, 3, 'Added: Percobaan 2', '2024-06-28 10:36:43'),
(81, 3, 'Added: Percobaan 2', '2024-06-28 10:40:15'),
(82, 3, 'Added: Pengguna Baru', '2024-06-28 11:07:23'),
(83, 3, 'Editted: Percobaan ubah1', '2024-06-28 11:20:38'),
(84, 3, 'Deleted: Percobaan ubah1', '2024-06-28 11:21:52'),
(85, 3, 'Deleted: Percobaan 2', '2024-06-28 11:22:10'),
(86, 3, 'Deleted: Percobaan 2', '2024-06-28 11:22:12'),
(87, 3, 'Added: Percobaan 2', '2024-06-28 11:23:31'),
(88, 3, 'Deleted: Percobaan 2', '2024-06-28 11:24:51'),
(89, 3, 'Added: Percobaan 2', '2024-06-28 11:26:52'),
(90, 3, 'Editted: pengujian 2', '2024-06-28 11:27:42'),
(91, 3, 'Deleted: pengujian 2', '2024-06-28 11:28:20'),
(92, 3, 'Deleted: Alfarizi Ibrahim', '2024-06-28 11:51:41'),
(93, 3, 'Added: Pengguna Baru', '2024-06-28 11:58:05'),
(94, 3, 'Editted: Percobaan ubah1', '2024-06-28 11:59:04'),
(95, 3, 'Deleted: Percobaan ubah1', '2024-06-28 11:59:26'),
(96, 3, 'Editted: Percobaan ubah1', '2024-06-28 12:13:04'),
(97, 3, 'Deleted: Percobaan ubah1', '2024-06-28 12:13:40'),
(98, 3, 'Added: Percobaan 2', '2024-06-28 12:14:23'),
(99, 3, 'Deleted: Percobaan 2', '2024-06-28 12:15:42'),
(100, 3, 'Added: Pengguna Baru', '2024-06-28 12:18:59'),
(101, 3, 'Editted: Percobaan ubah1', '2024-06-28 12:20:28'),
(102, 3, 'Deleted: Percobaan ubah1', '2024-06-28 12:21:05'),
(103, 3, 'Added: Percobaan 2', '2024-06-28 12:21:49'),
(104, 3, 'Deleted: Percobaan 2', '2024-06-28 12:23:08');

-- --------------------------------------------------------

--
-- Table structure for table `nilai`
--

CREATE TABLE `nilai` (
  `id_nilai` int NOT NULL,
  `id_siswa` int NOT NULL,
  `x1` decimal(5,2) DEFAULT NULL,
  `x2` decimal(5,2) DEFAULT NULL,
  `x3` decimal(5,2) DEFAULT NULL,
  `x4` decimal(5,2) DEFAULT NULL,
  `x5` decimal(5,2) DEFAULT NULL,
  `x6` decimal(5,2) DEFAULT NULL,
  `x7` decimal(5,2) DEFAULT NULL,
  `x8` decimal(5,2) DEFAULT NULL,
  `x9` decimal(5,2) DEFAULT NULL,
  `x10` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `prodi`
--

CREATE TABLE `prodi` (
  `id_prodi` int NOT NULL,
  `nama` varchar(50) NOT NULL,
  `kode` varchar(10) NOT NULL,
  `link` varchar(255) NOT NULL,
  `gambar` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prodi`
--

INSERT INTO `prodi` (`id_prodi`, `nama`, `kode`, `link`, `gambar`) VALUES
(1, 'Teknik Informatika', 'IF', 'https://www.polibatam.ac.id/program-studi/diploma3-teknik-informatika/', 'static/uploads/IF.jpg'),
(3, 'Teknologi Rekayasa Multimedia', 'MJ', 'https://www.polibatam.ac.id/program-studi/sarjana-terapan-teknologi-rekayasa-multimedia/', 'static/uploads/MJ.jpg'),
(4, 'Animasi', 'AN', 'https://www.polibatam.ac.id/program-studi/sarjana-terapan-animasi/', 'static/uploads/AN.jpg'),
(5, 'Rekayasa Keamanan Siber', 'RKS', 'https://www.polibatam.ac.id/program-studi/sarjana-terapan-rekayasa-keamanan-siber/', 'static/uploads/RKS.jpg'),
(6, 'Teknik Geomatika', 'GM', 'https://www.polibatam.ac.id/program-studi/diploma-3-teknik-geomatika/', 'static/uploads/GM.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `siswa`
--

CREATE TABLE `siswa` (
  `id_siswa` int NOT NULL,
  `nisn` int NOT NULL,
  `nama` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `tempat_lahir` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '-',
  `tanggal_lahir` date DEFAULT '2000-01-01',
  `jenis_kelamin` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '-',
  `sekolah_asal` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '-',
  `jurusan` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '-',
  `kontak` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '-',
  `alamat` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '-',
  `gambar` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `siswa`
--

INSERT INTO `siswa` (`id_siswa`, `nisn`, `nama`, `email`, `password`, `tempat_lahir`, `tanggal_lahir`, `jenis_kelamin`, `sekolah_asal`, `jurusan`, `kontak`, `alamat`, `gambar`) VALUES
(9, 84310583, 'ARJU', 'arjuanda7@gmail.com', 'Password$#', 'Batam', '2024-05-26', 'Laki - Laki', 'sma karang', 'IPS', '34575545435', 'Bengkong Sulawesi', 'static/uploads/kisspng-car-wash-clip-art-vector-graphics-image-5b92ba479698d4.9419430515363425996169.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indexes for table `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`id_log`),
  ADD KEY `id_admin` (`id_admin`);

--
-- Indexes for table `nilai`
--
ALTER TABLE `nilai`
  ADD PRIMARY KEY (`id_nilai`),
  ADD KEY `id_siswa` (`id_siswa`);

--
-- Indexes for table `prodi`
--
ALTER TABLE `prodi`
  ADD PRIMARY KEY (`id_prodi`);

--
-- Indexes for table `siswa`
--
ALTER TABLE `siswa`
  ADD PRIMARY KEY (`id_siswa`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id_admin` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `log`
--
ALTER TABLE `log`
  MODIFY `id_log` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

--
-- AUTO_INCREMENT for table `nilai`
--
ALTER TABLE `nilai`
  MODIFY `id_nilai` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `prodi`
--
ALTER TABLE `prodi`
  MODIFY `id_prodi` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `siswa`
--
ALTER TABLE `siswa`
  MODIFY `id_siswa` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `log`
--
ALTER TABLE `log`
  ADD CONSTRAINT `id_admin` FOREIGN KEY (`id_admin`) REFERENCES `admin` (`id_admin`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `nilai`
--
ALTER TABLE `nilai`
  ADD CONSTRAINT `id_siswa` FOREIGN KEY (`id_siswa`) REFERENCES `siswa` (`id_siswa`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
