open System

type types =
  | Int of int
  | Symbol of char
  | Gear0
  | Gear1 of int
  | Gear2 of int
  | None

let map =
  System.IO.File.ReadAllText "input.txt"
  |> (fun v -> v.Split "\r\n")
  |> Array.map Seq.toArray
  |> Array.map (Array.map (fun v -> 
    if Char.IsDigit v then Int (int v - int '0')
    elif v = '.' then None
    elif v = '*' then Gear0
    else Symbol v
  ))

let cols = map.[0].Length
let rows = map.Length

let extractNumber (r:int) (c:int) = 
  let rec loop (r:int) (c:int) (acc:int) (len:int) = 
    if c = cols then (acc, len)
    else 
      match map.[r].[c] with
      | Int i -> loop r (c+1) (acc*10 + i) (len+1)
      | _ -> (acc, len)
  
  if c = 0 then
    loop r c 0 0
  else
    match map.[r].[c-1] with
    | Int _ -> (0, 0)
    | _     -> loop r c 0 0

let extractNeighbors (r:int) (c:int) (num:int) (len:int) = 
  if len = 0 then ()
  else
    List.allPairs [r-1..r+1] [c-1..c+len]
    |> List.iter (fun (r, c) ->
        if r >= 0 && r < rows && c >= 0 && c < cols then 
          match map.[r].[c] with
          | Gear0 -> map.[r].[c] <- Gear1 num
          | Gear1 p -> map.[r].[c] <- Gear2 (p * num)
          | Gear2 p -> map.[r].[c] <- None
          | _ -> ()
      )

map |> Array.iteri (fun r row -> row |> Array.iteri (fun c col -> 
  extractNumber r c |> (fun (num, len) -> extractNeighbors r c num len 
  )
)) 

let sum_map = 
  map |> Array.mapi (fun r row -> row |> Array.mapi (fun c col -> 
    match col with
    | Gear2 p -> p
    | _ -> 0
))
// sum new_map
let sum = sum_map |> Array.fold (fun acc row -> Array.fold (+) acc row) 0

printfn "%A" sum
