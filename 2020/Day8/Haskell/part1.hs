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

parseProgram :: String -> [(String, Int)]
parseProgram =
    map (
        second (read . dropPrefix "+" :: String -> Int) .
        word1
    ) .
    lines

day8 =
    start (0, 0) [] .
    parseProgram
    where
        execute ptr acc ("nop", _) =
            (ptr + 1, acc)
        execute ptr acc ("acc", x) =
            (ptr + 1, acc + x)
        execute ptr acc ("jmp", x) =
            (ptr + x, acc)

        start (ptr, acc) executed prgm =
            if ptr `elem` executed then acc else
            fromMaybe 0 (
                prgm !? ptr >>= (\x ->
                    Just $ start (execute ptr acc x) (ptr:executed) prgm
                )
            )

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day8 contents
