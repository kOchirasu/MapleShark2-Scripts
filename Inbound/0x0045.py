from script_api import *

AddInt("TotalPoints") # Extra points (Rank1+Rank2)
sourceCount = AddInt("SourceCount")
for i in range(sourceCount):
    source = AddInt("Source")
    if source == 1:
        StartNode("Trophy")
    elif source == 2:
        StartNode("ChapterCompletion")
    else:
        StartNode("Unknown")

    jobRankCount = AddInt("JobRankCount")
    for j in range(jobRankCount):
        with Node("JobRank", True):
            AddShort("JobRank")
            AddInt("Points")
    EndNode(True)
