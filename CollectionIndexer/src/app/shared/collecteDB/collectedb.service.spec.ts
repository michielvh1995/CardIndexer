import { TestBed } from '@angular/core/testing';

import { CollectedbService } from './collectedb.service';

describe('CollectedbService', () => {
  let service: CollectedbService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CollectedbService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
