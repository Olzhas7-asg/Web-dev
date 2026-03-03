# Album Browser — Lab 6: Routing & HTTP

An Angular SPA that browses albums from the JSONPlaceholder REST API. Demonstrates routing, HttpClient, Observables, and a service layer.

## Prerequisites

- Node.js 18+
- Angular CLI: `npm install -g @angular/cli`

## Getting Started

```bash
# 1. Navigate to the project
cd lab6/album-browser

# 2. Install dependencies
npm install

# 3. Start development server
ng serve
```

Open your browser at **http://localhost:4200**

## Features

| Route | Component | Description |
|---|---|---|
| `/home` | HomeComponent | Welcome page |
| `/about` | AboutComponent | App info & student details |
| `/albums` | AlbumsComponent | List all albums (with delete) |
| `/albums/:id` | AlbumDetailComponent | View & edit album title |
| `/albums/:id/photos` | AlbumPhotosComponent | Photo grid for an album |

## Project Structure

```
src/app/
├── models/
│   ├── album.model.ts       # Album interface
│   └── photo.model.ts       # Photo interface
├── services/
│   └── album.service.ts     # All HTTP calls via HttpClient
└── components/
    ├── home/
    ├── about/
    ├── albums/
    ├── album-detail/
    └── album-photos/
```

## API

Uses [JSONPlaceholder](https://jsonplaceholder.typicode.com) — a free fake REST API.  
Note: PUT/DELETE calls are simulated; changes are reflected in the UI but not persisted.
