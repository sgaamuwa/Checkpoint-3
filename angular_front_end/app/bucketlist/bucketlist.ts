export interface Bucketlist{
    name: string;
    date_created: string;
    date_modified: string;
    items: Item[];
    created_by: string;
}

export interface Item{
    name: string;
    date_created: string;
    date_modified: string;
    done: boolean;
}