import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TargetsService {
  private apiUrl = 'http://localhost/targets_service';

  constructor(private http: HttpClient) {}

  getTargets(): Observable<any> {
    return this.http.get(`${this.apiUrl}/targets`);
  }

  addTarget(target: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/targets`, target);
  }

  deleteTarget(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/targets/${id}`);
  }
}
