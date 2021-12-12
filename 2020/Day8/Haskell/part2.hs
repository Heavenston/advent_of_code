import Data.List.Extra
import Data.Function
import Data.Bifunctor
import Data.Maybe
import System.IO
import Control.Concurrent
import Text.Read

breakOmit s =
    second (drop $ length s) .
    breakOn s
idxMap = flip zipWith [0..]

parseProgram :: String -> [(String, Int)]
parseProgram =
    map (
        second (read . delete '+' :: String -> Int) .
        word1
    ) .
    lines

switchNopJmp "jmp" = "nop"
switchNopJmp "nop" = "jmp"

day8 =
    start (-1, 0, 0) [] .
    parseProgram
    where
        execute lstjmp ptr acc ("nop", _) =
            (lstjmp, ptr + 1, acc)
        execute lstjmp ptr acc ("acc", x) =
            (lstjmp, ptr + 1, acc + x)
        execute lstjmp ptr acc ("jmp", x) =
            (ptr, ptr + x, acc)

        start (lstjmp, ptr, acc) executed prgm =
            if ptr `elem` executed then
                start
                    (-1, lstjmp, acc) executed
                    (idxMap (\index (istr, x) -> if index == lstjmp then (switchNopJmp istr, x) else (istr, x)) prgm)
            else
                maybe (acc, prgm) (\x ->
                    start (execute lstjmp ptr acc x) (ptr:executed) prgm
                ) (prgm !? ptr)

main = do
    h <- openFile "../test.txt" ReadMode
    contents <- hGetContents h
    print $ day8 contents
