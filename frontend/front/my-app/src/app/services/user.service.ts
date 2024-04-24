import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, map } from 'rxjs';
import { User } from '../models';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  BASE_URL = 'http://127.0.0.1:8000'
  constructor(private http: HttpClient) { }

  getUser(id: number) : Observable<Comment> {
    return this.http.get<Comment>(`/api/user/${id}`);
  }

}
