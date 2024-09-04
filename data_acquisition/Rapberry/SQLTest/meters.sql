-- Table: powertic.meters

-- DROP TABLE IF EXISTS powertic.meters;

CREATE TABLE IF NOT EXISTS public.meters
(
    serial_number text COLLATE pg_catalog."default" NOT NULL,
    sunspec_id text COLLATE pg_catalog."default" NOT NULL,
    id text COLLATE pg_catalog."default" NOT NULL,
    manufacturer text COLLATE pg_catalog."default" NOT NULL,
    model text COLLATE pg_catalog."default" NOT NULL,
    version text COLLATE pg_catalog."default" NOT NULL,
    locations_locationid smallint NOT NULL,
    registeryear text COLLATE pg_catalog."default" NOT NULL,
    status text COLLATE pg_catalog."default",
    CONSTRAINT meters_pkey PRIMARY KEY (serial_number),
    CONSTRAINT meters_serial_number_locations_locationid_key UNIQUE (serial_number, locations_locationid),
    CONSTRAINT meters_locations_locationid_fkey FOREIGN KEY (locations_locationid)
        REFERENCES public.locations (locationid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.meters
    OWNER to postgres;