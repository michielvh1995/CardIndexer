export interface Card {
    internal_id: number;
    name: string;
    count: number;

    // These are the properties maintained by wizards of the coast
    multiverseid?: number;
    set? : string;
    number? : number;
    location? : string;
  }