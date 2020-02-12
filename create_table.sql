-- Table: files.address_lat_long

-- DROP TABLE files.address_lat_long;

CREATE TABLE files.address_lat_long
(
    street_number character varying COLLATE pg_catalog."default",
    street_name character varying COLLATE pg_catalog."default",
    colonia character varying COLLATE pg_catalog."default",
    ciudad character varying COLLATE pg_catalog."default",
    state character varying COLLATE pg_catalog."default",
    postal_code character varying COLLATE pg_catalog."default",
    formatted_address character varying COLLATE pg_catalog."default",
    latitude character varying COLLATE pg_catalog."default",
    longitude character varying COLLATE pg_catalog."default",
    location_type character varying COLLATE pg_catalog."default",
    location_id integer,
    id integer NOT NULL DEFAULT nextval('files.address_lat_long_id_seq'::regclass),
    CONSTRAINT address_lat_long_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE files.address_lat_long
    OWNER to postgres;