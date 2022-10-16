# Modify git commit time to non-working hours
# 
# For example work hours is 9:00 AM to 6:00 PM from Mon to Fri.

CHANGE_TIME='ture'

weekday=`date '+%A'`

if [ $weekday = "Saturday" ] || [ $weekday = "Sunday" ]; then
    CHANGE_TIME='false'
fi

GIT_COMMITTER_DATE="$(date)" git commit --amend --no-edit --date "$(date)"
echo $GIT_COMMITTER_DATE
