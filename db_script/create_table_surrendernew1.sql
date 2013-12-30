CREATE TABLE surrendernew1
(
  transactionid serial NOT NULL,
  clastname character varying NOT NULL,
  cfirstname character varying NOT NULL,
  cmiddlename character varying NOT NULL,
  cdtitle character varying NOT NULL,
  penalty integer NOT NULL,
  Primary Key (transactionid)
);