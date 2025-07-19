-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 19, 2025 at 01:40 PM
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
-- Database: `mahasiswa1`
--

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswaaa`
--

CREATE TABLE `mahasiswaaa` (
  `npm` varchar(100) NOT NULL,
  `nama_lengkap` varchar(100) NOT NULL,
  `nama_panggilan` varchar(100) NOT NULL,
  `no_hp` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `kelas` varchar(100) NOT NULL,
  `matkul` varchar(100) NOT NULL,
  `prodi` varchar(100) NOT NULL,
  `lokasi_kampus` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `mahasiswaaa`
--

INSERT INTO `mahasiswaaa` (`npm`, `nama_lengkap`, `nama_panggilan`, `no_hp`, `email`, `kelas`, `matkul`, `prodi`, `lokasi_kampus`) VALUES
('2310020061', 'Taibah', 'Ebah', '081345286832', 'taibaht78@gmail.com', '4B REG BJM', 'Pemograman Visual 1', 'Sistem Informasi', 'Adhayaksa'),
('2310020061', 'Nur Hayati Dwi Lestari', 'Itar', '081234564321', 'itar@gmail.com', '4B REG BJM', 'Bahasa Inggris', 'Sistem Informasi', 'Adhayaksa'),
('2310020071', 'Nazriah Wardina', 'Dina', '089787654321', 'dinaa@gmail.com', '4B REG BJM', 'Bahasa Indonesia', 'Sistem Informasi', 'Handil Bakti'),
('2310026678', 'Siti Naila Nabila', 'nayy', '098765456789', 'nayyy@gmail.com', '4A REG BJM', 'Pemograman Basis Data', 'Sistem Informasi', 'Adhayaksa'),
('2310020041', 'Aulia Tiara', 'Yaya', '089765432345', 'yayaaaaaulia@gmail.com', '4A REG BJM', 'Pemograman  Berbasis Objek1', 'Sistem Informasi', 'Adhayaksa');

-- --------------------------------------------------------

--
-- Table structure for table `nilai`
--

CREATE TABLE `nilai` (
  `id` int NOT NULL,
  `id_mahasiswa` varchar(100) DEFAULT NULL,
  `nilai_harian` int DEFAULT NULL,
  `nilai_tugas` int DEFAULT NULL,
  `nilai_uts` int DEFAULT NULL,
  `nilai_uas` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `nilai`
--

INSERT INTO `nilai` (`id`, `id_mahasiswa`, `nilai_harian`, `nilai_tugas`, `nilai_uts`, `nilai_uas`) VALUES
(1, '2310020061', 80, 80, 90, 90),
(1, '2310020061', 80, 80, 90, 90),
(2, '2310020051', 80, 90, 80, 90),
(3, '2310020051', 85, 85, 90, 95),
(4, '2310020031', 80, 80, 85, 90),
(5, '2310020021', 89, 80, 85, 87);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
