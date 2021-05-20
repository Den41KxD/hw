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
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.directors (id, day_of_birth, place_of_birth, count_of_films) FROM stdin;
George Lukas	1944-05-14	Modesto,California	21
\.


--
-- Data for Name: film; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.film (id, genre, director, release_date, awards) FROM stdin;
scream	Horor	 Wes Craven	1996-12-20	\N
Star wars	science fiction	George Lucas	1995-09-20	\N
\.


--
-- PostgreSQL database dump complete
--

