import Data.List
import Data.List.Split
import Data.Function
import System.IO
import Control.Concurrent

xor a b = (a || b) && not (a && b)

day2 =
    length.filter
    (\w ->
        let splits = splitOneOf " :-" w in
        let first = read (head splits) - 1 in
        let second = read (splits !! 1) - 1 in
        let char = head $ splits!!2 in
        let word = splits!!4 in

        (word!!first == char) `xor` (word!!second == char)
    )

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day2 (lines contents)
