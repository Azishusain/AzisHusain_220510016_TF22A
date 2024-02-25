-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: sql.freedb.tech
-- Waktu pembuatan: 22 Feb 2024 pada 09.26
-- Versi server: 8.0.36-0ubuntu0.22.04.1
-- Versi PHP: 8.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `freedb_d32022pbo`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `apotek`
--

CREATE TABLE `apotek` (
  `id` int NOT NULL,
  `no_inv` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nama_obat` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `jumlah_pembelian` int DEFAULT NULL,
  `harga` decimal(50,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `apotek`
--

INSERT INTO `apotek` (`id`, `no_inv`, `nama_obat`, `jumlah_pembelian`, `harga`) VALUES
(9, '4444', 'Paracetamol', 10, 5000);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `apotek`
--
ALTER TABLE `apotek`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `no_inv` (`no_inv`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `apotek`
--
ALTER TABLE `apotek`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
