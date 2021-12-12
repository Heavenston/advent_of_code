import Data.List.Extra;
import Data.Function;
import Data.Functor.Composition;
import Data.Bifunctor
import System.IO

breakOmit s =
    second (drop $ length s) .
    breakOn s
readBinary :: String -> Int
readBinary = foldl (\acc a -> acc * 2 + (if a == '0' then 0 else 1)) 0

boardSize = 5

day4 input =
    let parts = splitOn "\n\n" input in

    let numbers = head parts in
    let numbersL = splitOn "," numbers in
    let numbersP = map (read . trim :: String -> Int) numbersL in

    let boards = tail parts in
    let boardsL = map (map trim . splitOn "\n" . dropSuffix "\n") boards in
    let boardsL2 = map (map $ splitOn " " . replace "  " " ") boardsL in
    let boardsP = map (map $ map (read :: String -> Int)) boardsL2 in

    run numbersP boardsP (map (map $ map $ const 0) boardsP)

        where
            apply a board mask = zipWith (\l ml ->
                    zipWith (\n nl -> if n == a || nl == 1 then 1 else 0) l ml
                ) board mask
            hasWon mask = any (all (==1)) mask || any (\i -> all ((==1).(!!(i-1))) mask) [1..boardSize]
            getScore board mask = sum $ zipWith (\l ml ->
                    sum $ zipWith (\n nl -> if nl == 0 then n else 0) l ml
                ) board mask

            run (n:numbers) boards masks =
                let newMasks = zipWith (apply n) boards masks in
                case find (hasWon . snd) (zip boards newMasks) of
                  Just (wBoard, wMask) -> n * getScore wBoard wMask
                  Nothing     -> run numbers boards newMasks


main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day4 $ contents
