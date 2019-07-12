export interface Event {
  _id:number;
  v_id:number;
  name:string;
  summary:string;
  description:string;
  url:string;
  start_time:string;
  end_time:string;
  created_at:string;
  modified_at:string;
  published_at:string;
  status:string;
  created_by:number;
  modified_by:number;
  listed:boolean;
  shareable:boolean;
  capacity:number;
}

// Note: Did not use any fields from Expansions