open System

type types =
  | Int of int
  | Symbol of char
  | None

let map =
  System.IO.File.ReadAllText "input.txt"
  |> (fun v -> v.Split "\r\n")
  |> Array.map Seq.toArray
  |> Array.map (Array.map (fun v -> 
    if Char.IsDigit v then Int (int v - int '0')
    elif v = '.' then None
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

let extractNeighbors (r:int) (c:int) (len:int) = 
  if len = 0 then false
  else
    List.allPairs [r-1..r+1] [c-1..c+len]
    |> List.exists (fun (r, c) ->
        r >= 0 && r < rows && c >= 0 && c < cols && 
        (match map.[r].[c] with
        | Symbol _ -> true
        | _ -> false
      ))

let new_map = 
  map |> Array.mapi (fun r row -> row |> Array.mapi (fun c col -> 
    extractNumber r c |> (fun (num, len) -> 
      if extractNeighbors r c len then num
      else 0
    )
)) 

// sum new_map
let sum = new_map |> Array.fold (fun acc row -> Array.fold (+) acc row) 0

printfn "%A" sum
