import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VulnsService {
  private apiUrl = 'http://localhost/vulns_service';

  constructor(private http: HttpClient) {}

  getVulnerabilities(): Observable<any> {
    return this.http.get(`${this.apiUrl}/vulnerabilities`);
  }

  addVulnerability(vuln: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/vulnerabilities`, vuln);
  }

  deleteVulnerability(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/vulnerabilities/${id}`);
  }
}
