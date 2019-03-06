-- INSERT INTO auth_user VALUES (null, 'pbkdf2_sha256$120000$TH14Dm7ojtWQ$ArXT7OjsyiZ5Qxpr3Z8mFIp7Hh10m0qhDh0vtjsG4Dk=', "2019-02-08 17:29:12", 0,'cust1', 'User', 'exampleUser@gmail.com', 0, 1, '2019-02-08 17:28:14', 'One');
-- INSERT INTO auth_user VALUES (null, 'pbkdf2_sha256$120000$aFwSrAL7i2fp$n+f+gG9Rx37PDzYT7E2v6WMUHPXmUKPWdQjOywBfW3o=', "2019-02-08 17:49:01", 0, 'cust2', 'User', 'user2@gmail.com', 0, 1, '2019-02-08 17:46:56', 'Two');
-- INSERT INTO auth_user VALUES (null, 'pbkdf2_sha256$120000$wuZz8vSAxYxr$GXNEva0KNibqZnHkIvlcF0ie4ikjqrCMr2GA+wuDwPA=', "2019-02-08 17:50:31", 0, 'cust3', 'User', 'user3@gmail.com', 0, 1, '2019-02-08 17:50:04', 'Three');

INSERT INTO sourcery_resource_type VALUES (null, 'Javascript', NULL, 1);
INSERT INTO sourcery_resource_type VALUES (null, 'React', NULL, 1);

INSERT INTO sourcery_resource VALUES (null, 'Javascript 30- Build 30 things in vanilla JS with 30 tutorials (Wes Bos)','https://javascript30.com/', 'Wanting to do this after graduation', 'https://s3.amazonaws.com/js30-cdn/small0.jpg', null, 0, 1, 1);
INSERT INTO sourcery_resource VALUES (null, 'Learn Enough Javascript to be Dangerous','https://www.learnenough.com/javascript-tutorial/hello_world', 'Someone recommended this a while back. This is the e-version of the book' 'https://softcover.s3.amazonaws.com/636/learn_enough_javascript/images/cover-web.png', null, 0, 1, 1);
INSERT INTO sourcery_resource VALUES (null, 'Learn React- Crash Course with Mosh','https://www.youtube.com/watch?v=Ke90Tje7VS0', 'Watched this a few months ago, might be useful to go back and check it out again', 'https://yt3.ggpht.com/a-/AAuE7mBCrbz-IwFv2CcXV5A4182dhvlR8_WZ2qBMNQ=s176-mo-c-c0xffffffff-rj-k-no', null, 0, 2, 1);
INSERT INTO sourcery_resource VALUES (null, 'A Simple Intro to React Hooks','https://daveceddia.com/intro-to-hooks/', 'Probably time to start learning hooks', 'https://daveceddia.com/images/hooks-intro@2x.jpg', null, 0, 2, 1);