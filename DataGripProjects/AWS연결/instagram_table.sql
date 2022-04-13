CREATE TABLE `User` (
    `userIdx` int AUTO_INCREMENT NOT NULL ,
    `email` varchar(45)  NOT NULL ,
    `password` varchar(45)  NOT NULL ,
    `nickName` varchar(45)  NOT NULL ,
    `name` varchar(45)  NOT NULL ,
    `profileImgUrl` text  NULL ,
    `website` varchar(45)  NULL ,
    `introduce` varchar(45)  NULL ,
    `open` boolean  NOT NULL DEFAULT 0,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp on update current_timestamp,
    PRIMARY KEY (
        `userIdx`
    )
);

CREATE TABLE `Post` (
    `postIdx` int AUTO_INCREMENT NOT NULL ,
    `userIdx` int  NOT NULL ,
    `content` varchar(300)  NOT NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp on update current_timestamp,
    PRIMARY KEY (
        `postIdx`
    )
);

CREATE TABLE `PostImg` (
    `postImgIdx` int AUTO_INCREMENT NOT NULL ,
    `postIdx` int  NOT NULL ,
    `imgUrl` varchar(45)  NOT NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp on update current_timestamp,
    PRIMARY KEY (
        `postImgIdx`
    )
);

CREATE TABLE `PostLike` (
    `postLikeIdx` int AUTO_INCREMENT NOT NULL ,
    `postIdx` int  NOT NULL ,
    `userIdx` int  NOT NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp on update current_timestamp,
    PRIMARY KEY (
        `postLikeIdx`
    )
);

CREATE TABLE `Comment` (
    `commentIdx` int AUTO_INCREMENT NOT NULL ,
    `userIdx` int  NOT NULL ,
    `postIdx` int  NOT NULL ,
    `content` varchar(100)  NOT NULL ,
    `parentComment` int  NOT NULL DEFAULT 0,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp on update current_timestamp,
    PRIMARY KEY (
        `commentIdx`
    )
);

CREATE TABLE `CommentLike` (
    `commentLikeIdx` int AUTO_INCREMENT NOT NULL ,
    `commentIdx` int  NOT NULL ,
    `userIdx` int  NOT NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp on update current_timestamp,
    PRIMARY KEY (
        `commentLikeIdx`
    )
);

CREATE TABLE `Tag` (
    `tagIdx` int AUTO_INCREMENT NOT NULL ,
    `userIdx` int  NOT NULL ,
    `postIdx` int  NULL ,
    `commentIdx` int  NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp on update current_timestamp,
    PRIMARY KEY (
        `tagIdx`
    )
);

CREATE TABLE `Follow` (
    `followIdx` int AUTO_INCREMENT NOT NULL ,
    `followerIdx` int  NOT NULL ,
    `followeeIdx` int  NOT NULL ,
    `approve` boolean  NOT NULL DEFAULT 0,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp on update current_timestamp,
    PRIMARY KEY (
        `followIdx`
    )
);

CREATE TABLE `ChatRoom` (
    `chatRoomIdx` int AUTO_INCREMENT NOT NULL ,
    `userIdx` int  NOT NULL ,
    `chatUser` int  NOT NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp on update current_timestamp,
    PRIMARY KEY (
        `chatRoomIdx`
    )
);

CREATE TABLE `Chat` (
    `chatIdx` int AUTO_INCREMENT NOT NULL ,
    `chatRoomIdx` int  NOT NULL ,
    `userIdx` int  NOT NULL ,
    `content` varchar(300)  NOT NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp on update current_timestamp,
    PRIMARY KEY (
        `chatIdx`
    )
);

CREATE TABLE `ChatLike` (
    `chatLikeIdx` int AUTO_INCREMENT NOT NULL ,
    `chatIdx` int  NOT NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp on update current_timestamp,
    PRIMARY KEY (
        `chatLikeIdx`
    )
);

ALTER TABLE `Post` ADD CONSTRAINT `fk_Post_userIdx` FOREIGN KEY(`userIdx`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `PostImg` ADD CONSTRAINT `fk_PostImg_postIdx` FOREIGN KEY(`postIdx`)
REFERENCES `Post` (`postIdx`);

ALTER TABLE `PostLike` ADD CONSTRAINT `fk_PostLike_postIdx` FOREIGN KEY(`postIdx`)
REFERENCES `Post` (`postIdx`);

ALTER TABLE `PostLike` ADD CONSTRAINT `fk_PostLike_userIdx` FOREIGN KEY(`userIdx`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `Comment` ADD CONSTRAINT `fk_Comment_userIdx` FOREIGN KEY(`userIdx`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `Comment` ADD CONSTRAINT `fk_Comment_postIdx` FOREIGN KEY(`postIdx`)
REFERENCES `Post` (`postIdx`);

ALTER TABLE `CommentLike` ADD CONSTRAINT `fk_CommentLike_commentIdx` FOREIGN KEY(`commentIdx`)
REFERENCES `Comment` (`commentIdx`);

ALTER TABLE `CommentLike` ADD CONSTRAINT `fk_CommentLike_userIdx` FOREIGN KEY(`userIdx`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `Tag` ADD CONSTRAINT `fk_Tag_userIdx` FOREIGN KEY(`userIdx`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `Tag` ADD CONSTRAINT `fk_Tag_postIdx` FOREIGN KEY(`postIdx`)
REFERENCES `Post` (`postIdx`);

ALTER TABLE `Tag` ADD CONSTRAINT `fk_Tag_commentIdx` FOREIGN KEY(`commentIdx`)
REFERENCES `Comment` (`commentIdx`);

ALTER TABLE `Follow` ADD CONSTRAINT `fk_Follow_followerIdx` FOREIGN KEY(`followerIdx`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `Follow` ADD CONSTRAINT `fk_Follow_followeeIdx` FOREIGN KEY(`followeeIdx`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `ChatRoom` ADD CONSTRAINT `fk_ChatRoom_userIdx` FOREIGN KEY(`userIdx`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `ChatRoom` ADD CONSTRAINT `fk_ChatRoom_chatUser` FOREIGN KEY(`chatUser`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `Chat` ADD CONSTRAINT `fk_Chat_chatRoomIdx` FOREIGN KEY(`chatRoomIdx`)
REFERENCES `ChatRoom` (`chatRoomIdx`);

ALTER TABLE `Chat` ADD CONSTRAINT `fk_Chat_userIdx` FOREIGN KEY(`userIdx`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `ChatLike` ADD CONSTRAINT `fk_ChatLike_chatIdx` FOREIGN KEY(`chatIdx`)
REFERENCES `Chat` (`chatIdx`);

ALTER TABLE User ADD gender varchar(10) NOT NULL AFTER profileImgUrl;
ALTER TABLE User ADD birth DATE NOT NULL AFTER gender;
ALTER TABLE User DROP birth;
ALTER TABLE Follow DROP approve;
ALTER TABLE User MODIFY COLUMN birth DATE NOT NULL;


show databases;
SHOW TABLES;
select * from instagram.User;
CREATE DATABASE instagram default CHARACTER SET UTF8;
drop table Follow