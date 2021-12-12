import Data.List.Extra
import Data.Function
import Data.Bifunctor
import Data.Maybe
import System.IO
import Control.Concurrent

instrToBin = replace "B" "1" . replace "R" "1" . replace "F" "0" . replace "L" "0"
readBinary :: String -> Int
readBinary = foldl (\acc a -> acc * 2 + (if a == '0' then 0 else 1)) 0

day5 =
    let seats = sort . map (readBinary . instrToBin) in
    let findForSeat (a:c:q) =
            if a + 2 == c then
                c - 1
            else
                findForSeat (c:q)
    in
        findForSeat . seats

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day5 $ lines contents
