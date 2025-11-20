# create table playlist(
#     pid int NOT NULL AUTO_INCREMENT,
#     Name varchar(40),
#     Playlist_data text not null,
#     uid int,
#     PRIMARY KEY(pid),
#     FOREIGN KEY(uid) references auth(id));