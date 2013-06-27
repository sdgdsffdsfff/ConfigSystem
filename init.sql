--创建数据库
create database config_manager character set 'utf8' collate 'utf8_general_ci';

use config_manager;

--创建项目表
create table rz_dc_project(
  id int not null auto_increment primary key,
  project_name varchar(20) not null,
  location varchar(200),
  project_manager varchar(25)
)DEFAULT CHARSET=utf8;

--初始化项目表
insert into rz_dc_project(project_name, location, project_manager) values('永安', '杭州', '陈耀');
insert into rz_dc_project(project_name, location, project_manager) values('华泰', '南京', '汪纪跃');
insert into rz_dc_project(project_name, location, project_manager) values('申万', '上海', '汪纪跃');

--创建采集问题表
create table rz_dc_gather_issue(
  id int not null auto_increment primary key,
  issue_project int not null,
  issue_status varchar(20) not null,
  issue_net_name varchar(200) not null,
  issue_net_add varchar(200) not null,
  issue_add_date date
) DEFAULT CHARSET=utf8;
