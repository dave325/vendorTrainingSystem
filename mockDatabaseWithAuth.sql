-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Aug 08, 2019 at 02:13 PM
-- Server version: 5.7.27
-- PHP Version: 7.2.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wordpress`
--

-- --------------------------------------------------------

--
-- Table structure for table `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('ae65b1f4fde9fbd2a40265da3462ac83ef4f22dd', '2019-08-06 18:20:57.257529', 5);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add role', 7, 'add_role'),
(26, 'Can change role', 7, 'change_role'),
(27, 'Can delete role', 7, 'delete_role'),
(28, 'Can view role', 7, 'view_role'),
(29, 'Can add vendor', 8, 'add_vendor'),
(30, 'Can change vendor', 8, 'change_vendor'),
(31, 'Can delete vendor', 8, 'delete_vendor'),
(32, 'Can view vendor', 8, 'view_vendor'),
(33, 'Can add user', 9, 'add_user'),
(34, 'Can change user', 9, 'change_user'),
(35, 'Can delete user', 9, 'delete_user'),
(36, 'Can view user', 9, 'view_user'),
(37, 'Can add member', 10, 'add_member'),
(38, 'Can change member', 10, 'change_member'),
(39, 'Can delete member', 10, 'delete_member'),
(40, 'Can view member', 10, 'view_member'),
(41, 'Can add event', 11, 'add_event'),
(42, 'Can change event', 11, 'change_event'),
(43, 'Can delete event', 11, 'delete_event'),
(44, 'Can view event', 11, 'view_event'),
(45, 'Can add attendance', 12, 'add_attendance'),
(46, 'Can change attendance', 12, 'change_attendance'),
(47, 'Can delete attendance', 12, 'delete_attendance'),
(48, 'Can view attendance', 12, 'view_attendance'),
(49, 'Can add Token', 13, 'add_token'),
(50, 'Can change Token', 13, 'change_token'),
(51, 'Can delete Token', 13, 'delete_token'),
(52, 'Can view Token', 13, 'view_token');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, '!M7SVIaUiyOJfUHmMP4biaF2pu7ayqPsvOBJzNoa9', NULL, 0, 'username', '', '', '', 0, 1, '2019-08-06 16:48:41.221823'),
(3, '!JxTOvjcAJDvDo4bXU95uI6ZG19nzoVI1l65ktyPX', NULL, 0, 'myname', '', '', '', 0, 1, '2019-08-06 16:49:20.680809'),
(4, 'pbkdf2_sha256$150000$JbPOZyksVPG7$bwVnf6Z6k3DOKL481Zn6YuTLQGpul5TIOYfCYwzi9jk=', NULL, 1, 'root', '', '', 'dongsoochung99@gmail.com', 1, 1, '2019-08-06 17:47:16.820164'),
(5, 'pbkdf2_sha256$150000$AyrAkhfLUrgg$eoAMPoSeTN4MJt8tZA0neXDafrFTE/gcd96ocq3dbZE=', NULL, 1, 'super', '', '', 'sevaschan99@hotmail.com', 1, 1, '2019-08-06 18:09:06.108294');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(13, 'authtoken', 'token'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(12, 'vendortraining', 'attendance'),
(11, 'vendortraining', 'event'),
(10, 'vendortraining', 'member'),
(7, 'vendortraining', 'role'),
(9, 'vendortraining', 'user'),
(8, 'vendortraining', 'vendor');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-07-25 18:57:04.153978'),
(2, 'auth', '0001_initial', '2019-07-25 18:57:04.479067'),
(3, 'admin', '0001_initial', '2019-07-25 18:57:05.424607'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-07-25 18:57:05.797148'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-07-25 18:57:05.928502'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-07-25 18:57:06.277809'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-07-25 18:57:06.351919'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-07-25 18:57:06.483686'),
(9, 'auth', '0004_alter_user_username_opts', '2019-07-25 18:57:06.605641'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-07-25 18:57:06.733866'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-07-25 18:57:06.752476'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-07-25 18:57:06.816478'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-07-25 18:57:06.892000'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-07-25 18:57:06.959582'),
(15, 'auth', '0010_alter_group_name_max_length', '2019-07-25 18:57:07.022561'),
(16, 'auth', '0011_update_proxy_permissions', '2019-07-25 18:57:07.073962'),
(17, 'sessions', '0001_initial', '2019-07-25 18:57:07.137531'),
(18, 'vendortraining', '0001_initial', '2019-07-25 18:57:07.495421'),
(19, 'vendortraining', '0002_auto_20190725_1557', '2019-07-25 18:57:08.650047'),
(20, 'vendortraining', '0003_remove_event_created_at', '2019-07-25 18:57:08.822304'),
(21, 'vendortraining', '0004_event_created_at', '2019-07-25 18:57:09.015844'),
(22, 'authtoken', '0001_initial', '2019-08-06 18:07:33.479911'),
(23, 'authtoken', '0002_auto_20160226_1747', '2019-08-06 18:07:33.560214');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vendortraining_attendance`
--

CREATE TABLE `vendortraining_attendance` (
  `id` int(11) NOT NULL,
  `event_id_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `event_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vendortraining_event`
--

CREATE TABLE `vendortraining_event` (
  `id` int(11) NOT NULL,
  `modified_at` date NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `modified_by_id` int(11) NOT NULL,
  `vendor_id_id` int(11) NOT NULL,
  `created_at` date NOT NULL,
  `vendor_id` int(11) DEFAULT NULL,
  `created_by` varchar(100) DEFAULT NULL,
  `modified_by` varchar(100) DEFAULT NULL,
  `is_approved` tinyint(1) DEFAULT NULL,
  `total_attendance` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vendortraining_event`
--

INSERT INTO `vendortraining_event` (`id`, `modified_at`, `created_by_id`, `modified_by_id`, `vendor_id_id`, `created_at`, `vendor_id`, `created_by`, `modified_by`, `is_approved`, `total_attendance`) VALUES
(1, '2019-08-06', 3, 5, 3, '2019-08-06', NULL, NULL, NULL, NULL, NULL),
(2, '2019-08-22', 1, 7, 2, '2019-08-02', NULL, NULL, NULL, NULL, NULL),
(3, '2019-08-22', 1, 7, 2, '2019-08-02', NULL, NULL, NULL, NULL, NULL),
(4, '2019-08-06', 3, 5, 3, '2019-08-06', NULL, NULL, NULL, NULL, NULL),
(5, '2019-08-06', 3, 5, 3, '2019-08-06', NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `vendortraining_member`
--

CREATE TABLE `vendortraining_member` (
  `id` int(11) NOT NULL,
  `company_role` varchar(100) NOT NULL,
  `user_id_id` int(11) NOT NULL,
  `vendor_id_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `vendor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vendortraining_role`
--

CREATE TABLE `vendortraining_role` (
  `id` int(11) NOT NULL,
  `role_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vendortraining_role`
--

INSERT INTO `vendortraining_role` (`id`, `role_name`) VALUES
(1, 'user'),
(3, 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `vendortraining_user`
--

CREATE TABLE `vendortraining_user` (
  `id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `address` text NOT NULL,
  `password` varchar(100) NOT NULL,
  `role_id_id` int(11) NOT NULL,
  `events` int(8) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `public` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vendortraining_user`
--

INSERT INTO `vendortraining_user` (`id`, `email`, `first_name`, `last_name`, `phone`, `address`, `password`, `role_id_id`, `events`, `role_id`, `public`) VALUES
(1, 'gg@gmail.com', 'john', 'smith', '123-456-7890', '87 queens', 'hello', 3, NULL, 3, 1),
(5, 'sample@email.com', 'hnjbgfrvghjn', 'vfcgvhj', 'cfgvj', 'cfgvhjncdeegf', 'sdghj', 1, NULL, 1, 1),
(6, 'dsfgkjnldfkjsglkj', 'hnjbgfrvghjn', 'vfcgvhj', 'cfgvj', 'cfgvhjncdeegf', 'sdghj', 1, NULL, 1, 1),
(7, 'dsfgkjnldfkjsglkj', 'hnjbgfrvghjn', 'vfcgvhj', 'cfgvj', 'cfgvhjncdeegf', 'sdghj', 1, NULL, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `vendortraining_vendor`
--

CREATE TABLE `vendortraining_vendor` (
  `vendor_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `phone` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_approved` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vendortraining_vendor`
--

INSERT INTO `vendortraining_vendor` (`vendor_id`, `name`, `address`, `phone`, `email`, `is_approved`) VALUES
(1, 'cerverizzo', 'TheQCTechIncqubator', '911', 'ed@yahoo.com', 1),
(2, 'asdlkfalskdn', 'asldfnajgiuhln.mansdf', '8165654', 'aksdfaksjniuoiugi76olhiu', NULL),
(3, 'sadfasd', 'asdfasdlkjlk', '6518132165', 'asdfanlkamnsdlf', NULL),
(4, 'adfoangoabuo', '5', '5', '5', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `vendortraining_attendance`
--
ALTER TABLE `vendortraining_attendance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vendortraining_atten_event_id_id_815f8b18_fk_vendortra` (`event_id_id`),
  ADD KEY `vendortraining_atten_user_id_id_224bae6c_fk_vendortra` (`user_id_id`);

--
-- Indexes for table `vendortraining_event`
--
ALTER TABLE `vendortraining_event`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vendortraining_event_modified_by_id_283be032_fk_vendortra` (`modified_by_id`),
  ADD KEY `vendortraining_event_vendor_id_id_370fc382_fk_vendortra` (`vendor_id_id`),
  ADD KEY `vendortraining_event_created_by_id_d86c6464_fk_vendortra` (`created_by_id`);

--
-- Indexes for table `vendortraining_member`
--
ALTER TABLE `vendortraining_member`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vendortraining_membe_user_id_id_c26d8c14_fk_vendortra` (`user_id_id`),
  ADD KEY `vendortraining_membe_vendor_id_id_588417d7_fk_vendortra` (`vendor_id_id`);

--
-- Indexes for table `vendortraining_role`
--
ALTER TABLE `vendortraining_role`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vendortraining_user`
--
ALTER TABLE `vendortraining_user`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vendortraining_user_role_id_id_5ad9f0ca_fk_vendortra` (`role_id_id`);

--
-- Indexes for table `vendortraining_vendor`
--
ALTER TABLE `vendortraining_vendor`
  ADD PRIMARY KEY (`vendor_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `vendortraining_attendance`
--
ALTER TABLE `vendortraining_attendance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `vendortraining_event`
--
ALTER TABLE `vendortraining_event`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `vendortraining_member`
--
ALTER TABLE `vendortraining_member`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `vendortraining_role`
--
ALTER TABLE `vendortraining_role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `vendortraining_user`
--
ALTER TABLE `vendortraining_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `vendortraining_vendor`
--
ALTER TABLE `vendortraining_vendor`
  MODIFY `vendor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `vendortraining_attendance`
--
ALTER TABLE `vendortraining_attendance`
  ADD CONSTRAINT `vendortraining_atten_event_id_id_815f8b18_fk_vendortra` FOREIGN KEY (`event_id_id`) REFERENCES `vendortraining_event` (`id`),
  ADD CONSTRAINT `vendortraining_atten_user_id_id_224bae6c_fk_vendortra` FOREIGN KEY (`user_id_id`) REFERENCES `vendortraining_user` (`id`);

--
-- Constraints for table `vendortraining_event`
--
ALTER TABLE `vendortraining_event`
  ADD CONSTRAINT `vendortraining_event_created_by_id_d86c6464_fk_vendortra` FOREIGN KEY (`created_by_id`) REFERENCES `vendortraining_vendor` (`vendor_id`),
  ADD CONSTRAINT `vendortraining_event_modified_by_id_283be032_fk_vendortra` FOREIGN KEY (`modified_by_id`) REFERENCES `vendortraining_user` (`id`),
  ADD CONSTRAINT `vendortraining_event_vendor_id_id_370fc382_fk_vendortra` FOREIGN KEY (`vendor_id_id`) REFERENCES `vendortraining_vendor` (`vendor_id`);

--
-- Constraints for table `vendortraining_member`
--
ALTER TABLE `vendortraining_member`
  ADD CONSTRAINT `vendortraining_membe_user_id_id_c26d8c14_fk_vendortra` FOREIGN KEY (`user_id_id`) REFERENCES `vendortraining_user` (`id`),
  ADD CONSTRAINT `vendortraining_membe_vendor_id_id_588417d7_fk_vendortra` FOREIGN KEY (`vendor_id_id`) REFERENCES `vendortraining_vendor` (`vendor_id`);

--
-- Constraints for table `vendortraining_user`
--
ALTER TABLE `vendortraining_user`
  ADD CONSTRAINT `vendortraining_user_role_id_id_5ad9f0ca_fk_vendortra` FOREIGN KEY (`role_id_id`) REFERENCES `vendortraining_role` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
