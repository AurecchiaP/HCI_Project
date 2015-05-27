DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS hardware;
DROP TABLE IF EXISTS software;
DROP TABLE IF EXISTS hci;
DROP TABLE IF EXISTS internet;
CREATE TABLE games (
  id int PRIMARY KEY,
  title text,
  body text,
  category text,
  linkToArticle text,
  previousTitle text,
  previousLink text,
  nextTitle text,
  nextLink text,
  externalLinks text,
  date text
);

CREATE TABLE hardware (
  id int PRIMARY KEY,
  title text,
  body text,
  category text,
  linkToArticle text,
  previousTitle text,
  previousLink text,
  nextTitle text,
  nextLink text,
  externalLinks text,
  date text
);

CREATE TABLE software (
  id int PRIMARY KEY,
  title text,
  body text,
  category text,
  linkToArticle text,
  previousTitle text,
  previousLink text,
  nextTitle text,
  nextLink text,
  externalLinks text,
  date text
);

CREATE TABLE hci (
  id int PRIMARY KEY,
  title text,
  body text,
  category text,
  linkToArticle text,
  previousTitle text,
  previousLink text,
  nextTitle text,
  nextLink text,
  externalLinks text,
  date text
);

CREATE TABLE internet (
  id int PRIMARY KEY,
  title text,
  body text,
  category text,
  linkToArticle text,
  previousTitle text,
  previousLink text,
  nextTitle text,
  nextLink text,
  externalLinks text,
  date text
);