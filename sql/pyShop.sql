/*
 Navicat Premium Data Transfer

 Source Server         : TestForMySql
 Source Server Type    : MySQL
 Source Server Version : 50713
 Source Host           : localhost:3306
 Source Schema         : python

 Target Server Type    : MySQL
 Target Server Version : 50713
 File Encoding         : 65001

 Date: 22/10/2021 14:28:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 33 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add 书籍管理', 7, 'add_bookinfo');
INSERT INTO `auth_permission` VALUES (26, 'Can change 书籍管理', 7, 'change_bookinfo');
INSERT INTO `auth_permission` VALUES (27, 'Can delete 书籍管理', 7, 'delete_bookinfo');
INSERT INTO `auth_permission` VALUES (28, 'Can view 书籍管理', 7, 'view_bookinfo');
INSERT INTO `auth_permission` VALUES (29, 'Can add people info', 8, 'add_peopleinfo');
INSERT INTO `auth_permission` VALUES (30, 'Can change people info', 8, 'change_peopleinfo');
INSERT INTO `auth_permission` VALUES (31, 'Can delete people info', 8, 'delete_peopleinfo');
INSERT INTO `auth_permission` VALUES (32, 'Can view people info', 8, 'view_peopleinfo');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$260000$0ZX5VMeT74IkLCqm01CcxU$TgNPKmQ4JSuPvWe2v7QlLG0W8UH6OY9Vs8toDoTGKf8=', '2021-05-11 17:11:56.292227', 1, 'wyuan', '', '', '543456229@qq.com', 1, 1, '2021-05-11 17:11:42.464435');
INSERT INTO `auth_user` VALUES (2, 'pbkdf2_sha256$260000$eRqnJzH3mbyJaKF7wbu8mJ$ewAtZ6K+iuV1dOv1jkdk8QVKaNUDJ7QsgnAztaWY1Ho=', '2021-10-22 11:02:10.198181', 1, 'admin', '', '', '543456229@qq.com', 1, 1, '2021-10-22 10:29:49.359620');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2021-05-11 17:24:40.436279', '1', '射雕英雄传', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (2, '2021-05-11 17:25:21.000297', '2', '天龙八部', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (3, '2021-05-11 17:25:42.404581', '3', '笑傲江湖', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (4, '2021-05-11 17:26:04.363168', '4', '雪山飞狐', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (5, '2021-05-11 17:27:13.223241', '1', 'PeopleInfo object (1)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (6, '2021-05-11 17:27:35.166746', '2', 'PeopleInfo object (2)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (7, '2021-05-11 17:27:50.893578', '3', 'PeopleInfo object (3)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (8, '2021-05-11 17:28:07.513186', '4', 'PeopleInfo object (4)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (9, '2021-05-11 17:28:31.972651', '5', 'PeopleInfo object (5)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (10, '2021-05-11 17:28:43.691514', '6', 'PeopleInfo object (6)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (11, '2021-05-11 17:28:59.496134', '7', 'PeopleInfo object (7)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (12, '2021-05-11 17:29:16.886324', '8', 'PeopleInfo object (8)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (13, '2021-05-11 17:29:38.137178', '9', 'PeopleInfo object (9)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (14, '2021-05-11 17:30:03.253335', '10', 'PeopleInfo object (10)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (15, '2021-05-11 17:30:36.924636', '11', 'PeopleInfo object (11)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (16, '2021-05-11 17:31:52.058533', '12', '岳不群', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (17, '2021-05-11 17:32:23.550438', '13', '东方不败', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (18, '2021-05-11 17:32:35.892756', '14', '胡斐', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (19, '2021-05-11 17:32:53.537549', '15', '苗若兰', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (20, '2021-05-11 17:33:11.184266', '16', '程灵素', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (21, '2021-05-11 17:33:27.940996', '17', '袁紫衣', 1, '[{\"added\": {}}]', 8, 1);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (7, 'book', 'bookinfo');
INSERT INTO `django_content_type` VALUES (8, 'book', 'peopleinfo');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2021-05-11 16:56:34.002532');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2021-05-11 16:56:34.689694');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2021-05-11 16:56:34.837298');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2021-05-11 16:56:34.846275');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2021-05-11 16:56:34.855251');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2021-05-11 16:56:34.949706');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2021-05-11 16:56:35.001537');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2021-05-11 16:56:35.054434');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2021-05-11 16:56:35.064370');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2021-05-11 16:56:35.112242');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2021-05-11 16:56:35.116230');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2021-05-11 16:56:35.126203');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2021-05-11 16:56:35.182056');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2021-05-11 16:56:35.257457');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2021-05-11 16:56:35.319905');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2021-05-11 16:56:35.330874');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2021-05-11 16:56:35.389718');
INSERT INTO `django_migrations` VALUES (18, 'book', '0001_initial', '2021-05-11 16:56:35.533461');
INSERT INTO `django_migrations` VALUES (19, 'book', '0002_auto_20210511_1656', '2021-05-11 16:56:35.738175');
INSERT INTO `django_migrations` VALUES (20, 'sessions', '0001_initial', '2021-05-11 16:56:35.782058');
INSERT INTO `django_migrations` VALUES (21, 'book', '0003_auto_20210511_1720', '2021-05-11 17:20:20.847447');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('f3fhoggnx9f2yh3gyduk0sch73xsbq1d', '.eJxVjEEOwiAQRe_C2pCOUwK4dO8ZCDMDUjWQlHbVeHdt0oVu_3vvbyrEdSlh7WkOk6iLAnX63SjyM9UdyCPWe9Pc6jJPpHdFH7TrW5P0uh7u30GJvXxrc7beEKL3jG6wSG4wOI4ZIAFIRgHnIgsZ9OjZ5mxtJnYAMJJAjur9AbcsN3k:1lgOQm:AZYUdGDnSiXgjVyqrUGuzpxAfECZwsYqmWp-lb-noS8', '2021-05-25 17:11:56.298210');
INSERT INTO `django_session` VALUES ('sbnzp4d1puikr5p9z1em1iri5fu056js', 'eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imlyb25tYW4ifQ:1lnY86:7v1d6SWauw1dXzAy-NnAzdBabA5cLVATQve_8EI5EGM', '2021-06-14 10:58:14.460053');

-- ----------------------------
-- Table structure for question
-- ----------------------------
DROP TABLE IF EXISTS `question`;
CREATE TABLE `question`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionType` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `optionA` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `optionB` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `optionC` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `optionD` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `score` int(11) NULL DEFAULT NULL,
  `answer` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of question
-- ----------------------------
INSERT INTO `question` VALUES (1, '计算机系统由（）组成', '单选题', '主机和系统软件', '硬件系统和应用软件', '硬件系统和软件系统', '微处理器和软件系统', 2, 'C');
INSERT INTO `question` VALUES (2, '在计算机领域中通常用主频来描述（） ', '单选题', '计算机的运算速度', '计算机的可靠性L', '计算机的可运行性', '计算机的可扩充性', 2, 'A');
INSERT INTO `question` VALUES (3, '在表示存储容量时，1MB等于()KB ', '单选题', '1000', '10000', '1024', '102.4', 2, 'C');
INSERT INTO `question` VALUES (4, '断电会使原来存储的信息丢失的存储器是（） ', '单选题', '内存', '光盘', 'U盘', '硬盘', 2, 'A');
INSERT INTO `question` VALUES (5, '通常说500G硬盘中500G指的是（）', '单选题', '厂家代号', '商标号', '磁盘编号', '磁盘容量', 2, 'D');
INSERT INTO `question` VALUES (6, '下列4种设备中，属于计算机输入设备的是（） ', '单选题', '显示器', '投影仪', '打印机', '鼠标', 2, 'D');
INSERT INTO `question` VALUES (7, '计算机病毒是可以造成机器故障的（） ', '单选题', '一种计算机设备', '一种计算机芯片', '一种计算机部件', '一种计算机程序', 2, 'D');
INSERT INTO `question` VALUES (8, '发现U盘带有计算机病毒后，比较彻底的清除方式是（） ', '单选题', '用查毒软件处理', '删除U盘上的所有文件', '格式化U盘', '用杀毒软件处理', 2, 'C');
INSERT INTO `question` VALUES (9, '键盘是目前使用最多的() ', '单选题', '存储器', '微处理器', '输入设备', '输出设备', 2, 'C');
INSERT INTO `question` VALUES (10, '信息技术就是计算机技术', '判断题', '', '', '', '', 1, '错');
INSERT INTO `question` VALUES (11, '在计算机内部信息表示的方式是二进制数', '判断题', '', '', '', '', 1, '对');
INSERT INTO `question` VALUES (12, '计算机只要硬件不出问题，就能正常工作 ', '判断题', '', '', '', '', 1, '错');
INSERT INTO `question` VALUES (13, '字节是计算机存储单位中的基本单位', '判断题', '', '', '', '', 1, '对');
INSERT INTO `question` VALUES (14, 'PC机突然停电时，RAM内存中的信息全部丢失，硬盘中的信息不受影响', '判断题', '', '', '', '', 1, '对');
INSERT INTO `question` VALUES (15, '一个完整的计算机系统应包括系统软件和应用软件', '判断题', '', '', '', '', 1, '错');
INSERT INTO `question` VALUES (16, '计算机的速度完全由CPU决定', '判断题', '', '', '', '', 1, '错');
INSERT INTO `question` VALUES (17, '简述操作系统的主要功能', '简答题', '', '', '', '', 5, '答：（1）CPU管理，解决CPU时间的分配问题 （2）作业运行控制\n （3）文件管理，主要负责整个文件的存储、检索、共享和保护等，为用户操作文件提供接口。（4）存储器管理，为每个应用程序提供存储空间的分配和协调应用程序的内存空间。（5）输入输出控制、协调、控制计算机和外部之间的输入输出的数据。');

-- ----------------------------
-- Table structure for t_book_info
-- ----------------------------
DROP TABLE IF EXISTS `t_book_info`;
CREATE TABLE `t_book_info`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `comment_count` int(11) NOT NULL,
  `is_del` tinyint(1) NOT NULL,
  `pub_date` date NULL DEFAULT NULL,
  `read_count` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `book_bookinfo_name_d3d0edfe_uniq`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_book_info
-- ----------------------------
INSERT INTO `t_book_info` VALUES (1, '射雕英雄传', 34, 0, '1980-05-01', 12);
INSERT INTO `t_book_info` VALUES (2, '天龙八部', 40, 0, '1986-07-24', 36);
INSERT INTO `t_book_info` VALUES (3, '笑傲江湖', 80, 0, '1995-12-24', 20);
INSERT INTO `t_book_info` VALUES (4, '雪山飞狐', 24, 0, '1987-11-11', 58);
INSERT INTO `t_book_info` VALUES (5, 'abc', 0, 0, '2021-05-12', 10);

-- ----------------------------
-- Table structure for t_people_info
-- ----------------------------
DROP TABLE IF EXISTS `t_people_info`;
CREATE TABLE `t_people_info`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` smallint(6) NOT NULL,
  `book_id` bigint(20) NOT NULL,
  `description` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `book_peopleinfo_name_68c22ffc_uniq`(`name`) USING BTREE,
  INDEX `book_peopleinfo_book_id_b216bb62_fk_book_bookinfo_id`(`book_id`) USING BTREE,
  CONSTRAINT `book_peopleinfo_book_id_b216bb62_fk_book_bookinfo_id` FOREIGN KEY (`book_id`) REFERENCES `t_book_info` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_people_info
-- ----------------------------
INSERT INTO `t_people_info` VALUES (1, '郭靖', 1, 1, '降龙十八掌', 0);
INSERT INTO `t_people_info` VALUES (2, '黄蓉', 2, 1, '打狗棍法', 0);
INSERT INTO `t_people_info` VALUES (3, '黄药师', 1, 1, '弹指神通', 0);
INSERT INTO `t_people_info` VALUES (4, '欧阳锋', 1, 1, '蛤蟆功', 0);
INSERT INTO `t_people_info` VALUES (5, '梅超风', 2, 1, '九阴白骨爪', 0);
INSERT INTO `t_people_info` VALUES (6, '乔峰', 1, 2, '降龙十八掌', 0);
INSERT INTO `t_people_info` VALUES (7, '段誉', 1, 2, '六脉神剑', 0);
INSERT INTO `t_people_info` VALUES (8, '虚竹', 1, 2, '天山六阳掌', 0);
INSERT INTO `t_people_info` VALUES (9, '王语嫣', 2, 2, '神仙姐姐', 0);
INSERT INTO `t_people_info` VALUES (10, '令狐冲', 1, 3, '独孤九剑', 0);
INSERT INTO `t_people_info` VALUES (11, '任盈盈', 2, 3, '弹琴', 0);
INSERT INTO `t_people_info` VALUES (12, '岳不群', 1, 3, '华山剑法', 0);
INSERT INTO `t_people_info` VALUES (13, '东方不败', 2, 3, '葵花宝典', 0);
INSERT INTO `t_people_info` VALUES (14, '胡斐', 1, 4, '胡家刀法', 0);
INSERT INTO `t_people_info` VALUES (15, '苗若兰', 2, 4, '黄衣', 0);
INSERT INTO `t_people_info` VALUES (16, '程灵素', 2, 4, '医术', 0);
INSERT INTO `t_people_info` VALUES (17, '袁紫衣', 2, 4, '六合拳', 0);

SET FOREIGN_KEY_CHECKS = 1;
