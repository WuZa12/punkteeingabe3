-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 27. Feb 2015 um 19:34
-- Server Version: 5.6.21
-- PHP-Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Datenbank: `database`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `klausuren`
--

CREATE TABLE IF NOT EXISTS `klausuren` (
  `id` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Thema` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `klausuren`
--

INSERT INTO `klausuren` (`id`, `Name`, `Thema`) VALUES
(0, 'TestKlausur', 'dies ist eine Testklausur, sie ist nur zum testen da');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Noten`
--

CREATE TABLE IF NOT EXISTS `Noten` (
  `id` int(11) NOT NULL,
  `matrikel` int(11) NOT NULL,
  `id_klausur` int(11) NOT NULL,
  `frage1` int(11) NOT NULL,
  `frage2` int(11) NOT NULL,
  `frage3` int(11) NOT NULL,
  `frage4` int(11) NOT NULL,
  `frage5` int(11) NOT NULL,
  `frage6` int(11) NOT NULL,
  `frage7` int(11) NOT NULL,
  `frage8` int(11) NOT NULL,
  `frage9` int(11) NOT NULL,
  `frage10` int(11) NOT NULL,
  `frage11` int(11) NOT NULL,
  `frage12` int(11) NOT NULL,
  `frage13` int(11) NOT NULL,
  `frage14` int(11) NOT NULL,
  `frage15` int(11) NOT NULL,
  `frage16` int(11) NOT NULL,
  `frage17` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `Noten`
--

INSERT INTO `Noten` (`id`, `matrikel`, `id_klausur`, `frage1`, `frage2`, `frage3`, `frage4`, `frage5`, `frage6`, `frage7`, `frage8`, `frage9`, `frage10`, `frage11`, `frage12`, `frage13`, `frage14`, `frage15`, `frage16`, `frage17`) VALUES
(1, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `klausuren`
--
ALTER TABLE `klausuren`
 ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `Noten`
--
ALTER TABLE `Noten`
 ADD PRIMARY KEY (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
