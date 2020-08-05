-- user
-- password = 123456
INSERT INTO user(name, email, password)
VALUES ("Duong Le", "duong@gmail.com", "pbkdf2:sha256:150000$hXyYurRD$48231332f02fabef7213045cba803565a5dde6aec22bc40cbfea3457b1b01739");

INSERT INTO user(name, email, password)
VALUES ("Minh Phan", "minhp@gmail.com", "pbkdf2:sha256:150000$V0MCW80Q$dda49ae5b8941f9fdbd21fcc92c46ec27b78ab188716aa36c3280e7a1092a480");

-- category
INSERT INTO category(name, description, image_url)
VALUES ("Spring", "warm", "https://miro.medium.com/max/3840/1*oxzfllcH_OqAppRptmWa8A.jpeg");

INSERT INTO category(name, description, image_url)
VALUES ("Summer", "Hot", "https://miro.medium.com/max/3840/1*oxzfllcH_OqAppRptmWa8A.jpeg");

INSERT INTO category(name, description, image_url)
VALUES ("Fall", "Cool", "https://miro.medium.com/max/3840/1*oxzfllcH_OqAppRptmWa8A.jpeg");

INSERT INTO category(name, description, image_url)
VALUES ("Winter", "Cold", "https://miro.medium.com/max/3840/1*oxzfllcH_OqAppRptmWa8A.jpeg");

-- Item
INSERT INTO item(description, image_url, user_id, category_id)
VALUES("Plant", "https://miro.medium.com/max/3840/1*oxzfllcH_OqAppRptmWa8A.jpeg", 1, 1);

INSERT INTO item(description, image_url, user_id, category_id)
VALUES("Water", "https://miro.medium.com/max/3840/1*oxzfllcH_OqAppRptmWa8A.jpeg", 1, 1);

INSERT INTO item(description, image_url, user_id, category_id)
VALUES("Ground", "https://miro.medium.com/max/3840/1*oxzfllcH_OqAppRptmWa8A.jpeg", 2, 1);

INSERT INTO item(description, image_url, user_id, category_id)
VALUES("Sky", "https://miro.medium.com/max/3840/1*oxzfllcH_OqAppRptmWa8A.jpeg", 1, 1);