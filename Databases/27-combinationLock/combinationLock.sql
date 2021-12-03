CREATE PROCEDURE combinationLock()
BEGIN
    SELECT round(exp(sum(log(char_length(characters))))) AS combinations
    FROM discs;
END
