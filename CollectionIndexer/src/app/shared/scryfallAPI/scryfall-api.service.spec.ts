import { TestBed } from '@angular/core/testing';

import { ScryfallAPIService } from './scryfall-api.service';

describe('ScryfallAPIService', () => {
  let service: ScryfallAPIService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ScryfallAPIService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
