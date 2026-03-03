import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { AlbumService } from '../../services/album.service';
import { Album } from '../../models/album.model';
import { Photo } from '../../models/photo.model';

function carCoverUrl(make: string): string {
  return `https://cdn.imagin.studio/getimage?customer=img&make=${encodeURIComponent(make)}&paintId=color-ff0000&angle=23`;
}

interface AlbumWithCover extends Album {
  coverUrl?: string;
}

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit {
  albums: AlbumWithCover[] = [];
  loading = true;
  error = '';

  constructor(private albumService: AlbumService, private router: Router) {}

  ngOnInit(): void {
    this.albumService.getAlbums().subscribe({
      next: (data) => {
        this.albums = data.map(a => ({
          ...a,
          coverUrl: carCoverUrl(a.title)
        }));
        this.loading = false;
      },
      error: () => {
        this.error = 'Failed to load albums. Please try again.';
        this.loading = false;
      }
    });
  }

  goToDetail(id: number): void {
    this.router.navigate(['/albums', id]);
  }

  deleteAlbum(event: Event, id: number): void {
    event.stopPropagation();
    this.albumService.deleteAlbum(id).subscribe({
      next: () => {
        this.albums = this.albums.filter(a => a.id !== id);
      },
      error: () => {
        alert('Failed to delete album.');
      }
    });
  }
}
