--
-- PostgreSQL database dump
--

-- Dumped from database version 17.3
-- Dumped by pg_dump version 17.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- Name: department; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.department (
    id_department integer NOT NULL,
    department_name character varying(255) NOT NULL,
    manual_count integer DEFAULT 0,
    id_faculty integer
);


ALTER TABLE public.department OWNER TO postgres;

--
-- Name: department_id_department_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.department_id_department_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.department_id_department_seq OWNER TO postgres;

--
-- Name: department_id_department_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.department_id_department_seq OWNED BY public.department.id_department;


--
-- Name: faculty; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.faculty (
    id_faculty integer NOT NULL,
    faculty_name character varying(255) NOT NULL,
    dean_fio character varying(255) NOT NULL,
    manual_count integer DEFAULT 0
);


ALTER TABLE public.faculty OWNER TO postgres;

--
-- Name: faculty_id_faculty_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.faculty_id_faculty_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.faculty_id_faculty_seq OWNER TO postgres;

--
-- Name: faculty_id_faculty_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.faculty_id_faculty_seq OWNED BY public.faculty.id_faculty;


--
-- Name: manual; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.manual (
    id_manual integer NOT NULL,
    manual_name character varying(255) NOT NULL,
    release_date date NOT NULL,
    id_teacher integer,
    page_count integer NOT NULL,
    status character varying(255) DEFAULT 'На проверке'::character varying,
    id_department integer,
    id_faculty integer
);


ALTER TABLE public.manual OWNER TO postgres;

--
-- Name: manual_id_manual_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.manual_id_manual_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.manual_id_manual_seq OWNER TO postgres;

--
-- Name: manual_id_manual_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.manual_id_manual_seq OWNED BY public.manual.id_manual;


--
-- Name: messages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.messages (
    id_message integer NOT NULL,
    id_sender integer,
    id_receiver integer,
    id_manual integer,
    message_text text,
    message_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    status character varying(255)
);


ALTER TABLE public.messages OWNER TO postgres;

--
-- Name: messages_id_message_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.messages_id_message_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.messages_id_message_seq OWNER TO postgres;

--
-- Name: messages_id_message_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.messages_id_message_seq OWNED BY public.messages.id_message;


--
-- Name: reviewer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reviewer (
    id_reviewer integer NOT NULL,
    reviewer_fio character varying(255) NOT NULL,
    id_manual integer
);


ALTER TABLE public.reviewer OWNER TO postgres;

--
-- Name: reviewer_id_reviewer_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reviewer_id_reviewer_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.reviewer_id_reviewer_seq OWNER TO postgres;

--
-- Name: reviewer_id_reviewer_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reviewer_id_reviewer_seq OWNED BY public.reviewer.id_reviewer;


--
-- Name: rio; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rio (
    id_worker integer NOT NULL,
    reviewer_fio character varying(255) NOT NULL,
    positions character varying(255) NOT NULL,
    manual_count integer DEFAULT 0
);


ALTER TABLE public.rio OWNER TO postgres;

--
-- Name: rio_id_worker_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.rio_id_worker_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.rio_id_worker_seq OWNER TO postgres;

--
-- Name: rio_id_worker_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.rio_id_worker_seq OWNED BY public.rio.id_worker;


--
-- Name: teacher; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teacher (
    id_teacher integer NOT NULL,
    teacher_fio character varying(255) NOT NULL,
    manual_count integer DEFAULT 0,
    academic_degree character varying(255),
    id_department integer
);


ALTER TABLE public.teacher OWNER TO postgres;

--
-- Name: teacher_id_teacher_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.teacher_id_teacher_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.teacher_id_teacher_seq OWNER TO postgres;

--
-- Name: teacher_id_teacher_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.teacher_id_teacher_seq OWNED BY public.teacher.id_teacher;


--
-- Name: department id_department; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department ALTER COLUMN id_department SET DEFAULT nextval('public.department_id_department_seq'::regclass);


--
-- Name: faculty id_faculty; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty ALTER COLUMN id_faculty SET DEFAULT nextval('public.faculty_id_faculty_seq'::regclass);


--
-- Name: manual id_manual; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manual ALTER COLUMN id_manual SET DEFAULT nextval('public.manual_id_manual_seq'::regclass);


--
-- Name: messages id_message; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.messages ALTER COLUMN id_message SET DEFAULT nextval('public.messages_id_message_seq'::regclass);


--
-- Name: reviewer id_reviewer; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reviewer ALTER COLUMN id_reviewer SET DEFAULT nextval('public.reviewer_id_reviewer_seq'::regclass);


--
-- Name: rio id_worker; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rio ALTER COLUMN id_worker SET DEFAULT nextval('public.rio_id_worker_seq'::regclass);


