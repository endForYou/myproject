CREATE TABLE `yzy_major_score_ngk` (
  `id` int NOT NULL,
  `major_name` varchar(255) DEFAULT NULL,
  `subject_need` varchar(255) DEFAULT NULL,
  `enroll_count` varchar(255) DEFAULT NULL,
  `highest_score` varchar(255) DEFAULT NULL,
  `lowest_score` varchar(255) DEFAULT NULL,
  `college_name` varchar(255) DEFAULT NULL,
  `college_direction` varchar(255) DEFAULT NULL,
  `year` varchar(255) DEFAULT NULL,
  `science_art` varchar(255) DEFAULT NULL,
  `grade` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;