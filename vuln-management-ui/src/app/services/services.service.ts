import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ServicesService {
  private apiUrl = 'http://localhost/services_service';

  constructor(private http: HttpClient) {}

  getServices(): Observable<any> {
    return this.http.get(`${this.apiUrl}/services`);
  }

  addService(service: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/services`, service);
  }

  deleteService(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/services/${id}`);
  }
}
