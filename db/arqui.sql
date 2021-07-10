--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3
-- Dumped by pg_dump version 13.3

-- Started on 2021-07-09 17:26:57

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
-- TOC entry 202 (class 1259 OID 16409)
-- Name: mascota; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mascota (
    nombre character varying(50),
    edad integer,
    raza character varying(50),
    descripcion character varying(264),
    idmascota integer NOT NULL
);


ALTER TABLE public.mascota OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16510)
-- Name: Mascota_idmascota_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.mascota ALTER COLUMN idmascota ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Mascota_idmascota_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 201 (class 1259 OID 16404)
-- Name: publicacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.publicacion (
    idmascota integer,
    idusuario integer,
    fecha time without time zone,
    idpublicacion integer NOT NULL
);


ALTER TABLE public.publicacion OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 16518)
-- Name: Publicacion_idpublicacion_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.publicacion ALTER COLUMN idpublicacion ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Publicacion_idpublicacion_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 205 (class 1259 OID 16427)
-- Name: mascotapublicacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mascotapublicacion (
    idmascota integer,
    idpublicacion integer,
    idrelmp integer NOT NULL
);


ALTER TABLE public.mascotapublicacion OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 16523)
-- Name: mascota/publicacion_idrelmp_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.mascotapublicacion ALTER COLUMN idrelmp ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."mascota/publicacion_idrelmp_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 200 (class 1259 OID 16398)
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario (
    nombre character varying(50),
    apellido character varying(50),
    rut character varying(50),
    pass character varying(60),
    contacto character varying(50),
    region character varying(50),
    email character varying(50) NOT NULL,
    idusuario integer,
    tipodeusuario boolean
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16417)
-- Name: usuariomascota; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuariomascota (
    idusuario integer,
    idmascota integer,
    idrelum integer NOT NULL
);


ALTER TABLE public.usuariomascota OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16536)
-- Name: usuario/mascota_idrelum_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.usuariomascota ALTER COLUMN idrelum ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."usuario/mascota_idrelum_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 204 (class 1259 OID 16422)
-- Name: usuariopublicacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuariopublicacion (
    idusuario integer,
    idpublicacion integer,
    idrelup integer NOT NULL
);


ALTER TABLE public.usuariopublicacion OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16542)
-- Name: usuario/publicacion_idrelup_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.usuariopublicacion ALTER COLUMN idrelup ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."usuario/publicacion_idrelup_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 211 (class 1259 OID 24651)
-- Name: usuario_idusuario_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuario_idusuario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usuario_idusuario_seq OWNER TO postgres;

--
-- TOC entry 3040 (class 0 OID 0)
-- Dependencies: 211
-- Name: usuario_idusuario_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuario_idusuario_seq OWNED BY public.usuario.idusuario;


--
-- TOC entry 2880 (class 2604 OID 24653)
-- Name: usuario idusuario; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario ALTER COLUMN idusuario SET DEFAULT nextval('public.usuario_idusuario_seq'::regclass);


--
-- TOC entry 3025 (class 0 OID 16409)
-- Dependencies: 202
-- Data for Name: mascota; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.mascota (nombre, edad, raza, descripcion, idmascota) OVERRIDING SYSTEM VALUE VALUES ('mely', 24, 'raza', 'loca', 2);
INSERT INTO public.mascota (nombre, edad, raza, descripcion, idmascota) OVERRIDING SYSTEM VALUE VALUES ('econe', 36, 'hamster', 'loco', 3);
INSERT INTO public.mascota (nombre, edad, raza, descripcion, idmascota) OVERRIDING SYSTEM VALUE VALUES ('lulú', 10, 'pug', 'desordenada', 4);


