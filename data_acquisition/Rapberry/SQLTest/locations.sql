-- Table: powertic.locations

-- DROP TABLE IF EXISTS powertic.locations;

CREATE TABLE IF NOT EXISTS public.locations
(
    locationid smallint NOT NULL,
    numbmeters integer,
    name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT locations_pkey PRIMARY KEY (locationid)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.locations
    OWNER to postgres;