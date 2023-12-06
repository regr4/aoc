import Control.Applicative (Alternative (some, (<|>)), optional)
import Control.Monad (forM_)
import Control.Monad.State.Strict
import Data.Char (digitToInt, isAlphaNum, isNumber)
import Data.Either (fromRight)
import Data.Functor (($>))
import Data.List (foldl', transpose)
import Data.Map.Strict qualified as M
import Data.Maybe (fromJust, isJust)
import Text.Parsec (Parsec, choice, eof, runParser, try)
import Text.Parsec.Char (char, digit, string)

type Constant = Int

data Register = W | X | Y | Z
  deriving (Show, Eq, Ord)

data RegOrCns
  = Reg Register
  | Cns Constant
  deriving (Eq, Show)

data Instruction
  = InputI Register
  | AddI Register RegOrCns
  | MulI Register RegOrCns
  | DivI Register RegOrCns
  | ModI Register RegOrCns
  | EqlI Register RegOrCns
  deriving (Show)

newtype Program = Prog {getInstrs :: [Instruction]}
  deriving (Show)

parseInstr :: Parsec String () Instruction
parseInstr =
  string "inp " *> (InputI <$> parseReg) <* eof
    <|> choice
      ( map
          (try . uncurry parseInstrHelper)
          [ ("add", AddI),
            ("mul", MulI),
            ("div", DivI),
            ("mod", ModI),
            ("eql", EqlI)
          ]
      )

parseInstrHelper :: String -> (Register -> RegOrCns -> Instruction) -> Parsec String () Instruction
parseInstrHelper name cons = do
  string name
  char ' '
  r1 <- parseReg
  char ' '
  r2 <- parseRegOrCns
  eof
  pure $ cons r1 r2

parseReg :: Parsec String () Register
parseReg =
  choice
    [ char 'w' $> W,
      char 'x' $> X,
      char 'y' $> Y,
      char 'z' $> Z
    ]

parseNum :: Parsec String () Int
parseNum = do
  sign <- optional (char '-')
  r <- some digit
  let r' :: Int
      r' = read r
  pure $ if isJust sign then -1 * r' else r'

parseRegOrCns :: Parsec String () RegOrCns
parseRegOrCns = (Cns <$> parseNum) <|> (Reg <$> parseReg)

parseLine :: String -> Instruction
parseLine = fromRight undefined . runParser parseInstr () ""

parseFile :: String -> Program
parseFile = Prog . map parseLine . lines

-- simplifying programs
-- you CANNOT just convert and optimise later
-- that gets too big
data Expr
  = ConstE Int
  | InpE Int
  | AddE Expr Expr
  | MulE Expr Expr
  | DivE Expr Expr
  | ModE Expr Expr
  | EqlE Expr Expr
  deriving (Show)

data SimplEnv = MkEnv
  { regs :: M.Map Register Expr,
    numInps :: Int
  }
  deriving (Show)

beginS :: SimplEnv
beginS = MkEnv {regs = M.fromList (map (second ConstE) [(W, 0), (X, 0), (Y, 0), (Z, 0)]), numInps = 0}
  where
    second f (a, b) = (a, f b)

regorcnsToExpr :: SimplEnv -> RegOrCns -> Expr
regorcnsToExpr env (Reg r) = regs env M.! r
regorcnsToExpr _ (Cns r) = ConstE r

helper :: (Expr -> Expr -> Expr) -> Register -> RegOrCns -> State SimplEnv ()
helper v a b = do
  env@MkEnv {regs, numInps} <- get
  let regs' = M.adjust (\e -> v e (regorcnsToExpr env b)) a regs
  put $ MkEnv {regs = regs', numInps}

toExprs :: Instruction -> State SimplEnv ()
toExprs (InputI b) = do
  MkEnv {regs, numInps} <- get
  let regs' = M.insert b (InpE numInps) regs
  put $ MkEnv {regs = regs', numInps = numInps + 1}
toExprs (AddI a (Cns 0)) = pure ()
toExprs (AddI a (Cns n)) = do
  MkEnv {regs, numInps} <- get
  case regs M.! a of
    ConstE a' -> put (MkEnv {regs = M.insert a (ConstE (a' + n)) regs, numInps})
    _ -> helper AddE a (Cns n)
  pure ()
