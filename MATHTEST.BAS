
CLS
RANDOMIZE TIMER
PRINT "Timed test.  Ew!"
PRINT
INPUT "Press enter to begin", a$
CLS
Correct = 0
StartTime = TIMER
FOR I = 1 TO 100
  X = INT(RND * 10)
  Y = INT(RND * 10)
  Sum = X + Y
  PRINT "<"; I; ">  ";
  PRINT Sum; "-"; X; "=";
  INPUT Answer
  IF Answer = Y THEN
    PRINT "Correct!"
    Correct = Correct + 1
  ELSE
    PRINT "No, it's"; Y
  END IF
  PRINT
NEXT I
StopTime = TIMER

PRINT "You got"; Correct; "Correct out of 100."
Seconds = StopTime - StartTime
Minutes = INT(Seconds / 60)
Seconds2 = Seconds - Minutes * 60
PRINT "It took you ";

' Make the minutes a seconds look nice
IF Minutes < 10 THEN
  PRINT USING "0#"; Minutes;
ELSE
  PRINT USING "##"; Minutes;
END IF
PRINT ":";
IF Seconds2 < 10 THEN
  PRINT USING "0#.#"; Seconds2
ELSE
  PRINT USING "##.#"; Seconds2
END IF

' Do it again, but log it this time

OPEN "mathtest.log" FOR APPEND AS #1
PRINT #1,
PRINT #1, "****************************************"
PRINT #1, DATE$; "   "; TIME$
PRINT #1, "You got"; Correct; "Correct out of 100."
PRINT #1, "It took you ";

' Make the minutes a seconds look nice
IF Minutes < 10 THEN
  PRINT #1, USING "0#"; Minutes;
ELSE
  PRINT #1, USING "##"; Minutes;
END IF
PRINT #1, ":";
IF Seconds2 < 10 THEN
  PRINT #1, USING "0#.#"; Seconds2
ELSE
  PRINT #1, USING "##.#"; Seconds2
END IF

CLOSE #1

