import Data.List.Extra;
import Data.Function;
import Data.Functor.Composition;
import Data.Bifunctor
import System.IO

day2 =
    uncurry (*) .
    foldr (
        (\(key, val) (hpos, depth) -> case key of
                                          "forward" -> (hpos + val, depth)
                                          "down"    -> (hpos, depth + val)
                                          "up"      -> (hpos, depth - val)
        ) . second read . breakOn " "
    ) (0, 0)

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day2 $ lines contents
