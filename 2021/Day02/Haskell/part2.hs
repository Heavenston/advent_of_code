import Data.List.Extra;
import Data.Function;
import Data.Functor.Composition;
import Data.Bifunctor
import System.IO

day2 :: [String] -> Int
day2 =
    (\(a, b, _) -> a * b) .
    foldl (flip $ interpretInstr . second read . breakOn " ") (0, 0, 0)

    where
        interpretInstr (key, x) (hpos, depth, aim) =
            case key of
              "forward" -> (hpos + x, depth + aim * x, aim)
              "down"    -> (hpos, depth, aim + x)
              "up"      -> (hpos, depth, aim - x)

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day2 $ lines contents
