import Control.Applicative
import Data.Char (digitToInt, isAlphaNum, isNumber)
import Data.Either (fromRight)
import Data.Maybe (fromJust)
import Data.List (foldl', transpose)
import qualified Data.Map.Strict as M
import Text.Parsec (Parsec, eof, runParser)
import Text.Parsec.Char (digit, string)

-- Parsing the file
-- is this a library function somewhere? couldn't find it with hoogle
splitHeader :: String -> (String, String)
splitHeader [] = error "malformed input"
splitHeader ('\n':'\n':r) = ([], r)
splitHeader (s:ss) = let (f, sn) = splitHeader ss in (s:f, sn)

-- Parsing the header
type Boxes = M.Map Int String

getDataLines :: [String] -> [String]
getDataLines = map (filter isAlphaNum) . filter (isNumber . head)

parseBoxes :: [String] -> Boxes
parseBoxes s = M.fromList (zip (map (digitToInt . head) s) (map tail s))

parseHeader :: String -> Boxes
parseHeader = parseBoxes . getDataLines . map reverse . transpose . lines

-- Parsing the instructions
data Instruction =
  Instr { amt :: Int,
          from :: Int,
          to :: Int
        }
  deriving (Show)

parseInstr :: Parsec String () Instruction
parseInstr = do
  string "move "
  n <- some digit
  string " from "
  f <- some digit
  string " to "
  t <- some digit
  eof
  pure $ Instr {amt = read n, from = read f, to = read t}

instr :: String -> Instruction
instr = fromRight undefined . runParser parseInstr () ""

-- running the crane
-- use f = reverse for part 1, f = id for part 2.
updateBoxes :: (String -> String) -> Boxes -> Instruction -> Boxes
updateBoxes f bs (Instr {amt, from, to}) = M.adjust (++ f lifted) to $ M.insert from val1' bs
  where
    val1 = bs M.! from
    (val1', lifted) = splitAt (length val1 - amt) val1

-- putting it all together
processFile :: String -> (String, String)
processFile contents = (toOutput res_part1, toOutput res_part2)
  where
    (header, body) = splitHeader contents

    initBoxes = parseHeader header
    instrs = map instr (lines body)

    res_part1 = foldl' (updateBoxes reverse) initBoxes instrs
    res_part2 = foldl' (updateBoxes id) initBoxes instrs

    toOutput = map (last . snd) . M.toAscList

main :: IO ()
main = do
  contents <- readFile "input"
  let (res1, res2) = processFile contents
  putStrLn $ "part 1: " ++ res1
  putStrLn $ "part 2: " ++ res2
