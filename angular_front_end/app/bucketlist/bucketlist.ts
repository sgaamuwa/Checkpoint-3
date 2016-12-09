export interface Bucketlist{
    id: number;
    name: string;
    date_created: string;
    date_modified: string;
    items: Item[];
    created_by: string;
}

export interface Item{
    id: number;
    name: string;
    date_created: string;
    date_modified: string;
    done: boolean;
}