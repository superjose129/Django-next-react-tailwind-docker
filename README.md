# nextjs-django-docker-starter

This repo. builds a simple web app using the following technologies:
- Two front-ends for you to choose from:
  - Next.js with TypeScript and Tailwind
  - React.js (a barebones implementation)
- Django REST
- Docker (with `docker-compose`)

![Screenshot of the basic app that this repo builds](https://github.com/ntlind/nextjs-django-docker-starter/blob/main/screenshot.png?raw=true)

## Getting Started

1. Clone this repo: `git clone https://github.com/ntlind/nextjs-django-docker-starter && cd nextjs-django-docker-starter`
2. Create and modify your `.env` file: `cp .env.example .env`
3. Run docker: `docker-compose up --build`
4. Handle migrations: `./run manage migrate`
5. Navigate to pages (defaults shown below):
   1. Django REST: `http://localhost:8000/char_count/`
   2. Next.js: `http://localhost:3000/`
   3. React: `http://localhost:3001/`
6. Delete the frontend you don't want by removing it from `docker-compose.yaml` and cleaning your `.env` file.
7. Run backend tests (if desired): `./run manage test`


## Learning Resources

- [Next.js with Tailwind](https://tailwindcss.com/docs/guides/nextjs)
- [Next.js proxies (a.k.a., rewrites)](https://nextjs.org/docs/api-reference/next.config.js/rewrites)
- [TypeScript](https://www.typescriptlang.org/)
- [Creating a React.js app with Docker (not REST framework)](https://dev.to/englishcraig/creating-an-app-with-docker-compose-django-and-create-react-app-31lf)
