from script_api import *

add_int("TotalPoints") # Extra points (Rank1+Rank2)
sourceCount = add_int("SourceCount")
for i in range(sourceCount):
    source = add_int("Source")
    if source == 1:
        start_node("Trophy")
    elif source == 2:
        start_node("ChapterCompletion")
    else:
        start_node("Unknown")

    jobRankCount = add_int("JobRankCount")
    for j in range(jobRankCount):
        with Node("JobRank", True):
            add_short("JobRank")
            add_int("Points")
    end_node(True)