--
-- Name: teacher id_teacher; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher ALTER COLUMN id_teacher SET DEFAULT nextval('public.teacher_id_teacher_seq'::regclass);


--
-- Data for Name: department; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.department (id_department, department_name, manual_count, id_faculty) FROM stdin;
1	ПО	5	1
\.


--
-- Data for Name: faculty; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.faculty (id_faculty, faculty_name, dean_fio, manual_count) FROM stdin;
1	ФФиПИ	Таныгин	10
\.


--
-- Data for Name: manual; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.manual (id_manual, manual_name, release_date, id_teacher, page_count, status, id_department, id_faculty) FROM stdin;
1	Методичка по крутости	2025-04-06	1	10	Одобрено	1	1
\.


--
-- Data for Name: messages; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.messages (id_message, id_sender, id_receiver, id_manual, message_text, message_date, status) FROM stdin;
1	1	1	1	Проверьте методичку	2025-04-06 20:43:45.005195	Отправлено
\.


--
-- Data for Name: reviewer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reviewer (id_reviewer, reviewer_fio, id_manual) FROM stdin;
1	Глазов Михаил Юрьевич	1
\.


--
-- Data for Name: rio; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.rio (id_worker, reviewer_fio, positions, manual_count) FROM stdin;
1	Глазов Михаил Юрьевич	Проверяющий	2
\.


--
-- Data for Name: teacher; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.teacher (id_teacher, teacher_fio, manual_count, academic_degree, id_department) FROM stdin;
1	Петров Михаил Евгеньевич	2	Лучший в мире	1
\.


--
-- Name: department_id_department_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.department_id_department_seq', 1, true);


--
-- Name: faculty_id_faculty_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.faculty_id_faculty_seq', 1, true);


--
-- Name: manual_id_manual_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.manual_id_manual_seq', 1, true);


--
-- Name: messages_id_message_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.messages_id_message_seq', 1, true);


--
-- Name: reviewer_id_reviewer_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reviewer_id_reviewer_seq', 1, true);


--
-- Name: rio_id_worker_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.rio_id_worker_seq', 1, true);


--
-- Name: teacher_id_teacher_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.teacher_id_teacher_seq', 1, true);


--
-- Name: department department_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (id_department);


--
-- Name: faculty faculty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_pkey PRIMARY KEY (id_faculty);


--
-- Name: manual manual_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manual
    ADD CONSTRAINT manual_pkey PRIMARY KEY (id_manual);


--
-- Name: messages messages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (id_message);


--
-- Name: reviewer reviewer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reviewer
    ADD CONSTRAINT reviewer_pkey PRIMARY KEY (id_reviewer);


--
-- Name: rio rio_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rio
    ADD CONSTRAINT rio_pkey PRIMARY KEY (id_worker);


--
-- Name: teacher teacher_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT teacher_pkey PRIMARY KEY (id_teacher);


--
-- Name: department department_id_faculty_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_id_faculty_fkey FOREIGN KEY (id_faculty) REFERENCES public.faculty(id_faculty) ON DELETE CASCADE;


--
-- Name: manual manual_id_department_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manual
    ADD CONSTRAINT manual_id_department_fkey FOREIGN KEY (id_department) REFERENCES public.department(id_department) ON DELETE SET NULL;


--
-- Name: manual manual_id_faculty_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manual
    ADD CONSTRAINT manual_id_faculty_fkey FOREIGN KEY (id_faculty) REFERENCES public.faculty(id_faculty) ON DELETE SET NULL;


--
-- Name: manual manual_id_teacher_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manual
    ADD CONSTRAINT manual_id_teacher_fkey FOREIGN KEY (id_teacher) REFERENCES public.teacher(id_teacher) ON DELETE CASCADE;


--
-- Name: messages messages_id_manual_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_id_manual_fkey FOREIGN KEY (id_manual) REFERENCES public.manual(id_manual) ON DELETE CASCADE;


--
-- Name: messages messages_id_receiver_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_id_receiver_fkey FOREIGN KEY (id_receiver) REFERENCES public.teacher(id_teacher) ON DELETE SET NULL;


--
-- Name: messages messages_id_sender_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_id_sender_fkey FOREIGN KEY (id_sender) REFERENCES public.teacher(id_teacher) ON DELETE SET NULL;


--
-- Name: reviewer reviewer_id_manual_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reviewer
    ADD CONSTRAINT reviewer_id_manual_fkey FOREIGN KEY (id_manual) REFERENCES public.manual(id_manual) ON DELETE CASCADE;


--
-- Name: teacher teacher_id_department_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT teacher_id_department_fkey FOREIGN KEY (id_department) REFERENCES public.department(id_department) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

