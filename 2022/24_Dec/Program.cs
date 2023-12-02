// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;


public class State {
    public int pos_x, pos_y;
    public int score;
    public List<Blizzard> blizzards = new List<Blizzard>();

    public State(int pos_x, int pos_y, int score, List<Blizzard> blizzards, bool update = true) {
        this.pos_x = pos_x;
        this.pos_y = pos_y;
        this.score = score;
        // copy blizzards
        foreach (Blizzard b in blizzards) {
            this.blizzards.Add(new Blizzard(b));
        }
        if (update) {
            UpdateBlizzards();
        }
    }
    public void UpdateBlizzards() {
        foreach (Blizzard b in blizzards) {
            b.Move();
        }
    }

    public bool IsDead() {
        foreach (Blizzard b in blizzards) {
            if (b.pos_x == pos_x && b.pos_y == pos_y) {
                return true;
            }
        }
        return false;
    }

} 
public class Blizzard {
    public int dir_x, dir_y;
    public int pos_x, pos_y;
    public Blizzard(char symbol, int pos_x, int pos_y) {
        this.pos_x = pos_x;
        this.pos_y = pos_y;

        switch (symbol) {
            case '^':
                dir_x = 0;
                dir_y = -1;
                break;
            case 'v':
                dir_x = 0;
                dir_y = 1;
                break;
            case '<':
                dir_x = -1;
                dir_y = 0;
                break;
            case '>':
                dir_x = 1;
                dir_y = 0;
                break;
        }
    }

    public Blizzard(Blizzard b) {
        this.dir_x = b.dir_x;
        this.dir_y = b.dir_y;
        this.pos_x = b.pos_x;
        this.pos_y = b.pos_y;
    }

    public void Move() {
        pos_x += dir_x;
        pos_y += dir_y;
        pos_x = pos_x % Program.len_x;
        pos_y = pos_y % Program.len_y;
    }

}

class Program {

    public static int len_x, len_y;
    static List<Blizzard> blizzards = new List<Blizzard>();

    static void Main(string[] args) {

        string[] lines = File.ReadAllLines("input.txt");
        len_y = lines.Length;
        len_x = lines[0].Length;
        for (int i = 0; i < len_y; i++) {
            for (int j = 0; j < len_x; j++) {
                if (lines[i][j] != '.')  {
                    blizzards.Add(new Blizzard(lines[i][j], j, i));
                }
            }
        }

        // print blizzards
        BFS();
    }

    static void BFS() {
        Queue<State> q = new Queue<State>();
        q.Enqueue(new State(0, -1, 0, blizzards, false));
        
        while (q.Count > 0) {
            State s = q.Dequeue();

            if (s.IsDead()) {
                Console.WriteLine(s.score);
                continue;
            }
            if (s.pos_x == len_x - 1 && s.pos_y == len_y) {
                Console.WriteLine(s.score);
                return;
            }
            // move
            q.Enqueue(new State(s.pos_x + 1, s.pos_y, s.score + 1, s.blizzards));
            q.Enqueue(new State(s.pos_x, s.pos_y + 1, s.score + 1, s.blizzards));
            q.Enqueue(new State(s.pos_x - 1, s.pos_y, s.score + 1, s.blizzards));
            q.Enqueue(new State(s.pos_x, s.pos_y - 1, s.score + 1, s.blizzards));
        }

    }

}