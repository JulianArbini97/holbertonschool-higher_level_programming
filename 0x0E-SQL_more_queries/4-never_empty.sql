-- script that creates the table id_not_null
CREATE TABLE IF NOT EXISTS `id_not_null` (`id` INT NOT NULL DEFAULT 1 UNIQUE,
`name` VARCHAR(256));