--
-- TOC entry 3028 (class 0 OID 16427)
-- Dependencies: 205
-- Data for Name: mascotapublicacion; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3024 (class 0 OID 16404)
-- Dependencies: 201
-- Data for Name: publicacion; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3023 (class 0 OID 16398)
-- Dependencies: 200
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.usuario (nombre, apellido, rut, pass, contacto, region, email, idusuario, tipodeusuario) OVERRIDING SYSTEM VALUE VALUES ('HOLA', NULL, NULL, NULL, NULL, NULL, 'ssd', 2, NULL);
INSERT INTO public.usuario (nombre, apellido, rut, pass, contacto, region, email, idusuario, tipodeusuario) OVERRIDING SYSTEM VALUE VALUES ('hola', 'xd', '20063954', 'hola', 'sjdjs', 'sdksk', 'nico@gmail.com', 3, NULL);
INSERT INTO public.usuario (nombre, apellido, rut, pass, contacto, region, email, idusuario, tipodeusuario) OVERRIDING SYSTEM VALUE VALUES ('nico', 'nicolas', '12341532', '$2b$12$7mLjCOZr46Hgm45Z0Wyz3uLxhxxA8j8Kcw1Ivr7MeEEIkF.O6Ap2C', '1234321', 'fksks', 'hola@gmail.com', 4, NULL);
INSERT INTO public.usuario (nombre, apellido, rut, pass, contacto, region, email, idusuario, tipodeusuario) OVERRIDING SYSTEM VALUE VALUES ('nicolas', 'rios', '2003', '$2b$12$2UvezJQeSD3IxNQASSiDY.Ub9WhCuINPaVDA04F72i3ik0ALU0KYC', '25323452', 'metropolitana', 'nicolas@mail.cl', 5, NULL);
INSERT INTO public.usuario (nombre, apellido, rut, pass, contacto, region, email, idusuario, tipodeusuario) OVERRIDING SYSTEM VALUE VALUES ('holi@mail.cl', 'rios', '20342324', '$2b$12$2o6UPaPjMAON8w2XezSDnuZAYqbUflS/07Q.Puo9tIJm1mKEME/tW', 'dsoadas', 'metro', 'holi@mail.cl', 6, NULL);
INSERT INTO public.usuario (nombre, apellido, rut, pass, contacto, region, email, idusuario, tipodeusuario) OVERRIDING SYSTEM VALUE VALUES ('adm', '2', '4653', '$2b$12$CWXIImBH4LpUQj7na9PHQO2OLZXCDWMPInxa2FoOkPuuIeGSsHyai', 'h@mail.cl', 'metropolitana', 'admin@mail.com', 8, true);


--
-- TOC entry 3026 (class 0 OID 16417)
-- Dependencies: 203
-- Data for Name: usuariomascota; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.usuariomascota (idusuario, idmascota, idrelum) OVERRIDING SYSTEM VALUE VALUES (3, 2, 2);
INSERT INTO public.usuariomascota (idusuario, idmascota, idrelum) OVERRIDING SYSTEM VALUE VALUES (3, 3, 3);
INSERT INTO public.usuariomascota (idusuario, idmascota, idrelum) OVERRIDING SYSTEM VALUE VALUES (3, 4, 4);


--
-- TOC entry 3027 (class 0 OID 16422)
-- Dependencies: 204
-- Data for Name: usuariopublicacion; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3041 (class 0 OID 0)
-- Dependencies: 206
-- Name: Mascota_idmascota_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Mascota_idmascota_seq"', 4, true);


--
-- TOC entry 3042 (class 0 OID 0)
-- Dependencies: 207
-- Name: Publicacion_idpublicacion_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Publicacion_idpublicacion_seq"', 1, false);


--
-- TOC entry 3043 (class 0 OID 0)
-- Dependencies: 208
-- Name: mascota/publicacion_idrelmp_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."mascota/publicacion_idrelmp_seq"', 1, false);


--
-- TOC entry 3044 (class 0 OID 0)
-- Dependencies: 209
-- Name: usuario/mascota_idrelum_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."usuario/mascota_idrelum_seq"', 4, true);


--
-- TOC entry 3045 (class 0 OID 0)
-- Dependencies: 210
-- Name: usuario/publicacion_idrelup_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."usuario/publicacion_idrelup_seq"', 1, false);


--
-- TOC entry 3046 (class 0 OID 0)
-- Dependencies: 211
-- Name: usuario_idusuario_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuario_idusuario_seq', 8, true);


--
-- TOC entry 2886 (class 2606 OID 16548)
-- Name: mascota Mascota_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mascota
    ADD CONSTRAINT "Mascota_pkey" PRIMARY KEY (idmascota);


--
-- TOC entry 2884 (class 2606 OID 16550)
-- Name: publicacion Publicacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publicacion
    ADD CONSTRAINT "Publicacion_pkey" PRIMARY KEY (idpublicacion);


--
-- TOC entry 2892 (class 2606 OID 16552)
-- Name: mascotapublicacion mascota/publicacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mascotapublicacion
    ADD CONSTRAINT "mascota/publicacion_pkey" PRIMARY KEY (idrelmp);


--
-- TOC entry 2888 (class 2606 OID 16556)
-- Name: usuariomascota usuario/mascota_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuariomascota
    ADD CONSTRAINT "usuario/mascota_pkey" PRIMARY KEY (idrelum);


--
-- TOC entry 2890 (class 2606 OID 16558)
-- Name: usuariopublicacion usuario/publicacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuariopublicacion
    ADD CONSTRAINT "usuario/publicacion_pkey" PRIMARY KEY (idrelup);


--
-- TOC entry 2882 (class 2606 OID 24704)
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (email);


-- Completed on 2021-07-09 17:26:58

--
-- PostgreSQL database dump complete
--

