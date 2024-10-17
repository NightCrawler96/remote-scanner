import { TestBed } from '@angular/core/testing';

import { VulnsService } from './vulns.service';

describe('VulnsService', () => {
  let service: VulnsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(VulnsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