toExprs (AddI a b) = helper AddE a b
toExprs (MulI a b)
  | b == Cns 0 = modify (\s -> s {regs = M.insert a (ConstE 0) (regs s)})
  | otherwise = helper MulE a b
toExprs (DivI a b) = helper DivE a b
toExprs (ModI a b) = helper ModE a b
toExprs (EqlI a b) = helper EqlE a b

{-
normalizeConsts :: Expr -> Expr
normalizeConsts (AddE (ConstE a) (ConstE b)) = ConstE (a + b)
normalizeConsts (AddE a (ConstE b)) = AddE (ConstE b) a
normalizeConsts (MulE (ConstE a) (ConstE b)) = ConstE (a * b)
normalizeConsts (MulE a (ConstE b)) = MulE (ConstE b) a
normalizeConsts (DivE (ConstE a) (ConstE b)) = ConstE (a `div` b)
normalizeConsts (DivE a (ConstE b)) = DivE (ConstE b) a
normalizeConsts (ModE (ConstE a) (ConstE b)) = ConstE (a `mod` b)
normalizeConsts (ModE a (ConstE b)) = ModE (ConstE b) a
normalizeConsts (EqlE (ConstE a) (ConstE b)) = ConstE (if a == b then 1 else 0)
normalizeConsts (EqlE a (ConstE b)) = EqlE (ConstE b) a
normalizeConsts e = e

reassociate :: Expr -> Expr
reassociate (AddE a (AddE b c)) = AddE (AddE (reassociate a) (reassociate b)) (reassociate c)
reassociate (MulE a (MulE b c)) = MulE (MulE (reassociate a) (reassociate b)) (reassociate c)
reassociate (DivE a b) = DivE (reassociate a) (reassociate b)
reassociate (ModE a b) = ModE (reassociate a) (reassociate b)
reassociate (EqlE a b) = EqlE (reassociate a) (reassociate b)
reassociate e = e

simplifyExpr :: Expr -> Expr
simplifyExpr = reassociate . normalizeConsts
-}
-- simplifyExpr :: Expr -> Expr
-- simplifyExpr e@(AddE (ConstE a) (ConstE b)) =
--   ConstE (a + b)
-- simplifyExpr e@(AddE a b) =
--   let bubbledAdd =
--         let a' = simplifyExpr a
--             b' = simplifyExpr b
--          in case b' of
--               ConstE i -> AddE (ConstE i) a
--               AddE (ConstE i) b'' -> AddE (ConstE i) (simplifyExpr (AddE a' b''))
--               _ -> AddE a' b'
--    in case bubbledAdd of
--         AddE (ConstE i) (AddE (ConstE j) a) -> AddE (ConstE (i + j)) a
--         e -> e
-- simplifyExpr e@(MulE (ConstE a) (ConstE b)) =
--   ConstE (a * b)
-- simplifyExpr e@(MulE a b) =
--   let bubbledAdd =
--         let a' = simplifyExpr a
--             b' = simplifyExpr b
--          in case b' of
--               ConstE i -> MulE (ConstE i) a
--               MulE (ConstE i) b'' -> MulE (ConstE i) (simplifyExpr (MulE a' b''))
--               _ -> MulE a' b'
--    in case bubbledAdd of
--         MulE (ConstE i) (AddE (ConstE j) a) -> AddE (ConstE (i * j)) a
--         e -> e
-- simplifyExpr e = e

simplifyExprs :: State SimplEnv ()
simplifyExprs = do
  MkEnv {regs, numInps} <- get

  pure ()

main :: IO ()
main = do
  contents <- readFile "input"
  let parsed = parseFile contents
  let res = execState (forM_ (getInstrs parsed) toExprs) beginS
  print (regs res)
  -- print $ M.map simplifyExpr $ regs res
  pure ()

-- let (res1, res2) = processFile contents
-- putStrLn $ "part 1: " ++ res1
-- putStrLn $ "part 2: " ++ res2
