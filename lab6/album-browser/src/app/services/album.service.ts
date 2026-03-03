import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of, tap, map } from 'rxjs';
import { Album } from '../models/album.model';
import { Photo } from '../models/photo.model';

@Injectable({
  providedIn: 'root'
})
export class AlbumService {
  private baseUrl = 'https://jsonplaceholder.typicode.com';

  // Local cache to persist changes across navigation
  private albumCache: Map<number, Album> = new Map();
  private deletedIds: Set<number> = new Set();

  constructor(private http: HttpClient) {}

  getAlbums(): Observable<Album[]> {
    return this.http.get<Album[]>(`${this.baseUrl}/albums`).pipe(
      map(albums =>
        albums
          .filter(a => !this.deletedIds.has(a.id))
          .map(a => this.albumCache.has(a.id) ? this.albumCache.get(a.id)! : a)
      )
    );
  }

  getAlbum(id: number): Observable<Album> {
    if (this.albumCache.has(id)) {
      return of(this.albumCache.get(id)!);
    }
    return this.http.get<Album>(`${this.baseUrl}/albums/${id}`).pipe(
      tap(album => this.albumCache.set(album.id, { ...album }))
    );
  }

  getAlbumPhotos(id: number): Observable<Photo[]> {
    return this.http.get<Photo[]>(`${this.baseUrl}/albums/${id}/photos`);
  }

  updateAlbum(album: Album): Observable<Album> {
    return this.http.put<Album>(`${this.baseUrl}/albums/${album.id}`, album).pipe(
      tap(() => {
        // Save updated title locally regardless of API response
        this.albumCache.set(album.id, { ...album });
      }),
      map(() => album)
    );
  }

  deleteAlbum(id: number): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/albums/${id}`).pipe(
      tap(() => {
        this.deletedIds.add(id);
        this.albumCache.delete(id);
      })
    );
  }
}
