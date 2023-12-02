
open System.IO
open System.Collections.Generic

type Blizzard = int * int * int * int // x_pos, y_pos, x_dir, y_dir
type BlizzardState = int * int * int // blizzards, time, x_pos, y_pos

let LoadBlizzards () =
    let parse y x c =
        match c with
        | '>' -> Some (x, y, 1, 0)
        | '<' -> Some (x, y, -1, 0)
        | '^' -> Some (x, y, 0, -1)
        | 'v' -> Some (x, y, 0, 1)
        | _ -> None
    // split map over each line 
    let lines = File.ReadAllLines "input.txt"
    let blizzards = (lines
        |> Seq.map Seq.toList  // convert each line to a list of chars
        |> Seq.mapi (fun y line -> Seq.mapi (fun x c -> parse y x c) line) // add x and y coordinates
        |> Seq.concat // flatten the sequence
        |> Seq.choose id // remove None values
        |> Seq.toList)

    let len_x, len_y = lines.[0].Length, lines.Length
    (blizzards, len_x, len_y)

let (blizzards, len_x, len_y) = LoadBlizzards ()

let CreateBlizzardsArray blizzards len_x len_y =
    let blizzardMap = Array2D.init len_x len_y (fun _ _ -> None)
    let InsertBlizzard b = 
        let (x, y, _, _) = b
        blizzardMap.[x, y] <- Some b
    blizzards |> List.iter InsertBlizzard
    blizzardMap

let blizzardMap = CreateBlizzardsArray blizzards len_x len_y

let modulo x m = (x % m + m) % m

let BlizzardPos (b : Blizzard) time =
    let (x, y, dx, dy) = b
    (modulo (x + dx * time) len_x, modulo (y + dy * time) len_y)

let IsDead x y time = 
    if x = 0 && y = -1 then
        false
    else
        // check if dead in constant time
        let IsCorrectBlizzard b =
            let (x, y, dx, dy) = b
            let (mx, my) = (modulo x len_x, modulo y len_y)
            // printfn "%A" (mx, my, time)
            blizzardMap.[mx, my] = Some (mx, my, dx, dy)

        [(x - time, y, 1, 0); (x + time, y, -1, 0); (x, y - time, 0, 1); (x, y + time, 0, -1)]
        |> List.exists IsCorrectBlizzard


let PrintBlizzards blizzards time =
    let blizzardMap = Array2D.init len_x len_y (fun _ _ -> '.')
    let InsertBlizzard b = 
        let (x, y) = BlizzardPos b time
        match b with
        | (_, _, 1, 0) -> blizzardMap.[x, y] <- '>'
        | (_, _, -1, 0) -> blizzardMap.[x, y] <- '<'
        | (_, _, 0, -1) -> blizzardMap.[x, y] <- '^'
        | (_, _, 0, 1) -> blizzardMap.[x, y] <- 'v'
        | _ -> ()

    blizzards |> List.iter InsertBlizzard

    for y in 0 .. len_y - 1 do
        for x in 0 .. len_x - 1 do
            printf "%c" blizzardMap.[x, y]
        printfn ""


// printfn "%A" (IsDead 2 2 blizzards 7)
// PrintBlizzards blizzards 2
// printfn "%A" (blizzardMap.[5, 0])

let lcm x y = 
    let rec gcd x y =
        if y = 0 then x else gcd y (x % y)
    (x * y) / (gcd x y)

// BFS
// define hashset for visited states
let dp = HashSet<BlizzardState>()
// Least common multiple of all len_x and len_y 
let lcm_len = lcm len_x len_y

let mutable curr_time = 0
let queue = new System.Collections.Generic.Queue<BlizzardState>()
queue.Enqueue (0, 0, -1)
while queue.Count > 0 do
    let (time, x, y) = queue.Dequeue()
    if time > curr_time then
        printfn "%A" time
        curr_time <- time

    // check if visited
    if dp.Contains (time % lcm_len, x, y) then
        ()
    else
        // check if reached end
        if x = len_x - 1 && y = len_y then
            printfn "%A" time
            queue.Clear()
        // check out of bounds
        elif (not (x = 0 && y = -1)) && (x < 0 || x >= len_x || y < 0 || y >= len_y) then
            ()
        // check if dead
        elif IsDead x y time then
            // printfn "dead: %A %A %A" time x y
            ()
        else
            dp.Add (time % lcm_len, x, y) |> ignore
            // printfn "%A %A %A" time x y
            let newTime = time + 1
            queue.Enqueue (time + 1, x, y)
            queue.Enqueue (time + 1, x + 1, y)
            queue.Enqueue (time + 1, x - 1, y)
            queue.Enqueue (time + 1, x, y + 1)
            queue.Enqueue (time + 1, x, y - 1)

