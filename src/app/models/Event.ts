export interface Event {
  _id:Number;
  v_id:Number;
  name:String;
  summary:String;
  description:String;
  url:String;
  start_time:String;
  end_time:String;
  created_at:String;
  modified_at:String;
  published_at:String;
  status:String;
  created_by:Number;
  modified_by:Number;
  listed:Boolean;
  shareable:Boolean;
  capacity:Number;
}

// Note: Did not use any fields from Expansions