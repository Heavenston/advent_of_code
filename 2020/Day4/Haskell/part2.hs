import Data.List.Extra
import Data.Function
import Data.Maybe
import System.IO
import Control.Concurrent
import Text.Read

stringIntRangeCheck string min max =
    fromMaybe False $ readMaybe string >>= (\x -> Just $ x >= min && x <= max)
hexDigits = ['0'..'9'] ++ ['a'..'f']

validateField [key, value]
  | key == "byr" = stringIntRangeCheck value 1920 2002
  | key == "iyr" = stringIntRangeCheck value 2010 2020
  | key == "eyr" = stringIntRangeCheck value 2020 2030
  | key == "hgt" = let (prefix, suffix) = splitAtEnd 2 value in
                   if suffix == "cm" then
                       stringIntRangeCheck prefix 150 193
                   else
                       suffix == "in" && stringIntRangeCheck prefix 59 76
  | key == "hcl" = head value == '#' && length value == 7 && all (`elem` hexDigits) (tail value)
  | key == "ecl" = value `elem` ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  | key == "pid" = (length value == 9) && isJust (readMaybe value :: Maybe Int)
  | key == "cid" = True
  | otherwise    = False

day4 batch requiredFields =
    -- Find list of passports              replace new lines with spaces
    let passports = splitOn "\n\n" batch & map (replace "\n" " ") in
    -- Get all fields from passports
    let textFields = map (splitOn " ") passports in
    -- Extract fields [key values] of each passports
    let fields = map (filter ((==2).length) . map (splitOn ":")) textFields in
    -- Extract field names of each passports
    let fieldNames = map (map head) fields in
    -- Extract all missing fields
    let missingFields = map (foldl (flip delete) requiredFields) fieldNames in
    -- Get invalid fields
    let invalidFields = map (map head . filter (not . validateField)) fields in

    let fieldThatHaveAProblem =
            zipWith (++) missingFields invalidFields in
    -- count who has zero missing
    length $ filter null fieldThatHaveAProblem

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day4 contents ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
