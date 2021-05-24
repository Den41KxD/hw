--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.actors (
    id name,
    surname character varying(100) NOT NULL,
    age date,
    place_of_birth character varying(100)
);


--
-- Name: directors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.directors (
    id name,
    day_of_birth date,
    place_of_birth character varying(100),
    count_of_films integer
);


--
-- Name: film; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.film (
    id name NOT NULL,
    genre character varying(100),
    director character varying(100),
    release_date date,
    awards character varying(100)
);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.actors (id, surname, age, place_of_birth) FROM stdin;
Anthony	Hopkins	1937-12-31	Port Talbot, Glamorgan, Wales
Den	Smith	1996-02-01	Alabama
Jonh	Jones	1996-02-02	Alabama
Mike	Taylor	1995-03-02	Delaware
Mike	Brown	1974-12-12	Hawaii
Greg	Williams	1964-11-12	Hawaii
Greg	Wilson	1964-11-23	Indiana
Anna	Davies	1764-09-15	Georgia
Anna	Patel	1984-09-15	Michigan
Janet	Thompson	1984-09-15	Maine
Robert	Robinson	1994-07-13	Louisiana
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.directors (id, day_of_birth, place_of_birth, count_of_films) FROM stdin;
George Lukas	1944-05-14	Modesto,California	21
Dickson	1945-05-21	Montana	4
Chaplin	1932-06-27	Hawaii	14
Whale	1936-05-23	Hawaii	17
pressburger	1976-03-02	Hawaii	12
Powell	1956-06-12	Louisiana	3
Olivier	1963-04-15	Louisiana	15
asquith	1982-10-26	Nebraska	19
Reed	1945-09-06	Nebraska	19
Hamar	1953-08-16	Minnesota	24
\.


--
-- Data for Name: film; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.film (id, genre, director, release_date, awards) FROM stdin;
Star wars	science fiction	George Lucas	1995-09-20	\N
Parasite	Crime	Kang	2019-07-13	\N
1917	War	Scott	2019-08-16	\N
Wonder_Woman	Fantasy	Gadot	1984-07-20	\N
The Croods	Animation	Cage	2019-04-23	\N
Tenet	Action	Washington	2017-02-23	\N
The Outpost	Drama	Eastwood	2021-10-27	\N
Onward	Animation	Pratt	2020-08-06	\N
The invisible man	Horror	Moss	2020-01-28	\N
Little woman	Drama	Ronan	2020-01-07	\N
birds of prey	Action	Robbie	2020-01-07	\N
Jojo rabbit	War	Johansson	2020-05-31	\N
The gentleman	Action	Hunnam	2020-01-27	\N
scream	Horror	 Wes Craven	1996-12-20	\N
\.


--
-- PostgreSQL database dump complete
--

