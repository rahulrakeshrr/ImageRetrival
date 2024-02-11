CREATE DATABASE fab_detec;
USE fab_detec;
CREATE TABLE image(
id int,
img blob);
insert into image(id,img) values(1,load_file("C:\Users\rahul\Pictures\Manali pics\WhatsApp Image 2022-09-26 at 11.15.15 PM (3).jpeg"));
insert into image(id,img) values(1,load_file("C:\Users\rahul\Pictures\Manali pics\WhatsApp Image 2022-09-26 at 11.16.51 PM (1).jpeg"));
insert into image(id,img) values(1,load_file("C:\Users\rahul\Pictures\Manali pics\WhatsApp Image 2022-09-26 at 11.17.47 PM.jpeg"));
insert into image(id,img) values(1,load_file("C:\Users\rahul\Pictures\Manali pics\WhatsApp Image 2022-09-26 at 11.23.01 PM (2).jpeg"));
insert into image(id,img) values(1,load_file("C:\Users\rahul\Pictures\Manali pics\WhatsApp Image 2022-09-20 at 3.59.24 PM.jpeg"));
