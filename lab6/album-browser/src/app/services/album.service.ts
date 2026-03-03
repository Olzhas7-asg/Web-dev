import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of, tap, map } from 'rxjs';
import { Album } from '../models/album.model';
import { Photo } from '../models/photo.model';

const CAR_BRANDS: Album[] = [
  { id: 1, userId: 1, title: 'Toyota' },
  { id: 2, userId: 1, title: 'BMW' },
  { id: 3, userId: 1, title: 'Mercedes-Benz' },
  { id: 4, userId: 1, title: 'Audi' },
  { id: 5, userId: 1, title: 'Ford' },
  { id: 6, userId: 1, title: 'Honda' },
  { id: 7, userId: 1, title: 'Volkswagen' },
  { id: 8, userId: 1, title: 'Chevrolet' },
  { id: 9, userId: 1, title: 'Nissan' },
  { id: 10, userId: 1, title: 'Hyundai' },
  { id: 11, userId: 1, title: 'Porsche' },
  { id: 12, userId: 1, title: 'Ferrari' },
  { id: 13, userId: 1, title: 'Lamborghini' },
  { id: 14, userId: 1, title: 'Tesla' },
  { id: 15, userId: 1, title: 'Jeep' },
  { id: 16, userId: 1, title: 'Subaru' },
  { id: 17, userId: 1, title: 'Mazda' },
  { id: 18, userId: 1, title: 'Kia' },
  { id: 19, userId: 1, title: 'Volvo' },
  { id: 20, userId: 1, title: 'Land Rover' },
  { id: 21, userId: 1, title: 'Jaguar' },
  { id: 22, userId: 1, title: 'Bentley' },
  { id: 23, userId: 1, title: 'Rolls-Royce' },
  { id: 24, userId: 1, title: 'Maserati' },
  { id: 25, userId: 1, title: 'Alfa Romeo' },
  { id: 26, userId: 1, title: 'Peugeot' },
  { id: 27, userId: 1, title: 'Renault' },
  { id: 28, userId: 1, title: 'Fiat' },
  { id: 29, userId: 1, title: 'Lexus' },
  { id: 30, userId: 1, title: 'Bugatti' },
];

// Car models per brand for real car photos
const CAR_MODELS: Record<number, string[]> = {
  1:  ['camry','corolla','rav4','highlander','supra'],
  2:  ['m3','x5','3-series','m8','7-series'],
  3:  ['c-class','e-class','s-class','gle','amg-gt'],
  4:  ['a4','q5','r8','tt','e-tron'],
  5:  ['mustang','f-150','explorer','bronco','gt'],
  6:  ['civic','accord','cr-v','nsx','pilot'],
  7:  ['golf','passat','tiguan','arteon','id4'],
  8:  ['camaro','corvette','tahoe','silverado','blazer'],
  9:  ['gt-r','370z','maxima','frontier','armada'],
  10: ['sonata','tucson','santa-fe','ioniq','palisade'],
  11: ['911','cayenne','panamera','taycan','macan'],
  12: ['488','sf90','roma','portofino','laferrari'],
  13: ['huracan','aventador','urus','gallardo','murcielago'],
  14: ['model-s','model-3','model-x','model-y','roadster'],
  15: ['wrangler','cherokee','gladiator','renegade','compass'],
  16: ['wrx','outback','forester','brz','crosstrek'],
  17: ['mx-5','cx-5','mazda3','rx-7','cx-9'],
  18: ['stinger','telluride','k5','ev6','sportage'],
  19: ['xc90','s60','v60','xc40','c40'],
  20: ['defender','discovery','range-rover','evoque','velar'],
  21: ['f-type','xe','xf','e-pace','f-pace'],
  22: ['continental','bentayga','flying-spur','mulsanne','bacalar'],
  23: ['phantom','ghost','wraith','dawn','cullinan'],
  24: ['ghibli','quattroporte','levante','granturismo','mc20'],
  25: ['giulia','stelvio','4c','gtv','brera'],
  26: ['308','508','3008','208','e-208'],
  27: ['megane','clio','zoe','arkana','austral'],
  28: ['500','panda','tipo','124-spider','abarth'],
  29: ['lc500','ls','rx','gx','ux'],
  30: ['chiron','veyron','divo','bolide','mistral'],
};

function carImageUrl(make: string, model: string): string {
  return `https://cdn.imagin.studio/getimage?customer=img&make=${encodeURIComponent(make)}&modelFamily=${encodeURIComponent(model)}&paintId=color-ff0000&angle=23`;
}

function coverImageUrl(make: string): string {
  const model = CAR_MODELS[CAR_BRANDS.find(b => b.title === make)?.id ?? 1]?.[0] ?? 'default';
  return carImageUrl(make, model);
}

@Injectable({
  providedIn: 'root'
})
export class AlbumService {
  private baseUrl = 'https://jsonplaceholder.typicode.com';
  private albumCache: Map<number, Album> = new Map();
  private deletedIds: Set<number> = new Set();

  constructor(private http: HttpClient) {}

  getAlbums(): Observable<Album[]> {
    return of(
      CAR_BRANDS
        .filter(a => !this.deletedIds.has(a.id))
        .map(a => this.albumCache.has(a.id) ? this.albumCache.get(a.id)! : { ...a })
    );
  }

  getAlbum(id: number): Observable<Album> {
    if (this.albumCache.has(id)) {
      return of(this.albumCache.get(id)!);
    }
    const album = CAR_BRANDS.find(a => a.id === id);
    if (album) {
      this.albumCache.set(id, { ...album });
      return of({ ...album });
    }
    return this.http.get<Album>(`${this.baseUrl}/albums/${id}`);
  }

  getAlbumPhotos(id: number): Observable<Photo[]> {
    const brand = CAR_BRANDS.find(a => a.id === id);
    const make = brand?.title ?? 'Toyota';
    const models = CAR_MODELS[id] ?? ['sedan','suv','coupe','sport','classic'];
    const photos: Photo[] = models.map((model, index) => ({
      id: index + 1,
      albumId: id,
      title: `${make} ${model.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase())}`,
      url: carImageUrl(make, model),
      thumbnailUrl: carImageUrl(make, model)
    }));
    return of(photos);
  }

  updateAlbum(album: Album): Observable<Album> {
    this.albumCache.set(album.id, { ...album });
    return of(album);
  }

  deleteAlbum(id: number): Observable<void> {
    this.deletedIds.add(id);
    this.albumCache.delete(id);
    return of(void 0);
  }
}

